import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number = input("Enter Your No. with +__: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
carrier_name = carrier.name_for_number(phone, "en")
region = geocoder.description_for_number(phone, "en")
print(phone)
print(time)
print(carrier_name)
print(region)
