import requests
from bs4 import BeautifulSoup
from datetime import date
from libs.Event import Event
from libs.Schedule import Schedule
from libs.ScheduleException import ScheduleException


class CyberSecLessonSchedule(object):
    def __init__(self):
        pass

    @staticmethod
    def getEventSchedule(courseYear, month, year):
        if (courseYear > 2 or courseYear < 1):
            raise Exception(
                'Course year cannot be larger than 2 and less than 1')

        if (month > 12 or month < 1):
            raise Exception(
                'Month year cannot be larger than 12 and less than 1')

        url = 'https://lekcijas.va.lv/lekcijas_request.php'
        form_data = {'nodala': 'KI', 'kurss': str(courseYear), 'gads': str(
            year), 'menesis': str(month), 'c_dala': ''}

        try:
            rq = requests.post(url, data=form_data)
            rq.raise_for_status()
        except:
            raise ScheduleException(rq.status_code)

        html = rq.text

        soup = BeautifulSoup(html, 'html.parser')
        schedule = Schedule()

        days = soup.find_all("td", {"class": "datums"})

        for day in days:
            onlineClasses = day.find_all("div", {"class": "laiks_3"})

            if (len(onlineClasses) > 0):
                day = day.div.contents[0]

                for n in range(len(onlineClasses)):
                    startTime = onlineClasses[n].contents[0].split(' - ')[0]
                    endTime = onlineClasses[n].contents[0].split(' - ')[1]
                    subject = onlineClasses[n].contents[5]

                    event = Event(
                        subject,
                        date(year=year, month=month, day=int(day)),
                        startTime,
                        endTime,
                    )

                    schedule.addEvent(event)
            else:
                continue

        return schedule
