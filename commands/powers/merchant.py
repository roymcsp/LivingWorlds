import time
from evennia import utils
from world.contents.crafting.recipes import RECIPES
from world.contents.crafting.materials import MATERIALS
from commands.command import MuxCommand
from evennia.utils.spawner import spawn

empire_list = ()
caliphate_list = ()
kingdom_list = ()

class CmdForge(MuxCommand):
    """
    Spell Name: Forge
       MP Cost: 10
        Syntax: forge material recipe
   Skills used: none

   Description:

   A simple spell that allows a merchant/artisan/trader
    to create either weapons or armor from material components.
   """

    key = "forge"
    locks = "cmd:all()"
    help_category = "commands"

    def func(self):
        args = self.args
        caller = self.caller
        recipe = ""
        material = ""

        if not args:
            caller.msg("Forge What?")
            return

        if " " in args:
            material, recipe = self.args.split(" ", 1)

        if recipe not in RECIPES.keys():
            caller.msg("That is not a valid recipe.")
            return

        item_name = "%s %s" % (material.capitalize(), recipe)
        item_aliases = RECIPES.get(recipe).get("aliases")
        item_desc = RECIPES.get(recipe).get("desc")
        item_weight = RECIPES.get(recipe).get("weight") * MATERIALS.get(material).get("weight_mod")
        item_value = RECIPES.get(recipe).get("value") * MATERIALS.get(material).get("value_mod")
        item_damage = RECIPES.get(recipe).get("damage_roll")
        item_range = RECIPES.get(recipe).get("range")
        item_durability = RECIPES.get(recipe).get("durability") * MATERIALS.get(material).get("durability_mod")
        item_hardness = RECIPES.get(recipe).get("hardness") * MATERIALS.get(material).get("hardness_mod")

        weapon_proto = {
            "key": item_name,
            "aliases": item_aliases,
            "typeclass": "typeclasses.weapons.Weapon",
            "desc": item_desc,
            "weight": item_weight,
            "value": item_value,
            "damage_roll": item_damage,
            "range": item_range,
            "durability": item_durability,
            "hardness": item_hardness,
            "location": caller
        }

        spawn(weapon_proto)
        caller.msg("You succeed in forging a %s %s" % (material.capitalize(), recipe))

"""    
class CmdForgeWeapon(MuxCommand):

     Spell Name: Forge Weapon
        MP Cost: 10
         Syntax: forgeweapon <recipe>
                
    Skills used: forge, weapons

    Description:

    A simple spell that allows a merchant/artisan/trader
     to create weapons from resource components.


    key = "forge"
    locks = "cmd:attr_ge(level, 1)"
    help_category = "commands"

    def func(self):
        args = self.args
        caller = self.caller
        tr = self.caller.traits
        lastcast = caller.db.forge_lastcast

        if not args:
            caller.msg("Forge What?")

        if tr.SP.current < 10:
            caller.msg("You don't have enough power to cast this spell")
            return

        if lastcast and time.time() - lastcast < 3 * 60:
            caller.msg("You cannot forge another item yet")
            return

        if "Kingdom" in caller.db.nation:
            forge = self.obj.search('Forge', global_search=True)
            weapon_list = kingdom_list
            if not forge:
                caller.msg("You must be in the forge to use this power")
                return
            if self.recipe not in weapon_list:
                caller.msg("This is not a valid recipe.")
                return

        elif "Caliphate" in  caller.db.nation:
            forge = self.obj.search('Forge', global_search=True)
            weapon_list = caliphate_list
            if not forge:
                caller.msg("You must be in the forge to use this power")
                return
            if self.recipe not in weapon_list:
                caller.msg("This is not a valid recipe.")
                return

        elif "Empire" in caller.db.nation:
            forge = self.obj.search('Forge', global_search=True)
            weapon_list = empire_list

            if not forge:
                caller.msg("You must be in the forge to use this power")
                return
            if self.recipe not in weapon_list:
                caller.msg("This is not a valid recipe.")
                return

        tr.SP.current -= 10

        item_name = "%s %s" % (material, recipe),
        item_aliases = recipe.aliases
        item_desc = recipe.desc
        item_weight = recipe.weight
        item_value = recipe.value
        item_damage = recipe.roll
        item_range = recipe.range
        item_durability = material.durability
        item_hardness = material.hardness

        weapon_proto = {
            "key": item_name,
            "aliases": item_aliases,
            "typeclass": "typeclasses.weapons.Weapon",
            "desc": item_desc,
            "weight": item_weight,
            "value": item_value,
            "damage_roll": item_damage,
            "range": item_range,
            "durability": item_durability,
            "hardness": item_hardness
        }

        caller.msg('You fire up the forge in preparation to forge an item.')
        caller.location.msg_contents(
            "{actor} fires up the forge in preperation to forge an item.",
            mapping=dict(actor=caller),
            exclude=caller)
        utils.delay(5, callback=self.forgeone)

    def forgeone(self):

        caller = self.caller
        caller.msg('')
        caller.location.msg_contents(
            "",
            mapping=dict(actor=caller),
            exclude=caller)
        utils.delay(5, callback=self.forgetwo)

    def forgetwo(self):
        caller = self.caller
        caller.msg("")
        caller.location.msg_contents(
            "",
            mapping=dict(actor=caller),
            exclude=caller)
        utils.delay(5, callback=self.forgethree)

    def forgethree(self):
        spawn(self.weapon_proto)

        caller = self.caller
        caller.msg("")
        caller.location.msg_contents(
            "",
            mapping=dict(actor=caller),
            exclude=caller)

        caller.db.forge_lastcast = time.time()

class ForgeArmor(MuxCommand):
    armor_proto = {
        "key": item_name,
        "aliases": item_aliases,
        "typeclass": armor_type,
        "desc": item_desc,
        "weight": item_weight,
        "value": item_value,
        "physical_bonus": item_pbonus,
        "magical_bonus": item_mbonus
    }


item_name = "%s %s" % (material, recipe),
item_aliases = recipe.aliases
item_desc = recipe.desc
item_weight = recipe.weight
item_value = recipe.value
item_damage = recipe.roll
item_range = recipe.range
item_durability = material.durability
item_hardness = material.hardness

weapon_proto = {
    "key": item_name,
    "aliases": item_aliases,
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": item_desc,
    "weight": item_weight,
    "value": item_value,
    "damage_roll": item_damage,
    "range": item_range,
    "durability": item_durability,
    "hardness": item_hardness
}

if tr.SP.current < 10:
    caller.msg("You don't have enough power to cast this spell")
    return

if lastcast and time.time() - lastcast < 3 * 60:
    caller.msg("You cannot forge another item yet")
    return

tr.SP.current -= 10
caller.msg('You fire up the forge in preparation to forge an item.')
caller.location.msg_contents(
    "{actor} fires up the forge in preperation to forge an item.",
    mapping=dict(actor=caller),
    exclude=caller)
"""