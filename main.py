import requests
import random
response=requests.get("https://opentdb.com/api.php?amount=200")
data=response.json()['results']
def display(problem):
    if data[problem]['type']=='multiple':
        print(problem+1,": ",data[problem]['question'])
        choices=[data[problem]['incorrect_answers'][0],data[problem]['incorrect_answers'][1],data[problem]['incorrect_answers'][2],data[problem]['correct_answer']]
        random.shuffle(choices)
        for choice in choices:
            print("\t\t",choice)
        # print(data[problem]['correct_answer'])
    else:
        print(problem+1,": ",data[problem]['question'])
        print("\t\t",'True')
        print("\t\t",'False')
        # print(data[problem]['correct_answer'])

display(0)
# for entry in data:
#     print(entry['type'])
