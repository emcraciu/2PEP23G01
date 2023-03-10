# built-in decorators

class MyClass:
    my_var = None

    def __init__(abcde, my_var):
        abcde.my_var = my_var

    @classmethod  # provides class of object instead of object as first argument
    def check_class_method(abcd):
        print(f'Value is: {abcd.my_var}')

    @staticmethod  # removes the first argument from method transforming it into a function
    def check_static_method():
        #print(self.my_var)
        print('This method does not have any object info')

    # @property  # this will create a property called "my_string_var" that does not need to be called to return a value
    # def my_string_var(self):
    #     return self.my_var
    #
    # @my_string_var.setter  # this will allow us to set "my_string_var" like a variable
    # def my_string_var(self, value):
    #     if type(value) != str:
    #         raise ValueError
    #     self.my_var = value


my_object = MyClass('MyVar')
print(my_object.my_var, 'from instance')
print(my_object.__class__.my_var, "from class")
#print(MyClass.my_var)
my_object.check_class_method()
my_object.__class__.check_class_method()
my_object.check_static_method()

# print('calling class method'.center(80, "#"))
# my_object.check_class_method()
# # MyClass.check_my_var(MyClass) # this is same as above call
#
# print('calling static method'.center(80, "#"))
# my_object.check_static_method()
# # MyClass.check_static_method() # this is same as above call
#
# print('getting and setting properties'.center(80, "#"))
# print(my_object.my_string_var)  # no need to call ()
# my_object.my_string_var = "myNewValue"
#
# print("Updated value is:", my_object.my_string_var)

