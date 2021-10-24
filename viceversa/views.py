from django.http.request import split_domain_port
from django.shortcuts import render

def home(requests):
    return render(requests, 'home.html')

def reverse(requests):
    get_text = requests.GET['usertext']
    reverse_text = get_text[: : -1]
    splitted_word = get_text.split()
    word_len = len(splitted_word)
    return render(requests, 'reverse.html', {'usertext': get_text, 'reversed_text': reverse_text, 'wordcount': word_len})