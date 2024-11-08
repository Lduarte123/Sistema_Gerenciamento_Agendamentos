class Config():
    def __init__(self):
        self.cfg = 'postgresql://postgres:postgres@localhost/senac'

    def get_cfg(self):
        return self.cfg