"""
Alfrey Chan
A01344049
"""
from board.board import make_board, describe_current_location, get_user_choice, validate_move
from board.board import move_character, check_if_goal_attained
from board.enemy_spawn import check_for_enemies
from combat.combat import battle
from character.create_character import create_character, update_xp


def game():
    board = make_board()
    character = create_character()
    achieved_goal = False
    print(describe_current_location(board, character))
    while not achieved_goal:
        direction = get_user_choice()
        valid_move = validate_move(character, direction)
        if valid_move:
            move_character(character, direction)
            character['radiation'] += 2
            print(describe_current_location(board, character))
            enemy_spawned = check_for_enemies(character)

            if enemy_spawned:
                print(f"A wild {enemy_spawned[0]} appeared!\n")
                battle(character, enemy_spawned)
                if character['HP'] == 0:
                    return print(f"You've been slayed by the mighty {enemy_spawned[0]}")
                update_xp(character, enemy_spawned[1]['XP'])
        else:
            print("This direction is blocked by rubble and debris, you'll need to find another way around.")

        if character['HP'] == 0:
            return print("You've fallen victim to the wasteland...\nGAME OVER")
        if character['radiation'] >= 100:
            return print("You've died from radiation poisoning...\nGAME OVER")
        achieved_goal = check_if_goal_attained(board, character)


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
