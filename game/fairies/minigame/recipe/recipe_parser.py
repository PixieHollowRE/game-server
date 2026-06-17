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


def _int_attr(el: ET.Element, name: str, default: int = 0) -> int:
    value = el.get(name)
    if value is None or value == "":
        return default
    return int(value)


def parse_recipes(xml_source: str, item_id: int = None) -> list[Recipe]:
    """
    Parse recipeData XML from a string or file path.
    Returns a list of Recipe objects.
    """
    try:
        root = ET.fromstring(xml_source)
    except ET.ParseError:
        # Try treating it as a file path
        tree = ET.parse(xml_source)
        root = tree.getroot()
 
    recipes = []
 
    xpath = f".//recipe[@itemId='{item_id}']" if item_id is not None else ".//recipe"
 
    for recipe_el in root.findall(xpath):
        recipe = Recipe(
            item_id=_int_attr(recipe_el, "itemId"),
            number=_int_attr(recipe_el, "number"),
            item_colors=recipe_el.get("itemColors"),
            level=_int_attr(recipe_el, "level"),
            difficulty=_int_attr(recipe_el, "difficulty"),
            dye_count=_int_attr(recipe_el, "dyecount"),
        )

        for ing_el in recipe_el.findall(".//ingredient"):
            recipe.ingredients.append(
                Ingredient(
                    item_id=_int_attr(ing_el, "itemId"),
                    amount=_int_attr(ing_el, "amount"),
                )
            )

        for step_el in recipe_el.findall(".//step"):
            recipe.steps.append(
                Step(
                    game_id=_int_attr(step_el, "gameId"),
                    level_ids=step_el.get("levelIds"),
                )
            )
 
        recipes.append(recipe)
 
    return recipes
