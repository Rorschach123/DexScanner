
INS_NOP                             = 0x00

INS_MOVE                            = 0x01
INS_MOVE_FROM16                     = 0x02
INS_MOVE16                          = 0x03
INS_MOVE_WIDE                       = 0x04
INS_MOVE_WIDE_FROM16                = 0x05
INS_MOVE_WIDE16                     = 0x06
INS_MOVE_OBJECT                     = 0x07
INS_MOVE_OBJECT_FROM16              = 0x08
INS_MOVE_OBJECT16                   = 0x09
INS_MOVE_RESULT                     = 0x0A
INS_MOVE_RESULT_WIDE                = 0x0B
INS_MOVE_RESULT_OBJECT              = 0x0C
INS_MOVE_EXCEPTION                  = 0x0D

INS_RETURN_VOID                     = 0x0E
INS_RETURN                          = 0x0F
INS_RETURN_WIDE                     = 0x10
INS_RETURN_OBJECT                   = 0x11

INS_CONST4                          = 0x12
INS_CONST16                         = 0x13
INS_CONST                           = 0x14
INS_CONST_HIGH16                    = 0x15
INS_CONST_WIDE16                    = 0x16
INS_CONST_WIDE32                    = 0x17
INS_CONST_WIDE                      = 0x18
INS_CONST_WIDE_HIGH16               = 0x19
INS_CONST_STRING                    = 0x1A
INS_CONST_STRING_JUMBO              = 0x1B
INS_CONST_CLASS                     = 0x1C

INS_MONITOR_ENTER                   = 0x1D
INS_MONITOR_EXIT                    = 0x1E
INS_CHECK_CAST                      = 0x1F
INS_INSTANCE_OF                     = 0x20

INS_ARRAY_LENGTH                    = 0x21
INS_NEW_INSTANCE                    = 0x22
INS_NEW_ARRAY                       = 0x23
INS_FILLED_NEW_ARRAY                = 0x24
INS_FILEED_NEW_ARRAY_RANGE          = 0x25
INS_FILL_ARRAY_DATA                 = 0x26

INS_THROW                           = 0x27
INS_GOTO                            = 0x28
INS_GOTO16                          = 0x29
INS_GOTO32                          = 0x2A
INS_PACKED_SWITCH                   = 0x2B
INS_SPARSE_SWITCH                   = 0x2C

INS_CMPL_FLOAT                      = 0x2D
INS_CMPG_FLOAT                      = 0x2E
INS_CMPL_DOUBLE                     = 0x2F
INS_CMPG_DOUBLE                     = 0x30
INS_CMP_LONG                        = 0x31

INS_IF_EQ                           = 0x32
INS_IF_NE                           = 0x33
INS_IF_LT                           = 0x34
INS_IF_GE                           = 0x35
INS_IF_GT                           = 0x36
INS_IF_LE                           = 0x37
INS_IF_EQZ                          = 0x38
INS_IF_NEZ                          = 0x39
INS_IF_LTZ                          = 0x3A
INS_IF_GEZ                          = 0x3B
INS_IF_GTZ                          = 0x3C
INS_IF_LEZ                          = 0x3D

INS_UNUSED_3E                       = 0x3E
INS_UNUSED_3F                       = 0x3F
INS_UNUSED_40                       = 0x40
INS_UNUSED_41                       = 0x41
INS_UNUSED_42                       = 0x42
INS_UNUSED_43                       = 0x43

INS_AGET                            = 0x44
INS_AGET_WIDE                       = 0x45
INS_AGET_OBJECT                     = 0x46
INS_AGET_BOOLEAN                    = 0x47
INS_AGET_BYTE                       = 0x48
INS_AGET_CHAR                       = 0x49
INS_AGET_SHORT                      = 0x4A
INS_APUT                            = 0x4B
INS_APUT_WIDE                       = 0x4C
INS_APUT_OBJECT                     = 0x4D
INS_APUT_BOOLEAN                    = 0x4E
INS_APUT_BYTE                       = 0x4F
INS_APUT_CHAR                       = 0x50
INS_APUT_SHORT                      = 0x51

INS_IGET                            = 0x52
INS_IGET_WIDE                       = 0x53
INS_IGET_OBJECT                     = 0x54
INS_IGET_BOOLEAN                    = 0x55
INS_IGET_BYTE                       = 0x56
INS_IGET_CHAR                       = 0x57
INS_IGET_SHORT                      = 0x58
INS_IPUT                            = 0x59
INS_IPUT_WIDE                       = 0x5A
INS_IPUT_OBJECT                     = 0x5B
INS_IPUT_BOOLEAN                    = 0x5C
INS_IPUT_BYTE                       = 0x5D
INS_IPUT_CHAR                       = 0x5E
INS_IPUT_SHORT                      = 0x5F

INS_SGET                            = 0x60
INS_SGET_WIDE                       = 0x61
INS_SGET_OBJECT                     = 0x62
INS_SGET_BOOLEAN                    = 0x63
INS_SGET_BYTE                       = 0x64
INS_SGET_CHAR                       = 0x65
INS_SGET_SHORT                      = 0x66
INS_SPUT                            = 0x67
INS_SPUT_WIDE                       = 0x68
INS_SPUT_OBJECT                     = 0x69
INS_SPUT_BOOLEAN                    = 0x6A
INS_SPUT_BYTE                       = 0x6B
INS_SPUT_CHAR                       = 0x6C
INS_SPUT_SHORT                      = 0x6D

INS_INVOKE_VIRTUAL                  = 0x6E
INS_INVOKE_SUPER                    = 0x6F
INS_INVOKE_DIRECT                   = 0x70
INS_INVOKE_STATIC                   = 0x71
INS_INVOKE_INTERFACE                = 0x72
INS_UNUSED73                        = 0x73

INS_INVOKE_VIRTUAL_RANGE            = 0x74
INS_INVOKE_SUPER_RANGE              = 0x75
INS_INVOKE_DIRECT_RANGE             = 0x76
INS_INVOKE_STATIC_RANGE             = 0x77
INS_INVOKE_INTERFACE_RANGE          = 0x78
INS_UNUSED79                        = 0x79
INS_UNUSED7A                        = 0x7A

INS_NEG_INT                         = 0x7B
INS_NOT_INT                         = 0x7C
INS_NEG_LONG                        = 0x7D
INS_NOT_LONG                        = 0x7E
INS_NEG_FLOAT                       = 0x7F
INS_NEG_DOUBLE                      = 0x80
INS_INT_TO_LONG                     = 0x81
INS_INT_TO_FLOAT                    = 0x82
INS_INT_TO_DOUBLE                   = 0x83
INS_LONG_TO_INT                     = 0x84
INS_LONG_TO_FLOAT                   = 0x85
INS_LONG_TO_DOUBLE                  = 0x86
INS_FLOAT_TO_INT                    = 0x87
INS_FLOAT_TO_LONG                   = 0x88
INS_FLOAT_TO_DOUBLE                 = 0x89
INS_DOUBLE_TO_INT                   = 0x8A
INS_DOUBLE_TO_LONG                  = 0x8B
INS_DOUBLE_TO_FLOAT                 = 0x8C
INS_INT_TO_BYTE                     = 0x8D
INS_INT_TO_CHAR                     = 0x8E
INS_INT_TO_SHORT                    = 0x8F

INS_ADD_INT                         = 0x90
INS_SUB_INT                         = 0x91
INS_MUL_INT                         = 0x92
INS_DIV_INT                         = 0x93
INS_REM_INT                         = 0x94
INS_AND_INT                         = 0x95
INS_OR_INT                          = 0x96
INS_XOR_INT                         = 0x97
INS_SHL_INT                         = 0x98
INS_SHR_INT                         = 0x99
INS_USHR_INT                        = 0x9A
INS_ADD_LONG                        = 0x9B
INS_SUB_LONG                        = 0x9C
INS_MUL_LONG                        = 0x9D
INS_DIV_LONG                        = 0x9E
INS_REM_LONG                        = 0x9F
INS_AND_LONG                        = 0xA0
INS_OR_LONG                         = 0xA1
INS_XOR_LONG                        = 0xA2
INS_SHL_LONG                        = 0xA3
INS_SHR_LONG                        = 0xA4
INS_USHR_LONG                       = 0xA5
INS_ADD_FLOAT                       = 0xA6
INS_SUB_FLOAT                       = 0xA7
INS_MUL_FLOAT                       = 0xA8
INS_DIV_FLOAT                       = 0xA9
INS_REM_FLOAT                       = 0xAA
INS_ADD_DOUBLE                      = 0xAB
INS_SUB_DOUBLE                      = 0xAC
INS_MUL_DOUBLE                      = 0xAD
INS_DIV_DOUBLE                      = 0xAE
INS_REM_DOUBLE                      = 0xAF

INS_ADD_INT_2ADDR                   = 0xB0
INS_SUB_INT_2ADDR                   = 0xB1
INS_MUL_INT_2ADDR                   = 0xB2
INS_DIV_INT_2ADDR                   = 0xB3
INS_REM_INT_2ADDR                   = 0xB4
INS_AND_INT_2ADDR                   = 0xB5
INS_OR_INT_2ADDR                    = 0xB6
INS_XOR_INT_2ADDR                   = 0xB7
INS_SHL_INT_2ADDR                   = 0xB8
INS_SHR_INT_2ADDR                   = 0xB9
INS_USHR_INT_2ADDR                  = 0xBA
INS_ADD_LONG_2ADDR                  = 0xBB
INS_SUB_LONG_2ADDR                  = 0xBC
INS_MUL_LONG_2ADDR                  = 0xBD
INS_DIV_LONG_2ADDR                  = 0xBE
INS_REM_LONG_2ADDR                  = 0xBF
INS_AND_LONG_2ADDR                  = 0xC0
INS_OR_LONG_2ADDR                   = 0xC1
INS_XOR_LONG_2ADDR                  = 0xC2
INS_SHL_LONG_2ADDR                  = 0xC3
INS_SHR_LONG_2ADDR                  = 0xC4
INS_USHR_LONG_2ADDR                 = 0xC5
INS_ADD_FLOAT_2ADDR                 = 0xC6
INS_SUB_FLOAT_2ADDR                 = 0xC7
INS_MUL_FLOAT_2ADDR                 = 0xC8
INS_DIV_FLOAT_2ADDR                 = 0xC9
INS_REM_FLOAT_2ADDR                 = 0xCA
INS_ADD_DOUBLE_2ADDR                = 0xCB
INS_SUB_DOUBLE_2ADDR                = 0xCC
INS_MUL_DOUBLE_2ADDR                = 0xCD
INS_DIV_DOUBLE_2ADDR                = 0xCE
INS_REM_DOUBLE_2ADDR                = 0xCF

INS_ADD_INT_LIT16                   = 0xD0
INS_SUB_INT_LIT16                   = 0xD1
INS_MUL_INT_LIT16                   = 0xD2
INS_DIV_INT_LIT16                   = 0xD3
INS_REM_INT_LIT16                   = 0xD4
INS_AND_INT_LIT16                   = 0xD5
INS_OR_INT_LIT16                    = 0xD6
INS_XOR_INT_LIT16                   = 0xD7
INS_ADD_INT_LIT8                    = 0xD8
INS_SUB_INT_LIT8                    = 0xD9
INS_MUL_INT_LIT8                    = 0xDA
INS_DIV_INT_LIT8                    = 0xDB
INS_REM_INT_LIT8                    = 0xDC
INS_AND_INT_LIT8                    = 0xDD
INS_OR_INT_LIT8                     = 0xDE
INS_XOR_INT_LIT8                    = 0xDF
INS_SHL_INT_LIT8                    = 0xE0
INS_SHR_INT_LIT8                    = 0xE1
INS_USHR_INT_LIT8                   = 0xE2
INS_UNUSEDE3                        = 0xE3
INS_UNUSEDE4                        = 0xE4
INS_UNUSEDE5                        = 0xE5
INS_UNUSEDE6                        = 0xE6
INS_UNUSEDE7                        = 0xE7
INS_UNUSEDE8                        = 0xE8
INS_UNUSEDE9                        = 0xE9
INS_UNUSEDEA                        = 0xEA
INS_UNUSEDEB                        = 0xEB
INS_UNUSEDEC                        = 0xEC
INS_UNUSEDED                        = 0xED

INS_EXECUTE_INLINE                  = 0xEE
INS_UNUSEDEF                        = 0xEF

INS_INVOKE_DIRECT_EMPTY             = 0xF0
INS_UNUSEDF1                        = 0xF1

INS_IGET_QUICK                      = 0xF2
INS_IGET_WIDE_QUICK                 = 0xF3
INS_IGET_OBJECT_QUICK               = 0xF4
INS_IPUT_QUICK                      = 0xF5
INS_IPUT_WIDE_QUICK                 = 0xF6
INS_IPUT_OBJECT_QUICK               = 0xF7
INS_INVOKE_VIRTUAL_QUICK            = 0xF8
INS_INVOKE_VIRTUAL_QUICK_RANGE      = 0xF9
INS_INVOKE_SUPER_QUICK              = 0xFA
INS_INVOKE_SUPER_QUICK_RANGE        = 0xFB
INS_UNUSEDFC                        = 0xFC
INS_UNUSEDFD                        = 0xFD
INS_UNUSEDFE                        = 0xFE
INS_UNUSEDFF                        = 0xFF

SMALI_OPCODE_DEF = [
    [INS_NOP,2],
    [INS_MOVE,2], [INS_MOVE_FROM16,4], [INS_MOVE16,4], [INS_MOVE_WIDE,2], [INS_MOVE_WIDE_FROM16,4], [INS_MOVE_WIDE16,4], [INS_MOVE_OBJECT,2],
    [INS_MOVE_OBJECT_FROM16,4], [INS_MOVE_OBJECT16,4], [INS_MOVE_RESULT,2], [INS_MOVE_RESULT_WIDE,2], [INS_MOVE_RESULT_OBJECT,2], [INS_MOVE_EXCEPTION,2],
    [INS_RETURN_VOID,2], [INS_RETURN,2], [INS_RETURN_WIDE,2], [INS_RETURN_OBJECT,2],
    [INS_CONST4,2], [INS_CONST16,4], [INS_CONST,6], [INS_CONST_HIGH16,4], [INS_CONST_WIDE16,4], [INS_CONST_WIDE32,6], [INS_CONST_WIDE,10], [INS_CONST_WIDE_HIGH16,4],
    [INS_CONST_STRING,4], [INS_CONST_STRING_JUMBO,4], [INS_CONST_CLASS,4],
    [INS_MONITOR_ENTER,2], [INS_MONITOR_EXIT,2], [INS_CHECK_CAST,4], [INS_INSTANCE_OF,4],
    [INS_ARRAY_LENGTH,2], [INS_NEW_INSTANCE,4], [INS_NEW_ARRAY,4], [INS_FILLED_NEW_ARRAY,6], [INS_FILEED_NEW_ARRAY_RANGE,6], [INS_FILL_ARRAY_DATA,6],
    [INS_THROW,2], [INS_GOTO,2], [INS_GOTO16,4], [INS_GOTO32,6], [INS_PACKED_SWITCH,6], [INS_SPARSE_SWITCH,6],
    [INS_CMPL_FLOAT,4], [INS_CMPG_FLOAT,4], [INS_CMPL_DOUBLE,4], [INS_CMPG_DOUBLE,4], [INS_CMP_LONG,4],
    [INS_IF_EQ,4], [INS_IF_NE,4], [INS_IF_LT,4], [INS_IF_GE,4], [INS_IF_GT,4], [INS_IF_LE,4],
    [INS_IF_EQZ,4], [INS_IF_NEZ,4], [INS_IF_LTZ,4], [INS_IF_GEZ,4], [INS_IF_GTZ,4], [INS_IF_LEZ,4],
    [INS_UNUSED_3E,-1], [INS_UNUSED_3F,-1], [INS_UNUSED_40,-1],[INS_UNUSED_41,-1],[INS_UNUSED_42,-1],[INS_UNUSED_43,-1],
    [INS_AGET,4], [INS_AGET_WIDE,4], [INS_AGET_OBJECT,4], [INS_AGET_BOOLEAN,4], [INS_AGET_BYTE,4], [INS_AGET_CHAR,4], [INS_AGET_SHORT,4],
    [INS_APUT,4], [INS_APUT_WIDE,4], [INS_APUT_OBJECT,4], [INS_APUT_BOOLEAN,4], [INS_APUT_BYTE,4], [INS_APUT_CHAR,4], [INS_APUT_SHORT,4],
    [INS_IGET,4], [INS_IGET_WIDE,4], [INS_IGET_OBJECT,4], [INS_IGET_BOOLEAN,4], [INS_IGET_BYTE,4], [INS_IGET_CHAR,4], [INS_IGET_SHORT,4],
    [INS_IPUT,4], [INS_IPUT_WIDE,4], [INS_IPUT_OBJECT,4], [INS_IPUT_BOOLEAN,4], [INS_IPUT_BYTE,4], [INS_IPUT_CHAR,4], [INS_IPUT_SHORT,4],
    [INS_SGET,4], [INS_SGET_WIDE,4], [INS_SGET_OBJECT,4], [INS_SGET_BOOLEAN,4], [INS_SGET_BYTE,4], [INS_SGET_CHAR,4], [INS_SGET_SHORT,4],
    [INS_SPUT,4], [INS_SPUT_WIDE,4], [INS_SPUT_OBJECT,4], [INS_SPUT_BOOLEAN,4], [INS_SPUT_BYTE,4], [INS_SPUT_CHAR,4], [INS_SPUT_SHORT,4],
    [INS_INVOKE_VIRTUAL, 6], [INS_INVOKE_SUPER, 6], [INS_INVOKE_DIRECT, 6], [INS_INVOKE_STATIC, 6],
    [INS_INVOKE_INTERFACE, 6], [INS_UNUSED73, -1],
    [INS_INVOKE_VIRTUAL_RANGE, 6], [INS_INVOKE_SUPER_RANGE, 6], [INS_INVOKE_DIRECT_RANGE, 6],
    [INS_INVOKE_STATIC_RANGE, 6], [INS_INVOKE_INTERFACE_RANGE, 6], [INS_UNUSED79, -1], [INS_UNUSED7A, -1],
    [INS_NEG_INT, 2], [INS_NOT_INT, 2], [INS_NEG_LONG, 2], [INS_NOT_LONG, 2], [INS_NEG_FLOAT, 2], [INS_NEG_DOUBLE, 2],
    [INS_INT_TO_LONG, 2], [INS_INT_TO_FLOAT, 2], [INS_INT_TO_DOUBLE, 2],
    [INS_LONG_TO_INT, 2], [INS_LONG_TO_FLOAT, 2], [INS_LONG_TO_DOUBLE, 2], [INS_FLOAT_TO_INT, 2],
    [INS_FLOAT_TO_LONG, 2], [INS_FLOAT_TO_DOUBLE, 2], [INS_DOUBLE_TO_INT, 2],
    [INS_DOUBLE_TO_LONG, 2], [INS_DOUBLE_TO_FLOAT, 2], [INS_INT_TO_BYTE, 2], [INS_INT_TO_CHAR, 2],
    [INS_INT_TO_SHORT, 2],
    [INS_ADD_INT, 4], [INS_SUB_INT, 4], [INS_MUL_INT, 4], [INS_DIV_INT, 4], [INS_REM_INT, 4], [INS_AND_INT, 4],
    [INS_OR_INT, 4], [INS_XOR_INT, 4], [INS_SHL_INT, 4], [INS_SHR_INT, 4], [INS_USHR_INT, 4],
    [INS_ADD_LONG, 4], [INS_SUB_LONG, 4], [INS_MUL_LONG, 4], [INS_DIV_LONG, 4], [INS_REM_LONG, 4], [INS_AND_LONG, 4],
    [INS_OR_LONG, 4], [INS_XOR_LONG, 4], [INS_SHL_LONG, 4], [INS_SHR_LONG, 4], [INS_USHR_LONG, 4],
    [INS_ADD_FLOAT, 4], [INS_SUB_FLOAT, 4], [INS_MUL_FLOAT, 4], [INS_DIV_FLOAT, 4], [INS_REM_FLOAT, 4],
    [INS_ADD_DOUBLE, 4], [INS_SUB_DOUBLE, 4], [INS_MUL_DOUBLE, 4], [INS_DIV_DOUBLE, 4], [INS_REM_DOUBLE, 4],
    [INS_ADD_INT_2ADDR,2], [INS_SUB_INT_2ADDR,2], [INS_MUL_INT_2ADDR,2], [INS_DIV_INT_2ADDR,2], [INS_REM_INT_2ADDR,2], [INS_AND_INT_2ADDR,2], [INS_OR_INT_2ADDR,2],
    [INS_XOR_INT_2ADDR,2], [INS_SHL_INT_2ADDR,2], [INS_SHR_INT_2ADDR,2], [INS_USHR_INT_2ADDR,2], [INS_ADD_LONG_2ADDR,2],
    [INS_SUB_LONG_2ADDR,2], [INS_MUL_LONG_2ADDR,2], [INS_DIV_LONG_2ADDR,2], [INS_REM_LONG_2ADDR,2], [INS_AND_LONG_2ADDR,2],[INS_OR_LONG_2ADDR,2], [INS_XOR_LONG_2ADDR,2],
    [INS_SHL_LONG_2ADDR,2], [INS_SHR_LONG_2ADDR,2], [INS_USHR_LONG_2ADDR,2], [INS_ADD_FLOAT_2ADDR,2], [INS_SUB_FLOAT_2ADDR,2], [INS_MUL_FLOAT_2ADDR,2], [INS_DIV_FLOAT_2ADDR,2],
    [INS_REM_FLOAT_2ADDR,2], [INS_ADD_DOUBLE_2ADDR,2], [INS_SUB_DOUBLE_2ADDR,2], [INS_MUL_DOUBLE_2ADDR,2], [INS_DIV_DOUBLE_2ADDR,2], [INS_REM_DOUBLE_2ADDR,2],
    [INS_ADD_INT_LIT16,4], [INS_SUB_INT_LIT16,4], [INS_MUL_INT_LIT16,4], [INS_DIV_INT_LIT16,4], [INS_REM_INT_LIT16,4], [INS_AND_INT_LIT16,4], [INS_OR_INT_LIT16,4], [INS_XOR_INT_LIT16,4],
    [INS_ADD_INT_LIT8,4], [INS_SUB_INT_LIT8,4], [INS_MUL_INT_LIT8,4], [INS_DIV_INT_LIT8,4], [INS_REM_INT_LIT8,4], [INS_AND_INT_LIT8,4], [INS_OR_INT_LIT8,4], [INS_XOR_INT_LIT8,4],
    [INS_SHL_INT_LIT8,4], [INS_SHR_INT_LIT8,4], [INS_USHR_INT_LIT8,4], [INS_UNUSEDE3,-1], [INS_UNUSEDE4,-1], [INS_UNUSEDE5,-1],
    [INS_UNUSEDE6,-1], [INS_UNUSEDE7,-1], [INS_UNUSEDE8,-1], [INS_UNUSEDE9,-1], [INS_UNUSEDEA,-1], [INS_UNUSEDEB,-1], [INS_UNUSEDEC,-1], [INS_UNUSEDED,-1],
    [INS_EXECUTE_INLINE,6], [INS_UNUSEDEF,-1], [INS_INVOKE_DIRECT_EMPTY,6], [INS_UNUSEDF1,-1],
    [INS_IGET_QUICK,4], [INS_IGET_WIDE_QUICK,4], [INS_IGET_OBJECT_QUICK,4], [INS_IPUT_QUICK,4], [INS_IPUT_WIDE_QUICK,4], [INS_IPUT_OBJECT_QUICK,4],
    [INS_INVOKE_VIRTUAL_QUICK,6], [INS_INVOKE_VIRTUAL_QUICK_RANGE,6], [INS_INVOKE_SUPER_QUICK,6], [INS_INVOKE_SUPER_QUICK_RANGE,6],
    [INS_UNUSEDFC,-1], [INS_UNUSEDFD,-1], [INS_UNUSEDFE,-1], [INS_UNUSEDFF,-1],
]