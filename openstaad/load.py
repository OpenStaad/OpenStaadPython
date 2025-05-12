from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Load():
    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._load = self._staad.Load

        self._functions= [
            "AddMemberConcForce",
            "AddResponseSpectrumLoadEx",
            "AddSelfWeightInXYZ",
            "AddWindDefinition",
            "ClearPrimaryLoadCase",
            "CreateNewPrimaryLoad",
            "CreateNewReferenceLoad",
            "DeleteDirectAnalysisDefinition",
            "DeleteDirectAnalysisDefinitionParameter",
            "DeleteWindDefinition",
            "GetLoadCaseTitle",
            "GetReferenceLoadCaseCount",
            "SetLoadActive",
            "SetReferenceLoadActive"
        ]

        for function_name in self._functions:
            self._load._FlagAsMethod(function_name)

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
    
    def DeleteWindDefinition(self,type_No:int=0):
        """
        Deletes Wind definition. All definitions will be deleted if this input is set as 0.
        """
        return self._load.DeleteWindDefinition(type_No)
    
    def GetLoadCaseTitle(self,lc:int=0):
        """
        Returns title of the specified load case as a text string. Input 0 to retrieve title of current active load case or reference load case.
        """
        return self._load.GetLoadCaseTitle(lc)
    
    def GetReferenceLoadCaseCount(self):
        """
        Returns the number of reference load case defined in Reference Load Definitions.
        """
        return self._load.GetReferenceLoadCaseCount()

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
    
    
    
    
    
