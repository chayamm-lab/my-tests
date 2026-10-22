message = "K4P9Z2"

def decode_message(message):
    return message[1]

print(f"Record Access Digit 1: {decode_message(message)}")


accounts = {
"neo": {"failed_logins": 1, "location": "HQ", "token": "N3O"},
"trinity": {"failed_logins": 7, "location": "UNKNOWN", "token": "TR7"},
"morpheus": {"failed_logins": 2, "location": "HQ", "token": "M8P"}
}

def find_suspicious_accounts(accounts):
    suspicious_accounts = []
    for username, details in accounts.items():
        if details["failed_logins"] >= 5 and details["location"] == "UNKNOWN":
            suspicious_accounts.append(username)
    return suspicious_accounts

result = find_suspicious_accounts(accounts)

print(result)

print(accounts["trinity"]["token"])

