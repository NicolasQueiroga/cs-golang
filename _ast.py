# ---
class ProgramNode:
    def __init__(self, var_decl, game_loop):
        self.var_decl = var_decl
        self.game_loop = game_loop


# ---


class VariablesDeclarationNode:
    def __init__(self, variables):
        self.variables = variables


class VariableNode:
    def __init__(self, data_type, identifier1, identifier2):
        self.data_type = data_type
        self.identifier1 = identifier1
        self.identifier2 = identifier2


# ---


class GameLoopNode:
    def __init__(self, digit1, digit2, loops):
        self.digit1 = digit1
        self.digit2 = digit2
        self.loops = loops


class LoopNode:
    def __init__(self, round_cond, round_statements):
        self.round_cond = round_cond
        self.round_statements = round_statements


# ---


class WeaponBuyNode:
    def __init__(self, weapon_identifier, digit):
        self.weapon_identifier = weapon_identifier
        self.digit = digit


class KillNode:
    def __init__(self, identifier, weapon_identifier):
        self.identifier = identifier
        self.weapon_identifier = weapon_identifier


class DeathNode:
    def __init__(self, identifier, weapon_identifier):
        self.identifier = identifier
        self.weapon_identifier = weapon_identifier


class BombPlantNode:
    def __init__(self, plant_location, bomb_site):
        self.plant_location = plant_location
        self.bomb_site = bomb_site


class BombDefuseNode:
    def __init__(self, bomb_site, digit):
        self.bomb_site = bomb_site
        self.digit = digit


class RoundEndNode:
    def __init__(self, team_identifier, round_winner, digit1, digit2):
        self.team_identifier = team_identifier
        self.round_winner = round_winner
        self.digit1 = digit1
        self.digit2 = digit2


# ---
