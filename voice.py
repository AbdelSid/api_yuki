from elevenlabs import set_api_key, generate, Voice, VoiceSettings
#set_api_key("8517ffd8094ba4b297208707b9dc3c34")
set_api_key("2de8729667e52cdb2e7494f1a53daf4a")
import requests

headers = {
    "xi-api-key": "2de8729667e52cdb2e7494f1a53daf4a",
}
#print(requests.get("https://api.elevenlabs.io/v1/user/subscription", headers=headers).json())

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

    print("Start Generate")

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




