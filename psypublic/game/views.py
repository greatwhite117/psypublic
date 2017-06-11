# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Player, Game
from django.http import HttpResponse


# Create your views here.
def index(request):
    try:
        if request.user.is_superuser:
            return redirect('admin:index')
        elif request.user.is_authenticated():
            context = {
                'contents' : '지금부터 게임을 시작하겠습니다',
                'next_page' : 'intro',
                'next_index' : 0,
            }
            return render(request, 'game/only_text.html', context)
        else:
            return redirect('login')
    except:
        return redirect('login')


def intro(request,num="0"):
    currentPlayer = Player.objects.get(user=request.user)
    context = {
    }
    token_multiply_private = currentPlayer.gamePlay.point_calc_private
    token_multiply_public = currentPlayer.gamePlay.point_calc_public
    template = 'game/image1_text.html'
    if num == "0":
        if currentPlayer.finished == True:
            return redirect('login')
        if currentPlayer.gamePlay.token_type == 't':
            token_string = '토큰이'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string = '사이버머니가'
            else:
                token_string = '점수가'
        if currentPlayer.gamePlay.token_type == 't':
            token_count_string = '몇 개'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_count_string = '몇 원'
            else:
                token_count_string = '몇 점'
        if currentPlayer.gamePlay.token_type == 't':
            token_string2 = '토큰을'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string2 = '사이버머니를'
            else:
                token_string2 = '점수를'
        if currentPlayer.gamePlay.token_type == 't':
            token_string3 = '토큰은'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string3 = '사이버머니는'
            else:
                token_string3 = '점수는'

        if currentPlayer.gamePlay.token_type == 't':
            token_string4 = '개'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string4 = '원'
            else:
                token_string4 = '점'

        context['contents'] ='여러분은 지금부터 %d번의 게임을 하게 됩니다.<br><br>'\
                              '본 게임은 %d명이 한 조로 구성되며,<br> 모든 구성원에게는 매번 %s %s의 %s 주어집니다.<br><br>' \
                              '당신은 %s의 %s<br><b> 개인 펀드 또는 공공 펀드</b>에 넣을 것인지 선택할 수 있습니다.<br><br>' \
                              '<b>공공 펀드</b>에 투자하지 않은 %s<br> 자동적으로 <b>개인 펀드</b>에 적립됩니다.' \
                              % (currentPlayer.gamePlay.main_iteration,currentPlayer.gamePlay.players, splitthousands(str(currentPlayer.gamePlay.token_given)), token_string4, token_string, token_count_string, token_string2, token_string3 )
        context['next_page'] = 'intro'
        context['next_index'] = int(num) + 1


    elif num == "1":
        template = 'game/image2_text.html'
        if currentPlayer.gamePlay.token_type == 't':
            token_string = '토큰은'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string = '사이버머니는'
            else:
                token_string = '점수는'
        if currentPlayer.gamePlay.token_type == 't':
            token_string_count = '개'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string_count = '원'
            else:
                token_string_count = '점'


        context['contents'] = '<b>개인 펀드</b>에 넣은 %s <b> %s배</b>가 되고,<br> <b>공공 펀드</b>에 넣은 %s <b>%s배</b>가 됩니다. <br><br>' \
                              '총 %d번의 시행이 끝난 후 두 펀드의 %s 당신의 총 수익으로 합산됩니다.' \
                              % (token_string,splitthousands(str(token_multiply_private)),
                                 token_string, splitthousands(str(token_multiply_public)),
                                 currentPlayer.gamePlay.main_iteration, token_string)
        context['next_page'] = 'intro'
        context['next_index'] = int(num) + 1


    elif num == "2":
        template = 'game/image3_text.html'
        if currentPlayer.gamePlay.token_type == 't':
            token_string = '토큰'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string = '사이버머니'
            else:
                token_string = '점수'
        if currentPlayer.gamePlay.token_type == 't':
            token_string2 = '토큰이'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string2 = '사이버머니가'
            else:
                token_string2 = '점수가'

        if currentPlayer.gamePlay.token_type == 't':
            token_string_count = '개'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string_count = '원'
            else:
                token_string_count = '점'

        context['contents'] = '예를 들어,<br> 당신이 개인 펀드에 투자하여 얻을 수 있는 수익은 다음과 같습니다.<br><br>' \
                              '1. 개인 펀드에 %s 0%s 가지고 있다면 : %s 원 (0 x %s)<br>' \
                              '2. 개인 펀드에 %s 1,000%s 가지고 있다면 : %s 원 (1,000 x %s)<br>' \
                              '3. 개인 펀드에 %s 2,000%s 가지고 있다면 : %s 원 (2,000 x %s)'\
                              % (token_string, token_string_count, str(0), splitthousands(str(token_multiply_private)),
                                 token_string, token_string_count, splitthousands(str(token_multiply_private * 1000)),splitthousands(str(token_multiply_private)),
                                 token_string, token_string_count, splitthousands(str(token_multiply_private * 2000)), splitthousands(str(token_multiply_private)))
        context['next_page'] = 'intro'
        context['next_index'] = int(num) + 1


    elif num == "3":
        template = 'game/image4_text.html'
        if currentPlayer.gamePlay.token_type == 't':
            token_string = '토큰'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string = '사이버머니'
            else:
                token_string = '점수'

        if currentPlayer.gamePlay.token_type == 't':
            token_string2 = '개수'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string2 = '총 양'
            else:
                token_string2 = '총 점'

        context['contents'] = '반면에, 공공 펀드에서 얻는 수익은 <br><b>' \
                              '"당신을 포함한 모든 구성원이 <br> 공공 펀드에 넣은 %s의 %s에 의해"</b>' \
                              '<br>결정됩니다.<br>구성원들이 더 많이 투자할 수록 더 많은 이익을 얻으며,<br> 수익은 모든 구성원에게 똑같이 배분됩니다.' \
                              % (token_string,token_string2 )
        context['next_page'] = 'intro'
        context['next_index'] = int(num) + 1


    elif num == "4":
        template = 'game/image5_text.html'
        if currentPlayer.gamePlay.token_type == 't':
            token_string = '토큰'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string = '사이버머니'
            else:
                token_string = '점수'
        if currentPlayer.gamePlay.token_type == 't':
            token_string_count = '개'
            token_string_count2 = '개'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string_count = '원'
                token_string_count2 = '원이'
            else:
                token_string_count = '점'
                token_string_count2 = '점이'
        if currentPlayer.gamePlay.token_type == 't':
            token_string2 = '토큰을'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string2 = '사이버머니를'
            else:
                token_string2 = '점수를'
        if currentPlayer.gamePlay.token_type == 't':
            token_string3 = '토큰이'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string3 = '사이버머니가'
            else:
                token_string3 = '점수가'

        context['contents'] = '예를 들어 <br><br>' \
                              '1) 당신이 공공 펀드에 %s 0%s 투자했으나,<br> 다른 구성원들이 투자한 %s 총 3,000%s라면 : <br>모두 1인당 %s 원씩 (3,000 x %s)<br><br>' \
                              '2) 당신이 공공 펀드에 %s 2,000%s 투자하고,<br> 다른 구성원들이 투자한 %s 총 3,000%s라면 : <br>모두 1인당 %s 원씩 ((2,000+3,000) x %s)<br><br>' \
                              '3) 당신이 공공 펀드에 %s 7,000%s 투자하고,<br> 다른 구성원들이 투자한 %s 총 0%s라면 : <br>모두 1인당 %s 원씩 (7,000 x %s)' % \
                             ( token_string2, token_string_count, token_string3, token_string_count2, splitthousands(str(3000 * token_multiply_public)), splitthousands(str(token_multiply_public)),
                                token_string2, token_string_count, token_string3, token_string_count2, splitthousands(str(5000 * token_multiply_public)), splitthousands(str(token_multiply_public)),
                                token_string2, token_string_count, token_string3, token_string_count2, splitthousands(str(7000 * token_multiply_public)), splitthousands(str(token_multiply_public)) )
        context['next_page'] = 'intro'
        context['next_index'] = int(num) + 1


    elif num == "5":
        template = 'game/image6_text.html'
        if currentPlayer.gamePlay.token_type == 't':
            token_string = '토큰'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string = '사이버머니'
            else:
                token_string = '점수'

        context['contents'] = '따라서 %d번의 게임이 끝난 후 당신의 총 수익은 다음과 같습니다. <br><br>' \
                              '총 수익 <br>= (<b>개인 펀드</b>의 총 %s x %s배) + (<b>공공 펀드</b>의 총 %s x %s배)' % \
                              (currentPlayer.gamePlay.main_iteration,token_string, splitthousands(str(token_multiply_private)), token_string, splitthousands(str(token_multiply_public)))

        context['next_page'] = 'intro'
        if currentPlayer.gamePlay.reward_On_Off:
            context['next_index'] = int(num) + 1
        else:
            context['next_index'] = int(num) + 2


    elif num == "6": # 보상 페이


        template = 'game/only_text.html'
        if currentPlayer.gamePlay.token_type == 't':
            token_string = '토큰을'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string = '사이버머니를'
            else:
                token_string = '점수를'


        context['contents'] = '여러분이 얼마의 %s 공공 펀드에 투자했는지는<br> 다른 사람에게 알려지지 않으며,<br><br> 모든 게임이 끝난 후 여러분은 총 수익에 따라 다른 결과를 제공받게 됩니다.' % (token_string)
        context['next_page'] = 'intro'
        context['next_index'] = int(num) + 1
    elif num == "7":
        context['contents'] = '게임의 규칙이 이해가 되었나요?'
        template = 'game/two_button.html'
        context['no_next_page'] = 'intro'
        context['yes_next_page'] = 'practice'
        context['NO'] = 'NO 설명 다시'
        context['YES'] = 'YES 연습게임 시작'
        context['next_index'] = 0
    else:
        context['contents'] = 'out of bound'
        context['next_page'] = 'intro'
        context['next_index'] = 0

    return render(request, template, context)




def practice(request,num="0"):

    currentPlayer = Player.objects.get(user=request.user)
    token_multiply_private = currentPlayer.gamePlay.point_calc_private
    token_multiply_public = currentPlayer.gamePlay.point_calc_public

    template = 'game/only_text.html'
    context = {}
    count = currentPlayer.gamePlay.practice_iteration


    if num == "0":
        template='game/wait_only_test.html'
        request.session['wait'] = currentPlayer.gamePlay.wait_time*1000
        request.session['iterate'] = 0
        request.session['money'] = currentPlayer.gamePlay.token_given
        request.session['total'] = 0

        context['contents'] = '연습게임을 시작하겠습니다.<br><br>다른 참가자들이 준비가 될 때까지 잠시만 기다려주세요.' \


        context['next_page'] = 'practice'
        context['wait'] = request.session['wait']
        context['next_index'] = int(num) + 1


    elif num == "1" and int(request.session.get('iterate')) < count:

        if currentPlayer.gamePlay.token_type == 't':
            token_string = '토큰이'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string = '사이버머니가'
            else:
                token_string = '점수가'

        if currentPlayer.gamePlay.token_type == 't':
            token_string2 = '토큰을'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string2 = '사이버머니를'
            else:
                token_string2 = '점수를'

        if currentPlayer.gamePlay.token_type == 't':
            token_string_count = '개'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string_count = '원'
            else:
                token_string_count = '점'


        request.session['iterate'] += 1
        template = 'game/input_money.html'

        context['next_page'] = 'practice'
        context['next_index'] = 2
        context['contents'] = '%s의 %s 지급되었습니다.<br>%s의 %s 공공펀드에 투자하겠습니까?' \
                              % (splitthousands(str(currentPlayer.gamePlay.token_given)) + token_string_count, token_string, '몇 '+token_string_count,token_string2)

        context['question'] = ''

    elif num == "2":

        import random


        minus = int(request.POST.get('minus'))
        request.session['money'] = currentPlayer.gamePlay.token_given
        fake_rand = int((random.randrange(1,currentPlayer.gamePlay.token_given) * currentPlayer.gamePlay.players)*0.001) *1000
        request.session['total'] += (currentPlayer.gamePlay.token_given-minus) * token_multiply_private + (minus+fake_rand) * token_multiply_public

        context['contents'] = ''

        assert isinstance(currentPlayer.gamePlay, object)
        if currentPlayer.gamePlay.token_type == 't':
            token_string_count = '개'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string_count = '원'
            else:
                token_string_count = '점'

#        if currentPlayer.gamePlay.feedback_my_donate_public:
        context['contents'] += '나의 공공펀드 투자 : <b>%s %s</b><br>' % (splitthousands(str(minus)), str(token_string_count))
#        if currentPlayer.gamePlay.feedback_my_donate_public:
        context['contents'] += '나의 개인펀드 투자 : ( %s ) - ( %s ) = <b> %s %s</b><br><br>' % (splitthousands(str(currentPlayer.gamePlay.token_given)),splitthousands(str(minus)),splitthousands(str(currentPlayer.gamePlay.token_given-minus)), str(token_string_count))
#        if currentPlayer.gamePlay.feedback_other_donate_public:
        context['contents'] += '다른 구성원의 투자 : 총 <b>%s %s</b><br><br>' % (splitthousands(str(fake_rand)),str(token_string_count))
#        if currentPlayer.gamePlay.feedback_my_only:
        context['contents'] += '나의 개인펀드 수익 : ( %s ) x ( %s ) = <b>%s 원</b><br>' % (splitthousands(str(currentPlayer.gamePlay.token_given-minus)),splitthousands(str(token_multiply_private)),splitthousands(str((currentPlayer.gamePlay.token_given-minus) * token_multiply_private)))
#        if currentPlayer.gamePlay.feedback_my_public:
        context['contents'] += '나의 공공펀드 수익 : {( %s ) + ( %s )} x ( %s ) = <b>%s  원</b><br><br>' % (splitthousands(str(minus)),splitthousands(str(fake_rand)),splitthousands(str(token_multiply_public)),splitthousands(str((minus+fake_rand) * token_multiply_public)))

        context['contents'] += '<b>이번 게임 나의 총 수익 : ( %s ) + ( %s ) = <span style ="color:blue">%s </span>원</b><br>' % (splitthousands(str((currentPlayer.gamePlay.token_given - minus) * token_multiply_private)),splitthousands(str((minus + fake_rand) * token_multiply_public)),splitthousands(str((currentPlayer.gamePlay.token_given - minus) * token_multiply_private + (minus + fake_rand) * token_multiply_public)))
        context['contents'] += '<b>나의 누적 총 수익 :  <span style ="color:red">%s </span>원<br></b>' % (splitthousands(str(request.session['total'])))

        context['next_page'] = 'practice'
        context['next_index'] = 1
    else:
        template = 'game/two_button.html'
        context['contents'] = '게임의 규칙이 이해가 되었나요?'
        context['no_next_page'] = 'practice'
        context['yes_next_page'] = 'real_game'
        context['wait'] = request.session['wait']
        context['NO'] = 'NO'
        context['YES'] = 'YES'
        context['next_index'] = 0
    return render(request, template, context)

def real_game(request,num="0"):
    currentPlayer = Player.objects.get(user=request.user)
    token_multiply_private = currentPlayer.gamePlay.point_calc_private
    token_multiply_public = currentPlayer.gamePlay.point_calc_public

    template = 'game/only_text.html'
    context = {}
    count = currentPlayer.gamePlay.main_iteration
    if num == "0":
        template = 'game/wait_only_test.html'
        request.session['how_much'] = ''
        request.session['iterate'] = 0
        request.session['wait'] = currentPlayer.gamePlay.wait_time * 1000
        request.session['real_iterate'] = 0
        request.session['money'] = currentPlayer.gamePlay.token_given
        request.session['total'] = 0

        context['contents'] = '본 게임을 시작하겠습니다.<br><br>다른 참가자들이 준비가 될 때까지 잠시만 기다려주세요.' \

        context['next_page'] = 'real_game'
        context['wait'] = request.session['wait']
        context['next_index'] = 1


    elif num == "1":
        context['contents'] = "지금부터 본 게임을 시작하겠습니다."
        context['next_page'] = 'real_game'
        context['next_index'] = 2

    elif num == "2" and int(request.session.get('real_iterate')) < count:

        if currentPlayer.gamePlay.token_type == 't':
            token_string = '토큰이'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string = '사이버머니가'
            else:
                token_string = '점수가'

        if currentPlayer.gamePlay.token_type == 't':
            token_string2 = '토큰을'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string2 = '사이버머니를'
            else:
                token_string2 = '점수를'

        if currentPlayer.gamePlay.token_type == 't':
            token_string_count = '개'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string_count = '원'
            else:
                token_string_count = '점'

        request.session['real_iterate'] += 1
        template = 'game/input_money.html'
        context['next_page'] = 'real_game'
        request.session['money'] = currentPlayer.gamePlay.token_given
        context['next_index'] = 3
        context['contents'] = '%s의 %s 지급되었습니다.<br>%s의 %s 공공펀드에 투자하겠습니까?' \
        % (splitthousands(str(currentPlayer.gamePlay.token_given)) + token_string_count, token_string, '몇 ' + token_string_count,token_string2)

        context['question'] = ''
    elif num == "3":
        minus = int(request.POST.get('minus'))

        request.session['how_much'] += str(minus) + ','

        request.session['total'] += minus

        import random

        minus = int(request.POST.get('minus'))
        request.session['money'] = currentPlayer.gamePlay.token_given

        assert isinstance(currentPlayer, object)
        fake_rand = int((random.randrange(1, currentPlayer.gamePlay.token_given) * currentPlayer.gamePlay.players) * 0.001) * 1000
        request.session['total'] += (currentPlayer.gamePlay.token_given-minus) * token_multiply_private + (minus+fake_rand) * token_multiply_public
        context['contents'] = ''

        if currentPlayer.gamePlay.token_type == 't':
            token_string_count = '개'
        else:
            if currentPlayer.gamePlay.token_type == 'c':
                token_string_count = '원'
            else:
                token_string_count = '점'

            if currentPlayer.gamePlay.feedback_my_donate_public:
                context['contents'] += '나의 공공펀드 투자 : <b>%s %s</b><br>' % (
                splitthousands(str(minus)), str(token_string_count))
            if currentPlayer.gamePlay.feedback_my_donate_public:
                context['contents'] += '나의 개인펀드 투자 : ( %s ) - ( %s ) = <b> %s %s</b><br><br>' % (
                splitthousands(str(currentPlayer.gamePlay.token_given)), splitthousands(str(minus)),
                splitthousands(str(currentPlayer.gamePlay.token_given - minus)), str(token_string_count))
            if currentPlayer.gamePlay.feedback_other_donate_public:
                context['contents'] += '다른 구성원의 투자 : 총 <b>%s %s</b><br><br>' % (
                splitthousands(str(fake_rand)), str(token_string_count))
            if currentPlayer.gamePlay.feedback_my_only:
                context['contents'] += '나의 개인펀드 수익 : ( %s ) x ( %s ) = <b>%s 원</b><br>' % (
                splitthousands(str(currentPlayer.gamePlay.token_given - minus)),
                splitthousands(str(token_multiply_private)),
                splitthousands(str((currentPlayer.gamePlay.token_given - minus) * token_multiply_private)))
            if currentPlayer.gamePlay.feedback_my_public:
                context['contents'] += '나의 공공펀드 수익 : {( %s ) + ( %s )} x ( %s ) = <b>%s  원</b><br><br>' % (
                splitthousands(str(minus)), splitthousands(str(fake_rand)), splitthousands(str(token_multiply_public)),
                splitthousands(str((minus + fake_rand) * token_multiply_public)))

                context['contents'] += '<b>이번 게임 나의 총 수익 : ( %s ) + ( %s ) = <span style ="color:blue">%s </span>원</b><br>' % (
                splitthousands(str((currentPlayer.gamePlay.token_given - minus) * token_multiply_private)),
                splitthousands(str((minus + fake_rand) * token_multiply_public)), splitthousands(str(
                    (currentPlayer.gamePlay.token_given - minus) * token_multiply_private + (
                    minus + fake_rand) * token_multiply_public)))
                context['contents'] += '<b>나의 누적 총 수익 :  <span style ="color:red">%s </span>원<br></b>' % (
                splitthousands(str(request.session['total'])))


        context['next_page'] = 'real_game'
        context['next_index'] = 2
    else:
        template = 'game/end.html'
        context['contents'] = "당신이 획득한 총 수익은 "+splitthousands(str(request.session.get('total')))+"원 입니다"
        print('shit')
        print(request.session['how_much'].split(',')[:-1])
        currentPlayer.total_donate = sum([int(i) for i in request.session['how_much'].split(',')[:-1]])
        currentPlayer.all_donate_list = request.session['how_much']
        currentPlayer.finished = True
        currentPlayer.save()
        context['next_page'] = 'logout'
    return render(request, template, context)

def splitthousands(s, sep=','):
    if len(s) <= 3: return s
    return splitthousands(s[:-3], sep) + sep + s[-3:]

def downloadcsv(request):
    if request.user.is_superuser:
        import csv
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="all_result.csv"'

        writer = csv.writer(response)
        writer.writerow(['User_ID','game_ID','total_donate','trial_main','token_type','token_given'])
        for obj in Player.objects.all():
            row = [str(obj.user_id),str(obj.gamePlay_id),str(obj.total_donate),str(obj.gamePlay.main_iteration) ,str(obj.gamePlay.token_type),str(obj.gamePlay.token_given)]
            for test in obj.all_donate_list.split(','):
                row.append(test)
            print(row)
            writer.writerow(row)
    else :
        return redirect('http://www.naver.com')
    return response
