class Slab:
    def __init__(self, thickness: int, density: int, material: str):
        self.thickness = thickness
        """ Толщина плиты """
        self.material = material
        """Материал плиты"""
        self.density = density
        """Плотность материала"""

    def __str__(self):
        return f"Толщина перекрытия - {self.thickness}, материал - {self.material}"

    def __repr__(self):
        return f"{self.__class__.__name__}(thickness={self.thickness!r}, material={self.material!r})"

    def lenth(self):
        print(f"Длина пролета от {self.thickness*27} до {self.thickness*32}")
        """указывает рекомендуемый интервал назначения длины пролета"""

    def material_density(self):
        print(f"Плотность материала {self.material}: {self.density}")
        """Прописывает указанную плотность для указанного материала"""

class ConcreteSlab(Slab):

    def __str__(self):
        return f"Толщина перекрытия - {self.thickness}, материал - {self.material}, класс бетона - В25"
    """Бетон имеет важную характеристику - класс по прочности"""
    def lenth(self):
        print (f"Рекомендуемая длина пролета - {self.thickness*30}")
    """Рекомендуется длину пролета назначать в районе 30 толщин плиты"""
if __name__ == "__main__":
    # Write your solution here
    conc_B25 = ConcreteSlab(200, 2400, 'Бетон' )
    conc_B25.lenth()
    conc_B25.material_density()
    pass