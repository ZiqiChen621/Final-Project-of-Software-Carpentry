import window
import snake
import time
import threading


def game_init():
    width, height = 40, 20
    _window = window.GameWindow(gw_tittle="Snake", gw_width=width, gw_height=height)
    _snake = snake.Snake(s_len=5, s_width=width, s_height=height)
    return _snake, _window


def game_run(snake):
    global dir
    global stop
    global speed
    delay = 1.5
    while True:
        if stop != True:
            life = snake.move(dir)
            if life != snake.SNAKE_LIFE:
                break  # die, exit
        snake.show(window)
        delay = 1 - speed * 0.05
        if delay < 0.05:
            delay = 0.05
        time.sleep(delay)


dir = snake.Snake.DIR_RIGHT
stop = False
speed = 0
score = 0
if __name__ == "__main__":
    snake, window = game_init()
    gt = threading.Thread(target=game_run, args=(snake,))
    gt.start()
    while True:
        event = window.event()
        if event != window.EVENT_NONE:
            if event == window.EVENT_QUIT:
                window.quit()
            elif event == window.EVENT_KUP or \
                    event == window.EVENT_KDOWN or \
                    event == window.EVENT_KLEFT or \
                    event == window.EVENT_KRIGHT:
                dir = event
            elif event == window.EVENT_STOP:
                if stop == False:
                    stop = True
                else:
                    stop = False
                #print(dir, snake.s_life)
            elif event == window.EVENT_ADD:
                speed = speed + 1
            elif event == window.EVENT_SUB:
                speed = speed - 1
            elif event == window.EVENT_KING:
                if snake.s_king == True:
                    snake.s_king = False
                else:
                    snake.s_king = True
        if snake.s_life != snake.SNAKE_LIFE:
            window.quit()
        if score != snake.s_score:
            score = snake.s_score
            if(score % 10 == 0):
                speed = speed + 1
