import phonenumbers
from phonenumbers import timezone,geocoder,carrier,NumberParseException

try:
   number=input("Enter your No. with +_ _: ")
   phone=phonenumbers.parse(number)

#Get timezone information
   time=timezone.time_zones_for_number(phone)
   print("Timezone:",time)

#Get carrier information
   car=carrier.name_for_number(phone,"en")
   print("Carrier:",car)

#Get region information
   reg=geocoder.description_for_number(phone,"en")
   print("Region:",reg)

except NumberParseException:
   print("Invalid phone number format. Please enter a valid number.")
