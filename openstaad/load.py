from openstaad.tools import *
from comtypes import automation
from comtypes import client
from comtypes import CoInitialize
from comtypes import COMError
import os

class Load():
    def __init__(self, filePath: str = None):
        CoInitialize()
        
        try:
            if filePath:
                filePath = os.path.abspath(filePath)
                if not os.path.exists(filePath):
                    raise FileNotFoundError(filePath)

                root_com = client.CoGetObject(filePath, dynamic=True)
            else:

                root_com = client.GetActiveObject("StaadPro.OpenSTAAD")

            self._load = root_com.Load

        except COMError:
            raise RuntimeError("Cannot connect to STAAD.Pro")

        self._functions= [
    	"AddMemberConcForce",
	    "AddNodalLoad",
    	"AddResponseSpectrumLoadEx",
    	"AddSelfWeightInXYZ",
    	"AddWindDefinition",
    	"ClearPrimaryLoadCase",
	    "ClearReferenceLoadCase",
    	"CreateNewPrimaryLoad",
    	"CreateNewReferenceLoad",
    	"DeleteDirectAnalysisDefinition",
    	"DeleteDirectAnalysisDefinitionParameter",
    	"DeletePrimaryLoadCases",
    	"DeleteWindDefinition",
        "GetActiveLoad",
        "GetConcForceCount",
        "GetConcForces",
        "GetEnvelopeCount",
        "GetEnvelopeIDs",
    	"GetLoadCombinationCaseCount",
    	"GetLoadCombinationCaseNumbers",
    	"GetLoadCaseTitle",
        "GetLoadEnvelopeDetails",
        "GetLoadItemsCount",
    	"GetLoadListCount",
        "GetLoadListfromLoadEnvelope",
    	"GetLoadType",
        "GetMemberLoadInfo",
        "GetNodalLoadCount",
        "GetNodalLoads",
        "GetNodalLoadInfo",
        "GetNoLoadFactorDirectionInNotionalLoad",
        "GetNoOfSetsInReferenceLoad",
        "GetNotionalLoadByIndex",
        "GetNotionalLoadCount",
    	"GetPrimaryLoadCaseCount",
        "GetPrimaryLoadCaseNumbers",
        "GetReferenceLoadByIndex",
    	"GetReferenceLoadCaseCount",
    	"GetReferenceLoadCaseNumbers",
        "GetReferenceLoadCaseTitle",
        "GetReferenceLoadType",
        "GetTrapLoadCount",
        "GetTrapLoads",
        "GetUDLLoadCount",
        "GetUDLLoads",
        "GetUNIMomentCount",
        "GetUNIMoments",
    	"SetLoadActive",
    	"SetReferenceLoadActive"
	    ]

        for function_name in self._functions:
            self._load._FlagAsMethod(function_name)

    def __getattr__(self, name):
        return getattr(self._load, name)

    def AddMemberConcForce(self,varBeamNo:list[int],varDirection:int,varForce:float,varD1:float,varD2:float):
        """
        Adds CONCENTRATED FORCE to beam(s).
        """
        def make_safe_array_long(array):
            size = len(array)
            return automation._midlSAFEARRAY(ctypes.c_long).create(array)
        
        safe_list = make_safe_array_long(varBeamNo)
        varBeamNo = make_variant_vt_ref(safe_list, automation.VT_ARRAY | automation.VT_I4)

        return self._load.AddMemberConcForce(varBeamNo,varDirection,varForce,varD1,varD2)
    
    def AddNodalLoad(self, nodes : list[int], fx : float, fy:float, fz:float, mx:float, my:float, mz:float):
        def make_safe_array_long(array):
            return automation._midlSAFEARRAY(ctypes.c_long).create(array)

        safe_list = make_safe_array_long(nodes)
        varNodeNo = make_variant_vt_ref(safe_list, automation.VT_ARRAY | automation.VT_I4)

        self._load.AddNodalLoad(varNodeNo,fx, fy, fz, mx, my, mz)
    
    def AddResponseSpectrumLoadEx(self, code_number:int, modal_combination:int, set_names_1:list, set_values_1:list, spectrum_data_pairs:list[tuple],set_names_2:list=None, set_values_2:list=None):
        """Adds Response Spectrum load item to the currently active load case.

        Parameters
        [in]	code_number	Response Spectrum Loading Code. Refer to the following table for the integers corresponding to different codes.
        [in]	modal_combination	Modal combination rule. (SRSS = 0, ABS = 1, CQC = 2, ASCE = 3, TEN = 4, CSM = 5, GRP = 6)
        [in]	Set1Names	VARIANT BSTR array containing parameter key words. Refer to the Techincal Reference sections as indicated below.
        [in]	Set1Vals	Parameters values corresponding to the keywords supplied in varSet1Names array.
        [in]	Set2Names	Optional VARIANT BSTR array containing parameter key words for the spectrum generation data command. NULL can be used if not neeed.
        [in]	Set2Vals	Parameters values corresponding to the keywords supplied in varSet2Names array. NULL can be used if not needed.
        [in]	DataPairs	VARIANT double array containing pairs of time period and accleration data. NULL can used if not needed. Inputs (varSet2Names, varSet2Vals) and (varDataPairs) are mutually exclusive, i.e. if one is specified, other should not specified.
        """
        def make_safe_array_string1(values):
            return automation._midlSAFEARRAY(automation.BSTR).create(values)
        
        def make_safe_array_double1(values):
            return automation._midlSAFEARRAY(ctypes.c_double).create(values)
        
        array_names_1 = make_safe_array_string1(set_names_1)
        array_values_1 = make_safe_array_double1(set_values_1)

        if spectrum_data_pairs is not None:
            flat_spectrum = [val for pair in spectrum_data_pairs for val in pair]
            arr_spectrum = make_safe_array_double1(flat_spectrum)
            var_spectrum = make_variant_vt_ref(arr_spectrum, automation.VT_ARRAY | automation.VT_R8)
        else:
            var_spectrum = None

        var_set2_names = None
        var_set2_vals = None

        var_set1_names = make_variant_vt_ref(array_names_1, automation.VT_ARRAY | automation.VT_BSTR)
        var_set1_vals = make_variant_vt_ref(array_values_1, automation.VT_ARRAY | automation.VT_R8)

        return self._load.AddResponseSpectrumLoadEx(code_number,modal_combination,var_set1_names,var_set1_vals,var_set2_names,var_set2_vals,var_spectrum)
    
    def AddSelfWeightInXYZ(self, load_direction: int, load_factor: float):
        """
        Adds a self weight to the active load case.
        """
        v_direction = automation.VARIANT()
        v_direction.value = load_direction

        v_factor = automation.VARIANT()
        v_factor.value = float(load_factor)

        return self._load.AddSelfWeightInXYZ(v_direction, v_factor)
    
    def AddWindDefinition(self,type_No:int,type_name:str):
        """
        Adds a Wind Definition named type_name" with number ID type_No.
        """
        return self._load.AddWindDefinition(type_No,type_name)
    
    def ClearPrimaryLoadCase(self,load_case:int,is_reference_lc:bool=False):
        """
        Clears the load items in a specified Primary Load cases or Reference Load cases.
        """
        return self._load.ClearPrimaryLoadCase(load_case,is_reference_lc)
    
    def ClearReferenceLoadCase(self,reference_load_number: int):
        self._load.ClearReferenceLoadCase(reference_load_number)
    
    def CreateNewPrimaryLoad(self,LoadTitle:str="LOAD CASE X"):
        """
        Creates new PRIMARY load case.
        """
        return self._load.CreateNewPrimaryLoad(LoadTitle)
    
    def CreateNewReferenceLoad(self,load_No:int,loadcase_title:str,load_type:int):
        """
        Creates a new Reference Load Definition and set as active.
        """
        return self._load.CreateNewReferenceLoad(load_No,loadcase_title,load_type)
    
    def DeleteDirectAnalysisDefinition(self):
        """
        Deletes whole Direct Analysis Definition.
        """
        return self._load.DeleteDirectAnalysisDefinition()
    
    def DeleteDirectAnalysisDefinitionParameter(self,parameter_type:int=0):
        """
        Deletes respective parameters from Direct Analysis Definition based on the Parameter Type passed as argument (FLEX/AXIAL).
        Flex  --- 0
        Axial --- 2
        """
        return self._load.DeleteDirectAnalysisDefinitionParameter(parameter_type)
    
    def DeletePrimaryLoadCases(self,load_case:int,is_reference:bool=False):
        return self._load.DeletePrimaryLoadCases(load_case,is_reference)
    
    def DeleteWindDefinition(self,type_No:int=0):
        """
        Deletes Wind definition. All definitions will be deleted if this input is set as 0.
        """
        return self._load.DeleteWindDefinition(type_No)
    
    def GetActiveLoad(self):
        """
        Returns the current load case number.
        """
        return self._load.GetActiveLoad()
    
    def GetConcForceCount(self, beam_no:int):
        """
        Get number of concentrated force(s) present for the specified beam.
        """
        return self._load.GetConcForceCount(beam_no)
    
    def GetConcForces(self, beam_no:int):
        """
        Returns the concentrated force(s) with all the parameters for the specified member.
        """

        conc_force_count=self._load.GetConcForceCount(beam_no)

        safe_list_direction= make_safe_array_long(conc_force_count)
        list_direction = make_variant_vt_ref(safe_list_direction,  automation.VT_ARRAY | automation.VT_I4)

        safe_list_force= make_safe_array_double(conc_force_count)
        list_force = make_variant_vt_ref(safe_list_force,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_d1= make_safe_array_double(conc_force_count)
        list_d1 = make_variant_vt_ref(safe_list_d1,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_d2= make_safe_array_double(conc_force_count)
        list_d2 = make_variant_vt_ref(safe_list_d2,  automation.VT_ARRAY | automation.VT_R8)

        retval= self._load.GetConcForces(beam_no, list_direction, list_force, list_d1, list_d2)

        if not bool(retval):
            return [], [], [], []
        
        return (list_direction[0], list_force[0], list_d1[0], list_d2[0])
    
    def GetEnvelopeCount(self):
        """
        Returns the number of envelope load cases defined in the current structure.
        """
        return self._load.GetEnvelopeCount()
    
    def GetEnvelopeIDs(self):
        """
        Gets the list of Loads Envelope IDs present in the staad file.
        """
        envelope_id_count=self._load.GetEnvelopeCount()

        safe_list_env_id= make_safe_array_long(envelope_id_count)
        env_id_list= make_variant_vt_ref(safe_list_env_id,  automation.VT_ARRAY | automation.VT_I4)

        return self._load.GetEnvelopeIDs(env_id_list)


    def GetLoadCaseTitle(self,lc:int=0):
        """
        Returns title of the specified load case as a text string. Input 0 to retrieve title of current active load case or reference load case.
        """
        return self._load.GetLoadCaseTitle(lc)
    
    def GetLoadCombinationCaseCount(self):
        """
        Gets total number of combination load case(s) present in the current structure.
        """
        return self._load.GetLoadCombinationCaseCount()
    
    def GetLoadCombinationCaseNumbers(self):
        """
        Gets all load combination case number(s).
        """
        lc_case_count=self._load.GetLoadCombinationCaseCount()
        safe_list = make_safe_array_long(lc_case_count)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._load.GetLoadCombinationCaseNumbers(lista)

        return (lista[0])
    
    def GetLoadEnvelopeDetails(self,envelope_no:int):
        """
        Returns a tuple containing EnvelopeType and NumberofLoadCasesInEnvelope information respectively. 
        Type of Load Envelope
        """
        safe_envelope_type= make_safe_array_long(0)
        envelope_type=make_variant_vt_ref(safe_envelope_type,automation.VT_I4)

        safe_number_of_lc_envelope= make_safe_array_long(0)
        number_of_lc_envelope=make_variant_vt_ref(safe_number_of_lc_envelope,automation.VT_I4)

        self._load.GetLoadEnvelopeDetails(envelope_no,envelope_type,number_of_lc_envelope)

        return (envelope_type[0],number_of_lc_envelope[0])
    
    def GetLoadItemsCount(self,load_case:int):
        """
        Gets the number of load items in the specified load case.
        """
        return self._load.GetLoadItemsCount(load_case)

    def GetLoadItemType(self,load_case:int, item_index:int):
        """
        Returns the load item type for the specified loadIndex and loadCase.
        """
        LOAD_ITEM_TYPE = {
        4000: "SelfWeight",
        3110: "Nodal Load (Node)",
        3120: "Nodal Load (Inclined)",
        3910: "Nodal Load (Support Displacement)",
        3312: "Partial plate pressure load",
        3210: "Uniform Force",
        3220: "Uniform Moment",
        3230: "Concentrated Force",
        3240: "Concentrated Moment",
        3250: "Linear Varying",
        3260: "Trapezoidal",
        3261: "Hydrostatic",
        3620: "Pre/Post Stress",
        3810: "Fixed End",
        3275: "Uniform Force (Physical)",
        3280: "Uniform Moment (Physical)",
        3285: "Concentrated Force (Physical)",
        3290: "Concentrated Moment (Physical)",
        3295: "Trapezoidal (Physical)",
        3410: "Area",
        3510: "FloorLoadYrange",
        3511: "FloorLoadXrange",
        3520: "FloorLoadZrange",
        3530: "FloorLoadGroup",
        3551: "OneWayFloorLoadXrange",
        3552: "OneWayFloorLoadYrange",
        3553: "OneWayFloorLoadZrange",
        3554: "OneWayFloorLoadGroup",
        3310: "Pressure on full plate",
        3311: "Concentrated Load (Plate)",
        3320: "Trapezoidal (Plate)",
        3322: "Solid",
        3710: "Temperature",
        3720: "Strain",
        3721: "Strain Rate",
        4400: "UBC Load",
        4405: "IbcLoad",
        4410: "1893Load",
        4500: "AijLoad",
        4510: "ColombianLoad",
        4520: "CFELoad",
        4530: "RPALoad",
        4540: "NTCLoad",
        4550: "NRCLoad",
        4560: "NRCLoad2005",
        4561: "NRCLoad2010",
        4570: "TurkishLoad",
        4575: "GB50011Load",
        4576: "Colombian2010Load",
        4600: "Wind Load",
        4610: "Wind Load Dynamic",
        4650: "Snow Load",
        4651: "Snow Load Data",
        4820: "TimeHistoryLoad",
        4100: "Spectrum Load",
        4101: "Spectrum Data",
        4200: "Repeat load",
        4201: "Repeat load data",
        4220: "Reference Load",
        4222: "Notional Load",
        4223: "Notional Load Data",
        4700: "Calulate Natural Frequency",
        4701: "Calulate Rayleigh Frequency",
        4710: "Modal Calculation Requested",
        }
        
        load_type_code=self._load.GetLoadItemType(load_case, item_index)

        return LOAD_ITEM_TYPE.get(load_type_code, "Unknown Load Item Type")
    
    def GetLoadListCount(self):
        """
        Gets the number of existing load list(s)
        """
        return self._load.GetLoadListCount()
    
    def GetLoadListfromLoadEnvelope(self,envelope_no:int):
        """
        Gets the list of primary load case reference Ids present in the load envelope passed.
        """
        load_envelope_details=self.GetLoadEnvelopeDetails(envelope_no)
        
        safe_list_lc= make_safe_array_long(load_envelope_details[1])
        lc_list= make_variant_vt_ref(safe_list_lc,  automation.VT_ARRAY | automation.VT_I4)

        self._load.GetLoadListfromLoadEnvelope(envelope_no, lc_list)

        return (list(lc_list[0]))
    
    def GetLoadType(self,load_no:int):
        """
        Returns primary load case category(s) as an long value.
        """
        LOAD_TYPE = {
            0:  "Dead",
            1:  "Live",
            2:  "Roof Live",
            3:  "Wind",
            4:  "Seismic-H",
            5:  "Seismic-V",
            6:  "Snow",
            7:  "Fluids",
            8:  "Soil",
            9:  "Rain",
            10: "Ponding",
            11: "Dust",
            12: "Traffic",
            13: "Temperature",
            14: "Imperfection",
            15: "Accidental",
            16: "Flood",
            17: "Ice",
            18: "Wind Ice",
            19: "Crane Hook",
            20: "Mass",
            21: "Gravity",
            22: "Push",
            23: "None",
        }

        load_type_code=self._load.GetLoadType(load_no)

        return LOAD_TYPE.get(load_type_code, "Unknown Load Item Type")
    
    def GetMemberLoadInfo(self, load_index:int):
        """
        Gets member load(s) information generated by specified load item in specified load case.
        """
        load_count=3

        safe_list_direction= make_safe_array_long(1)
        list_direction = make_variant_vt_ref(safe_list_direction,  automation.VT_ARRAY | automation.VT_I4)

        safe_list_force= make_safe_array_double(load_count)
        list_force = make_variant_vt_ref(safe_list_force,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_distance= make_safe_array_double(load_count)
        list_distance = make_variant_vt_ref(safe_list_distance,  automation.VT_ARRAY | automation.VT_R8)

        retval= self._load.GetMemberLoadInfo(load_index, list_direction, list_force, list_distance)

        if not bool(retval):
            return [], [], []
        
        return (list_direction[0], list_force[0], list_distance[0])
    
    def GetNodalLoadCount(self, node_no:int):
        """
        Returns number of nodal loads present for the specified node.
        """
        return self._load.GetNodalLoadCount(node_no)
    
    def GetNodalLoads(self, node_no:int):
        """
        Returns tuple of list of forces in X direction, forces in Y direction, forces in Z direction, moments in X direction, moments in Y direction and moments in Z direction respectively.
        """
        node_count=self._load.GetNodalLoadCount(node_no)

        safe_list_fx= make_safe_array_double(node_count)
        list_fx = make_variant_vt_ref(safe_list_fx,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_fy= make_safe_array_double(node_count)
        list_fy = make_variant_vt_ref(safe_list_fy,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_fz= make_safe_array_double(node_count)
        list_fz = make_variant_vt_ref(safe_list_fz,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_mx= make_safe_array_double(node_count)
        list_mx = make_variant_vt_ref(safe_list_mx,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_my= make_safe_array_double(node_count)
        list_my = make_variant_vt_ref(safe_list_my,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_mz= make_safe_array_double(node_count)
        list_mz = make_variant_vt_ref(safe_list_mz,  automation.VT_ARRAY | automation.VT_R8)

        self._load.GetNodalLoads(node_no, list_fx, list_fy, list_fz, list_mx, list_my, list_mz)

        return (list_fx[0], list_fy[0], list_fz[0], list_mx[0], list_my[0], list_mz[0])
        
    def GetNodalLoadInfo(self, load_index:int):
        """
        Gets nodal load(s) generated by specified load item in specified load case.
        """
        
        safe_list_force= make_safe_array_double(6)
        list_force = make_variant_vt_ref(safe_list_force,  automation.VT_ARRAY | automation.VT_R8)

        self._load.GetNodalLoadInfo(load_index, list_force)

        return (list_force[0])

    def GetNoOfSetsInReferenceLoad(self,index:int):
        """
        Returns the number of reference load case-factor sets in a specified reference load item.
        """
        return self._load.GetNoOfSetsInReferenceLoad(index)
    
    def GetNotionalLoadByIndex(self,index:int): ###TO BE CHECKED
        """
        Gets load case(s), direction(s) and factor(s) for specified Notional load.
        """
        notional_load_count = self._load.GetNoLoadFactorDirectionInNotionalLoad(index)

        safe_list_direction= make_safe_array_long(notional_load_count)
        list_direction = make_variant_vt_ref(safe_list_direction,  automation.VT_ARRAY | automation.VT_I4)

        safe_list_loadcase= make_safe_array_long(notional_load_count)
        list_loadcase = make_variant_vt_ref(safe_list_loadcase,  automation.VT_ARRAY | automation.VT_I4)

        safe_list_factor= make_safe_array_double(notional_load_count)
        list_factor = make_variant_vt_ref(safe_list_factor,  automation.VT_ARRAY | automation.VT_R8)

        self._load.GetNotionalLoadByIndex(index, list_loadcase, list_direction, list_factor)

        return (list_loadcase[0], list_direction[0], list_factor[0])



    
    def GetNotionalLoadCount(self):
        """
        Returns the number of Notional load.
        """
        return self._load.GetNotionalLoadCount()
    
    def GetNoLoadFactorDirectionInNotionalLoad(self,index:int):
        """
        Gets the no of factor for specified Notional load.
        """
        return self._load.GetNoLoadFactorDirectionInNotionalLoad(index)

    def GetPrimaryLoadCaseCount(self):
        """
        Returns the total number of primary load cases present in the current structure.
        """
        return self._load.GetPrimaryLoadCaseCount()
    
    def GetPrimaryLoadCaseNumbers(self):
        """
        Gets all primary load case number(s).
        """
        lc_case_count=self._load.GetPrimaryLoadCaseCount()
        safe_list = make_safe_array_long(lc_case_count)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._load.GetPrimaryLoadCaseNumbers(lista)

        return (lista[0])
    
    def GetReferenceLoadByIndex(self,index:int):
        """
        Retrieves a dictionary of load case numbers and their corresponding factors for a given reference load case.
        """

        reference_lc_count = self._load.GetNoOfSetsInReferenceLoad(index)

        if reference_lc_count <= 0:
            return
        
        ref_load_safe_array= make_safe_array_long(reference_lc_count)
        ref_load_array_variant= make_variant_vt_ref(ref_load_safe_array, automation.VT_ARRAY | automation.VT_I4)
        
        factor_safe_array= make_safe_array_double(reference_lc_count)
        factor_array_variant= make_variant_vt_ref(factor_safe_array, automation.VT_ARRAY | automation.VT_R8)
        retval = self._load.GetReferenceLoadByIndex(index, ref_load_array_variant, factor_array_variant)

        if retval <= 0:
            return [], []
        
        return list(ref_load_array_variant[0]), list(factor_array_variant[0])
    
    def GetReferenceLoadCaseCount(self):
        """
        Returns the number of reference load case defined in Reference Load Definitions.
        """
        return self._load.GetReferenceLoadCaseCount()

    def GetReferenceLoadCaseNumbers(self):
        """
        Retrieves reference load case number IDs from Reference Load Definitions.
        """
        lc_case_count=self._load.GetReferenceLoadCaseCount()
        safe_list = make_safe_array_long(lc_case_count)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._load.GetReferenceLoadCaseNumbers(lista)

        return (lista[0])
    
    def GetReferenceLoadCaseTitle(self,load_No:int):
        """
        Returns the title of a reference load case.
        """
        return self._load.GetReferenceLoadCaseTitle(load_No)
    
    def GetReferenceLoadType(self,load_No:int):
        """
        Returns the type of a reference load.
        """
        return self._load.GetReferenceLoadType(load_No)
    
    def GetTrapLoadCount(self, beam_no:int):
        """
        Returns number of trapezoidal load(s) present for the specified beam.
        """
        return self._load.GetTrapLoadCount(beam_no)
    
    def GetTrapLoads(self, beam_no:int):
        """
        Returns the trapezoidal load(s) with all the parameters for the specified member.
        """

        trap_load_count=self._load.GetTrapLoadCount(beam_no)

        safe_list_direction= make_safe_array_long(trap_load_count)
        list_direction = make_variant_vt_ref(safe_list_direction,  automation.VT_ARRAY | automation.VT_I4)

        safe_list_w1= make_safe_array_double(trap_load_count)
        list_w1 = make_variant_vt_ref(safe_list_w1,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_w2= make_safe_array_double(trap_load_count)
        list_w2 = make_variant_vt_ref(safe_list_w2,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_d1= make_safe_array_double(trap_load_count)
        list_d1 = make_variant_vt_ref(safe_list_d1,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_d2= make_safe_array_double(trap_load_count)
        list_d2 = make_variant_vt_ref(safe_list_d2,  automation.VT_ARRAY | automation.VT_R8)

        retval= self._load.GetTrapLoads(beam_no, list_direction, list_w1, list_w2, list_d1, list_d2)

        if not bool(retval):
            return [], [], [], [], []
        
        return (list_direction[0], list_w1[0], list_w2[0], list_d1[0], list_d2[0])
    
    def GetUDLLoadCount(self, beam_no:int):
        """
        Returns the number of uniformly distributed load(s) present for the specified beam.
        """
        return self._load.GetUDLLoadCount(beam_no)

    def GetUDLLoads(self, beam_no:int):
        """
        Gets the uniformly distributed load(s) with all the parameters for the specified member.
        """
        udl_count=self._load.GetUDLLoadCount(beam_no)

        safe_list_direction= make_safe_array_long(udl_count)
        list_direction = make_variant_vt_ref(safe_list_direction,  automation.VT_ARRAY | automation.VT_I4)

        safe_list_force= make_safe_array_double(udl_count)
        list_force = make_variant_vt_ref(safe_list_force,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_d1= make_safe_array_double(udl_count)
        list_d1 = make_variant_vt_ref(safe_list_d1,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_d2= make_safe_array_double(udl_count)
        list_d2 = make_variant_vt_ref(safe_list_d2,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_d3= make_safe_array_double(udl_count)
        list_d3 = make_variant_vt_ref(safe_list_d3,  automation.VT_ARRAY | automation.VT_R8)

        retval= self._load.GetUDLLoads(beam_no, list_direction, list_force, list_d1, list_d2, list_d3)

        if not bool(retval):
            return [], [], [], [], []
        return (list_direction[0], list_force[0], list_d1[0], list_d2[0], list_d3[0])

    def GetUNIMomentCount(self, beam_no:int):
        """
        Returns the count of uniformly distributed (UNI) moment applied to the specified member.
        """
        return self._load.GetUNIMomentCount(beam_no)
    
    def GetUNIMoments(self, beam_no:int): ###NEED TO BE CHECKED
        """
        Returns the uniformly distributed (UNI) moments with all the parameters for the specified member.
        """

        uni_moment_count=self._load.GetUNIMomentCount(beam_no)

        safe_list_direction= make_safe_array_long(uni_moment_count)
        list_direction = make_variant_vt_ref(safe_list_direction,  automation.VT_ARRAY | automation.VT_I4)

        safe_list_moment= make_safe_array_double(uni_moment_count)
        list_moment = make_variant_vt_ref(safe_list_moment,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_d1= make_safe_array_double(uni_moment_count)
        list_d1 = make_variant_vt_ref(safe_list_d1,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_d2= make_safe_array_double(uni_moment_count)
        list_d2 = make_variant_vt_ref(safe_list_d2,  automation.VT_ARRAY | automation.VT_R8)

        safe_list_d3= make_safe_array_double(uni_moment_count)
        list_d3 = make_variant_vt_ref(safe_list_d3,  automation.VT_ARRAY | automation.VT_R8)

        retval= self._load.GetUNIMoments(beam_no, list_direction, list_moment, list_d1, list_d2, list_d3)

        if not bool(retval):
            return [], [], [], [], []
        
        return (list_direction[0], list_moment[0], list_d1[0], list_d2[0], list_d3[0])
        
    def SetLoadActive(self,load_case:int):
        """
        Makes the specified load number active, in order to add or remove load item(s).
        """
        return self._load.SetLoadActive(load_case)

    def SetReferenceLoadActive(self,load_case:int):
        """
        Identify a Load Case in Load Case Details to add, count and get reference load item(s).
        """
        return self._load.SetReferenceLoadActive(load_case)
    
    
    
    
    
    
    
    
