from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        players.sort(key=lambda x:x.goals+x.assists, reverse=True)

        return [player for player in players if player.nationality == nationality]

