"""
root.py — dominio Root del subpaquete ops, sobre bridge.

Métodos alineados al comportamiento del oficial (PascalCase). Conexión inyectable:
la Session le pasa una conexión + bridge compartidos; sin ellos, funciona standalone.
"""

from typing import Optional
from .bridge import Bridge
from ._com import acquire


class Root:
    def __init__(self, connection=None, bridge=None, filePath: Optional[str] = None):
        # Conexión inyectada (Session) o standalone (abre la suya).
        self._root = connection if connection is not None else acquire(filePath)
        self._b = bridge if bridge is not None else Bridge()

        self._functions = [
            "Analyze",
            "AnalyzeEx",
            "AnalyzeModel",
            "GetAnalysisStatus",
            "GetAnalysisErrorMessages",
            "GetAnalysisWarningMessages",
            "GetApplicationVersion",
            "GetBaseUnit",
            "GetInputUnitForForce",
            "GetInputUnitForLength",
            "SetInputUnitForForce",
            "SetInputUnitForLength",
            "SetInputUnits",
            "GetSTAADFile",
            "GetSTAADFileFolder",
            "NewSTAADFile",
            "OpenSTAADFile",
            "CloseSTAADFile",
            "SaveModel",
            "GetShortJobInfo",
            "SetShortJobInfo",
            "GetFullJobInfo",
            "SetFullJobInfo",
            "GetErrorMessage",
            "GetMainWindowHandle",
            "GetProcessHandle",
            "GetProcessId",
            "IsAnalyzing",
            "IsPhysicalModel",
            "SetSilentMode",
            "ShowApplication",
            "UpdateStructure",
            "Quit",
        ]
        for function_name in self._functions:
            self._root._FlagAsMethod(function_name)

    def __getattr__(self, name):
        return getattr(self._root, name)

    # ------------------------------------------------------------------ #
    # Análisis
    # ------------------------------------------------------------------ #
    def Analyze(self):
        self._root.Analyze()

    def AnalyzeModel(self):
        self._root.AnalyzeModel()

    def AnalyzeEx(self, silentMode: int, hiddenMode: int, waitTillComplete: int):
        """Analiza el .STD con modos silent/hidden y espera opcional.

        Los tres enteros (0/1) van crudos, como el oficial.
        """
        return self._root.AnalyzeEx(silentMode, hiddenMode, waitTillComplete)

    def IsAnalyzing(self) -> bool:
        """True si hay un análisis en curso."""
        return bool(self._root.IsAnalyzing())

    def GetAnalysisStatus(self, modelPath: Optional[str] = None) -> dict:
        """Estado del análisis del modelo (por defecto, el abierto)."""
        if modelPath is None:
            modelPath = self.GetSTAADFile(bFullPath=True)

        warnings = self._b.out_int()
        errors = self._b.out_int()
        cpu = self._b.out_double()

        retval = self._root.GetAnalysisStatus(modelPath, warnings.ref, errors.ref, cpu.ref)

        status = {
            -2: "Invalid model path",
            -1: "Analysis Terminated",
            0: "General Error",
            1: "Analysis is in progress",
            2: "Analysis completed without errors or warnings",
            3: "Analysis completed with warnings but without errors",
            4: "Analysis completed with errors",
            5: "Analysis has not been performed",
        }

        return {
            "ReturnValue": retval,
            "ReturnString": status[retval],
            "NoOfWarnings": warnings.value,
            "NoOfErrors": errors.value,
            "CPUTime": int(cpu.value),
        }

    def GetAnalysisErrorMessages(self, modelPath: Optional[str] = None) -> list:
        """Mensajes de error del análisis (array de strings, VT_ARRAY|VT_BSTR)."""
        if modelPath is None:
            modelPath = self.GetSTAADFile(bFullPath=True)

        n = self.GetAnalysisStatus(modelPath)["NoOfErrors"]
        if n == 0:
            return []

        messages = self._b.out_str_array(n)
        self._root.GetAnalysisErrorMessages(modelPath, messages.ref)
        return messages.value

    def GetAnalysisWarningMessages(self, modelPath: Optional[str] = None) -> list:
        """Mensajes de advertencia del análisis (array de strings)."""
        if modelPath is None:
            modelPath = self.GetSTAADFile(bFullPath=True)

        n = self.GetAnalysisStatus(modelPath)["NoOfWarnings"]
        if n == 0:
            return []

        messages = self._b.out_str_array(n)
        self._root.GetAnalysisWarningMessages(modelPath, messages.ref)
        return messages.value

    # ------------------------------------------------------------------ #
    # Info de aplicación / unidades (getters)
    # ------------------------------------------------------------------ #
    def GetApplicationVersion(self) -> str:
        """Versión de la aplicación como 'MajorA.MajorB.Minor.Build'."""
        a = self._b.out_int()
        b = self._b.out_int()
        minor = self._b.out_int()
        build = self._b.out_int()

        self._root.GetApplicationVersion(a.ref, b.ref, minor.ref, build.ref)

        return f"{a.value}.{b.value}.{minor.value}.{build.value}"

    def GetBaseUnit(self) -> str:
        """'English' o 'Metric' (viene como valor de retorno, sin out-param)."""
        retVal = self._root.GetBaseUnit()
        return {1: "English", 2: "Metric"}[retVal]

    def GetInputUnitForForce(self) -> str:
        """Unidad de fuerza de entrada del .STD abierto.

        El oficial la lee como string (VT_BSTR): 'kip', 'kN', etc.
        """
        output = {
            "kip": "Kilopound",
            "lb": "Pound",
            "kg": "Kilogram",
            "mton": "Metric Ton",
            "N": "Newton",
            "kN": "KiloNewton",
            "mN": "MegaNewton",
            "dN": "DecaNewton",
        }
        u = self._b.out_str()
        self._root.GetInputUnitForForce(u.ref)
        return output[u.value]

    def GetInputUnitForLength(self) -> str:
        """Unidad de longitud de entrada del .STD abierto.

        El oficial la lee como string (VT_BSTR): 'in', 'm', 'mm', etc.
        """
        output = {
            "in": "Inch",
            "ft": "Feet",
            "cm": "CentiMeter",
            "m": "Meter",
            "mm": "MilliMeter",
            "dm": "DeciMeter",
            "km": "KiloMeter",
        }
        u = self._b.out_str()
        self._root.GetInputUnitForLength(u.ref)
        return output[u.value]

    # ------------------------------------------------------------------ #
    # Unidades (setters) — entradas envueltas en VARIANT (in_int), como el oficial
    # ------------------------------------------------------------------ #
    def SetInputUnitForForce(self, forceUnit: int):
        if not (0 <= forceUnit <= 7):
            return
        self._root.SetInputUnitForForce(self._b.in_int(forceUnit))

    def SetInputUnitForLength(self, lengthUnit: int):
        if not (0 <= lengthUnit <= 7):
            return
        self._root.SetInputUnitForLength(self._b.in_int(lengthUnit))

    def SetInputUnits(self, lengthUnit: int, forceUnit: int):
        if not (0 <= forceUnit <= 7) or not (0 <= lengthUnit <= 7):
            return
        self._root.SetInputUnits(self._b.in_int(lengthUnit), self._b.in_int(forceUnit))

    # ------------------------------------------------------------------ #
    # Archivo
    # ------------------------------------------------------------------ #
    def GetSTAADFile(self, bFullPath: bool = True) -> str:
        """Ruta (o nombre) del .STD actual. bFullPath va crudo."""
        f = self._b.out_str()
        self._root.GetSTAADFile(f.ref, bFullPath)
        return f.value

    def GetSTAADFileFolder(self) -> str:
        """Carpeta del .STD actual."""
        folder = self._b.out_str()
        self._root.GetSTAADFileFolder(folder.ref)
        return folder.value

    def NewSTAADFile(self, fileName: str, lengthUnit: int, forceUnit: int):
        """Crea un .STD con las unidades de longitud y fuerza dadas (0..7).

        Entradas envueltas como el oficial: fileName -> in_value, unidades -> in_int.
        El llamador provee la ruta/nombre completo (el oficial no crea carpetas).
        """
        if not (0 <= forceUnit <= 7):
            return
        if not (0 <= lengthUnit <= 7):
            return
        self._root.NewSTAADFile(
            self._b.in_value(fileName),
            self._b.in_int(lengthUnit),
            self._b.in_int(forceUnit),
        )

    def OpenSTAADFile(self, file: str):
        """Abre un .STD. La ruta entra envuelta (in_value), como el oficial."""
        self._root.OpenSTAADFile(self._b.in_value(file))

    def CloseSTAADFile(self):
        self._root.CloseSTAADFile()

    def SaveModel(self, saveSilent: bool = False):
        """Guarda el modelo; saveSilent -> int(saveSilent), como el oficial."""
        self._root.SaveModel(int(saveSilent))

    # ------------------------------------------------------------------ #
    # Job info
    # ------------------------------------------------------------------ #
    def GetShortJobInfo(self) -> tuple:
        """(nombre, id, estado) del trabajo, como strings."""
        name = self._b.out_str()
        job_id = self._b.out_str()
        status = self._b.out_str()
        self._root.GetShortJobInfo(name.ref, job_id.ref, status.ref)
        return name.value, job_id.value, status.value

    def SetShortJobInfo(self, job_name: str, job_id: str, job_status: str):
        """Entradas envueltas (in_value), como el oficial."""
        self._root.SetShortJobInfo(
            self._b.in_value(job_name),
            self._b.in_value(job_id),
            self._b.in_value(job_status),
        )

    def GetFullJobInfo(self) -> list:
        """Los 13 campos del job info como lista de strings."""
        fields = [self._b.out_str() for _ in range(13)]
        self._root.GetFullJobInfo(*[f.ref for f in fields])
        return [f.value for f in fields]

    def SetFullJobInfo(
        self,
        job_name: str,
        job_client: str = "",
        eng_name: str = "",
        eng_date: str = "",
        job_number: str = "",
        revision: str = "",
        part_name: str = "",
        reference: str = "",
        checker_name: str = "",
        checker_date: str = "",
        approver_name: str = "",
        approval_date: str = "",
        comments: str = "",
    ):
        """Los 13 campos del job info; cada uno entra envuelto (in_value)."""
        args = [
            job_name, job_client, eng_name, eng_date, job_number, revision,
            part_name, reference, checker_name, checker_date, approver_name,
            approval_date, comments,
        ]
        self._root.SetFullJobInfo(*[self._b.in_value(a) for a in args])

    # ------------------------------------------------------------------ #
    # Aplicación / proceso / estructura
    # ------------------------------------------------------------------ #
    def SetSilentMode(self, silent: bool):
        """Activa/desactiva el modo silencioso."""
        self._root.SetSilentMode(int(silent))

    def ShowApplication(self):
        """Trae la aplicación STAAD.Pro al frente."""
        self._root.ShowApplication()

    def UpdateStructure(self):
        """Actualiza la estructura en la aplicación."""
        self._root.UpdateStructure()

    def IsPhysicalModel(self) -> bool:
        """True si el modelo es físico."""
        return bool(self._root.IsPhysicalModel())

    def GetMainWindowHandle(self):
        """Handle de la ventana principal."""
        return self._root.GetMainWindowHandle()

    def GetProcessHandle(self):
        """Handle del proceso STAAD.Pro."""
        return self._root.GetProcessHandle()

    def GetProcessId(self):
        """PID del proceso STAAD.Pro."""
        return self._root.GetProcessId()

    def GetErrorMessage(self) -> str:
        """Último mensaje de error lanzado por OpenSTAAD (licencia, vista, etc.)."""
        return self._root.GetErrorMessage()

    def Quit(self):
        """Cierra la aplicación STAAD.Pro."""
        self._root.Quit()
