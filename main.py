def func1(arg1, arg2):
    var66 = func2(arg1, arg2)
    var67 = (arg1 ^ arg1) & arg1 | arg2
    var68 = -841 + arg2
    var69 = var67 & -324
    var70 = var66 ^ var68 & (676 | arg1)
    var71 = (var68 & 1455973854) | var67 ^ -1565506847
    var72 = 1466612546 & var68 - var69 | var67
    var73 = (392 & var67 & 667) - var72
    var74 = -234097961 + var67 & -22368877
    var75 = arg2 | (var67 - var67 ^ var67)
    var76 = var73 + var71 ^ var69
    var77 = var74 - (var69 - var67) - var68
    var78 = arg2 ^ var72
    var79 = var75 + (var75 | var66) + var71
    var80 = -149 ^ -2088202281
    var81 = (arg2 | var68 ^ arg2) | var70
    var82 = var68 - var80 | (var77 | var69)
    var83 = (var68 | var68) ^ 1831959912
    var84 = var74 + var66
    var85 = (var72 ^ arg1) - var82 | -1501976002
    var86 = var80 + (var68 & -895)
    var87 = (var85 & var68 - var75) - var66
    var88 = arg1 & arg1
    if var88 < var66:
        var89 = (var74 | 1173541051) | var85 + var86
    else:
        var89 = var70 - var88 & var75 + var74
    var90 = var85 ^ -1062119257
    result = ((var74 & var87) ^ 626 ^ var79 & ((var82 | var71 | var86 + var85) ^ var84) | var84 + var67) | -370952644
    return result
def func2(arg3, arg4):
    def func3(arg5, arg6):
        var7 = (arg6 | arg5 - 593) + arg3
        var8 = ((var7 | arg3) | var7) - arg6
        var9 = (arg4 + arg5 ^ -1309069057) - arg5
        var10 = -449 - var9
        var11 = arg3 + var9
        var12 = (-248 | 1092014791) & 320 & var8
        var13 = (var7 ^ var12 + var7) + arg6
        var14 = arg4 & arg5
        var15 = var7 | var13
        if var8 < var13:
            var16 = (var12 + -116717660 ^ var9) + var14
        else:
            var16 = arg4 | 2135607526 + var11 - var12
        var17 = var12 + arg5
        if var12 < var10:
            var18 = var8 & ((-247937074 ^ arg5) + arg4)
        else:
            var18 = var10 + arg6 | arg4
        var19 = var12 + (var11 & var14) ^ var10
        var20 = ((-854 + var11) | var12) & var10
        var21 = ((var7 + var10) - var20) - var11
        var22 = (var20 - arg3) | (var13 & var8)
        var23 = -992 + var8 + var11
        var24 = arg3 & (var15 | var9 | var9)
        var25 = arg4 & ((var17 & var7) | arg5)
        var26 = arg3 | arg4
        result = var14 + var9
        return result
    var27 = func3(arg3, arg4)
    var31 = func4(arg4, arg3)
    if arg4 < arg4:
        var36 = class6()
    else:
        var36 = class8()
    for var37 in range(23):
        var36.func7(var27, arg3)
    var55 = func10(var31, arg3)
    var56 = (arg4 | (var27 & var55)) | var55
    var57 = var55 | (var55 ^ var56) + var27
    var58 = var27 - var31 + var27
    var59 = -660942978 & var56 | arg4 & var31
    var60 = var57 - var59 + -1946349963
    var61 = var31 & arg3
    var62 = 904 - var61 | 149264445 ^ var56
    var63 = (var56 | arg3) | var60 ^ 134
    var64 = (var31 - var57 - var27) ^ var62
    var65 = (var62 & -1178688288 - arg3) | var60
    result = (var27 - var31) ^ var65 | var31
    return result
def func10(arg38, arg39):
    var40 = 1893237622 + 680658035
    var41 = (-1855201986 + 909) & -479
    var42 = (arg39 & 1056704380) & (var40 & 16)
    var43 = arg38 ^ arg38 + 276 - var42
    var44 = var43 | (var40 ^ -1020558737) | arg39
    var45 = arg39 ^ 248
    var46 = var45 + 543503046 & var41 & var45
    var47 = var44 | var40 - var40
    var48 = var41 | var45 & var45
    var49 = var40 + (var47 - arg39 | var42)
    var50 = (var49 - arg39) | var44 + var46
    var51 = (var41 + var47 - 527) ^ var45
    var52 = var46 & (var40 | var48)
    var53 = var40 ^ (arg39 & var42)
    var54 = -605 + 561859492 | var52 | var46
    result = var40 & (var45 - (var44 - arg38 ^ var53 - var53)) ^ var53 + arg39
    return result
class class8(object):
    def func7(self, arg34, arg35):
        result = (arg34 + ((arg34 | ((arg35 | 0) & -944335133)) & 0)) & arg35
        return result
class class6(class8):
    def func7(self, arg32, arg33):
        result = arg32 ^ (-1 + arg32)
        return result
def func4(arg28, arg29):
    def func5(acc, rest):
        var30 = -2 + -3 | -2
        if acc == 0:
            return var30
        else:
            result = func5(acc - 1, var30)
            return result
    result = func5(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 91'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,