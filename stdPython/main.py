
#===============================================================================
# import os
# import time
# import re #Regular Expressions
# from Kitchen import Recipe
# from os.path import join, getsize
# import find
#===============================================================================

#===============================================================================
# def add(a,b):
#     return a+b
# def print_dir_info(dir_path):
#     for name in os.listdir(dir_path):
#         full_path = os.path.join(dir_path, name)
#         file_size = os.path.getsize(full_path)
#         mod_time = time.ctime(os.path.getmtime(full_path))
#         print("%-32s: %8d bytes, modified %s" % (name, file_size, mod_time))
#  
# f = Recipe()
# western_ingredients = {"eggs":2, "milk":1, "cheese":1, "ham":1, "peppers":1, "onion":1}
# f.create("western", western_ingredients)
# print(f.recipes)
#  
# print("---------------------------")    
# print_dir_info(os.getcwd())
# print("---------------------------")    
# for root, dirs, files in os.walk(os.getcwd()):
#     print(root, "consumes", end="")
#     print(sum([getsize(join(root, name)) for name in files]), end="")
#     print("bytes in", len(files), "non-directory files")
#      
# def print_pdf (root, dirs, files):
#     for file in files:
#         path = os.path.join (root, file)
#         path = os.path.normcase (path)
#         if not re.search (r".*\.pdf", path): continue
#         if re.search (r" ", path): continue
#         print(path)
#         
# for root, dirs, files in os.walk('C:\\Download\\Application'):
#     print_pdf(root, dirs, files)
# print("---------------------------")    
# s = ('xxx', 'abcxxxabc', 'xyx', 'abc', 'x.x', 'axa', 'axxxxa', 'axxya')
# a=filter ((lambda s: re.match(r"xxx", s)), s)
# b=filter ((lambda s: re.search(r"xxx", s)), s)
# print(*a)
# print(*b)
# 
# print(find.find(r"py$", content='find'))
#===============================================================================
import dbm
db = dbm.open('websites', 'c')
# Add an item.
db['www.python.org'] = 'Python home page'
print(db['www.python.org'])
# Close and save to disk.
db.close()