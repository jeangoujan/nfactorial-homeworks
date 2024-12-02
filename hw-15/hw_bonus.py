"""
💎 Exercise 1: User Management System

Design a User Management System for an application. 
The User class should have details such as name and email. 
he User Management System should allow users to register, 
delete their account, and update their information.
"""


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserManagementSystem:
    def __init__(self):
        self.users = []

    def register(self, user):
        self.users.append(user)

    def delete_account(self, user):
        self.users.remove(user)

    def update_info(self, user, new_info):
        if 'name' in new_info:
            user.name = new_info['name']
        if 'email' in new_info:
            user.email = new_info['email']






"""
💎 Exercise 2: Quiz Application

Create a Quiz class that has a list of Questions. 
Each Question has a question, a list of options and a correct answer. 
The Quiz should allow questions to be added, and it should calculate the 
score of a user based on the answers they provide.
"""


class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer


class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def calculate_score(self, user_answers):
        user_score = 0
        q = ''
        a = ''
        for question, answer in user_answers.items():
            q = question
            a = answer
        for question in self.questions:
            correct = question.correct_answer
            if correct == a:
                user_score += 1

        return user_score


"""
💎 Exercise 3: Recipe Management System

Design a Recipe Management System. The Recipe class should have a name, 
a list of ingredients and the preparation steps. 
The Recipe Management System should allow recipes to be added, removed, 
and searched by ingredient.
"""


class Recipe:
    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps


class RecipeManagementSystem:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        self.recipes.remove(recipe)

    def search_by_ingredient(self, ingredient):
        found_recipes = []
        for recipe in self.recipes:
            ingrs = recipe.ingredients
            for i in ingrs:
                if i == ingredient:
                    found_recipes.append(recipe)

        return found_recipes


# system = RecipeManagementSystem()
# recipe1 = Recipe("Kartoshka Zharenaya", ["kartoshka", "sol"], ['step1', 'step2'])
#
# system.add_recipe(recipe1)
# print(system.search_by_ingredient("kartoshka"))
"""
💎 Exercise 4: Online Shopping System

Create a ShoppingCart class for an online shopping system. 
The Product class represents a product with name and price. 
The ShoppingCart should allow products to be added, removed, 
and it should calculate the total price of the products in the cart.
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def calculate_total(self):
        total_price = 0
        for product in self.products:
            price = product.price
            total_price += price

        return total_price
