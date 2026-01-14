from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Properties():
    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._property = self._staad.Property

        self._functions= [
            'GetAlphaAngleForSection',
            'GetBeamConstants',
            'GetBeamMaterialName',
            'GetBeamProperty',
            'GetBeamPropertyAll',
            'GetBeamSectionDisplayName',
            'GetBeamSectionName',
            'GetBeamSectionPropertyRefNo',
            'GetBeamSectionPropertyTypeNo',
            'GetBetaAngle',
            'GetCountofSectionPropertyValuesEx',
            'GetCountryTableNo',
            'GetElementGlobalOffset',
            'GetElementLocalOffset',
            'GetElementMaterialName',
            'GetElementOffsetSpec', #NOT WORKING - IT MAKES STAAD TO CRASH
            'GetIsotropicMaterialAssignedBeamCount',
            'GetIsotropicMaterialAssignedBeamList',
            'GetIsotropicMaterialCount',
            'GetIsotropicMaterialProperties',
            'GetIsotropicMaterialPropertiesAssigned',
            'GetMaterialProperty',
            'GetMemberGlobalOffSet',
            'GetMemberLocalOffSet',
            'GetMemberReleaseSpecEx',
            'GetMemberSpecCode',
            'GetPlateMaterialName',
            'GetPublishedProfileName',
            'GetSectionPropertyAssignedBeamCount',
            'GetSectionPropertyAssignedBeamList',
            'GetSectionPropertyCount',
            'GetSectionPropertyCountry',
            'GetSectionPropertyName',
            'GetSectionPropertyType',
            'GetSectionPropertyValues',
            'GetSectionPropertyValuesEx', #ONGOING
            'GetSectionTableNo', #NOT WORKING - ONLY RETURNS 0 OR 1
            'GetSTAADProfileName'
        ]

        for function_name in self._functions:
            self._property._FlagAsMethod(function_name)

    def GetAlphaAngleForSection(self,ref_no:int):
        """
        Returns the alpha angle of the section in radian.
        Gets the angle between the principal axis and geometric axis of the section

        Parameters:
        [in]	ref_no	The specified reference property ID.
        [out]	dAlpha	alpha angle returned (in Radian).
        """
                
        angle = ctypes.c_double()
        
        result = self._property.GetAlphaAngleForSection(ref_no, ctypes.byref(angle))
        
        # Extraer el valor del parámetro de salida
        angle_value = angle.value
        
        return angle_value
    
    def GetBeamConstants(self,beam:int):
        """
        Get material constants by specified beam number ID.
        """

        safe_n1 = make_safe_array_double(1)
        n1 = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        safe_n2 = make_safe_array_double(1)
        n2 = make_variant_vt_ref(safe_n2,  automation.VT_R8)

        safe_n3 = make_safe_array_double(1)
        n3 = make_variant_vt_ref(safe_n3,  automation.VT_R8)

        safe_n4 = make_safe_array_double(1)
        n4 = make_variant_vt_ref(safe_n4,  automation.VT_R8)

        safe_n5 = make_safe_array_double(1)
        n5 = make_variant_vt_ref(safe_n5,  automation.VT_R8)

        ret_val = self._property.GetBeamConstants(beam,n1,n2,n3,n4,n5)

        return {'Constants_found':ret_val,
                'Elastic_Modulus': round(n1.value[0], 3),
                'Poisson': round(n2.value[0], 3),
                'Density': round(n3.value[0], 3),
                'Thermal_Coeff': round(n4.value[0], 5),
                'Damping_Ratio': round(n5.value[0], 3),
                }

    def GetBeamMaterialName(self,beam:int):
        """
        Get beam material string name.
        """
        return self._property.GetBeamMaterialName(beam)
    
    def GetBeamProperty(self,beam:int):
        """
        Retrieve short member properties of the specified beam member.
        """

        safe_n1 = make_safe_array_double(1)
        n1 = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        safe_n2 = make_safe_array_double(1)
        n2 = make_variant_vt_ref(safe_n2,  automation.VT_R8)

        safe_n3 = make_safe_array_double(1)
        n3 = make_variant_vt_ref(safe_n3,  automation.VT_R8)

        safe_n4 = make_safe_array_double(1)
        n4 = make_variant_vt_ref(safe_n4,  automation.VT_R8)

        safe_n5 = make_safe_array_double(1)
        n5 = make_variant_vt_ref(safe_n5,  automation.VT_R8)

        safe_n6 = make_safe_array_double(1)
        n6 = make_variant_vt_ref(safe_n6,  automation.VT_R8)

        safe_n7 = make_safe_array_double(1)
        n7 = make_variant_vt_ref(safe_n7,  automation.VT_R8)

        safe_n8 = make_safe_array_double(1)
        n8 = make_variant_vt_ref(safe_n8,  automation.VT_R8)

        ret_val = self._property.GetBeamProperty(beam,n1,n2,n3,n4,n5,n6,n7,n8)

        return {'Value':ret_val,
                'Width': round(n1.value[0], 3),
                'Depth': round(n2.value[0], 3),
                'Ax': round(n3.value[0], 6),
                'Ay': round(n4.value[0], 6),
                'Az': round(n5.value[0], 6),
                'Ix': round(n6.value[0], 6),
                'Iy': round(n7.value[0], 6),
                'Iz': round(n8.value[0], 6),
                }

    def GetBeamPropertyAll(self,beam:int):
        """
        Retrieve long member properties of the specified beam member.
        """

        safe_n1 = make_safe_array_double(1)
        n1 = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        safe_n2 = make_safe_array_double(1)
        n2 = make_variant_vt_ref(safe_n2,  automation.VT_R8)

        safe_n3 = make_safe_array_double(1)
        n3 = make_variant_vt_ref(safe_n3,  automation.VT_R8)

        safe_n4 = make_safe_array_double(1)
        n4 = make_variant_vt_ref(safe_n4,  automation.VT_R8)

        safe_n5 = make_safe_array_double(1)
        n5 = make_variant_vt_ref(safe_n5,  automation.VT_R8)

        safe_n6 = make_safe_array_double(1)
        n6 = make_variant_vt_ref(safe_n6,  automation.VT_R8)

        safe_n7 = make_safe_array_double(1)
        n7 = make_variant_vt_ref(safe_n7,  automation.VT_R8)

        safe_n8 = make_safe_array_double(1)
        n8 = make_variant_vt_ref(safe_n8,  automation.VT_R8)

        safe_n9 = make_safe_array_double(1)
        n9 = make_variant_vt_ref(safe_n9,  automation.VT_R8)

        safe_n10 = make_safe_array_double(1)
        n10 = make_variant_vt_ref(safe_n10,  automation.VT_R8)

        ret_val = self._property.GetBeamPropertyAll(beam,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)

        return {'Value':ret_val,
                'Width': round(n1.value[0], 3),
                'Depth': round(n2.value[0], 3),
                'Ax': round(n3.value[0], 6),
                'Ay': round(n4.value[0], 6),
                'Az': round(n5.value[0], 6),
                'Ix': round(n6.value[0], 6),
                'Iy': round(n7.value[0], 6),
                'Iz': round(n8.value[0], 6),
                'Tf': round(n9.value[0], 6),
                'Tw': round(n10.value[0], 6),
                }

    def GetBeamSectionDisplayName(self,beam:int):
        """
        This function returns the display section name of the specified beam.
        """
        return self._property.GetBeamSectionDisplayName(beam)


    def GetBeamSectionName(self,beam:int):
        """
        Gets the section name of a given beam.
        """
        return self._property.GetBeamSectionName(beam)

    def GetBeamSectionPropertyRefNo(self,beam:int):
        """
        Gets the section property reference number for a given beam.
        """
        return self._property.GetBeamSectionPropertyRefNo(beam)
    
    def GetBeamSectionPropertyTypeNo(self,beam:int):
        """
        Gets the section property type number of the specified beam.
        """
        return self._property.GetBeamSectionPropertyTypeNo(beam)
    
    def GetBetaAngle(self,beam:int):
        """
        Retrieve beta angle of the specified beam member.
        """
        return self._property.GetBetaAngle(beam)
    
    def GetCountofSectionPropertyValuesEx(self):
        """
        Returns the total count of Section Property values.
        """
        return self._property.GetCountofSectionPropertyValuesEx()
    
    def GetCountryTableNo(self,beam:int):
        """
        Get The country CODE. for the specified member.
        """
        return self._property.GetCountryTableNo(beam)
    
    def GetElementGlobalOffset(self,plate_no:int,plate_node_index:int):
        """
        Get element offsets in all three local directions.
        """
        
        safe_n1 = make_safe_array_double(1)
        n1 = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        safe_n2 = make_safe_array_double(1)
        n2 = make_variant_vt_ref(safe_n2,  automation.VT_R8)

        safe_n3 = make_safe_array_double(1)
        n3 = make_variant_vt_ref(safe_n3,  automation.VT_R8)

        ret_val = self._property.GetElementGlobalOffset(plate_no,plate_node_index,n1,n2,n3)

        return {'Found_Offset':ret_val,
        'Offset_X': round(n1.value[0], 3),
        'Offset_Y': round(n2.value[0], 3),
        'Offset_Z': round(n3.value[0], 3),
        }
    
    def GetElementLocalOffset(self,plate_no:int,plate_node_index:int):
        """
        Get element offsets in all three local directions.
        """
        
        safe_n1 = make_safe_array_double(1)
        n1 = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        safe_n2 = make_safe_array_double(1)
        n2 = make_variant_vt_ref(safe_n2,  automation.VT_R8)

        safe_n3 = make_safe_array_double(1)
        n3 = make_variant_vt_ref(safe_n3,  automation.VT_R8)

        ret_val = self._property.GetElementLocalOffset(plate_no,plate_node_index,n1,n2,n3)

        return {'Found_Offset':ret_val,
        'Offset_X': round(n1.value[0], 3),
        'Offset_Y': round(n2.value[0], 3),
        'Offset_Z': round(n3.value[0], 3),
        }

    def GetElementMaterialName(self,element:int):
        """
        Get entity material string name.
        """
        return self._property.GetElementMaterialName(element)
    
    #NOT WORKING - IT MAKES STAAD TO CRASH
    def GetElementOffsetSpec(self,plate_no:int,plate_node_index:int):
        """
        Get element offsets in all three local directions.
        """
        
        safe_n1 = make_safe_array_double(1)
        n1 = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        safe_n2 = make_safe_array_double(1)
        n2 = make_variant_vt_ref(safe_n2,  automation.VT_R8)

        safe_n3 = make_safe_array_double(1)
        n3 = make_variant_vt_ref(safe_n3,  automation.VT_R8)

        offset_code = ctypes.c_long()

        ret_val = self._property.GetElementOffsetSpec(plate_no,plate_node_index,ctypes.byref(offset_code),n1,n2,n3)

        return {'Found_Offset':ret_val,
        'Direction': offset_code.value,
        'Offset_X': round(n1.value[0], 3),
        'Offset_Y': round(n2.value[0], 3),
        'Offset_Z': round(n3.value[0], 3),
        }

    def GetIsotropicMaterialAssignedBeamCount(self,material:str):
        """
        Get isotropic material assigned beam count.
        """     
        result = self._property.GetIsotropicMaterialAssignedBeamCount(material)
        
        return result
    
    def GetIsotropicMaterialAssignedBeamList(self,material:str):
        """
        Get isotropic material assigned beam list.
        """

        beams = self._property.GetIsotropicMaterialAssignedBeamCount(material)
        safe_list = make_safe_array_long(beams)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._property.GetIsotropicMaterialAssignedBeamList(material, lista)

        return (lista[0])
    
    def GetIsotropicMaterialCount(self):
        """
        Get the number of isotropic material present in the current structure.
        """     
        result = self._property.GetIsotropicMaterialCount()
        
        return result

    def GetIsotropicMaterialProperties(self,material_index:int):
        """
        Get the properties for the specified isotropic material number.
        """

        safe_n1 = make_safe_array_double(1)
        n1 = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        safe_n2 = make_safe_array_double(1)
        n2 = make_variant_vt_ref(safe_n2,  automation.VT_R8)

        safe_n3 = make_safe_array_double(1)
        n3 = make_variant_vt_ref(safe_n3,  automation.VT_R8)

        safe_n4 = make_safe_array_double(1)
        n4 = make_variant_vt_ref(safe_n4,  automation.VT_R8)

        safe_n5 = make_safe_array_double(1)
        n5 = make_variant_vt_ref(safe_n5,  automation.VT_R8)

        safe_n6 = make_safe_array_double(1)
        n6 = make_variant_vt_ref(safe_n6,  automation.VT_R8)

        ret_val = self._property.GetIsotropicMaterialProperties(material_index,n1,n2,n3,n4,n5,n6)

        return {'Material':material_index,
                'Elastic_Modulus': round(n1.value[0], 3),
                'Poisson': round(n2.value[0], 3),
                'Shear_Modulus': round(n3.value[0], 3),
                'Density': round(n4.value[0], 3),
                'Thermal_Coeff': round(n5.value[0], 3),
                'Damping_Ratio': round(n6.value[0], 3),
                'string_name': ret_val}

    def GetIsotropicMaterialPropertiesAssigned(self,material_index:int):

        """
        Gets isotropic material properties and if material assigned to element(s) or not.
        """

        safe_n1 = make_safe_array_double(1)
        n1 = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        safe_n2 = make_safe_array_double(1)
        n2 = make_variant_vt_ref(safe_n2,  automation.VT_R8)

        safe_n3 = make_safe_array_double(1)
        n3 = make_variant_vt_ref(safe_n3,  automation.VT_R8)

        safe_n4 = make_safe_array_double(1)
        n4 = make_variant_vt_ref(safe_n4,  automation.VT_R8)

        safe_n5 = make_safe_array_double(1)
        n5 = make_variant_vt_ref(safe_n5,  automation.VT_R8)

        safe_n6 = make_safe_array_double(1)
        n6 = make_variant_vt_ref(safe_n6,  automation.VT_R8)

        safe_n7 = make_safe_array_long(1)
        n7 = make_variant_vt_ref(safe_n7, automation.VT_I4)

        ret_val = self._property.GetIsotropicMaterialPropertiesAssigned(material_index,n1,n2,n3,n4,n5,n6,n7)

        if n7.value[0] == 1:
            assigned = True
        else:
            assigned = False

        return {'Material':material_index,
                'Elastic_Modulus': round(n1.value[0], 3),
                'Poisson': round(n2.value[0], 3),
                'Shear_Modulus': round(n3.value[0], 3),
                'Density': round(n4.value[0], 3),
                'Thermal_Coeff': round(n5.value[0], 3),
                'Damping_Ratio': round(n6.value[0], 3),
                'Is_Assigned': assigned
                }

    def GetMaterialProperty(self,material:int):
        """
        Get material constants based on specific material name.
        """

        safe_n1 = make_safe_array_double(1)
        n1 = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        safe_n2 = make_safe_array_double(1)
        n2 = make_variant_vt_ref(safe_n2,  automation.VT_R8)

        safe_n3 = make_safe_array_double(1)
        n3 = make_variant_vt_ref(safe_n3,  automation.VT_R8)

        safe_n4 = make_safe_array_double(1)
        n4 = make_variant_vt_ref(safe_n4,  automation.VT_R8)

        safe_n5 = make_safe_array_double(1)
        n5 = make_variant_vt_ref(safe_n5,  automation.VT_R8)

        ret_val = self._property.GetMaterialProperty(material,n1,n2,n3,n4,n5)

        return {'Material':material,
                'Elastic_Modulus': round(n1.value[0], 3),
                'Poisson': round(n2.value[0], 3),
                'Density': round(n3.value[0], 3),
                'Thermal_Coeff': round(n4.value[0], 3),
                'Damping_Ratio': round(n5.value[0], 3),
                }

    def GetMemberGlobalOffSet(self, beam:int, start = 1):
        """
        Get beam end offsets in all three global directions.
        """
        if start:
            end = 0
        else:
            end = 1

        safe_n1 = make_safe_array_double(1)
        n1 = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        safe_n2 = make_safe_array_double(1)
        n2 = make_variant_vt_ref(safe_n2,  automation.VT_R8)

        safe_n3 = make_safe_array_double(1)
        n3 = make_variant_vt_ref(safe_n3,  automation.VT_R8)

        retval = self._property.GetMemberGlobalOffSet(beam,end,n1,n2,n3)

        return { 'Has_offset': retval,
            'Offset_X': round(n1.value[0], 3),  
            'Offset_Y': round(n2.value[0], 3),
            'Offset_Z': round(n3.value[0], 3),
        }
    
    def GetMemberLocalOffSet(self, beam:int, start = 1):
        """
        Get beam end offsets in all three local directions.
        """
        if start:
            end = 0
        else:
            end = 1

        safe_n1 = make_safe_array_double(1)
        n1 = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        safe_n2 = make_safe_array_double(1)
        n2 = make_variant_vt_ref(safe_n2,  automation.VT_R8)

        safe_n3 = make_safe_array_double(1)
        n3 = make_variant_vt_ref(safe_n3,  automation.VT_R8)

        retval = self._property.GetMemberLocalOffSet(beam,end,n1,n2,n3)

        return { 'Has_offset': retval,
            'Offset_X': round(n1.value[0], 3),  
            'Offset_Y': round(n2.value[0], 3),
            'Offset_Z': round(n3.value[0], 3),
        }

    def GetMemberReleaseSpecEx(self,beam:int, start = True):
        """
        Gets the member release specifications (FX, FY, FZ, MX, MY, MZ) for a given beam at a specified end.
        """
        if start:
            end = 0
        else:
            end = 1

        safe_n1 = make_safe_array_long(6)
        n1 = make_variant_vt_ref(safe_n1, automation.VT_ARRAY | automation.VT_I4)

        safe_n2 = make_safe_array_long(6)
        n2 = make_variant_vt_ref(safe_n2, automation.VT_ARRAY | automation.VT_I4)

        safe_n3 = make_safe_array_long(6)
        n3 = make_variant_vt_ref(safe_n3, automation.VT_ARRAY | automation.VT_I4)

        safe_n4 = make_safe_array_long(6)
        n4 = make_variant_vt_ref(safe_n4, automation.VT_ARRAY | automation.VT_I4)

        retval = self._property.GetMemberReleaseSpecEx(beam,end,n1,n2,n3,n4)

        return n1.value[0]
    
    def GetMemberSpecCode(self, memb:int):
        """
        Obtain the code specification of member.
        
        Returns:
            int: Specification Code
                0 -> Truss Member
                1 -> Tension-only Member
                2 -> Compression-only Member
                3 -> Cable-only Member
                4 -> Joist Member
                -1 -> Other
        """
        
        specCode = ctypes.c_long()
        
        result = self._property.GetMemberSpecCode(memb, ctypes.byref(specCode))
        
        spec_value = specCode.value
        
        return spec_value
    
    def GetPlateMaterialName(self,plate:int):   
        """
        Get plate material string name.
        """
        return self._property.GetPlateMaterialName(plate)

    def GetPublishedProfileName(self,staad_name:str,country_code:int):
        """
        Get project published name by STAAD profile name.
        """
        return self._property.GetPublishedProfileName(staad_name,country_code)
    
    def GetSectionPropertyAssignedBeamCount(self,ref_no:int):
        """
        Get section assigned beam count.
        """
        return self._property.GetSectionPropertyAssignedBeamCount(ref_no)
    
    def GetSectionPropertyAssignedBeamList(self, ref_no: int):
        """
        Get section assigned beam list.
        """
        count = self._property.GetSectionPropertyAssignedBeamCount(ref_no)

        if count == 0:
            return []

        safe_array = make_safe_array_long(count)

        beam_list = make_variant_vt_ref(safe_array,automation.VT_ARRAY | automation.VT_I4)

        self._property.GetSectionPropertyAssignedBeamList(ref_no, beam_list)

        return beam_list[0]



    def GetSTAADProfileName(self,published_name:str,country_code:int):
        """
        Gets STAAD profile name by published profile name.
        """
        return self._property.GetSTAADProfileName(published_name,country_code)
    
    def GetSectionPropertyCount(self):
        """
        The total number of different sectional properties.
        """
        return self._property.GetSectionPropertyCount()

    def GetSectionPropertyCountry(self,ref_no:int):
        """
        Return the country reference number for the section property reference number specified.
        """

        return self._property.GetSectionPropertyCountry(ref_no)
        
    def GetSectionPropertyName(self,ref_no:int):
        """
        Get the property name for the specified section property reference number.
        """
        name_var, name_bstr = make_safe_bstr()

        self._property.GetSectionPropertyName(ref_no, name_var)

        return name_bstr.value
    
    def GetSectionPropertyType(self,ref_no:int):
        """
        Return the section property type for the specified section property reference number.
        """
        return self._property.GetSectionPropertyType(ref_no)
    
    def GetSectionPropertyValues(self,ref_no:int):
        """
            Gets various geometric property values for a section given its reference number. The descriptions of the returned dictionary keys are based on the function's docstring. 
            Return:
            [out]	varfWidth	Width of the section (WID).
            [out]	varfDepth	Depth of the section (DEP).
            [out]	varfAx	Cross section area (Ax).
            [out]	varfAy	Shear area in local y-axis. If zero, shear deformation is ignored in the analysis (Ay).
            [out]	varfAz	Shear area in local z-axis. If zero, shear deformation is ignored in the analysis (Az).
            [out]	varfIx	Moment of inertia about local z-axis (Ix).
            [out]	varfIy	Moment of inertia about local y-axis (Iy).
            [out]	varfIz	Torsional constant (Iz).
            [out]	varfTf	Thickness of top flange (Tf).
            [out]	varfTw	Thickness of web (Tw).
        """

        safe_n1 = make_safe_array_double(1)
        n1 = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        safe_n2 = make_safe_array_double(1)
        n2 = make_variant_vt_ref(safe_n2,  automation.VT_R8)

        safe_n3 = make_safe_array_double(1)
        n3 = make_variant_vt_ref(safe_n3,  automation.VT_R8)

        safe_n4 = make_safe_array_double(1)
        n4 = make_variant_vt_ref(safe_n4,  automation.VT_R8)

        safe_n5 = make_safe_array_double(1)
        n5 = make_variant_vt_ref(safe_n5,  automation.VT_R8)

        safe_n6 = make_safe_array_double(1)
        n6 = make_variant_vt_ref(safe_n6,  automation.VT_R8)

        safe_n7 = make_safe_array_double(1)
        n7 = make_variant_vt_ref(safe_n7,  automation.VT_R8)

        safe_n8 = make_safe_array_double(1)
        n8 = make_variant_vt_ref(safe_n8,  automation.VT_R8)

        safe_n9 = make_safe_array_double(1)
        n9 = make_variant_vt_ref(safe_n9,  automation.VT_R8)

        safe_n10 = make_safe_array_double(1)
        n10 = make_variant_vt_ref(safe_n10,  automation.VT_R8)

        ret_val = self._property.GetSectionPropertyValues(ref_no,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)
        
        a1 = round(n1.value[0]*1000)/1000
        a2 = round(n2.value[0]*1000)/1000
        a3 = round(n3.value[0]*1000000)/1000000
        a4 = round(n4.value[0]*1000000)/1000000
        a5 = round(n5.value[0]*1000000)/1000000
        a6 = round(n6.value[0]*1000000)/1000000
        a7 = round(n7.value[0]*1000)/1000
        a8 = round(n8.value[0]*1000)/1000
        a9 = round(n9.value[0]*10000)/10000
        a10 = round(n10.value[0]*10000)/10000
        
        return {'Is_Ref':ret_val,
                'WID': a1,
                'DEP': a2,
                'Ax': a3,
                'Ay': a4,
                'Az': a5,
                'Ix': a6,
                'Iy': a7,
                'Iz': a8,
                'Tf': a9,
                'Tw': a10
                }
        
    def GetSectionPropertyValuesEx(self, ref_no: int):
        """
        Get all parameters of a specified section property by section property ID.
        """

        # --------------------------------------------------
        # 1. propType (out) → LONG
        # --------------------------------------------------
        safe_type = make_safe_array_long(1)
        var_type = make_variant_vt_ref(
            safe_type,
            automation.VT_I4
        )

        # --------------------------------------------------
        # 2. Tamaño del array (CORRECTO)
        # --------------------------------------------------
        count = self._property.GetCountofSectionPropertyValuesEx(ref_no)

        if count <= 0:
            return {
                "status": count,
                "error": "Invalid section property reference"
            }

        # --------------------------------------------------
        # 3. Crear SAFEARRAY de valores
        # --------------------------------------------------
        safe_values = make_safe_array_double(count)
        var_values = make_variant_vt_ref(
            safe_values,
            automation.VT_ARRAY | automation.VT_R8
        )

        # --------------------------------------------------
        # 4. Llamada principal
        # --------------------------------------------------
        status = self._property.GetSectionPropertyValuesEx(
            ref_no,
            var_type,
            var_values
        )

        if status < 0:
            return {
                "status": status,
                "error": "Failed to get section property values"
            }

        # --------------------------------------------------
        # 5. Resultado
        # --------------------------------------------------
        prop_type = safe_type[0]
        values = list(safe_values)

        return {
            "status": status,
            "prop_type": prop_type,
            "raw_values": values
        }




    def GetSectionTableNo(self,beam:int):
        """
        Get section table number.
        """
        return self._property.GetSectionTableNo(beam)

    
    def IsRelease(self, memb):
        """
        Checks if a member has any releases specified at its start or end node.
        *Note: The accuracy of this function depends on `GetMemberReleaseSpecEx` returning a tuple of 6 release values for each end. If `GetMemberReleaseSpecEx` only returns a single integer (e.g., FX status), the comparison `rel_i == (0,0,0,0,0,0)` will likely not work as intended.*
        """
        rel_i = self.GetMemberReleaseSpecEx(memb, start=True)
        rel_j = self.GetMemberReleaseSpecEx(memb,start=False)     

        if rel_i == (0,0,0,0,0,0) and rel_j == (0,0,0,0,0,0):
            return False
        else:
            return True

    