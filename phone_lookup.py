import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def phone_info(number):
    try:
        parsed_number = phonenumbers.parse(number)

        country = geocoder.description_for_number(parsed_number, "en")
        sim_operator = carrier.name_for_number(parsed_number, "en")
        time_zones = timezone.time_zones_for_number(parsed_number)

        print("\n📞 Phone Number Information:")
        print(f"🌍 Country: {country}")
        print(f"📡 Carrier: {sim_operator if sim_operator else 'Unknown'}")
        print(f"⏰ Time Zone: {', '.join(time_zones)}")
    
    except Exception as e:
        print(f"❌ Invalid phone number. Error: {str(e)}")
