# ----------------------------------------------------------------------
# This is the file mad_libs.py
#
# The intent is to give you practice writing a complete, interactive
# Python program using a lot of Python data types, especially lists,
# sets, and dictionaries.
#
# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
#
# Things to do:
#
# Define a bunch of templates in which some of the words begin with a colon (:).
# The words that begin with a colon are the words that you will ask the user
# to fill in. An example of a template is:
#
#     "The :color :animal :action over the :adjective :plant."
#
# You should define a list of at least 10 templates. Be creative!
#
# Your app should begin by selecting a random template. Then, for each word
# that begins with a colon in the template, prompt the user for a word
# that fits the description. Make sure that their input is between 1 and 30
# characters long, to prevent them from making too much of a mess of things.
#
# After the user has filled in all of the words, print the completed
# template with the user's words filled in. Then after a blank line, print
# a line crediting the author of the template. Then, print a couple of blank
# lines and ask them if they want to play again. If they say "yes" (or "sí"
# or "oui") or any acceptable version of an affirmative answer, start over
# with a new random template. Otherwise, say "no", print "Thanks for playing!"
# and exit the program.
#
# Here are some constraints:
#
#   1. The templates should be a list of dictionaries, in which each entry
#      has a "text" fields and an "author" field. The "text" field should
#      contain the template string, and the "author" field should contain
#      the name of the person who wrote the template.
#
#   2. The possible "yes" answers should be stored in a set.
# ----------------------------------------------------------------------

import random
import re



templates = [
    {
        "text": "Some :adjective :creature with a :weapon is eating :dessert.",
        "author": "rtoal"
    },
    {
        "text": "Look! There is a :adverb :adjective :noun :verb in :place.",
        "author": "The whole class"
    },
    {
        "text": "The :color :animal :past_tense_verb over the :adjective :plant.",
        "author": "rtoal"
    },
    {
        "text": "Dear :person, I am writing to tell you that your :noun has been "
                ":past_tense_verb by a :adjective :animal.",
        "author": "The whole class"
    },
    {
        "text": "To make the perfect :food, first :verb the :noun, then add "
                ":number cups of :liquid.",
        "author": "rtoal"
    },
    {
        "text": "Breaking news: a :adjective :profession was seen :verb_ing "
                "through :place while wearing a :color :clothing_item.",
        "author": "The whole class"
    },
    {
        "text": "My :family_member once :past_tense_verb a :adjective :animal "
                "and now we are :adjective forever.",
        "author": "rtoal"
    },
    {
        "text": "Welcome to :place! Please keep your :body_part inside the "
                ":vehicle at all times and do not feed the :animal.",
        "author": "The whole class"
    },
    {
        "text": "In the year :number, scientists discovered that :food is "
                "really just a :adjective :noun in disguise.",
        "author": "rtoal"
    },
    {
        "text": "Once upon a time, a :adjective :profession named :person "
                "found a magic :noun and shouted \":exclamation!\"",
        "author": "The whole class"
    },
]

yes_answers = {
    "yes", "y", "si", "sí", "oui", "yup", "bet", "yea", "yeah", "ye", "yep",
    "sure", "ok", "okay" "ight" "alr" "alright"
}

MIN_LENGTH = 1
MAX_LENGTH = 30


BLANK_PATTERN = re.compile(r":(\w+)")


def ask_for_word(description):
    """Keep prompting until the user gives a word of valid length."""
    label = description.replace("_", " ")
    while True:
        answer = input(f"Enter a {label}: ").strip()
        if MIN_LENGTH <= len(answer) <= MAX_LENGTH:
            return answer
        print(f"Please enter between {MIN_LENGTH} and {MAX_LENGTH} characters.")


def fill_template(text):
    """Prompt for each blank in the template and return the completed text."""
    return BLANK_PATTERN.sub(lambda match: ask_for_word(match.group(1)), text)


def play_round():
    """Play one round: pick a template, fill it in, and show the result."""
    template = random.choice(templates)
    completed = fill_template(template["text"])
    print()
    print(completed)
    print()
    print(f"Template written by: {template['author']}")


def wants_to_play_again():
    """Ask the user whether to play again and interpret the answer."""
    print("\n")
    answer = input("Do you want to play again? ").strip().lower()
    return answer in yes_answers


def main():
    while True:
        play_round()
        if not wants_to_play_again():
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()