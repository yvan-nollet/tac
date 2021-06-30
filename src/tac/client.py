import pygame

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0


class Player:
    """Player."""

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.val = 3

    def draw(self, win):
        """Draw the rectangle representing the player."""
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.val
        elif keys[pygame.K_RIGHT]:
            self.x += self.val
        elif keys[pygame.K_UP]:
            self.y -= self.val
        elif keys[pygame.K_DOWN]:
            self.y += self.val

        self.rect = (self.x, self.y, self.width, self.height)


def redraw_window(win, player: Player) -> None:
    """Redraw the window."""

    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()


p = Player(50, 50, 100, 100, (0, 255, 0))


def main():
    """Main loop."""
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redraw_window(win, p)


main()
