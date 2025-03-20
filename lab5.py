import random
import string
dict={}
dictKey=set()
dictValue=set()
print("Choose 5 characters (lowercase only) and assign 5 replacement options each:")
for _ in range(5):
    print("enter a lowercase character:")
    key=input()
    dict[key]=set()
    for _ in range(3):
        print("enter a replacement for  " + key)
        value=input()
        dict[key].add(value)




print(dict)
passwords = []
weakPasswords = []
strongPasswords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)
print(passwords)
count=0;
for password in passwords:
    for key in dict:
            password = password.replace(key, random.choice(list(dict[key])))
            for x in password:
                if x==key:
                    count+=1

            if(count<5):
                 weakPasswords.append(password)
            else:
                strongPasswords.append(password)

print("weak passwords:")
print(weakPasswords)
print("strong passwords:")
print(strongPasswords)



