from PokeAPI import PokeAPI
import plugins
import string
import random

#Version 0.2:
#Cleaned up the input correction function, attempting to remove if-else chains. fixed sun and moon stuff since they added it to the API
#TODO: Better error handling, pretty up code.

def _initialize():
	plugins.register_user_command(["pokedex"])
	

	#Red and Blue: 1 - 151
	
	#Silver and Gold: 152-251
	
	#Ruby and Sapphire: 252 - 386
	
	#Diamond and Pearl: 387 - 494
	
	#Black and White: 495-649
	
	#X and Y: 650 - 721
	
	#Sun and Moon: 722 - 802

def idRandomVersion(id): 									#Method to get random versions.
	
	if id >= 1 and id < 152:
        
        versionSelection = fromVersionRedAndBlue()
	
		return versionSelection									
		
	if id >= 152 and id < 252:
	
		versionSelection = fromVersionGoldAndSilver()
	
		return versionSelection
		
	if id >= 252 and id < 387:
	
		versionSelection = fromVersionRubyAndSapphire()
	
		return versionSelection
	
	if id >= 387 and id < 495:
	
		versionSelection = fromVersionDiamondAndPearl()
	
		return versionSelection
		
	if id >= 495 and id < 650:
	
		versionSelection = fromVersionBlackAndWhite()
	
		return versionSelection
		
	if id >= 650 and id < 722:
	
		versionSelection = fromVersionXAndY()
	
		return versionSelection
	
	if id >= 722 and id < 803:
	
		versionSelection = fromVersionSunAndMoon()
	
		return versionSelection
		
		
def fromVersionRedAndBlue():  #Dirty hardcode to make sure that it doesn't call for a random pokemon from a game before where it first appeared 
	
	#alpha-sapphire, omega-ruby, x, y, white-2, black-2, white, black, heartgold, soulsilver, platinum, diamond, pearl, leafgreen, firered, emerald
	#sapphire, ruby, crystal, silver, gold, yellow, blue, red
	
	versionList = ["alpha-sapphire", "omega-ruby", "x", "y", "white-2", "black-2", "white", "black", "heartgold", "soulsilver", "platinum", "diamond", "pearl", "leafgreen", "firered", "emerald", "sapphire", "ruby", "crystal", "gold", "silver", "yellow", "blue", "red"]

	selectedVersion = random.choice(versionList)
	
	return selectedVersion

def fromVersionGoldAndSilver(): 

	#alpha-sapphire, omega-ruby, x, y, white-2, black-2, white, black, heartgold, soulsilver, platinum, diamond, pearl, leafgreen, firered, emerald
	#sapphire, ruby, crystal, silver, gold
	
	versionList = ["alpha-sapphire", "omega-ruby", "x", "y", "white-2", "black-2", "white", "black", "heartgold", "soulsilver", "platinum", "diamond", "pearl", "leafgreen", "firered", "emerald", "sapphire", "ruby", "crystal", "gold", "silver"]
	
	selectedVersion = random.choice(versionList)
	
	return selectedVersion
	
def fromVersionRubyAndSapphire():

	#alpha-sapphire, omega-ruby, x, y, white-2, black-2, white, black, heartgold, soulsilver, platinum, diamond, pearl, leafgreen, firered, emerald
	#sapphire, ruby
	
	versionList = ["alpha-sapphire", "omega-ruby", "x", "y", "white-2", "black-2", "white", "black", "heartgold", "soulsilver", "platinum", "diamond", "pearl", "leafgreen", "firered", "emerald", "sapphire", "ruby"]
	
	selectedVersion = random.choice(versionList)
	
	return selectedVersion
	
def fromVersionDiamondAndPearl(): 

	#alpha-sapphire, omega-ruby, x, y, white-2, black-2, white, black, heartgold, soulsilver, platinum, diamond, pearl
	
	versionList = ["alpha-sapphire", "omega-ruby", "x", "y", "white-2", "black-2", "white", "black", "heartgold", "soulsilver", "platinum", "diamond", "pearl"]
	
	selectedVersion = random.choice(versionList)
	
	return selectedVersion
	
def fromVersionBlackAndWhite():
	
	#alpha-sapphire, omega-ruby, x, y, white-2, black-2, white, black
	
	versionList = ["alpha-sapphire", "omega-ruby", "x", "y", "white-2", "black-2", "white", "black"]
	
	selectedVersion = random.choice(versionList)
	
	return selectedVersion
	
def fromVersionXAndY():

	#alpha-sapphire, omega-ruby, x, y
	
	versionList = ["alpha-sapphire", "omega-ruby", "x", "y"]
	
	selectedVersion = random.choice(versionList)
	
	return selectedVersion
	
def fromVersionSunAndMoon():
	
	#moon only due to API.
	
	selectedVersion = "moon"
	
	return selectedVersion
	
	

		
		
	


def pokedex(bot, event, *args): #Primary bot listener function. 

	if len(args) >= 4: #Rigid commands to prevent bot spam in chat. Possibly add regex later.
			yield from bot.coro_send_message(event.conv, "<i>The proper formats are: <b>pokemonname gameversion language</b>, <b>pokemonname gameversion</b>, <b>pokemonname</b>, or no arguments for a random pokemon</i>")
			
			return
	
	pk = PokeAPI()
	
	if len(args) == 3:
	
		pokemonName = args[0] #First argument is pokemon name
	
		versionName = args[1] #Second argument is game name
	
		languageName = args[2] #Third argument is language
	
	if len(args) == 2:
	
		pokemonName = args[0]
		
		versionName = args [1]
		
		languageName = "en" #Default to English
		
	if len(args) == 1:
	
		pokemonName = args[0]
		
		languageName = "en"
		
	if len(args) == 0: #If a pokemon is requested without any arguments at all
		
		randomID = randint(1,803) #Random ID for name and version
		
		pokemonName = str(randomID)
		
		versionName = idRandomVersion(randomID)
		
		languageName = "en"
		
		
	
	
		
		
	
	
	##TODO: Add default english option.
	
	pokedexSpeciesEntry = pk.get_pokemon_species(pokemonName.lower()) #Gets info for whole species
	pokedexPokemon = pk.get_pokemon(pokemonName.lower()) 		      #Gets specific pokemon info
	
	pokedexFlavor = pokedexSpeciesEntry['flavor_text_entries']  #Grabs pokedex flavor description
	pokedexName = pokedexSpeciesEntry['names']					#Grabs pokedex pokemon name
	pokedexGenera = pokedexSpeciesEntry['genera'] 				#Grabs pokemon genus
	pokedexHeight = pokedexPokemon['height']                    #Grabs pokemon height
	pokedexWeight = pokedexPokemon['weight']					#Grabs pokemon weight
	pokedexTypes = pokedexPokemon['types']						#Grabs pokemon type(s)
	pokedexPokemonID = pokedexPokemon['id']						#Grabs pokemon ID


    if len(args) == 1: #Dirty workaround for the single name command
		
		versionName = idRandomVersion(pokedexPokemonID)
		
		


    versionNameCorrectionDict = { #dictionary and loop to correct some common input errors.
    "fire-red": "firered",
    "leaf-green": "leafgreen", 
    "black2": "black-2", 
    "white2": "white-2", 
    "alphasapphire": "alpha-sapphire", 
    "omegaruby": "omega-ruby"
    }

    for key, value in versionNameCorrectionDict.items(): 
        if key == versionName:
            versionName = value

        
			
	
	
	nameList = [element["name"] for element in pokedexName if "name" in element if languageName.lower() in element["language"].values()] ##Grab name for the input pokemon/language
	
	if pokedexPokemonID > 721: #Sun and Moon ID'd Pokemon
		flavorList = [element["flavor_text"] for element in pokedexFlavor if "flavor_text" in element if languageName.lower() in element["language"].values() if "moon" in element["version"].values()] #Grab pokeflavor for sun and moon
	else: 
		flavorList = [element["flavor_text"] for element in pokedexFlavor if "flavor_text" in element if languageName.lower() in element["language"].values() if versionName.lower() in element["version"].values()] #Grab pokeflavor
	
	genusList = [element["genus"] for element in pokedexGenera if "genus" in element if languageName.lower() in element["language"].values()] #grab pokemon genus.
	type1List = [element["type"] for element in pokedexTypes if "type" in element if element["slot"] == 1] #List for the pokemon's first type
	type2List = [element["type"] for element in pokedexTypes if "type" in element if element["slot"] == 2]	#List for the Pokemon's second type
	pokemonHeight = str(pokedexHeight) #Formatting pokedex height and weight
	pokemonWeight = str(pokedexWeight)
	
	if len(pokemonHeight) == 0:
		return
	
	if len(pokemonHeight) == 1:
		formattedHeight = "Height:" + " " + "0." + pokemonHeight + " " + "Metres"
	
		
	else:
		
		heightIndex = (len(pokemonHeight) - 2) #Position of character just before the last
		
		formattedHeight = "Height:" + " " + pokemonHeight[0:heightIndex] + pokemonHeight[heightIndex] + "." + pokemonHeight[-1] + " " + "Metres"  
		
	if len(pokemonWeight) == 0:
		
			return
	
	if len(pokemonWeight) == 1:
		
				formattedWeight = "Weight:" + " " + "0." + pokemonWeight + " " + "Kilograms"
		
	else:
		
		weightIndex = (len(pokemonWeight) - 2)
			
		formattedWeight = "Weight:" + " " + pokemonWeight[0:weightIndex] + pokemonWeight[weightIndex] + "." + pokemonWeight[-1] + " " + "Kilograms"
			
				
				
	if len(flavorList) > 0 and len(nameList) > 0 and len(genusList) > 0 and len(type1List) > 0:
	
		flavorString = str(flavorList[0])
		nameString = str(nameList[0])
		genusString = str(genusList[0])
		
		if type2List:  
			type1List = [element["name"] for element in type1List if "name" in element]
			type2List = [element["name"] for element in type2List if "name" in element]
			typeString = str(type1List) + str(type2List)
		
		if not type2List: 
		
			type1List = [element["name"] for element in type1List if "name" in element]
			typeString = str(type1List)
			
		
	
	else: 
		yield from bot.coro_send_message(event.conv, "<i>No such entry, friend</i>")
		
		return
	
	cleanedFlavorString = str.replace(flavorString, "\n", "\r\n")
	
	pokedexEntryString = '<b>"{}"</b><br /><br /><i>{}</i><br />{}<br /><br />{}<br />{}<br /><br /><i>"{}"</i>'.format(nameString, genusString, typeString, formattedHeight, formattedWeight, cleanedFlavorString)
	
	
	yield from bot.coro_send_message(event.conv, pokedexEntryString)
		
		

