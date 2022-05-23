
def squart():
    for y in range(line_number):
        for x in range(column_number):
            enemy_sprite = pygame.sprite.Sprite()
            enemy_sprite.image = pygame.image.load('images/enemy.bmp')
            enemy_sprite.rect = enemy_sprite.image.get_rect()
            enemy_sprite.rect.x = enemy_width + 5 * enemy_width * x
            enemy_sprite.rect.y = enemy_height + 2 * enemy_width * y
            enemies.add(enemy_sprite)