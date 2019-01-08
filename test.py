from googlevoice import Voice

def run():
    voice = Voice()
    voice.login()
    for msg in voice.sms().messages:
        if msg.phoneNumber == "+13145918660":
            msg.mark(0)
            print('marked')

__name__ == '__main__' and run()
