# 8.voting system
# Voting System
# Concepts: Dictionary, Loop
# Count votes for candidates.
# Requirements:
# Store candidates and votes
# Add vote
# Display winner?
votes = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

def cast_vote():
    print("\nCandidates:")
    for candidate in votes:
        print(candidate)
    
    choice = input("Enter candidate name to vote: ")
    
    if choice in votes:
        votes[choice] += 1
        print(" Vote casted successfully!")
    else:
        print(" Invalid candidate")
def show_results():
    print(" Vote Count:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")

def show_winner():
    winner = max(votes, key=votes.get)
    print(f" Winner is {winner} with {votes[winner]} votes!")

while True:
    print("\n===== Voting Menu =====")
    print("1. Cast Vote")
    print("2. Show Results")
    print("3. Show Winner")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        cast_vote()
    elif choice == "2":
        show_results()
    elif choice == "3":
        show_winner()
    elif choice == "4":
        print(" Exiting voting system")
        break
    else:
        print(" Invalid choice")
