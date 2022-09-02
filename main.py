from fakeUserData import generator
import random

gender = random.choice(["Female", "Male"])
print("Name: " + generator.firstName(gender) + " " + generator.lastName())
print("Email: " + generator.email())
print("Password: " + generator.createPassword())
print("Birthday: " + random.choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", 
"10", "11", "12"]) + "/" + random.choice(["01", "02", "03", "04", "05", "06", 
"07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", 
"20", "21", "22", "23", "24", "25", "26", "27", "28"]) + "/" + 
random.choice(["1980", "1981", "1982", "1983", "1984", "1985", "1986", 
"1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1996", 
"1997", "1998", "1999", "2000"]))
print("SSN: " + generator.ssn())
print("Phone Number: " + generator.usPhoneNumber())
print("Country: " + "United States")
print("State: " + generator.state())
print("City: " + generator.city())
print("Street: " + generator.street())
print("Zipcode: " + generator.zipCode())
print("IP Adress: " + generator.ipAddress())
