'''# chatbot/views.py
from django.views import View
from django.http import JsonResponse
from .aichat import generate_response

class ChatbotView(View):
    def post(self, request, *args, **kwargs):
        message = request.POST.get('message')
        response = generate_response(message)
        return JsonResponse({'message': response})'''