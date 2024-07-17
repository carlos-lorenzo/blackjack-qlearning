from blackjack.table import Table
from blackjack.players import Player


table = Table()

table.add_player(Player())

table.start_turn()
table.play_turn()
#table.dealer.play(table.deck)