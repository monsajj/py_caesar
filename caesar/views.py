from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, 'caesar/index.html')


def decipher(request):
    text = request.GET.get('decryption_text')
    decrypted_text = 'decrypted text - ' + text
    return JsonResponse({'decrypted_text': decrypted_text}, status=200)
