from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Properties():
    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._property = self._staad.Property

        self._functions= [
            'GetBeamSectionName',
            'GetBeamSectionPropertyRefNo',
            'GetSectionPropertyValues',
            'GetAlphaAngleForSection',
            'GetMemberReleaseSpecEx',
            'GetMemberSpecCode'
        ]

        for function_name in self._functions:
            self._property._FlagAsMethod(function_name)

    ## PROPERTIES FUNCTIONS

    def GetBeamSectionName(self,beam):
        return self._property.GetBeamSectionName(beam)

    def GetBeamSectionPropertyRefNo(self,beam):
        return self._property.GetBeamSectionPropertyRefNo(beam)


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
    
    ## SPECIFICATIONS

    def GetAlphaAngleForSection(self,ref_no):
        """
        Returns the alpha angle of the section in radian.
        Gets the angle between the principal axis and geometric axis of the section

        Parameters:
        [in]	nPropNo	The specified property ID.
        [out]	dAlpha	alpha angle returned (in Radian).
        """
        safe_n1 = make_safe_array_double(0)
        n1 = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        self._property.GetAlphaAngleForSection(ref_no,n1)

        return n1.value[0]
    
     ## SPECIFICATIONS

    def GetMemberReleaseSpecEx(self,beam, star = True):
    ## solo funcionan ben el n1 que es el de los releses FX, FY, FZ, MX, MY, MZ
        if star:
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
    
    def isrelease(self, memb):
        rel_i = self.GetMemberReleaseSpecEx(memb, star=True)
        rel_j = self.GetMemberReleaseSpecEx(memb,star=False)     

        if rel_i == (0,0,0,0,0,0) and rel_j == (0,0,0,0,0,0):
            return False
        else:
            return True
        
    def GetMemberSpecCode(self, memb):
        """
        Warning('GetMemberSpecCode output could be wrong')
         0->    Truss Member
         1->	Tension-only Member
         2->	Compression-only Member
         3->	Cable-only Member
         4->	Joist Member
        -1->    Other
        """
        make_safe_array_int = make_safe_array_long(1)
        spe = make_variant_vt_ref(make_safe_array_int, automation.VT_ARRAY | automation.VT_I4)
        # print(Warning('GetMemberSpecCode output could be wrong'))
        return int(self._property.GetMemberSpecCode(memb,spe))