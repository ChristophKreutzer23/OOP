
class Wasserfahrzeug:

    def __init__(self, baujahr: int = 2022, besitzer: str = 'Max Mustermann', name: str = 'Wasserfahrzeug_name', tiefgang: float = 12.2):
        self.baujahr = baujahr
        self.besitzer = besitzer
        self.name = name
        self.tiefgang = tiefgang

    def __repr__(self):
        return f'Wasserfahrzeug[name={self.name},besitzer={self.besitzer},baujahr={self.baujahr},tiefgang={self.tiefgang}]'


if __name__ == '__main__':
    wf = Wasserfahrzeug()
    print(wf.tiefgang)
