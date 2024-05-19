"""
Evil Eval is a simple script designed to test an input with various eval payloads.
The primary goal is to identify which payload the eval function is vulnerable.

Author: Potion
"""
import argparse
import requests

HEADER = {
  'Content-Type': 'text/plain'
}

def print_titlescreen():
  print(r"""
  ___________     .__.__    ___________             .__   
  \_   _____/__  _|__|  |   \_   _____/__  _______  |  |  
  |    __)_\  \/ /  |  |    |    __)_\  \/ /\__  \ |  |  
  |        \\   /|  |  |__  |        \\   /  / __ \|  |__
  /_______  / \_/ |__|____/ /_______  / \_/  (____  /____/
          \/                        \/            \/      
  """)

def print_response(response, error_message):
  if not error_message:
    print(response.text)
  elif error_message not in response.text and response.text != '{}':
    print(response.text)

def send_payloads(url, error_message, json_key=None):
  print('[+] Starting payload fuzzing')
  with open('payloads.txt', 'r') as payloads:
    for payload in payloads:
      if payload[0] == '#' or payload[0] == '\n':
        continue
      else:
        current_payload = payload.strip()
        if json_key:
          json_data = {json_key: current_payload}
          response = requests.post(url=url, json=json_data, headers=HEADER)
        else:
          data = current_payload
          response = requests.post(url=url, data=data, headers=HEADER)
        print_response(response, error_message)

def main():
  parser = argparse.ArgumentParser(
    prog        = 'Evil Eval',
    description = 'Evil Eval is a simple script designed to test an input with various eval payloads.',
    epilog      = 'The primary goal is to identify which payload the eval function is vulnerable.'
  )
  
  parser.add_argument('-u', '--url', metavar='', help='The URL you are attacking.', required=True)
  parser.add_argument('-e', '--error', metavar='', help='Set the error message to filter unsuccessful payloads.')
  parser.add_argument('-j', '--json', metavar='', help='Set the JSON key if payload is JSON.')
  
  args = parser.parse_args()
  url, error_message, json_key = args.url, args.error, args.json
  if json_key:
    HEADER['Content-Type'] = 'application/json'

  print_titlescreen()
  send_payloads(url, error_message, json_key)

if __name__ == '__main__':
  main()
