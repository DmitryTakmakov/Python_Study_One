class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def extractor(cls, date: str):
        d, m, y = date.split('-')
        return int(d), int(m), int(y)

    @staticmethod
    def validator(date: str):
        d, m, y = Date.extractor(date)
        if 1 < d < 30 and 1 < m < 12 and len(str(y)) == 4:
            return 'Все в порядке'
        else:
            return 'Один из параметров соответствует заданному формату.'


day, month, year = Date.extractor('16-02-2020')
print(day, month, year)
print(Date.validator('100-12-1900'))
# хочу оговориться, что я совершенно не понял логику этого задания...
