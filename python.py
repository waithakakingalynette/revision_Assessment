# 1.**Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

class Stories:
    def __init__(self,title,moral_value,length,language):
        self.title=title
        self.moral_value=moral_value
        self.length=length
        self.language=language

    def getStory(self):
        return f"The story {self.title}  teaches a moral of {self.moral_value}  is of length {self.length}.The language used in this story is {self.language}"  

story= Stories ("Born A crime","Do not give up",12,"English")
print(story.getStory())


class StoryTeller:
    def __init__(self,name,language, title):
        self.name =name
        self.title=title
        self.language=language
    def tellStories(self):
        return f"{self.name} is telling {self.title} in {self.language}" 

stories=StoryTeller("Grace Ogot","Luo","Tekayo") 
print(stories.tellStories())  

class Translator(StoryTeller):
    def __init__(self,targetLanguage,name, title,language):
        self.name=name
        self.title=title
        self.language=language
        self.targetLanguage=targetLanguage

    def tellStory(self):
        return f"{self.name} translates {self.title} from {self.language} to {self.targetLanguage}"  

translate=Translator("Luo" ,"Paula Karimi","Tekayo","Kiswahili")  
print(translate.tellStory())  


# 2. **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.

class Recipe:
     def __init__(self,name,country,unique_ingredients,preparation_time,cooking_method,nutritional_value) :
         self.name=name
         self.country=country
         self.unique_ingredients=unique_ingredients
         self.preparation_time=preparation_time
         self.cooking_method=cooking_method
         self.nutritional_value=nutritional_value
class MoroccanRecipe(Recipe):
    def __init__(self, name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value):
        super().__init__(name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value)
    def cook(self):
        return f"for{self.name} of country  {self.country}  cook the meal with{self.ingredients} and prepare at{self.preparation_time} using method{self.cooking_method}to gain  nutritional_value{self.nutritional_value}"
class EthopianRecipe(Recipe):
    def __init__(self, name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value):
        super().__init__(name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value)
    def cook(self):
        return f"for{self.name} of country  {self.country}  cook the meal with{self.ingredients} and prepare at  {self.preparation_time} using method{self.cooking_method}to gain  nutritional_value{self.nutritional_value}"
class  NigerianRecipe(Recipe):
    def __init__(self, name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value):
        super().__init__(name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value)
    def cook(self):
        return f"for{self.name} of country  {self.country}  cook the meal with{self.ingredients} and prepare at{self.preparation_time} using method{self.cooking_method}to gain  nutritional_value{self.nutritional_value}"
# morrocan= MoroccanRecipe("Wheat","Morrocco",[Maji,skuma],"30 minutes","grilling","500gms","cumin")
# ethopian= EthiopianRecipe("chicken_breasts","Ethopia",[anjera,milk],"45 minutes","stewing","600gms","doro wat")
nigerian=NigerianRecipe("Jollo Rice","Nigeria",["rice","tomato","onion"],"1 hour","cooking","700gms","party jollof")
# print(morrocan.cook())
# print(ethiopian.cook())
print(nigerian.cook())