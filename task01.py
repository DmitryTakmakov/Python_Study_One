from time import sleep


class TrafficLight:
    __color = None
    __cycle_counter = 0  # да, про вторую переменную в задаче не говорилось, но для тестовых потребностей пусть будет

    def running(self):
        while True:
            self.__color = 'Red'
            print(f'{self.__color} light! Everyone stop!')
            sleep(7)
            self.__color = 'Yellow'
            print(f'{self.__color} light! Be prepared')
            sleep(2)
            self.__color = 'Green'
            print(f'{self.__color} light! Go, go, go!')
            sleep(10)
            self.__cycle_counter += 1
            if self.__cycle_counter > 10:
                break


if __name__ == '__main__':
    t_l_object = TrafficLight()
    t_l_object.running()
