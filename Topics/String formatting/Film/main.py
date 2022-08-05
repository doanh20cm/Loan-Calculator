import datetime
_dir, director, year = input(), input(), int(input())
print(f"{_dir} (dir. {director}) {'came' if year < datetime.datetime.now().year else 'come'} out in {year}")