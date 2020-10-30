import requests
import random
import json
from tkinter import Tk, Label, Button, StringVar
from random import randrange
# response=requests.get("https://opentdb.com/api.php?amount=1")#use this for api call
# data=response.json()['results']#use this with api call
with open('api.json') as f:
    response=json.load(f)
data=response['results']
counter=0
def nextValue():
    global counter
    counter+=1
    Q.set(counter)

window=Tk()
Q=StringVar()
Q.set("Testf")
window.title("Trivia Game")
window.geometry("800x600")
window.label = Label(window, textvariable=Q).pack()
NextProblem=Button(window,text="text",command=nextValue).pack()


def display(problem):
    letters=['A','B','C','D']
    if data[problem]['type']=='multiple':
        print(problem+1,": ",data[problem]['question'])
        choices=[data[problem]['incorrect_answers'][0],
                 data[problem]['incorrect_answers'][1],
                 data[problem]['incorrect_answers'][2],
                 data[problem]['correct_answer']]
        random.shuffle(choices)
        labledChoice={
                'A': choices[0],
                'B': choices[1],
                'C': choices[2],
                'D': choices[3]
        }
        for key,value in labledChoice.items():
            print("\t\t",key,':',value)

        submission = input("Choice:")
        if submission.upper() in letters:
            if labledChoice[submission.upper()]==data[problem]['correct_answer']:
                print('Correct')
                return 0
            else:
                print('Incorrect')
                return -1
        else:
            print('Incorrect')
            return -1
    else:
        print(problem+1,": ",data[problem]['question'])
        print("\t\t",'True')
        print("\t\t",'False')
        submission = input("Choice:")
        if submission.upper()==data[problem]['correct_answer'].upper():
            print('Correct')
            return 0

        else:
            print('Incorrect')
            return -1
def problems(amount):
    score=amount
    for problem in range(amount):
        score+=display(problem)
    print (100*score/amount,'%')
# display(randrange(50))
# problems(randrange(50))
# problems(10)
class GUI:
    def __init__(self,master):
        self.master = master
        master.title("Trivia Game")

        self.label = Label(master, textvariable=Q)
        self.label.pack()

        self.greet_button = Button(master, text="Choice",command=self.greet )
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")


# root = Tk()
# gui=GUI(root)
# root.mainloop()
window.mainloop()