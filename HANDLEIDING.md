# 🎬 Creator Studio voor Claude — Handleiding

> 🍎🪟 **Werkt op Mac en Windows.** Stappen die verschillen zijn aangeduid met **🍎 Mac** en **🪟 Windows**. De Windows-stappen zijn nieuw in v1.1. Klopt iets niet met wat je ziet? Laat het ons weten.

**Je eigen creatieve team in Claude.** Na deze installatie werkt Claude voor jou als:

| Rol | Wat Claude doet |
|---|---|
| 🎬 **Video-editor** | Monteert je video's in je eigen CapCut-project: eerst een ruwe montage, en pas na jouw goedkeuring ondertitels, animaties en effecten. |
| 🎨 **Creative designer** | Thumbnails, carrousels, posters, advertenties en social graphics in jouw stijl. |
| ✨ **Motion designer** | Geanimeerde tekst, geanimeerde cijfers, logo-animaties en AI-effecten. |
| 📑 **Presentatie-designer** | Sponsordecks, pitch decks en mediakits. |
| 📊 **Data-designer** | Grafieken en infographics van je cijfers. |
| 🔍 **Contentstrateeg** | Analyseert je Instagram en TikTok: wat werkt, welke hooks, trends en ideeën, plus een plan voor volgende week. |

Alles vertrekt van **jouw eigen socials**. Claude bekijkt wat je post, hoe het eruitziet en wat goed scoort, en werkt in die stijl verder. Brand guidelines heb je niet nodig.

🇬🇧 English version: [README.md](README.md)

---

## Wat heb je nodig

- [ ] Een **Claude Pro- of Max-abonnement**. Computer use (Claude die CapCut bedient) en geplande taken werken niet op het gratis plan.
- [ ] Een **Mac** of een **Windows 10/11**-pc.
- [ ] **CapCut Desktop**, als je Claude wil laten monteren.
- [ ] Je **Instagram- en/of TikTok-account**. Voor statistieken heb je een creator- of zakelijk account nodig.
- [ ] Ongeveer **30 minuten**.

---

## Deel A: Claude klaarzetten

### Stap 1: Installeer de Claude desktop-app
1. Ga naar **claude.com/download** en download de app voor je computer.
2. Installeer de app en log in met je Claude-account.
3. **Belangrijk:** Claude kan alleen aan je mappen, CapCut en je browser als de desktop-app **openstaat** en je computer **niet in slaap** is.

### Stap 2: Zet de juiste functies aan
Open in de desktop-app de **Instellingen** (Settings):
1. Bij **Capabilities**: zet **Code execution and file creation** aan. Skills werken niet zonder.
2. Zet **Computer use** aan. Je vindt het bij **Capabilities**, of bij **System** onder *This computer*. Zo kan Claude CapCut bedienen.

---

## Deel B: Het pakket installeren

### Stap 3: Download en pak uit
Download het pakket (de ZIP van de GitHub-pagina) en pak het uit.

### Stap 4: Upload de 6 skills
1. Ga in Claude naar **Customize → Skills**.
2. Klik op **+** → **Create skill** → **Upload a skill**.
3. Upload een voor een de 6 ZIP-bestanden uit de map **`install/`**:
   - `studio-video-editor.zip`
   - `studio-visual-director.zip`
   - `studio-motion-design.zip`
   - `studio-presentation-design.zip`
   - `studio-data-visualization.zip`
   - `studio-content-scan.zip`
4. Controleer dat alle 6 **aan** staan.

> ⚠️ Upload de ZIP-bestanden, niet de mappen uit `skills/`. Hernoem ze niet.

---

## Deel C: Je werkmap op je computer

### Stap 5: Maak je Creator Studio-map
1. Kopieer de map **`workspace-template`** uit het pakket naar **Documenten** (of iCloud Drive) en noem ze **`Creator Studio`**.
2. Wat erin zit:
   - `01 Designs`, `02 Presentations`, `03 Motion` en `04 Content reports`: hier bewaart Claude wat hij voor je maakt.
   - `05 My logo & fonts`: optioneel. Zet hier je logo (PNG/SVG) en fonts in als je die hebt.
   - `EDITING-PLAYBOOK.md`: je montagevoorkeuren. Laat het gerust leeg, Claude vult het aan na je eerste goedgekeurde video.
   - `Tools/whisper`: optioneel, voor transcriptie van je beelden (zie stap 9b).

### Stap 6: Zoek de paden van je mappen op
Die heb je nodig in stap 7. Je hebt drie paden nodig.
- **🍎 Mac:** klik in Finder **met de rechtermuisknop** op een map, **houd de Option-toets (⌥) ingedrukt** en kies **"Kopieer … als padnaam"**.
- **🪟 Windows:** klik in Verkenner **met de rechtermuisknop** op een map en kies **"Als pad kopiëren"** (Windows 10: houd **Shift** ingedrukt bij het rechtsklikken). Haal de aanhalingstekens weg als je plakt.

| Map | 🍎 Voorbeeld Mac | 🪟 Voorbeeld Windows |
|---|---|---|
| Je Creator Studio-map | `/Users/jouwnaam/Documents/Creator Studio` | `C:\Users\jouwnaam\Documents\Creator Studio` |
| Je ruwe beelden | `/Users/jouwnaam/Downloads` | `C:\Users\jouwnaam\Downloads` |
| Je CapCut-projecten | `/Users/jouwnaam/Movies/CapCut` | `C:\Users\jouwnaam\AppData\Local\CapCut` |

> 💡 Niet zeker waar CapCut je projecten bewaart? Open in CapCut de **Instellingen** en kijk bij de **locatie van concepten** (drafts). Dat is de map. Op Windows is `AppData` verborgen: plak het pad in de adresbalk van Verkenner om de map te openen.

---

## Deel D: Je Claude Project

### Stap 7: Maak het Project en vul je profiel in
1. Maak in Claude een nieuw **Project** aan, bv. "Mijn Creative Studio".
2. Open **`project-instructions.md`** in een teksteditor (🍎 TextEdit / 🪟 Kladblok).
3. Vul bovenaan het **CREATOR PROFILE** in. Alles tussen `[ ]` vervang je door je eigen gegevens: naam, accounts, taal, regio, je vaste formats, je tone of voice, montageprogramma en de drie paden uit stap 6.
4. Kopieer **het hele bestand** en plak het bij de **instructies** van het Project.

> 💡 Hoe beter je je formats en tone of voice beschrijft, hoe beter Claude je stijl treft.

---

## Deel E: Claude toegang geven tot je computer

### Stap 8: Koppel je mappen aan het Project
Open het Project in de **desktop-app** en voeg bij de gekoppelde mappen (connected folders) deze drie toe:
1. Je **Creator Studio**-map
2. Je map met **ruwe beelden** (bv. Downloads)
3. Je **CapCut**-map (uit stap 6)

- Claude ziet **alleen** de mappen die je koppelt, en alleen zolang de desktop-app openstaat.
- Vraagt Claude later zelf toegang tot een map? Dan krijg je een melding om goed te keuren.
- Wil je een map niet meer delen? Verwijder ze in hetzelfde menu.

### Stap 9: Geef de toestemmingen
**🍎 Mac:** de eerste keer dat Claude je scherm gebruikt (bv. bij je eerste montage), vraagt macOS om twee toestemmingen:
- **Toegankelijkheid** (Accessibility): zodat Claude kan klikken, typen en scrollen.
- **Schermopname** (Screen Recording): zodat Claude kan zien wat er op je scherm staat.

Sta beide toe via **Systeeminstellingen → Privacy en beveiliging**, zet de schakelaar bij **Claude** aan en herstart de app als macOS daarom vraagt.

**🪟 Windows:** je hoeft geen extra systeeminstellingen aan te passen. Vraagt Windows bij de installatie van de desktop-app om beheerdersrechten, sta dat dan toe.

**Allebei:** daarna vraagt Claude **per app** toestemming, bv. voor CapCut. Sta die toe. Claude werkt op de achtergrond en neemt nooit je hele scherm over.

---

### Stap 9b (optioneel): Whisper installeren voor transcriptie
Met Whisper leest Claude **wat er gezegd wordt** in je beelden, nog voor hij monteert. Zo vindt hij de beste quotes, hooks en grappige momenten op inhoud. Alles blijft lokaal op je computer.

**🍎 Mac**
1. Open **Terminal** (Cmd + spatie → typ "Terminal").
2. Typ `cd ` (met een spatie erna), sleep de map **`Creator Studio/Tools/whisper`** in het Terminal-venster en druk op Enter.
3. Typ `pip3 install faster-whisper` en druk op Enter.
4. Typ `python3 transcribe.py --download-only` en druk op Enter. Dit downloadt het model (± 1,6 GB) in de map `models`. Wacht tot je **"ready"** ziet. Weinig plaats of een oudere computer? Gebruik dan `--model small` (± 0,5 GB).

**🪟 Windows**
1. Installeer **Python 3** via **python.org** → Downloads. Vink in het installatieprogramma **"Add python.exe to PATH"** aan.
2. Open de map **`Creator Studio\Tools\whisper`** in Verkenner, klik in de adresbalk, typ `powershell` en druk op Enter. PowerShell opent in die map.
3. Typ `py -m pip install faster-whisper` en druk op Enter.
4. Typ `py transcribe.py --download-only` en druk op Enter. Wacht tot je **"ready"** ziet (± 1,6 GB; voeg `--model small` toe voor ± 0,5 GB).
5. Optioneel, sneller: `winget install Gyan.FFmpeg`.

**Allebei:** vul in je Creator Profile bij **WHISPER FOLDER** het pad naar `Tools/whisper` in.

Vanaf nu transcribeert de video-editor automatisch alle beelden met spraak voor Versie 1. De transcripties komen in een map `_Transcripties` naast je beelden. Sla je deze stap over, dan werkt de editor gewoon op beeld.

## Deel F: Je socials koppelen

### Stap 10: Log in in de ingebouwde browser
De desktop-app heeft een **ingebouwde browser**. Open ze en log **zelf** in op:
- **Instagram** (instagram.com)
- **TikTok** (tiktok.com, en open daarna ook TikTok Studio)
- **YouTube Studio**, als je YouTube gebruikt

Je blijft ingelogd, dus dit doe je maar één keer. Daarna kan Claude je posts, video's en statistieken **lezen**.

> 🔒 Claude vult nooit wachtwoorden in. Hij post, liket, reageert en stuurt geen DM's in jouw naam. Hij leest alleen.

### Stap 11 (optioneel): Metricool
Gebruik je al **Metricool**? Koppel het dan in Claude bij de **connectors** en zet je Metricool brand ID in het Creator Profile. Zo krijgt Claude je cijfers sneller en over een langere periode. Gebruik je het niet? Sla deze stap over.

---

## Deel G: Testen

### Stap 12: Probeer elke rol
Typ deze vragen in je Project. Elke rol start met een korte briefing.

| Rol | Probeer |
|---|---|
| 🔍 Contentstrateeg | "Analyseer mijn content van deze week en maak een plan voor volgende week." |
| 🎨 Creative designer | "Maak een carrousel van 5 slides over [onderwerp]." of "Maak een thumbnail voor mijn nieuwste video." |
| ✨ Motion designer | "Maak een geanimeerde titel voor mijn volgende video." |
| 📑 Presentatie-designer | "Maak een mediakit om naar merken te sturen." |
| 📊 Data-designer | "Zet mijn cijfers van de laatste 30 dagen in een overzichtelijke infographic." |
| 🎬 Video-editor | Zie hieronder ⬇️ |

### Zo laat je Claude een video monteren
1. Maak in **CapCut** een nieuw project aan en **importeer je clips**. Geef het project een duidelijke naam, bv. `Nieuwe video`.
2. Vraag in je Claude Project: **"Monteer mijn nieuwe video."**
3. Claude stelt de montagebriefing: projectnaam, soort video, platform, lengte, stijl, muziek, extra instructies.
4. Claude opent CapCut en maakt **Versie 1**: alleen de montage, zonder ondertitels of effecten.
5. Je bekijkt V1 **in CapCut** en geeft feedback, of je zegt duidelijk "V1 is goedgekeurd". Elke feedbackronde wordt een nieuwe tijdlijn (V2, V3 …) in hetzelfde project, zodat eerdere versies blijven staan.
6. Pas na je goedkeuring doet Claude de afwerking: ondertitels (het Whisper-`.srt`-bestand, rechtstreeks in CapCut geïmporteerd, als er gesproken wordt), animaties, muziek, effecten.
7. Claude **exporteert niets** tot je erom vraagt.

> 💡 Laat de desktop-app open en houd je computer wakker. Claude werkt op de achtergrond en neemt nooit je hele scherm over. Klik alleen niet zelf in CapCut terwijl Claude aan het monteren is.

---

## Deel H (optioneel): Wekelijkse scan op automatische piloot

Vraag in je Project: *"Maak een geplande taak voor mijn wekelijkse contentscan."* Plak er de prompt uit **`scheduled-tasks/weekly-content-scan.md`** bij, met je eigen gegevens ingevuld. Laat de desktop-app openstaan op het geplande moment. Maak de taak maar één keer aan.

---

## Problemen oplossen

| Probleem | Oplossing |
|---|---|
| Claude zegt dat hij geen toegang heeft tot een map | Controleer of de map gekoppeld is aan het Project (stap 8) en of de desktop-app openstaat. |
| Claude kan CapCut niet bedienen | Controleer of computer use aanstaat (stap 2). 🍎 Mac: heeft Claude toegang tot Toegankelijkheid en Schermopname (stap 9)? Herstart de app. |
| Claude zegt dat Whisper niet geïnstalleerd is | Doe stap 9b, of laat het zo: de editor werkt dan op beeld. |
| Claude zegt dat hij moet inloggen op Instagram of TikTok | Log opnieuw in via de ingebouwde browser (stap 10). |
| Er verschijnen geen statistieken | Je account moet een creator- of zakelijk account zijn. Kijk in de app of je je statistieken zelf wel ziet. |
| Een skill wordt niet gebruikt | Kijk in **Customize → Skills** of hij aanstaat. Je kan hem ook bij naam noemen: "Gebruik studio-video-editor". |
| Uploaden van een skill mislukt | Upload de ZIP uit `install/`, niet de map, en hernoem het bestand niet. |
| Claude gebruikt de verkeerde taal of naam | Controleer je Creator Profile in de Project-instructies. |

---

## Goed om te weten
- **Je data blijft van jou.** Dit pakket bevat geen persoonlijke gegevens van wie dan ook. De skills draaien enkel in je eigen Claude-account.
- **Jij houdt de controle.** Claude ziet alleen de mappen die je koppelt, leest je socials alleen, en exporteert of post niets zonder dat je het vraagt.
- **Pas gerust aan.** Verander briefingvragen of werkwijzen in de skillbestanden in `skills/`. Zip daarna de *map* opnieuw (niet de inhoud ervan), of gebruik `make-zips.sh`, en upload ze opnieuw.

## Updaten
Wat er per versie veranderd is, staat in [CHANGELOG.md](CHANGELOG.md).

Download de nieuwe versie, verwijder de oude skills in **Customize → Skills** en upload de nieuwe ZIP's. Je Project, je profiel en je Creator Studio-map blijven zoals ze zijn.
