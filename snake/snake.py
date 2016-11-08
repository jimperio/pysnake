import pygame
from random import randint


size = width, height = 200, 200
cell_width = 10
cell_height = 10
num_rows = width / cell_width
num_cols = height / cell_height

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 200, 0

dirs = {
  123: (0, -1),
  124: (0, 1),
  125: (1, 0),
  126: (-1, 0),
}

def next_head(head, direction):
  y, x = head
  dy, dx = direction
  return (y + dy) % num_rows, (x + dx) % num_cols

def random_food_pos():
  return randint(0, num_rows - 1), randint(0, num_cols - 1)

def main():
  pygame.init()
  screen = pygame.display.set_mode(size)
  clock = pygame.time.Clock()

  done = False
  curr_direction = (0, 1)
  food_pos = None
  curr_speed = 10

  mid_y = num_rows / 2
  mid_x = num_cols / 2
  segments = [(mid_y, x) for x in range(mid_x, mid_x+4)]

  while not done:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        direction = dirs.get(event.scancode, None)
        if direction is not None:
          # TODO: Prevent reversing direction.
          curr_direction = direction
      elif event.type == pygame.QUIT:
        done = True

    curr_head = segments[-1]
    head = next_head(curr_head, curr_direction)
    if head in segments:
      # TODO: Display game over.
      break
    segments.append(head)
    if head == food_pos:
      food_pos = None
      curr_speed += 1
    else:
      segments.pop(0)

    while food_pos is None or food_pos in segments:
      food_pos = random_food_pos()

    screen.fill(green)
    for i, (y, x) in enumerate(segments):
      pygame.draw.rect(screen, white, [cell_width * x, cell_height * y, cell_width, cell_height])

    food_y, food_x = food_pos
    pygame.draw.rect(screen, red, [cell_width * food_x, cell_height * food_y, cell_width, cell_height])
    pygame.display.flip()

    clock.tick(curr_speed)

  pygame.quit()


if __name__ == "__main__":
  main()
