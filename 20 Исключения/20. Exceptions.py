import json
import datetime

class Booking:

    def __init__(self, room_name, start, end):
        print("Начинаем создание бронирования")
        if start > end:
            raise ValueError

        self.room_name  = room_name
        
        self.__start = start
        self.__end   = end

        self.duration   = int((end - start).total_seconds()//60)

        self.start_date = datetime.datetime.strftime(start, "%Y-%m-%d")
        self.start_time = datetime.datetime.strftime(start, "%H:%M")
        
        self.end_date   = datetime.datetime.strftime(end, "%Y-%m-%d")
        self.end_time   = datetime.datetime.strftime(end, "%H:%M")
         
    
    start = property()
    end   = property()
    
    @start.setter
    def start(self, start_date):
        if start_date > self.__end:
            raise ValueError
        self.__start = start_date
        self.start_date = datetime.datetime.strftime(start_date, "%Y-%m-%d")
        self.start_time = datetime.datetime.strftime(start_date, "%H:%M")
        self.duration   = int((self.__end - start_date).total_seconds()//60)

    @end.setter
    def end(self, end_date):
        if self.__start > end_date:
            raise ValueError
        self.__end = end_date
        self.end_date = datetime.datetime.strftime(end_date, "%Y-%m-%d")
        self.end_time = datetime.datetime.strftime(end_date, "%H:%M")
        self.duration = int((end_date - self.__start).total_seconds()//60)

    def create_booking(room_name, start, end):
        Booking = Booking(........)
        try:
            result = register_booking(booking)
        except ....:
            ....
        return json.dumps(......)




b = Booking("Nikita", datetime.datetime(2022, 9, 1, 14), datetime.datetime(2022, 9, 1, 15, 15))
print(b.__dict__)

b.start = datetime.datetime(2022, 9, 1, 15)
print(b.__dict__)

b.end = datetime.datetime(2022, 9, 1, 16)
print(b.__dict__)

print(b.start)
print(b.end)

deadline1 = datetime.datetime(2022, 9, 1, 14)
print(deadline1)

deadline2 = datetime.datetime(2022, 9, 1, 15, 15)
print(deadline2)

duration =int((deadline2 - deadline1).total_seconds()//60)
print(duration)

date = datetime.datetime.strftime(deadline1, "%Y-%m-%d")
print(date)

time = datetime.datetime.strftime(deadline1, "%H:%M")
print(time)

