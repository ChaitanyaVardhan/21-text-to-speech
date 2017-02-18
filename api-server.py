from subprocess import call
from uuid import uuid4

from flask import Flask
from flask import request
from flask import send_from_directory

app = Flask(__name__)

@app.route('/tts')
def tts():
    #text sent by client through curl or browser
    text = str(request.args.get('text'))

    #create a filename
    file = str(uuid4()) + '.wav'
    
    # run TTS engine
    call(['espeak', '-w', '/tmp/' + file, text])

    # send rendered audio back to client
    return send_from_directory(
        '/tmp',
        file,
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(host='::')
