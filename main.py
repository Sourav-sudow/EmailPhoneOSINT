from modules.phone_lookup import phone_info
from modules.email_lookup import email_info

def main():
    print("🔍 Email & Phone Number OSINT Tool")
    
    while True:
        print("\n1️⃣ Phone Number Lookup")
        print("2️⃣ Email Lookup")
        print("3️⃣ Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        
        if choice == "1":
            phone_number = input("📞 Enter phone number (with country code, e.g., +91XXXXXXXXXX): ").strip()
            if phone_number:
                phone_info(phone_number)
            else:
                print("❌ Invalid input. Please enter a valid phone number.")
        
        elif choice == "2":
            email = input("📧 Enter email address: ").strip()
            if email:
                email_info(email)
            else:
                print("❌ Invalid input. Please enter a valid email address.")

        elif choice == "3":
            print("👋 Exiting the tool. Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
