from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Properties():
    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._property = self._staad.Property

        self._functions= [
            'GetAlphaAngleForSection',
            'GetBeamSectionName',
            'GetBeamSectionPropertyRefNo',
            'GetMemberReleaseSpecEx',
            'GetMemberSpecCode',
            'GetSectionPropertyValues'
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
        a9 = round(n9.value[0]*1000)/1000
        a10 = round(n10.value[0]*1000)/1000
        
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

