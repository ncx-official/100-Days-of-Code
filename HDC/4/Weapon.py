class Weapon:
    def __init__(self, id, name, view, win_ids, draw_ids, lose_ids):
        self.id = id
        self.name = name
        self.view = view
        self.win_ids = win_ids
        self.draw_ids = draw_ids
        self.lose_ids = lose_ids
    
    def compareAction(self, opponentWeapon):
        if opponentWeapon.id in self.win_ids:
            return True
        elif opponentWeapon.id in self.draw_ids:
            return None
        return False
    
    def getPreset(self):
        print(self.view)