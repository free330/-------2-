# services/history_service.py
class HistoryService:
    def __init__(self):
        self.history = []
        self.current = -1

    def push(self, move_record):
        """记录一步移动"""
        self.history.append(move_record)
        self.current = len(self.history) - 1

    def undo(self):
        """撤销上一步，返回记录用于反向动画"""
        if self.current < 0:
            return None
        record = self.history[self.current]
        self.current -= 1
        return record

    def clear(self):
        self.history = []
        self.current = -1