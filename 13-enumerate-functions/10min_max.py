# Advance min and max function

# iske baare mai pehle be parh chuke hain

# agar mene dekhna hai mere names list me kis name ki length badi hai
# to me MAX function use karunga zaahir hai
# def func(item):
#     return len(item)
# names = ['AmeerHamza', 'Ahmed', 'Sattar', 'Kashi']
# print(max(names, key = func))
# func is liye banaya take aik func len ka kam kare
# same as max ki jaga min be  kar sakte hain

# use of func with lambda(Good method, practice, idea, and inevate)
#print(max(names, key = lambda item : len(item))) # Perfect
# wese yeh theek hai woh func use  karne ki scene nahi bnti hai
# code badsurat lagta hai

students = {
    'Hamza' : {'score' : 90, 'age' : 20},
    'Nihal' : {'score' : 85, 'age' : 19},
    'ahmed' : {'score' : 80, 'age' : 18}
}
print(max(students, key = lambda item : students[item]['age']))
students2 = [
    {'name' : 'Hamza', 'score' : 90, 'age' : 20},
    {'name' : 'Nihal', 'score' : 85, 'age' : 19},
    {'name' : 'ahmed', 'score' : 80, 'age' : 18}
]
#print(max(students2, key = lambda item : item.get('score')))
# mera score "hamza" ziada hai to is liye yehi print hua jo score ziada hogi
# wahi print karega max function