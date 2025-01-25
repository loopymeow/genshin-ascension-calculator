#imports
import pygame, sys, os, time
from pygame.locals import QUIT

pygame.init()

#window design
width, height = 450, 750
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("genshin ascension calculator")

def getFileValue(file, line):
  f = open(file, "r")
  all = f.readlines()
  all = all[line]
  all = all[0:(len(all) - 1)]
  f.close()
  return all

def changeFileValue(file, line, new):
  oldf = open(file, "r")
  all = oldf.readlines()
  all[line] = str(new) + "\n"
  oldf.close()
  newf = open(file, "w")
  newf.writelines(all)
  newf.close()

def loadValues():
  one = int(getFileValue("save.txt", 0))
  two = int(getFileValue("save.txt", 1))
  three = int(getFileValue("save.txt", 2))
  four = int(getFileValue("save.txt", 3))
  five = int(getFileValue("save.txt", 4))
  aimType = str((getFileValue("save.txt", 5)))
  aimAmount = int(getFileValue("save.txt", 6))
  return one, two, three, four, five, aimType, aimAmount

def saveValues(one, two, three, four, five, aimType, aimAmount):
  changeFileValue("save.txt", 0, one)
  changeFileValue("save.txt", 1, two)
  changeFileValue("save.txt", 2, three)
  changeFileValue("save.txt", 3, four)
  changeFileValue("save.txt", 4, five)
  changeFileValue("save.txt", 5, aimType)
  changeFileValue("save.txt", 6, aimAmount)

def clearSave():
  changeFileValue("save.txt", 0, 0)
  changeFileValue("save.txt", 1, 0)
  changeFileValue("save.txt", 2, 0)
  changeFileValue("save.txt", 3, 0)
  changeFileValue("save.txt", 4, 0)
  changeFileValue("save.txt", 5, "one")
  changeFileValue("save.txt", 6, 0)

class images():
  def __init__(self):
    #backgrounds
    self.red_bg = pygame.image.load(os.path.join("images/red_bg.png"))
    self.red_bg = pygame.transform.scale(self.red_bg, (width, height))
    self.green_bg = pygame.image.load(os.path.join("images/green_bg.png"))
    self.green_bg = pygame.transform.scale(self.green_bg, (width, height))
    #banner
    self.banner = pygame.image.load(os.path.join("images/banner.png"))
    self.banner = pygame.transform.scale(self.banner, (96, 94))
    #numbers
    self.num0 = pygame.image.load(os.path.join("images/numbers/0.png"))
    self.num1 = pygame.image.load(os.path.join("images/numbers/1.png"))
    self.num2 = pygame.image.load(os.path.join("images/numbers/2.png"))
    self.num3 = pygame.image.load(os.path.join("images/numbers/3.png"))
    self.num4 = pygame.image.load(os.path.join("images/numbers/4.png"))
    self.num5 = pygame.image.load(os.path.join("images/numbers/5.png"))
    self.num6 = pygame.image.load(os.path.join("images/numbers/6.png"))
    self.num7 = pygame.image.load(os.path.join("images/numbers/7.png"))
    self.num8 = pygame.image.load(os.path.join("images/numbers/8.png"))
    self.num9 = pygame.image.load(os.path.join("images/numbers/9.png"))
    ### small
    
    self.numS0 = pygame.transform.scale(self.num0, (20, 30))
    self.numS1 = pygame.transform.scale(self.num1, (20, 30))
    self.numS2 = pygame.transform.scale(self.num2, (20, 30))
    self.numS3 = pygame.transform.scale(self.num3, (20, 30))
    self.numS4 = pygame.transform.scale(self.num4, (20, 30))
    self.numS5 = pygame.transform.scale(self.num5, (20, 30))
    self.numS6 = pygame.transform.scale(self.num6, (20, 30))
    self.numS7 = pygame.transform.scale(self.num7, (20, 30))
    self.numS8 = pygame.transform.scale(self.num8, (20, 30))
    self.numS9 = pygame.transform.scale(self.num9, (20, 30))
    ### big
    self.numB0 = pygame.transform.scale(self.num0, (41, 60))
    self.numB1 = pygame.transform.scale(self.num1, (41, 60))
    self.numB2 = pygame.transform.scale(self.num2, (41, 60))
    self.numB3 = pygame.transform.scale(self.num3, (41, 60))
    self.numB4 = pygame.transform.scale(self.num4, (41, 60))
    self.numB5 = pygame.transform.scale(self.num5, (41, 60))
    self.numB6 = pygame.transform.scale(self.num6, (41, 60))
    self.numB7 = pygame.transform.scale(self.num7, (41, 60))
    self.numB8 = pygame.transform.scale(self.num8, (41, 60))
    self.numB9 = pygame.transform.scale(self.num9, (41, 60))

  def background(self, background):
    if background == "red":
      win.blit(self.red_bg, (0, 0))
    if background == "green":
      win.blit(self.green_bg, (0, 0))

  def draw_numbers(self):
    #big numbers
    data = []
    for line in range(0,5):
      temp = getFileValue("save.txt", line,)
      data.append(temp)
    for i in range(0,5):
      value = data[i]
      length = int(len(value))

      charCount=0
      for char in value:
        placement = (345 + (charCount*41) - (length*20) ,210+ i*104.5)
        if char == "0":
          win.blit(self.numB0, placement)
        if char == "1":
          win.blit(self.numB1, placement)
        if char == "2":
          win.blit(self.numB2, placement)
        if char == "3":
          win.blit(self.numB3, placement)
        if char == "4":
          win.blit(self.numB4, placement)
        if char == "5":
          win.blit(self.numB5, placement)
        if char == "6":
          win.blit(self.numB6, placement)
        if char == "7":
          win.blit(self.numB7, placement)
        if char == "8":
          win.blit(self.numB8, placement)
        if char == "9":
          win.blit(self.numB9, placement)
        charCount=charCount+1

      #small numbers
      temp = getFileValue("save.txt", 6,)
      value = temp
      length = int(len(value))

      charCount=0
      for char in value:
        placement = (270 + (charCount*20) - (length*10) ,157)
        if char == "0":
          win.blit(self.numS0, placement)
        if char == "1":
          win.blit(self.numS1, placement)
        if char == "2":
          win.blit(self.numS2, placement)
        if char == "3":
          win.blit(self.numS3, placement)
        if char == "4":
          win.blit(self.numS4, placement)
        if char == "5":
          win.blit(self.numS5, placement)
        if char == "6":
          win.blit(self.numS6, placement)
        if char == "7":
          win.blit(self.numS7, placement)
        if char == "8":
          win.blit(self.numS8, placement)
        if char == "9":
          win.blit(self.numS9, placement)
        charCount=charCount+1
    
  def draw_banner(self):
    temp = getFileValue("save.txt", 5)
    if temp == "one":
      win.blit(self.banner, (85, 193))
    if temp == "two":
      win.blit(self.banner, (85, 298))
    if temp == "three":
      win.blit(self.banner, (86, 402))
    if temp == "four":
      win.blit(self.banner, (87, 507))
    if temp == "five":
      win.blit(self.banner, (86, 612))
      

      
def draw_window(background):

  images.background(background)
  images.draw_numbers()
  images.draw_banner()

def convertInt(one, two, three, four, five, aimAmount):
  one = int(one)
  two = int(two)
  three = int(three)
  four = int(four)
  five = int(five)
  aimAmount = int(aimAmount)
  return one, two, three, four, five, aimAmount

def calculateNeed(one, two, three, four, five, aimType, aimAmount):
  one, two, three, four, five, aimAmount = convertInt(one, two, three, four, five, aimAmount)
  need = 0
  if aimType == "one":
    need = aimAmount - one
  if aimType == "two":
    need = one // 3
    need = aimAmount - two - need
  if aimType == "three":
    need = one // 3
    need = ((need + two) // 3)
    need = ((need + three) // 3)
    need = aimAmount - three - need
  if aimType == "four":
    need = one // 3
    need = ((need + two) // 3)
    need = ((need + three) // 3)
    need = aimAmount - four - need
  if aimType == "five":
    need = one // 3
    need = ((need + two) // 3)
    need = ((need + three) // 3)
    need = ((need + four) // 3)
    need = aimAmount - five - need
  if need < 1:
    return ("green")
  else:
    return ("red")

def get_input():
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      xpos = pos[0]
      ypos = pos[1]
      if 16.8<xpos<129 and 13.2<ypos<48: #reset button
        clearSave()
      if 344<xpos<380 and 152<ypos<188: #aimminus
        temp = int(getFileValue("save.txt", 6))
        if temp!=0:
          changeFileValue("save.txt", 6, temp-1)
      if 392<xpos<430 and 149<ypos<187: #aimplus
        temp = int(getFileValue("save.txt", 6))
        if temp!=999:
          changeFileValue("save.txt", 6, temp+1)

      #FIRST LAYER
      if 18<xpos<71 and 215<ypos<261: #minus1
        temp = int(getFileValue("save.txt", 0))
        if temp!=0:
          changeFileValue("save.txt", 0, temp-1)
      if 91<xpos<174 and 197<ypos<278: #aim1
        changeFileValue("save.txt", 5, "one")
      if 193<xpos<246 and 21<ypos<262: #plus1
        temp = int(getFileValue("save.txt", 0))
        if temp!=999:
          changeFileValue("save.txt", 0, temp+1)

      #SECOND LAYER
      if 20<xpos<71 and 316<ypos<368: #minus2
        temp = int(getFileValue("save.txt", 1))
        if temp!=0:
          changeFileValue("save.txt", 1, temp-1)
      if 90<xpos<176 and 304<ypos<384: #aim2
        changeFileValue("save.txt", 5, "two")
      if 193<xpos<248 and 317<ypos<366: #plus2
        temp = int(getFileValue("save.txt", 1))
        if temp!=999:
          changeFileValue("save.txt", 1, temp+1)
          
      #THIRD LAYER
      if 19<xpos<74 and 421<ypos<470: #minus3
        temp = int(getFileValue("save.txt", 2))
        if temp!=0:
          changeFileValue("save.txt", 2, temp-1)
      if 93<xpos<176 and 407<ypos<486: #aim3
        changeFileValue("save.txt", 5, "three")
      if 194<xpos<246 and 422<ypos<470: #plus3
        temp = int(getFileValue("save.txt", 2))
        if temp!=999:
          changeFileValue("save.txt", 2, temp+1)
          
      #FOURTH LAYER
      if 20<xpos<73 and 527<ypos<576: #minus4
        temp = int(getFileValue("save.txt", 3))
        if temp!=0:
          changeFileValue("save.txt", 3, temp-1)
      if 92<xpos<179 and 512<ypos<590: #aim4
        changeFileValue("save.txt", 5, "four")
      if 194<xpos<244 and 527<ypos<572: #plus4
        temp = int(getFileValue("save.txt", 3))
        if temp!=999:
          changeFileValue("save.txt", 3, temp+1)
          
      #FIFTH LAYER
      if 20<xpos<72 and 631<ypos<682: #minus5
        temp = int(getFileValue("save.txt", 4))
        if temp!=0:
          changeFileValue("save.txt", 4, temp-1)
      if 91<xpos<176 and 617<ypos<697: #aim5
        changeFileValue("save.txt", 5, "five")
      if 192<xpos<245 and 632<ypos<681: #plus5
        temp = int(getFileValue("save.txt", 4))
        if temp!=999:
          changeFileValue("save.txt", 4, temp+1)
          
          

def main(run, one, two, three, four, five, aimType, aimAmount):
  while run == True:
    one, two, three, four, five, aimType, aimAmount = loadValues()
    background = calculateNeed(one, two, three, four, five, aimType, aimAmount)
    draw_window(background)
    get_input()
    
    pygame.display.update()
    clock.tick(int(60))

#initialising starter variables and classes
run = True
images = images()
clock = pygame.time.Clock()
one, two, three, four, five, aimType, aimAmount = loadValues()

main(run, one, two, three, four, five, aimType, aimAmount)
