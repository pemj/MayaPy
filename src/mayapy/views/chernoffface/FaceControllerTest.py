import FaceController
import time


functions = dir(FaceController)
ignore = ["mc", "sm", "__.*__"]
functions = filter(lambda x: x not in ignore, functions)
functions = filter(lambda x: '_' not in x, functions)

count = 0
for function_name_outer in functions:
    method_to_call_outer = getattr(FaceController, function_name_outer)
    for i in [-100, 100, 0]:
        method_to_call_outer(i)
        for function_name in functions:
            methodToCall = getattr(FaceController, function_name)
            for j in [-100, 100, 0]:
                count += 1
                print "count: {0} -- {1}: {2} -- {3}: {4}".format(count, function_name_outer, i, function_name, j)
                methodToCall(j)
                time.sleep(.5)
