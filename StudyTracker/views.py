from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Answer
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
@api_view(['POST'])
def checkanswers(request):
    
    data = json.loads(request.body)
    user_answers = data.get('answers', [])
    bookVersions = data.get('bookVersions')
    testOptions = data.get('testOptions')
    correct_answers_list_qs_filtered= Answer.objects.filter(Cambridge=bookVersions, Test=testOptions)  
    correct_answers_dict = {}
    if correct_answers_list_qs_filtered.exists():
        # first_record = correct_answers_list_qs_filtered.first()  # Get the first record
        # correct_answers = first_record.CorrectAnswers 
        # for item in correct_answers:
        #     lines = item.split('\r\n')  # Split by line breaks

        #     for line in lines:
        #         parts = line.split()  # Split each line into question number and answer
        #         if len(parts) == 2:
        #             question_number, correct_answer = parts
        #             correct_answers_dict[question_number] = correct_answer

        first_record = correct_answers_list_qs_filtered.first()  # Get the first record
        correct_answers = first_record.CorrectAnswers 
        lines = correct_answers.split('\r\n')  # Split by line breaks

        for line in lines:
            parts = line.split()  # Split each line into question number and answer
            if len(parts) == 2:
                question_number, correct_answer = parts
                correct_answers_dict[question_number] = correct_answer
    else:
        return JsonResponse({'correct_answers': 'no answer'})
    #correct_answers_list = list(correct_answers)  
    
    
   #return JsonResponse({'correct_answers': correct_answers})
    
    score = 0
    results = []
    for question in range(1, len(user_answers) + 1):
        user_answer = user_answers[question - 1]  
        
        if str(question) in correct_answers_dict:
            correct_answer = correct_answers_dict[str(question)]
            
            if user_answer == correct_answer:
                score += 1
    


            results.append({'question': correct_answer, 'user_answer': user_answers[int(question) - 1]})

    return JsonResponse({'user':user_answers, 'db':correct_answers_dict, 'score': score, 'results': results, 'testOptions' : testOptions,'bookVersions': bookVersions})
 
