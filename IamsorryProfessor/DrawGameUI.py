import pygame
from pygame.locals import *
import Setting


class GetTextFromFile:
    def __init__(self, text_file): # file을 open 후 전달
        self.line = text_file.readlines() # line은 list
        self.line_list = self.divide_lines_to_list(self.line)
    
    def divide_lines_to_list(self, lines):
        line_list = [[0] * 8 for _ in range(8)] # 동적할당 하면 좋을텐데
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
    def __init__(self, image, position, width, height):
        self.image = image
        self.position = position
        self.width = width
        self.height = height

    def draw_image(self):
        Setting.windowSurface.blit(self.image, self.position)


class DrawMessageBox(DrawUI):
    def __init__(self, image, font, text, position, width, height):
        super().__init__(image, position, width, height)
        self.text = text
        self.font = font
        self.is_draw = False

    def draw_message(self):
        self.draw_image()
        draw_text = self.font.render(self.text, True, Setting.BLACK, Setting.GRAY)
        textRectObj = draw_text.get_rect()
        textRectObj.center = (self.position[0]+100, self.position[1]+80)
        Setting.windowSurface.blit(draw_text, textRectObj)
        