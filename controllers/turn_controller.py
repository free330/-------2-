# controllers/turn_controller.py
class TurnController:
    def __init__(self, model, move_service, history_service):
        self.model = model
        self.move_service = move_service
        self.history = history_service

    def handle_tableau_click(self, tableau_idx, card, from_pos, to_pos):
        record = self.move_service.move_from_tableau_to_hand(tableau_idx, card, from_pos, to_pos)
        if record:
            self.history.push(record)
        return record

    def handle_hand_click(self, from_pos, to_pos):
        record = self.move_service.draw_from_stock(from_pos, to_pos)
        if record:
            self.history.push(record)
        return record

    def handle_stock_click(self):
        return None

    def undo(self):
        return self.history.undo()