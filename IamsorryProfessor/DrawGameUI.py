import pygame
from pygame.locals import *
import Setting
import ClassTemplate

class GetTextFromFile:
    def __init__(self, text_file): # file을 open 후 전달
        self.line = text_file.readlines() # line은 list
        self.line_list = self.divide_lines_to_list(self.line)
    
    def divide_lines_to_list(self, lines):
        line_list = [[0] * 9 for _ in range(9)] # 동적할당 하면 좋을텐데
        count_block = 0
        count_line = 0
        for line in lines:
            if line != '\n':
                line_list[count_block][count_line] = line
                count_line += 1
            else:
                count_block += 1
                count_line = 0
        return line_list


# file_name = open("ProfessorSaid.txt", 'r', encoding='UTF8')
# text_file = GetTextFromFile(file_name)
# for i in text_file.line_list:
#     print(i)


class DrawUI:
    def __init__(self, image, position, width, height, scale):
        # self.image = pygame.transform.scale(image, (image.get_width()*scale, image.get_height()* scale))
        self.image = image
        self.sheet = ClassTemplate.SpriteSheet(self.image)
        self.position = position
        self.width = width
        self.height = height
        self.scale = scale
        self.now_image = self.sheet.get_image(0, 0, self.image.get_width(), self.image.get_height(), scale, (0, 0, 0))

    def draw_image(self):
        Setting.windowSurface.blit(self.now_image, self.position)

    def draw_cut_image(self, new_width): # Health Bar
        self.now_image = self.sheet.get_image(0, 0, new_width, self.image.get_height(), self.scale, (0, 0, 0))


class DrawMessageBox(DrawUI):
    def __init__(self, image, font, text, position, width, height, scale):
        super().__init__(image, position, width, height, scale)
        self.text = text
        self.font = font
        self.is_draw = False

    def draw_message(self, text):
        self.draw_image()
        draw_text = self.font.render(str(text), True, Setting.WHITE)
        textRectObj = draw_text.get_rect()
        textRectObj = (self.position[0]+50, self.position[1]+50)
        Setting.windowSurface.blit(draw_text, textRectObj)
        
        