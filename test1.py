from openstaad import Root, Geometry,Load,Output,Properties, Support, View


root = Root()

staad_path1="C:\\Users\\ccarvajal\\OneDrive - TEN\\Documentos\\05- Ni_Refinery\\01-MT2_Building\\Staad\\MT2 - Steel_SLS.std"
staad_path2="C:\\Users\\ccarvajal\\OneDrive - TEN\Desktop\\test_staad\\MT2_Steel.STD"

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

