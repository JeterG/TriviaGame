import requests
import random
response=requests.get("https://opentdb.com/api.php?amount=50")
data=response.json()['results']
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

        # submission = input("Choice:")
        # if submission.upper()
        print(labledChoice['A'])
    else:
        print(problem+1,": ",data[problem]['question'])
        print("\t\t",'True')
        print("\t\t",'False')
display(0)
