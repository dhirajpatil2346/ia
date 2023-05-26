def greet(Bot_name):
    print("hello master i am ",Bot_name,"what is your name \n>>>")
    name=input()
    print("aaicha gavat kai naav ahe tumcha ",name )
def  guessage():
    print("tera bap apunach he phir bhi guess karenga age\n")
    print("apon ko reminder bol after dividing by 3,5,7 aur numverich deneka\n")
    age=int(input("3 wala : "))
    age1=int(input("5 wala : "))
    age2=int(input("7 wala : "))
    mage=((age)*70+(age1)*21+(age2)*15)%105
    print("tera age hae",mage)
def joke():
    print("ek joke sunav kya\n>>>")
    x=input("Y/N>>>")
    if x.lower()=='y':
        print("teri jindagi hi mazak hae isse jyada kya maza karu\n")
    else:
        print("abhe chutiye joke nahi sunake ka\n")
def bye():
    print("abhe ghar ja sale mera time waste kar raha hae khud ko toh kuch kaam hae nahi \n")
    qw=input("review de be aise hi kaha ja raha hai\n>>>")
    print('apka review ka ghanta farak nahi hae \n')


if '__main__'== __name__:
    greet("kokila\n")
    guessage()
    joke()
    bye()