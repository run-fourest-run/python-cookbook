import copy

class Squad:
    def __init__(self,mates):
        if mates is None:
            self.mates = []
        else:
            self.mates = list(mates)

    def __iter__(self):
        return (i for i in (self.mates))

    def __repr__(self):
        classname = type(self).__name__
        return '{}({!r}'.format(classname,*self)


class Player:
    __slots__ = ('__name','kils','wins','loses','deaths')

    def __init__(self,name,kills,wins,loses,deaths):
        self.__name = name
        self.kills = kills
        self.wins = wins
        self.deaths = deaths
        self.loses = loses


    @property
    def name(self):
        return self.__name

    def getkd(self):
        kdratio = self.kills/self.deaths
        return kdratio


    def __repr__(self):
        classname = type(self).__name__
        return '{}(!r},{!r},{!r},{!r})'.format(classname,self.name,self.kills,self.wins,self.loses)


warzone_trios_squad = Squad(['Jared','Spencer','Alex'])
warzone_trios_squad_copy = copy.copy(warzone_trios_squad)
warzone_trios_squad_deep_copy = copy.deepcopy(warzone_trios_squad_copy)







