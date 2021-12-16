import sys
import time
import pygame



class GameWindow(object):
    '''
    Define Color
    '''
    COLOR_RED = (255, 0, 0)
    COLOR_GREEN = (0, 255, 0)
    COLOR_BLUE = (0, 0, 255)
    COLOR_BLACK = (0, 0, 0)
    COLOR_WHITE = (255, 255, 255)
    COLOR_GRAY = (160, 160, 160)

    '''
    Define Event
    '''
    EVENT_KUP = (0, -1)
    EVENT_KDOWN = (0, 1)
    EVENT_KLEFT = (-1, 0)
    EVENT_KRIGHT = (1, 0)
    EVENT_QUIT = (2, 0)
    EVENT_STOP = (2, 1)
    EVENT_ADD = (2, 2)
    EVENT_SUB = (2, 3)
    EVENT_KING = (2, 4)
    EVENT_NONE = (0, 0)

    def __init__(self, gw_tittle="GameWindow", gw_width=40, gw_height=20, gw_bgcol=COLOR_WHITE, pnt_size=20,  pnt_col=COLOR_RED):
        self.gw_width = gw_width*pnt_size
        self.gw_height = gw_height*pnt_size
        self.gw_bgcol = gw_bgcol
        self.pnt_size = pnt_size
        self.pnt_col = pnt_col
        pygame.init()
        self._game_window = pygame.display.set_mode(
            (self.gw_width, self.gw_height))
        pygame.display.set_caption(gw_tittle)

    '''
    Color 1 delete color 2

    Parameters
    :param c1: color 1
    :param c2: color 2
    '''

    def _color_sub(self, c1, c2):
        return((c1[0]-c2[0]), (c1[1]-c2[1]), (c1[2]-c2[2]))

    '''
    Fill the screen with background color
    '''

    def clear(self):
        color = self._color_sub(self.COLOR_WHITE, self.gw_bgcol)
        self._game_window.fill(self.gw_bgcol)
        for x in range(self.maxx()+1):
            pygame.draw.line(self._game_window, color, (x*self.pnt_size, 0), (x*self.pnt_size, self.gw_height), 1)
        for y in range(self.maxy()+1):
            pygame.draw.line(self._game_window, color, (0, y * self.pnt_size), (self.gw_width, y*self.pnt_size), 1)

    '''
    The maximum of x-axis
    '''

    def maxx(self):
        return(self.gw_width//self.pnt_size - 1)

    '''
    The maximum of y-axis
    '''

    def maxy(self):
        return(self.gw_height//self.pnt_size - 1)

    '''
    refresh the screen
    '''

    def update(self):
        pygame.display.update()

    '''
    draw a square at the signed point on the screen
    
    Parameters
    :param x: x-axis number of left-up corner of square
    :param y: y-axis number of left-up corner of square
    :param color: color filled in the square
    '''

    def _rect(self, x, y, *color):
        pntcol = self.pnt_col
        if len(color) != 0:
            pntcol = color[0]
        pos = (x, y, self.pnt_size, self.pnt_size)
        pygame.draw.rect(self._game_window, pntcol, pos, 0)

    '''
    draw a circle at the signed point on the screen
    the circle is in a outer square
    
    Parameters
    :param x1: x-axis number of left-up corner of outer square
    :param y1: y-axis number of left-up corner of outer square
    :param x2: x-axis number of right-down corner of outer square
    :param y2: y-axis number of right-down corner of outer square
    :param color: color filled in the circle 
    '''

    def _circle(self, x1, y1, x2, y2, *color):
        pntcol = self.pnt_col
        if len(color) != 0:
            pntcol = color[0]

        r1 = abs(x2-x1)//2
        r2 = abs(y2-y1)//2
        r = min(r1, r2)
        x = min(x1, x2) + r
        y = min(y1, y2) + r
        pygame.draw.circle(self._game_window, pntcol, (x, y), r, 0)

    '''
    draw a square at the signed point on the screen
    
    Parameters
    :param x: x-axis number of left-up corner of square
    :param y: y-axis number of left-up corner of square
    :param color: color filled in the square
    '''

    def rect(self, x, y, *color):
        pntcol = self.pnt_col
        if len(color) != 0:
            pntcol = color[0]
        if x < 0 or x > self.maxx() or y < 0 or y > self.maxy():
            return
        self._rect(x*self.pnt_size, y*self.pnt_size, pntcol)

    '''
    draw a circle at the signed point on the screen
    the circle is in a outer square
    
    Parameters
    :param x: x-axis number of left-up corner of outer square
    :param y: y-axis number of left-up corner of outer square
    :param color: color filled in the circle
    '''

    def circle(self, x, y, *color):
        pntcol = self.pnt_col
        if len(color) != 0:
            pntcol = color[0]
        if x < 0 or x > self.maxx() or y < 0 or y > self.maxy():
            return
        x = x*self.pnt_size
        y = y*self.pnt_size
        self._circle(x, y, x+self.pnt_size, y+self.pnt_size, pntcol)

    '''
    define events
    '''

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return self.EVENT_QUIT
            elif event.type == pygame.KEYDOWN:  # KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    return self.EVENT_KLEFT
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    return self.EVENT_KRIGHT
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    return self.EVENT_KUP
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    return self.EVENT_KDOWN
                elif event.key == pygame.K_SPACE:
                    return self.EVENT_STOP
                elif event.key == pygame.K_F1:
                    return self.EVENT_ADD
                elif event.key == pygame.K_F2:
                    return self.EVENT_SUB
                elif event.key == pygame.K_ESCAPE:
                    return self.EVENT_QUIT
                elif event.key == pygame.K_F3:
                    return self.EVENT_KING
        return self.EVENT_NONE

    '''
    Define Quit
    '''

    def quit(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    # game window test
    game = GameWindow("Snake")
    x = 0
    y = 0
    dx = 1
    dy = 1

    # print(game.DIR_DOWN == game.DIR_UP)
    # print(game.DIR_DOWN != game.DIR_UP)

    # for _ in range(200):
    while True:
        event = game.event()
        if event != game.EVENT_NONE:
            if event == game.EVENT_QUIT:
                game.quit()
            else:
                print(event)
        x += dx
        y += dy

        game.clear()
        game.circle(x, y)
        game.update()
        time.sleep(0.1)

        if x >= game.maxx() or x <= 0:
            dx = -dx
        if y >= game.maxy() or y <= 0:
            dy = -dy
