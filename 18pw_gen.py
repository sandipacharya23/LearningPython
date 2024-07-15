import random
def password_generator():

    alphabet = 'a,b,c,d,r,e,s,g,h,y,u'
    alphabet_upper = alphabet.upper()
    numbers = '1,2,3,4,5,6,0'

    all_combine = alphabet +',' + alphabet_upper + ','+  numbers
    all_combine_to_list = all_combine.split(",")

    random1 = random.choice(all_combine_to_list)
    random2 = random.choice(all_combine_to_list)
    random3 = random.choice(all_combine_to_list)
    random4 = random.choice(all_combine_to_list)
    random5 = random.choice(all_combine_to_list)

    password = random1 + random2+ random3+random4 +random5
    print(password)

password_generator()