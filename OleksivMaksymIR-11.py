class Camera:
    def __init__(self, produce_name: str, memory: float, zoom: float):
        self.__produce_name = produce_name
        self.__memory = memory
        self.__zoom = zoom
        num = 10
        line = "text"

    @property
    def produce_name(self):
        return self.__produce_name

    def get_produce_name(self):
        return self.__produce_name

    @produce_name.setter
    def produce_name(self, el):
        self.__produce_name = el

    @property
    def memory(self):
        return self.__memory

    @property
    def zoom(self):
        return self.__zoom

    def __str__(self) -> str:
        return (
            f"Camera: {self.produce_name} | memory: {self.memory} | zoom: {self.zoom}"
        )

    def __repr__(self) -> str:
        return f"Camera('{self.produce_name}', {self.memory}, {self.zoom})"

    def __del__(self):
        print("Об'єкт видалено")


if __name__ == "__main__":
    a = Camera("Camera1", 1024, 15)
    b = Camera("Camera2", 2048, 20)
    c = Camera("Camera3", 3072, 25)
    print(a.produce_name, a.memory, a.zoom, sep=" | ")
    print(b.produce_name, b.memory, b.zoom, sep=" | ")
    print(c.produce_name, c.memory, c.zoom, sep=" | ")
