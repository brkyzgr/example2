print("""
*****************************************************************
*                                                               *                                                      
*                                                               *
*                                                               *
*                  Ozgur Game Sales Platform                    *
*                                                               *
*                                                               *
*                                                               *
*****************************************************************
""")

psnumber=int(input("Please enter the number of Ps4 games you will receive: "))
pcnumber=int(input("Please enter the number of PC games you will receive: "))

psprice= 40
pcprice= 10
total=0
turklira= 7.44

try:
    if psnumber < 0 or psnumber==0:
        print("Please enter the number of pieces except 0 and minus value: ")
    elif pcnumber < 0 or pcnumber==0:
        print("Please enter the number of pieces except 0 and minus value: ")
    else:
        print("You are logged in correctly. ")

    total= (psnumber*psprice)+(pcnumber*pcprice)
    turklira= total * 7.44
    
    
    
    
    print(f"""
    
    Number of PC game pieces you entered     : {pcnumber}
    The number of Ps4 game pieces you entered: {psnumber}
    Total price you will pay                 : {total}$
    Optional TL payment fee                  : {turklira}TL
    
    Thank you for shopping.
    """)
except ValueError as error:
    print("You Made an Incorrect Transaction")
    
    
    


