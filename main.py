# Створити клас – календарна дата з полями: день (1-31), місяць (1-12), рік (ціле число).
# Визначити конструктор, функції зміни дня, місяця і року, отримання значень дня, місяця і року,
# отримання назви дня тижня для заданої дати і по назві дня тижня – найближчої дати від заданої, яка буде цим днем.
# Перевантажити операції < (порівняння дат у календарі за днем тижня), + (визначення найближчої дати від заданої,
# яка буде днем тижня – другим операндом). Відсортувати масив екземплярів класу дат у календарі за зростанням значення дня тижня,
# для кожної дати в масиві визначити найближчу дату, яка буде заданим днем тижня.
class CalendarDate:
    days_in_week = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П\'ятниця', 'Субота', 'Неділя']

    def __init__(self, day, month, year):
        self.set_date(day, month, year)

    def is_leap_year(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def get_days_in_month(self, month, year):
        days_in_month = [0, 31, 29 if self.is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days_in_month[month]

    def set_date(self, day, month, year):
        if isinstance(day, int) and isinstance(month, int) and isinstance(year, int):
            if 1 <= month <= 12 and 1 <= year:
                if 1 <= day <= self.get_days_in_month(month, year):
                    self.day = day
                    self.month = month
                    self.year = year
                else:
                    raise ValueError("Неправильно введений день")
            else:
                raise ValueError("Неправильно введений місяць або рік")
        else:
            raise ValueError("Дата повинна складатись з цілих чисел")

    def zeller_algorithm(self):
        d, m, y = self.day, self.month, self.year
        if m < 3:
            m += 12
            y -= 1
        return ((d + (13 * (m + 1)) // 5 + y + y // 4 - y // 100 + y // 400) - 2) % 7

    def day_of_week(self):
        return self.days_in_week[self.zeller_algorithm()]

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"

    def __lt__(self, other):
        return self.zeller_algorithm() < other.zeller_algorithm()

    def __add__(self, weekday):
        if weekday in self.days_in_week:
            days_difference = (self.days_in_week.index(weekday) - self.days_in_week.index(self.day_of_week())) % 7
            if days_difference == 0:
                days_difference = 7
            new_day, new_month, new_year = self.day + days_difference, self.month, self.year

            if new_day > self.get_days_in_month(new_month, new_year):
                new_day -= self.get_days_in_month(new_month, new_year)
                new_month += 1

            if new_month > 12:
                new_month = 1
                new_year += 1

            return CalendarDate(new_day, new_month, new_year)
        else:
            raise ValueError("Неправильна назва дня")


dates = [CalendarDate(23, 8, 1899), CalendarDate(12, 12, 1795), CalendarDate(5, 11, 1771), CalendarDate(22, 6, 1995),
         CalendarDate(15, 4, 1616), CalendarDate(1, 12, 1719), CalendarDate(2, 5, 2050), CalendarDate(29, 2, 2040),
         CalendarDate(2, 6, 2093), CalendarDate(2, 5, 2173), CalendarDate(15, 5, 2623), CalendarDate(3, 5, 2223),
         CalendarDate(4, 5, 2823)]
dates.sort()

print("Сортування за днями тижня:")
for date in dates:
    print(f"{date} - {date.day_of_week()}")

weekday = 'Понеділок'
print(f"\nНаступні дати коли буде {weekday}:")
for date in dates:
    print(f"Наступна дата після {date} коли буде {weekday}, це {date + weekday}")
input("Натисніть Enter для продовження...")