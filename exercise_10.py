import random

def create_story():
    characters = ["Frodo", "Sam", "Merry", "Pippin", "Gandalf", "Legolas", "Gimli", "Aragorn", "Boromir", "Merry", "Pippin", "Gandalf", "Legolas", "Gimli", "Aragorn", "Boromir"]
    actions = ["Save", "Fight Against", "Find", "Kill", "Eat", "Sleep", "Pray", "Sing", "Dance", "Play", "Learn", "Read", "Write", "Code", "Rock", "Roll", "Dance", "Play", "Learn", "Read", "Write", "Code", "Rock", "Roll"]
    locations = ["Shire", "Rivendell", "Mordor", "Minas Tirith", "Gondor", "Angband", "Moria", "Lorien", "Isengard", "Shire", "Rivendell", "Mordor", "Minas Tirith", "Gondor", "Angband", "Moria", "Lorien", "Isengard"]

    story = f"{random.choice(characters)} {random.choice(actions)} {random.choice(locations)}"
    print(story)

if __name__ == "__main__":
    create_story()