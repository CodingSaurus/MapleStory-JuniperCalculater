print("[쥬니퍼베리 씨앗 계산기]\n")

while True:
    seed = int(input("쥬니퍼베리 씨앗 가격 입력 : "))
    seed_low = seed * 50 / 200
    seed_high = seed * 60 / 200

    oil = int(input("쥬니퍼베리 씨앗 오일 가격 입력 : "))
    oil_realPrice = seed * 6 * 10 #단순히 씨앗을 6개 사용해서 만든 오일 10개의 순수 가격임. 씨앗을 그대로 팔았을 때의 가격이라 마진이 없다고 봄
    oil_salePrice = oil * 9 #씨앗을 오일로 가공 한 이후의 가격. 우리가 얻을 금액. 마진이 붙어있음. 씨앗은 60개 썼다고 생각하되 오일은 9개임.

    jehwek = int(input("재획비 가격 입력 : "))
    jehwek_realPrice_make = seed * 66 #오일 10개 만들어서 쓸 때
    jehwek_realPrice_buy = oil * 10 #오일 10개 사서 쓸 때

    print("\n★ 쥬니퍼베리 씨앗을 팔았을 때 피로도 1당 메소의 기댓값은", seed_low, "~", seed_high)
    print("- 최저 기댓값 50개, 최고 기댓값 60개 나왔다고 가정함.")

    print("\n★ 쥬니퍼베리 씨앗 오일을 팔았을 때 피로도 1당 메소의 기댓값은", ((oil_salePrice - oil_realPrice)/10))
    print("- 오일 제작은 10퍼센트 확률로 실패함")

    print("\n★ 재획비")
    print("만들어서 팔았을 때 피로도 1당 메소의 기댓값은", (((jehwek * 3) - jehwek_realPrice_make)) / 5)
    print("사서 팔았을 때 피로도 1당 메소의 기댓값은", (((jehwek * 3 ) - jehwek_realPrice_buy) / 5))
    print("\n- 쥬니퍼베리 씨앗오일 외 다른 재료 가격은 고려하지 않음")

    print("\n--------------------------------------------------------------------\n")
