def cesar_cypher(text,numar):
    cuvant=[]
    dif=0
    for i in text:
        if i==" ":
            print(" ",end='')
        elif (ord(i)+numar) > 122:
            dif=ord(i)+numar-122
            cuvant=chr(96+dif)
            print(cuvant,end='')        
        else:    
            cuvant=chr(ord(i)+numar)
            print(cuvant,end='')
           
text=input("Introduceti textul:")
numar=int(input("Introduceti n:"))        
cesar_cypher(text,numar)        
