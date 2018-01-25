import os
import re
import requests
import threading
import queue

def file_handling(directory, filen, que):
    f = open(directory + "\\\\" + filen, 'r') #doklejam poprzedzające foldery i \\ do nazwy pliku
    refs = re.findall('<a.*href="(.*)">', f.read())
    f.close()
    for ref in refs:
        if re.match("(http).*", ref):
            if (requests.get(ref)).status_code == 200:
                que.put("Odnośnik " + ref + " jest aktywny")
            else:
                que.put("Odnośnik " + ref + " jest nieaktywny")
        else:
            try:
                if re.match("[A-Z]:\.*", ref):
                    fl = open(ref, 'r')
                else:
                    fl = open(directory + "\\\\" + ref, 'r')
                que.put("Plik " + ref + " istnieje")
            except:
                que.put("Plik " + ref + " nie istnieje")
            finally:
                fl.close()

def active_inside(directory, que):
    lista_watkow = []
    for filen in os.listdir(directory):
        if re.match(".*(\.)(html)", filen):
            th = threading.Thread(target = file_handling, args = (directory, filen, que))
            th.start()
            lista_watkow.append(th)
        elif os.path.isdir(directory + "\\\\" + filen):
            th = threading.Thread(target = active_inside, args = (directory + "\\\\" + filen, que)) #doklejam folder, w którym się obecnie znajdujemy przed ten, w który się wgłębiamy
            th.start()
            lista_watkow.append(th)
    for w in lista_watkow:
        w.join()

def active(directory):
    que = queue.Queue()
    active_inside(directory, que)
    #print(que.qsize())
    for i in range(0, que.qsize()):
        yield que.get()


for ref in active(os.getcwd()):
    print(ref)
