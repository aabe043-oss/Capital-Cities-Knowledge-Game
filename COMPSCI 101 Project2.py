
# COMPSCI 101 Project

"""
World Capitals Quiz Game
Author: Aritha Abeyawardana (Username: aabe043)

"""


import random


def main():
    input_filename = "WorldCapitals.txt"
    output_filename = "HighScores.txt"
    username = "aabe043"

    
    print_banner(username)

    
    world_capitals_dict = get_world_capitals_dictionary(input_filename)

    
    total_score = run_quiz(world_capitals_dict)

    
    handle_high_scores(output_filename, username, total_score)


def print_banner(username):
    title = f"World Capitals Quiz For {username.upper()}"
    border = "#" * (len(title) + 4)
    print(border)
    print(f"#  {title}  #")
    print(border)
    print()


def get_world_capitals_dictionary(filename):
    country_capital_dict = {}
    input_file = open(filename, "r")
    lines = input_file.readlines()

    for line in lines:
        line = line.strip()
        components = line.split(":")
        if len(components) == 2:
            country = components[0].strip()
            capital = components[1].strip()
            country_capital_dict[country] = capital

    input_file.close()
    return country_capital_dict


def get_player_answer(target_country, cities):
    print(f"Choices available: {cities}\n")
    city = input(f"What is the capital city of {target_country}? ")

    while city not in cities:
        print("You must choose from the city choices available!")
        city = input(f"What is the capital city of {target_country}? ")

    cities.remove(city)
    return city


def run_round(world_capitals_dict, countries_tested):
    target_country, capital_cities = get_question_data(world_capitals_dict,
                                                       countries_tested)
    correct_answer = world_capitals_dict[target_country]
    attempts = 0
    max_attempts = 3
    is_correct = False
    score = 0

    while attempts < max_attempts and not is_correct:
        player_answer = get_player_answer(target_country, capital_cities)
        attempts += 1

        if player_answer == correct_answer:
            print("Your answer is correct! Well done!")
            is_correct = True
            score = 4 - attempts
        elif attempts < max_attempts:
            print("Your answer is incorrect! Please try again!\n")

    if not is_correct:
        print("Your answer is incorrect! Better luck next time!")

    return score


def run_quiz(world_capitals_dict):
    countries_tested = []
    overall_score = 0
    round_number = 1

    while round_number <= 6:
        print(f"Round {round_number}:\n")

        round_score = run_round(world_capitals_dict, countries_tested)
        overall_score += round_score

        round_number += 1
        print()

    print(f"You have scored {overall_score} out of 18 "
          "for the World Capital's Quiz!\n")
    return overall_score


def read_high_scores(filename):
    input_file = open(filename, "r")
    lines = input_file.readlines()
    input_file.close()

    scores = []
    index = 1
    while index < len(lines):
        line = lines[index].strip()
        if "." in line:
            parts = line.split(".")
            score_value = int(parts[1].strip())
            scores.append(score_value)
        index += 1
    return scores


def update_high_scores(filename, username, high_scores, new_score):
    high_scores.append(new_score)


    sorted_scores = []
    while len(high_scores) > 0:
        highest = high_scores[0]
        index = 1
        while index < len(high_scores):
            if high_scores[index] > highest:
                highest = high_scores[index]
            index += 1
        sorted_scores.append(highest)
        high_scores.remove(highest)


    top_five = []
    index = 0
    while index < len(sorted_scores) and index < 5:
        top_five.append(sorted_scores[index])
        index += 1


    output_file = open(filename, "w")
    output_file.write(f"High Scores for {username}\n")

    index = 0
    while index < len(top_five):
        line = str(index + 1) + ". " + str(top_five[index]) + "\n"
        output_file.write(line)
        index += 1

    output_file.close()


def handle_high_scores(filename, username, new_score):
    high_scores = read_high_scores(filename)
    update_high_scores(filename, username, high_scores, new_score)


if __name__ == "__main__":
    main()
