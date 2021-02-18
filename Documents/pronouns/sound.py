import gtts
from playsound import playsound
tts = gtts.gTTS("enough")
tts.save("enough.mp3")
playsound("enough.mp3")



