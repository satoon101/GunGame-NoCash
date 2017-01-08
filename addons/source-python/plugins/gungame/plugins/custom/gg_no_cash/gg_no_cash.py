# ../gungame/plugins/custom/gg_no_cash/gg_no_cash.py

"""Keep player cash always set to 0."""

# ============================================================================
# >> IMPORTS
# ============================================================================
# Python
from contextlib import suppress

# Source.Python
from entities.hooks import EntityCondition, EntityPostHook
from memory import make_object
from players.entity import Player


# =============================================================================
# >> ENTITY HOOKS
# =============================================================================
@EntityPostHook(EntityCondition.is_player, 'add_account')
def _set_cash(args, return_value):
    with suppress(ValueError):
        make_object(Player, args[0]).cash = 0
