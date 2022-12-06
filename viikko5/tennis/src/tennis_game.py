class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.points = {
            player1_name: 0,
            player2_name: 0
        }

        self.scores = [
            "Love",
            "Fifteen",
            "Thirty",
            "Forty"
        ]

    def won_point(self, player_name):
        self.points[player_name] += 1

    def get_score(self):
        score_1 = self.points[self.player1]
        score_2 = self.points[self.player2]
        
        if score_1 == score_2 and score_1 > 3:
            return "Deuce"
        elif score_1 > 3 and score_1 >= score_2 + 2:
            return f"Win for {self.player1}"
        elif score_2 > 3 and score_2 >= score_1 + 2:
            return f"Win for {self.player2}"
        elif score_1 > score_2 and score_1 > 3:
            return f"Advantage {self.player1}"
        elif score_2 > score_1 and score_2 > 3:
            return f"Advantage {self.player2}"

        score = ""
        score = self.scores[score_1]
        score = score + "-"
        
        if score_1 == score_2:
            score = score + "All"
        else:
            score = score + self.scores[score_2]
        
        return score
