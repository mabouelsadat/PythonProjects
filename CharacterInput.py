x = 200
y = 200.1
is_Signed_In = True

print (type(is_Signed_In))

print(" this is parsing shit " + str(x))

email = """Dear Sender

Your email has been registered. 

regards, 
Support Team 
"""

print(len(email))
print(email[1:-2])
print(email.upper())

#replacing
print(email.replace("Lorem", "400"))

#Splitting
print(email.split())

#in

print("Dear"  in email )

name = "Mohamed"
lastname = "Abouelsaadat"
email = "m.abouelsadat@gmail.com"


Email_To_Sender = """Dear {} {}

Your email {} has been registered. 

regards, 
Support Team 
"""

print(Email_To_Sender.format(name , lastname, email))