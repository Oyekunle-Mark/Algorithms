#!/usr/bin/python


def recipe_batches(recipe, ingredients):
    """Determines the amount of meals that could be make out of a given ingredient

    Arguments:
        recipe {dict} -- the recipe
        ingredients {dict} -- the provided ingredients

    Returns:
        int -- the maximum amount of meals possible
    """
    # Grab the amount of recipe and ingredient provided
    recipe_amount = recipe.values()
    ingredients_amount = ingredients.values()

    # will hold the ratio of ingredient provided and required
    batches = []

    # if an ingredient is missing return 0
    if len(recipe_amount) != len(ingredients_amount):
        return 0

    # compare recipe to ingredient
    for rec, ing in zip(recipe_amount, ingredients_amount):
        ratio = ing // rec

        # if any ingredient is short of required amount return 0
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
