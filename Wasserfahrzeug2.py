
class Wasserfahrzeug:

    def __init__(self, baujahr: int = 2022, besitzer: str = 'Max Mustermann', name: str = 'Wasserfahrzeug_name', tiefgang: float = 12.2):
        self.__baujahr = baujahr
        self.__besitzer = besitzer
        self.__name = name
        self.__tiefgang = tiefgang

    def __repr__(self):
        return f'Wasserfahrzeug[name={self.__name},besitzer={self.__besitzer},baujahr={self.__baujahr},tiefgang={self.__tiefgang}]'

    def get_baujahr(self):
        return self.__baujahr

    def get_besitzer(self):
        return self.__besitzer

    def get_name(self):
        return self.__name

    def get_tiefgang(self):
        return self.__tiefgang

    def set_baujahr(self, baujahr: int):
        if baujahr > -2000 and baujahr < 2023:
            self.__baujahr = baujahr

    def set_besitzer(self, besitzer: str):
        self.__besitzer = besitzer

    def set_name(self, name: str):
        self.__name = name

    def set_tiefgang(self, tiefgang: float):
        if tiefgang > 0 and tiefgang < 100:
            self.__tiefgang = tiefgang


if __name__ == '__main__':
    wf = Wasserfahrzeug()
    print(wf.get_tiefgang())
    wf.set_tiefgang(1233)
    print(wf.get_tiefgang())
    wf.set_tiefgang(1.2)
    print(wf.get_tiefgang())
    wf.set_tiefgang(-2)
    print(wf.get_tiefgang())
