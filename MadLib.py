#Machine Problem 1 - PyLibs

#Define a story template #using string interpolation to insert value for my variable in my predefined text
story_template = """Once upon a time, {} was at the center of a controversial event involving the relocation of the {}s from {} to {}. The plan was to {} valuable land from the island of {}, forcing the {}s to leave their ancestral home. This action was meant to make way for large-scale development projects.

{} had a significant role in formulating this scheme, leading to the displacement of the {}s. The {}s, who had lived on {} for centuries, were devastated by the forced relocation. The plan was to move them to {}, which {} thought would offer new opportunities.

The {}, known for its advocacy for indigenous rights, was outraged by {}'s actions because displacing the original residents was harsh. They decided to arrest {}, but when {} heard of their plan, {} tried to {}. However, thanks to the {}'s strong sense of {} and its {} nature, {} was soon {} by the {}.

During the trial, {} was asked how many {}s had been affected by the relocation. Calmly, {} responded that the number was {} plus {}, totaling {} {}s. Despite the overwhelming evidence of relocations and other illegal transactions between big figures and {}, {} remained {}. Due to {} lack of empathy and refusal to make amends, {} was sentenced to be {}.

On the day of the sentence, {} sat in a judgement chair. As the crowd outside grew, {} maintained a {} facade and declared, “If you want my secrets, you must uncover them! I’ve hidden clues around {}. Good luck!”. {} strongly believed that the {}’s actions were just a part of {} plan to clout chase and then {} would be able to escape with all the fortune, leaving everyone searching for {} forever.

{} expected the crowd to {} in excitement. However, they stared in confusion. For the first time, {} felt genuine fear and tried to escape but was unsuccessful. Desperate and fearing the loss of all {} hard-earned gains, {} begged to be forgiven, but {} pleas were silenced when a poisonous {} pierced through {} mouth, and everything went {}.

{} awoke to the sound of an old, ordinary bus. Feeling a sharp pain in {} mouth, {} saw familiar faces of locals from {}. Although {} felt {} among them, there was relief in being alive. Suddenly, {} noticed a newspaper headline: “{}: Headshot by an Unknown {}.”

A man stood next to the bus driver, announcing, “Next stop, {}!”. {} shouted but only a muffled sound of a cry of a baby was heard, {} stiffened when a woman above {} inserted something on {} mouth. {} is now part of the {}, and unfortunately for {}, {}'s now a child of one of the people {} mistreated. As the bus rolled away, a tear fell from {}'s eye, knowing that this was just the beginning of a new journey to reap what {} had sown. \n"""


#Collect user input
name = input("Enter a name for your character with this format (e.g., Robin): ")
pronoun1 = input("Choose a pronoun for your character (he or she): ")
pronoun2 = input("Choose another pronoun for your character (his or her): ")
pronoun3 = input("Choose another pronoun for your character (him or her): ")
verb1 = input("Enter the opposite of the word 'give'(in lowercase): ")
#restricted input for verb1
while True:
	if verb1 == "take":
		break
	else:
		verb1 = input("Give and ____. Input Answer: ")
place1 = input("Enter a name of an island with this format (e.g., Palawan): ")
group_of_people = input("Enter an indigenous people in the Philippines with this format (e.g., Igorot): ")
place2 = input("Enter another place with this format (e.g., Iloilo): ")
organization = input("Enter an organization with this format (e.g., National Commission on Indigenous Peoples): ")
verb2 = input("Enter a term that conveys a similar meaning of taking someone into custody or holding them under control: ")
verb3 = input("Enter the opposite of the word 'walk': ").lower()
#restricted input for verb3
while True:
	if verb3 == "run":
		break
	else:
		verb3 = input("Hint: It is a physical activity involving moving rapidly on foot. Input Answer: ")
animal = input("Enter an animal (e.g., elephant): ")
noun1 = input("Enter a noun that represents one of the different senses (e.g., taste): ")
verb4 = input("Enter the past tense of the word 'catch' (in lowercase): ")
#restricted input for verb4
while True:
	if verb4 == "caught":
		break
	else:
		verb4 = input("UWU! Try again. Input Answer: ")
num1 = int(input("Enter a counting number (e.g., 44): "))
#condition for num1
while True:
	if num1 >= 1:
		break
	else:
		num1 = int(input("Choose from 1 to positive infinity: "))
num2 = int(input("Enter another counting number (e.g., 44): "))
#condition for num2
while True:
	if num2 >= 1:
		break
	else:
		num2 = int(input("Choose from 1 to positive infinity: "))
personal_trait = input("Enter the opposite of the word 'OA' (in lowercase): ")
#restricted input for personal_trait
while True:
	if personal_trait == "nonchalant":
		break
	else:
		personal_trait = input("It is your crush who seemed to care less about your dms. Input Answer: ")
punishment = input("Enter a punishment in past tense (e.g., kicked): ")
noun2 = input("Enter a type of weapon (e.g., sword): ")
color = input("Enter a shade that is the opposite of 'white' (in lowercase): ")
#restricted input for color
while True:
	if color == "black":
		break
	else:
		color = input("Sure, sure, I close my eyes. - Queen Yasmin.\n What do you see? Input Answer: ")
adjective = input("Fill in the blank with the correct word to complete the lyric.\n And I'm so ____ of love song, so tired of fears.\n Enter the answer (in lowercase): ")
#restricted input for adjective
while True:
	if adjective == "sick":
		break
	else:
		adjective = input("Hint: The word you are looking for means 'unwell' or 'ill'. Input Answer: ")
ML_Role = input("Choose an ML Role with this format (Assassin, Marksman, Mage, or Fighter): ")
verb5 = input("Enter a gesture you make with your hands to celebrate or applaud someone: ")
noun3 = input("What is the synonym of the word 'smart' (in lowercase): ")
def add(num1, num2):
	return (num1 + num2)

#Print the completed Mad Lib story
print("\nHere is your Mad Lib story!")
print("\n\033[1mFrom Oppressor to Oppressed\033[0m\n")

#Insert user inputs into the story
print(story_template.format(name,group_of_people,place1,place2,verb1,place1,group_of_people,name,group_of_people,group_of_people,place1,place2,pronoun1,organization,name,name,pronoun1,pronoun1,verb3,animal,noun1,noun3,name,verb4,organization,pronoun1,group_of_people,pronoun1,num1,num2,add(num1,num2),group_of_people,name,pronoun1,personal_trait,pronoun2,name,punishment,pronoun1,pronoun1,personal_trait,place1,name,organization,pronoun2,pronoun1,pronoun3,name,verb5,pronoun1,pronoun2,pronoun1,pronoun2,noun2,pronoun2,color,name,pronoun2,pronoun1,place1,pronoun1,adjective,pronoun1,name,ML_Role,place2,name,pronoun1,pronoun3,pronoun2,name,group_of_people,pronoun3,pronoun1,pronoun1,name,pronoun1,pronoun1))

print("\033[1mThe End\033[0m")
