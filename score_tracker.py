import json
import os

class ScoreTracker:
    def __init__(self, filepath="scores.json"):
        self.filepath = filepath
        self.scores = self.load_scores()

    def load_scores(self) -> dict:
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                return json.load(f)
        return {"player_wins": 0, "ai_wins": 0, "draws": 0}

    def save_scores(self):
        with open(self.filepath, "w") as f:
            json.dump(self.scores, f, indent=4)

    def record_result(self, winner: str):
        if winner == "X":
            self.scores["player_wins"] += 1
        elif winner == "O":
            self.scores["ai_wins"] += 1
        else:
            self.scores["draws"] += 1
        self.save_scores()
