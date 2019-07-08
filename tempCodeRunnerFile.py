import datetime
test_date = datetime.date.today()
print('{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year.'.format(test_date))
