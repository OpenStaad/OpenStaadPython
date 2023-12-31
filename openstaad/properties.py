from openstaad.Safe_variables import *
from comtypes import automation

class Properties():
    def __init__(self,os):
        self._os = os.Property

        self._functions= [
            'GetBeamSectionName',
            'GetBeamSectionPropertyRefNo',
            'GetSectionPropertyValues'
        ]

        for function_name in self._functions:
            self._os._FlagAsMethod(function_name)

    ## PROPERTIES FUNCTIONS

    def GetBeamSectionName(self,beam):
        return self._os.GetBeamSectionName(beam)

    def GetBeamSectionPropertyRefNo(self,beam):
        return self._os.GetBeamSectionPropertyRefNo(beam)


    def GetSectionPropertyValues(self,ref_no):
        """ [out]	varfWidth	Width of the section (WID).
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

       
                
        ret_val = self._os.GetSectionPropertyValues(ref_no,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)
        
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