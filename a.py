#this is a sample

import requests
url = "http://ecs-alb-1504531980.us-west-2.elb.amazonaws.com:8502/opensky"
my_response = requests.get(url)
pj_data = my_response.json()
print(pj_data) 
