// 1.**Ancestral Stories:** In many African cultures, the art of storytelling is passed
// down from generation to generation. Imagine you're creating an application that records these oral stories and translates them into different languages. The
// stories vary by length, moral lessons, and the age group they are intended for.
// Think about how you would model `Story`, `StoryTeller`, and `Translator`
// objects, and how inheritance might come into play if there are different types of
// stories or storytellers.

class Stories{
    constructor(title,moral_lesson,length,language){
        this.title = title,
        this.moral_lesson=moral_lesson,
        this.length =length,
        this.language = language
        
    }
    getStory(){
        return `The story ${this.title} is of ${this.moral_lesson} and is of length ${this.length}.The language used is ${this.language}`
    }


}
const story= new Stories("Born a Crime", "Do not sleep",12,"Kikuyu")
console.log(story.getStory());

class StoryTeller extends Stories{
    constructor(){

    }
}


class Translator{
    
}

// 2. **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// methods.