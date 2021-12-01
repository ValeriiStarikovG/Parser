import glob

# Add lines to list as elements
def getLinesFromFile(file) -> list:
    f = open(file, 'r')
    sList = []
    for line in f:
        line = line.replace('\n', '')
        sList.append(line)
    f.close() 
    return sList

# Find needed rows and add to list under right key
def getNeededRows(sList : list, sMap : dict, delimiter : str, params : list):
    for s in sList:
        prt = s.rsplit(delimiter)
        for param in params:
            if (prt[0] == param):
                if (prt[0] not in sMap):
                    sMap[prt[0]] = []
                sMap[prt[0]].append(prt[1])


# main_input
list_of_files = glob.glob('input/*.txt') 
sMap = {}
for file in list_of_files:
    sList = getLinesFromFile(file)
    getNeededRows(sList, sMap, ': ', ['a', 'e', 'new', 'g'])
print(sMap)
print()


#main_output
output_file = open('output/output.txt', 'a')
for key in sMap:
    output_file.write(key + ' ::: ')
    for element in sMap[key]:
        output_file.write(element + ', ')
    output_file.write('\n')

output_file.close()