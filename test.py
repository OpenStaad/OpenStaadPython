
def test():
    print("Hello World!")

    ## FILE FUNCTIONS
    print(root.GetAnalysisStatus())
    print(root.GetApplicationVersion())
    print(root.GetBaseUnit())
    print(root.GetInputUnitForForce())
    print(root.GetInputUnitForLength())
    print(root.GetSTAADFile())
    print(root.GetSTAADFile(bFullPath=False))
    print(root.GetSTAADFileFolder())

    ## GEOMETRY - NODE

    node_1 = 10
    node_2 = 20
    cordidinates = (0.0, 104.35, 0.0)

    print(geometry.GetLastNodeNo())
    print(geometry.GetNodeCoordinates(node_1))
    print(geometry.GetNodeCount())
    print(geometry.GetNodeDistance(node_1,node_2))
    print(geometry.GetNodeIncidence(node_1))
    print(geometry.GetNodeList()[0:10])
    print(geometry.GetNodeNumber(cordidinates))
    print(geometry.GetNoOfSelectedNodes())
    print(geometry.GetSelectedNodes()[0:10])

    ## GEOMETRY - BEAM

    print("\nBEAM FUNCTIONS\n")

    beam_1 = 10

    print(geometry.GetBeamLength(beam_1))
    print(geometry.GetBeamList()[0:10])
    print(geometry.GetLastBeamNo())
    print(geometry.GetMemberCount())
    print(geometry.GetMemberIncidence(beam_1))
    print(geometry.GetNoOfSelectedBeams())
    print(geometry.GetSelectedBeams()[0:10])
    print(geometry.GetNoOfBeamsConnectedAtNode(node_1))
    print(geometry.GetBeamsConnectedAtNode(node_1))

    ## GEOMETRY - GROUP

    print("\nGROUP FUNCTIONS\n")

    group_1 = '_SOME_GROUPU'

    print(geometry.GetGroupEntityCount(group_1))
    print(geometry.GetGroupEntities(group_1)[0:10])

    ## PROPERTIES FUNCTIONS

    print("\nPROPERTIES FUNCTIONS\n")

    beam_1 = 10

    print(properties.GetBeamSectionName(beam_1))
    print(properties.GetBeamSectionPropertyRefNo(beam_1))
    print(properties.GetSectionPropertyValues(4))
    print(properties.GetMemberSpecCode(424))


    ## OUTPUT FUNCTIONS

    print("\nOUTPUT FUNCTIONS\n")

    beam_1 = 384
    node = 1
    # print(get.results.GetMemberEndForces(beam=beam_1, start=False, lc=5001, local = 1))
    # print(get.results.GetMemberEndForces(beam=beam_1, start=False, lc=5001, local = 0))
    # print(get.results.GetSupportReactions(node))
    print(load.GetLoadCaseTitle(lc=1))



if __name__ == "__main__":
    from openstaad import *

    geometry = Geometry()
    load = Load()
    output = Output()
    properties = Properties()
    root = Root()
    view = View()

