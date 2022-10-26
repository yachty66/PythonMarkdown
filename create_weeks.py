import datetime
from datetime import timedelta, date


def cmd():
    start_date = input("Please enter start date in format YYYY-MM-DD: ")
    end_date = input("Please enter end date in format YYYY-MM-DD: ")
    path = input("Please enter path to file /Users/YourFolder/YourFile.md: ")
    # try except for function
    try:
        creator(start_date, end_date, path)
    except:
        print("Check your input")


def weeks_for_year(year):
    last_week = date(year, 12, 28)
    return last_week.isocalendar()[1]


def onDay(date, day):
    """
    Returns the date of the next given weekday after
    the given date. For example, the date of next Monday.

    NB: if it IS the day we're looking for, this returns 0.
    consider then doing onDay(foo, day + 1).
    """
    days = (day - date.weekday() + 7) % 7
    return date + datetime.timedelta(days=days)


def creator(start_date, end_date, path):
    """
    Args:
        start_date (string): YYYY-MM-DD
        end_date (string)
        path (string)

    Returns:
        [type]: [description]
    """
    list_with_weeks = []
    week_num = datetime.datetime.strptime(start_date, "%Y-%m-%d").isocalendar()[1]
    list_with_weeks.append(week_num)
    monday1 = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    monday1 = monday1 - timedelta(days=monday1.weekday())
    monday2 = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    monday2 = monday2 - timedelta(days=monday2.weekday())
    weeks = (monday2 - monday1).days / 7
    number_weeks_for_year = weeks_for_year(
        int(datetime.datetime.strptime(start_date, "%Y-%m-%d").date().year)
    )
    for i in range(int(weeks)):
        if list_with_weeks[-1] != number_weeks_for_year:
            list_with_weeks.append(list_with_weeks[-1] + 1)
        else:
            list_with_weeks.append(1)

    with open(path, "a") as f:
        for i in list_with_weeks:
            f.write("# Week " + str(i) + "\n")


if __name__ == "__main__":
    cmd()
