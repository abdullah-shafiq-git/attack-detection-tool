import logging
logging.basicConfig(filename='D:/SOC-Lab/attack_log.log', level=logging.INFO)
logging.info('Phishing email sent to user1 at 2025-08-26 12:00 PM')
logging.error('Brute force attack on IP 192.168.1.200, 50 attempts')
logging.warning('Unusual data transfer at 12:15 PM')
for i in range(3):
    logging.info(f'Suspicious login from IP 10.0.0.{i} at 12:20 PM')