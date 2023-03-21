from django.shortcuts import render
import random
import requests

# Create your views here.
def greeting(request):
    return render(request, 'lottos/greeting.html')

def index(request):
    return render(request, 'lottos/index.html')


def lotto(request):
    # lotto 당첨 번호 가져오기
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1054'
    
    # 파이썬으로 요청 후 응답받기 (자세한 내용은 requests docs 참고)
    res = requests.get(url)
    lotto_dict = res.json() # json -> dict로 변경

    # print(lotto_dict['totSellamnt'])

    lotto = []
    bonus = lotto_dict['bnusNo']
    for i in range(1, 7):
        lotto.append(lotto_dict[f'drwtNo{i}'])
    # print(lotto)
    
    win_rate = {
        '1등' : 0,
        '2등' : 0,
        '3등' : 0,
        '4등' : 0,
        '5등' : 0,
        '꽝' : 0
    }
    for i in range(1000):
        # 랜덤 로또 번호
        numbers = range(1, 46)
        lotto_num = random.sample(numbers, 6)
        
        # 로또 번호 비교
        cnt = 0
        for num in lotto_num:
            if num in lotto:
                cnt += 1
        
        if cnt == 6:
            win_rate['1등'] += 1
        elif cnt == 5:
            if bonus in lotto_num:
                win_rate['2등'] += 1
            else:
                win_rate['3등'] += 1
        elif cnt == 4:
            win_rate['4등'] += 1
        elif cnt == 3:
            win_rate['5등'] += 1
        else:
            win_rate['꽝'] += 1
    
    
    context = {
        'lotto_num' : lotto_num,
        'lotto' : lotto,
        'win_rate' : win_rate,
        'bonus' : bonus,
    }
    return render(request, 'lottos/lotto.html', context)