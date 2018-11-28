import os
print("please enter the location")
location = raw_input("")
os.chdir(location)
items = os.listdir(location)
if items <= 0:
    print("folder is empty")
else:
    print(items)
    print("new name?")
    newName = raw_input()
    print(newName)
    i = 0
    print(format(i, '02d'))
    print(items[1])
    print(len(os.listdir(location)))
    for i in range(len(os.listdir(location))):
        ex = items[i].split('.')
        exsten = ex[len(ex)-1]
        print("changings " + items[i] + " to " + newName + (format(i+1, '02d')) + '.' + exsten)
        os.rename(items[i], newName + (format(i+1, '02d')) + '.' + exsten)
raw_input()
