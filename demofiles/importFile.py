# first import importlib.util module.
import importlib.util
 
# get python module spec from the provided python source file. The spec_from_file_location function takes two parameters, the first parameter is the module name, then second parameter is the module file full path. 
test_spec = importlib.util.spec_from_file_location("Test", "/home/.../Test.py")
 
# pass above test_spec object to module_from_spec function to get custom python module from above module spec.
test_module = importlib.util.module_from_spec(test_spec)
 
# load the module with the spec.
test_spec.loader.exec_module(test_module)
 
# # invoke the module variable.
print (test_module.user_name)
# 'jerry'
# >>> 
# # create an instance of a class in the module.
test_hello = test_module.TestHello()
# >>> 
# # call the module class's function.
test_hello.print_hello_message()
# hello jerry