"""
command.py — dominio Command (comandos de análisis) del subpaquete ops, sobre bridge.

Métodos alineados al comportamiento del oficial (PascalCase).
"""

from .bridge import Bridge
from ._com import acquire


class Command:
    def __init__(self, connection=None, bridge=None, filePath=None):
        staad = connection if connection is not None else acquire(filePath)
        self._b = bridge if bridge is not None else Bridge()
        self._command = staad.Command

        self._functions = [
            "PerformAnalysis",
            "PerformPDeltaAnalysisNoConverge",
            "CreateSteelDesignCommand",
            "PerformCableAnalysis",
            "PerformBucklingAnalysis",
            "SetFloorDiaphragmBaseCommand",
            "DeleteFloorDiaphragmBaseCommand",
            "SetCheckSoftStoryCommand",
            "DeleteCheckSoftStoryCommand",
            "SetCheckIrregularitiesCommand",
            "DeleteCheckIrregularitiesCommand",
            "PerformBucklingAnalysisEx",
            "PerformCableAnalysisEx",
            "PerformDirectAnalysis",
            "PerformNonlinearAnalysisEx",
            "DeleteAllAnalysisCommands",
            "PerformPDeltaAnalysisEx",
        ]
        for function_name in self._functions:
            self._command._FlagAsMethod(function_name)

    def PerformAnalysis(self, printOption: int):
        self._command.PerformAnalysis(printOption)

    def PerformPDeltaAnalysisNoConverge(self, NoOfIterations: int, PrintOption: int):
        self._command.PerformPDeltaAnalysisNoConverge(NoOfIterations, PrintOption)

    def CreateSteelDesignCommand(
        self,
        NDesignCode: int,
        NCommandNo: int,
        IntValues: list,
        FloatValues: list,
        StringValues: list,
        NAssignList: list,
    ):
        """Crea un comando de diseño en acero. Los arrays entran como SAFEARRAY crudo."""
        self._command.CreateSteelDesignCommand(
            NDesignCode,
            NCommandNo,
            self._b.in_int_array(IntValues),
            self._b.in_double_array(FloatValues),
            self._b.in_str_array(StringValues),
            self._b.in_int_array(NAssignList),
        )

    def PerformCableAnalysis(self, NoOfIterations: int, PrintOption: int):
        self._command.PerformCableAnalysis(NoOfIterations, PrintOption)

    def PerformBucklingAnalysis(self, MaxNoOfIterations: int, PrintOption: int):
        self._command.PerformBucklingAnalysis(MaxNoOfIterations, PrintOption)

    def SetFloorDiaphragmBaseCommand(self, baseElevationValue: float):
        return self._command.SetFloorDiaphragmBaseCommand(baseElevationValue)

    def DeleteFloorDiaphragmBaseCommand(self):
        return self._command.DeleteFloorDiaphragmBaseCommand()

    def SetCheckSoftStoryCommand(self, DesignCode: int):
        return self._command.SetCheckSoftStoryCommand(DesignCode)

    def DeleteCheckSoftStoryCommand(self):
        return self._command.DeleteCheckSoftStoryCommand()

    def SetCheckIrregularitiesCommand(self, DesignCode):
        return self._command.SetCheckIrregularitiesCommand(DesignCode)

    def DeleteCheckIrregularitiesCommand(self):
        return self._command.DeleteCheckIrregularitiesCommand()

    def PerformBucklingAnalysisEx(self, Method: int, MaxNoOfIterations: int, PrintOption: int):
        return self._command.PerformBucklingAnalysisEx(Method, MaxNoOfIterations, PrintOption)

    def PerformCableAnalysisEx(self, AdvancedCableAnalysis: int, AdvOptions: list, Params: list, PrintOption: int):
        """Los arrays de entrada van envueltos en VARIANT (VT_ARRAY)."""
        adv_options = self._b.in_int_array_variant(AdvOptions)
        params = self._b.in_double_array_variant(Params)
        return self._command.PerformCableAnalysisEx(
            AdvancedCableAnalysis, adv_options.ref, params.ref, PrintOption
        )

    def PerformDirectAnalysis(self, Option: int, Params: list, AddOptions: list, PrintOption: int):
        """params va antes que add_options en la llamada COM (como el oficial)."""
        add_options = self._b.in_int_array_variant(AddOptions)
        params = self._b.in_double_array_variant(Params)
        return self._command.PerformDirectAnalysis(
            Option, params.ref, add_options.ref, PrintOption
        )

    def PerformNonlinearAnalysisEx(
        self,
        PrintOption: int,
        Arclength: float,
        NoOfIterations: int,
        Tolerance: float,
        Steps: int,
        Rebuild: int,
        AddGeometricStiffness: int,
        DispLimitData: list,
    ):
        """DispLimitData entra como SAFEARRAY crudo de doubles."""
        return self._command.PerformNonlinearAnalysisEx(
            PrintOption,
            Arclength,
            NoOfIterations,
            Tolerance,
            Steps,
            int(Rebuild),
            int(AddGeometricStiffness),
            self._b.in_double_array(DispLimitData),
        )

    def DeleteAllAnalysisCommands(self):
        return self._command.DeleteAllAnalysisCommands()

    def PerformPDeltaAnalysisEx(self, NoOfIterations: int, PrintOption: int, bSmallDelta: int, AddGeometricStiffness: int):
        return self._command.PerformPDeltaAnalysisEx(NoOfIterations, PrintOption, bSmallDelta, AddGeometricStiffness)
