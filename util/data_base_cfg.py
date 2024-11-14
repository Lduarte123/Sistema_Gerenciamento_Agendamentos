class Config():
    def __init__(self):
        self.cfg = 'postgresql://postgres:123@localhost/postgres'

    def get_cfg(self):
        return self.cfg