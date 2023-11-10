from playsound import playsound

from elevenlabs import set_api_key
set_api_key("8517ffd8094ba4b297208707b9dc3c34")


def dislpay_voice_list():
    from elevenlabs import voices, generate

    voices = voices()
    cpt = 0
    for i in voices:
        print("VOICE " + str(cpt) + " : " + str(i).split("name='")[1].split("'")[0])
        cpt += 1


from elevenlabs import generate

def audioTest():

    audio = generate(
      text="Hey I am coming soon with a new voice",
      voice="Bella",
      model="eleven_multilingual_v2"
    )

    return audio

