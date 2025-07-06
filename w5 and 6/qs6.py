class Recipe:
    def __init__(self, id, name, ingredients, description):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.description = description
    
    def display_recipe(self):
        print(f"\nRecipe ID: {self.id}")
        print(f"Name: {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print(f"Description: {self.description}")
        print("-" * 30)

class RecipeBook:
    def __init__(self):
        self.recipes = []
    
    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        print(f"Recipe '{recipe.name}' added successfully!")
    
    def display_all_recipes(self):
        if not self.recipes:
            print("\nNo recipes in the book yet!")
        else:
            print("\nAll Recipes in the Book:")
            for recipe in self.recipes:
                recipe.display_recipe()
    
    def find_recipe_by_id(self, id):
        for recipe in self.recipes:
            if recipe.id == id:
                return recipe
        return None

def create_recipe():
    print("\nEnter Recipe Details:")
    id = input("Enter recipe ID: ")
    name = input("Enter recipe name: ")
    
    print("Enter ingredients (type 'done' when finished):")
    ingredients = []
    while True:
        ingredient = input("- ")
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)
    
    description = input("Enter recipe description: ")
    
    return Recipe(id, name, ingredients, description)

def main():
    recipe_book = RecipeBook()
    
    while True:
        print("\nRecipe Book Menu:")
        print("1. Add a new recipe")
        print("2. View all recipes")
        print("3. Find a recipe by ID")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            recipe = create_recipe()
            recipe_book.add_recipe(recipe)
        
        elif choice == '2':
            recipe_book.display_all_recipes()
        
        elif choice == '3':
            id = input("Enter recipe ID to search: ")
            found_recipe = recipe_book.find_recipe_by_id(id)
            if found_recipe:
                found_recipe.display_recipe()
            else:
                print(f"No recipe found with ID {id}")
        
        elif choice == '4':
            print("Thank you for using Recipe Book!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1-4.")

if __name__ == "__main__":
    main()