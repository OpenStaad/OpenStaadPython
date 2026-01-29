from openstaad.tools import *
from comtypes import automation
from comtypes import client
from comtypes import CoInitialize
from comtypes import COMError
import os

class Geometry():
    
    def __init__(self, filePath: str = None):
        CoInitialize()
        
        try:
            if filePath:
                filePath = os.path.abspath(filePath)
                if not os.path.exists(filePath):
                    raise FileNotFoundError(filePath)

                root_com = client.CoGetObject(filePath, dynamic=True)
            else:

                root_com = client.GetActiveObject("StaadPro.OpenSTAAD")

            self._geometry = root_com.Geometry

        except COMError:
            raise RuntimeError("Cannot connect to STAAD.Pro")

        self._functions= [
        "AddBeam",
        "AddMultiplePlates",
        "AddNode",
        "AddPlate",
        "ClearMemberSelection",
        "ClearPlateSelection",
        "CreateGroup",
        "UpdateGroup",
        "CreatePhysicalMember",
        "DeletePhysicalMember",
        "DeletePlate",
        "DoTranslationalRepeat",
        "GetAnalyticalMemberCountForPhysicalMember",
        "GetAnalyticalMembersForPhysicalMember",
        "GetAreaOfPlates",
        "GetBeamLength",
        "GetBeamList",
        "GetBeamsConnectedAtNode",
        "GetGroupCount",
        "GetGroupEntities",
        "GetGroupEntityCount",
        "GetGroupNames",
        "GetIntersectBeamsCount",
        "GetLastBeamNo",
        "GetLastNodeNo",
        "GetLastPhysicalMemberNo",
        "GetLastPlateNo",
        "GetMemberCount",
        "GetMemberIncidence",
        "GetNodeCoordinates",
        "GetNodeCount",
        "GetNodeDistance",
        "GetNodeIncidence",
        "GetNodeList",
        "GetNodeNumber",
        "GetNoOfBeamsConnectedAtNode",
        "GetNoOfSelectedBeams",
        "GetNoOfSelectedNodes",
        "GetNoOfSelectedPhysicalMembers",
        "GetNoOfSelectedPlates",
        "GetPMemberCount",
        "GetPhysicalMemberCount",
        "GetPhysicalMemberList",
        "GetPhysicalMemberUniqueID",
        "GetPlateCount",
        "GetPlateIncidence",
        "GetPlateList",
        "GetPlateNodeCount",
        "GetPlateUniqueID",
        "GetSelectedBeams",
        "GetSelectedNodes",
        "GetSelectedPhysicalMembers",
        "GetSelectedPlates",
        "IntersectBeams",
        "RenumberBeam",
        "SelectMultipleBeams",
        "SelectMultiplePhysicalMembers",
        "SelectMultiplePlates",
        "SelectPhysicalMember",
        "SelectPlate",
        "SetPhysicalMemberUniqueID",
        "SetPlateUniqueID"
        ]

        for function_name in self._functions:
            self._geometry._FlagAsMethod(function_name)

    def __getattr__(self, name):
        return getattr(self._geometry, name)

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
    
    def DeletePhysicalMember(self,p_member:int):
        self._geometry.DeletePhysicalMember(p_member)

    def GetAnalyticalMemberCountForPhysicalMember(self,p_member:int):
        return self._geometry.GetAnalyticalMemberCountForPhysicalMember(p_member)
    
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
        
        safe_n1 = make_safe_array_double(1)
        dTolerance = make_variant_vt_ref(safe_n1, automation.VT_R8)

        def make_safe_array_long(array):
            size = len(array)
            return automation._midlSAFEARRAY(ctypes.c_long).create(array)
    
        safe_beam_list = make_safe_array_long(BeamNosArray)
        BeamNosArray = make_variant_vt_ref(safe_beam_list, automation.VT_ARRAY | automation.VT_I4)
        
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

    #Not Working yet
    def GetAnalyticalMembersForPhysicalMember(self, p_member: int):
        
        no_am = self._geometry.GetAnalyticalMemberCountForPhysicalMember(p_member)

        if no_am == 0:
            return []

        safe_list = automation._midlSAFEARRAY(ctypes.c_int).create([0] * no_am)

        var_p_member = automation.VARIANT(p_member)
        var_no_am = automation.VARIANT(no_am)
        var_member_list = automation.VARIANT()
        var_member_list._.c_void_p = ctypes.addressof(safe_list)
        var_member_list.vt = automation.VT_ARRAY | automation.VT_I4 | automation.VT_BYREF

        self._geometry.GetAnalyticalMembersForPhysicalMember(
            var_p_member, var_no_am, var_member_list
        )

        return list(safe_list)

    def GetLastPhysicalMemberNo(self):
        return self._geometry.GetLastPhysicalMemberNo()

    def GetNoOfSelectedPhysicalMembers(self):
        return self._geometry.GetNoOfSelectedPhysicalMembers()

    def GetPhysicalMemberCount(self):
        return self._geometry.GetPhysicalMemberCount()
            
    def GetPhysicalMemberList(self):
        no_p_members=self._geometry.GetPhysicalMemberCount()

        safe_list = make_safe_array_long(no_p_members)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._geometry.GetPhysicalMemberList(lista)

        return (lista[0])
    
    def GetPhysicalMemberUniqueID(self,p_member):
        return self._geometry.GetPhysicalMemberUniqueID(p_member)
    
    def GetPMemberCount(self):
        return self._geometry.GetPMemberCount()
        
    def ClearPlateSelection(self):
        self._geometry.ClearPlateSelection() 

    def GetLastPlateNo(self):
        """
        Returns the plate number ID of the last plate in the model.
        """
        return self._geometry.GetLastPlateNo()
    
    def GetNoOfSelectedPlates(self):
        """Returns the number of selected plate(s)."""
        return self._geometry.GetNoOfSelectedPlates()
    
    def GetPlateCount(self):
        """Returns the total number of plates in the current model."""
        return self._geometry.GetPlateCount()
    
    def GetPlateNodeCount(self,plate):
        """Returns the number of nodes provided with for plate connectivity."""
        return self._geometry.GetPlateNodeCount(plate)
    
    def GetPlateIncidence(self,plate):
        safe_n1 = make_safe_array_long(1)
        p1 = make_variant_vt_ref(safe_n1,  automation.VT_I4)

        safe_n2 = make_safe_array_long(1)
        p2 = make_variant_vt_ref(safe_n2,  automation.VT_I4)

        safe_n3 = make_safe_array_long(1)
        p3 = make_variant_vt_ref(safe_n3,  automation.VT_I4)

        safe_n4 = make_safe_array_long(1)
        p4 = make_variant_vt_ref(safe_n4,  automation.VT_I4)

        self._geometry.GetPlateIncidence(plate,p1,p2,p3,p4)

        number_of_nodes = self.GetPlateNodeCount(plate)

        return (p1[0],p2[0],p3[0],p4[0])[0:number_of_nodes]
    
    def GetPlateList(self):
        n_nodes =  self._geometry.GetPlateCount()
        safe_list = make_safe_array_long(n_nodes)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._geometry.GetPlateList(lista)

        return (lista[0])
    
    def GetPlateUniqueID(self,plate):
        return self._geometry.GetPlateUniqueID(plate)
    
    def GetSelectedPlates(self):
        n_nodes = self.GetNoOfSelectedPlates()
        safe_list = make_safe_array_long(n_nodes)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._geometry.GetSelectedPlates(lista)

        return (lista[0])
    
    def RenumberBeam(self, oldBeamNo: int, newBeamNo: int):
        """
        Renumber a beam.
        """
        result = int(self._geometry.RenumberBeam(oldBeamNo, newBeamNo))
        return bool(result)

    #SelectPlate

    def SelectPlate(self,plate,add_mode = True):
        if not add_mode:
            self.ClearPlateSelection()

        self._geometry.SelectPlate(plate)

    def SelectMultiplePlates(self, lista, add_mode = True):
        if not add_mode:
            self.ClearPlateSelection()
        
        safe_list = make_safe_array_long_input(lista)
        lista_variant = make_variant_vt_ref(safe_list, automation.VT_ARRAY | automation.VT_I4)
        
        self._geometry.SelectMultiplePlates(lista_variant)

    def SetPlateUniqueID(self,plate,unique_id):
        self._geometry.SetPlateUniqueID(plate,unique_id)  

    def AddPlate(self,node_A,node_B, node_C, node_D = None):

        if node_D == None:
           self._geometry.AddPlate(node_A,node_B, node_C)

        else:
            self._geometry.AddPlate(node_A,node_B, node_C, node_D)
            
    def DeletePlate(self,plate):
        self._geometry.DeletePlate(plate)
        
       
    def GetAreaOfPlates(self,plates: list) -> list[float]:
        
        safe_palte_list = make_safe_array_int_input(plates)
        plate_list = make_variant_vt_ref(safe_palte_list, automation.VT_ARRAY | automation.VT_I4)
        
        safe_area = make_safe_array_double(len(plates))
        area = make_variant_vt_ref(safe_area,  automation.VT_ARRAY | automation.VT_R8)
        
        self._geometry.GetAreaOfPlates(plate_list,area)
        
        return area.value[0]

    
    def CreateGroup(self, group_type: int, group_name: str):
        """
        Creates a group with specified name for the specified type for selected entities.
        
        IMPORTANT: You must select entities before calling this function!
        Use SelectMultipleBeams(), SelectMultiplePlates(), etc. to select entities first.

        Parameters:
        group_type (int): The type of the group:
            1: Nodes
            2: Members  
            3: Plates
            4: Solids
            5: Geometry (Members, Plates and Solids)
            6: Floor (Floor beam)
        group_name (str): The name of the group to be created.

        Returns:
        int: Return code from STAAD:
            0: OK
            -1: General error
            -100: Invalid Argument
            -110: No beam/plate/solid has been selected
            -2005: No node has been selected
            -3005: No member has been selected
            -4005: No plate has been selected
            -5005: No solid has been selected
            -7001: Group already exists
        """
        try:
            # Validar parámetros de entrada
            if not isinstance(group_type, int) or group_type < 1 or group_type > 6:
                raise ValueError("group_type debe ser un entero entre 1 y 6")
            
            if not isinstance(group_name, str) or not group_name.strip():
                raise ValueError("group_name debe ser una cadena no vacía")
            
            # Limpiar el nombre del grupo (remover espacios extra)
            clean_group_name = group_name.strip()
            
            # Crear parámetro seguro para el nombre del grupo usando tools
            safe_group_name, bstr_name = make_safe_bstr()
            bstr_name.value = clean_group_name
            
            # Llamar a la función de STAAD con parámetros seguros
            result = self._geometry.CreateGroup(group_type, safe_group_name)
            
            # Interpretar el resultado
            if result == 0:
                print(f"✓ Grupo '{clean_group_name}' creado exitosamente")
            elif result == -2005:
                print(f"✗ Error: No hay nodos seleccionados para crear el grupo")
            elif result == -3005:
                print(f"✗ Error: No hay miembros seleccionados para crear el grupo")
            elif result == -4005:
                print(f"✗ Error: No hay placas seleccionadas para crear el grupo")
            elif result == -110:
                print(f"✗ Error: No hay elementos seleccionados para crear el grupo")
            elif result == -7001:
                print(f"✗ Error: El grupo '{clean_group_name}' ya existe")
            elif result == -100:
                print(f"✗ Error: Argumento inválido")
            else:
                print(f"✗ Error desconocido: {result}")
            
            return result
            
        except Exception as e:
            print(f"Error en CreateGroup: {e}")
            raise
    
    def UpdateGroup(self, group_name: str, flag: int, entity_list: list):
        """
        Updates (replaces, removes, adds) entities to a specified group.
        
        Parameters:
        group_name (str): Group string name.
        flag (int): Option for operation:
            0 = replace the group entities with array of entities
            1 = remove entities from this group
            2 = add entities to this group
        entity_list (list): List of entity number IDs to update in the group.
        
        Returns:
        int: Return code from STAAD:
            0: OK
            -1: General error
            -107: Array of integer expected
        
        Example:
        # Add entities to "NodeGroup" group
        result = geometry.UpdateGroup("NodeGroup", 2, [101, 102, 103, 104])
        
        # Replace all entities in group
        result = geometry.UpdateGroup("BeamGroup", 0, [201, 202, 203])
        
        # Remove entities from group  
        result = geometry.UpdateGroup("BeamGroup", 1, [201, 202])
        """
        try:
            # Validar parámetros de entrada
            if not isinstance(group_name, str) or not group_name.strip():
                raise ValueError("group_name debe ser una cadena no vacía")
            
            if not isinstance(flag, int) or flag < 0 or flag > 2:
                raise ValueError("flag debe ser un entero entre 0 y 2")
            
            if not isinstance(entity_list, list) or len(entity_list) == 0:
                raise ValueError("entity_list debe ser una lista no vacía de enteros")
            
            # Validar que todos los elementos sean enteros
            if not all(isinstance(x, int) for x in entity_list):
                raise ValueError("Todos los elementos en entity_list deben ser enteros")
            
            # Limpiar el nombre del grupo
            clean_group_name = group_name.strip()
            
            # Crear parámetro seguro para el nombre del grupo
            safe_group_name, bstr_name = make_safe_bstr()
            bstr_name.value = clean_group_name
            
            # Crear VARIANT para el flag
            flag_variant = automation.VARIANT(flag)
            
            # Crear VARIANT para entity count
            entity_count = len(entity_list)
            entity_count_variant = automation.VARIANT(entity_count)
            
            # Crear array seguro para la lista de entidades
            safe_entity_list = make_safe_array_long_input(entity_list)
            entity_list_variant = make_variant_vt_ref(safe_entity_list, automation.VT_ARRAY | automation.VT_I4)
            
            # Llamar a la función de STAAD con parámetros seguros
            result = self._geometry.UpdateGroup(
                safe_group_name,
                flag_variant,
                entity_count_variant,
                entity_list_variant
            )
            
            # Interpretar el resultado
            if result == 0:
                operation_names = {0: "reemplazado", 1: "eliminado", 2: "agregado"}
                operation = operation_names.get(flag, "actualizado")
                print(f"✓ Grupo '{clean_group_name}' {operation} exitosamente ({entity_count} entidades)")
            elif result == -1:
                print(f"✗ Error general actualizando el grupo '{clean_group_name}'")
            elif result == -107:
                print(f"✗ Error: Se esperaba un array de enteros")
            else:
                print(f"✗ Error desconocido actualizando grupo '{clean_group_name}': {result}")
            
            return result
            
        except Exception as e:
            print(f"Error en UpdateGroup: {e}")
            raise
    
    