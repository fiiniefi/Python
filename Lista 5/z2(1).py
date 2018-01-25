import os
import re
import requests

def active(directory):
    for filen in os.listdir(directory):
        if re.match(".*(\.)(html)", filen):
            f = open(directory + "\\\\" + filen, 'r') #doklejam poprzedzające foldery i \\ do nazwy pliku
            refs = re.findall('<a.*href="(.*)">', f.read())
            f.close()
            for ref in refs:
                if re.match("(http).*", ref):
                    if (requests.get(ref)).status_code == 200:
                        yield "Odnośnik " + ref + " jest aktywny"
                    else:
                        yield "Odnośnik " + ref + " jest nieaktywny"
                else:
                    try:
                        if re.match("[A-Z]:\.*", ref):
                            fl = open(ref, 'r')
                        else:
                            fl = open(directory + "\\\\" + ref, 'r')
                        yield "Plik " + ref + " istnieje"
                    except:
                        yield "Plik " + ref + " nie istnieje"
                    finally:
                        fl.close()
        elif os.path.isdir(directory + "\\\\" + filen):
            yield from active(directory + "\\\\" + filen) #doklejam folder, w którym się obecnie znajdujemy przed ten, w który się wgłębiamy

for ref in active(os.getcwd()):
    print(ref)
