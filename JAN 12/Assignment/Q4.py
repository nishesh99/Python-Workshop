firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
print("Hello! "+firstname+" "+lastname+".")
print(f"Hello! {firstname} {lastname}.")
print("Hello! {} {}.".format(firstname,lastname))
print("Hello! {0} {1}.".format(firstname,lastname))
print("{} {} {}.".format("Hello!",firstname,lastname))
print("Hello! {first_key} {last_key}.".format(first_key=firstname,last_key=lastname))
#print ("your firstname is {} and lastname is {},{}" .format(firstname,lastname)}
print("Hello! {1} {0}.".format(lastname,firstname))