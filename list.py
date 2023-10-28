#story="hello sir forgot what people whoud say about you"
#string function

#print(len(story))
#print(story.find("you"))
#print(story.endswith("you"))
#print(story.count("hello"))
#print(story.replace("hello"," bhau"))
#print(story.capitalize())
#print(story.endswith("you"))

#name=input("enter your name")
#print("Good afternoon," +name)

#letter=''' Dear <|NAME|>
#     Greetings exam abc coding house i am happy to tell you about your selection
 #    your are selected !
  #   have  a nice day ahead !
   #  Thanks for regards,
   # date:<|DATE|>'''

#name=input("enter your name\n")
#date=input("enter the date\n")
#letter=letter.replace("<|NAME|>",name)
#letter=letter.replace("<|DATE|>",date)
#print(letter)










letter= ''' Dear  <|NAME|>,
        Grettings from ABC coding house.i am happy to tell you about your selection
        your are selected!
        have a nice day ahead!
        Thanks and regards,
        bill
        date:<|DATE|>'''

name=input("Enter your name \n")
Date =input ("Enter the date \n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",Date)
print(letter)