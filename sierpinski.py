
import pygame

# sets up the colors that will be used later
colors = [pygame.Color(0, 0, 0, 255),       # Black
          pygame.Color(255, 0, 0, 255),     # Red
          pygame.Color(0, 255, 0, 255),     # Green
          pygame.Color(0, 0, 255, 255),     # Blue
          pygame.Color(255, 255, 255, 255)]  # White


BLACK = 0
RED = 1
GREEN = 2
BLUE = 3
WHITE = -1



#drawing the initial triangle
def draw_triangle(p1, p2, p3, color, line_width, screen):
    pygame.draw.polygon(screen, colors[color], [p1, p2, p3], line_width)
    pygame.display.flip()
#finds midmpoint of a given side so that an new triangle can be drawn from that point
def find_midpoint(p1, p2):
    return((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(degree, p1, p2, p3, color, line_width, screen):
    draw_triangle(p1, p2, p3, BLUE, 1, screen)
    if degree > 0: #recursive call
        sierpinski(degree-1, p1, find_midpoint(p1, p2),
                   find_midpoint(p1, p3), WHITE, 1, screen)

        sierpinski(degree-1, p2, find_midpoint(p2, p3),
                   find_midpoint(p2, p1), WHITE, 1, screen)

        sierpinski(degree-1, p3, find_midpoint(p3, p2),
                   find_midpoint(p3, p1), WHITE, 1, screen)


def main():
    pygame.init()

    width = 640
    height = 640
    size = [width, height]

  
    p1 = [5, height - 5]
    p2 = [width / 2, 5]
    p3 = [width - 5, height - 5]
    initial_color = BLUE
    initial_line_width = 1  

    degree = 6 

    
    pygame.display.set_caption("Sierpinski Triangle")

    screen = pygame.display.set_mode(size)

    screen.fill(WHITE)

    sierpinski(degree, p1, p2, p3, initial_color, initial_line_width, screen)


    done = False
    count = 0
    while not done:
        count = count + 1
        if count % 1000000 == 0:
            print(".", end="")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    print("\nNow Quitting")
    pygame.quit()
    


if __name__ == "__main__":
    main()
