# script imports
import argparse

# initialize parser
parser = argparse.ArgumentParser()

# adding phone argument
parser.add_argument(
   'phone', 
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
   help = 'Specifiy API key',
   )

# Read arguments from command line
args = parser.parse_args()

# the basic setup
import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': args.phone,
  'message': args.message,
  'key': args.key,
})
print(resp.json())