import sys
import requests

try:
    host = sys.argv[1]; data = ""

except IndexError:
    print(f"Usage: {sys.argv[0]} <https://cfx.re(link)>")
    sys.exit()

try:
    response = requests.get(host)
    headers = response.headers
    for count, header in enumerate(headers):
        if header == "X-Citizenfx-Url":
            data = data + "[{}] | ({}): {}\n".format(count, header, headers[header])
        elif header == "X-Citizenfx-Join-Token":
            data = data + "[{}] | ({}): {}\n".format(count, header, headers[header])
        else:
            data = data + "[{}] | ({}): {}\n".format(count, header, headers[header])

    print(data)

except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema):
    print(f"Host: ({host}) is invalid. Check for typos and make sure the link contains https:// or http:// if it's not a RAW IP")
