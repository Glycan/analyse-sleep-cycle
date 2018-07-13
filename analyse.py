from datetime import datetime, timedelta
import json
from collections import Counter, defaultdict
from pprint import pprint 


def classify(start_minutes, duration_hours):
	if start_minutes < 3.25 and duration_hours > 8: #before 11:15
		return "good"
	elif start_minutes < 3.75 and duration_hours > 7.5: #before 11:45
		return "ok"
	else:
		return "meh"

def analyse(data):
	all_days = []
	weeks = defaultdict(lambda :Counter())
	months = defaultdict(lambda :Counter())
	for day in data:
		start = datetime.strptime(day["start"], "%Y-%m-%dT%H:%M:%S")
		stop = datetime.strptime(day["stop"], "%Y-%m-%dT%H:%M:%S")
		if start.hour < 20:	# must have gone to bed past midnight
			start_hours = 4 + start.hour + start.minute / 60.0
			start = start - timedelta(1)
		else:
			start_minutes = start.hour - 20  + start.minute / 60.0
		duration_hours = (stop - start).total_seconds() / 3600
		classification = classify(start_minutes, duration_hours)
		all_days.append([start.strftime("%Y-%m-%d"), classification])
		months[start.strftime("%Y-%m")].update([classification])
		weeks[
			start.strftime("%Y-%m week #") + str(start.day / 7)
			].update([classification])
	return all_days, months, weeks


with open("sleep_data.json") as f:
	data = json.load(f)
	all_days, months, weeks = analyse(data)
	print "months\n--------"
	for month, sleep in sorted(months.items()):
		print "{}: {} good, {} ok, {} meh".format(
			month, sleep["good"], sleep["ok"], sleep["meh"]
		)
	print "\nweeks\n---------"
	for week, sleep in sorted(weeks.items()):
		print "{}: {} good, {} ok, {} meh".format(
			week, sleep["good"], sleep["ok"], sleep["meh"]
			)
