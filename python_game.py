from random import randint
from random import choice
from time import sleep

class unit():
    maxhp = 1
    hp = 1
    maxmp = 1
    mp = 1
    atk = 1
    rate = 1
    run = 1
    level = 1
    turn = 1
    na = 1
    def __init__(self, name):
        self.name = name

class 탑(unit):
        maxhp = 200
        hp = 200
        maxmp = 100
        mp = 100
        atk = 50
        rate = 8
        run = 1
        level = 1
        def 스킬(self):
            print("""전격폭발 : 전기에너지 구체를 상대에게 100 데미지를  날린다. mp 40 소모
                  초전하 : 전기에너지를 내뿜어 상대에게 40 데미지를 입힌다. mp 20 소모
                  가속관문 : 전기장을 생성해 상대에게 위협을 가한다. mp 10 소모 """)
        def 전격폭발(self):
            if self.mp >=40:
                print("구체가 적중했다")
                self.mp -= 40
                self.atk = 100
            else:
                print("마나가 모자르다...")
                self.turn = 0
                
        def 초전하(self):
            if self.mp>= 20:
                print("에너지가 내뿜어지기 시작했다.")
                print("주변이 파랗게 변한다..")
                self.mp -= 20
                self.atk = 40
            else:
                print("마나가 모자르다...")
                self.turn = 0
        def 가속관문(self):
            if self.mp >= 10:
                print("푸르른 전기장이 생성되었다.")
                print("왠지 접근하면 안될것같다..")
                self.mp -= 10
            else:
                print("마나가 모자르다...")
                self.turn = 0
class 미드(unit):
        maxhp = 150
        hp = 150
        maxmp = 200
        mp = 200
        atk = 20
        rate = 8
        run =1
        level = 1
        def 스킬(self):
            print("""
            과부하 : 마법 에너지를 모아 돌풍을 발사한다. 상대에게 100 데미지를 입힌다. mp 20 소모
            룬감옥 : 마법 에너지로 상대를 가둬놓는 감옥을 생성한다. 상대에게 50 데미지를 입힌다. mp 10 소모
            주문전이 : 마법 에너지로 상대를 타격하고 표식을 남긴다. 상대에게 50 데미지를 입힌다. mp 15 소모""")
        def 과부하(self):
            if self.mp >= 20:
                print("돌풍이 날라갔다.")
                print("정확히 적중했다!")
                self.mp -= 20
                self.atk = 100
            else:
                print("마나 관리좀 하지!")
                self.turn = 0
        def 룬감옥(self):
            if self.mp >=10:
                print("푸르른 감옥이 생성되었다.")
                print("상대는 꼼짝을 못한다!")
                self.mp -= 10
                self.atk = 50
            else:
                print("마나 관리좀 하지!")
                self.turn = 0
        def 주문전이(self):
            if self.mp >= 15:
                print("마법데미지를 입혔다.")
                print("상대에게 표식이 남았다!")
                self.mp -= 15
                self.atk = 50
            else:
                print("마나 관리좀 하지!")
                self.turn = 0
class 원딜(unit):
        maxhp = 120
        hp = 120
        maxmp = 100
        mp = 100
        atk = 50
        rate =10
        run = 1
        level = 1
        def 스킬(self):
            print("""
                이케시아폭우 : 근처 상대에게 미사일을 날린다. 상대에게 60 데미지를 입힌다. mp 50 소모
                공허추적자 : 상대에게 80 데미지짜리 미사일을 날린다. mp 80 소모
                고속충전 : 본인의 마나를 50 충전한다. mp 20 소모""")
        def 이케시아폭우(self):
            if self.mp>= 50:
                print("미사일이 적중했다")
                print("상당히 고통스러울거야")
                self.mp -= 50
                self.atk = 60
            else:
                print("고속충전이 필요하겠군")
                self.turn = 0
        def 공허추적자(self):
            if self.mp>=80:
                print("이 미사일은 확실히 강력하다")
                self.mp -= 80
                self.atk = 80
            else:
                print("고속충전이 필요하겠군")
                self.turn = 0
        def 고속충전(self):
            if self.mp>=10:
                print("마나가 충전되었다.")
                self.mp += 40
            else:
                print("난 이제 가망이 없어..")
                self.turn = 0
class 드래곤(unit): 
        hp = 200
        mp = 200
        atk = 50
        rate = 8
        def 평타(self):
            self.mdmg = self.atk
        def 브레스(self):
            if self.mp >= 50:
                print("불이다 불!!!!!!!!!!!")
                self.mp -= 50
                self.mdmg = 60
            else:
                print("아직 불을 뿜을 힘이 없나보다")
        def 꼬리치기(self):
            if self.mp >= 50:
                print("꼬리를 피하지 못했다.. 너무 빠른걸")
                self.mp -= 50
                self.mdmg = 60
            else:
                print("잘하면 드래곤을 잡을수도..?")
        def AI(self):
            if self.hp <= 0:
                print("드래곤이 쓰러졌다.")
            elif randint(1,3) == 1:
                print("드래곤이 공격한다!!!!!!!")
                self.평타()
            elif randint(1,3) == 2:
                print("아니.. 드래곤의 입에서...?")
                self.브레스()
            elif randint(1,3) == 3:
                print("으잉 갑자기 드래곤이 등을 돌려..?")
                self.꼬리치기()
class 바론(unit):
        hp = 300
        mp = 200
        atk = 60
        rate = 8
        def 평타(self):
            self.mdmg = self.atk
        def 포이즌레인(self):
            if self.mp >= 50:
                print("독을 흠뻑 맞았다.")
                self.mp -= 50
                self.mdmg = 80
            else:
                print("바론은 씩씩거리고있다.")
        def 독의습격(self):
            if self.mp >= 40:
                print("독이 몸에 묻었다.")
                self.mp -= 40
                self.mdmg = 60
            else:
                print("입에 독을 물고있는거야 쟤..?")
        def AI(self):
            if self.hp <= 0:
                print("바론을 잡았다!!!!!!!")
            elif randint(1,3) ==1:
                print("바론이 날 때려!")
                self.평타()
            elif randint(1,3) ==2:
                print("초록색 액체가 보이는데..?")
                self.포이즌레인()
            elif randint(1,3) ==3:
                print("바론이 화가 난 것 같 아..")
                self.독의습격()
class 미니언(unit):
        hp = 50
        atk = 10
        rate = 1
        def 평타(self):
            self.mdmg = self.atk
        def AI(self):
            if self.hp <=0:
                print("미니언 정도는 우습지")
            else:
                print("아이 간지러워")
                self.평타()
class 대포미니언(unit):
        hp = 80
        atk = 20
        rate = 1
        def 평타(self):
            self.mdmg = self.atk
        def AI(self):
            if self.hp <=0:
                print("대포는 좀 버거웠군..")
            else:
                print("얘는 생각보다 강력하다..")
                self.평타()
              
turn = 0
start = 1
name = input("닉네임을 정해봅시다 : ")
while start == 1:
    line = input('''탑,미드,원딜''' + name + " 의 직업은? ")
    if line == '탑':
        cha = 탑('cha')
        break
    elif line == '미드':
        cha = 미드('cha')
        break
    elif line == '원딜':
        cha = 원딜('cha')
        break
    else:
        print("서폿 가고싶으세요..?")
        sleep(1)
sleep(1)
print("탈출을 시작해 보자!")
while start == 1:
    sleep(1)
    way = input('''상하좌우'''+ name + "는 어디로 갈까? :")
    if way == '상':
        st = 미니언('st')
        wi = '미니언'
        sleep(1)
        print(name + "는 위로 향했다.")
        sleep(1)
        print("미니언이다!")
        break
    elif way == '하':
        st = 대포미니언('st')
        wi = '대포미니언'
        sleep(1)
        print(name + "는 아래로 향했다.")
        sleep(1)
        print("대포미니언이다!")
        break
    elif way == '좌':
        st = 드래곤('st')
        wi = '드래곤'
        sleep(1)
        print(name + "는 왼쪽으로 향했다.")
        sleep(1)
        print("드래곤이다!")
        break
    elif way == '우':
        st = 바론('st')
        wi = '바론'
        sleep(1)
        print(name + "는 오른쪽으로 향했다.")
        sleep(1)
        print("바론이라니 세상에..")
        break
    else:
        print("고민은 길수록 좋지않아")
while cha.hp > 0 and st.hp > 0:
    sleep(1)
    turn = turn + 1
    print( str(turn) + "번째 턴")
    sleep(1)
    print("-----------" + name + "의 턴-----------")
    while start ==1:
        
        st.mdmg = 0
        a = input(name + "는 무엇을 할까? 공격 or 스킬")
        if a == '공격':
            cha.dmg = cha.atk
            print(name + "의 공격")
            break
        elif a == '스킬':
            cha.스킬()
        elif a == '전격폭발':
            cha.전격폭발()
            break
        elif a == '초전하':
            cha.초전하()
            break
        elif a == '가속관문':
            cha.가속관문()
            break
        elif a == '과부하':
            cha.과부하()
            break
        elif a == '룬감옥':
            cha.룬감옥()
            break
        elif a == '주문전이':
            cha.주문전이()
            break
        elif a == '이케시아폭우':
            cha.이케시아폭우()
            break
        elif a == '공허추적자':
            cha.공허추적자()
            break
        elif a == '고속충전':
            cha.고속충전()
            break
        else:
            print("그 행동이 아니잖아!?")
    if cha.atk > 0 and randint(1,10) >= cha.rate:
        sleep(1)
        print("아니 빗나갔다고..?")
    elif cha.atk > 0:
        st.hp = st.hp - cha.atk
        
    
    sleep(1)
    print("----------몬스터 차례----------")
    sleep(1)
    st.AI()
    if st.mdmg > 0 and randint(1,10) >= st.rate:
        sleep(1)
        print("오 간신히 피했다..")
    elif st.mdmg > 0:
        sleep(1)
        cha.hp = cha.hp - st.mdmg
if cha.hp <= 0:
    sleep(1)
    print(name + "는 사망했다.")
    sleep(1)
if st.hp <= 0 :
    sleep(1)
    print(name + "가 승리했다.")
