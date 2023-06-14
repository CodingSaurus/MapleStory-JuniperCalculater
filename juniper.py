print("[쥬니퍼베리 씨앗 계산기]\n")

while True:
    seed = int(input("쥬니퍼베리 씨앗 가격 입력 : "))
    seed_low = (seed * 50 / 200)
    seed_high = (seed * 60 / 200)

    oil = int(input("쥬니퍼베리 씨앗 오일 가격 입력 : "))
    oil_realPrice = (seed * 6 * 10)
    oil_salePrice = (oil * 9)

    print("\n쥬니퍼베리 씨앗을 팔았을 때 피로도 1당 메소의 기댓값은", seed_low, "~", seed_high)
    print("최저 기댓값 50개, 최고 기댓값 60개 나왔다고 가정함.")

    print("\n쥬니퍼베리 씨앗 오일을 팔았을 때 피로도 1당 메소의 기댓값은", ((oil_salePrice - oil_realPrice)/10))
    print("오일 제작은 10퍼센트 확률로 실패함")
    print("\n--------------------------------------------------------------------\n")
