#1. 퀴즈1 / 재귀함수 리스트 평탄화
example = [[1,2,3],[4,[5,6]],7,[8,9]]

flatten(example)
[7]

def flatten(example):
    output = []
    for item in example:
        if type(item) == list:
            output.extend(flatten(item))
        else:
            output.append(item)
    return output

print(flatten(example))




#2. 퀴즈2 / 재귀함수 x의 n제곱
def power(a, n):
    if n == 1:
        return a
    return power(a, n-1) * a

power(2, 10)




#3. 퀴즈3 / 재귀함수 최대공약수
def gcd(a, b):
    if a % b == 0:
        return b
    return(gcd(b, a % b))


gcd(192,162)
