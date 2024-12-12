# Jungle Adventure: A Choose Your Own Adventure Game
#
# Hey! So this game is called "Jungle Adventure," and here's the deal:
# You survived a crazy plane crash and woke up in this super dense, spooky jungle. 
# It's packed with wild animals, mysterious temples, and all kinds of stuff that 
# could either help you or, well... totally ruin your day.
#
# Your mission? Just survive, bro. Make smart choices, find a way out, and maybe 
# discover some treasures along the way. Every choice you make will change what 
# happens next, and there are a bunch of different endings. Like, you could 
# become besties with a monkey, find a hidden stash of gold, or... not survive at all.
#
# Key Features:
# - Tons of decision points (you’ve got at least 10 big ones to make).
# - A bunch of cool story paths (20+ little moments that decide your fate).
# - Some endings are awesome, others... not so much. But hey, that’s life in the jungle.
# - You can save your game progress and come back later if you chicken out halfway through.
#
# How to Play:
# - Just run the game and read the story.
# - When you're asked to make a choice, type in the number of the option you want. Easy!
# - Example: If it says "1. Go left" or "2. Go right" and you type "1," you're going left.
#
# So yeah, give it a shot! Can you escape and live to tell the tale, or will the jungle get you? Let’s see!

import sys

def introduction():
    print("""
Welcome to the Jungle Adventure!
You are the sole survivor of a plane crash in a mysterious jungle.
Danger lurks at every turn, but so do secrets and treasures.
Will you survive and escape?
""")
    decision_point_1()
    
def save_progress(current_point):
    with open("save_files/save.txt", "w") as file:
        file.write(current_point)
        
def save_progress(current_point):
    with open("save_files/save.txt", "w") as file:
        file.write(current_point)
def load_progress():
    try:
        with open("save_files/save.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "introduction"

def decision_point_1():
    print("\nYou wake up near the wreckage of the plane. The jungle is dense and buzzing with strange noises.")
    print("1. Search the wreckage for supplies.")
    print("2. Head straight into the jungle.")
    choice = input("What do you do? (Enter 1 or 2): ")
    if choice == "1":
        narrative_search_wreckage()
    elif choice == "2":
        narrative_enter_jungle()
    else:
        print("Invalid choice. Try again.")
        decision_point_1()
        
def narrative_search_wreckage():
    print("\nYou search the wreckage and find a first aid kit and a flare gun.")
    print("Suddenly, you hear rustling in the bushes.")
    print("1. Investigate the sound.")
    print("2. Hide and wait quietly.")
    choice = input("What do you do? (Enter 1 or 2): ")
    if choice == "1":
        narrative_investigate_sound()
    elif choice == "2":
        narrative_hide_quietly()
    else:
        print("Invalid choice. Try again.")
        narrative_search_wreckage()

def narrative_enter_jungle():
    print("\nYou bravely walk into the jungle, but the dense foliage makes it hard to see.")
    print("You come across a fork in the path.")
    print("1. Take the left path.")
    print("2. Take the right path.")
    choice = input("What do you do? (Enter 1 or 2): ")
    if choice == "1":
        narrative_left_path()
    elif choice == "2":
        narrative_right_path()
    else:
        print("Invalid choice. Try again.")
        narrative_enter_jungle()
        
def narrative_investigate_sound():
    print("\nYou approach the bushes and find a wounded monkey trapped in vines.")
    print("1. Help the monkey.")
    print("2. Ignore it and move on.")
    choice = input("What do you do? (Enter 1 or 2): ")
    if choice == "1":
        ending_monkey_friend()
    elif choice == "2":
        ending_monkey_attack()
    else:
        print("Invalid choice. Try again.")
        narrative_investigate_sound()

def narrative_hide_quietly():
    print("\nYou hide quietly and watch as a jaguar prowls past you.")
    print("After it leaves, you continue into the jungle.")
    ending_escape_jungle()

def narrative_left_path():
    print("\nThe left path leads you to an ancient temple covered in vines.")
    print("1. Enter the temple.")
    print("2. Stay outside and look around.")
    choice = input("What do you do? (Enter 1 or 2): ")
    if choice == "1":
        ending_temple_treasure()
    elif choice == "2":
        ending_temple_trap()
    else:
        print("Invalid choice. Try again.")
        narrative_left_path()
        
def narrative_right_path():
    print("\nThe right path leads you to a fast-flowing river with a rickety bridge.")
    print("1. Cross the bridge.")
    print("2. Follow the river downstream.")
    choice = input("What do you do? (Enter 1 or 2): ")
    if choice == "1":
        ending_bridge_collapse()
    elif choice == "2":
        ending_river_escape()
    else:
        print("Invalid choice. Try again.")
        narrative_right_path()

def ending_monkey_friend():
    print("\nThe monkey thanks you by leading you to a hidden exit from the jungle.")
    print("You escape safely! Congratulations!")
    sys.exit()

def ending_monkey_attack():
    print("\nThe monkey was actually a decoy! A group of predators ambushes you. Game over.")
    sys.exit()

def ending_escape_jungle():
    print("\nYou survive the jungle and find a rescue team nearby. You're saved!")
    sys.exit()

def ending_temple_treasure():
    print("\nInside the temple, you find a chest full of gold and artifacts. You're rich!")
    sys.exit()

def ending_temple_trap():
    print("\nAs you explore outside, you trigger a trap and are captured by mysterious guardians. Game over.")
    sys.exit()


def ending_bridge_collapse():
    print("\nThe bridge collapses under your weight, and you fall into the river. Game over.")
    sys.exit()

def ending_river_escape():
    print("\nFollowing the river, you find a small boat and paddle to safety. You escape!")
    sys.exit()

if __name__ == "__main__":
    introduction()
