from render.scene.gamescene import GameScene

class NetworkedGameScene(GameScene):
    def __init__(self, quoridor, game, background=None):
        super().__init__(quoridor, game, background)
        