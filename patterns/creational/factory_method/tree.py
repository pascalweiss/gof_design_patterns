

# ------------------Product-----------------------

class Tree:
    def get_name(self):
        raise NotImplementedError


# ---------------ConcreteProduct------------------

class CorkOak(Tree):
    def get_name(self):
        return "cork oak"


class Olive(Tree):
    def get_name(self):
        return "olive"


class Cypress(Tree):
    def get_name(self):
        return "cypress"


class Spruce(Tree):
    def get_name(self):
        return "spruce"


class Pine(Tree):
    def get_name(self):
        return "pine"


class Beech(Tree):
    def get_name(self):
        return "beech"
