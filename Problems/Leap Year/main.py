# put your python code here
year = int(input())

leap = bool(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)

print("Leap" if leap else "Ordinary")
