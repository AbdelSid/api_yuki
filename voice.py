from playsound import playsound


def dislpay_voice_list():
    from elevenlabs import voices, generate

    voices = voices()
    cpt = 0
    for i in voices:
        print("VOICE " + str(cpt) + " : " + str(i).split("name='")[1].split("'")[0])
        cpt += 1


from elevenlabs import generate

audio = generate(
  text="Hey I am coming soon with a new voice",
  voice="Bella",
  model="eleven_multilingual_v2"
)

with open("audio.mp3", "wb") as f:
    f.write(audio)

