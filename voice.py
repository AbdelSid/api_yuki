from elevenlabs import set_api_key, generate, Voice, VoiceSettings
set_api_key("8517ffd8094ba4b297208707b9dc3c34")
set_api_key("1c50566023c708a7611405284a8ca330")

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

def generateAudio(text, nameFile="audio"):

    if len(text) > 555:
        model = "eleven_turbo_v2"
    else:
        model = "eleven_multilingual_v2"

    audio = generate(
        text=text,
        voice=Voice(
            voice_id='EXAVITQu4vr4xnSDxMaL',
            voice_settings=VoiceSettings(stability=0.4, similarity_boost=0.8, style=0.8, use_speaker_boost=True),
            model=model
        )
    )

    with open(f"{nameFile}.mp3", "wb") as f:
        f.write(audio)

