import time
a='Password'

i=1
n=5
while i:
    check_password=input("check the password")
    if a==check_password:
        break
    
    else:
        print("wrong password wait for 5 sec")
        while n:
            print(n)
            n-=1
            time.sleep(1)
i+=1
print("password verified")
