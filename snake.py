import random

X = 0
Y = 1


class Snake(object):
    '''
    set up the direction of the snake
    '''
    DIR_UP = (0, -1)
    DIR_DOWN = (0, 1)
    DIR_LEFT = (-1, 0)
    DIR_RIGHT = (1, 0)

    '''
    features of the snake
    '''
    BODY_NONE = -1
    BODY_FOOD = 0
    BODY_HEAD = 1
    BODY_SNAKE = 2
    BODY_WALL = 3

    '''
    Life range of the snake
    '''
    SNAKE_WIN = 4
    SNAKE_LIFE = 5
    SNAKE_DIE = 6

    def __init__(self, s_len=5, s_width=40, s_height=20):  # (640/20 - 1, 480/20 -1)
        self.s_width = s_width
        self.s_height = s_height
        self.s_life = self.SNAKE_LIFE
        self._dir = self.DIR_RIGHT

        self.s_king = False

        self.s_list = []
        self.s_wall = []
        self._create_wall()
        self.s_map = self._map_create(self.BODY_NONE)

        

        # create a food, food = list[0]
        _s_food = self._create_body()
        self.s_list.append(_s_food)
        # creat a head, head = list[1]
        self._s_head = self._create_body()
        self.s_list.append(self._s_head)

        # create body and add body to list
        for _ in range(s_len-1):
            self._s_head = (self._s_head[0]-1, self._s_head[1])
            self.s_list.append(self._s_head)
        # print(self.s_list)

        self.s_score = 0  # len(self.s_list)

    '''
    Draw a map: map[x][y]
    '''
    def _map_create(self, val):
        s_map_x = []
        for _ in range(self.s_width):
            s_map_y = []
            for _ in range(self.s_height):
                s_map_y.append(val)
            s_map_x.append(s_map_y)
        return s_map_x

    '''
    Initialized the map
    '''
    def _map_init(self, map, val):
        for x in range(self.s_width):
            for y in range(self.s_height):
                map[x][y] = val

    '''
    check whether the points are on the board

    Parameters
    :param pnt: designated point
    '''
    def _check_pnt(self, pnt):
        x = pnt[0]
        y = pnt[1]
        if x < 0 and x >= self.s_width and y < 0 and y >= self.s_height:
            return False
        else:
            return True

    '''
    check whether this point is same with others
    
    Parameters
    :param body: designated points
    '''
    def _check_body(self, body):
        if len(self.s_list) != 0:
            for bd in self.s_list:
                #print(body, bd)
                if body == bd:
                    if body == self.s_list[0]:
                        return True, self.BODY_FOOD
                    elif body == self.s_list[1]:
                        return True, self.BODY_HEAD
                    else:
                        return True, self.BODY_SNAKE
        
        if len(self.s_wall) != 0:
            for bd in self.s_wall:
                #print(body, bd)
                if body == bd:
                    return True, self.BODY_WALL

        return False, self.BODY_NONE

    '''
    Create a random point
    '''
    def _create_body(self):
        # try all point
        for _ in range(self.s_width*self.s_height):
            body = self._random_xy(self.s_width - 1, self.s_height - 1)
            chkbd, _ = self._check_body(body)
            if chkbd == False:
                return body
        return None

    # def _get_dirlist(self):
    #     dir = []
    #     dir.append(self.DIR_UP)
    #     dir.append(self.DIR_RIGHT)
    #     dir.append(self.DIR_DOWN)
    #     dir.append(self.DIR_LEFT)

    '''
    Create a wall
    '''
    def _create_wall(self):
        dir_list = [self.DIR_UP, self.DIR_RIGHT, self.DIR_DOWN, self.DIR_LEFT]
        dir = random.randint(0, 3)  # direction of the wall

        # len = min(self.s_width, self.s_height)
        # len = random.randint(3, len)
        len = 5  # set the length of the wall to 5

        wall = self._create_body()  # set up the start point of the wall
        self.s_wall.append(wall)
        # print(wall, self.s_wall)

        for _ in range(len):  # draw other points according to the direction of the wall
            wall = self._add_xy(wall, dir_list[dir])
            # print(wall)
            if self._check_pnt(wall) != False:
                self.s_wall.append(wall)
                # print(self.s_wall)
            else:  # break the loop when reach the edge of the wall
                break
        # print(self.s_wall)

    '''
    Create random points

    Parameters
    :param startx: min of x-axis
    :param starty: min of y-axis
    :param endx: max of x-axis
    :param endy: max of y-axis
    '''
    def _random_xy(self, endx, endy, startx=0, starty=0):
        return [random.randint(startx, endx), random.randint(starty, endy)]

    '''
    add x and y of points 1&2

    Parameters
    :param t1: point 1
    :param t2: point 2
    '''
    def _add_xy(self, t1, t2):
        return [t1[0]+t2[0], (t1[1]+t2[1])]

    '''
    check the direction (cannot move to opposite direction)

    :param dir0: direction 1
    :param dir1: direction 2
    '''
    def _check_dir(self, dir0, dir1):
        if abs(dir0[0]) == abs(dir1[0]) and abs(dir0[1]) == abs(dir1[1]):
            return False
        else:
            return True

    '''
    Draw food and snakes (draw the map to the snakes)

    :param pen: window object
    '''
    def show(self, pen):
        pen.clear()
        self.draw()
        for x in range(self.s_width):
            for y in range(self.s_height):
                if self.s_map[x][y] != self.BODY_NONE:
                    if self.s_map[x][y] == self.BODY_FOOD:
                        pen.circle(x, y, pen.COLOR_BLUE)  # draw food
                    if self.s_map[x][y] == self.BODY_HEAD:
                        pen.rect(x, y, pen.COLOR_RED)  # draw head
                    if self.s_map[x][y] == self.BODY_SNAKE:
                        pen.rect(x, y, pen.COLOR_GREEN)  # draw snake
                    if self.s_map[x][y] == self.BODY_WALL:
                        pen.rect(x, y, pen.COLOR_BLACK)  # draw snake
        pen.update()

    '''
    Put food and snakes in the map
    '''
    def draw(self):
        x = 0
        y = 0
        self._map_init(self.s_map, self.BODY_NONE)
        if len(self.s_list) != 0:
            x = self.s_list[0][0]
            y = self.s_list[0][1]
            if x >= 0 and x < self.s_width and y >= 0 and y < self.s_height:
                self.s_map[x][y] = self.BODY_FOOD  # draw food

            x = self.s_list[1][0]
            y = self.s_list[1][1]
            if x >= 0 and x < self.s_width and y >= 0 and y < self.s_height:
                self.s_map[x][y] = self.BODY_HEAD  # draw head

            for s in range(2, len(self.s_list)):  # draw snake
                x = self.s_list[s][0]
                y = self.s_list[s][1]
                if x >= 0 and x < self.s_width and y >= 0 and y < self.s_height:
                    self.s_map[x][y] = self.BODY_SNAKE
        if len(self.s_wall) != 0:
            for w in self.s_wall:
                x = w[0]
                y = w[1]
                if x >= 0 and x < self.s_width and y >= 0 and y < self.s_height:
                    self.s_map[x][y] = self.BODY_WALL

    '''
    Move the snake

    :param dir: Direction of the snakes
    '''
    def move(self, dir=DIR_RIGHT):

        if self._check_dir(self._dir, dir):
            self._dir = dir

        head = self.s_list[1]  # save head
        last = self.s_list[-1]  # save tail
        # move the snake body forward(copy list[n-1] to list[n])
        for idx in range(len(self.s_list)-1, 1, -1):
            self.s_list[idx] = self.s_list[idx-1]

        head_t = self._add_xy(head, self._dir)  # new head

        # check snake head(cross wall)
        if head_t[0] < 0:
            head_t[0] = self.s_width - 1
        elif head_t[0] > self.s_width - 1:
            head_t[0] = 0

        if head_t[1] < 0:
            head_t[1] = self.s_height - 1
        elif head_t[1] > self.s_height - 1:
            head_t[1] = 0

        chk, bd = self._check_body(head_t)  # check the head
        # if bd != self.BODY_NONE:
        #    print(chk, bd)
        if chk == True and bd != self.BODY_NONE:
            if bd == self.BODY_HEAD or bd == self.BODY_SNAKE or bd == self.BODY_WALL:  # eat yourself or wall
                if self.s_king != True:  # Difficult Mode
                    self.s_life = self.SNAKE_DIE  # die
                    return self.s_life
            else:  # eat food
                self.s_list.append(last)  # body growth
                self.s_score = self.s_score + 1  # add score
                if self.s_score % 10 == 0:  # Add a wall evey 10 foods are eaten
                    self._create_wall()
                food = self._create_body()  # create food
                if food == None:  # no space to create food
                    self.s_life = self.SNAKE_WIN
                    return self.s_life
                self.s_list[0] = food

        self.s_list[1] = head_t  # update head

        if len(self.s_list) == ((self.s_width * self.s_height)):
            self.s_life = self.SNAKE_WIN
        return self.s_life

    def _is_safe(self):
        pass

    def _bfs_search(self):
        pass

    def auto_move(self):
        pass


if __name__ == "__main__":
    s = Snake()
    # s.move()
    # print(s.s_list)
    # print(s.s_list[-1])
    # for i in range(10, 1, -1):
    #     print(i)
    # for bd in range(len(s.s_list)):
    #     print(s.s_list[bd], bd)
    # head = s.s_list[2]
    # print(s._check_body(head))
    # print(s.s_map)
