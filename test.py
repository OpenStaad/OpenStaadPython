
def test():
    print("Hello World!")

    ## FILE FUNCTIONS
    print(get.file.GetAnalysisStatus())
    print(get.file.GetApplicationVersion())
    print(get.file.GetBaseUnit())
    print(get.file.GetInputUnitForForce())
    print(get.file.GetInputUnitForLength())
    print(get.file.GetSTAADFile())
    print(get.file.GetSTAADFile(bFullPath=False))
    print(get.file.GetSTAADFileFolder())

    ## GEOMETRY - NODE

    node_1 = 10
    node_2 = 20
    cordidinates = (0.0, 104.35, 0.0)

    print(get.geometry.GetLastNodeNo())
    print(get.geometry.GetNodeCoordinates(node_1))
    print(get.geometry.GetNodeCount())
    print(get.geometry.GetNodeDistance(node_1,node_2))
    print(get.geometry.GetNodeIncidence(node_1))
    print(get.geometry.GetNodeList()[0:10])
    print(get.geometry.GetNodeNumber(cordidinates))
    print(get.geometry.GetNoOfSelectedNodes())
    print(get.geometry.GetSelectedNodes()[0:10])

    ## GEOMETRY - BEAM

    print("\nBEAM FUNCTIONS\n")

    beam_1 = 10

    print(get.geometry.GetBeamLength(beam_1))
    print(get.geometry.GetBeamList()[0:10])
    print(get.geometry.GetLastBeamNo())
    print(get.geometry.GetMemberCount())
    print(get.geometry.GetMemberIncidence(beam_1))
    print(get.geometry.GetNoOfSelectedBeams())
    print(get.geometry.GetSelectedBeams()[0:10])
    print(get.geometry.GetNoOfBeamsConnectedAtNode(node_1))
    print(get.geometry.GetBeamsConnectedAtNode(node_1))

    ## GEOMETRY - GROUP

    print("\nGROUP FUNCTIONS\n")

    group_1 = '_SOME_GROUPU'

    print(get.geometry.GetGroupEntityCount(group_1))
    print(get.geometry.GetGroupEntities(group_1)[0:10])

    ## PROPERTIES FUNCTIONS

    print("\nPROPERTIES FUNCTIONS\n")

    beam_1 = 10

    print(get.properties.GetBeamSectionName(beam_1))
    print(get.properties.GetBeamSectionPropertyRefNo(beam_1))
    print(get.properties.GetSectionPropertyValues(4))
    print(get.properties.GetMemberSpecCode(424))


    ## OUTPUT FUNCTIONS

    print("\nOUTPUT FUNCTIONS\n")

    beam_1 = 384
    node = 1
    # print(get.results.GetMemberEndForces(beam=beam_1, start=False, lc=5001, local = 1))
    # print(get.results.GetMemberEndForces(beam=beam_1, start=False, lc=5001, local = 0))
    # print(get.results.GetSupportReactions(node))
    print(get.load.GetLoadCaseTitle(lc=1))



if __name__ == "__main__":
    from openstaad.get import Get

    get = Get() 
    
    test()