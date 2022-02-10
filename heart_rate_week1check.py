print('Heart Rate Program')
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""
age = int(input('What is your age? '))
max_heart_rate_per_minute = 220 - age
max_heart_rate = max_heart_rate_per_minute * .85
min_heart_rate = max_heart_rate_per_minute * .65

print(f'At age {age}, you should maintain your heart rate at between {min_heart_rate:.0f} beats per minute \
and {max_heart_rate:.2f} beats per minute during a 20-minute exercise.')

print()
