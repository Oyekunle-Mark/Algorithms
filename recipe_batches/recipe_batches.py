#!/usr/bin/python


def recipe_batches(recipe, ingredients):
    recipe_amount = recipe.values()
    ingredients_amount = ingredients.values()

    batches = []

    if len(recipe_amount) != len(ingredients_amount):
        return 0

    for rec, ing in zip(recipe_amount, ingredients_amount):
        ratio = ing // rec

        if ratio == 0:
            return 0

        batches.append(ratio)

    return min(batches)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
