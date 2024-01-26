import os
import threading

responders = []

def p(ip):
    global responders
    response = os.system("ping -n 1 -w 50 " + ip)
    if response == 0:
        responders.append(ip)

if __name__ == "__main__":
    threads = []
    for i in range(1,256):
        ip = "192.168.0." + str(i)
        t = threading.Thread(target=p, args=(ip,))
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()
        
    responders.sort()
    print("\n\n")
    print("=============================")
    print("Responders:")
    print("=============================")
    for r in responders:
        print(r)
