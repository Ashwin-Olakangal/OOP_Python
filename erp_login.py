import requests

url = "https://erp.bits-pilani.ac.in:4431/psp/hcsprod/?cmd=login&languageCd=ENG"

header_data = {
    "User-Agent": "<Go to erp and inspect element while logging in to find this field>"
}

payload = {
    "timezoneOffset": -330,
    "userid": "<ENTER USER ID>",
    "pwd": "<ENTER PASSWORD>",
}

# Making a post request to erp
r = requests.post(url, data=payload, headers=header_data, timeout=5)

print(r.content)
# you can find fields only availabe once logged in, such as favorite (ctrl + f),
# to verify that sucessful login has taken place

print("The program was run")

