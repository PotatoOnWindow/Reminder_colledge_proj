from datetime import date

class remind():
    def __init__(self):
        # all of it is **th day. so decrease by 1 for each
        self.days = [1, 2, 3, 5, 8, 12, 18, 25, 45] 


    def check_date(self, start_date, now_date):
        isItRemindDay = False
        dates_diff = (now_date - start_date).days
        if dates_diff in self.days:
            isItRemindDay = True

        return isItRemindDay
