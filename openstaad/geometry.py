from openstaad.tools import *
from comtypes import automation
from comtypes import client
from comtypes import CoInitialize

class Geometry():
    CoInitialize()
    def __init__(self):
        # CoInitialize()
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._geometry = self._staad.Geometry

        self._functions= [
            "GetLastNodeNo",
            "GetNodeCoordinates",
            "GetNodeCount",
            "GetNodeDistance",
            "GetNodeIncidence",
            "GetNodeList",
            "GetNodeNumber",
            "GetNoOfSelectedNodes",
            "GetSelectedNodes",
            'GetBeamLength',
            'GetBeamList',
            'GetMemberCount',
            'GetLastBeamNo',
            'GetMemberIncidence',
            'GetNoOfSelectedBeams',
            'GetSelectedBeams',
            'GetNoOfBeamsConnectedAtNode',
            'GetBeamsConnectedAtNode',
            'GetGroupEntities',
            'GetGroupEntityCount',
            'ClearMemberSelection',
            'SelectMultipleBeams',
            'GetGroupCount',
            'GetGroupNames',
            'CreatePhysicalMember',
            'AddNode',
            'AddBeam',
            'DoTranslationalRepeat',
            'GetIntersectBeamsCount',
            'IntersectBeams'
        ]

        for function_name in self._functions:
            self._geometry._FlagAsMethod(function_name)

    ## NODE FUNCTIONS

    def GetLastNodeNo(self):
        return self._geometry.GetLastNodeNo()
    
    def GetNodeCoordinates(self,node:int):
        safe_n1 = make_safe_array_double(1)
        x = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        safe_n2 = make_safe_array_double(1)
        y = make_variant_vt_ref(safe_n2,  automation.VT_R8)

        safe_n3 = make_safe_array_double(1)
        z = make_variant_vt_ref(safe_n3,  automation.VT_R8)

        self._geometry.GetNodeCoordinates(node,x,y,z)
        
        x = round(x[0]*1000)/1000
        y = round(y[0]*1000)/1000
        z = round(z[0]*1000)/1000

        return (x,y,z)

    def GetNodeCount(self):
        return self._geometry.GetNodeCount()

    def GetNodeDistance(self,nodeA, nodeB):

        distance = round(self._geometry.GetNodeDistance(nodeA,nodeB)*1000)/1000

        return distance

    def GetNodeIncidence(self,node):
        safe_n1 = make_safe_array_double(1)
        x = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        safe_n2 = make_safe_array_double(1)
        y = make_variant_vt_ref(safe_n2,  automation.VT_R8)

        safe_n3 = make_safe_array_double(1)
        z = make_variant_vt_ref(safe_n3,  automation.VT_R8)

        self._geometry.GetNodeIncidence(node,x,y,z)

        x = round(x[0]*1000)/1000
        y = round(y[0]*1000)/1000
        z = round(z[0]*1000)/1000

        return (x,y,z)

    def GetNodeList(self):
        n_nodes =  self._geometry.GetNodeCount()
        safe_list = make_safe_array_long(n_nodes)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._geometry.GetNodeList(lista)

        return (lista[0])

    def GetNodeNumber(self,x_y_z_coordinates:tuple):
        return self._geometry.GetNodeNumber(x_y_z_coordinates[0],x_y_z_coordinates[1],x_y_z_coordinates[2])

    def GetNoOfSelectedNodes(self):
        return self._geometry.GetNoOfSelectedNodes()

    def GetSelectedNodes(self):
        n_nodes = self.GetNoOfSelectedNodes()
        safe_list = make_safe_array_long(n_nodes)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._geometry.GetSelectedNodes(lista)

        return (lista[0])

    ## BEAM FUNCTIONS
    
    def GetBeamLength(self,beam):
        length = round(self._geometry.GetBeamLength(beam)*1000)/1000
        return length

    def GetMemberCount(self):
        return self._geometry.GetMemberCount()

    def GetBeamList(self):
        beams = self._geometry.GetMemberCount()
        safe_list = make_safe_array_long(beams)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._geometry.GetBeamList(lista)

        return (lista[0])

    def GetLastBeamNo(self):
        return self._geometry.GetLastBeamNo()

    def GetMemberCount(self):
        return self._geometry.GetMemberCount()

    def GetMemberIncidence(self,beam):
        safe_n1 = make_safe_array_long(1)
        x = make_variant_vt_ref(safe_n1,  automation.VT_I4)

        safe_n2 = make_safe_array_long(1)
        y = make_variant_vt_ref(safe_n2,  automation.VT_I4)

        self._geometry.GetMemberIncidence(beam,x,y)

        return (x[0],y[0])

    def GetNoOfSelectedBeams(self):
        return self._geometry.GetNoOfSelectedBeams()
    
    def GetSelectedBeams(self):
        n_beams = self._geometry.GetNoOfSelectedBeams()
        safe_list = make_safe_array_long(n_beams)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._geometry.GetSelectedBeams(lista)

        return (lista[0])

    def GetNoOfBeamsConnectedAtNode(self,node):
        return self._geometry.GetNoOfBeamsConnectedAtNode(node)
       
 
    def GetBeamsConnectedAtNode(self,node):
        No_Nodes = self._geometry.GetNoOfBeamsConnectedAtNode(node)
       
        safe_list = make_safe_array_long(No_Nodes)
        list = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)
 
        retval=self._geometry.GetBeamsConnectedAtNode(node,list)
 
        return list[0]

    ## GROUP FUNCTIONS

    def GetGroupEntityCount(self,group_name):
        return self._geometry.GetGroupEntityCount(group_name)

    def GetGroupEntities(self,group_name):
        beams = self._geometry.GetGroupEntityCount(group_name)
        safe_list = make_safe_array_long(beams)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)
        
        self._geometry.GetGroupEntities(group_name,lista)
        
        return lista[0]
    
    def ClearMemberSelection(self):
        self._geometry.ClearMemberSelection()

    def SelectMultipleBeams(self, lista):
        
        safe_list = make_safe_array_long_input(lista)
        lista_variant = make_variant_vt_ref(safe_list, automation.VT_ARRAY | automation.VT_I4)
        
        self._geometry.SelectMultipleBeams(lista_variant)

    def GetGroupCount(self,grouptype):
        return self._geometry.GetGroupCount(grouptype)

    def GetGroupNames(self,grouptype):
        group_count = self._geometry.GetGroupCount(grouptype)
        group_names_safe_array = make_safe_array_string(group_count)
        group_names = make_variant_vt_ref(group_names_safe_array, automation.VT_ARRAY | automation.VT_BSTR)

        self._geometry.GetGroupNames(grouptype, group_names)

        return group_names[0]
    
    def CreatePhysicalMember(self,member_list:list):
        """
        Creates a physical member from specified analytical members.
        Note: This method is not supported for physical models
        
        MemberList	List of physical member IDs (array of type long) that would form the physical member to be created
        """
        num=len(member_list)

        safe_list = make_safe_array_long_input(member_list)
        lista_variant = make_variant_vt_ref(safe_list, automation.VT_ARRAY | automation.VT_I4)
        retval=self._geometry.CreatePhysicalMember(num,lista_variant,None)
        


    def AddNode(self,x:float=0.0,y:float=0.0,z:float=0.0):
        retval=self._geometry.AddNode(x,y,z)
        return retval
    
    def AddBeam(self,node_A,node_B):
        retval=self._geometry.AddBeam(node_A,node_B)
        return retval

    def make_safe_array_long(data):
        if not isinstance(data, list):
            raise TypeError("Data must be a list of integers")
        
        size = len(data)
        safe_array = automation._midlSAFEARRAY(ctypes.c_long).create([0] * size)
        
        for i in range(size):
            safe_array[i] = data[i]
        
        return safe_array

    def make_variant_vt_ref(safe_array, vt_type):
        variant = automation.VARIANT()
        variant.vt = vt_type
        variant._.parray = safe_array
        return variant
    
    def DoTranslationalRepeat(self, varLinkBays: bool, varOpenBase: bool, varAxisDir: int, varSpacingArray: list[float], varNobays: int, varRenumberBay: bool, varRenumberArray: list, varGeometryOnly: bool):
        try:
            
            def make_safe_array_double(array):
                size = len(array)
                return automation._midlSAFEARRAY(ctypes.c_double).create(array)

            # Conversión de varSpacingArray
            safe_spacing_array = make_safe_array_double(varSpacingArray)
            varSpacingArray = make_variant_vt_ref(safe_spacing_array, automation.VT_ARRAY | automation.VT_R8)
            
            retval = self._geometry.DoTranslationalRepeat(varLinkBays, varOpenBase, varAxisDir, varSpacingArray, varNobays, varRenumberBay, varRenumberArray, varGeometryOnly)
            return retval
        except Exception as e:
            print(f"An error occurred in DoTranslationalRepeat: {e}")
            raise
    
    def IntersectBeams(self, Method: int, BeamNosArray: list[int], dTolerance: float, NewBeamNosArray: int):
        
        # Conversión de dTolerance
        safe_n1 = make_safe_array_double(1)
        dTolerance = make_variant_vt_ref(safe_n1, automation.VT_R8)

        # Ajuste en make_safe_array_long para manejar listas
        def make_safe_array_long(array):
            size = len(array)
            return automation._midlSAFEARRAY(ctypes.c_long).create(array)
        
        # Conversión de BeamNosArray
        safe_beam_list = make_safe_array_long(BeamNosArray)
        BeamNosArray = make_variant_vt_ref(safe_beam_list, automation.VT_ARRAY | automation.VT_I4)
        
        # Conversión de NewBeamNosArray
        # safe_beam_list = make_safe_array_long(NewBeamNosArray)
        # NewBeamNosArray = make_variant_vt_ref(safe_beam_list, automation.VT_ARRAY | automation.VT_I4)

        
        # Llamada a la función interna
        retval = self._geometry.IntersectBeams(Method, BeamNosArray, dTolerance, NewBeamNosArray)
        return retval
    
    def GetIntersectBeamsCount(self, BeamNosArray: list[int], dTolerance: float):
        safe_n1 = make_safe_array_double(1)
        dTolerance = make_variant_vt_ref(safe_n1, automation.VT_R8)
        
        def make_safe_array_long(array):
            size = len(array)
            return automation._midlSAFEARRAY(ctypes.c_long).create(array)
        
        safe_list = make_safe_array_long(BeamNosArray)
        BeamNosArray = make_variant_vt_ref(safe_list, automation.VT_ARRAY | automation.VT_I4)
        
        n_beams = self._geometry.GetIntersectBeamsCount(BeamNosArray, dTolerance)
        return n_beams
    

    


