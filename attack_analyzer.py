with open('D:/SOC-Lab/attack_log.log', 'r') as file:
    logs = file.readlines()
for log in logs:
    if 'Brute force' in log:
        print('CRITICAL ALERT: Brute force attack detected!')
    elif 'Phishing' in log:
        print('WARNING: Phishing attempt detected!')
    elif 'Suspicious login' in log:
        print('ALERT: Multiple suspicious logins!')
print(f'Total attack logs: {len(logs)}')