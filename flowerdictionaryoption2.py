
# Different dictionarys for different flower features
# Size dictionary:
size_dictionary = { 'Rose' : 'medium','Allium' : 'large', 'Oriental Lily': 'large', 'Peruvian Lily': 'medium', 'Athene Amaryllis': 'medium', 'Bearded Iris': 'medium'}
# Colour dictionary:
colour_dictionary = { 'Rose' : 'red','Allium' : 'purple', 'Oriental Lily': 'sweet', 'Peruvian Lily': 'orange', 'Athene Amaryllis': 'white', 'Bearded Iris': 'purple'}
#Smell dictionary
smell_dictionary = { 'Rose' : 'sweet','Allium' : 'onions', 'Oriental Lily': 'sweet', 'Peruvian Lily': 'none', 'Athene Lily': 'mild', 'Bearded Iris': 'grapes'}
#Season dictionary
season_dictionary = { 'Rose' : 'summer','Allium' : 'summer', 'Oriental Lily': 'summer', 'Peruvian Lily': 'summer', 'Athene Lily': 'winter', 'Bearded Iris': 'spring'}
#Latin name
latin_dictionary = { 'Rose' : 'rosa macdub','Allium' : 'allium sativum', 'Oriental Lily': 'lilium ornamentalis', 'Peruvian Lily': 'alstreomeria', 'Athene Lily': 'hippeastrum athene', 'Bearded Iris': 'iris germanica'}
#Maintenance
maintenance_dictionary = { 'Rose' : 'high','Allium' : 'low', 'Oriental Lily': 'low', 'Peruvian Lily': 'low', 'Athene Lily': ' medium', 'Bearded Iris': 'high'}


#  etc etc

# Find all flowers of certain feature in certain dictionary:
# Arguments: a dictionary, a feature to find
def find_feature(in_dictionary, feature):
    matching_flowers = []
    for key,value in in_dictionary.items(): 
        if value == feature:
            matching_flowers.append(key)
    if(len(matching_flowers) == 0):
        print('No flowers with desired feature in given dictionary.')
    return matching_flowers

def return_all_flower_features(in_dictionaries,flower):
    feature_list = []
    for dictionary in in_dictionaries:
        feature_list.append(dictionary[flower])
    return feature_list


print(find_feature(colour_dictionary,'purple'))
