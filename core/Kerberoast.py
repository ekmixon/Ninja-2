
def kerb(fname,user,domain):
    #fname="kerberoast/out.txt"
    hashfile = f"kerberoast/{user}@{domain}_hashes"
    file=open(fname,"r")
    data=file.read()
    data=data.split("############")
    SPN=data[1]                       # AV data
    Tickets=data[2]                       #  process list
    kerb=data[3]
    Hashes=kerb.split("*******")
    print ("Found Service Principle Names : \n"+SPN)
    print ("Generated Tickets : \n"+Tickets)
    print ("Output of Invoke-Kerberoast : \n"+kerb)
    print(f"Hashes saved in {hashfile}")
    with open(hashfile,"a") as f:
        print (kerb)
        for i in Hashes[1:]:
            i=i+"\n"
            f.write(i+"\n")
