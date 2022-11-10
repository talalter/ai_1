class Vertex:

    def __init__(self, id_, peoples=0, is_brittle=False):
        self.id_ = id_
        self.peoples = peoples
        self.is_brittle = is_brittle
        self.is_broken = False

    def get_is_brittle(self):
        return self.is_brittle

    def __str__(self):
        return str(self.id_)