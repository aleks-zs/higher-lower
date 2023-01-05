from art import logo, vs
from game_data import data
from user import User
import random
import os


class Game:
    def __init__(self):
        self.guess_counter = 0
        self.still_rolling = True
        self.right_guess_user = None

    def end_game(self):
        self.still_rolling = False
        print(logo)
        print('Sorry that is wrong. Final score: ' + str(self.guess_counter))

    def add_to_counter(self):
        self.guess_counter += 1

    def get_counter(self):
        return self.guess_counter

    def select_random_user_from_list(self, name=None):
        random_user = None

        if name is not None:
            user_not_found = True
            while user_not_found:
                random_user = random.choice(list(data))
                if random_user.get('name') != name:
                    user_not_found = False
        else:
            random_user = random.choice(list(data))

        user = User(random_user.get('name'),
                    random_user.get('follower_count'),
                    random_user.get('description'),
                    random_user.get('country'))
        return user

    def compare_users(self, user1, user2):
        print(f'Compare A: {user1.name}, a {user1.description}, from {user1.country}.')
        print(vs)
        print(f'Against B: {user2.name}, a {user2.description}, from {user2.country}.')

        user_choice = input("Who has more followers? Type 'A' or 'B' :")

        if user1.follower_count > user2.follower_count and user_choice == 'A':
            self.add_to_counter()
            self.right_guess_user = user1
        elif user2.follower_count > user1.follower_count and user_choice == 'B':
            self.add_to_counter()
            self.right_guess_user = user2
        else:
            self.end_game()

    def game_initial_step(self):
        print(logo)
        user1 = self.select_random_user_from_list()
        user2 = self.select_random_user_from_list(user1.name)
        self.compare_users(user1, user2)
        os.system('clear')

    def game_step(self):
        print(logo)
        print("You are right! Current score: " + str(self.get_counter()))
        user2 = self.select_random_user_from_list(self.right_guess_user.name)
        self.compare_users(self.right_guess_user, user2)
        os.system('clear')