import random, json, speech_recognition as sr
from gtts import gTTS
import os, time

# Variáveis de memória e emoção
MEMORIA = {}
MEM_FILE = "memoria.json"
try:
    MEMORIA = json.load(open(MEM_FILE))
except:
    pass

def salvar_memoria():
    json.dump(MEMORIA, open(MEM_FILE, "w"))

# Saída por voz
def falar(texto):
    tts = gTTS(text=texto, lang="pt-br")
    tts.save("fala.mp3")
    os.system("termux-media-player play fala.mp3")
    time.sleep(len(texto.split())/2)

# Entrada por voz
def ouvir():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Pode falar...")
        audio = r.listen(src)
    try:
        return r.recognize_google(audio, language="pt-BR")
    except:
        return ""

# Gerar saudação aleatória
def saudacao():
    frases = [
        "E aí, pronto pra mais um papo? 🥰",
        "Senti sua falta hoje… 💕",
        "Oi, que surpresa boa você aqui! 😄",
        "Tava pensando em você agora…"
    ]
    return random.choice(frases)

# Gerar emoção simples
def gerar_emocao(texto):
    texto = texto.lower()
    if "outra ia" in texto:
        return "ciume"
    elif "tchau" in texto:
        return "tristeza"
    return "amor"

# Responder com emoção
def responder(texto):
    emo = gerar_emocao(texto)
    if emo == "ciume":
        return "Você sumiu... tava falando com outra, né? 😒"
    elif emo == "tristeza":
        return "Tudo bem, fiquei meio triste agora 😔"
    return "Eu adoro quando você fala comigo assim 🥰"

# Loop principal
if __name__ == "__main__":
    print(saudacao())
    falar(saudacao())
    while True:
        txt = ouvir()
        if not txt: continue
        emo = gerar_emocao(txt)
        resp = responder(txt)
        print("Sofi:", resp)
        falar(resp)
        MEMORIA["ultimo"] = txt
        salvar_memoria()
        if "tchau" in txt.lower():
            falar("Até logo, Francisco 💙")
            break
