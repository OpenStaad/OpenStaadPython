from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Load():
    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._load = self._staad.Load

        self._functions= [
            'GetLoadCaseTitle',
            'AddResponseSpectrumLoadEx',
            'SetLoadActive',
            'ClearPrimaryLoadCase',
            'AddMemberConcForce',
            'CreateNewPrimaryLoad',
            'DeleteWindDefinition',
            'AddWindDefinition',
            'CreateNewReferenceLoad',
            'GetReferenceLoadCaseCount',
            'GetReferenceLoadCaseNumbers',
            'SetReferenceLoadActive',
            'DeleteDirectAnalysisDefinition',
            'DeleteDirectAnalysisDefinitionParameter',
            'AddSelfWeightInXYZ'
        ]

        for function_name in self._functions:
            self._load._FlagAsMethod(function_name)

    def GetLoadCaseTitle(self,lc):
        return self._load.GetLoadCaseTitle(lc)
    
    def AddMemberConcForce(self,varBeamNo:list[int],varDirection:int,varForce:float,varD1:float,varD2:float):

        def make_safe_array_long(array):
            size = len(array)
            return automation._midlSAFEARRAY(ctypes.c_long).create(array)
        
        safe_list = make_safe_array_long(varBeamNo)
        varBeamNo = make_variant_vt_ref(safe_list, automation.VT_ARRAY | automation.VT_I4)

        return self._load.AddMemberConcForce(varBeamNo,varDirection,varForce,varD1,varD2)
    
    def AddResponseSpectrumLoadEx(self, code_number, modal_combination, set_names_1, set_values_1, set_names_2, set_values_2, spectrum_data_pairs):
        """Adds Response Specturm load item to the currently active load case.

        Parameters
        [in]	code_number	Response Spectrum Loading Code. Refer to the following table for the integers corresponding to different codes.
        [in]	modal_combination	Modal combination rule. (SRSS = 0, ABS = 1, CQC = 2, ASCE = 3, TEN = 4, CSM = 5, GRP = 6)
        [in]	Set1Names	VARIANT BSTR array containing parameter key words. Refer to the Techincal Reference sections as indicated below.
        [in]	Set1Vals	Parameters values corresponding to the keywords supplied in varSet1Names array.
        [in]	Set2Names	Optional VARIANT BSTR array containing parameter key words for the spectrum generation data command. NULL can be used if not neeed.
        [in]	Set2Vals	Parameters values corresponding to the keywords supplied in varSet2Names array. NULL can be used if not needed.
        [in]	DataPairs	VARIANT double array containing pairs of time period and accleration data. NULL can used if not needed. Inputs (varSet2Names, varSet2Vals) and (varDataPairs) are mutually exclusive, i.e. if one is specified, other should not specified."""
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

    def SetLoadActive(self,load_case):
        return self._load.SetLoadActive(load_case)

    def ClearPrimaryLoadCase(self,load_case:int,is_reference_lc:bool=False):
        return self._load.ClearPrimaryLoadCase(load_case,is_reference_lc)
    
    def CreateNewPrimaryLoad(self,LoadTitle:str="LOAD CASE X"):
        return self._load.CreateNewPrimaryLoad(LoadTitle)

    def DeleteWindDefinition(self,type_No):
        return self._load.DeleteWindDefinition(type_No)

    def AddWindDefinition(self,type_No,type_name):
        return self._load.AddWindDefinition(type_No,type_name)

    def CreateNewReferenceLoad(self,load_No,loadcase_title,load_type):
        return self._load.CreateNewReferenceLoad(load_No,loadcase_title,load_type)

    def GetReferenceLoadCaseCount(self):
        return self._load.GetReferenceLoadCaseCount()
    
    # def GetReferenceLoadCaseNumbers(self):
    #     return self._load.GetReferenceLoadCaseNumbers()

    def SetReferenceLoadActive(self,load_case):
        return self._load.SetReferenceLoadActive(load_case)
    
    def DeleteDirectAnalysisDefinition(self):
        return self._load.DeleteDirectAnalysisDefinition()
    
    def DeleteDirectAnalysisDefinitionParameter(self,parameter_type):
        return self._load.DeleteDirectAnalysisDefinitionParameter(parameter_type)
    
    def AddSelfWeightInXYZ(self, load_direction: int, load_factor: float):

        v_direction = automation.VARIANT()
        v_direction.value = load_direction

        v_factor = automation.VARIANT()
        v_factor.value = float(load_factor)

        return self._load.AddSelfWeightInXYZ(v_direction, v_factor)
    
