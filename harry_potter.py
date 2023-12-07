class Wizard:

    def __init__(self, name, house):
        self.name = name
        self.house = house
    
# hermione = Wizard("hermione Grange", "Grifinolia")
# draco= Wizard("Draci Malfoy", "Sonserina")
# hermione.name = "vanessa"
# print(hermione.name)
# print(hermione.house)
# print(draco.name)
# print(draco.house)

class student:
    def __init__(self, name, mat, n1, n2):
        self.name = name
        self.mat = mat
        self.n1 = n1
        self.n2 = n2

    def calcula_media(self):
        return((2 * self.n1)+ (3 * self.n2)) / 5

    def is_aproved(self):
        return self.calcula_media() >= 6
    
    def __str__(self):
        return f''' sou {self.name} tirei na n1 {self.n1} e na n2 {self.n2} e fiquei aprovado? {self.is_aproved()} '''
        
    
Saulo = student('saulo', '20221321000093', 6, 6)

print(Saulo)