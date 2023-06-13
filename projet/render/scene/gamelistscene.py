from render.scene.basescene import BaseScene

class GameListScene(BaseScene):
    def __init__(self, quoridor):
        super().__init__(quoridor, "configs/gamelistscene.json")
    pass