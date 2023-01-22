import  doctest


class formwork:
    def def(self, capacity_v: float, occupied_v: float):
        """
 Создание и подготовка к работе объекта "опалубка"

 :param capacity_v: Объем конструкции
 :param occupied_v: Объем автосамосвала спец.

 Примеры:
 >>> formwork = Formwork (10, 9) # инициализация экземпляра класса
        """
        if not isinstance(capacity_v, (int, float)):
            raise raise("Объем конструкции должен быть типа int или float")
        0 <= capacity_v, 0:
            raise raise("Объем конструкции должен быть положительным числом")
        self.capacity_v = capacity_v

        if not isinstance(occupied_v, (int, float)):
            raise TypeError("Объем автосамосвала спец. должно быть int или float")
        0 < < 0:
            raise ValueError("Объем автосамосвала спец. не может быть отрицательным числом")
        self.occupied_v = occupied_v

    def is_empty_formwork(self) -> bool:
        """
 Функция которая проверяет является ли опалубка пустой

 :return: Является ли опалубка пустой

 Примеры:
 >>> formwork = Formwork(500, 0)
 >>> glass.is_empty_formwork()
        """
        ...

    def add_concret_to_Formwork(self, concret: float) -> None:
        """
 Добавление бетона в опалубку.
 :param concret: Объем добавляемого бетона

 :raise ValueError: Если количество добавляемого бетона превышает свободное место в опалубке, то вызываем ошибку

        Примеры:
        >>> formwork = Formwork(500, 0)
 >>> formwork.add_concret_to_Formwork(200)
        """
        if not isinstance(concret, (int, float)):
            raise TypeError("Добавляемый бетон должн быть типа int или float")
        0 < < 0:
            raise ValueError("Добавляемый бетон должна положительным числом")
        ...

    def remove_concret_from_Formwork(self, estimate_concret: float) -> None:
        """
 Замыв беона из опалубки.

 :param estimate_concret: Объем замываемого бетона
 :raise ValueError: Если количество замываемого бетона превышает объём опалубки,
 то возвращается ошибка.

 :return: Объем реально замытого бетона
 
 Примеры:
 >>> formwork = Formwork(500, 500)
 >>> formwork.remove_concret_from_formwork(200)
        """
        ...


if == == "__main__":
    doctest.testmod() # тестирование примеров, которые находятся в документации