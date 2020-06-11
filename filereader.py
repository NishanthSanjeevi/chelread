import os
cache_dict = dict()
repo_cache = dict()
d = dict()
# active_dict = dict()
repoId = 0

MyCacheFileLocation = os.path.dirname(os.path.abspath(__file__)) + "\\Cache.txt"
CacheFile = open(MyCacheFileLocation, 'w+')        
def throw(e):
    raise Exception(e)

def setPath(path, file):
    return str(path+'\\'+file)


def setPathList(path,file_list):
    for i in range(len(file_list)):
        file_list[i] = setPath(path,file_list[i])
    return file_list

def convertTabsToSpaces(s):
    s = s.split('\t')
    s = str(" ".join(s))
    return s

def PopulateDict():
    return ""


    
def addToDictUtil(line,file,line_number):
    l = line.split()

    s = str(file +":"+str(line_number))

    for i in l:
        if i == '':
            continue
        if i in d:
            d[i].append(s)
        else:
            d[i] = [s]        
    

def addToDict(current_file):
    

    try:
        f = open(current_file,'r')
    except:
        print("unable to open",current_file)
        return
        
    # alllines = f.readlines()
    # f.seek(0)
    # print(alllines)

    try:
        current_line = f.readline().strip()
        current_line_number = 1
    except:
        return
    
    while current_line:
        # print(current_line)
        # current_line = convertTabsToSpaces(current_line)
        # print(current_line)

        addToDictUtil(current_line, current_file, current_line_number)


        current_line_number += 1
        try:
            current_line = f.readline().strip()
        except:
            continue



    f.close()

def Cache(d):
    if len(d) != 0:
        repo_cache[path] = repoId
        repoId+=1
        cache_dict[repoId] = d
        d = {}
        return
    throw("Invalid Caching attempted")

def fileList(path,recursion=False):
    try:
        Cache(d)
    except:
        e = "sake of exception"

        
    file_list = setPathList(path,os.listdir(path))
    #print(file_list)

    if recursion == True:
        for i in file_list:
            if "." not in i:
                try:
                    recursive_file_list = setPathList(i,os.listdir(i))
                    file_list += recursive_file_list

                except:
                    e = "sake of exception"
                    # print("File without extension, not directory : ", i)
    #print(file_list)


    for i in file_list:
        if "." in i:
            addToDict(i)

            
    print("SUCCESS...")


    
def Search(s):
    if len(d) == 0:
        throw("Need to populate")
        return

    l = d[s]
    for i in l:
        print(i)
                
def IsCached(path):
    if path in repo_cache:
        return True
    return False

def fetchFromCache(path):
    if IsCached(path):
        try:
            Cache(d)
        except:
            e = "sake of exception"
        d = cache_dict[repo_cache[path]]
        print("cache set")
        


s = Search
    
fl = fileList


