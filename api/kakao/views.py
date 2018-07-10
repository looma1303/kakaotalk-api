from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime

def keyboard(request):

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    saying = received_json_data['content']
    today_date = datetime.date.today().strftime("%m월 %d일")

    return JsonResponse({
            'message': {
                'text': today_date+'의 급식표는\n'+'입니다.'
            },
            'keyboard': {
                'type': 'bottons',
                'bottons': ['오늘 급식표']
            },
    }) 
