from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line4 = '<a href="/play/">进入游戏界面</a>'
    line3 = '<hr>'
    line2 = '<img src="https://img.3dmgame.com/uploads/allimg/180522/409_180522102710_1.png" width=2000>'
    return HttpResponse(line1 + line4 + line3 + line2)

def play(request):
    line1 = '<h1 style="text-align: center">游戏界面</h1>'
    line2 = '<a href="/">返回主页面</a>'
    line3 = '<img src="https://image.9game.cn/2019/9/2/94565968.jpg" width=2000>'
    return HttpResponse(line1 + line2 + line3)
