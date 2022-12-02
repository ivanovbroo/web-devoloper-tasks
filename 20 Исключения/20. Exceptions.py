import json
import datetime


class Booking:

    def __init__(self, room_name: str, start: datetime.datetime, end: datetime.datetime) -> None:
        if start > end:
            raise ValueError("Начальная дата позже конечной даты")

        self.__room_name = room_name
        self.__start     = start
        self.__end       = end         
    
    start = property()
    end   = property()
    
    @start.setter
    def start(self, start_date):
        if start_date > self.__end:
            raise ValueError("Начальная дата позже конечной даты")
            
        self.__start = start_date

    @end.setter
    def end(self, end_date):
        if self.__start > end_date:
            raise ValueError("Начальная дата позже конечной даты")
        self.__end = end_date

    @property
    def room_name(self):
        return self.__room_name

    @property
    def duration(self):
        return float((self.__end - self.__start).total_seconds()//60)
    
    @property
    def start_date(self):
        return self.__start.strftime("%Y-%m-%d")
    
    @property
    def start_time(self):
        return self.__start.strftime("%H:%M")

    @property
    def end_date(self):
        return self.__end.strftime("%Y-%m-%d")
    
    @property
    def end_time(self):
        return self.__end.strftime("%H:%M")

    def create_booking(room_name, start, end):
        print("Начинаем создание бронирования")
        booking = Booking(room_name, start, end)
        date_booking = dict()
        try:            
            if register_booking(booking) == True:
                date_booking["created"] = True
                date_booking["msg"]     = "Бронирование создано"
            else:
                date_booking["created"] = False
                date_booking["msg"]     = "Комната занята"

        except KeyError:
            date_booking["created"] = False
            date_booking["msg"]     = "Комнатане найдена"
        finally:
            print("Заканчиваем создание бронирования")

        date_booking["booking"] = {"room_name" : booking.room_name,
                                   "start_date": booking.start_date,
                                   "start_time": booking.start_time,
                                   "end_date"  : booking.end_date,
                                   "end_time"  : booking.end_time,
                                   "duration"  : booking.duration}

        return json.dumps(date_booking)




b = Booking(1, datetime.datetime(2022, 9, 1, 14), datetime.datetime(2022, 9, 1, 15, 15))
print(b.__dict__)

print(b.end_date)

b.start = datetime.datetime(2022, 9, 1, 15)
print(b.__dict__)

b.end = datetime.datetime(2022, 9, 1, 16)
print(b.__dict__)

