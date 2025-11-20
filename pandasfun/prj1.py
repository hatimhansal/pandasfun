import pandas as pd
x=0
print("#########################################")
print("_______________pandas__________________")
print("#########################################")

print("1)Cree  serie : ")
print("2)Cree  Dataserie : ")
x=int(input("Ecrire number 1-2:"))

if x==1 :
    j=[]
    print("1)wana Tableau Exemple :")
    print("2)give value in tableau :")
    alp=int(input('your choix :'))
    if alp == 2 :
        range1=int(input("how much index you give :"))
        for i in range (0,range1) :
            v1=input(f"give donner une tableau {i+1}:")
            j.append(v1)
        df1=pd.Series(j)
        print(df1)
    elif alp == 1 :
        df2=pd.Series([12,13,14,15])
        print(df2)
        d2=0
        df2=pd.Series(["p","a","n","d","a","s"])
        print(d2)
        print("1)Copie le code Serie ")
        print("2) Exit")
        e0=input("Ecrire choix :")
        if e0 == 1 :
            print('import pandas as pd /n    df2=pd.Series([12,13,14,15])  /n print(df2) /n d3=0    df3=pd.Series(["p","a","n","d","a","s"])  /n  print(d3) ')
        elif e0 == 2 :
            x=0
            print("_______________pandas__________________")
            print("1)Cree un serie : ")
            print("2) cree un Dataserie : ")
            x=int(input("Ecrire number :"))
        else :
            ex0 =0
            while ex0 == 0 :
                print("Error choix (1) or (2)")
                e0=input("Ecrire choix :")
                if e0 == 1 or e0 == 2:
                    ex0 = 1
                    j=[]
                    alp=[]
                    df=0
                    df1=0
################################################# choix 2
elif  x==2 :  
   
    print("1) Exemple dicsionner :")
    print("2) Give value  dicsionner :") 
    alp=int(input('your choix :'))
    if alp == 2 :
        print('Exemple in this cas form dics {"name":["n1","n2","n3"]}')
        range1=int(input("how give number Colum  :"))
        d={}
        w=0
        for i in range (0,range1) :
                v1=input(f"give donner  name  tableau incide dictionner {i+1} :")
                v2=input(f"give donner   valeur {w+1} :")
                v3=input(f"give donner   valeur {w+2} :")
                v4=input(f"give donner   valeur {w+3} :")
                d[v1] = [v2,v3,v4]
        df1=pd.DataFrame(d) 
        print(df1)
        print("1)Filter Name disc whit math :")
        print("2) Filter Name with Value (ex:'name > value') :")
        print("3)Gite info")
        F1=int(input("Name disc for filter"))
        if F1 == 2 :
            
            print("1)I do more two filter :")
            print("2) One filter :")
            print("3)Ajouter objet :")
            print("3 Back <-- :")

            FF1=input("Choses 1-2 :")
            if FF1 == 1 :
                print("Name dics you filter : ")
                name1=input("Name tableau incide disc :")
                signe1=input(" > / < / ==  :")
                vul1=input("valeur thr filter :")
                yn=input(" and / or : ")
                name2=input("Name tableau incide disc ex('age') :")
                signe2=input(" > / < / == :")
                vul2=input("valeur thr filter :")
                if yn == "and" :
                    if signe1 == ">" and signe2 == ">" :
                        df2=[df1[name1] > vul1 and df1[name2] > vul2 ]
                        print(df2)

                    elif  signe1 == "<" and signe2 == ">" :
                        df2=[df1[name1] < vul1 and df1[name2] > vul2 ]
                        print(df2)

                    elif signe1 == ">" and signe2 =="<" :
                        df2=[df1[name1] > vul1 and df1[name2] < vul2 ]
                        print(df2)
                        
                    elif signe1 == "==" and signe2 =="==" :
                        df2=[df1[name1] == vul1 and df1[name2] == vul2 ]
                        print(df2)
                        
                    elif signe1 == "==" and signe2 =="<" :
                        df2=[df1[name1] == vul1 and df1[name2] < vul2 ]
                        print(df2)
                        
                    elif signe1 == ">" and signe2 =="==" :
                        df2=[df1[name1] > vul1 and df1[name2] == vul2 ]
                        print(df2)

                    elif signe1 == "<" and signe2 =="==" :
                        df2=[df1[name1] < vul1 and df1[name2] == vul2 ]
                        print(df2)

                    elif signe1 == "==" and signe2 ==">" :
                        df2=[df1[name1] == vul1 and df1[name2] > vul2 ]
                        print(df2)

                    else :
                        print("erreur !")


                elif yn == "or"  :
                    if signe1 == ">" and signe2 == ">" :
                        df2=[df1[name1] > vul1 or df1[name2] > vul2 ]
                        print(df2)
                        
                    elif  signe1 == "<" and signe2 == ">" :
                        df2=[df1[name1] < vul1 or df1[name2] > vul2 ]
                        print(df2)

                    elif signe1 == ">" and signe2 =="<" :
                        df2=[df1[name1] > vul1 or df1[name2] < vul2 ]
                        print(df2)

                    elif signe1 == "==" and signe2 =="==" :
                        df2=[df1[name1] == vul1 or df1[name2] == vul2 ]
                        print(df2)

                    elif signe1 == "==" and signe2 =="<" :
                        df2=[df1[name1] == vul1 or df1[name2] < vul2 ]
                        print(df2)

                    elif signe1 == ">" and signe2 =="==" :
                        df2=[df1[name1] > vul1 or df1[name2] == vul2 ]
                        print(df2)

                    elif signe1 == "<" and signe2 =="==" :
                        df2=[df1[name1] < vul1 or df1[name2] == vul2 ]
                        print(df2)

                    elif signe1 == "==" and signe2 ==">" :
                        df2=[df1[name1] == vul1 or df1[name2] > vul2 ]
                        print(df2)
                    else :
                        print("erreur !")
                        print("1)I do more two filter ")
                        print("5) Afficher My objet without filter")
                        print("6) Back <--")
                        FF1=input("Your choix :")

                        if FF1 == 5  :
                            print(df1)
                            
                                
                            print("1)I do more two filter :")
                            print("2) One filter :")
                            print("3)Ajouter objet :")
                            print("4) Back <-- :")
                            FF1=input("Choses 1-2-3-4 :")
                        else :
                            print("1)I do more two filter ")
                            print("1)I do more two filter :")
                            print("2) One filter :")
                            print("3)Ajouter objet :")
                            print("4) Back <-- :")
                            FF1=input("Choses 1-2-3-4 : ")
                        FF1=input("Choses 1-2-3-4 : ")


                         
                elif FF1 == 2:
                    print("Name dics you filter :")
                    print("Name dics you filter : ")
                    name3=input("Name tableau incide disc :")
                    f3=input(" > / < / == / + / * / - :")
                    vul3=input("valeur thr filter :")
                    if f3 == ">" :
                        df3=df1[df1[name3] > vul3]
                        print(f" df3={df1}[{df1}{[name3]} > {vul3}]",df3)
                    elif f3 == "<" :
                        df3=df1[df1[name3] < vul3]
                        print(f" df3={df1}[{df1}{[name3]} < {vul3}] = ",df3)
                    
                    elif f3 == "+" :
                        df3=df1[name3] + vul3
                        print(f" df3={df1}{[name3]} + {vul3} = ",df3)
                    elif f3 == "*" :
                        df3=df1[name3] * vul3
                        print(f" df3={df1}{[name3]} * {vul3} = ",df3)
                    elif f3 == "-" :
                        df3=df1[name3] - vul3
                        print(f" df3={df1}{[name3]} - {vul3} = ",df3)
                    else :
                        print("1)I do more two filter :")
                        print("2) One filter :")
                        print("3)Ajouter objet :")
                        print("3 Back <-- :")
                        FF1=input("Choses 1-2 :")
                    print("1)Afficher My objet without filter :")
                    print(df1)

    ###### It's not complette 


                    


                


            




