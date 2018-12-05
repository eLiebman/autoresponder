import time
from googlevoice import Voice


def run():
    voice = Voice()
    voice.login()    # login will prompt for email/password in the command line
    response = "I'm testing a python app that sends texts through google voice. Text me back!"
    while True:
        # get messages
        for msg in voice.sms().messages:
            if not msg.isRead:
                voice.send_sms(msg.phoneNumber, response)
                msg.mark(1)
        time.sleep(30)

__name__ == '__main__' and run()
