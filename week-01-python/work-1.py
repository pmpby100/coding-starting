# 구현 내용
# - 처음 파이썬을 실행시키면,
# 한식, 중식, 일식 중 한 가지를 고르라는 내용이 나옵니다.
# - 그 중에서 한 가지를 고르면 식당 이름을 하나 임의로 추천해 줍니다.
#
# 힌트
# 리스트를 여러 개 사용하고 사용자의 입력을 받아야 합니다.
# 리스트에서 데이터를 임의로 하나를 뽑는 방법은 크게 2가지가 있습니다.
# 그 중 어느 걸 사용해도 좋습니다.
# 다만 강의 중에 해당 내용을 배우지 않기 때문에, 검색을 활용합니다.
# 검색 키워드 : random, randint, shuffle, choice

import random

# 1) 리스트를 만든다
KOREAN_FOOD = ("김치찌개", "비빔밥", "국수")
CHINESE_FOOD = ("짜장면", "탕수육", "짬뽕")
JAPANESE_FOOD = ("라멘", "돈까스", "돈부리")

# 2) 사용자로부터 입력
user_choice = input("한식, 중식, 일식 중에서 골라주세요:")

# 3) 임의로 추천
if user_choice == "한식":
    choice_result = random.choice(KOREAN_FOOD)
    # choice_result = KOREAN_FOOD(
    #     random.randint(0, lenKOREAN_FOOD))
    # )
elif user_choice == "중식":
    choice_result = random.choice(CHINESE_FOOD)
elif user_choice == "일식":
    choice_result = random.choice(JAPANESE_FOOD)
else:
    print("한식, 중식, 일식 중에서 선택하셔야 됩니다.")

if choice_result:
    print("{} 중에서 {}가 선택 되었습니다.".format(user_choice, choice_result))
