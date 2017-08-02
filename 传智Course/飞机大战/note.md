## 项目一 飞机大战
### Pygame
Pygame是一组功能强大而有趣的模块，可用于管理图形、动画乃至声音，让你更轻松的开发复杂的游戏。

### 安装Pygame（Ubuntu）
安装pip:
pip --version
sudo apt-get install python-pygame

### 阶段：
创建一艘能够根据用户输入而左右移动和射击的飞船
创建一群作为射杀目标的外星人，并做其它改进，如限制可供玩家使用的飞船数以及添加记分牌

### 规划项目
在游戏《外星人入侵》中，玩家控制着一艘最初出现在屏幕底部中央的飞船。玩家可以使用箭头键左右移动飞船，还可使用空格键进行射击。游戏开始时，一群外星人出现在天空中，他们在屏幕中向下移动。玩家的任务是射杀这些外星人。玩家将所有外星人都消灭干净后，将出现一群新的外星人，他们移动的速度更快。只要有外星人撞到了玩家的飞船或到达了屏幕底部，玩家就损失一艘飞船。玩家损失三艘飞船后，游戏结束。

### 开始游戏
1. 创建Pygame窗口：
screen=pygame.display.set_mode((x,y),0,32)
2. 创建一个和窗口大小的图片，用来充当背景
background=pygame.image.load(imgpath).convert()
3. 把图片放到窗口中显示

4. 创建一个飞机图片
```python
import time

while True:
    #设定需要显示的背景图
    screen.blit(gackground,(x,y))
    #
    pygame.display.update()
    #降低cpu使用率
    time.sleep(0.01)

if __name__=="__main__":
    main()
```
5. 按键检测
```python
#检测事件
for event in pygame.event.get():
    #
    if event.type==QUIT:
        print('exit')
        exit()
    elif event.type==KEYDOWN:
        if event.key==K_a or event.key==K_LEFT:
            print('left')
        elif event.key==K_b or event.key== K_RIGHT:
            print('right')
        elif event.key==K_SPACE:
            print('space')

```
6. 面向对象

通过类生成一个对象，封装
```python
class HeroPlane(object):
    def __init__(self,screen):
        #设置飞机的默认位置
        self.x = 230
        self.y = 600
        #设置要显示内容的窗口
        self.screen =
        self.imageName = "./feiji/hero.gif"
        self.image = pygame.image.load(self.imageName).conver()
        #用于存储英雄飞机发射的所有子弹
        self.bullet = []

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        #
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

        #修改所有子弹的位置
        #for bullet in self.bulletList:
        #    bullet.x


    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.y += 10

    def sheBullet(self):
        newBullet = Bullet(self.x,self.y,self.screen)
        self.bulletList.append(newBullet)

#子弹类
class Bullet(boject):
    def __init__(self):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(self.imageName).conver()

    #
    def move(self)
        self.y -=2

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

        #判断子弹是否越界

        #存放需要删除的对象信息
        needDelItemList =[]

        for i in self.bulletList:
            if i.y<0:
                needDilItemList.append(i)

        for i in needDelItemList:


if __name__=="__main__":
    #1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,890),0,32)

    #2.创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png).conver()

    #3.创建一个飞机对象
    heroPlane = HeroPlane(screen)

    #4.创建一个敌人飞机
    enemyPlane = EnemyPlane(screen)

    #
    while True:
        #
        screen.blit(background,(0,0))
        #
        heroPlane.display()

        #检测事件
        for event in pygame.event.get():
            #
            if event.type==QUIT:
                print('exit')
                exit()
            elif event.type==KEYDOWN:
                if event.key==K_a or event.key==K_LEFT:
                    print('left')
                    heroPlane.moveLeft()
                elif event.key==K_b or event.key== K_RIGHT:
                    print('right')
                    herPlane.moveRight()
                elif event.key==K_SPACE:
                    print('space')
                    heroPlane.sheBullet()



```

#子弹任务
1. 实现飞机在你想要的位置显示
2. 实现按键控制飞机移动
3. 实现按下空格键的时候，显示一颗子弹

```python
#子弹类
class Bullet(boject):
    def __init__(self):
        self.x = 
        self.y = 
        self.image = pygame.image.load(self.imageName).conver()

```

## note2
#删除值
for i in range(6)
    bulletList.remove()

#显示敌机


#让敌机移动


方法调用，局部变量清除，加self.对象存在
