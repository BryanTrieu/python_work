parks_employee = 'leslie'
print("Is the  Parks and Rec employee Leslie? I predict True.")
print (parks_employee == 'leslie')

print ("Is the employee Ron? I predict False.")
print(parks_employee == 'ron')

parks_age = [45, 48]
average_age = sum(parks_age)/len(parks_age)
print ("Is average age of the two higher than 50? I predict False.")
print (average_age > 50)

print ("Is average age of the two higher than 40? I predict True.")
print (average_age > 40)

print ("Is the sum of their ages greater than 100? I predict False.")
print (sum(parks_age) > 100)

parks_employees = ['leslie','ron','tom','donna','jerry']
print ("Is Larry part of the Parks and Rec employees? I predict False.")
print ('larry' in parks_employees)

print ("Is Jerry part of the Parks and Rec employees? I predict True.")
print ('jerry' in parks_employees)

print ("Is Jean Ralphio NOT in the Parks and Rec employees list?  I predict True.")
print ('jean ralphio' not in parks_employees)