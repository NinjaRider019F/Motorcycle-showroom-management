import mysql.connector
F=2
while 1:
    print("###############WELCOME TO KAWASAKI###############")
    user=input("Enter your username:")
    pas=input("Enter your password:")
    
    print()
    if pas=="4321" and user=='JATIN':
        d=mysql.connector.connect(host='localhost',user='root',password="")
        c=d.cursor()        
        c.execute('create database if not exists Kawasaki;')
        c.execute('use Kawasaki;')
        for x in c:
            print(x)
            
        c.execute('create table if not exists series(Sno int,Model char(50),Price char(20),Engine char(20),Torque char(20),Braking_system char(20),TOP_SPEED char(20));')
        c.execute("show tables;")
        for w in c:
            print(w)
            
        print("###############WELCOME TO THE WORLD OF SPEED###############")  
        print()
        while 1:
            
            print()
            print("  How can I assist you sir?")
            print()
            print("1.Add a bike?:- ")
            print("2.Update an existing bike:- ")
            print("3.Delete any bike's record:- ")
            print("4.Show details of a bike:-")
            print("5.About KAWASAKI:- ")
            print("6.Show most demanded features")
            print("7.Exit")
            print()
            n=int(input("Enter your choice:"))
            
            if n==1:
                
                sn=int(input("Enter Serial no:- "))
                modl=input("Enter Model:- ")
                prc=input("Enter Price:- ")
                engn=input("Enter Engine(in cc):- ")
                torq=input("Enter Torque:- ")
                ab=input("Enter Braking_system(Mechanical_Disc/ABS):- ")
                tpspd=input("Enter Top speed:- ")
                print()
                v="insert into series values({},'{}','{}','{}','{}','{}','{}');".format(sn,modl,prc,engn,torq,ab,tpspd)
                print(v)
                c.execute(v)
                ver=input("Do you want to save this bike? ")
                print("(a)yes")
                print("(b)no")
                if ver=="yes":
                    d.commit()
                elif ver=="no":
                    print("Thank you")
                    print()
                 
                
                
                print("Bike added successfully.....")
                print()
                print("Serial no:- ",sn)
                print("Model:- ",modl)
                print("Price:- ",prc)
                print("Engine(in cc):- ",engn)
                print("Torque:- ",torq)
                print("Braking_system(Mechanical_Disc/ABS):- ",ab)
                print("Top speed:- ",tpspd)
                input("Press Enter to go to main screen...")
                
                continue
            elif n==5:
                print('''\nKAWASAKI MOTORS CORP., U.S.A.\nHard work and a dream. That's what established American Kawasaki Motorcycle Corp. way back in March of 1966. The first headquarters, an old meat warehouse in Chicago, was a humble beginning for the factory team sent to open the U.S. market.They started with practically nothing - no customers, no distributors and no image.But they had something more important - a strong desire to succeed and a promise from the factory to supply the best products.The first bikes, which were small two strokes sold under the brand name of Omega.But U.S. riders wanted more excitement, so the factory quickly responded with a pair of potential rotary valve twins called the Samurai and Avenger. Here was the first indication that Kawasaki would become a company specializing in high-performance fun.These bikes were sold under the Kawasaki name -- and there was a second operation,Eastern Kawasaki Motorcycle Corp., to handle east coast distribution. In 1968, this firm and the original Chicago company merged to form Kawasaki Motors Corp., U.S.A. (KMC) in Southern California.In 1969, the incredible Mach III 500cc two-stroke triple launched Kawasaki's performance image around the world. By the time of the legendary four cylinder 900cc Z1 in 1973, Kawasaki was a major power in the motorcycle industry, and KMC was building its own unified distribution network to offer dealers and customers better service.Diversification came early when Kawasaki pioneered the personal watercraft business in 1973.Today our JET SKI® watercraft brand is a leader in an exploding market.The 1980's saw further expansion into ATVs and Side x Side vehicles.Today, KMC's annual revenue tops 1.6 billion dollars. There are approximately 480 employees and more than 1,500 dealers. Our bestselling Ninja® sportbikes, classic Vulcan® cruisers,rugged ATV and Mule™ Side x Side vehicles and exclusive JET SKI® watercraft form the foundation Besides the headquarters building in Foothill Ranch, California, KMC has regional sales offices and/or distribution centers in Piscataway, New Jersey; Atlanta, Georgia; Fort Worth,Texas and Hebron, Kentucky. Kawasaki Motors Manufacturing Corp., U.S.A. of Lincoln, Nebraska operates a small engine manufacturing plant in Maryville, Missouri..Several far-sighted Kawasaki executives germinated the idea way back in 1974, and it was simple. If you're selling in America, why not build there too -- save time, save shipping and employ local labor. It worked, and years later firms like Nissan, Toyota, VW and Honda followed Kawasaki's lead.''')
                print()
                
                input("Press enter to go to main menu")
                continue
            elif n==2:
                
                updt=input("Do you want to update:-\n(a)Single bike\n(b)All bikes\n:- ")
                if updt=="a":
                    
                    u=int(input("Enter Serial no of bike to be updated:- "))
                    c.execute("select * from series where sno={};".format(u))
                    rec=c.fetchall()
                    for x in rec:
                        if u==x[0]:
                            print("Serial no:- ",x[0])
                            print("Model:- ",x[1])
                            print("Price:- ",x[2])
                            print("Engine(in cc):- ",x[3])
                            print("Torque:- ",x[4])
                            print("Braking_system(Mechanical_Disc/ABS):- ",x[5])
                            print("Top speed:- ",x[6],"\n")
                        print()
                        
                        js=input("Enter the field to be updated('Serial no','Model','Price','Engine','Torque','Braking_system','Top speed'):- ")
                        if js=='Serial no':
                            na=int(input("Enter new serial no:"))
                            s="update series set Sno={} where Sno={};".format(na,u)
                            #u=na
                            c.execute(s)
                            print()
                            print("Updated successfully......")
                            d.commit()
                            
                        elif js=='Model':
                            nn=input("Enter new model:")
                            s="update series set model='{}' where Sno={};".format(nn,u)
                            c.execute(s)
                            print()
                            print("Updated successfully......")
                            d.commit()
                            
                        elif js=='Price':
                            nd=input("Enter new price:- ")
                            s="update series set price='{}' where Sno={};".format(nd,u)
                            print()
                            c.execute(s)
                            print("Updated successfully......")
                            d.commit()
                            
                        elif js=='Engine':
                            np=input("Enter new engine :- ")
                            s="update series set engine='{}' where Sno={};".format(np,u)
                            print()
                            c.execute(s)
                            d.commit()
                            print("Updated successfully......")
                            
                        elif js=='Torque':
                            ni=input("Enter new torque:- ")
                            s="update series set torque='{}' where Sno={};".format(ni,u)
                            c.execute(s)
                            print()
                            d.commit()
                            print("Updated successfully......")
                            
                        elif js=='Braking_system':
                            ni=input("Enter new Braking_system:- ")
                            s="update series set Braking_system='{}' where Sno={};".format(ni,u)
                            c.execute(s)
                            print()
                            d.commit()
                            print("Updated successfully......")
                            
                        elif js=='Top speed':
                            ni=input("Enter new Top speed:- ")
                            s="update series set TOP_SPEED='{}' where Sno={};".format(ni,u)
                            print()
                            c.execute(s)
                            print("Updated successfully......")
                            d.commit()
                        print("Updated records are:- ","\n")
                        print()
                        print("New updated recordes are:- ")
                        print()
                        c.execute("select * from series;")
                        rec=c.fetchall()
                        for x in rec:
                            print("SERIAL NO:- ",x[0])
                            print("MODEL:- ",x[1])
                            print("PRICE:- ",x[2])
                            print("ENGINE:- ",x[3])
                            print("TORQUE:- ",x[4])
                            print("Braking_system:- ",x[5])
                            print("TOP SPEED:- ",x[6],"\n")
                    
                
                elif updt=="b":
                    js=input("Enter the field to be updated('Model','Price','Engine','Torque','Braking_system','Top speed'):- ")

                    if js=='Model':
                        nn=input("Enter new model:")
                        s="update series set model='{}';".format(nn)
                        c.execute(s)
                        print()
                        print("Updated successfully......")
                        d.commit()
                        
                    elif js=='Price':
                        nd=input("Enter new price:- ")
                        s="update series set price='{}';".format(nd)
                        print()
                        c.execute(s)
                        print("Updated successfully......")
                        d.commit()
                        
                    elif js=='Engine':
                        np=input("Enter new engine :- ")
                        s="update series set engine='{}';".format(np)
                        print()
                        c.execute(s)
                        d.commit()
                        print("Updated successfully......")
                        
                    elif js=='Torque':
                        ni=input("Enter new torque:- ")
                        s="update series set torque='{}';".format(ni)
                        c.execute(s)
                        print()
                        d.commit()
                        print("Updated successfully......")
                        
                    elif js=='Braking_system':
                        ni=input("Enter new Braking_system:- ")
                        s="update series set Braking_system='{}';".format(ni)
                        c.execute(s)
                        print()
                        d.commit()
                        print("Updated successfully......")
                        
                    elif js=='Top speed':
                        ni=input("Enter new Top speed:- ")
                        s="update series set TOP_SPEED='{}';".format(ni)
                        print()
                        c.execute(s)
                        print("Updated successfully......")
                        d.commit()
                        
                        print("Updated records are:- ","\n")
                    input("Press Enter to go to main screen...")
                    continue
                
            elif n==3:
                choice=input("(a)Do you want to delete a single record\n(b)Do you want to delete all records of the table\n:- ")
                if choice=="a":
                    agan=input("Are you sure you want to delete a record of any bike(yes/no):- ")
                    if agan=="yes":
                        
                        print("The records of bikes are:- ")
                        c.execute("select * from series;")
                        rec=c.fetchall()
                        for x in rec:
                            print("SERIAL NO:- ",x[0])
                            print("MODEL:- ",x[1])
                            print("PRICE:- ",x[2])
                            print("ENGINE:- ",x[3])
                            print("TORQUE:- ",x[4])
                            print("Braking_system:- ",x[5])
                            print("TOP SPEED:- ",x[6],"\n")
                        u=int(input("Enter serial no of bike whose record you want to delete:- "))
                        c.execute("delete from series where Sno={}".format(u))
                        d.commit()
                    
                        print("Deleted succesfully")
                        print("The new records of bikes are:- ")
                        c.execute("select * from series;")
                        rec=c.fetchall()
                        for x in rec:
                            print("SERIAL NO:- ",x[0])
                            print("MODEL:- ",x[1])
                            print("PRICE:- ",x[2])
                            print("ENGINE:- ",x[3])
                            print("TORQUE:- ",x[4])
                            print("Braking_system:- ",x[5])
                            print("TOP SPEED:- ",x[6],"\n")
                        

                    elif agan=="no":
                        print()
                        print("Task accomplished")
                        print("Thank you")
                        print()
                    
                    print("The records of bikes are:- ")
                    c.execute("select * from series;")
                    rec=c.fetchall()
                    for x in rec:
                        print("SERIAL NO:- ",x[0])
                        print("MODEL:- ",x[1])
                        print("PRICE:- ",x[2])
                        print("ENGINE:- ",x[3])
                        print("TORQUE:- ",x[4])
                        print("Braking_system:- ",x[5])
                        print("TOP SPEED:- ",x[6],"\n")
                    d.commit()
                    
                    
                        
                elif choice=="b":
                    print("The records of bikes are:- ")
                    c.execute("select * from series;")
                    rec=c.fetchall()
                    print(rec)
                    
                    again=input("Are you sure you want to delete all records(yes/no):- ")
                    if again=="yes":
                        c.execute("delete from series;")
                        d.commit()
                        print("Deleted succesfully")
                        print("The new records of bikes are:- ")
                        c.execute("select * from series;")
                        rec=c.fetchall()
                        print(rec)
                    elif again=="no":
                        print()
                        print("Task accomplished")
                        print("Thank you")
                        print()
                        break
                    break
                input("Press enter to go to main screen")
                continue
                                

            elif n==4:
                shw=input("Enter your choice:-\n(a)Show single bike record\n(b)Show all bike records\n:- ")
                print()
                
                if shw=="a":
                    u=int(input("Enter Serial no(1 to 7):- "))
                    c.execute("select * from series where Sno={};".format(u))
                    rec=c.fetchall()
                    for x in rec:
                        if u==x[0]:
                            print("SERIAL NO:- ",x[0])
                            print("MODEL:- ",x[1])
                            print("PRICE:- ",x[2])
                            print("ENGINE:- ",x[3])
                            print("TORQUE:- ",x[4])
                            print("Braking_system:- ",x[5])
                            print("TOP SPEED:- ",x[6],"\n")
                            
                    input("Press Enter to go to MAIN MENU...")
                    continue
                elif shw=="b":
                    c.execute("select * from series;")
                    rec=c.fetchall()
                    for x in rec:
                        print("SERIAL NO:- ",x[0])
                        print("MODEL:- ",x[1])
                        print("PRICE:- ",x[2])
                        print("ENGINE:- ",x[3])
                        print("TORQUE:- ",x[4])
                        print("Braking_system:- ",x[5])
                        print("TOP SPEED:- ",x[6],"\n")
                        
            elif n==6:
                
                print("(a)Bike having top speed")
                print("(b)Bike having most powerfull engine")
                print("(c)Most expensive bike")
                print("(d)Most cheapest bike")
                print()
                ns=input("Which top bike feature you want to see from our records:-  ")
                print()
                
                if ns=='a':
                    c.execute("select model,TOP_SPEED from series where TOP_SPEED=(select max(TOP_SPEED) from series);")
                    for x in c:
                        print("select model from series where Engine(in cc)=(select max(Engine(in cc)) from series);")
                        print(x)
                        print()
                        
                elif ns=='b':
                    c.execute("select model,Engine from series where Engine=(select max(Engine) from series);")
                    for x in c:
                        print("Bike having most powerfull engine is:- ")
                        print(x)
                        print()
                        
                elif ns=='c':
                    c.execute("select model,Price from series where Price=(select max(Price) from series);")
                    for x in c:
                        print("Most expensive bike is:- ")
                        print(x)
                        print()
                        
                elif ns=='d':
                    c.execute("select model,Price from series where Price=(select min(Price) from series);")
                    for x in c:
                        print("Most cheapest bike is:- ")
                        print(x)
                        print()
                input("Press enter to go to main screen")
                continue

            

            elif n==7:
                print("######EXITING KAWASAKI######")
                print("@Have a nice day@")
                break
            break
        break
       
        
    elif F==0:
        print("Too many wrong attempts")
        print("You are being blocked")
        break
        
    else:
        print("Invalid Input")
        F-=1
        print("You have ",F+1," chances remaining")
