def ATM():
    user_name = input ('Insert Name:')
    #print (user_name)
    correct_user_pin = 2020
    Account_amount = int(30000)
    user_pin = int (input ('Insert PIN:'))
    
    
    if user_pin != correct_user_pin:
        print ('Wrong Pin')
    if user_pin == correct_user_pin :
        print ('****')
        Cash_withdraw = int (input('Insert Withdraw amount:'))
        if Cash_withdraw <= Account_amount :
            Account_bal = Account_amount - Cash_withdraw
            print ('Withdraw successful and your account balance is: ', Account_bal)
        #if Cash_withdraw != Account_amount :
        else :
            print ('Insuffient balance')


            
        
    
        
 
ATM()