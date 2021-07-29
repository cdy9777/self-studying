import re

p = re.compile('ca.e')
# . (ca.e) : .은 하나의 문자열 의미 > care,cafe,case | caffee(x)
# ^ (^de) : 문자열의 시작 > desk, destination | fade(x)
# $ (se$) : 문자열의 끝 > case, base | face(x)


def print_match(m):
    if m:
        print(m)
        # print(m.group())  # 일치하는 부분 문자열 반화
        # print(m.string)  # 입력받은 문자열 반환
        # print(m.start())  # 일치하는 문자열의 시작 index
        # print(m.end())  # 일치하는 문자열의 끝 index
        # print(m.span())  # 일치하는 문자열의 시작/끝 index
    else:
        print('매칭되지 않음')


# m = p.match('careless')  # match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.serach('careless') # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

m = p.findall('good care cafe')  # findall: 주어진 문장에서 일치하는 부분 모두 리스트로 반환
print_match(m)
