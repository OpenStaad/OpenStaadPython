
from openstaad import *

geometry    = Geometry()
load        = Load()
output      = Output()
properties  = Properties()
root        = Root()
view        = View()


print("Start Testing...")
print('-'*20+'\nGeometry node Functions\n'+'-'*20)

## GEOMETRY - NODE
node_1 = 1
node_2 = 2
cordidinates = (0.0, 0, 0.0)
print('- GetLastNodeNo')
print(geometry.GetLastNodeNo())

print('- GetNodeCoordinates')
print(geometry.GetNodeCoordinates(node_1))

print('- GetNodeCount')
print(geometry.GetNodeCount())

print('- GetNodeDistance')
print(geometry.GetNodeDistance(node_1,node_2))

print('- GetNodeIncidence')
print(geometry.GetNodeIncidence(node_1))

print('- GetNodeList')
print(geometry.GetNodeList()[0:10])

print('- GetNodeNumber')
print(geometry.GetNodeNumber(cordidinates))

print('- GetNoOfSelectedNodes')
print(geometry.GetNoOfSelectedNodes())

print('- GetSelectedNodes')
print(geometry.GetSelectedNodes()[0:10])

# ## GEOMETRY - BEAM

print('-'*20+'\nGeometry beam Functions\n'+'-'*20)

beam_1 = 1
print('- GetBeamLength')
print(geometry.GetBeamLength(beam_1))

print('- GetBeamList')
print(geometry.GetBeamList()[0:10])

print('- GetLastBeamNo')
print(geometry.GetLastBeamNo())

print('- GetMemberCount')
print(geometry.GetMemberCount())

print('- GetMemberIncidence')
print(geometry.GetMemberIncidence(beam_1))

print('- GetNoOfSelectedBeams')
print(geometry.GetNoOfSelectedBeams())

print('- GetSelectedBeams')
print(geometry.GetSelectedBeams()[0:10])

print('- GetNoOfBeamsConnectedAtNode')
print(geometry.GetNoOfBeamsConnectedAtNode(node_1))

print('- GetBeamsConnectedAtNode')
print(geometry.GetBeamsConnectedAtNode(node_1))

# ## GEOMETRY - GROUP

print('-'*20+'\nGeometry group Functions\n'+'-'*20)

group_1 = '_BEAMS'
print('- GetGroupEntityCount')
print(geometry.GetGroupEntityCount(group_1))

print('- GetGroupEntities')
print(geometry.GetGroupEntities(group_1)[0:10])

# print("\nPROPERTIES FUNCTIONS\n")

print('-'*20+'\nProperties Functions\n'+'-'*20)

print('- GetBeamSectionName')
print(properties.GetBeamSectionName(beam_1))

print('- GetBeamSectionPropertyRefNo')
print(properties.GetBeamSectionPropertyRefNo(beam_1))

print('- GetSectionPropertyValues')
print(properties.GetSectionPropertyValues(4))

print('- GetMemberSpecCode')
print(properties.GetMemberSpecCode(424))

# ## ROOT FUNCTIONS 

print('-'*20+'\nRoot Functions\n'+'-'*20)

print('- GetAnalysisStatus')
print(root.GetAnalysisStatus())

print('- GetApplicationVersion')
print(root.GetApplicationVersion())

print('- GetBaseUnit')
print(root.GetBaseUnit())

print('- GetInputUnitForForce')
print(root.GetInputUnitForForce())

print('- GetInputUnitForLength')
print(root.GetInputUnitForLength())

print('- GetSTAADFile')
print(root.GetSTAADFile())

print('- GetSTAADFile')
print(root.GetSTAADFile(bFullPath=False))

print('- GetSTAADFileFolder')
print(root.GetSTAADFileFolder())

## OUTPUT FUNCTIONS

print('-'*20+'\nOutput Functions\n'+'-'*20)

print('- GetMemberEndForces')
print(output.GetMemberEndForces(beam=beam_1, start=False, lc=1, local = 1))

print('- GetSupportReactions')
print(output.GetSupportReactions(node_1))

print('-'*20+'\nLoad Functions\n'+'-'*20)

print('- GetLoadCaseTitle')
print(load.GetLoadCaseTitle(lc=1))


from openstaad import Root, Geometry,Load,Output,Properties, Support, View


root = Root()

staad_path1=""
staad_path2=""

root1 = Root(staad_path1)
geometry1=Geometry(staad_path1)
load1=Load(staad_path1)
output1=Output(staad_path1)
properties1=Properties(staad_path1)
support1=Support(staad_path1)
view1=View(staad_path1)
root2 = Root(staad_path2)
load2=Load(staad_path2)
output2=Output(staad_path2)
geometry2=Geometry(staad_path2)
properties2=Properties(staad_path2)
support2=Support(staad_path2)
view2=View(staad_path2)

print(root1.GetSTAADFile())
print(geometry1.GetSelectedBeams())
print(load1.GetLoadListCount())
print(output1.GetSupportReactions(1,10))
print(properties1.GetBeamSectionName(1))
print(support1.GetSupportType(2))
view1.ShowMembers([1,2,3,4])
print(root2.GetSTAADFile())
print(geometry2.GetSelectedBeams())
print(load2.GetLoadCombinationCaseCount())
print(output2.GetSupportReactions(2,10))
print(properties2.GetBeamSectionName(71))
print(support2.GetSupportType(4))
view2.ShowMembers([1,2,3,4])

