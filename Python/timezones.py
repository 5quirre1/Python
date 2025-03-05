from datetime import datetime
import os
try:
    import pytz
except ImportError:
   os.system("pip install pytz") 
   import pytz

timezones = [
    "America/New_York",        # New York
    "Europe/London",           # London
    "Asia/Tokyo",              # Tokyo
    "Australia/Sydney",        # Sydney
    "Africa/Nairobi",          # Nairobi
    "America/Los_Angeles",     # Los Angeles
    "Europe/Paris",            # Paris
    "Asia/Kolkata",            # Kolkata
    "America/Chicago",         # Chicago
    "Asia/Seoul",              # Seoul
    "Europe/Berlin",           # Berlin
    "Asia/Singapore",          # Singapore
    "America/Mexico_City",     # Mexico City
    "Asia/Dubai",              # Dubai
    "Europe/Rome",             # Rome
    "Africa/Cairo",            # Cairo
    "Asia/Hong_Kong",          # Hong Kong
    "America/Toronto",         # Toronto
    "Europe/Amsterdam",        # Amsterdam
    "Asia/Kuala_Lumpur",       # Kuala Lumpur
    "Pacific/Auckland",        # Auckland
    "America/Denver",          # Denver
    "Africa/Johannesburg",     # Johannesburg
    "Asia/Bangkok",            # Bangkok
    "America/Sao_Paulo",       # Sao Paulo
    "Europe/Madrid",           # Madrid
    "Asia/Jakarta",            # Jakarta
    "America/Vancouver",       # Vancouver
    "Europe/Zurich",           # Zurich
]


def show_time_in_timezones(timezones):
    current_utc_time = datetime.now(pytz.utc)

    print("Current Time in Different Time Zones:\n")
    for zone in timezones:
        local_timezone = pytz.timezone(zone)
        local_time = current_utc_time.astimezone(local_timezone)

        formatted_time = local_time.strftime("%A, %B %d, %Y - %I:%M:%S %p %Z")

        print(f"{zone}: {formatted_time}\n")

if __name__ == "__main__":
    show_time_in_timezones(timezones)
