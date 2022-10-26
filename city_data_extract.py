# import urllib library
from urllib.request import urlopen
from urllib.request import Request
# import json
import json

# store the URL in url as
# parameter for urlopen
# url = "https://api.github.com"

request = Request("https://www.wedmegood.com/node/v1/footer/get?path=/vendors/mumbai/wedding-photographers")
# request.add_header("Token", "61eb928d999da6.40781096")

status = urlopen(request).status

print(status)
# store the response of URL
# response = urlopen(url)
# response = urlopen(request)

# storing the JSON response
# from url in data
# data_json = json.loads(response.read())

# print the json response
# print(data_json)