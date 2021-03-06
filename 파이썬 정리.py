모든 프로그래밍은 결국 데이터를 다루는 행위
  자료형에 대한 이해는 프로그래밍의 길에 있어서는 첫걸음
파이썬의 자료형으로는 <정수형, 실수형, 복소수형, 문자열, 리스트, 튜플, 사전>등이 있다.
  파이썬의 자료형은 필수적으로 알아두어야 한다.

//

정수형(Interger) == 정수를 다루는 자료형

양, 음, 0 포함

EX)
# 양의 정수

a = 1000
print(a)

# 음의 정수

a = -7
print(a)

# 0

a = 0
print(a)


실수형(Real Number) == 소수점 아래의 데이터를 포함하는 수 자료형

EX1)
# 양의 실수

a = 10.123
print(a)

# 음의 실수

a = -10.123
print(a)

// 수 자료형의 연산

수 자료형에 대하여 사칙연산과 나머지 연산자가 많이 사용된다.

단, 나누기 연산자를 주의해서 사용하여야 한다.

파이썬에서 나누기 연산자(/)는 나눠진 결과를 실수형으로 반환한다

다양한 로직을 설계할 때 나머지 연산자(%)를 이용해야 할 때가 많다.

몫을 얻기 위해서는 몫 연산자(//)를 사용한다

또 거듭제곱 연산자(**)도 있다.

//

리스트 자료형

여러개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형이다

C나 자바에서 Array의 기능 및 연결 리스트와 유사한 기능을 지원한다,

1. 리스트 초기화

리스트는 대괄호 ([]) 안에 원소를 넣어 초기화 하며 쉼표로 원소를 구분한다
비어 있는 리스트를 선언하고자 할 때는 list() 혹은 간단히 []를 이용할 수 있다.
리스트의 원소에 접근할때는 인덱스의 값을 괄호에 넣는다

EX)

a =  [1, 2, 3, 4, 5]
print(a)

print(a[3])

n = 10
a = [0] * n
print(a)

바꾸고 싶을 때

a[4] = 4 # 5번째 원소가 바뀜

이렇게 인덱스 값을 입력하여 리스트의 특정한 원소에 접근 하는 것을 인덱싱이라고 한다.

리스트에서 연속적인 위치를 갖는 원소들을 가져와야 할 때는 슬라이싱(Slicing)을 이용한다.

대괄호 안에 콜론(:)을 넣어서 시작 인덱스와 끝 인덱스를 설정할 수 있습니다.
끝 인덱스는 실제 인덱스보다 1을 더 크게 설정한다.

EX)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#네 번째 원소만 출력

print(a[3])

# 두 번째 원소부터 네번째 원소까지
print(a[1 : 4]) 

# 결과 : [2, 3, 4]

리스트 컴프리헨션

array = [ i for i in range(10)]

print(array)

// 응용하기

# 0 부터 19까지의 수 중에서 홀수만 포함하는 리스트

array = [ i for i in range(20) if i % 2 == 1] #0~19 for = 그때의 그 원소만을 남겨두겠다.
print(array)

# 1 부터 9까지의 수들의 제곱 값을 포함하는 리스트

array = [i * i for i in range(1, 20)] #1~19
print(array)

리스트 관련 기타 메서드

append()
변수명.append()
리스트에 원소 하나를 삽입할 때 사용한다
시간 복잡도는 O(1)

sort()
변수명.sort() // 변수명.sort(reverse = True)
기본 정렬 기능으로 오름차순(혹은 내림차순)으로 정렬한다
시간 복잡도는 O(NlogN)

reverse()
변수명.reverse()
리스트의 원소의 순서를 모두 뒤집어 놓는다
시간 복잡도는 O(N)

insert()
insert(삽입할 위치 인덱스, 삽입할 값)
특정한 인덱스의 위치에 원소를 삽입할 때 사용한다.
시간 복잡도는 O(N)

count() 
변수명.count(특정 값)
리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 사용한다.
시간 복잡도는 O(N)

remove()
변수명.remove(특정 값)
특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러 개면 하나만 제거한다.
시간 복잡도는 O(N)

//

리스트에서 특정 값을 가지는 원소 모두 제거하기

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

#remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set] # i라는 원소가 a에 있는 원소를 하나씩 확인 하면서 그때의 i 가 제거 대상이 아닐때만 남겨두어라
print(result)

//

문자열 자료형

문자열 변수를 초기화할 때는 큰따옴표나 작은 따옴표를 이용한다.

a = 'Hello world'
print(a)

문자열 연산

문자열 변수에 덧셈을 이용하면 문자열이 더해져서 연결(Concatenate)된다.
문자열 변수를 특정한 양의 정수와 곱하는 경우, 문자열이 그 값만큼 여러 번 더해지게 된다.
문자열에 대해서도 마찬가지로 인덱싱, 슬라이싱을 이용할 수 있다.

다만, 문자열은 특정 인덱스의 값을 변경할 수는 없다. (Immutable)

//

튜플 자료형

튜플 자료형은 리스트랑 유사, 문법적 차이 유

튜플은 한 번 선언된 값을 변경할 수 없다.
리스트는 대괄호[]를 사용하지만 튜플은 소괄호()를 사용한다.

EX)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

#네 번째 원소만 출력
print(a[3])

#두 번째 원소부터 네 번째 원소까지
print(a[1 : 4])

튜플을 사용하면 좋은 경우

서로 다른 성질의 데이터를 묶어서 관리해야 할 때
EX) 최단경로 알고리즘에서는 (비용, 노드번호) 형태로 튜플 자료형을 자주 사용

데이터의 나열을 해싱(Hashing)의 키 값으로 사용해야 할 때
튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용 될 수 있다.

리스트보다 메모리를 효율적으로 사용해야 할 때

// 

사전 자료형

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
  print("'사과'를 키로 가지고 있는 데이터가 존재합니다")

//

사전 자료형 관련 메서드

사전 자료형에서는 키와 값을 별도로 뽑아내기 위한 메서드를 지원
  키 데이터만 뽑아서 리스트로 이용할 때는 keys() 함수를 이용합니다.
  값 데이터만을 뽑아서 리스트로 이용할 때는 values() 함수를 이용합니다.
  
EX)

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

#키 데이터만을 담은 리스트 생성
key_list = data.keys()

#값 데이터만을 담은 리스트 생성
value_list = data.values()

#출력해보기
print(key_list)
print(value_list)

#각 키에 따른 값을 하나씩 출력
for key in key_list:
  print(data[key])
  
//

집합 자료형

집합은 

1. 중복을 허용하지 않는다
2. 순서가 없다

집합은 리스트 혹은 문자열을 이용해서 초기화 할 수 있다.
이때 set() 함수를 이용한다.

또는 중괄호 안에 각 원소를 콤마를 기준으로 구분하여 삽입함으로써 초기화 할 수 있다.
데이터의 조회 및 수정에 있어서 O(1) - 상수 의 시간에 처리

사전 자료형과 집합 자료형의 특징

리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있습니다.
사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없습니다.
  사전의 키 혹은 집합의 원소를 이용해 O(1)의 시간 복잡도로 조회합니다.




 
