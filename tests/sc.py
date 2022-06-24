from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{} 유닛이 생성되었습니다.".format(name))
    
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        self.hp -= damage
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        super().__init__(name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        super().__init__("마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        super().__init__("탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if self.seize_developed == False:
            return
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.seize_mode == True
            self.damage *= 2
            self.speed = 0
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.seize_mode == False
            self.damage /= 2
            self.speed = 1

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        super().__init__(name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        super().__init__("레이스", 80, 20, 5)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == True:
            self.clocked == False
            print("{} : 클로킹 모드가 해제되었습니다.".format(self.name))
        else:
            self.clocked = True
            print("{} : 클로킹 모드가 설정되었습니다.".format(self.name))

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

game_start()
m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5, 20))

game_over()