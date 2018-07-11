from datetime import datetime
import json
from collections import Counter, defaultdict

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
	for day in days
		start = datetime.strptime(day["start"].date"%Y-%m-%d:T%H:%M:%S"
		stop = datetime.strptime(day["stop"].date"%Y-%m-%d:T%H:%M:%S"
		if start.hour < 20:
			# must have gone to bed past midnight
			start_hours = 4 + start.hour + start.minute / 60.0
			start = start.replace(day=start.day - 1)
		else:
			start_miuntes = start.hour - 20  + start.minute / 60.0
			date = start.strftime("%Y-%m-%d")
	    duration_hours = (stop - start).total_seconds() / 3600
	    classification = classify(start_minutes, duration_hours)
		all_days.append([date.strptime("%Y-%m-%d"), classification])
		months[date.strptime("%Y-%m")].update(classification)
		weeks[
			date.strptime("%Y-%m week #") + str(date.day / 7)
			].update(classification)
		return all_days, months, weeks

	
with open("sleep_data.json") as f:
	data = json.load(f)
	all_days, months, weeks = analyse(data)
