"""
design.py — dominio Design del subpaquete ops, sobre bridge.

Métodos alineados al comportamiento del oficial (PascalCase). Sin manejo de
errores por ahora (no se replican los `raise_os_error_if_error_code`).
"""

import comtypes.client as cc

from .bridge import Bridge
from ._com import acquire


class Design:
    def __init__(self, connection=None, bridge=None, filePath=None):
        staad = connection if connection is not None else acquire(filePath)
        self._b = bridge if bridge is not None else Bridge()
        self._design = staad.Design

        self._functions = [
            "CreateDesignBrief",
            "AssignDesignParameter",
            "AssignDesignCommand",
            "AssignDesignGroup",
            "GetDesignBriefCode",
        ]
        for function_name in self._functions:
            self._design._FlagAsMethod(function_name)

    def CreateDesignBrief(self, design_code: int) -> int:
        """Crea un design brief con el código dado; devuelve su ID de referencia."""
        return self._design.CreateDesignBrief(design_code)

    def AssignDesignParameter(
        self,
        design_ref_id: int,
        design_param: str,
        design_param_value: str,
        member_ids,
    ) -> bool:
        """Asigna un parámetro de diseño a los miembros dados. True si OK."""
        if isinstance(member_ids, int):
            member_ids = [member_ids]
        members = self._b.in_int_array_variant(member_ids)
        retVal = self._design.AssignDesignParameter(
            design_ref_id, design_param, design_param_value, members.ref
        )
        return retVal == 0

    def AssignDesignCommand(
        self,
        design_ref_id: int,
        design_command_name: str,
        design_command_value: str,
        member_ids,
    ) -> bool:
        """Asigna un comando de diseño a los miembros dados. True si OK."""
        if isinstance(member_ids, int):
            member_ids = [member_ids]
        members = self._b.in_int_array_variant(member_ids)
        retVal = self._design.AssignDesignCommand(
            design_ref_id, design_command_name, design_command_value, members.ref
        )
        return retVal == 0

    def AssignDesignGroup(
        self,
        design_ref_id: int,
        design_group_name: str,
        design_group_value: str,
        same_as_member: int,
        member_ids,
    ) -> bool:
        """Asigna miembros físicos a un grupo de diseño. True si OK."""
        if isinstance(member_ids, int):
            member_ids = [member_ids]
        members = self._b.in_int_array_variant(member_ids)
        retVal = self._design.AssignDesignGroup(
            design_ref_id,
            design_group_name,
            design_group_value,
            same_as_member,
            members.ref,
        )
        return retVal == 0

    def GetDesignBriefCode(self, design_ref_id: int) -> int:
        """Código de diseño de un design brief."""
        return self._design.GetDesignBriefCode(design_ref_id)

    def GetMemberDesignParameters(self, design_ref_id: int, member_no: int) -> dict:
        """Parámetros de diseño de un miembro en un design brief.

        Devuelve un dict con: status, count, _raw (objeto COM) y parameters
        (nombre -> [valor, unidad, descripción, default]).
        """
        design_params = cc.CreateObject("StaadPro.MembSteelDgnParams")
        status = self._design.GetMemberDesignParameters(
            design_ref_id, member_no, design_params
        )

        try:
            count = getattr(design_params, "Count")
        except Exception:
            count = None

        def _get_attr(name):
            try:
                return getattr(design_params, name)
            except Exception:
                return None

        raw_names = _get_attr("Name")
        raw_values = _get_attr("Value")
        raw_units = _get_attr("Unit")
        raw_descriptions = _get_attr("Description")
        raw_defaults = _get_attr("Default")

        def _materialize(obj):
            """Convierte una colección COM o indexador en lista Python."""
            if obj is None:
                return []
            if isinstance(obj, str):
                return [obj]
            if isinstance(obj, (list, tuple)):
                return list(obj)
            if callable(obj) and count is not None:
                result = []
                for i in range(int(count)):
                    try:
                        result.append(obj(i))
                    except Exception:
                        result.append(None)
                return result
            if hasattr(obj, "__len__") and hasattr(obj, "__getitem__"):
                try:
                    return [obj[i] for i in range(len(obj))]
                except Exception:
                    return []
            return [obj]

        names_list = _materialize(raw_names)
        values_list = _materialize(raw_values)
        units_list = _materialize(raw_units)
        descriptions_list = _materialize(raw_descriptions)
        defaults_list = _materialize(raw_defaults)

        parameters = {}
        for i, nm in enumerate(names_list):
            if nm is None:
                continue
            if isinstance(nm, str) and nm.strip() == "":
                continue
            parameters[str(nm)] = [
                values_list[i] if i < len(values_list) else None,
                units_list[i] if i < len(units_list) else None,
                descriptions_list[i] if i < len(descriptions_list) else None,
                defaults_list[i] if i < len(defaults_list) else None,
            ]

        return {
            "status": status,
            "count": count,
            "_raw": design_params,
            "parameters": parameters,
        }
