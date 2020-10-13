def solution(seoul):
    location = seoul.index('Kim')
    answer = f'김서방은 {location}에 있다'


    for kim in seoul:
        if 'Kim' in seoul:
            return answer