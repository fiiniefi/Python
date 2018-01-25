import os
import re

def merge(d1, d2):
    for key in d2:
        if key in d1.keys():
            d1[key] += d2[key]
        else:
            d1[key] = d2[key]

def calls(directory):
    dic = calls_inside(directory)
    for key in dic:
        yield (key, dic[key])

def calls_inside(directory):
    dic = {}
    for filen in os.listdir(directory):
        if re.match(".*\.html", filen):
            f = open(directory + "\\\\" + filen, 'r')
            refs = re.findall('<a.*href="(.*)">', f.read())
            f.close()
            for ref in refs:
                if not re.match("(http).*", ref):
                    ref = os.path.basename(ref)
                    if ref in dic.keys():
                        dic[ref] += [filen]
                    else:
                        dic[ref] = [filen]
        elif os.path.isdir(directory + "\\\\" + filen):
            merge(dic, calls_inside(directory + "\\\\" + filen))
    return dic


for (key, val) in calls(os.getcwd()):
    print(key, "- - -", val)
