"""9-11 import admin module and test class and methods"""
from admin import Admin

# Testing class Admin and its methods
admin_1 = Admin('ron', 'swanson')

admin_1.describe_user()
admin_1.privileges.show_privileges()

# Testing class Admin and Privileges methods
admin_2 = Admin('leslie', 'knope')

admin_2.describe_user()
admin_2.privileges.show_privileges()