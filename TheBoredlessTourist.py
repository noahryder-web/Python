# The Boredless Tourist, an online application giving you the power to find the parts of the city that fit the pace of your life. We at The Boredless Tourist run a recommendation engine using Python. We first evaluate what a person’s interests are and then give them recommendations in their area to venues, restaurants, and historical destinations that we think they’ll be engaged by. 
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"] 

test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]] #There is a list within a list here, the database knows what each elements stands for 

def get_destination_index(destination):
    destination_index = destinations.index(destination)  # Finds the index of the destination. Tell me where the destination we are passing is located within the list 
    return destination_index # This will tell us where it is located so we have to return the code 

print(get_destination_index("Los Angeles, USA")) 
# This is going to see where this is in the list (the index here will be 2) We wouldnt be able to find this is we didn't return the function 
# If it is not in the list it will show ValueError 

def get_traveler_location(traveler):
    traveler_destination = traveler[1] # Based on the tes traveler we can see the location is at index one, therefore the destination is seen at one 
    traveler_destination_index = get_destination_index(traveler_destination) # Retreive the index of the destination where the traveler is, we know it will be at index one in the list
# What it also does here is it looks at the get traveler location function and it sees where the location of the traveler is in that list, so for Shanghai it would be at index one within the list 
    return traveler_destination_index # Once again just helps with passing the data and giving us access 

test_destination_index = get_traveler_location(test_traveler) 
print(test_destination_index)
# We are doing this to test the function, this will call Shanghai by stating index 1, where is is in the list as we call the test_traveler 


attractions = [] # Creates an empty list of attrations for every destination 
for destination in destinations: 
# This loop means: destination is basically each thing within the destinations list, the loop will run 5 times as there are 5 places within the list 
  attractions.append([]) # This will run 5 times within the list, therefore will add 5 empty lists within the attractions list 
# This can also be done manually 
print(attractions) 
# Will just print the list with 5 empty lists within a list 

def add_attraction(destination, attraction):
    try:
      destination_index = get_destination_index(destination) # The same as above we go to the above function and we call a destination within that function 
      attractions_for_destination = attractions[destination_index].append(attraction) # If there is no synatc error then the place does exist in the list. We will then first look at the attractions list and then look at the index in the attractions list. E.g if we look for paris france and we want to add an attraction for the Paris destination 
# We found our corresponding attraction within the destinations list and then we add the attraction to that specific list 
    except SyntaxError: # If we cant find it it will not add it to the list 
      return 
# This function will do nothing when the place is not within the list and will return nothing 

add_attraction("Los Angeles, USA" , ["Venice Beach", ["beach"]])
print(attractions)
# Since it does exist in the list and is at index two and then it will look at the attractions list (which is the empty lists) therefore the empty list at the attractions list will then add beach and Venice beach 
# This will then print the list with the beach as the third element wihtin the list of attractions 

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# Does what the above with LA does, the list is now pretty big 

def find_attractions(destination, interests):
    destination_index = get_destination_index(destination) # Used the function multiple times previously 
    attractions_in_city = attractions[destination_index] # Look up the destinations attractions, we know the attractions list corresponds to the destinations list. We look at the list of attractions for the specified destination 
    attractions_with_interests = [] # Creates a new list, if the attraction matches interest then we save into here 

    for attraction in attractions_in_city: 
      possible_attraction = attraction # A temporary variable is created here 
      attraction_tags = attraction[1] # Attraction tags are what the attraction is and is based behind index 1. So here attraction tags we are assigning to the index one which is the actual attraction   
      
      for interest in interests:
        if interest in attraction_tags: # If the interest is within the list where index 2 is the attraction tags (describes what the attraction is)
          attractions_with_interests.append(possible_attraction[0]) # Adding the 0 here will also show the name of the attraction and not the tags (0 element is where the attraction is)
          
    return attractions_with_interests # This will iterate through all the attractions within the destination we are in and for all the interests, if the interest is included then it will add to the attractions with interest list 

la_arts = find_attractions("Los Angeles, USA", ['art'])
print(la_arts) # This will print out the LACMA as it shows the interest for this location, it will also print out the tags for the attractions, with the 0 it will not show the tags 

def get_attractions_for_traveler(traveler):
    
    traveler_destination = traveler[1]  # Destination 
    traveler_interests = traveler[2]  # The interests are after destination we are just saving this 

    
    traveler_attractions = find_attractions(traveler_destination, traveler_interests) # Returns the names of the attractions for the city the traveler is in 
    
    interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
    
# If we want the last attraction there we add a full stop after it, if there is more attractions we add a comma 

    for i in range(len(traveler_attractions)):  # Look at the list and see how many elements are there 
      if traveler_attractions[-1] == traveler_attractions[i]: # If it is more the i (the amount) then we use a comma and if its ended then we use a fullstop 
        interests_string += "the " + traveler_attractions[i] + "."
      else:
        interests_string += "the " + traveler_attractions[i] + ", "

    return interests_string


smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)