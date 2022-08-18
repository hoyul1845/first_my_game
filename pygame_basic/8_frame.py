import pygame
import os
pygame.init() # 초기화 (반드시 필요)
 
 
 #화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
 
 
# FPS
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
 
 
 
 
 
  
  # 화면 타이틀 설정
pygame.display.set_caption("Nado Pang")
image_path = os.path.join(current_path, "images") 
# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))


  
# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60)
    
     
     
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False 
         
    pygame.display.update() # 게임화면을 다시 그리기!
    
    
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255,))
    screen.blit(timer, (10,10))
    

# pygame 종료
pygame.quit()


 