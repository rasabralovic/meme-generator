# Meme Generator

Preprosta spletna aplikacija za izdelavo klasičnih memov. Uporabnik naloži sliko, vpiše zgornje in spodnje besedilo, aplikacija pa na sliko nariše besedilo (belo s črno obrobo) in ustvarjeni meme prikaže v brskalniku.

Aplikacija je dockerizirana, zato za zagon potrebujete samo Docker.

## Uporabljene tehnologije

- **Python 3.12** – programski jezik
- **Flask** – spletno ogrodje (sprejem zahtev, prikaz strani, prejem obrazca)
- **Pillow** – obdelava slik (risanje besedila na sliko)
- **HTML + Jinja** – uporabniški vmesnik in predloge
- **Docker** – zapakiranje aplikacije z vsem okoljem v sliko in zagon v kontejnerju

## Potek obdelave

1. **Prejem datoteke** – brskalnik pošlje sliko in obe besedili z zahtevo POST.
2. **Obdelava** – Pillow odpre sliko, določi velikost pisave glede na velikost slike in nariše zgornje in spodnje besedilo na sredino ob robovih slike.
3. **Vrnitev slike** – slika se shrani v pomnilnik kot PNG in se prikaže v brskalniku namesto privzete slike.

## Struktura projekta

```
meme-generator/
├── app.py                 # aplikacija Flask
├── DejaVuSans-Bold.ttf    # pisava za besedilo
├── requirements.txt       # knjižnice Python
├── Dockerfile             # navodila za gradnjo slike
├── .dockerignore          # datoteke, ki jih Docker prezre
├── static/
│   └── default_image.jpg  # privzeta slika
└── templates/
    └── index.html         # spletna stran z obrazcem
```

## Zagon z Dockerjem

Predpogoj: nameščen [Docker](https://docs.docker.com/get-docker/).

1. Prenesite repozitorij:
   ```
   git clone https://github.com/TVOJ_NALOG/meme-generator.git
   cd meme-generator
   ```

2. Zgradite sliko:
   ```
   docker build -t meme-generator .
   ```

3. Zaženite kontejner:
   ```
   docker run -p 5000:5000 meme-generator
   ```

4. V brskalniku odprite [http://localhost:5000](http://localhost:5000).

Kontejner ustavite s `Ctrl+C` ali v drugem terminalu z:
```
docker ps
docker stop <CONTAINER ID>
```

## Uporaba

1. V razdelku **Input tab** izberite sliko.
2. Vpišite zgornje (**Top text**) in spodnje besedilo (**Bottom text**). Obe polji sta neobvezni.
3. Kliknite **submit** – ustvarjeni meme se prikaže na levi strani.
