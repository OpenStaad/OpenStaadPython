from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Root():
    def __init__(self):      
        staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._root = staad
        
        self._functions = ['GetAnalysisStatus',
                           'GetApplicationVersion',
                           'GetBaseUnit',
                           'GetSTAADFile',
                           'GetSTAADFileFolder',
                           'GetInputUnitForForce',
                           'GetInputUnitForLength'
        ]

        for function_name in self._functions:
            self._root._FlagAsMethod(function_name)
    
    def GetAnalysisStatus(self):
        """
        Get analysis status for the open STAAD Model. 

        Output: Dictionary with the following keys:
            ReturnValue: int : 
                -2: Invalid model path
                -1: Analysis Terminated
                0: General Error
                1: Analysis is in progress
                2: Analysis completed without errors or warnings
                3: Analysis completed with warnings but without errors
                4: Analysis completed with errors
                5: Analysis has not been performed

            ReturnString: str
                Description of the ReturnValue

            NoOfWarnings: int
                Number of warnings in the analysis

            NoOfErrors: int
                Number of errors in the analysis

            CPUTime(sec): int
                CPU time taken for the analysis in seconds  
        """

        safe_NoOfWarnings = make_safe_array_long(0)
        NoOfWarnings = make_variant_vt_ref(safe_NoOfWarnings,  automation.VT_I4)

        safe_NoofErrors = make_safe_array_long(0)
        NoofErrors = make_variant_vt_ref(safe_NoofErrors,  automation.VT_I4)

        safe_CPUTime = make_safe_array_double(0)
        CPUTime = make_variant_vt_ref(safe_CPUTime,  automation.VT_R8)

        szModelNameWithPath = self.GetSTAADFile(bFullPath=True)


        retval = self._root.GetAnalysisStatus(szModelNameWithPath, NoOfWarnings, NoofErrors, CPUTime)

        status_dict = {
                        -2: "Invalid model path",
                        -1: "Analysis Terminated",
                        0: "General Error",
                        1: "Analysis is in progress",
                        2: "Analysis completed without errors or warnings",
                        3: "Analysis completed with warnings but without errors",
                        4: "Analysis completed with errors",
                        5: "Analysis has not been performed"
                    }

        output = {'ReturnValue':retval,
                   'ReturnString':status_dict[retval],
                    'NoOfWarnings':NoOfWarnings[0],
                  'NoOfErrors':NoofErrors[0],
                  'CPUTime(sec)':int(CPUTime[0])}

        return output

    def GetApplicationVersion(self):
        """
        Returns The	current application version as string.

        """
        safe_MajorA = make_safe_array_long(0)
        MajorA = make_variant_vt_ref(safe_MajorA,  automation.VT_I4)   

        safe_MajorB = make_safe_array_long(0)
        MajorB = make_variant_vt_ref(safe_MajorB,  automation.VT_I4)  

        safe_Minor = make_safe_array_long(0)
        Minor = make_variant_vt_ref(safe_Minor,  automation.VT_I4)  

        safe_Build = make_safe_array_long(0)
        Build = make_variant_vt_ref(safe_Build,  automation.VT_I4)  

        self._root.GetApplicationVersion(MajorA, MajorB, Minor, Build)
        
        output = 'Version ' + str(MajorA[0]) + '.' + str(MajorB[0]) + '.' + str(Minor[0]) + '.' + str(Build[0])

        return output

    def GetBaseUnit(self):
        """
        Returns the base unit for the currently open .STD file.
            
            Output: str
                English or Metric

                For English system of units (The values that are derived from a length unit, e.g. dimensions, areas, stresses, will be based on inches, 'in'. All values derived from a force unit, e.g. Axial force, moments, stresses, etc, will be based on kilopounds, 'KIP').
                For Metric system of units (The values that are derived from a length unit, will be based on Meters, 'm'. All values derived from a force unit, will be based on kilo newtons, 'kNs').

        """
        safe_retVal  = make_safe_array_long(0)
        retVal  = make_variant_vt_ref(safe_retVal ,  automation.VT_I4)  

        retVal = self._root.GetBaseUnit()

        output = {1:'English',2:'Metric'}

        return output[retVal]
    
    def GetInputUnitForForce(self):
        """
        Retrieves the input unit of force of the currently open .STD file.

         0- Kilopound 1- Pound 2- Kilogram 3- Metric Ton 4- Newton 5- KiloNewton 6- MegaNewton 7- DecaNewton

        """
        output = {0:'Kilopound',1:'Pound',2:'Kilogram',3:'Metric Ton',4:'Newton',5:'KiloNewton',6:'MegaNewton',7:'DecaNewton'}

        safe_retVal  = make_safe_array_long(0)
        retVal  = make_variant_vt_ref(safe_retVal ,  automation.VT_I4)  

        a = self._root.GetInputUnitForForce(retVal)
    
        return output[a]

    def GetInputUnitForLength(self):
        """
        Retrieves the input unit of length of the currently open .STD file.

       0- Inch, 1- Feet, 2- Feet, 3- CentiMeter, 4- Meter, 5- MilliMeter, 6 - DeciMeter, 7 – KiloMeter
        """
        output = {0:'Inch',1:'Feet',2:'Feet',3:'CentiMeter',4:'Meter',5:'MilliMeter',6:'DeciMeter',7:'KiloMeter'}

        safe_retVal  = make_safe_array_long(0)
        retVal  = make_variant_vt_ref(safe_retVal ,  automation.VT_I4)  

        a = self._root.GetInputUnitForLength(retVal)
    
        return output[a]

    def GetSTAADFile(self,bFullPath: bool =True):
        """
        Retrieves the path or the name of the current .STD file.

        Input: bFullPath: True or False

        output: str

        """    

        safe_fileName = make_safe_str()
        fileName = make_variant_vt_ref(safe_fileName,  automation.VT_BSTR)
        
        self._root.GetSTAADFile(fileName, bFullPath)
        return fileName[0]
    
    def GetSTAADFileFolder(self):
        """
        Retrieves the folder path of current STAAD file.
        """  
        safe_fileFolder = make_safe_str()
        fileFolder = make_variant_vt_ref(safe_fileFolder,  automation.VT_BSTR)

        self._root.GetSTAADFileFolder(fileFolder)

        return fileFolder[0]

    
