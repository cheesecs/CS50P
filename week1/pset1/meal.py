def main():
    user_input = input('What time is it?')
    meal_time = convert(user_input)
    if 7 <= meal_time <= 8:
        print('breakfast time')
    elif 12 <= meal_time <= 13:
        print('lunch time')
    elif 18 <= meal_time <= 19:
        print('dinner time')

def convert(time):
    hours, minutes = time.split(':')
    now_time = float(hours) + (float(minutes) / 60)
    return now_time

if __name__ == "__main__":
    main()