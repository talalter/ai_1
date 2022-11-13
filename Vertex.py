
class Vertex:
    def __init__(self, id_, people=0, is_brittle=False):
        self.id_ = id_
        self.people = people
        self.people_saved = 0
        self.first_agent_id = None
        self.is_brittle = is_brittle
        self.is_broken = False

    def get_is_brittle(self):
        return self.is_brittle

    def get_is_broken(self):
        return self.is_broken

    def __repr__(self):
        return "id=%d people=%d saved_people=%d brittle=%s broken=%s" % (self.id_,
                                                                         self.people,
                                                                         self.people_saved,
                                                                         self.is_brittle,
                                                                         self.is_broken)