print("Hey wassup its Jake, I've got a bit of a problem. Both my girl and the boys want to hang today")
choice = input("Should I choose my girl or the boys? ")
if choice == "My Girl":
    pay = input("Should I pay for dinner or should we split the check? ")
    if pay == "Pay":
        print("My girl was so happy that I chose her and paid for her, we stayed together and I've never been happier!")
    elif pay == "Split":
        print("My girl got mad at me and broke up with me, so I'm sad now :(")
elif choice == "The Boys":
    print("Me and the boys are gonna play some video games")
    print("Oh no my girl's calling!")
    answer = input("Should I answer the call? ")
    if answer == "Yes":
        print("My girl is a bit mad that I didn't hang out with her but we had a good talk and are all good now")
    elif answer == "No":
        print("My girl just yelled at me for a half hour straight and then broke up with me :(")
