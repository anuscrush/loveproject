from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def yes_response(request):
    message = """<h2>I love you toooo 😘❤️</h2>
    <p>You made my life beautiful 💕 Chitti Thalli 💖 mana eddaram kalusthe yemaina chesesthammm  
    Thank you for loving me, caring me and staying with me 🥺❤️
    I’m really lucky to have you in my life Chitti Thalli 💖
    Nuvvu natho unte life ni inka beautiful ga lead cheyyochu Bangaram 😇😘
    I love you sooooo much 😘❤️
    UmmmmaAaa neyyyyy 😘❤️😘❤️</p>"""
    
    return render(request, "result.html", {"message": message})


def no_response(request):
    message = """<h2>😜 Sare… but nuvvu naa MuddhuGummma vi 💖 don't leave me at any situations bujjulu  
    you are my mine ❤️🤝 manam eddaram yeppudu kalise vundhammmm ok naaa</h2>
    <p>Happy Valentine’s Day Bujjuluuu ❤️</p>"""
    
    return render(request, "result.html", {"message": message})