from elevenlabs import set_api_key, generate, Voice, VoiceSettings
set_api_key("8517ffd8094ba4b297208707b9dc3c34")


def dislpay_voice_list():
    from elevenlabs import voices, generate

    voices = voices()
    cpt = 0
    for i in voices:
        print("VOICE " + str(cpt) + " : " + str(i).split("name='")[1].split("'")[0])
        cpt += 1

def audioTest():

    audio = generate(
      text="Hey I am coming soon with a new voice",
      voice="Bella",
      model="eleven_multilingual_v2"
    )

    return audio

def generateAudio(text):

    audio = generate(
        text=text,
        voice=Voice(
            voice_id='EXAVITQu4vr4xnSDxMaL',
            settings=VoiceSettings(stability=0.2, similarity_boost=0.65, style=0.9, use_speaker_boost=True)
        )
    )

    with open("audio.mp3", "wb") as f:
        f.write(audio)
