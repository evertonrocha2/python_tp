def min_to_hours(mins):
    hours = mins // 60
    minutes = mins % 60
    return hours, minutes

def hour_to_min(hours, mins):
    return hours * 60 + mins

if __name__ == "__main__":
    mins = int(input("Enter minutes: "))
    hours, minutes = min_to_hours(mins)
    print(mins, "minutes is equal to", hours, "hours and", minutes, "minutes")

    hours = int(input("Enter hours:"))
    minutes = int(input("Enter minutes:"))
    print(hours, "hours and ", minutes, "minutes is equal to", hour_to_min(hours, minutes), "minutes")