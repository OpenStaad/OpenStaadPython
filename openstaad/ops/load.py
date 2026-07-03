"""
load.py — dominio Load del subpaquete ops, sobre bridge.

Métodos alineados al comportamiento del oficial (PascalCase). Se omiten los
`raise_os_error_if_error_code`; se conservan los condicionales que son lógica de
retorno. Los arrays de entrada van crudos (in_*_array) o envueltos en VARIANT
(in_*_array_variant) según lo que hace el oficial método a método.
"""

from .bridge import Bridge
from ._com import acquire


class Load:
    def __init__(self, connection=None, bridge=None, filePath=None):
        staad = connection if connection is not None else acquire(filePath)
        self._b = bridge if bridge is not None else Bridge()
        self._load = staad.Load

        self._functions = [
            "CreateNewPrimaryLoad", "CreateNewLoadCombination", "CreateNewReferenceLoad",
            "CreateLoadEnvelop", "CreateLoadList", "CreateNewPrimaryLoadEx",
            "CreateNewPrimaryLoadEx2", "SetLoadActive", "SetReferenceLoadActive",
            "SetLoadType", "SetASDLoadAttribute", "SetLSDLoadAttribute",
            "AddSelfWeightInXYZ", "AddSelfWeightInXYZToGeometry", "AddNodalLoad",
            "AddSupportDisplacement", "AddMemberUniformForce", "AddMemberUniformMoment",
            "AddMemberConcForce", "AddMemberConcMoment", "AddMemberLinearVari",
            "AddMemberTrapezoidal", "AddMemberAreaLoad", "AddMemberFixedEnd",
            "AddElementPressure", "AddElementHydrostaticPressure", "AddTemperatureLoad",
            "AddStrainLoad", "AddLoadAndFactorToCombination", "AddMemberFloorLoad",
            "AddMemberFloorLoadEx", "AddElementTrapPressureEx", "AddWindDefinition",
            "AddWindIntensity", "AddWindExposure", "AddWindLoad", "AddSeismicDefinition",
            "AddSeismicDefSelfWeight", "AddSeismicDefMemberWeight", "AddSeismicDefJointWeight",
            "AddSeismicDefElementWeight", "AddSeismicDefFloorWeight", "AddSeismicLoad",
            "AddAutoLoadCombinations", "AddRepeatLoad", "AddLoadCasesToEnvelop",
            "AddReferenceLoad", "AddSeismicDefWallArea", "AddWindDefinitionASCE7Parameters",
            "AddNotionalLoad", "AddDirectAnalysisDefinitionParameter",
            "AddResponseSpectrumLoadEx", "AddAutoCombinationRepeat",
            "RemoveLoadCasesFromEnvelop", "RemoveAttribute", "ClearPrimaryLoadCase",
            "ClearReferenceLoadCase", "IsDynamicLoadIncluded", "IsCombinationCase",
            "SplitLoadsOnBeam", "MergeLoadsOnBeam", "BeginLoadMerging", "EndLoadMerging",
            "ModifySeismicDefinitionParams", "ComputeWallWindPressureProfile",
            "ComputeWallWindPressureProfileASCE72016", "DeleteLoadEnvelop", "DeleteLoadList",
            "DeletePrimaryLoadCases", "DeleteReferenceLoadCases", "DeleteWindDefinition",
            "DeleteDirectAnalysisDefinitionParameter", "DeleteDirectAnalysisDefinition",
            "GetPrimaryLoadCaseCount", "GetPrimaryLoadCaseNumbers",
            "GetLoadCombinationCaseCount", "GetLoadCombinationCaseNumbers",
            "GetReferenceLoadCount", "GetReferenceLoadCaseCount",
            "GetReferenceLoadCaseNumbers", "GetNoOfSetsInReferenceLoad",
            "GetReferenceLoadByIndex", "GetReferenceLoadType", "GetReferenceLoadCaseTitle",
            "GetBeamCountAtFloor", "GetInfluenceArea", "GetActiveLoad", "GetNodalLoadCount",
            "GetNodalLoads", "GetUDLLoadCount", "GetUDLLoads", "GetUNIMomentCount",
            "GetUNIMoments", "GetTrapLoadCount", "GetTrapLoads", "GetConcForceCount",
            "GetConcForces", "GetConcMomentCount", "GetConcMoments",
            "GetNoOfLoadAndFactorPairsForCombination", "GetLoadAndFactorForCombination",
            "GetLoadCaseTitle", "GetElementPressureLoadCount", "GetElementPressureLoads",
            "GetElementConcLoadCount", "GetElementConcLoads", "GetLoadType",
            "GetLoadListCount", "GetLoadCountInLoadList", "GetLoadsInLoadList",
            "GetAttribute", "GetRepeatLoadCount", "GetNoLoadFactorInRepeatLoad",
            "GetRepeatLoadByIndex", "GetLinearVaryingLoadCount", "GetLinearVaryingLoads",
            "GetLoadTypeCount", "GetListSizeForLoadType", "GetAssignmentListForLoadType",
            "GetNodalLoadInfo", "GetMemberLoadInfo", "GetElementLoadInfo",
            "GetNotionalLoadCount", "GetNoLoadFactorDirectionInNotionalLoad",
            "GetNotionalLoadByIndex", "GetLoadItemsCount", "GetLoadItemType",
            "GetEnvelopeCount", "GetLoadEnvelopeDetails", "GetLoadListfromLoadEnvelope",
            "GetEnvelopeIDs",
        ]
        for function_name in self._functions:
            self._load._FlagAsMethod(function_name)

    # ------------------------------------------------------------------ #
    # Creación de casos / listas
    # ------------------------------------------------------------------ #
    def CreateNewPrimaryLoad(self, primaryLoadTitle: str):
        return self._load.CreateNewPrimaryLoad(primaryLoadTitle)

    def CreateNewLoadCombination(self, loadCombTitle: str, loadCombNo: int):
        return self._load.CreateNewLoadCombination(loadCombTitle, loadCombNo)

    def CreateNewReferenceLoad(self, nodeNo: int, referenceLoadCaseTitle: str, loadType: int):
        return self._load.CreateNewReferenceLoad(nodeNo, referenceLoadCaseTitle, loadType)

    def CreateLoadEnvelop(self, envelopNumber: int, envelopType: int, loadCaseList: list):
        return self._load.CreateLoadEnvelop(envelopNumber, envelopType, self._b.in_int_array(loadCaseList))

    def CreateLoadList(self, listType: int, loadCaseList: list):
        return bool(self._load.CreateLoadList(listType, self._b.in_int_array(loadCaseList)))

    def CreateNewPrimaryLoadEx(self, primaryLoadTitle: str, loadType: int):
        return self._load.CreateNewPrimaryLoadEx(primaryLoadTitle, loadType)

    def CreateNewPrimaryLoadEx2(self, primaryLoadTitle: str, loadType: int, loadCaseNo: int):
        return self._load.CreateNewPrimaryLoadEx2(primaryLoadTitle, loadType, loadCaseNo)

    def SetLoadActive(self, loadNumber: int):
        return self._load.SetLoadActive(loadNumber)

    def SetReferenceLoadActive(self, nLoadCaseNo: int):
        return self._load.SetReferenceLoadActive(nLoadCaseNo)

    def SetLoadType(self, loadCaseNumber: int, loadType: int):
        return bool(self._load.SetLoadType(loadCaseNumber, loadType))

    def SetASDLoadAttribute(self, loadCaseRefID: int, strengthType: int, allowStressIncrease: bool):
        return self._load.SetASDLoadAttribute(loadCaseRefID, strengthType, allowStressIncrease) == 0

    def SetLSDLoadAttribute(self, loadCaseRefID: int):
        return self._load.SetLSDLoadAttribute(loadCaseRefID) == 0

    # ------------------------------------------------------------------ #
    # Cargas: self weight, nodal, miembro, elemento
    # ------------------------------------------------------------------ #
    def AddSelfWeightInXYZ(self, varInDirection: int, varLoadFactor: float):
        return self._load.AddSelfWeightInXYZ(varInDirection, varLoadFactor)

    def AddSelfWeightInXYZToGeometry(self, varGeomNumberIDs: list, varInDirection: int, varLoadFactor: float):
        return self._load.AddSelfWeightInXYZToGeometry(self._b.in_int_array(varGeomNumberIDs), varInDirection, varLoadFactor)

    def AddNodalLoad(self, nodeIds: list, forceInXDir: float, forceInYDir: float, forceInZDir: float, momentInXDir: float, momentInYDir: float, momentInZDir: float):
        return self._load.AddNodalLoad(self._b.in_int_array(nodeIds), forceInXDir, forceInYDir, forceInZDir, momentInXDir, momentInYDir, momentInZDir)

    def AddSupportDisplacement(self, nodeIds: list, varDirection: int, varDispValue: float):
        return self._load.AddSupportDisplacement(self._b.in_int_array(nodeIds), varDirection, varDispValue)

    def AddMemberUniformForce(self, beamIds: list, varDirection: int, varForce: float, varD1: float, varD2: float, varD3: float):
        return self._load.AddMemberUniformForce(self._b.in_int_array(beamIds), varDirection, varForce, varD1, varD2, varD3)

    def AddMemberUniformMoment(self, beamIds: list, varDirection: int, varMoment: float, varD1: float, varD2: float, varD3: float):
        return bool(self._load.AddMemberUniformMoment(self._b.in_int_array(beamIds), varDirection, varMoment, varD1, varD2, varD3))

    def AddMemberConcForce(self, beamIds: list, varDirection: int, varForce: float, varD1: float, varD2: float):
        return bool(self._load.AddMemberConcForce(self._b.in_int_array(beamIds), varDirection, varForce, varD1, varD2))

    def AddMemberConcMoment(self, beamIds: list, varDirection: int, varMoment: float, varD1: float, varD2: float):
        return bool(self._load.AddMemberConcMoment(self._b.in_int_array(beamIds), varDirection, varMoment, varD1, varD2))

    def AddMemberLinearVari(self, memberIds: list, varDirection: int, varW1: float, varW2: float, varW3: float):
        return bool(self._load.AddMemberLinearVari(self._b.in_int_array(memberIds), varDirection, float(varW1), float(varW2), float(varW3)))

    def AddMemberTrapezoidal(self, memberIds: list, varDirection: int, varW1: float, varW2: float, varD1: float, varD2: float):
        return bool(self._load.AddMemberTrapezoidal(self._b.in_int_array(memberIds), varDirection, varW1, varW2, varD1, varD2))

    def AddMemberAreaLoad(self, beamIds: list, load: float):
        return bool(self._load.AddMemberAreaLoad(self._b.in_int_array(beamIds), load))

    def AddMemberFixedEnd(self, beamIds: list, loadStart, loadEnd):
        return bool(self._load.AddMemberFixedEnd(self._b.in_int_array(beamIds), self._b.in_double_array(loadStart), self._b.in_double_array(loadEnd)))

    def AddElementPressure(self, plateIds: list, varDirection: int, varPressure: float, varX1: float, varY1: float, varX2: float, varY2: float):
        return bool(self._load.AddElementPressure(self._b.in_int_array(plateIds), varDirection, varPressure, varX1, varY1, varX2, varY2))

    def AddElementHydrostaticPressure(self, plateIds: list, varLoadDirection: int, varInterpolateDirection: int, varMinLoad: float, varMaxLoad: float):
        return self._load.AddElementHydrostaticPressure(self._b.in_int_array(plateIds), varLoadDirection, varInterpolateDirection, varMinLoad, varMaxLoad)

    def AddTemperatureLoad(self, elementIds: list, varTempAxialElong: float, varTempDiffTopAndBtm: float, varTemDiffSide: float):
        return self._load.AddTemperatureLoad(self._b.in_int_array(elementIds), varTempAxialElong, varTempDiffTopAndBtm, varTemDiffSide) == 0

    def AddStrainLoad(self, elementIds: list, varAxialElong: float):
        return self._load.AddStrainLoad(self._b.in_int_array(elementIds), varAxialElong) == 0

    def AddLoadAndFactorToCombination(self, loadCombNo: int, loadNo: int, factor: float):
        return bool(self._load.AddLoadAndFactorToCombination(loadCombNo, loadNo, factor))

    def AddMemberFloorLoad(self, varPressure: float, varYMIN: float, varYMAX: float, varZMIN: float, varZMAX: float, varXMIN: float, varXMAX: float):
        return self._load.AddMemberFloorLoad(varPressure, varYMIN, varYMAX, varZMIN, varZMAX, varXMIN, varXMAX) == 0

    def AddMemberFloorLoadEx(self, rangeType: int, loadDirection: int, pressure: float, grpOrOneWay: int, yMIN: float, yMAX: float, zMIN: float, zMAX: float, xMIN: float, xMAX: float):
        return self._load.AddMemberFloorLoadEx(rangeType, loadDirection, pressure, grpOrOneWay, yMIN, yMAX, zMIN, zMAX, xMIN, xMAX)

    def AddElementTrapPressureEx(self, PlateIDs: list, LoadDirection: int, LoadVaryDirection: int, StartPressure: float, EndPressure: float, Pressure3: float, Pressure4: float):
        return self._load.AddElementTrapPressureEx(self._b.in_int_array(PlateIDs), LoadDirection, LoadVaryDirection, StartPressure, EndPressure, Pressure3, Pressure4)

    # ------------------------------------------------------------------ #
    # Viento
    # ------------------------------------------------------------------ #
    def AddWindDefinition(self, varTypeNo: int, varTypeName: str):
        return bool(self._load.AddWindDefinition(varTypeNo, varTypeName))

    def AddWindIntensity(self, varTypeNo: int, varIntensity: list, varHeight: list):
        intensity = self._b.in_double_array_variant(varIntensity)
        height = self._b.in_double_array_variant(varHeight)
        return bool(self._load.AddWindIntensity(varTypeNo, intensity.ref, height.ref))

    def AddWindExposure(self, varTypeNo: int, varExposureFactor: float, varNodeArray: list):
        nodes = self._b.in_int_array_variant(varNodeArray)
        return bool(self._load.AddWindExposure(varTypeNo, varExposureFactor, nodes.ref))

    def AddWindLoad(self, varTypeNo: int, varDirection: int, dFraction: float, varOpenStructure: int, dYMIN: float, dYMAX: float, dZMIN: float, dZMAX: float, dXMIN: float, dXMAX: float):
        return bool(self._load.AddWindLoad(varTypeNo, varDirection, dFraction, varOpenStructure, dYMIN, dYMAX, dZMIN, dZMAX, dXMIN, dXMAX))

    def AddWindDefinitionASCE7Parameters(self, varTypeNo: int, code: int, windSpeed: float, heightAboveSeaLvl: float, bldgclass: int, bldgtype: int, expCat: int, varEscarpment: bool, wallType: int, varIsFlexible: bool, varEscarpmentData: list, varbldgData: list, varUnitsData: list, varFactorsUserInput: list, varFactors: list):
        return bool(self._load.AddWindDefinitionASCE7Parameters(
            varTypeNo, code, windSpeed, heightAboveSeaLvl, bldgclass, bldgtype, expCat,
            varEscarpment, wallType, varIsFlexible,
            self._b.in_double_array(varEscarpmentData), self._b.in_double_array(varbldgData),
            self._b.in_double_array(varUnitsData), self._b.in_double_array(varFactorsUserInput),
            self._b.in_double_array(varFactors)
        ))

    # ------------------------------------------------------------------ #
    # Sísmica
    # ------------------------------------------------------------------ #
    def AddSeismicDefinition(self, varType: int, varAccidental: int):
        return self._load.AddSeismicDefinition(varType, varAccidental)

    def AddSeismicDefSelfWeight(self, varWeightFactor: float):
        # FIX vs oficial: el oficial llamaba a AddSeismicDefMemberWeight (método y nº de args
        # equivocados). Se corrige al método COM propio (existe, está flageado en _functions).
        return self._load.AddSeismicDefSelfWeight(varWeightFactor)

    def AddSeismicDefMemberWeight(self, varSeismicType: int, loadType: int, weight: float, startDist: float, endDist: float, memberList: list):
        return self._load.AddSeismicDefMemberWeight(varSeismicType, loadType, weight, startDist, endDist, self._b.in_int_array(memberList))

    def AddSeismicDefJointWeight(self, weight: float, nodeList: list):
        return self._load.AddSeismicDefJointWeight(weight, self._b.in_int_array(nodeList))

    def AddSeismicDefElementWeight(self, pressure: float, elementList: list):
        return self._load.AddSeismicDefElementWeight(pressure, elementList)

    def AddSeismicDefFloorWeight(self, rangeType: int, loadDirection: int, pressure: float, grpOrOneWay: int, yMIN: float, yMAX: float, zMIN: float, zMAX: float, xMIN: float, xMAX: float):
        return self._load.AddSeismicDefFloorWeight(rangeType, loadDirection, pressure, grpOrOneWay, yMIN, yMAX, zMIN, zMAX, xMIN, xMAX)

    def AddSeismicLoad(self, loadDirection: int, factor: float):
        return self._load.AddSeismicLoad(loadDirection, factor) == 0

    def AddSeismicDefWallArea(self, nTypeNo: int, direction: str, sizeArray: list):
        size = self._b.in_double_array_variant(sizeArray)
        return self._load.AddSeismicDefWallArea(nTypeNo, direction, size.ref) == 0

    def ModifySeismicDefinitionParams(self, varParamName: str, varValue: float):
        return self._load.ModifySeismicDefinitionParams(varParamName, varValue) == 0

    # ------------------------------------------------------------------ #
    # Combinaciones / repeat / envelope / referencia
    # ------------------------------------------------------------------ #
    def AddAutoLoadCombinations(self, loadCombCode: str, loadCombCategory: str, loadList: list):
        start = self._b.out_int()
        self._load.AddAutoLoadCombinations(loadCombCode, loadCombCategory, self._b.in_int_array(loadList), start.ref)
        return start.value

    def AddRepeatLoad(self, varLoadCaseList: list, varFactorList: list):
        return self._load.AddRepeatLoad(self._b.in_int_array(varLoadCaseList), self._b.in_double_array(varFactorList))

    def AddLoadCasesToEnvelop(self, varEnvNo: int, varLoadCaseList: list):
        return self._load.AddLoadCasesToEnvelop(varEnvNo, self._b.in_int_array(varLoadCaseList))

    def AddReferenceLoad(self, varRefLoadCaseNoIds: list, varFactorList: list):
        return self._load.AddReferenceLoad(self._b.in_int_array(varRefLoadCaseNoIds), self._b.in_double_array(varFactorList))

    def AddNotionalLoad(self, varPrimaryLoadCaseList: list, varPLFactorList: list, varPLDirectionList: list, varReferenceLoadCaseList: list, varRLFactorList: list, varRLDirectionList: list):
        pl = self._b.in_int_array_variant(varPrimaryLoadCaseList)
        plf = self._b.in_double_array_variant(varPLFactorList)
        pld = self._b.in_int_array_variant(varPLDirectionList)
        rl = self._b.in_int_array_variant(varReferenceLoadCaseList)
        rlf = self._b.in_double_array_variant(varRLFactorList)
        rld = self._b.in_int_array_variant(varRLDirectionList)
        self._load.AddNotionalLoad(pl.ref, plf.ref, pld.ref, rl.ref, rlf.ref, rld.ref)
        return True

    def AddDirectAnalysisDefinitionParameter(self, pParamType: int, members: list, param: float):
        return bool(self._load.AddDirectAnalysisDefinitionParameter(pParamType, self._b.in_int_array(members), param))

    def AddResponseSpectrumLoad(self, rsaCode: int, rsaCombination: int, varSet1Names: list, varSet1Vals: list, varSet2Names: list, varSet2Vals: list, varDataPairs: list):
        return self._load.AddResponseSpectrumLoadEx(
            rsaCode, rsaCombination,
            self._b.in_str_array(varSet1Names), self._b.in_double_array(varSet1Vals),
            self._b.in_str_array(varSet2Names), self._b.in_double_array(varSet2Vals),
            self._b.in_double_array(varDataPairs)
        )

    def AddAutoCombinationRepeat(self, varCode: str, varCategory: str, varLoadList: list, varStartLoadCaseNo: int, varGeneratedLCS: int, bVarReference: bool, bVarNotional: bool, dVarNotionalLoadFactor: float, bVarGB50017: bool, nVarFloor: int, bVarX: bool, bVarNegtiveX: bool, bVarZ: bool, bVarNegtiveZ: bool):
        return self._load.AddAutoCombinationRepeat(
            varCode, varCategory, self._b.in_int_array(varLoadList), varStartLoadCaseNo,
            varGeneratedLCS, bVarReference, bVarNotional, dVarNotionalLoadFactor, bVarGB50017,
            nVarFloor, bVarX, bVarNegtiveX, bVarZ, bVarNegtiveZ
        ) == 0

    def RemoveLoadCasesFromEnvelop(self, varEnvNo: int, varLoadCaseList: list):
        return bool(self._load.RemoveLoadCasesFromEnvelop(varEnvNo, self._b.in_int_array(varLoadCaseList)))

    def RemoveAttribute(self, lLoadCase: int):
        return self._load.RemoveAttribute(lLoadCase) == 0

    def ClearPrimaryLoadCase(self, varLoadCaseNos: list, isReferenceLoad: bool):
        return self._load.ClearPrimaryLoadCase(self._b.in_int_array(varLoadCaseNos), isReferenceLoad)

    def ClearReferenceLoadCase(self, varLoadCaseNos: list):
        return self._load.ClearReferenceLoadCase(self._b.in_int_array(varLoadCaseNos))

    def IsDynamicLoadIncluded(self, nLoadCase: int):
        return bool(self._load.IsDynamicLoadIncluded(nLoadCase))

    def IsCombinationCase(self, nLoadCase: int):
        return bool(self._load.IsCombinationCase(nLoadCase))

    def SplitLoadsOnBeam(self, varBeamOld: int, varBeamNew: int):
        return bool(self._load.SplitLoadsOnBeam(varBeamOld, varBeamNew))

    def MergeLoadsOnBeam(self, varBeamToKeep: int, varBeamToMerge: int):
        return bool(self._load.MergeLoadsOnBeam(varBeamToKeep, varBeamToMerge))

    def BeginLoadMerging(self):
        return self._load.BeginLoadMerging()

    def EndLoadMerging(self):
        return self._load.EndLoadMerging()

    def ComputeWallWindPressureProfile(self, loadingCode: int, windSpeed: float, bldgClass: int, bldgType: int, expCat: int, bEscarpment: bool, varUnitsData: list, varEscarpmentData: list, varBldgData: list, wallType: int):
        return self._load.ComputeWallWindPressureProfile(
            loadingCode, windSpeed, bldgClass, bldgType, expCat, int(bEscarpment),
            self._b.in_int_array(varUnitsData), self._b.in_double_array(varEscarpmentData),
            self._b.in_double_array(varBldgData), wallType
        )

    def ComputeWallWindPressureProfileASCE72016(self, windSpeed: float, heightAboveSeaLvl: float, bldgClass: int, bldgType: int, expCat: int, bEscarpment: bool, varUnitsData: list, varEscarpmentData: list, varBldgData: list, wallType: int):
        return self._load.ComputeWallWindPressureProfileASCE72016(
            windSpeed, heightAboveSeaLvl, bldgClass, bldgType, expCat, int(bEscarpment),
            self._b.in_int_array(varUnitsData), self._b.in_double_array(varEscarpmentData),
            self._b.in_double_array(varBldgData), wallType
        )

    # ------------------------------------------------------------------ #
    # Borrado
    # ------------------------------------------------------------------ #
    def DeleteLoadEnvelop(self, varEnvNo: int):
        return bool(self._load.DeleteLoadEnvelop(varEnvNo))

    def DeleteLoadList(self, varLoadListIndex: int):
        return bool(self._load.DeleteLoadList(varLoadListIndex))

    def DeletePrimaryLoadCases(self, varLoadCaseNos: list, varIsReferenceLoads: bool):
        return bool(self._load.DeletePrimaryLoadCases(self._b.in_int_array(varLoadCaseNos), varIsReferenceLoads))

    def DeleteReferenceLoadCases(self, varLoadCaseNos: list):
        return bool(self._load.DeleteReferenceLoadCases(self._b.in_int_array(varLoadCaseNos)))

    def DeleteWindDefinition(self, nTypeNo: int):
        return self._load.DeleteWindDefinition(nTypeNo) == 0

    def DeleteDirectAnalysisDefinitionParameter(self, pParamType: int):
        return self._load.DeleteDirectAnalysisDefinitionParameter(pParamType)

    def DeleteDirectAnalysisDefinition(self):
        return self._load.DeleteDirectAnalysisDefinition()

    # ------------------------------------------------------------------ #
    # Getters de casos
    # ------------------------------------------------------------------ #
    def GetPrimaryLoadCaseCount(self):
        return self._load.GetPrimaryLoadCaseCount()

    def GetPrimaryLoadCaseNumbers(self):
        n = self._load.GetPrimaryLoadCaseCount()
        ids = self._b.out_int_array(n)
        self._load.GetPrimaryLoadCaseNumbers(ids.ref)
        return ids.value

    def GetLoadCombinationCaseCount(self):
        return self._load.GetLoadCombinationCaseCount()

    def GetLoadCombinationCaseNumbers(self):
        n = self._load.GetLoadCombinationCaseCount()
        ids = self._b.out_int_array(n)
        self._load.GetLoadCombinationCaseNumbers(ids.ref)
        return ids.value

    def GetReferenceLoadCount(self):
        return self._load.GetReferenceLoadCount()

    def GetReferenceLoadCaseCount(self):
        return self._load.GetReferenceLoadCaseCount()

    def GetReferenceLoadCaseNumbers(self):
        n = self._load.GetReferenceLoadCaseCount()
        ids = self._b.out_int_array(n)
        self._load.GetReferenceLoadCaseNumbers(ids.ref)
        return ids.value

    def GetNoOfSetsInReferenceLoad(self, nIndex: int):
        return self._load.GetNoOfSetsInReferenceLoad(nIndex)

    def GetReferenceLoadByIndex(self, nIndex: int):
        n = self.GetNoOfSetsInReferenceLoad(nIndex)
        if n <= 0:
            return
        loads = self._b.out_int_array(n)
        factors = self._b.out_double_array(n)
        self._load.GetReferenceLoadByIndex(nIndex, loads.ref, factors.ref)
        return (loads.value, factors.value)

    def GetReferenceLoadType(self, varLoadNo: int):
        return self._load.GetReferenceLoadType(varLoadNo)

    def GetReferenceLoadCaseTitle(self, varLoadNo: int):
        return self._load.GetReferenceLoadCaseTitle(varLoadNo)

    def GetActiveLoad(self):
        return self._load.GetActiveLoad()

    def GetLoadCaseTitle(self, varLoadNo: int):
        return self._load.GetLoadCaseTitle(varLoadNo)

    def GetLoadType(self, varLoadNo: int):
        return self._load.GetLoadType(varLoadNo)

    # ------------------------------------------------------------------ #
    # Floor / influencia
    # ------------------------------------------------------------------ #
    def GetBeamCountAtFloor(self, varfMinX: float, varfMaxX: float, varfMinY: float, varfMaxY: float, varfMinZ: float, varfMaxZ: float, varnDirection: int):
        return self._load.GetBeamCountAtFloor(varfMinX, varfMaxX, varfMinY, varfMaxY, varfMinZ, varfMaxZ, varnDirection)

    def GetInfluenceArea(self, varfMinX: float, varfMaxX: float, varfMinY: float, varfMaxY: float, varfMinZ: float, varfMaxZ: float, varnDirection: int):
        n = self._load.GetBeamCountAtFloor(varfMinX, varfMaxX, varfMinY, varfMaxY, varfMinZ, varfMaxZ, varnDirection)
        beamIds = self._b.out_int_array(n)
        areas = self._b.out_double_array(n)
        self._load.GetInfluenceArea(varfMinX, varfMaxX, varfMinY, varfMaxY, varfMinZ, varfMaxZ, varnDirection, beamIds.ref, areas.ref)
        return {bid: area for bid, area in zip(beamIds.value, areas.value)}

    # ------------------------------------------------------------------ #
    # Cargas nodales / de miembro / de elemento (getters)
    # ------------------------------------------------------------------ #
    def GetNodalLoadCount(self, nNodeNo: int):
        return self._load.GetNodalLoadCount(nNodeNo)

    def GetNodalLoads(self, nNodeNo: int):
        n = self._load.GetNodalLoadCount(nNodeNo)
        cols = [self._b.out_double_array(n) for _ in range(6)]
        self._load.GetNodalLoads(n, *[c.ref for c in cols])
        return tuple(c.value for c in cols)

    def GetUDLLoadCount(self, nBeamNo: int):
        return self._load.GetUDLLoadCount(nBeamNo)

    def GetUDLLoads(self, nBeamNo: int):
        n = self.GetUDLLoadCount(nBeamNo)
        if n <= 0:
            return ([], [], [], [], [])
        direction = self._b.out_int_array(n)
        force = self._b.out_double_array(n)
        d1 = self._b.out_double_array(n)
        d2 = self._b.out_double_array(n)
        d3 = self._b.out_double_array(n)
        retval = self._load.GetUDLLoads(nBeamNo, direction.ref, force.ref, d1.ref, d2.ref, d3.ref)
        if not bool(retval):
            return ([], [], [], [], [])
        return (direction.value, force.value, d1.value, d2.value, d3.value)

    def GetUNIMomentCount(self, nBeamNo: int):
        return self._load.GetUNIMomentCount(nBeamNo)

    def GetUNIMoments(self, nBeamNo: int):
        n = self._load.GetUNIMomentCount(nBeamNo)
        direction = self._b.out_int_array(n)
        moment = self._b.out_double_array(n)
        d1 = self._b.out_double_array(n)
        d2 = self._b.out_double_array(n)
        d3 = self._b.out_double_array(n)
        self._load.GetUNIMoments(nBeamNo, direction.ref, moment.ref, d1.ref, d2.ref, d3.ref)
        return list(zip(direction.value, moment.value, d1.value, d2.value, d3.value))

    def GetTrapLoadCount(self, nBeamNo: int):
        return self._load.GetTrapLoadCount(nBeamNo)

    def GetTrapLoads(self, nBeamNo: int):
        n = self._load.GetTrapLoadCount(nBeamNo)
        direction = self._b.out_int_array(n)
        w1 = self._b.out_double_array(n)
        w2 = self._b.out_double_array(n)
        d1 = self._b.out_double_array(n)
        d2 = self._b.out_double_array(n)
        self._load.GetTrapLoads(nBeamNo, direction.ref, w1.ref, w2.ref, d1.ref, d2.ref)
        return list(zip(direction.value, w1.value, w2.value, d1.value, d2.value))

    def GetConcForceCount(self, nBeamNo: int):
        return self._load.GetConcForceCount(nBeamNo)

    def GetConcForces(self, nBeamNo: int):
        n = self._load.GetConcForceCount(nBeamNo)
        direction = self._b.out_int_array(n)
        force = self._b.out_double_array(n)
        d1 = self._b.out_double_array(n)
        d2 = self._b.out_double_array(n)
        self._load.GetConcForces(nBeamNo, direction.ref, force.ref, d1.ref, d2.ref)
        return list(zip(direction.value, force.value, d1.value, d2.value))

    def GetConcMomentCount(self, nBeamNo: int):
        return self._load.GetConcMomentCount(nBeamNo)

    def GetConcMoments(self, nBeamNo: int):
        # FIX vs oficial: el oficial dimensionaba con GetConcForceCount y leía con GetConcForces
        # (devolvía datos de FUERZAS, no momentos). Se corrige a los métodos de momento.
        n = self._load.GetConcMomentCount(nBeamNo)
        direction = self._b.out_int_array(n)
        moment = self._b.out_double_array(n)
        d1 = self._b.out_double_array(n)
        d2 = self._b.out_double_array(n)
        self._load.GetConcMoments(nBeamNo, direction.ref, moment.ref, d1.ref, d2.ref)
        return list(zip(direction.value, moment.value, d1.value, d2.value))

    def GetNoOfLoadAndFactorPairsForCombination(self, varLoadCombNo: int):
        return self._load.GetNoOfLoadAndFactorPairsForCombination(varLoadCombNo)

    def GetLoadAndFactorForCombination(self, varLoadCombNo: int):
        n = self._load.GetNoOfLoadAndFactorPairsForCombination(varLoadCombNo)
        ids = self._b.out_int_array(n)
        factors = self._b.out_double_array(n + 1)
        self._load.GetLoadAndFactorForCombination(varLoadCombNo, ids.ref, factors.ref)
        return (ids.value, factors.value)

    def GetElementPressureLoadCount(self, varPlateNo: int):
        return self._load.GetElementPressureLoadCount(varPlateNo)

    def GetElementPressureLoads(self, varPlateNo: int):
        n = self._load.GetElementPressureLoadCount(varPlateNo)
        direction = self._b.out_int_array(n)
        cols = [self._b.out_double_array(n) for _ in range(5)]
        self._load.GetElementPressureLoads(n, direction.ref, *[c.ref for c in cols])
        return list(zip(direction.value, *[c.value for c in cols]))

    def GetElementConcLoadCount(self, varPlateNo: int):
        return self._load.GetElementConcLoadCount(varPlateNo)

    def GetElementConcLoads(self, varPlateNo: int):
        # FIX vs oficial: el oficial dimensionaba con GetElementPressureLoadCount (conteo de
        # cargas de presión, no concentradas). Se corrige al conteo propio.
        n = self.GetElementConcLoadCount(varPlateNo)
        direction = self._b.out_int_array(n)
        cols = [self._b.out_double_array(n) for _ in range(3)]
        self._load.GetElementConcLoads(n, direction.ref, *[c.ref for c in cols])
        return list(zip(direction.value, *[c.value for c in cols]))

    # ------------------------------------------------------------------ #
    # Load lists / attributes / repeat / linear varying
    # ------------------------------------------------------------------ #
    def GetLoadListCount(self):
        return self._load.GetLoadListCount()

    def GetLoadCountInLoadList(self, varLoadListIndex: int):
        return self._load.GetLoadCountInLoadList(varLoadListIndex)

    def GetLoadsInLoadList(self, varLoadListIndex: int):
        n = self.GetLoadCountInLoadList(varLoadListIndex)
        if n == 0:
            return []
        loads = self._b.out_int_array(n)
        self._load.GetLoadsInLoadList(varLoadListIndex, loads.ref)
        return loads.value

    def GetAttribute(self, lLoadCase: int):
        self._load.GetAttribute(lLoadCase)
        return True

    def GetRepeatLoadCount(self):
        return self._load.GetRepeatLoadCount()

    def GetNoLoadFactorInRepeatLoad(self, nIndex: int):
        return self._load.GetNoLoadFactorInRepeatLoad(nIndex)

    def GetRepeatLoadByIndex(self, nIndex: int):
        n = self._load.GetNoLoadFactorInRepeatLoad(nIndex)
        loadCases = self._b.out_int_array(n)
        factors = self._b.out_double_array(n)
        self._load.GetRepeatLoadByIndex(nIndex, loadCases.ref, factors.ref)
        return {lc: f for lc, f in zip(loadCases.value, factors.value)}

    def GetLinearVaryingLoadCount(self, nBeamNo: int):
        return self._load.GetLinearVaryingLoadCount(nBeamNo)

    def GetLinearVaryingLoads(self, nBeamNo: int):
        n = self._load.GetLinearVaryingLoadCount(nBeamNo)
        direction = self._b.out_int_array(n)
        w1 = self._b.out_double_array(n)
        w2 = self._b.out_double_array(n)
        w3 = self._b.out_double_array(n)
        self._load.GetLinearVaryingLoads(n, direction.ref, w1.ref, w2.ref, w3.ref)
        return list(zip(direction.value, w1.value, w2.value, w3.value))

    def GetLoadTypeCount(self, loadType: int):
        return self._load.GetLoadTypeCount(loadType)

    def GetListSizeForLoadType(self, loadType: int, loadIndex: int):
        return self._load.GetListSizeForLoadType(loadType, loadIndex)

    def GetAssignmentListForLoadType(self, loadType: int, loadIndex: int):
        size = self.GetListSizeForLoadType(loadType, loadIndex)
        if size < 1:
            return []
        entities = self._b.out_int_array(size)
        retval = self._load.GetAssignmentListForLoadType(loadType, loadIndex, entities.ref)
        if retval == 0:
            return []
        return entities.value

    def GetNodalLoadInfo(self, loadIndex: int):
        forces = self._b.out_double_array(6)
        self._load.GetNodalLoadInfo(loadIndex, forces.ref)
        return forces.value

    def GetMemberLoadInfo(self, loadIndex: int):
        direction = self._b.out_int()
        force = self._b.out_double_array(3)
        distance = self._b.out_double_array(3)
        retval = self._load.GetMemberLoadInfo(loadIndex, direction.ref, force.ref, distance.ref)
        if not bool(retval):
            return (0, [0, 0, 0], [0, 0, 0])
        return (direction.value, force.value, distance.value)

    def GetElementLoadInfo(self, loadIndex: int):
        direction = self._b.out_int()
        force = self._b.out_double_array(4)
        distance = self._b.out_double_array(4)
        self._load.GetElementLoadInfo(loadIndex, direction.ref, force.ref, distance.ref)
        return [direction.value, force.value, distance.value]

    # ------------------------------------------------------------------ #
    # Notional / items / envelope
    # ------------------------------------------------------------------ #
    def GetNotionalLoadCount(self):
        return self._load.GetNotionalLoadCount()

    def GetNoLoadFactorDirectionInNotionalLoad(self, nIndex: int):
        return self._load.GetNoLoadFactorDirectionInNotionalLoad(nIndex)

    def GetNotionalLoadByIndex(self, nIndex: int):
        # FIX vs oficial: el oficial llamaba a GetElementLoadInfo (método COM equivocado) con el
        # count como primer arg. Se corrige al método propio GetNotionalLoadByIndex con nIndex.
        # OJO: el orden/tipos de los out-params (loadCase, factor, direction) es la conjetura más
        # razonable pero NO está verificado contra la firma COM real -> confirmar en Windows.
        n = self._load.GetNoLoadFactorDirectionInNotionalLoad(nIndex)
        loadCase = self._b.out_int_array(n)
        factor = self._b.out_double_array(n)
        direction = self._b.out_int_array(n)
        self._load.GetNotionalLoadByIndex(nIndex, loadCase.ref, factor.ref, direction.ref)
        return list(zip(direction.value, loadCase.value, factor.value))

    def GetLoadItemsCount(self, loadCaseNo: int):
        return self._load.GetLoadItemsCount(loadCaseNo)

    def GetLoadItemType(self, loadCaseNo: int, loadItemIndex: int):
        return self._load.GetLoadItemType(loadCaseNo, loadItemIndex)

    def GetEnvelopeCount(self):
        return self._load.GetEnvelopeCount()

    def GetLoadEnvelopeDetails(self, EnvNo: int):
        envType = self._b.out_int()
        numCases = self._b.out_int()
        self._load.GetLoadEnvelopeDetails(EnvNo, envType.ref, numCases.ref)
        return (envType.value, numCases.value)

    def GetLoadListfromLoadEnvelope(self, EnvNo: int):
        _envType, numCases = self.GetLoadEnvelopeDetails(EnvNo)
        loads = self._b.out_int_array(numCases)
        self._load.GetLoadListfromLoadEnvelope(EnvNo, loads.ref)
        return loads.value

    def GetEnvelopeIDs(self):
        n = self._load.GetEnvelopeCount()
        ids = self._b.out_int_array(n)
        self._load.GetEnvelopeIDs(ids.ref)
        return ids.value
