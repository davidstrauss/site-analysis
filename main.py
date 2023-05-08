import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# open the file containing the domain names
with open("domains.txt", "r") as file:
    # read the domain names into a list
    domains = [line.strip() for line in file]

# define a dictionary to store the header counts
header_counts = {}

# loop through the domain names
for domain in domains:
    if domain.startswith('#'):
        continue

    print(domain)

    try:
        # make an HTTPS request to the domain and get the response headers
        response = requests.get("https://" + domain, verify=False, timeout=2)
    except Exception as e:
        print(e)
        continue
    headers = response.headers

    # loop through the headers and update the header counts
    for header in headers:
        if header not in header_counts:
            header_counts[header] = 1
        else:
            header_counts[header] += 1

# print the header counts
for header, count in header_counts.items():
    print(f"{header}: {count}")
