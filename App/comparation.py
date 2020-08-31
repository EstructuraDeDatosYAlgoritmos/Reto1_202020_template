class Comparation:
    def __init__(self, tag='id'):
        self.tag = tag

    def upVal(self, element1, element2):
        if float(element1[self.tag]) > float(element2[self.tag]):
            return True
        return False

    def downVal(self, element1, element2):
        if float(element1[self.tag]) < float(element2[self.tag]):
            return True
        return False