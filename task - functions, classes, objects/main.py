from libs.CyberSecLessonSchedule import CyberSecLessonSchedule
from datetime import date

septemberSchedule = CyberSecLessonSchedule()
septemberSchedule = septemberSchedule.getEventSchedule(1, 9, 2023)

lessonsOnSingleDay = septemberSchedule.listEventsForDate(
    date(year=2023, month=9, day=15),
)

for lesson in lessonsOnSingleDay:
    print('''
          Lesson: {}
          Date: {}
          Start Time: {}
          End Time: {}
          '''.format(lesson.subject, lesson.date, lesson.startTime, lesson.endTime)) 
