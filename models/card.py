# models/card.py
class Card:
    """单张纸牌模型"""
    def __init__(self, suit: int, rank: int, face_up: bool = False):
        self.suit = suit      # 0:♠,1:♥,2:♣,3:♦
        self.rank = rank      # 1-13 (A=1, J=11, Q=12, K=13)
        self.face_up = face_up

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def to_dict(self):
        return {'suit': self.suit, 'rank': self.rank, 'face_up': self.face_up}

    @classmethod
    def from_dict(cls, data):
        return cls(data['suit'], data['rank'], data['face_up'])