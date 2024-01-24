"""
    A pygame program that replicates the motion inputs found in Fighting Games such as Street Fighter, Guilty Gear, KOF,
    etc.
    As of writing, I plan to support:
        - Basic Shoto Inputs(QCF, QCB, DP)

    In the future I'd like to add some more inputs, such as some specific 3D fighter moves (EWGF, Mist Step, etc.),
    and more complex or lesser seen inputs (SPD, HCF/B, tiger knee, and whatever that pretzel input is.)

    There will be a visuals on screen with a sprite featuring an appropriate character, with a sprite ripped from the game.
    They will perform the move on successful inputs.

    Lachlan Paul, 2023
"""

import pygame

# Dictionaries containing all the moves for specific characters
ryu = {
    # Basic shoto moves
    "QCF": [2, 3, 6],
    "QCB": [2, 1, 4],
    "DP": [6, 2, 3],

    # Super Moves
    "QCFx2": [2, 3, 6, 2, 3, 6],
    "QCBx2": [2, 1, 4, 2, 1, 4]
}

zangief = {
    # Basic grappler moves (half and full circles)
    "360": [6, 3, 2, 1, 4, 7, 8, 9],  # Have fun doing this on a keyboard. I'm so glad I main Gief on a joystick.
    "720": [6, 3, 2, 1, 4, 7, 8, 9, 6, 3, 2, 1, 4, 7, 8, 9]  # MY LOYAL FANS! WITTNESS MY FULL MIGHT! NO MERCY, NO REMORSE! DOOOORYIA!
}

kazuya = {
    # Basic Mishima moves
    "EWGF": [6, 5, 2, 3]
}

selected_character = ryu  # Ryu by default


def check_for_input(character, input_history):
    """Checks input history to see if it's equal to a move"""
    for move, notation in character.items():
        if notation == input_history:
            return move
    return None


def main():
    pygame.init()

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Motion Inputs")

    screen.fill((120, 120, 120))
    pygame.display.flip()

    game_running = True

    clock = pygame.time.Clock()
    frames_without_combo = 0
    input_history = []

    up_pressed = False
    left_pressed = False
    right_pressed = False
    down_pressed = False


    while game_running:
        clock.tick(60)
        frames_without_combo += 1

        if frames_without_combo >= 60:
            frames_without_combo = 0
            input_history = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    up_pressed = True
                if event.key == pygame.K_LEFT:
                    left_pressed = True
                if event.key == pygame.K_RIGHT:
                    right_pressed = True
                if event.key == pygame.K_DOWN:
                    down_pressed = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    up_pressed = False
                if event.key == pygame.K_LEFT:
                    left_pressed = False
                if event.key == pygame.K_RIGHT:
                    right_pressed = False
                if event.key == pygame.K_DOWN:
                    down_pressed = False

            # Adds inputs to input_history
            if left_pressed and up_pressed:
                input_history.append(7)
            if right_pressed and up_pressed:
                input_history.append(9)
            if left_pressed and down_pressed:
                input_history.append(1)
            if right_pressed and down_pressed:
                input_history.append(3)
            elif up_pressed:
                input_history.append(8)
            elif left_pressed:
                input_history.append(4)
            elif right_pressed:
                input_history.append(6)
            elif down_pressed:
                input_history.append(2)
            elif selected_character == kazuya:
                input_history.append(5)

            print(input_history)

            move_inputted = check_for_input(ryu, input_history)
            if move_inputted:
                print(move_inputted)

    pygame.quit()


if __name__ == '__main__':
    main()
