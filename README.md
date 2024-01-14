# sms.py
Send SMS from random numbers using Textbelt API

After testing I realized that the free text per day is tied to the IP that made the request

*IF YOU WANT TO STAY ANONYMOUS, MAKE THE REQUEST OVER THE TOR NETWORK*

Example Output

```
❯ python3 sms.py -h
usage: sms.py [-h] [-k KEY] phone message

For your convinience, you can buy an API key at https://textbelt.com/purchase/ and set is as the default key in the code instead of typing it in everytime :)

This script was intended from anonymous SMS messages, so it is recommended that you connect to the TOR network before using this script.

positional arguments:
  phone              Specify phone number (US/Canada Only)
  message            Specify message to send (Max 160 characters)

options:
  -h, --help         show this help message and exit
  -k KEY, --key KEY  Specifiy API key (default: textbelt)

Examples:
    sms.py 1234567890 "you can format the number like this" [your_api_key]
    sms.py 123-456-7890 "or you can format the number like this"
```

