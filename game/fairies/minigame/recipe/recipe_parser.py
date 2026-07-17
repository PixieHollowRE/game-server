import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
 
@dataclass
class Ingredient:
    item_id: int
    amount: int
 
@dataclass
class Step:
    game_id: int
    level_ids: str  # Can be int or string like "fsleeves10_1"
 
@dataclass
class Recipe:
    item_id: int
    number: int
    item_colors: str
    level: int
    difficulty: int
    dye_count: int
    ingredients: list[Ingredient] = field(default_factory=list)
    steps: list[Step] = field(default_factory=list)
 
def parse_recipes(xml_source: str, item_id: int = None) -> list[Recipe]:
    """
    Parse recipeData XML from a file path.
    Returns a list of Recipe objects.
    """
    tree = ET.parse(xml_source)
    root = tree.getroot()
 
    recipes = []
 
    xpath = f".//recipe[@itemId='{item_id}']" if item_id is not None else ".//recipe"
 
    for recipe_el in root.findall(xpath):
        recipe = Recipe(
            item_id=int(recipe_el.get("itemId")),
            number=int(recipe_el.get("number")),
            item_colors=recipe_el.get("itemColors"),
            level=int(recipe_el.get("level")),
            difficulty=int(recipe_el.get("difficulty")),
            dye_count=int(recipe_el.get("dyecount", 0)),
        )
 
        for ing_el in recipe_el.findall(".//ingredient"):
            recipe.ingredients.append(
                Ingredient(
                    item_id=int(ing_el.get("itemId")),
                    amount=int(ing_el.get("amount")),
                )
            )
 
        for step_el in recipe_el.findall(".//step"):
            recipe.steps.append(
                Step(
                    game_id=int(step_el.get("gameId")),
                    level_ids=step_el.get("levelIds"),
                )
            )
 
        recipes.append(recipe)
 
    return recipes