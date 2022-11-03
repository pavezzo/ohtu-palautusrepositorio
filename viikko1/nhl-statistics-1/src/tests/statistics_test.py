import unittest
from statistics import Statistics, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_statistics_finds_right_player(self):
        player = self.statistics.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_statistics_returns_none_if_no_player(self):
        self.assertEqual(self.statistics.search("Koivu"), None)

    def test_statistics_finds_right_players_for_team(self):
        players = self.statistics.team("EDM")
        self.assertEqual(players[1].name, "Kurri")

    def test_find_top_players_by_points(self):
        players = self.statistics.top(2)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")

    def test_find_top_players_by_goals(self):
        players = self.statistics.top(2, SortBy.GOALS)
        self.assertEqual(players[0].name, "Lemieux")
        self.assertEqual(players[1].name, "Yzerman")
    
    def test_find_top_players_by_ASSISTS(self):
        players = self.statistics.top(2, SortBy.ASSISTS)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Yzerman")
