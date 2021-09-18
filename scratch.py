import os
import fileinput

for root, dirs, files in os.walk('viatools/sync3scales'):
    for filename in [filename_ for filename_ in files if '.json' in filename_]:
        with open(root + '/' + filename, 'r') as file:
            contents = file.read() 
        contents = contents.replace('fill', 'expand') 
        print(contents)
        with open(root + '/' + filename, 'w') as file:
            file.write(contents) 
