import time
from googlevoice import Voice


def run():
    received_messages = []
    delay_time = 7 # time in seconds to wait between message checks
    response_message = "Hello Human! \n You will now receive the Zine Prologue. When finished, you may proceed to enter the Zine\n It works best with headphones. \n https://drive.google.com/file/d/1AKW5qbpcqbbVzaICtkejU0DBrW9HlIdb/view?usp=sharing" # your autoreply message
    voice = Voice()
    voice.login()    # login will prompt for email/password in the command line
    print('Running...\nPress ctrl C to quit')

    while True:
        # get messages
        try:
            for msg in voice.sms().messages:
                if not msg.isRead:
                    # reply
                    voice.send_sms(msg.phoneNumber, response_message)
                    msg.mark(1)
            time.sleep(delay_time)
        except:
            continue

__name__ == '__main__' and run()
