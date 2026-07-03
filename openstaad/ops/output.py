"""
output.py — dominio Output (resultados de análisis) del subpaquete ops, sobre bridge.

Métodos alineados al comportamiento del oficial (PascalCase). Se omiten los
`raise_os_error_if_error_code`; se conservan los condicionales que son lógica de
retorno. Las unidades de salida usan el estilo BSTR-byref (out_bstr).
"""

from .bridge import Bridge
from ._com import acquire


class Output:
    def __init__(self, connection=None, bridge=None, filePath=None):
        staad = connection if connection is not None else acquire(filePath)
        self._b = bridge if bridge is not None else Bridge()
        self._output = staad.Output

        # Algunos métodos necesitan el conteo de soportes (de Support).
        self._support_com = staad.Support
        self._support_com._FlagAsMethod("GetSupportCount")

        self._functions = [
            "GetOutputUnitForDimension", "GetOutputUnitForSectDimension",
            "GetOutputUnitForSectArea", "GetOutputUnitForSectInertia",
            "GetOutputUnitForSectModulus", "GetOutputUnitForDensity",
            "GetOutputUnitForDisplacement", "GetOutputUnitForRotation",
            "GetOutputUnitForForce", "GetOutputUnitForMoment", "GetOutputUnitForDistForce",
            "GetOutputUnitForDistMoment", "GetOutputUnitForStress", "GetNodeDisplacements",
            "GetSupportReactions", "GetMemberEndDisplacements", "GetMemberEndForces",
            "GetAllPlateCenterStressesAndMoments", "GetPlateCenterNormalPrincipalStresses",
            "GetAllPlateCenterForces", "GetAllPlateCenterMoments", "GetAllSolidNormalStresses",
            "GetMemberSteelDesignRatio", "GetMinMaxBendingMoment", "GetMinMaxShearForce",
            "GetMinMaxAxialForce", "GetMaxSectionDisplacement", "GetMaxBeamStresses",
            "GetIntermediateMemberTransDisplacements",
            "GetAllPlateCenterPrincipalStressesAndAngles", "GetPlateCenterVonMisesStresses",
            "GetAllSolidShearStresses", "GetAllSolidPrincipalStresses",
            "GetAllSolidVonMisesStresses", "GetIntermediateMemberForcesAtDistance",
            "GetIntermediateDeflectionAtDistance", "GetPlateCornerForces",
            "GetMemberDesignSectionName", "AreResultsAvailable", "GetNLLoadStep",
            "GetNLNodeDisplacements", "GetIntermediateMemberAbsTransDisplacements",
            "GetNoOfModesExtracted", "GetModeFrequency", "GetModalDisplacementAtNode",
            "GetModalMassParticipationFactors", "GetStaticCheckResult", "GetMatInfluenceAreas",
            "GetBasePressures", "IsBucklingAnalysisResultsAvailable", "GetNoOfBucklingFactors",
            "GetBucklingFactor", "GetBucklingModeDisplacementAtNode",
            "GetResultantForceAlongLineForPlateList",
            "GetResultantForceAlongLineForParametricSurface", "GetPlateStressAtPoint",
            "GetTimeHistoryIntegrationStepInfo", "GetTimeHistoryResponseAtTime",
            "GetTimeHistoryResponse", "GetTimeHistoryResponseMinMax",
            "GetMemberSteelDesignResults", "GetMemberSteelDesignMinFailureRatio",
            "GetMemberSteelDesignMaxFailureRatio", "IsMultipleMemberSteelDesignResultsAvailable",
            "GetSteelDesignParameterBlockCount", "GetSteelDesignParameterBlockNameByIndex",
            "GetMultipleMemberSteelDesignRatio", "GetMultipleMemberSteelDesignResults",
            "GetMultipleMemberSteelDesignMaxRatio",
            "GetAllPlateCenterPrincipalStressesAndAnglesEx", "GetPMemberEndForces",
            "GetPMemberIntermediateForcesAtDistance",
        ]
        for function_name in self._functions:
            self._output._FlagAsMethod(function_name)

    # ------------------------------------------------------------------ #
    # Unidades de salida (BSTR-byref)
    # ------------------------------------------------------------------ #
    def _unit(self, com_method):
        u = self._b.out_bstr()
        com_method(u.ref)
        return u.value

    def GetOutputUnitForDimension(self):
        return self._unit(self._output.GetOutputUnitForDimension)

    def GetOutputUnitForSectDimension(self):
        return self._unit(self._output.GetOutputUnitForSectDimension)

    def GetOutputUnitForSectArea(self):
        return self._unit(self._output.GetOutputUnitForSectArea)

    def GetOutputUnitForSectInertia(self):
        return self._unit(self._output.GetOutputUnitForSectInertia)

    def GetOutputUnitForSectModulus(self):
        return self._unit(self._output.GetOutputUnitForSectModulus)

    def GetOutputUnitForDensity(self):
        return self._unit(self._output.GetOutputUnitForDensity)

    def GetOutputUnitForDisplacement(self):
        return self._unit(self._output.GetOutputUnitForDisplacement)

    def GetOutputUnitForRotation(self):
        return self._unit(self._output.GetOutputUnitForRotation)

    def GetOutputUnitForForce(self):
        return self._unit(self._output.GetOutputUnitForForce)

    def GetOutputUnitForMoment(self):
        return self._unit(self._output.GetOutputUnitForMoment)

    def GetOutputUnitForDistForce(self):
        return self._unit(self._output.GetOutputUnitForDistForce)

    def GetOutputUnitForDistMoment(self):
        return self._unit(self._output.GetOutputUnitForDistMoment)

    def GetOutputUnitForStress(self):
        return self._unit(self._output.GetOutputUnitForStress)

    # ------------------------------------------------------------------ #
    # Desplazamientos / reacciones / fuerzas
    # ------------------------------------------------------------------ #
    def GetNodeDisplacements(self, nodeNo: int, loadCaseNo: int):
        disp = self._b.out_double_array(6)
        self._output.GetNodeDisplacements(nodeNo, loadCaseNo, disp.ref)
        return disp.value

    def GetSupportReactions(self, nodeNo: int, loadCaseNo: int):
        reactions = self._b.out_double_array(6)
        self._output.GetSupportReactions(nodeNo, loadCaseNo, reactions.ref)
        return reactions.value

    def GetMemberEndDisplacements(self, memberNo: int, end: int, loadCaseNo: int):
        disp = self._b.out_double_array(6)
        self._output.GetMemberEndDisplacements(memberNo, end, loadCaseNo, disp.ref)
        return disp.value

    def GetMemberEndForces(self, memberNo: int, end: int, loadCaseNo: int, LocalOrGlobal: int):
        forces = self._b.out_double_array(6)
        self._output.GetMemberEndForces(memberNo, end, loadCaseNo, forces.ref, LocalOrGlobal)
        return forces.value

    def GetIntermediateMemberTransDisplacements(self, memberNo: int, distance, loadCaseNo: int):
        disp = self._b.out_double_array(6)
        self._output.GetIntermediateMemberTransDisplacements(memberNo, distance, loadCaseNo, disp.ref)
        return disp.value

    def GetIntermediateMemberForcesAtDistance(self, memberNo: int, distance: float, loadCaseNo: int):
        forces = self._b.out_double_array(6)
        self._output.GetIntermediateMemberForcesAtDistance(memberNo, distance, loadCaseNo, forces.ref)
        return forces.value

    def GetIntermediateMemberAbsTransDisplacements(self, memberNo: int, distance: float, loadCaseNo: int):
        disp = self._b.out_double_array(6)
        self._output.GetIntermediateMemberAbsTransDisplacements(memberNo, distance, loadCaseNo, disp.ref)
        return disp.value

    def GetIntermediateDeflectionAtDistance(self, memberNo: int, distance, loadCaseNo: int):
        dy = self._b.out_double()
        dz = self._b.out_double()
        self._output.GetIntermediateDeflectionAtDistance(memberNo, distance, loadCaseNo, dy.ref, dz.ref)
        return (dy.value, dz.value)

    def GetPlateCornerForces(self, plateNo: int, cornerCode: int, loadCaseNo: int):
        forces = self._b.out_double_array(6)
        self._output.GetPlateCornerForces(plateNo, cornerCode, loadCaseNo, forces.ref)
        return forces.value

    def GetPMemberEndForces(self, memberNo: int, end: int, loadCaseNo: int, LocalOrGlobal: int):
        forces = self._b.out_double_array(6)
        self._output.GetPMemberEndForces(memberNo, end, loadCaseNo, forces.ref, LocalOrGlobal)
        return forces.value

    def GetPMemberIntermediateForcesAtDistance(self, memberNo: int, distance, loadCaseNo: int):
        forces = self._b.out_double_array(6)
        self._output.GetPMemberIntermediateForcesAtDistance(memberNo, distance, loadCaseNo, forces.ref)
        return forces.value

    # ------------------------------------------------------------------ #
    # Placas / sólidos
    # ------------------------------------------------------------------ #
    def GetAllPlateCenterStressesAndMoments(self, plateNo: int, loadCaseNo: int):
        vals = self._b.out_double_array(8)
        self._output.GetAllPlateCenterStressesAndMoments(plateNo, loadCaseNo, vals.ref)
        return vals.value

    def GetPlateCenterNormalPrincipalStresses(self, plateNo: int, loadCaseNo: int):
        smax_t = self._b.out_double()
        smin_t = self._b.out_double()
        smax_b = self._b.out_double()
        smin_b = self._b.out_double()
        self._output.GetPlateCenterNormalPrincipalStresses(
            plateNo, loadCaseNo, smax_t.ref, smin_t.ref, smax_b.ref, smin_b.ref
        )
        return (smax_t.value, smin_t.value, smax_b.value, smin_b.value)

    def GetAllPlateCenterForces(self, plateNo: int, loadCaseNo: int):
        forces = self._b.out_double_array(5)
        self._output.GetAllPlateCenterForces(plateNo, loadCaseNo, forces.ref)
        return forces.value

    def GetAllPlateCenterMoments(self, plateNo: int, loadCaseNo: int):
        moments = self._b.out_double_array(3)
        self._output.GetAllPlateCenterMoments(plateNo, loadCaseNo, moments.ref)
        return moments.value

    def GetAllPlateCenterPrincipalStressesAndAngles(self, plateNo: int, loadCaseNo: int):
        vals = self._b.out_double_array(8)
        self._output.GetAllPlateCenterPrincipalStressesAndAngles(plateNo, loadCaseNo, vals.ref)
        return vals.value

    def GetPlateCenterVonMisesStresses(self, plateNo: int, loadCaseNo: int):
        vt = self._b.out_double()
        vb = self._b.out_double()
        self._output.GetPlateCenterVonMisesStresses(plateNo, loadCaseNo, vt.ref, vb.ref)
        return (vt.value, vb.value)

    def GetAllPlateCenterPrincipalStressesAndAnglesEx(self, plateNo: int, loadCaseNo: int):
        stresses = self._b.out_double_array(6)
        angles = self._b.out_double_array(2)
        self._output.GetAllPlateCenterPrincipalStressesAndAnglesEx(plateNo, loadCaseNo, stresses.ref, angles.ref)
        return (stresses.value, angles.value)

    def GetAllSolidNormalStresses(self, nSolidNo: int, nCorner: int, loadCaseNo: int):
        vals = self._b.out_double_array(3)
        self._output.GetAllSolidNormalStresses(nSolidNo, nCorner, loadCaseNo, vals.ref)
        return vals.value

    def GetAllSolidShearStresses(self, nSolidNo: int, nCorner: int, loadCaseNo: int):
        vals = self._b.out_double_array(3)
        self._output.GetAllSolidShearStresses(nSolidNo, nCorner, loadCaseNo, vals.ref)
        return vals.value

    def GetAllSolidPrincipalStresses(self, nSolidNo: int, nCorner: int, loadCaseNo: int):
        vals = self._b.out_double_array(3)
        self._output.GetAllSolidPrincipalStresses(nSolidNo, nCorner, loadCaseNo, vals.ref)
        return vals.value

    def GetAllSolidVonMisesStresses(self, nSolidNo: int, nCorner: int, loadCaseNo: int):
        val = self._b.out_double()
        self._output.GetAllSolidVonMisesStresses(nSolidNo, nCorner, loadCaseNo, val.ref)
        return val.value

    def GetPlateStressAtPoint(self, plateNo: int, loadNo: int, stressPoint: list, facingPoint):
        sp = self._b.in_double_array_variant(stressPoint)
        fp = self._b.in_double_array_variant(facingPoint)
        stresses = self._b.out_double_array(32)
        self._output.GetPlateStressAtPoint(plateNo, loadNo, sp.ref, fp.ref, stresses.ref)
        return stresses.value

    # ------------------------------------------------------------------ #
    # Diseño en acero / min-max / misceláneos
    # ------------------------------------------------------------------ #
    def GetMemberSteelDesignRatio(self, beamNo: int):
        ratio = self._b.out_double()
        self._output.GetMemberSteelDesignRatio(beamNo, ratio.ref)
        return ratio.value

    def _min_max_4(self, com_method, *args):
        dMin = self._b.out_double()
        dMinPos = self._b.out_double()
        dMax = self._b.out_double()
        dMaxPos = self._b.out_double()
        com_method(*args, dMin.ref, dMinPos.ref, dMax.ref, dMaxPos.ref)
        return (dMin.value, dMinPos.value, dMax.value, dMaxPos.value)

    def GetMinMaxBendingMoment(self, memberNo: int, dir: str, loadCaseNo: int):
        return self._min_max_4(self._output.GetMinMaxBendingMoment, memberNo, dir, loadCaseNo)

    def GetMinMaxShearForce(self, memberNo: int, dir: str, loadCaseNo: int):
        return self._min_max_4(self._output.GetMinMaxShearForce, memberNo, dir, loadCaseNo)

    def GetMinMaxAxialForce(self, memberNo: int, loadCaseNo: int):
        return self._min_max_4(self._output.GetMinMaxAxialForce, memberNo, loadCaseNo)

    def GetMaxSectionDisplacement(self, memberNo: int, dir: str, loadCaseNo: int):
        dMax = self._b.out_double()
        dMaxPos = self._b.out_double()
        self._output.GetMaxSectionDisplacement(memberNo, dir, loadCaseNo, dMax.ref, dMaxPos.ref)
        return (dMax.value, dMaxPos.value)

    def GetMaxBeamStresses(self, beamNo: int, loadCaseNo: int):
        compStress = self._b.out_double()
        compCorner = self._b.out_int()
        tensileStress = self._b.out_double()
        tensileCorner = self._b.out_int()
        self._output.GetMaxBeamStresses(beamNo, loadCaseNo, compStress.ref, compCorner.ref, tensileStress.ref, tensileCorner.ref)
        return (compStress.value, compCorner.value, tensileStress.value, tensileCorner.value)

    def GetMemberDesignSectionName(self, beamNo: int):
        return str(self._output.GetMemberDesignSectionName(beamNo))

    def AreResultsAvailable(self):
        return bool(self._output.AreResultsAvailable())

    def GetNLLoadStep(self, loadCaseNo: int):
        return int(self._output.GetNLLoadStep(loadCaseNo))

    def GetNLNodeDisplacements(self, nodeNo: int, loadCaseNo: int, loadStep: int):
        loadLevel = self._b.out_double()
        disp = self._b.out_double_array(6)
        self._output.GetNLNodeDisplacements(nodeNo, loadCaseNo, loadStep, loadLevel.ref, disp.ref)
        return (loadLevel.value, disp.value)

    # ------------------------------------------------------------------ #
    # Modos / dinámica
    # ------------------------------------------------------------------ #
    def GetNoOfModesExtracted(self):
        return self._output.GetNoOfModesExtracted()

    def GetModeFrequency(self, modeNo: int):
        freq = self._b.out_double()
        self._output.GetModeFrequency(modeNo, freq.ref)
        return float(freq.value)

    def GetModalDisplacementAtNode(self, modeNo: int, nodeNo: int):
        disp = self._b.out_double_array(6)
        self._output.GetModalDisplacementAtNode(modeNo, nodeNo, disp.ref)
        return disp.value

    def GetModalMassParticipationFactors(self, modeNo: int):
        px = self._b.out_double()
        py = self._b.out_double()
        pz = self._b.out_double()
        self._output.GetModalMassParticipationFactors(modeNo, px.ref, py.ref, pz.ref)
        return (float(px.value), float(py.value), float(pz.value))

    def GetStaticCheckResult(self, loadCaseNo: int):
        loads = self._b.out_double_array(6)
        reaction = self._b.out_double_array(6)
        self._output.GetStaticCheckResult(loadCaseNo, loads.ref, reaction.ref)
        return (loads.value, reaction.value)

    # ------------------------------------------------------------------ #
    # Mat / presiones de base
    # ------------------------------------------------------------------ #
    def GetMatInfluenceAreas(self, nodelist: list):
        count = self._support_com.GetSupportCount()
        yz = self._b.out_double_array(count)
        zx = self._b.out_double_array(count)
        xy = self._b.out_double_array(count)
        nodes = self._b.in_int_array_variant(nodelist)
        self._output.GetMatInfluenceAreas(nodes.ref, yz.ref, zx.ref, xy.ref)
        return (yz.value, zx.value, xy.value)

    def GetBasePressures(self, loadCaseNo: int, nodelist: list):
        count = self._support_com.GetSupportCount()
        x = self._b.out_double_array(count)
        y = self._b.out_double_array(count)
        z = self._b.out_double_array(count)
        nodes = self._b.in_int_array_variant(nodelist)
        self._output.GetBasePressures(loadCaseNo, nodes.ref, x.ref, y.ref, z.ref)
        return (x.value, y.value, z.value)

    # ------------------------------------------------------------------ #
    # Pandeo
    # ------------------------------------------------------------------ #
    def IsBucklingAnalysisResultsAvailable(self):
        return bool(self._output.IsBucklingAnalysisResultsAvailable())

    def GetNoOfBucklingFactors(self):
        return self._output.GetNoOfBucklingFactors()

    def GetBucklingFactor(self, buckling_mode_no: int):
        lam = self._b.out_double()
        self._output.GetBucklingFactor(buckling_mode_no, lam.ref)
        return lam.value

    def GetBucklingModeDisplacementAtNode(self, buckling_mode_no: int, node_no: int):
        disp = self._b.out_double_array(6)
        self._output.GetBucklingModeDisplacementAtNode(buckling_mode_no, node_no, disp.ref)
        return disp.value

    # ------------------------------------------------------------------ #
    # Resultantes a lo largo de línea
    # ------------------------------------------------------------------ #
    def GetResultantForceAlongLineForPlateList(self, plateList: list, nplates: int, loadIdList: list, startNode: list, endNode: list, isTransformForceToGlobal: int, firstNode: int, secondNode: int, thirdNode: int):
        res = self._b.out_double_array(6)
        plates = self._b.in_int_array_variant(plateList)
        loads = self._b.in_int_array_variant(loadIdList)
        start = self._b.in_double_array_variant(startNode)
        end = self._b.in_double_array_variant(endNode)
        self._output.GetResultantForceAlongLineForPlateList(
            plates.ref, nplates, loads.ref, start.ref, end.ref,
            isTransformForceToGlobal, firstNode, secondNode, thirdNode, res.ref
        )
        return res.value

    def GetResultantForceAlongLineForParametricSurface(self, parametricSurfaceName: str, nplates: int, loadId: int, startNode: list, endNode: list, facingNode: list, isTransformForceToGlobal: int, firstNode: int, secondNode: int, thirdNode: int):
        res = self._b.out_double_array(6)
        start = self._b.in_int_array_variant(startNode)
        end = self._b.in_int_array_variant(endNode)
        facing = self._b.in_int_array_variant(facingNode)
        self._output.GetResultantForceAlongLineForParametricSurface(
            parametricSurfaceName, nplates, loadId, start.ref, end.ref, facing.ref,
            isTransformForceToGlobal, firstNode, secondNode, thirdNode, res.ref
        )
        return res.value

    # ------------------------------------------------------------------ #
    # Time history
    # ------------------------------------------------------------------ #
    def GetTimeHistoryIntegrationStepInfo(self):
        timeStep = self._b.out_double()
        nsteps = self._output.GetTimeHistoryIntegrationStepInfo(timeStep.ref)
        return (float(timeStep.value), nsteps)

    def GetTimeHistoryResponseAtTime(self, load_case: int, node_no: int, dof_no: int, response_type: int, at_time: float):
        response = self._b.out_double()
        result = self._output.GetTimeHistoryResponseAtTime(load_case, node_no, dof_no, response_type, at_time, response.ref)
        return (response.value, result)

    def GetTimeHistoryResponse(self, load_case: int, node_no: int, dof_no: int, response_type: int):
        _delta, nsteps = self.GetTimeHistoryIntegrationStepInfo()
        response = self._b.out_double_array(nsteps)
        self._output.GetTimeHistoryResponse(load_case, node_no, dof_no, response_type, response.ref)
        return response.value

    def GetTimeHistoryResponseMinMax(self, load_case: int, node_no: int, dof_no: int, response_type: int):
        respMax = self._b.out_double()
        timeMax = self._b.out_double()
        respMin = self._b.out_double()
        timeMin = self._b.out_double()
        self._output.GetTimeHistoryResponseMinMax(
            load_case, node_no, dof_no, response_type, respMax.ref, timeMax.ref, respMin.ref, timeMin.ref
        )
        return (respMax.value, timeMax.value, respMin.value, timeMin.value)

    # ------------------------------------------------------------------ #
    # Resultados de diseño en acero (mixtos BSTR + escalares + array)
    # ------------------------------------------------------------------ #
    def GetMemberSteelDesignResults(self, beamNo: int):
        designcode = self._b.out_bstr()
        designstatus = self._b.out_bstr()
        criticalratio = self._b.out_double()
        allowableratio = self._b.out_double()
        criticalloadcase = self._b.out_int()
        criticalsection = self._b.out_double()
        criticalclause = self._b.out_bstr()
        designsection = self._b.out_bstr()
        designforce = self._b.out_double_array(3)
        klbyr = self._b.out_double()
        self._output.GetMemberSteelDesignResults(
            beamNo, designcode.ref, designstatus.ref, criticalratio.ref, allowableratio.ref,
            criticalloadcase.ref, criticalsection.ref, criticalclause.ref, designsection.ref,
            designforce.ref, klbyr.ref
        )
        return (designcode.value, designstatus.value, criticalratio.value, allowableratio.value,
                criticalloadcase.value, criticalsection.value, criticalclause.value,
                designsection.value, designforce.value, klbyr.value)

    def GetMemberSteelDesignMinFailureRatio(self):
        ratio = self._b.out_double()
        self._output.GetMemberSteelDesignMinFailureRatio(ratio.ref)
        return ratio.value

    def GetMemberSteelDesignMaxFailureRatio(self):
        ratio = self._b.out_double()
        self._output.GetMemberSteelDesignMaxFailureRatio(ratio.ref)
        return ratio.value

    def IsMultipleMemberSteelDesignResultsAvailable(self):
        return bool(self._output.IsMultipleMemberSteelDesignResultsAvailable())

    def GetSteelDesignParameterBlockCount(self):
        return self._output.GetSteelDesignParameterBlockCount()

    def GetSteelDesignParameterBlockNameByIndex(self, index: int):
        name = self._b.out_bstr()
        self._output.GetSteelDesignParameterBlockNameByIndex(index, name.ref)
        return name.value

    def GetMultipleMemberSteelDesignRatio(self, param_blk_name: str, beam_no: int):
        ratio = self._b.out_double()
        self._output.GetMultipleMemberSteelDesignRatio(param_blk_name, beam_no, ratio.ref)
        return ratio.value

    def GetMultipleMemberSteelDesignResults(self, param_blk_name: str, beam_no: int):
        designcode = self._b.out_bstr()
        designstatus = self._b.out_bstr()
        criticalratio = self._b.out_double()
        allowableratio = self._b.out_double()
        criticalloadcase = self._b.out_int()
        criticalclause = self._b.out_bstr()
        designsection = self._b.out_bstr()
        self._output.GetMultipleMemberSteelDesignResults(
            param_blk_name, beam_no, designcode.ref, designstatus.ref, criticalratio.ref,
            allowableratio.ref, criticalloadcase.ref, criticalclause.ref, designsection.ref
        )
        return (designcode.value, designstatus.value, criticalratio.value, allowableratio.value,
                criticalloadcase.value, criticalclause.value, designsection.value)

    def GetMultipleMemberSteelDesignMaxRatio(self, beamNo: int):
        ratio = self._b.out_double()
        self._output.GetMultipleMemberSteelDesignMaxRatio(beamNo, ratio.ref)
        return ratio.value
