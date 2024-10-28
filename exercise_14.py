def votation():
    votes = [0, 0, 0]
    for _ in range(3):
        vote = int(input("Enter a vote (1, 2, or 3): ")) - 1
        if 0 <= vote <= 2:
            votes[vote] += 1
        else:
            print("Invalid vote")
        print("Result of the votes:", votes)

if __name__ == "__main__":
    votation()
    