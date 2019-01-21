#thanks to Lumi for the idea :)
#basically this just is gay compliments so yea
#gender is a catagory
#ex. if you type in man i'll use that string if you type in male it'll use the same string
#if you want to add different ways to use any pronouns go for it
#but again thanks to Lumi for this jokey script i just sat here for an hour working on this
#github.com/YeAxol
gender = input('What gender are you today? ')
name = input('What name are you calling yourself today? ')
if gender in ['Male', 'male', 'Man', 'man']:
    print(name + ' you are really cute prince')
elif gender in ["Female", "Fem", "fem", "female"]:
    print(name + ' you are really cute princess')
else:
    print(name + ' you are really cute')
