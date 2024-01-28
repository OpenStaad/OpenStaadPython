from openstaad.Safe_variables import *
from comtypes import automation

class _Geometry():
    def __init__(self,os):
        self._os = os.Geometry

        self._functions= [
            "GetLastNodeNo",
            "GetNodeCoordinates",
            "GetNodeCount",
            "GetNodeDistance",
            "GetNodeIncidence",
            "GetNodeIncidence_CIS2",
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
            'GetGroupEntities',
            'GetGroupEntityCount',
            'GetNoOfBeamsConnectedAtNode',
            'GetBeamsConnectedAtNode'
        ]

        for function_name in self._functions:
            self._os._FlagAsMethod(function_name)

    ## NODE FUNCTIONS

    def GetLastNodeNo(self):
        return self._os.GetLastNodeNo()
    
    def GetNodeCoordinates(self,node:int):
        safe_n1 = make_safe_array_double(1)
        x = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        safe_n2 = make_safe_array_double(1)
        y = make_variant_vt_ref(safe_n2,  automation.VT_R8)

        safe_n3 = make_safe_array_double(1)
        z = make_variant_vt_ref(safe_n3,  automation.VT_R8)

        self._os.GetNodeCoordinates(node,x,y,z)
        
        x = round(x[0]*1000)/1000
        y = round(y[0]*1000)/1000
        z = round(z[0]*1000)/1000

        return (x,y,z)

    def GetNodeCount(self):
        return self._os.GetNodeCount()

    def GetNodeDistance(self,nodeA, nodeB):

        distance = round(self._os.GetNodeDistance(nodeA,nodeB)*1000)/1000

        return distance

    def GetNodeIncidence(self,node):
        safe_n1 = make_safe_array_double(1)
        x = make_variant_vt_ref(safe_n1,  automation.VT_R8)

        safe_n2 = make_safe_array_double(1)
        y = make_variant_vt_ref(safe_n2,  automation.VT_R8)

        safe_n3 = make_safe_array_double(1)
        z = make_variant_vt_ref(safe_n3,  automation.VT_R8)

        self._os.GetNodeIncidence(node,x,y,z)

        x = round(x[0]*1000)/1000
        y = round(y[0]*1000)/1000
        z = round(z[0]*1000)/1000

        return (x,y,z)

    def GetNodeList(self):
        n_nodes =  self._os.GetNodeCount()
        safe_list = make_safe_array_long(n_nodes)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._os.GetNodeList(lista)

        return (lista[0])

    def GetNodeNumber(self,x_y_z_coordinates:tuple):
        return self._os.GetNodeNumber(x_y_z_coordinates[0],x_y_z_coordinates[1],x_y_z_coordinates[2])

    def GetNoOfSelectedNodes(self):
        return self._os.GetNoOfSelectedNodes()

    def GetSelectedNodes(self):
        n_nodes = self.GetNoOfSelectedNodes()
        safe_list = make_safe_array_long(n_nodes)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._os.GetSelectedNodes(lista)

        return (lista[0])

    ## BEAM FUNCTIONS
    
    def GetBeamLength(self,beam):
        length = round(self._os.GetBeamLength(beam)*1000)/1000
        return length

    def GetMemberCount(self):
        return self._os.GetMemberCount()

    def GetBeamList(self):
        beams = self._os.GetMemberCount()
        safe_list = make_safe_array_long(beams)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._os.GetBeamList(lista)

        return (lista[0])

    def GetLastBeamNo(self):
        return self._os.GetLastBeamNo()

    def GetMemberCount(self):
        return self._os.GetMemberCount()

    def GetMemberIncidence(self,beam):
        safe_n1 = make_safe_array_long(1)
        x = make_variant_vt_ref(safe_n1,  automation.VT_I4)

        safe_n2 = make_safe_array_long(1)
        y = make_variant_vt_ref(safe_n2,  automation.VT_I4)

        self._os.GetMemberIncidence(beam,x,y)

        return (x[0],y[0])

    def GetNoOfSelectedBeams(self):
        return self._os.GetNoOfSelectedBeams()
    
    def GetSelectedBeams(self):
        n_beams = self._os.GetNoOfSelectedBeams()
        safe_list = make_safe_array_long(n_beams)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._os.GetSelectedBeams(lista)

        return (lista[0])

    def GetNoOfBeamsConnectedAtNode(self,node):
        return self._os.GetNoOfBeamsConnectedAtNode(node)
       
 
    def GetBeamsConnectedAtNode(self,node):
        No_Nodes = self._os.GetNoOfBeamsConnectedAtNode(node)
       
        safe_list = make_safe_array_long(No_Nodes)
        list = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)
 
        retval=self._os.GetBeamsConnectedAtNode(node,list)
 
        return list[0]

    ## GROUP FUNCTIONS

    def GetGroupEntityCount(self,group_name):
        return self._os.GetGroupEntityCount(group_name)

    def GetGroupEntities(self,group_name):
        beams = self._os.GetGroupEntityCount(group_name)
        safe_list = make_safe_array_long(beams)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)
        
        self._os.GetGroupEntities(group_name,lista)
        
        return lista[0]