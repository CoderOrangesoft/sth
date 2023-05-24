import opt
import random
import math

version = "𝟭.𝟯 𝗯𝘂𝗶𝗹𝗱𝟭"
print("OrangeBounce version",version,"by Orangesoft")
print("新版本下载地址: coderorangesoft.github.io/d")
print("本代码开源 并基于GPL3.0协议")
#在这里输入密码
password = "liaoyongan"

#0为防守,1为攻击,2为随机,3为蹲守
if ((password[8] == "a") and (password[9] == "n")):
    print("[PASSWORD PROTECT 1A]密码验证成功!")
    TANK1 = 1
    TANK2 = 1
    TANK3 = 1
    TANK4 = 0
    TANK5 = 3

if (password[1] != "i"):
    #密码保护程序
    password = 0
    TANK1 = 0
    TANK2 = 0
    TANK3 = 0
    TANK4 = 0
    TANK5 = 0
    print("[PASSWORD PROTECT 2A]密码验证失败!")
    print("[PASSWORD PROTECT 2B]代码停止!")
else:
    print("[PASSWORD PROTECT 2A]密码验证成功!")

#不要动 不然输了我不负责
if (password):
    #密码保护程序
    r1 = random.randint(0,1)
    r2 = random.randint(0,1)
    r3 = random.randint(0,1)
    r4 = random.randint(0,1)
    r5 = random.randint(0,1)

def tank1_update():
    global password
    if (password):
        global TANK1
        if TANK1 == 0:
            return defence()
        elif TANK1 == 1:
            return attack()
        elif TANK1 == 3:
            return doorKeeper()
        else:
            if r1 == 1:
                return attack()
            else:
                return defence()


def tank2_update():
    global password
    if (password):
        global TANK2
        if (password):
            if TANK2 == 1:
                return attack()
            elif TANK2 == 0:
                return defence()
            elif TANK2 == 3:
                return doorKeeper()
            else:
                if r2 == 1:
                    return attack()
                else:
                    return defence()


def tank3_update():
    global password
    global TANK3
    if TANK3 == 1:
        if (password):
            return attack()
        else:
            print("[PASSWORD PROTECT 3A](with function)密码验证失败!")
            return 0,0
    elif TANK3 == 0:
        return defence()
    elif TANK3 == 3:
        return doorKeeper()
    else:
        if r3 == 1:
            return attack()
        else:
            return defence()


def tank4_update():
    global password
    global TANK4
    if TANK4 == 1:
        return attack()
    elif TANK4 == 0:
        return defence()
    elif TANK4 == 3:
        return doorKeeper()
    else:
        if r4 == 1:
            return attack()
        else:
            return defence()

def tank5_update():
    global password
    global TANK5
    if TANK5 == 1:
        if (password):
            return attack()
    elif TANK5 == 0:
        return defence()
    elif TANK5 == 3:
        if (password):
            return doorKeeper()
    else:
        if r5 == 1:
            return attack()
        else:
            return defence()


# 定义机器人attack( )进攻策略的方法
def attack():
    if opt.BALL.vx < 0:
        if opt.BALL.y > 0 :
            vs , hs = move_to(opt.BALL.x-2 , opt.BALL.y-2)
        else:
            vs , hs = move_to(opt.BALL.x-2 , opt.BALL.y+2)
    else:
        if opt.BALL.y > 0 :
            vs , hs = move_to(opt.BALL.x-1.5 , opt.BALL.y+1.5)
        else:
            vs , hs = move_to(opt.BALL.x-1.5 , opt.BALL.y-1.5)
    angle_ball = opt.TANK.angle_to(opt.BALL.x,opt.BALL.y)
    if opt.TANK.cool_remain == 0:
        if angle_ball > 0 and angle_ball < 2:
            opt.TANK.do_fire()
        if angle_ball > 358 and angle_ball < 360:
            opt.TANK.do_fire()
    
    # 当attack()被tank_update()调用时，每一帧都会执行以上策略，并返回vs,hs值
    return vs, hs


# 定义机器人defence( )防守策略的方法
def defence():
    if opt.BALL.x < -35:
        vs , hs = move_to(opt.BALL.x-3 , opt.BALL.y)
    elif opt.BALL.y >= 0 :
        if opt.TANK.is_point_in_range(-49, 5, 1):
            vs, hs = 0, 0
        else:
            vs , hs = move_to(-49 , 5)
    else:
        if opt.TANK.is_point_in_range(-49, -5, 1):
            vs, hs = 0, 0
        else:
            vs , hs = move_to(-49 , -5)  
    # 当defence()被tank_update()调用时，每一帧都会执行以上策略，并返回vs,hs值
    return vs, hs

def doorKeeper():
    ball_x = opt.BALL.x
    ball_y = opt.BALL.y

    if 8 > ball_y > -8 and 43 < ball_x < 50: 
        vs, hs = move_to(ball_x-2, ball_y)
    elif opt.TANK.is_point_in_range(46,0,1):
        vs, hs = 0 ,0
    else:
        vs, hs = move_to(46 , 1)
    return vs, hs
  

# 定义一个move_to(tx, ty)函数，使机器人自动向目标点(tx, ty)行驶
def move_to(tx, ty):
    radian = opt.TANK.radian_to(tx, ty)
    vs = math.cos(radian)
    hs = -1 * math.sin(radian)
    return vs, hs
