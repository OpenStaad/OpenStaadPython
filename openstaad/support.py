from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Support():

    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._support = self._staad.Support

        self._functions= [
            'AssignSupportToNode',
            'CreateSupportFixed',
            'CreateSupportPinned',
            'GetSupportType',
            'GetSupportInformation'	
        ]

        for function_name in self._functions:
            self._support._FlagAsMethod(function_name)

    def AssignSupportToNode(self,NoNode:int,Support_type_ID:int):
        """
        Assigns the specified support to node(s).
        """
        self._support.AssignSupportToNode(NoNode,Support_type_ID)

    def CreateSupportFixed(self):
        """
        Creates a fully fixed support.
        """
        self._support.CreateSupportFixed()

    def CreateSupportPinned(self):
        """
        Creates a pinned support (i.e., free to rotate about local y and z axis, fixed in all other degrees of freedom).
        """
        self._support.CreateSupportPinned()

    def GetSupportType(self,node:int):
        """
        Gets the support type for the specified node.
        """
        return self._support.GetSupportType(node)
    
    # def GetSupportInformation(self, node: int):
    #     """
    #     Gets support information for the specified node, including release specification
    #     and spring specification.

    #     Parameters
    #     ----------
    #     vaSupportNode : int
    #         The supported node number ID.

    #     varReleaseSpec : array-like (out)
    #         Degrees of freedom specification for:
    #         [FX, FY, FZ, MX, MY, MZ]

    #         Values:
    #         - 0  : Released
    #         - 1  : Fixed
    #         - -1 : Spring (see varSpringSpec)

    #     varSpringSpec : array-like (out)
    #         Variable spring constants corresponding to:
    #         [KFX, KFY, KFZ, KMX, KMY, KMZ]

    #     Returns
    #     -------
    #     int
    #         Support type identifier:

    #         0   : No support
    #         1   : Pinned support
    #         2   : Fixed support
    #         3   : Fixed support with releases
    #         4   : Enforced support
    #         5   : Enforced support with releases
    #         6   : Inclined support
    #         7   : Footing foundation
    #         8   : Elastic mat foundation
    #         9   : Plate mat foundation
    #         10  : MultiLinear spring support
    #         11  : Generated pinned support
    #         12  : Generated fixed support
    #         13  : Generated fixed support with releases
    #         -1  : General error
    #     """

    #     safe_release = make_safe_array_double(6)
    #     var_release  = make_variant_vt_ref(
    #         safe_release,
    #         automation.VT_ARRAY | automation.VT_R8
    #     )

    #     safe_spring = make_safe_array_double(6)
    #     var_spring  = make_variant_vt_ref(
    #         safe_spring,
    #         automation.VT_ARRAY | automation.VT_R8
    #     )

    #     ret = self._support.GetSupportInformation(
    #         node,
    #         var_release,
    #         var_spring
    #     )

    #     return {
    #         'Is_Valid': ret,
    #         'ReleaseSpec': list(var_release.value),
    #         'SpringSpec':  list(var_spring.value)
    #     }

    def GetSupportInformation(self, node: int):

        # ReleaseSpec → LONG
        safe_release = make_safe_array_long(6)
        var_release  = make_variant_vt_ref(
            safe_release,
            automation.VT_ARRAY | automation.VT_I4
        )

        # SpringSpec → DOUBLE
        safe_spring = make_safe_array_double(6)
        var_spring  = make_variant_vt_ref(
            safe_spring,
            automation.VT_ARRAY | automation.VT_R8
        )

        ret = self._support.GetSupportInformation(
            node,
            var_release,
            var_spring
        )

        return {
            'Is_Valid': ret,
            'ReleaseSpec': list(var_release.value),
            'SpringSpec':  list(var_spring.value)
        }




