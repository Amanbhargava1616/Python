# https://www.tutorialspoint.com/python/os_file_methods.htm

import os
from time import sleep

# os.rename("file_to_rename.txt", "renamed_file.txt")
# sleep(2)
# os.remove("renamed_file.txt")


print(os.path.exists("./file_handling_1.py"))


current_dire = os.getcwd()
print(current_dire)
