# from VegmartPdf import *
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 






items=['bende','badane','tomato','alu','onion']

rate=[80,60,40,40,40,50]
quantity1=[]
ammount=[]
itemlist=[]
grand_Total=0
# ---------
# pdf

DATA = [ 
	[ "Name", "Quantity","Price/kg (Rs.)","Total" ], 
	
] 



# -------
print("vegmart Billing")
print("The list of the items availabel...")
for t in items:
    print(t,end=", ")
print()
sublist=[]
try:
    while True:
        
            n=input("enter the item:")
            if n!="done":
                itemlist.append(n)
                sublist.append(n)
                
            
            if n=="done":
                
                
                break

            else:
                quantity=int(input("quantity :"))
                quantity1.append(quantity)
                sublist.append(quantity)
                for i in items:
                    if i==n:
                        rat=int(rate[items.index(i)])
                        price=int(quantity*rat)
                        grand_Total+=price
                        ammount.append(price)
                        sublist.append(rate[items.index(n)])

                        sublist.append(int(quantity*rat))

            DATA.append(list(sublist))
            
            sublist.clear()
    DATA.append(["","","Grand Total ",grand_Total])
except:
        print("Something went wrong please check it..")
print("the total value is ")

h=0
i=0
stringT=[]
for i in itemlist:
    # text=(itemlist[h])+str(quantity1[h])+'kg'+':'+str(ammount[h])
    # pdf(text)
    # stringT.append(f'{text}/n')
    # print(itemlist[h] ,quantity1[h],"KG",":", ammount[h])
    
    h+=1
print(DATA)

pdf = SimpleDocTemplate( "Bill.pdf" , pagesize = A4 )
styles = getSampleStyleSheet() 

# fetching the style of Top level heading (Heading1) 
title_style = styles[ "Heading1" ] 
title_style1 = styles[ "Heading6" ] 

# 0: left, 1: center, 2: right 
title_style.alignment = 1
title_style1.alignment = 1

# creating the paragraph with 
# the heading text and passing the styles of it 
title = Paragraph( "Veg Mart" , title_style ) 
title = Paragraph( "Thank You for visiting,have a nice day" , title_style1 ) 

style = TableStyle( 
	[ 
		( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
		( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ), 
		( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ), 
		( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
		( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
		( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
	] 
) 

# creates a table object and passes the style to it 
table = Table( DATA , style = style ) 

# final step which builds the 
# actual pdf putting together all the elements 
pdf.build([ title , table ]) 