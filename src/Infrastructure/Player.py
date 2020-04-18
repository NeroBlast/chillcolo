

class Joueur():
    
    def __intit__(self,nom):
        super().__init__()
        self.nom = nom
        self.gorgee = 0
    
    def add_gorgee(self,nb_gorgee):
        self.gorgee += nb_gorgee