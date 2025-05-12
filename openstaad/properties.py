from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Properties():
    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._property = self._staad.Property

        self._functions= [
            "AssignBeamProperty",
            "AssignMaterialToMember",
            "AssignMemberSpecToBeam",
            "CreateBeamPropertyFromTable",
            "CreateMemberReleaseSpec",
            "GetAlphaAngleForSection",
            "GetBeamSectionName",
            "GetBeamSectionPropertyRefNo",
            "GetMemberReleaseSpecEx",
            "GetMemberSpecCode",
            "GetSectionPropertyValues"
        ]

        for function_name in self._functions:
            self._property._FlagAsMethod(function_name)

    def AssignBeamProperty(self, beams_list: list[int], propertyNo: int):
        """
        Assign beam property.
        """
        def make_safe_array_long(array):
            size = len(array)
            return automation._midlSAFEARRAY(ctypes.c_long).create(array)

        safe_list = make_safe_array_long(beams_list)
        beams_list = make_variant_vt_ref(safe_list, automation.VT_ARRAY | automation.VT_I4)

        retval= self._property.AssignBeamProperty(beams_list, propertyNo)

        return retval
    
    def AssignMaterialToMember(self, material_name: str, beamNo: list[int]):
        """
        Assign material to member.
        """
        def make_safe_array_long(array):
            size = len(array)
            return automation._midlSAFEARRAY(ctypes.c_long).create(array)
        
        safe_list = make_safe_array_long(beamNo)
        beamNo = make_variant_vt_ref(safe_list, automation.VT_ARRAY | automation.VT_I4)

        retval= self._property.AssignMaterialToMember(material_name, beamNo)

        return retval
    
    def AssignMemberSpecToBeam(self, Beams: list[int], specNo: int):
        """
        Assign specifications to beam(s).
        """
        def make_safe_array_long(array):
            size = len(array)
            return automation._midlSAFEARRAY(ctypes.c_long).create(array)
        
        # Crear SAFEARRAY para 'release'
        safe_list_release = make_safe_array_long(Beams)
        Beams = make_variant_vt_ref(safe_list_release, automation.VT_ARRAY | automation.VT_I4)

        retval= self._property.AssignMemberSpecToBeam(Beams, specNo)

        return retval
    
    def CreateBeamPropertyFromTable(self,Country_code:int,profile_name:str,type_spec:int=0,spec_1:float=0.0,spec_2:float=0.0):
        
        """
        Creates beam property from table.

        COUNTRY CODE
         1->    American
         2->	Australian
         3->	British
         4->	Canadian
         5->	Chinese
         6->	Dutch
         7->	European
         8->	French
         9->	German
         10->	Indian
         11->	Japanese
         12->	Russian
         13->	Southafrican
         14->	Spanish
         15->	Venezuelan
         16->	Korean
         17->	Aluminum
         18->	American cold formed
         19->	Indian cold formed
         20->	Mexican
         21->	American Steel Joist
         22->	AITCTimber
         23->	Lysaght cold formed
         24->	British cold formed
         25->	Canadian Timber
         26->	Butler cold formed
         27->	Kingspan cold formed
         28->	RCeco cold formed
         29->	Japanese cold formed
         30->	Australian cold formed
        """
        propertyNo = self._property.CreateBeamPropertyFromTable(Country_code,profile_name,type_spec,spec_1,spec_2)
    
    def CreateMemberReleaseSpec(self, location: int, release: list[int], spring_const: list[float]):
        """
        Creates MEMBER RELEASE specification.

        LOCATION
            0 -> Start
            1 -> End
        RELEASE
            [FX, FY, FZ, MX, MY, MZ]
        SPRINGCONST
            [KFX, KFY, KFZ, KMX, KMY, KMZ]
        """
        
        def make_safe_array_long(array):
            size = len(array)
            return automation._midlSAFEARRAY(ctypes.c_long).create(array)
        
        def make_safe_array_double(array):
            size = len(array)
            return automation._midlSAFEARRAY(ctypes.c_double).create(array)
        
        safe_list_release = make_safe_array_long(release)
        release_variant = make_variant_vt_ref(safe_list_release, automation.VT_ARRAY | automation.VT_I4)
        
        safe_list_spring_const = make_safe_array_double(spring_const)
        spring_const_variant = make_variant_vt_ref(safe_list_spring_const, automation.VT_ARRAY | automation.VT_R8)
        
        retval = self._property.CreateMemberReleaseSpec(location, release_variant, spring_const_variant)
        return retval
    
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

