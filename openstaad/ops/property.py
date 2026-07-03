"""
property.py — dominio Property del subpaquete ops, sobre bridge.

Métodos alineados al comportamiento del oficial (PascalCase). Se omiten los
`raise_os_error_if_error_code` y los `raise OsErrorBase`. Los arrays de entrada
van envueltos en VARIANT (in_*_array_variant) según lo hace el oficial. Es el
módulo más grande del paquete.
"""

from .bridge import Bridge
from ._com import acquire


class Property:
    def __init__(self, connection=None, bridge=None, filePath=None):
        staad = connection if connection is not None else acquire(filePath)
        self._b = bridge if bridge is not None else Bridge()
        self._property = staad.Property

        self._functions = [
            "AssignBeamProperty", "AssignPlateThickness", "AssignMemberSpecToBeam",
            "AssignMaterialToPlate", "AssignMaterialToMember", "CreatePlateThicknessProperty",
            "CreateBeamPropertyFromTable", "CreateAnglePropertyFromTable",
            "CreateMemberOffsetSpec", "CreateMemberReleaseSpec", "GetMemberReleaseSpec",
            "GetPlateThickness", "GetBeamPropertyAll", "GetBeamProperty", "GetMaterialProperty",
            "GetBeamMaterialName", "GetElementMaterialName", "GetPlateMaterialName",
            "DeleteMaterial", "SetMaterialName", "RemoveMaterialFromBeam",
            "RemoveMaterialFromPlate", "CreateChannelPropertyFromTable",
            "CreateTubePropertyFromTable", "CreatePipePropertyFromTable",
            "CreatePrismaticRectangleProperty", "CreatePrismaticCircleProperty",
            "CreatePrismaticTeeProperty", "CreatePrismaticTrapezoidalProperty",
            "CreatePrismaticGeneralProperty", "CreateTaperedIProperty",
            "CreateTaperedTubeProperty", "CreateAssignProfileProperty", "AssignBetaAngle",
            "CreateMemberTrussSpec", "CreateMemberInactiveSpec", "CreateMemberTensionSpec",
            "CreateMemberCompressionSpec", "CreateMemberIgnoreStiffSpec", "CreateMemberCableSpec",
            "CreateElementPlaneStressSpec", "CreateElementIgnoreInplaneRotnSpec",
            "AssignElementSpecToPlate", "CreateMemberPartialReleaseSpec",
            "CreateElementNodeReleaseSpec", "GetCountryTableNo", "GetSectionTableNo",
            "GetBeamSectionName", "GetBeamSectionPropertyTypeNo", "GetBetaAngle",
            "GetSectionPropertyCount", "GetSectionPropertyName", "GetSectionPropertyType",
            "GetSectionPropertyCountry", "GetIsotropicMaterialCount",
            "GetIsotropicMaterialProperties", "GetOrthotropic2DMaterialCount",
            "GetOrthotropic2DMaterialProperties", "GetOrthotropic3DMaterialCount",
            "GetOrthotropic3DMaterialProperties", "GetMemberGlobalOffSet",
            "GetMemberLocalOffSet", "GetIsotropicMaterialPropertiesAssigned",
            "AddControlDependentRelation", "CreateIsotropicMaterialProperties", "CreateUPTTable",
            "RemoveUPTTable", "AddUPTPropertyWIDEFLANGE", "AddUPTPropertyCHANNEL",
            "AddUPTPropertyANGLE", "AddUPTPropertyDOUBLEANGLE", "AddUPTPropertyTEE",
            "AddUPTPropertyPIPE", "AddUPTPropertyTUBE", "AddUPTPropertyGENERAL",
            "AddUPTPropertyISECTION", "AddUPTPropertyPRISMATIC", "RemovePropertyFromUPTTable",
            "CreateMemberAttribute", "AssignMemberAttribute", "DeleteMemberAttribute",
            "GetMemberCountByAttribute", "GetMemberListByAttribute", "CreateElementAttribute",
            "AssignElementAttribute", "DeleteElementAttribute", "GetElementCountByAttribute",
            "GetElementListByAttribute", "GetAssignedAttributeCount",
            "GetAssignedAttributeByIndex", "RemoveAttribute", "GetMemberSpecCode",
            "GetPublishedProfileName", "GetSTAADProfileName", "GetSectionPropertyValues",
            "GetSectionPropertyValuesEx", "DeleteMemberReleaseSpec",
            "GetBeamSectionPropertyValuesEx", "GetSectionPropertyAssignedBeamCount",
            "GetSectionPropertyAssignedBeamList", "GetIsotropicMaterialAssignedBeamCount",
            "GetIsotropicMaterialAssignedBeamList", "CreatePropertyFromUserTable",
            "GetBeamSectionPropertyRefNo", "GetUserProvidedTableCount", "GetSectionPropertyList",
            "RemovePropertyFromBeam", "DeleteProperty", "GetUserProvidedTableList",
            "GetUserProvidedTableSectionCount", "GetUserProvidedTableSectionList",
            "GetUserProvidedTableSectionProperties", "GetPropertyUniqueID", "SetPropertyUniqueID",
            "DeleteMemberSpec", "RemoveMemberReleaseSpecFromBeam", "RemoveMemberOffsetSpecFromBeam",
            "RemoveMemberTrussSpecFromBeam", "RemoveMemberInactiveSpecFromBeam",
            "RemoveMemberTensionSpecFromBeam", "RemoveMemberIgnoreStiffSpecFromBeam",
            "GetBeamConstants", "CreateBeamPropertyFromTableEx",
            "RemoveMemberCompressionSpecFromBeam", "RemoveMemberCableSpecFromBeam",
            "RemoveElementPlaneStressSpecFromPlate", "RemoveElementIgnoreInplaneRotnSpecFromPlate",
            "RemoveElementNodeReleaseSpecFromPlate", "GetUserProvidedTableNo",
            "GetUserProvidedTableSectionType", "GetMemberReleaseSpecEx",
            "GetThicknessPropertyCount", "GetThicknessPropertyList",
            "GetThicknessPropertyAssignedPlateCount", "GetThicknessPropertyAssignedPlateList",
            "GetThicknessPropertyValues", "GetPlateSectionPropertyRefNo", "RemovePropertyFromPlate",
            "GetIsotropicMaterialAssignedPlateCount", "GetIsotropicMaterialAssignedPlateList",
            "AssignMaterialToSolid", "RemoveMaterialFromSolid", "GetSolidMaterialName",
            "GetIsotropicMaterialAssignedSolidCount", "GetIsotropicMaterialAssignedSolidList",
            "CreateIsotropicMaterialPropertiesEx", "GetIsotropicMaterialPropertiesEx",
            "GetMaterialPropertyEx", "CreateUPTTableEx", "GetShapeCode", "GetRecordForSection",
            "GetMemberAttributeCount", "GetMemberAttributeList",
            "GetUserProvidedTableSectionPropertyCount", "CreateBeamPropertyFromTableComposite",
            "CreateBeamPropertyFromTableWithCoverPlates", "AddUPTPropertyWIDEFLANGEUNEQUAL",
            "AddUPTPropertyWIDEFLANGECOMPOSITE", "CreateTeePropertyFromTable",
            "SetTypeToIsotropicMaterial", "GetTypeForIsotropicMaterial", "CreatePropertyFromUPTTable",
            "GetUptGeneralProfilePointsCount", "GetUptGeneralProfileBoundaryPoints",
            "GetUptGeneralStressLocationPoints", "GetInactiveMemberCount", "GetInactiveMemberList",
            "GetAlphaAngleForSection", "GetCentroidLocationForSection",
            "DeleteAllControlDependentRelations", "CreateWideFlangePropertyFromTable",
            "CreateIsotropicMaterialSteel", "CreateIsotropicMaterialConcrete",
            "CreateIsotropicMaterialAluminum", "CreateIsotropicMaterialTimber",
            "RemoveAllElementNodeReleaseSpec", "CreateElementOffsetSpec",
            "CreateElementLocalZOffsetSpec", "GetElementLocalOffset", "GetElementGlobalOffSet",
            "GetElementOffSetSpec", "GetCountofSectionPropertyValuesEx", "CreateMemberCableSpecEx",
            "GetElementOffsetSpecCount", "RemoveAllElementOffsetSpec",
            "UpdatePropertiesToDesignSection", "GetFireProofedBeamCount", "GetFireProofedBeamList",
            "GetFireProofDataForBeam", "GetFireProofingSpecCount", "GetFireProofingSpecDetails",
            "GetFireProofingSpecAssignedBeamCount", "GetFireProofingSpecAssignedBeamList",
            "CreateMemberFireProofingSpec", "RemoveMemberFireProofingSpecFromBeam",
            "GetBeamSectionDisplayName", "SetStandardProfileDBFolder", "GetStandardProfileDBFolder",
            "GetDefaultStandardProfileDBFolder", "IsStandardDatabaseSection",
            "GetStandardSectionDatabaseName", "GetStandardSectionTableName", "GetStandardSectionName",
            "GetMemberCountByAttributeIndex", "GetMemberListByAttributeIndex",
        ]
        for function_name in self._functions:
            self._property._FlagAsMethod(function_name)

    def _ids(self, ids):
        """Normaliza int->[int] y devuelve un ComVar de array int envuelto en VARIANT."""
        if isinstance(ids, int):
            ids = [ids]
        return self._b.in_int_array_variant(ids)

    # ---- asignaciones ----
    def AssignBeamProperty(self, beam_ids, property_id: int):
        return self._property.AssignBeamProperty(self._ids(beam_ids).ref, property_id) == 0

    def AssignPlateThickness(self, plate_ids, thickness_property_id: int):
        return self._property.AssignPlateThickness(self._ids(plate_ids).ref, thickness_property_id) == 0

    def AssignMemberSpecToBeam(self, beam_ids, spec_id: int):
        return self._property.AssignMemberSpecToBeam(self._ids(beam_ids).ref, spec_id) == 0

    def AssignMaterialToPlate(self, material_name: str, plate_ids):
        return self._property.AssignMaterialToPlate(material_name, self._ids(plate_ids).ref) == 0

    def AssignMaterialToMember(self, material_name: str, member_ids):
        return self._property.AssignMaterialToMember(material_name, self._ids(member_ids).ref)

    def AssignBetaAngle(self, beam_ids, beta_angle: float):
        return self._property.AssignBetaAngle(self._ids(beam_ids).ref, beta_angle)

    def AssignElementSpecToPlate(self, plate_ids, spec_no: int):
        return self._property.AssignElementSpecToPlate(self._ids(plate_ids).ref, spec_no)

    def AssignMaterialToSolid(self, material_name: str, solid_ids: list):
        return self._property.AssignMaterialToSolid(material_name, self._b.in_int_array_variant(solid_ids).ref)

    def RemoveMaterialFromSolid(self, solid_id_list: list):
        return self._property.RemoveMaterialFromSolid(self._b.in_int_array_variant(solid_id_list).ref)

    def RemoveMaterialFromPlate(self, plate_ids):
        return self._property.RemoveMaterialFromPlate(self._ids(plate_ids).ref)

    def RemoveMaterialFromBeam(self, beam_id: int):
        return self._property.RemoveMaterialFromBeam(beam_id) == 0

    # ---- creación de propiedades de sección ----
    def CreatePlateThicknessProperty(self, thickness_list: list):
        return self._property.CreatePlateThicknessProperty(self._b.in_double_array_variant(thickness_list).ref)

    def CreateBeamPropertyFromTable(self, country_code: int, section_name: str, type_spec: int, add_spec_1: float, add_spec_2: float):
        return self._property.CreateBeamPropertyFromTable(country_code, section_name, type_spec, add_spec_1, add_spec_2)

    def CreateAnglePropertyFromTable(self, country_code: int, section_name: str, specification_type_no: int, add_spec: float):
        return self._property.CreateAnglePropertyFromTable(country_code, section_name, specification_type_no, add_spec)

    def CreateChannelPropertyFromTable(self, country_code: int, section_name: str, spec_type: int, additional_spec_1: float):
        return self._property.CreateChannelPropertyFromTable(country_code, section_name, spec_type, additional_spec_1)

    def CreateTubePropertyFromTable(self, country_code: int, section_name: str, spec_type: int, add_spec_1: float, add_spec_2: float, add_spec_3: float):
        return self._property.CreateTubePropertyFromTable(country_code, section_name, spec_type, add_spec_1, add_spec_2, add_spec_3)

    def CreatePipePropertyFromTable(self, country_code: int, section_name: str, spec_type: int, additional_spec_1: float, additional_spec_2: float):
        return self._property.CreatePipePropertyFromTable(country_code, section_name, spec_type, additional_spec_1, additional_spec_2)

    def CreatePrismaticRectangleProperty(self, depth_along_y_axis: float, depth_along_z_axis: float):
        return self._property.CreatePrismaticRectangleProperty(depth_along_y_axis, depth_along_z_axis)

    def CreatePrismaticCircleProperty(self, circle_diameter: float):
        return self._property.CreatePrismaticCircleProperty(circle_diameter)

    def CreatePrismaticTeeProperty(self, total_section_depth: float, flange_width: float, stem_depth: float, stem_width: float):
        return self._property.CreatePrismaticTeeProperty(total_section_depth, flange_width, stem_depth, stem_width)

    def CreatePrismaticTrapezoidalProperty(self, section_depth: float, top_fiber_section_width: float, bottom_fiber_section_width: float):
        return self._property.CreatePrismaticTrapezoidalProperty(section_depth, top_fiber_section_width, bottom_fiber_section_width)

    def CreatePrismaticGeneralProperty(self, property_value_list: list):
        return self._property.CreatePrismaticGeneralProperty(self._b.in_double_array_variant(property_value_list).ref)

    def CreateTaperedIProperty(self, property_value_list: list):
        return self._property.CreateTaperedIProperty(self._b.in_double_array_variant(property_value_list).ref)

    def CreateTaperedTubeProperty(self, tube_type: int, start_member_section_depth: float, end_member_section_depth: float, section_thickness: float):
        return self._property.CreateTaperedTubeProperty(tube_type, start_member_section_depth, end_member_section_depth, section_thickness)

    def CreateAssignProfileProperty(self, profile_type: int):
        return self._property.CreateAssignProfileProperty(profile_type)

    def CreateBeamPropertyFromTableEx(self, country_code: int, section_name: str, solid_shape_type: int):
        return self._property.CreateBeamPropertyFromTableEx(country_code, section_name, solid_shape_type)

    def CreateBeamPropertyFromTableComposite(self, country_code: int, section_name: str, spec_type: int, additional_spec_list: list):
        return self._property.CreateBeamPropertyFromTableComposite(country_code, section_name, spec_type, self._b.in_double_array_variant(additional_spec_list).ref)

    def CreateBeamPropertyFromTableWithCoverPlates(self, country_code: int, section_name: str, spec_type: int, additional_spec_list: list):
        return self._property.CreateBeamPropertyFromTableWithCoverPlates(country_code, section_name, spec_type, self._b.in_double_array_variant(additional_spec_list).ref)

    def CreateTeePropertyFromTable(self, country_code: int, section_name: str, spec_type: int):
        return self._property.CreateTeePropertyFromTable(country_code, section_name, spec_type)

    def CreateWideFlangePropertyFromTable(self, country_code: int, section_name: str, spec_type, specs_list: list):
        if specs_list is None or len(specs_list) == 0:
            specs_list = [0]
        return self._property.CreateWideFlangePropertyFromTable(country_code, section_name, spec_type, self._b.in_double_array_variant(specs_list).ref)

    def CreatePropertyFromUserTable(self, section_name: str, table_no: int):
        return self._property.CreatePropertyFromUserTable(section_name, table_no)

    def CreatePropertyFromUPTTable(self, table_id: int, section_name: str):
        return self._property.CreatePropertyFromUPTTable(table_id, section_name)

    def CreateParametricSurfaceThicknessProperty(self, node_thickness_list: list):
        return self._property.CreateParametricSurfaceThicknessProperty(self._b.in_double_array_variant(node_thickness_list).ref)

    # ---- specs de miembro / elemento ----
    def CreateMemberOffsetSpec(self, offset_location: int, offset_with_respect_to: int, offset_x: float, offset_y: float, offset_z: float):
        return self._property.CreateMemberOffsetSpec(offset_location, offset_with_respect_to, offset_x, offset_y, offset_z)

    def CreateMemberReleaseSpec(self, offset_location: int, dof_values: list, spring_constant_values: list):
        dof = self._b.in_int_array_variant(dof_values)
        spring = self._b.in_double_array_variant(spring_constant_values)
        return self._property.CreateMemberReleaseSpec(offset_location, dof.ref, spring.ref)

    def CreateMemberPartialReleaseSpec(self, location: int, dof_release: list, factor: list):
        dof = self._b.in_int_array_variant(dof_release)
        fac = self._b.in_double_array_variant(factor)
        return self._property.CreateMemberPartialReleaseSpec(location, dof.ref, fac.ref)

    def CreateElementNodeReleaseSpec(self, node_id: int, dof_release: list):
        return self._property.CreateElementNodeReleaseSpec(node_id, self._b.in_int_array_variant(dof_release).ref)

    def CreateMemberTrussSpec(self):
        return self._property.CreateMemberTrussSpec()

    def CreateMemberInactiveSpec(self):
        return self._property.CreateMemberInactiveSpec()

    def CreateMemberTensionSpec(self):
        return self._property.CreateMemberTensionSpec()

    def CreateMemberCompressionSpec(self):
        return self._property.CreateMemberCompressionSpec()

    def CreateMemberIgnoreStiffSpec(self):
        return self._property.CreateMemberIgnoreStiffSpec()

    def CreateMemberCableSpec(self, tension_or_unstressed_len: int, spec_value: float):
        return self._property.CreateMemberCableSpec(tension_or_unstressed_len, spec_value)

    def CreateMemberCableSpecEx(self, tension_or_unstressed_len: int, spec_value: float, tension_end_node_indicator: int, self_weight_factor_x: float, self_weight_factor_y: float, self_weight_factor_z: float):
        return self._property.CreateMemberCableSpecEx(tension_or_unstressed_len, spec_value, tension_end_node_indicator, self_weight_factor_x, self_weight_factor_y, self_weight_factor_z)

    def CreateElementPlaneStressSpec(self):
        return self._property.CreateElementPlaneStressSpec()

    def CreateElementIgnoreInplaneRotnSpec(self):
        return self._property.CreateElementIgnoreInplaneRotnSpec()

    def CreateElementOffsetSpec(self, offset_direction: int, plate_node_index: int, x_offset: float, y_offset: float, z_offset: float):
        return self._property.CreateElementOffsetSpec(offset_direction, plate_node_index, x_offset, y_offset, z_offset)

    def CreateElementLocalZOffsetSpec(self, node1_localz_offset: float, node2_localz_offset: float, node3_localz_offset: float, node4_localz_offset: float):
        return self._property.CreateElementLocalZOffsetSpec(node1_localz_offset, node2_localz_offset, node3_localz_offset, node4_localz_offset)

    def CreateMemberFireProofingSpec(self, fire_proof_type: int, thickness_value: float, density: float):
        return self._property.CreateMemberFireProofingSpec(fire_proof_type, thickness_value, density)

    # ---- getters de sección / material (escalares y arrays) ----
    def GetMemberReleaseSpec(self, member_no: int, end: int):
        release = self._b.out_int_array(6)
        spring = self._b.out_double_array(6)
        self._property.GetMemberReleaseSpec(member_no, end, release.ref, spring.ref)
        return (release.value, spring.value)

    def GetMemberReleaseSpecEx(self, beam_id: int, release_spec_position: int):
        release = self._b.out_int_array(6)
        spring = self._b.out_double_array(6)
        mpFactor = self._b.out_double()
        mpFactorList = self._b.out_double_array(3)
        self._property.GetMemberReleaseSpecEx(beam_id, release_spec_position, release.ref, spring.ref, mpFactor.ref, mpFactorList.ref)
        return (release.value, spring.value, mpFactor.value, mpFactorList.value)

    def GetPlateThickness(self, plate_no: int):
        thickness = self._b.out_double_array(4)
        self._property.GetPlateThickness(plate_no, thickness.ref)
        return thickness.value

    def _beam_props(self, com_method, beam_id, n):
        outs = [self._b.out_double() for _ in range(n)]
        com_method(beam_id, *[o.ref for o in outs])
        return tuple(o.value for o in outs)

    def GetBeamPropertyAll(self, beam_id: int):
        return self._beam_props(self._property.GetBeamPropertyAll, beam_id, 10)

    def GetBeamProperty(self, beam_id: int):
        return self._beam_props(self._property.GetBeamProperty, beam_id, 8)

    def GetBeamConstants(self, beam_id: int):
        return self._beam_props(self._property.GetBeamConstants, beam_id, 5)

    def GetMaterialProperty(self, MaterialName: str):
        outs = [self._b.out_double() for _ in range(5)]
        self._property.GetMaterialProperty(MaterialName, *[o.ref for o in outs])
        return tuple(o.value for o in outs)

    def GetMaterialPropertyEx(self, material_name: str):
        outs = [self._b.out_double() for _ in range(10)]
        self._property.GetMaterialPropertyEx(material_name, *[o.ref for o in outs])
        return tuple(o.value for o in outs)

    def GetBeamMaterialName(self, beam_id: int):
        return self._property.GetBeamMaterialName(beam_id)

    def GetElementMaterialName(self, element_id: int):
        return self._property.GetElementMaterialName(element_id)

    def GetPlateMaterialName(self, plate_id: int):
        return self._property.GetPlateMaterialName(plate_id)

    def GetSolidMaterialName(self, solid_id: int):
        return self._property.GetSolidMaterialName(solid_id)

    def DeleteMaterial(self, material_name: str):
        return self._property.DeleteMaterial(material_name)

    def SetMaterialName(self, material_name: str):
        self._property.SetMaterialName(material_name)

    def GetCountryTableNo(self, beam_id: int):
        return self._property.GetCountryTableNo(beam_id)

    def GetSectionTableNo(self, beam_id: int):
        return self._property.GetSectionTableNo(beam_id)

    def GetBeamSectionName(self, beam_id: int):
        return self._property.GetBeamSectionName(beam_id)

    def GetBeamSectionPropertyTypeNo(self, beam_id: int):
        return self._property.GetBeamSectionPropertyTypeNo(beam_id)

    def GetBetaAngle(self, beam_id: int):
        return self._property.GetBetaAngle(beam_id)

    def GetSectionPropertyCount(self):
        return self._property.GetSectionPropertyCount()

    def GetSectionPropertyName(self, sctn_prop_id: int):
        name = self._b.out_bstr()
        self._property.GetSectionPropertyName(sctn_prop_id, name.ref)
        return name.value

    def GetSectionPropertyType(self, sec_ref_no: int):
        return self._property.GetSectionPropertyType(sec_ref_no)

    def GetSectionPropertyCountry(self, sec_ref_no: int):
        return self._property.GetSectionPropertyCountry(sec_ref_no)

    def GetSectionPropertyValues(self, prof_type: int):
        outs = [self._b.out_double() for _ in range(10)]
        self._property.GetSectionPropertyValues(prof_type, *[o.ref for o in outs])
        return tuple(o.value for o in outs)

    def GetSectionPropertyValuesEx(self, section_property_id: int):
        propType = self._b.out_int()
        propValues = self._b.out_double_array(24)
        self._property.GetSectionPropertyValuesEx(section_property_id, propType.ref, propValues.ref)
        return (propType.value, propValues.value)

    def GetBeamSectionPropertyValuesEx(self, beam_id: int):
        propType = self._b.out_int()
        properties = self._b.out_double_array(24)
        self._property.GetBeamSectionPropertyValuesEx(beam_id, propType.ref, properties.ref)
        return (propType.value, properties.value)

    def GetCountofSectionPropertyValuesEx(self):
        return self._property.GetCountofSectionPropertyValuesEx()

    # ---- materiales isotrópicos / ortotrópicos ----
    def GetIsotropicMaterialCount(self):
        return self._property.GetIsotropicMaterialCount()

    def GetIsotropicMaterialProperties(self, material_number: int):
        outs = [self._b.out_double() for _ in range(6)]
        name = self._property.GetIsotropicMaterialProperties(material_number, *[o.ref for o in outs])
        return (name, *[o.value for o in outs])

    def GetIsotropicMaterialPropertiesAssigned(self, material_no: int):
        outs = [self._b.out_double() for _ in range(6)]
        assigned = self._b.out_int()
        name = self._property.GetIsotropicMaterialPropertiesAssigned(material_no, *[o.ref for o in outs], assigned.ref)
        return (name, *[o.value for o in outs], assigned.value)

    def GetIsotropicMaterialPropertiesEx(self, material_number: int):
        outs = [self._b.out_double() for _ in range(11)]
        name = self._property.GetIsotropicMaterialPropertiesEx(material_number, *[o.ref for o in outs])
        return (name, *[o.value for o in outs])

    def GetOrthotropic2DMaterialCount(self):
        return self._property.GetOrthotropic2DMaterialCount()

    def GetOrthotropic2DMaterialProperties(self, material_no: int):
        outs = [self._b.out_double() for _ in range(6)]
        self._property.GetOrthotropic2DMaterialProperties(material_no, *[o.ref for o in outs])
        return tuple(o.value for o in outs)

    def GetOrthotropic3DMaterialCount(self):
        return self._property.GetOrthotropic3DMaterialCount()

    def GetOrthotropic3DMaterialProperties(self, material_no: int):
        outs = [self._b.out_double() for _ in range(6)]
        self._property.GetOrthotropic3DMaterialProperties(material_no, *[o.ref for o in outs])
        return tuple(o.value for o in outs)

    def CreateIsotropicMaterialProperties(self, material_name: str, elasticity_mod: float, poisson: float, shear_mod: float, density: float, coef_thermal_exp: float, damp_ratio: float):
        return self._property.CreateIsotropicMaterialProperties(material_name, elasticity_mod, poisson, shear_mod, density, coef_thermal_exp, damp_ratio)

    def CreateIsotropicMaterialPropertiesEx(self, material_name: str, elasiticity: float, poisson: float, shear_modulus: float, density: float, alpha: float, damping_ratio: float, fy: float, fu: float, ry: float, rt: float, fcu: float):
        return self._property.CreateIsotropicMaterialPropertiesEx(material_name, elasiticity, poisson, shear_modulus, density, alpha, damping_ratio, fy, fu, ry, rt, fcu)

    def CreateIsotropicMaterialSteel(self, name: str, elasticity_mod: float, poisson_ratio: float, shear_modulus: float, density: float, thermal_expansion: float, damping_ratio: float, tensile_strength: float, yield_strength: float, tensile_ratio: float, yield_ratio: float, is_physical: int):
        return self._property.CreateIsotropicMaterialSteel(name, elasticity_mod, poisson_ratio, shear_modulus, density, thermal_expansion, damping_ratio, tensile_strength, yield_strength, tensile_ratio, yield_ratio, is_physical)

    def CreateIsotropicMaterialConcrete(self, name: str, elasticity: float, poisson: float, shear_modulus: float, density: float, alpha: float, damping_ratio: float, compressive_strength: float, physical: int):
        return self._property.CreateIsotropicMaterialConcrete(name, elasticity, poisson, shear_modulus, density, alpha, damping_ratio, compressive_strength, physical)

    def CreateIsotropicMaterialAluminum(self, material_name: str, elasticity_mod: float, poisson: float, shear_mod: float, density: float, thermal_exp: float, damping_ratio: float, physical_flag: int):
        return self._property.CreateIsotropicMaterialAluminum(material_name, elasticity_mod, poisson, shear_mod, density, thermal_exp, damping_ratio, physical_flag)

    def CreateIsotropicMaterialTimber(self, material_name: str, elasticity: float, poisson: float, shear_modulus: float, density: float, thermal_expansion: float, damping_ratio: float, physical_flag: int):
        return self._property.CreateIsotropicMaterialTimber(material_name, elasticity, poisson, shear_modulus, density, thermal_expansion, damping_ratio, physical_flag)

    def SetTypeToIsotropicMaterial(self, material_name: str, material_type: int):
        return self._property.SetTypeToIsotropicMaterial(material_name, material_type)

    def GetTypeForIsotropicMaterial(self, material_name: str):
        matType = self._b.out_int()
        self._property.GetTypeForIsotropicMaterial(material_name, matType.ref)
        return matType.value

    # ---- offsets ----
    def GetMemberGlobalOffSet(self, beam_id: int, member_offset_position: int):
        outs = [self._b.out_double() for _ in range(3)]
        self._property.GetMemberGlobalOffSet(beam_id, member_offset_position, *[o.ref for o in outs])
        return tuple(o.value for o in outs)

    def GetMemberLocalOffSet(self, beam_id: int, member_offset_position: int):
        outs = [self._b.out_double() for _ in range(3)]
        self._property.GetMemberLocalOffSet(beam_id, member_offset_position, *[o.ref for o in outs])
        return tuple(o.value for o in outs)

    def GetElementLocalOffset(self, plate_id: int, plate_node_index: int):
        outs = [self._b.out_double() for _ in range(3)]
        self._property.GetElementLocalOffset(plate_id, plate_node_index, *[o.ref for o in outs])
        return tuple(o.value for o in outs)

    def GetElementGlobalOffSet(self, plate_id: int, plate_node_index: int):
        outs = [self._b.out_double() for _ in range(3)]
        self._property.GetElementGlobalOffSet(plate_id, plate_node_index, *[o.ref for o in outs])
        return tuple(o.value for o in outs)

    def GetElementOffSetSpec(self, plate_id: int, plate_node_index: int):
        direction = self._b.out_int()
        outs = [self._b.out_double() for _ in range(3)]
        self._property.GetElementOffSetSpec(plate_id, plate_node_index + 1, direction.ref, *[o.ref for o in outs])
        return (direction.value, *[o.value for o in outs])

    def GetElementOffsetSpecCount(self):
        return self._property.GetElementOffsetSpecCount()

    def RemoveAllElementOffsetSpec(self):
        return self._property.RemoveAllElementOffsetSpec()

    def RemoveAllElementNodeReleaseSpec(self):
        return self._property.RemoveAllElementNodeReleaseSpec()

    # ---- control/dependent ----
    def AddControlDependentRelation(self, control_node: int, rigid_type: int, fx: int, fy: int, fz: int, mx: int, my: int, mz: int, dependent_node_list: list):
        nodes = self._b.in_int_array_variant(dependent_node_list)
        return self._property.AddControlDependentRelation(control_node, rigid_type, fx, fy, fz, mx, my, mz, nodes.ref) == 0

    def DeleteAllControlDependentRelations(self):
        return self._property.DeleteAllControlDependentRelations() == 0

    # ---- UPT tables ----
    def CreateUPTTable(self, table_type: int):
        return self._property.CreateUPTTable(table_type)

    def CreateUPTTableEx(self, table_ref_id: int, table_type: int):
        return self._property.CreateUPTTableEx(table_ref_id, table_type)

    def RemoveUPTTable(self, table_ref_id: int):
        return self._property.RemoveUPTTable(table_ref_id)

    def AddUPTPropertyWIDEFLANGE(self, table_ref_id, stn_name, cro_sec_area, sectn_depth, web_Thickness, top_flange_width, top_flange_thickness, torsional_constant, moi_l_y, moi_l_z, shear_area_y, shear_area_z):
        return self._property.AddUPTPropertyWIDEFLANGE(table_ref_id, stn_name, cro_sec_area, sectn_depth, web_Thickness, top_flange_width, top_flange_thickness, torsional_constant, moi_l_y, moi_l_z, shear_area_y, shear_area_z) == 0

    def AddUPTPropertyCHANNEL(self, table_reference_id, stn_name, cro_sec_area, sectn_depth, web_Thickness, top_flange_width, top_flange_thickness, torsional_constant, moi_l_y, moi_l_z, c_z, shear_area_y, shear_area_z):
        return self._property.AddUPTPropertyCHANNEL(table_reference_id, stn_name, cro_sec_area, sectn_depth, web_Thickness, top_flange_width, top_flange_thickness, torsional_constant, moi_l_y, moi_l_z, c_z, shear_area_y, shear_area_z) == 0

    def AddUPTPropertyANGLE(self, table_reference_id, section_name, depth_of_angle, width_of_angle, flange_thickness, gyration_radius, shear_area_y, shear_area_z):
        return self._property.AddUPTPropertyANGLE(table_reference_id, section_name, depth_of_angle, width_of_angle, flange_thickness, gyration_radius, shear_area_y, shear_area_z) == 0

    def AddUPTPropertyDOUBLEANGLE(self, table_reference_id, section_name, depth_angle, width_angle, flanges_thickness, distance_between_two_angles, torsional_constant, moi_y, moi_z, dist_z_top_section, shear_area_y, shear_area_z):
        return self._property.AddUPTPropertyDOUBLEANGLE(table_reference_id, section_name, depth_angle, width_angle, flanges_thickness, distance_between_two_angles, torsional_constant, moi_y, moi_z, dist_z_top_section, shear_area_y, shear_area_z) == 0

    def AddUPTPropertyTEE(self, table_reference_id, section_name, cross_section_area, section_depth, top_flange_width, top_flange_thickness, web_thickness, torsional_constant, moi_y, moi_z, dist_z_top_section, shear_area_y, shear_area_z):
        return self._property.AddUPTPropertyTEE(table_reference_id, section_name, cross_section_area, section_depth, top_flange_width, top_flange_thickness, web_thickness, torsional_constant, moi_y, moi_z, dist_z_top_section, shear_area_y, shear_area_z) == 0

    def AddUPTPropertyPIPE(self, table_reference_id, section_name, out_diameter, in_diameter, shear_area_y, shear_area_z):
        return self._property.AddUPTPropertyPIPE(table_reference_id, section_name, out_diameter, in_diameter, shear_area_y, shear_area_z)

    def AddUPTPropertyTUBE(self, table_reference_id, section_name, cross_section_area, section_depth, top_flange_width, top_flange_thickness, torsional_constant, moi_y, moi_z, shear_area_y, shear_area_z):
        return self._property.AddUPTPropertyTUBE(table_reference_id, section_name, cross_section_area, section_depth, top_flange_width, top_flange_thickness, torsional_constant, moi_y, moi_z, shear_area_y, shear_area_z) == 0

    def AddUPTPropertyGENERAL(self, table_reference_id, section_name, cross_section_area, section_depth, thickness_parallel_depth, width_of_section, thickness_parallel_flange, torsional_constant, moi_y, moi_z, section_modulus_z, section_modulus_y, shear_area_y, shear_area_z, plastic_modulus_z, plastic_modulus_y, warping_constant, depth_of_web):
        return self._property.AddUPTPropertyGENERAL(table_reference_id, section_name, cross_section_area, section_depth, thickness_parallel_depth, width_of_section, thickness_parallel_flange, torsional_constant, moi_y, moi_z, section_modulus_z, section_modulus_y, shear_area_y, shear_area_z, plastic_modulus_z, plastic_modulus_y, warping_constant, depth_of_web) == 0

    def AddUPTPropertyISECTION(self, table_reference_id, section_name, depth_of_web, thickness_of_web, depth_of_web1, width_of_top_flange, thickness_of_top_flange, width_of_bottom_flange, thickness_of_bottom_flange, shear_area_y, shear_area_z, torsional_constant):
        return self._property.AddUPTPropertyISECTION(table_reference_id, section_name, depth_of_web, thickness_of_web, depth_of_web1, width_of_top_flange, thickness_of_top_flange, width_of_bottom_flange, thickness_of_bottom_flange, shear_area_y, shear_area_z, torsional_constant) == 0

    def AddUPTPropertyPRISMATIC(self, table_reference_id, section_name, cross_section_area, torsional_constant, moment_of_inertia_y, moment_of_inertia_z, shear_area_y, shear_area_z, depth_y, depth_z):
        return self._property.AddUPTPropertyPRISMATIC(table_reference_id, section_name, cross_section_area, torsional_constant, moment_of_inertia_y, moment_of_inertia_z, shear_area_y, shear_area_z, depth_y, depth_z) == 0

    def AddUPTPropertyWIDEFLANGEUNEQUAL(self, table_reference_id: int, section_name: str, profile_spec_list: list):
        return self._property.AddUPTPropertyWIDEFLANGEUNEQUAL(table_reference_id, section_name, self._b.in_double_array_variant(profile_spec_list).ref)

    def AddUPTPropertyWIDEFLANGECOMPOSITE(self, table_reference_id: int, section_name: str, profile_spec_list: list):
        return self._property.AddUPTPropertyWIDEFLANGECOMPOSITE(table_reference_id, section_name, self._b.in_double_array_variant(profile_spec_list).ref)

    def RemovePropertyFromUPTTable(self, table_reference_id: int, section_name: str):
        return self._property.RemovePropertyFromUPTTable(table_reference_id, section_name)

    def GetUserProvidedTableCount(self):
        return self._property.GetUserProvidedTableCount()

    def GetUserProvidedTableList(self):
        n = self._property.GetUserProvidedTableCount()
        tables = self._b.out_int_array(n)
        self._property.GetUserProvidedTableList(tables.ref)
        return tables.value

    def GetUserProvidedTableSectionCount(self, table_id: int):
        return self._property.GetUserProvidedTableSectionCount(table_id)

    def GetUserProvidedTableSectionList(self, table_id: int):
        n = self._property.GetUserProvidedTableSectionCount(table_id)
        sections = self._b.out_str_array(n)
        self._property.GetUserProvidedTableSectionList(table_id, sections.ref)
        return sections.value

    def GetUserProvidedTableSectionProperties(self, table_id: int, section_name: str, property_count: int = 24):
        sectionType = self._b.out_int()
        values = self._b.out_double_array(property_count)
        self._property.GetUserProvidedTableSectionProperties(table_id, section_name, sectionType.ref, values.ref)
        return (sectionType.value, values.value)

    def GetUserProvidedTableNo(self, table_index: int):
        return self._property.GetUserProvidedTableNo(table_index)

    def GetUserProvidedTableSectionType(self, table_id: int):
        sectionType = self._b.out_int()
        self._property.GetUserProvidedTableSectionType(table_id, sectionType.ref)
        return sectionType.value

    def GetUserProvidedTableSectionPropertyCount(self, upt_table_id: int, section_name: str):
        return self._property.GetUserProvidedTableSectionPropertyCount(upt_table_id, section_name)

    # ---- atributos ----
    def CreateMemberAttribute(self, attribute_name: str, str_Value: str):
        return self._property.CreateMemberAttribute(attribute_name, str_Value) == 0

    def AssignMemberAttribute(self, attribute_name: str, str_Value: str, member_list):
        return self._property.AssignMemberAttribute(attribute_name, str_Value, self._ids(member_list).ref) == 0

    def DeleteMemberAttribute(self, attribute_name: str, str_Value: str):
        return self._property.DeleteMemberAttribute(attribute_name, str_Value) == 0

    def GetMemberCountByAttribute(self, attribute_name: str, str_Value: str):
        return self._property.GetMemberCountByAttribute(attribute_name, str_Value)

    def GetMemberListByAttribute(self, attribute_name: str, str_Value: str):
        n = self._property.GetMemberCountByAttribute(attribute_name, str_Value)
        members = self._b.out_int_array(n)
        self._property.GetMemberListByAttribute(attribute_name, str_Value, members.ref)
        return members.value

    def CreateElementAttribute(self, attribute_name: str, str_value: str):
        return self._property.CreateElementAttribute(attribute_name, str_value) == 0

    def AssignElementAttribute(self, attribute_name: str, str_Value: str, element_list):
        return self._property.AssignElementAttribute(attribute_name, str_Value, self._ids(element_list).ref) == 0

    def DeleteElementAttribute(self, attribute_name: str, str_value: str):
        return self._property.DeleteElementAttribute(attribute_name, str_value) == 0

    def GetElementCountByAttribute(self, attribute_name: str, str_value: str):
        return self._property.GetElementCountByAttribute(attribute_name, str_value)

    def GetElementListByAttribute(self, attribute_name: str, str_value: str):
        n = self._property.GetElementCountByAttribute(attribute_name, str_value)
        elements = self._b.out_int_array(n)
        self._property.GetElementListByAttribute(attribute_name, str_value, elements.ref)
        return elements.value

    def GetAssignedAttributeCount(self, member_id: int):
        return self._property.GetAssignedAttributeCount(member_id)

    def GetAssignedAttributeByIndex(self, attribute_index: int):
        name = self._b.out_str()
        val = self._b.out_str()
        self._property.GetAssignedAttributeByIndex(attribute_index, name.ref, val.ref)
        return (name.value, val.value)

    def RemoveAttribute(self, attribute_name: str, str_value: str, member_ids):
        return self._property.RemoveAttribute(attribute_name, str_value, self._ids(member_ids).ref) == 0

    def GetMemberAttributeCount(self):
        return self._property.GetMemberAttributeCount()

    def GetMemberAttributeList(self):
        n = self._property.GetMemberAttributeCount()
        names = self._b.out_str_array(n)
        values = self._b.out_str_array(n)
        count = self._property.GetMemberAttributeList(names.ref, values.ref)
        return (names.value, values.value, count)

    def GetMemberCountByAttributeIndex(self, index: int):
        return self._property.GetMemberCountByAttributeIndex(index)

    def GetMemberListByAttributeIndex(self, index: int):
        n = self.GetMemberCountByAttributeIndex(index)
        members = self._b.out_int_array(n)
        self._property.GetMemberListByAttributeIndex(index, members.ref)
        return members.value

    # ---- spec code / perfiles ----
    def GetMemberSpecCode(self, member_id: int):
        specCode = self._b.out_int()
        self._property.GetMemberSpecCode(member_id, specCode.ref)
        return specCode.value

    def GetPublishedProfileName(self, staad_profile_name: str, country_code: int):
        return self._property.GetPublishedProfileName(staad_profile_name, country_code)

    def GetSTAADProfileName(self, published_name: str, country_code: int):
        return self._property.GetSTAADProfileName(published_name, country_code)

    def GetShapeCode(self, country_code: int, section_name: str):
        return self._property.GetShapeCode(country_code, section_name)

    def GetRecordForSection(self, country_code: int, section_name: str):
        return self._property.GetRecordForSection(country_code, section_name)

    def GetBeamSectionDisplayName(self, beam_id: int):
        return self._property.GetBeamSectionDisplayName(beam_id)

    # ---- listas asignadas ----
    def GetSectionPropertyAssignedBeamCount(self, prof_type: int):
        return self._property.GetSectionPropertyAssignedBeamCount(prof_type)

    def GetSectionPropertyAssignedBeamList(self, prof_type: int):
        n = self._property.GetSectionPropertyAssignedBeamCount(prof_type)
        beams = self._b.out_int_array(n)
        self._property.GetSectionPropertyAssignedBeamList(prof_type, beams.ref)
        return beams.value

    def GetIsotropicMaterialAssignedBeamCount(self, material_name):
        return self._property.GetIsotropicMaterialAssignedBeamCount(material_name)

    def GetIsotropicMaterialAssignedBeamList(self, material_name: str):
        n = self._property.GetIsotropicMaterialAssignedBeamCount(material_name)
        beams = self._b.out_int_array(n)
        self._property.GetIsotropicMaterialAssignedBeamList(material_name, beams.ref)
        return beams.value

    def GetIsotropicMaterialAssignedPlateCount(self, material_name):
        return self._property.GetIsotropicMaterialAssignedPlateCount(material_name)

    def GetIsotropicMaterialAssignedPlateList(self, material_name: str):
        n = self._property.GetIsotropicMaterialAssignedPlateCount(material_name)
        plates = self._b.out_int_array(n)
        self._property.GetIsotropicMaterialAssignedPlateList(material_name, plates.ref)
        return plates.value

    def GetIsotropicMaterialAssignedSolidCount(self, material_name: str):
        return self._property.GetIsotropicMaterialAssignedSolidCount(material_name)

    def GetIsotropicMaterialAssignedSolidList(self, material_name: str):
        n = self._property.GetIsotropicMaterialAssignedSolidCount(material_name)
        solids = self._b.out_int_array(n)
        self._property.GetIsotropicMaterialAssignedSolidList(material_name, solids.ref)
        return solids.value

    def GetBeamSectionPropertyRefNo(self, beam_id: int):
        return self._property.GetBeamSectionPropertyRefNo(beam_id)

    def GetSectionPropertyList(self):
        n = self._property.GetSectionPropertyCount()
        props = self._b.out_int_array(n)
        self._property.GetSectionPropertyList(props.ref)
        return props.value

    def RemovePropertyFromBeam(self, beam_id: int):
        return self._property.RemovePropertyFromBeam(beam_id) == 0

    def DeleteProperty(self, property_id: int):
        return self._property.DeleteProperty(property_id)

    def GetPropertyUniqueID(self, property_unique_id: int):
        return self._property.GetPropertyUniqueID(property_unique_id)

    def SetPropertyUniqueID(self, property_number: int, property_unique_id: str):
        self._property.SetPropertyUniqueID(property_number, property_unique_id)

    # ---- remove specs ----
    def DeleteMemberReleaseSpec(self, beam_id: int, release_location: int):
        return self._property.DeleteMemberReleaseSpec(beam_id, release_location)

    def DeleteMemberSpec(self, spec_id: int):
        return self._property.DeleteMemberSpec(spec_id)

    def RemoveMemberReleaseSpecFromBeam(self, beam_id: int, release_location: int):
        return self._property.RemoveMemberReleaseSpecFromBeam(beam_id, release_location)

    def RemoveMemberOffsetSpecFromBeam(self, beam_id: int, release_location: int):
        return self._property.RemoveMemberOffsetSpecFromBeam(beam_id, release_location)

    def RemoveMemberTrussSpecFromBeam(self, beam_id: int):
        return self._property.RemoveMemberTrussSpecFromBeam(beam_id) == 0

    def RemoveMemberInactiveSpecFromBeam(self, beam_id: int):
        return self._property.RemoveMemberInactiveSpecFromBeam(beam_id) == 0

    def RemoveMemberTensionSpecFromBeam(self, beam_id: int):
        return self._property.RemoveMemberTensionSpecFromBeam(beam_id) == 0

    def RemoveMemberIgnoreStiffSpecFromBeam(self, beam_id: int):
        return self._property.RemoveMemberIgnoreStiffSpecFromBeam(beam_id) == 0

    def RemoveMemberCompressionSpecFromBeam(self, beam_id: int):
        return self._property.RemoveMemberCompressionSpecFromBeam(beam_id) == 0

    def RemoveMemberCableSpecFromBeam(self, beam_id: int, tension_or_length: int):
        return self._property.RemoveMemberCableSpecFromBeam(beam_id, tension_or_length)

    def RemoveElementPlaneStressSpecFromPlate(self, plate_id: int):
        return self._property.RemoveElementPlaneStressSpecFromPlate(plate_id) == 0

    def RemoveElementIgnoreInplaneRotnSpecFromPlate(self, plate_id: int):
        return self._property.RemoveElementIgnoreInplaneRotnSpecFromPlate(plate_id) == 0

    def RemoveElementNodeReleaseSpecFromPlate(self, plate_id: int, node_id: int):
        return self._property.RemoveElementNodeReleaseSpecFromPlate(plate_id, node_id) == 0

    def RemoveMemberFireProofingSpecFromBeam(self, beam_id: int):
        return self._property.RemoveMemberFireProofingSpecFromBeam(beam_id)

    # ---- thickness ----
    def GetThicknessPropertyCount(self):
        return self._property.GetThicknessPropertyCount()

    def GetThicknessPropertyList(self):
        n = self._property.GetThicknessPropertyCount()
        props = self._b.out_int_array(n)
        self._property.GetThicknessPropertyList(props.ref)
        return props.value

    def GetThicknessPropertyAssignedPlateCount(self, property_reference_id: int):
        return self._property.GetThicknessPropertyAssignedPlateCount(property_reference_id)

    def GetThicknessPropertyAssignedPlateList(self, property_reference_id: int):
        n = self._property.GetThicknessPropertyAssignedPlateCount(property_reference_id)
        plates = self._b.out_int_array(n)
        self._property.GetThicknessPropertyAssignedPlateList(property_reference_id, plates.ref)
        return plates.value

    def GetThicknessPropertyValues(self, property_reference_id: int):
        thk = self._b.out_double_array(4)
        self._property.GetThicknessPropertyValues(property_reference_id, thk.ref)
        return thk.value

    def GetPlateSectionPropertyRefNo(self, PlateNo: int):
        return self._property.GetPlateSectionPropertyRefNo(PlateNo)

    def RemovePropertyFromPlate(self, plate_id: int):
        return self._property.RemovePropertyFromPlate(plate_id)

    # ---- UPT general profile / sección ----
    def GetUptGeneralProfilePointsCount(self, table_reference_id: int, section_name: str):
        outer = self._b.out_int()
        inner = self._b.out_int()
        self._property.GetUptGeneralProfilePointsCount(table_reference_id, section_name, outer.ref, inner.ref)
        return (outer.value, inner.value)

    def GetUptGeneralProfileBoundaryPoints(self, table_number_id: int, section_name: str, is_inner: bool):
        outer, _inner = self.GetUptGeneralProfilePointsCount(table_number_id, section_name)
        zp = self._b.out_double_array(int(outer))
        yp = self._b.out_double_array(int(outer))
        self._property.GetUptGeneralProfileBoundaryPoints(table_number_id, section_name, is_inner, zp.ref, yp.ref)
        return (zp.value, yp.value)

    def GetUptGeneralStressLocationPoints(self, table_reference_id: int, section_name: str):
        zp = self._b.out_double_array(4)
        yp = self._b.out_double_array(4)
        self._property.GetUptGeneralStressLocationPoints(table_reference_id, section_name, zp.ref, yp.ref)
        return (zp.value, yp.value)

    # ---- inactive / alpha / centroid ----
    def GetInactiveMemberCount(self):
        return self._property.GetInactiveMemberCount()

    def GetInactiveMemberList(self):
        n = self._property.GetInactiveMemberCount()
        members = self._b.out_int_array(n)
        self._property.GetInactiveMemberList(members.ref)
        return members.value

    def GetAlphaAngleForSection(self, spec_property_id: int):
        alpha = self._b.out_double()
        self._property.GetAlphaAngleForSection(spec_property_id, alpha.ref)
        return float(alpha.value)

    def GetCentroidLocationForSection(self, property_id: int):
        cey = self._b.out_double()
        cez = self._b.out_double()
        self._property.GetCentroidLocationForSection(property_id, cey.ref, cez.ref)
        return (cey.value, cez.value)

    # ---- fireproofing ----
    def GetFireProofedBeamCount(self):
        return self._property.GetFireProofedBeamCount()

    def GetFireProofedBeamList(self):
        n = self._property.GetFireProofedBeamCount()
        beams = self._b.out_int_array(n)
        self._property.GetFireProofedBeamList(beams.ref)
        return beams.value

    def GetFireProofDataForBeam(self, beam_id: int):
        ftype = self._b.out_int()
        thickness = self._b.out_double()
        density = self._b.out_double()
        self._property.GetFireProofDataForBeam(beam_id, ftype.ref, thickness.ref, density.ref)
        return (ftype.value, thickness.value, density.value)

    def GetFireProofingSpecCount(self):
        return self._property.GetFireProofingSpecCount()

    def GetFireProofingSpecDetails(self, index: int):
        ftype = self._b.out_int()
        thickness = self._b.out_double()
        density = self._b.out_double()
        assignCount = self._b.out_int()
        self._property.GetFireProofingSpecDetails(index, ftype.ref, thickness.ref, density.ref, assignCount.ref)
        return (ftype.value, thickness.value, density.value, assignCount.value)

    def GetFireProofingSpecAssignedBeamCount(self, index: int):
        return self._property.GetFireProofingSpecAssignedBeamCount(index)

    def GetFireProofingSpecAssignedBeamList(self, index: int):
        n = self._property.GetFireProofingSpecAssignedBeamCount(index)
        beams = self._b.out_int_array(n)
        self._property.GetFireProofingSpecAssignedBeamList(index, beams.ref)
        return beams.value

    # ---- standard profile DB ----
    def UpdatePropertiesToDesignSection(self):
        return self._property.UpdatePropertiesToDesignSection()

    def SetStandardProfileDBFolder(self, folder_name: str):
        return self._property.SetStandardProfileDBFolder(folder_name) == 0

    def GetStandardProfileDBFolder(self):
        return self._property.GetStandardProfileDBFolder()

    def GetDefaultStandardProfileDBFolder(self):
        return self._property.GetDefaultStandardProfileDBFolder()

    def IsStandardDatabaseSection(self, section_reference_id: int):
        return self._property.IsStandardDatabaseSection(section_reference_id)

    def GetStandardSectionDatabaseName(self, section_property_id: int):
        return self._property.GetStandardSectionDatabaseName(section_property_id)

    def GetStandardSectionTableName(self, section_reference_id: int):
        return self._property.GetStandardSectionTableName(section_reference_id)

    def GetStandardSectionName(self, section_reference_id: int):
        return self._property.GetStandardSectionName(section_reference_id)
