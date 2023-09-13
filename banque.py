import pickle
import os

db_file='database'

if not os.path.exists(db_file):
    with open('database','wb') as file :
        pickle.dump([],file)


with open('database','rb') as file:
    account=pickle.load(file)
    



while True:
    print(" ")
    print('\t1.Connection')
    print('\t2.Create account')
    print('\t3.Exit ')
    print(" ")
    
    while True:
        choice=input('\tEnter your choice :  ')
        if choice.isdigit():
            choice=int(choice)
            break
        elif choice=="" or choice==" ":
            print("\tYou don't choose anything")
        else:
            print('\tYou Make a Bad Choice')
    print(' ')
    
    match choice:
        case 1:
            connection=False #pou teste si moun nan konekte
            compte={}
            id_client=input('\tEnter identifier : ')
            password=input('\tEnter your password : ')
            for i in account:
                if i['id_client']==id_client and i['password']==password:
                    print('\tYou are successfully connected\n')
                    compte=i
                    connection=True
                    break
                else:
                    connection=False
                    print('\tincorrect information \n')
                
            while connection:
                if connection== True:
                    print('\t1.Balance')
                    print('\t2.Storage')
                    print('\t3.withdrawal')
                    print('\t0.back')
                    print(' ')
                    choice1=input('\tMake a Choice : ')

                if choice1=='0':
                    break
                
                match choice1:
                    case '1':
                        print(f"\tYou have {compte['montant']} $")
                    case '2':
                        account.remove(compte)
                        montant=int(input('\tEnter the amount you want to put in : '))
                        compte['montant']+=montant
                        account.append(compte)
                        print(f"\tYou have {compte['montant']} $ now ")
                        
                        with open('database','wb') as file:
                            pickle.dump(account,file)
                    case '3':
                       
                        ret=int(input('\tenter the amount you want to withdraw : '))
                        montant = ret
                        while True:
                            if ret>compte['montant']:
                                print('\twithdrawal you ask the faith too much')
                                
                            else:
                                account.remove(compte)
                                compte['montant']-=montant
                                account.append(compte)
                                print(f"\tYou stay {compte['montant']} $ now")

                                with open('database','wb') as file:
                                    pickle.dump(account,file)
                            break
        case 2:
            user_account={}

            nom=input('\tLast_name : ')
            prenom=input('\tFirst_name : ')
            password=input('\tPassword : ')
            
            while True:
                test_id = False
                id_client=input('\tAntre idantifyan kliyan(fakiltatif(tanpri fèl ak premye lèt non premye lèt siyati plis twa chif ou vle)) : ')
                for i in account:
                    if i['id_client']== id_client:
                        print('\tId that is already registered :  ')
                        test_id = True
                        break
                    else:
                        test_id = False
                        
                if test_id == False: 
                    break       
          
            while True:
                montant=input("\tEnter the amount you're putting on it :  ")
                
                if montant.isdigit():
                    montant=int(montant)
                    if montant<5:
                        print('\t insufficient amount')
                    else:
                        break
                else:
                    print('\tAmount not valid')
            
            print(' ')    
            user_account['nom']=nom
            user_account['prenom']=prenom
            user_account['id_client']=id_client
            user_account['montant']=montant
            user_account['password']=password
            
            account.append(user_account)
            with open('database','wb') as file:
                pickle.dump(account,file)
            print(f"\tyour account is successfully registered by your \tname:{nom} your \tid:{id_client} \tamount of money:{montant}")
            
        case 3 :
            break
        case _ :
            print('Your choice is not in our menu')