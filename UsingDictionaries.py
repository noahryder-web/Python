# Using Dictionaries 
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Extend letter_to_points to handle lowercase inputs
letters_and_points = {key: value for key, value in zip(letters, points)}
letters_and_points.update({key.lower(): value for key, value in zip(letters, points)})
letters_and_points[" "] = 0


def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letters_and_points.get(letter, 0)
  return point_total
brownie_points = score_word("BROWNIE")
print(brownie_points)


player_to_words = {"player1" : ["BLUE", "TENNIS", 'EXIT'], "wordNerd" : ["EARTH", "EYES", "MACHINE"], "Lexi Con" : ["ERASER", "BELLY", 'HUSKY'], "Prof Reader" : ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}

# Function to update point totals for all players
def update_point_totals():
    for player, words in player_to_words.items():
        player_to_points[player] = sum(score_word(word) for word in words)

# Function to allow players to play a new word
def play_word(player, word):
    if player in player_to_words:
        player_to_words[player].append(word)
    else:
        player_to_words[player] = [word]
    # Recompute points for the player
    player_to_points[player] = sum(score_word(w) for w in player_to_words[player])

# Add a new word for a player and print updated points
play_word("vixenpop", "COLD")
print(player_to_points)

# Initial point calculation
update_point_totals()

# Example: Adding a new word for a player
play_word("player1", "BROWNIE")
play_word("newPlayer", "hello")

# Output results
print(player_to_words)
print(player_to_points)

# Output: 15
#{'vixenpop': 7}
#{'player1': ['BLUE', 'TENNIS', 'EXIT', 'BROWNIE'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD'], 'vixenpop': ['COLD'], 'newPlayer': ['hello']}
#{'vixenpop': 7, 'player1': 44, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31, 'newPlayer': 8}

