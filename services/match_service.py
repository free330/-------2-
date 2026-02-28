# services/match_service.py
class MatchService:
    @staticmethod
    def can_match(card1, card2):
        """两张牌数字相差1即可，无花色限制"""
        return abs(card1.rank - card2.rank) == 1