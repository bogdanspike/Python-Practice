with open("Log.txt",'r') as logg:
    k=0
    for i in logg:
        stat=i.split()
        if stat[-1]=="ON":
            print("Porneste la:",stat[0:3])
        elif stat[-1]=='ERR':
            k+=1
            print("Are eroare la:",stat[0:3])
        else:
             print("Se inchide la:",stat[0:3])   
    print("Numar total de erori:",k)
            
