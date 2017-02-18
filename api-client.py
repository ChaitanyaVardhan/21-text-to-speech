import requests

SERVER_IP_ADDRESS = '[::1]'

# send text to the endpoint
def send_text(text):
    # tell the user what text they are sending
    print('You sent {0}'.format(text))

    # endpoint url and request
    tts_url = 'http://' + SERVER_IP_ADDRESS + ':5000/tts?text={0}'
    speech = requests.get(url=tts_url.format(text))

    if speech.status_code != 200:
        raise Exception('Server produced a %d error' % speech.status_code)

    # save the received audio file to disk
    speech_output = open('speech.wav', 'wb')
    speech_output.write(speech.content)
    speech_output.close()

#Read the text to speechify from the CLI
if __name__ == '__main__':
    from sys import argv
    send_text(argv[1])
