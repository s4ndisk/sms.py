# script imports
import argparse
import time
   
# initialize parser
parser = argparse.ArgumentParser(
    description='For your convinience, you can buy an API key at https://textbelt.com/purchase/ and set is as the default key in the code instead of typing it in everytime :)\n\nThis script was intended from anonymous SMS messages, so it is recommended that you connect to the TOR network before using this script. Traffic was analyzed using wireshark and can be viewed on the github',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog='Examples:\n    sms.py 1234567890 "you can format the number like this" [your_api_key]\n    sms.py 123-456-7890 "or you can format the number like this"' 
)

# adding phone argument
parser.add_argument(
   'phone',
   type=int,
   help = 'Specify phone number (US/Canada Only)'
   )

# adding phone argument
parser.add_argument(
   'message', 
   help = 'Specify message to send (Max 160 characters)'
   )

# adding API key argument
parser.add_argument(
   '-k',
   '--key', 
   default='textbelt', 
   help = 'Specifiy API key (default: textbelt)',
   )

# Read arguments from command line
args = parser.parse_args()

print("sms.py v1 Attempting to send message to:", args.phone)

time.sleep(2)

# verify ammount of characters in the message is within the allowed limit
if (sum(len(line) for line in args.message.splitlines())) > 160:
    print('Your message contains more than 160 characters and cannot be sent! Please condense your message so it is under 160 characters.')
else: 
  None

# the basic setup
import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': args.phone,
  'message': args.message,
  'key': args.key,
})
print(resp.json())