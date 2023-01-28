question = "Do you support the use of medical cannabis in Greece?"
options = ["Yes", "No"]
votes = [0, 0]

print("Welcome to the electronic voting system!")
print(question)
for i, option in enumerate(options):
    print(f"{i + 1}. {option}")

while True:
    vote = input("Please enter the number of your choice (or 'q' to quit): ")
    if vote == 'q':
        break
    try:
        vote = int(vote)
        if vote < 1 or vote > len(options):
            print("Invalid vote. Please try again.")
        else:
            votes[vote - 1] += 1
    except ValueError:
        print("Invalid vote. Please try again.")

print("\nVoting Results:")
for i, option in enumerate(options):
    print(f"{option}: {votes[i]} votes")
