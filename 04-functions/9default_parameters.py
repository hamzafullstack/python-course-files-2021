def user_info(first_name, last_name, age): #age = 19
    print(f"your first name is {first_name}")
    print(f"your last_name is {last_name}")
    print(f"your age is {age}")

user_info('Ameerhamza', 'Baloch', 19) #age will overwrite if enter in def

"""Now lets talk about default parametters

agar upr user_info me age pass nahi karuga 19 to error ayegi "Type error"
agar upr def me age = 19 kar dun aur userinfo me age na likhon run hogi, yesss
age = None # default parameter
last_name 'unknown', #default parameter """