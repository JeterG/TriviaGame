import requests
import random
import json
from random import randrange
# response=requests.get("https://opentdb.com/api.php?amount=1")#use this for api call
# data=response.json()['results']#use this with api call
with open('api.json') as f:
    response=json.load(f)
data=response['results']
def display(problem):
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
        if labledChoice[submission.upper()]==data[problem]['correct_answer']:
            print("Correct")
        else:
            print("Incorrect")
    else:
        print(problem+1,": ",data[problem]['question'])
        print("\t\t",'True')
        print("\t\t",'False')
        submission = input("Choice:")
        if submission.upper()==data[problem]['correct_answer'].upper():
            print('Correct')
        else:
            print('Incorrect')
display(randrange(50))
