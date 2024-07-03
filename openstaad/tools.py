from comtypes import automation
import ctypes

def make_safe_array_double(size): 
    return automation._midlSAFEARRAY(ctypes.c_double).create([0]*size)

def make_safe_array_int(size): 
    return automation._midlSAFEARRAY(ctypes.c_int).create([0]*size)

def make_safe_array_long(size): 
    return automation._midlSAFEARRAY(ctypes.c_long).create([0]*size)

def make_safe_str(): 
    return automation.c_char_p()

def make_safe_array_string(size):
    return automation._midlSAFEARRAY(automation.BSTR).create([""]*size)

def make_variant_vt_ref(obj, var_type):
    var = automation.VARIANT()
    var._.c_void_p = ctypes.addressof(obj)
    var.vt = var_type | automation.VT_BYREF
    return var

def make_safe_array_long_input(lista): 
    return automation._midlSAFEARRAY(ctypes.c_long).create(lista)


APICALL = {'file':'',
            'geometry':'Geometry',
            'property':'Property',
            'support':'Support',
            'load':'Load',
            'table':'Table',
            'view':'View',
            'output':'Output',
            'commands':'Commands'
}