# 🎬 Creator Studio for Claude

> 🍎🪟 **Works on Mac and Windows.** Steps that differ are marked **🍎 Mac** and **🪟 Windows**. The Windows steps are new in v1.1 — if something doesn't match what you see, let us know.

**Your own creative team inside Claude.** After this setup, Claude works for you as:

| Role | What Claude does |
|---|---|
| 🎬 **Video editor** | Edits your videos in your own CapCut project — rough cut first, captions, animations and effects only after your approval. |
| 🎨 **Creative designer** | Thumbnails, carousels, posters, ads and social graphics in your style. |
| ✨ **Motion designer** | Animated text, animated stats, logo animations and AI effects. |
| 📑 **Presentation designer** | Sponsor decks, pitch decks and media kits. |
| 📊 **Data designer** | Charts and infographics of your numbers. |
| 🔍 **Content strategist** | Analyzes your Instagram and TikTok: what works, which hooks, trends and ideas — plus a plan for next week. |

Everything starts from **your own socials**: Claude looks at what you post, how it looks and what performs, and works in that style. No brand guidelines needed.

🇳🇱 Nederlandstalige handleiding: [HANDLEIDING.md](HANDLEIDING.md)

---

## What you need

- [ ] A **Claude Pro or Max** plan — computer use (Claude controlling CapCut) and scheduled tasks don't work on the free plan.
- [ ] A **Mac** or a **Windows 10/11** PC.
- [ ] **CapCut Desktop** if you want Claude to edit.
- [ ] Your **Instagram and/or TikTok** account — a creator or business account for statistics.
- [ ] About **30 minutes**.

---

## Part A — Get Claude ready

### Step 1 — Install the Claude desktop app
1. Go to **claude.com/download** and download the app for your computer.
2. Install it and sign in with your Claude account.
3. **Important:** Claude can only reach your folders, CapCut and browser while the desktop app is **open** and your computer is **awake**.

### Step 2 — Turn on the right features
In the desktop app, open **Settings**:
1. Under **Capabilities**: turn on **Code execution and file creation** — skills need it.
2. Turn on **Computer use** — under **Capabilities**, or under **System** → *This computer*. This lets Claude control CapCut.

---

## Part B — Install the package

### Step 3 — Download and unzip
Download the package (the ZIP from this GitHub page) and unzip it.

### Step 4 — Upload the 6 skills
1. In Claude, go to **Customize → Skills**.
2. Click **+** → **Create skill** → **Upload a skill**.
3. Upload the 6 ZIP files from the **`install/`** folder, one by one:
   `studio-video-editor` · `studio-visual-director` · `studio-motion-design` · `studio-presentation-design` · `studio-data-visualization` · `studio-content-scan`
4. Check that all 6 are switched **on**.

> ⚠️ Upload the ZIP files, not the folders from `skills/`. Don't rename them.

---

## Part C — Your workspace on your computer

### Step 5 — Create your Creator Studio folder
1. Copy the **`workspace-template`** folder to **Documents** (or iCloud Drive) and rename it **`Creator Studio`**.
2. Inside: `01 Designs`, `02 Presentations`, `03 Motion`, `04 Content reports` (Claude saves its work here), `05 My logo & fonts` (optional: your logo and fonts) `EDITING-PLAYBOOK.md` (your editing preferences — leave it empty, Claude fills it in after your first approved video) and `Tools/whisper` (optional transcription, step 9b).

### Step 6 — Find your folder paths
You need them in step 7.
- **🍎 Mac:** in Finder, **right-click** a folder, **hold Option (⌥)** and choose **"Copy … as Pathname"**.
- **🪟 Windows:** in File Explorer, **right-click** a folder and choose **"Copy as path"** (Windows 10: hold **Shift** while right-clicking). Remove the quotes when you paste.

| Folder | 🍎 Mac example | 🪟 Windows example |
|---|---|---|
| Your Creator Studio folder | `/Users/yourname/Documents/Creator Studio` | `C:\Users\yourname\Documents\Creator Studio` |
| Your raw footage | `/Users/yourname/Downloads` | `C:\Users\yourname\Downloads` |
| Your CapCut projects | `/Users/yourname/Movies/CapCut` | `C:\Users\yourname\AppData\Local\CapCut` |

> 💡 Not sure where CapCut keeps your projects? In CapCut open **Settings** and look at the **drafts location** — that's the folder. On Windows, `AppData` is hidden: paste the path into the File Explorer address bar to open it.

---

## Part D — Your Claude Project

### Step 7 — Create the Project and fill in your profile
1. In Claude, create a new **Project**, e.g. "My Creative Studio".
2. Open **`project-instructions.md`** in a text editor (🍎 TextEdit / 🪟 Notepad).
3. Fill in the **CREATOR PROFILE** at the top: replace everything between `[ ]` — name, accounts, language, region, recurring formats, tone of voice, editing software and the three paths from step 6.
4. Copy **the whole file** into the Project's **instructions**.

> 💡 The better you describe your formats and tone of voice, the better Claude matches your style.

---

## Part E — Give Claude access to your computer

### Step 8 — Connect your folders to the Project
Open the Project in the **desktop app** and add these three folders as connected folders:
1. Your **Creator Studio** folder
2. Your **raw footage** folder (e.g. Downloads)
3. Your **CapCut** folder (from step 6)

Claude only sees folders you connect, and only while the desktop app is open. If Claude asks for access to a folder later, you'll get a prompt to approve. Remove a folder any time in the same menu.

### Step 9 — Grant the permissions
**🍎 Mac:** the first time Claude uses your screen (e.g. your first edit), macOS asks for two permissions:
- **Accessibility** — so Claude can click, type and scroll
- **Screen Recording** — so Claude can see your screen

Allow both in **System Settings → Privacy & Security** (switch on **Claude**), and restart the app if asked.

**🪟 Windows:** no extra system settings needed. If Windows asks for administrator permission while installing the desktop app, allow it.

**Both:** Claude then asks permission **per app** (e.g. CapCut) — allow it. Claude works in the background and never takes over your whole screen.

---

### Step 9b (optional) — Install Whisper for transcription
With Whisper, Claude reads **what is said** in your footage before editing, so it finds the best quotes, hooks and funny moments by content. Everything stays local on your computer.

**🍎 Mac**
1. Open **Terminal** (Cmd + Space → "Terminal").
2. Type `cd ` (with a space), drag the **`Creator Studio/Tools/whisper`** folder into the Terminal window, press Enter.
3. Type `pip3 install faster-whisper`, press Enter.
4. Type `python3 transcribe.py --download-only`, press Enter. This downloads the model (± 1.6 GB) into `models`. Wait for **"ready"**. Short on space or an older computer? Use `--model small` (± 0.5 GB).

**🪟 Windows**
1. Install **Python 3** from **python.org** → Downloads. In the installer, tick **"Add python.exe to PATH"**.
2. Open the **`Creator Studio\Tools\whisper`** folder in File Explorer, click in the address bar, type `powershell` and press Enter. PowerShell opens in that folder.
3. Type `py -m pip install faster-whisper`, press Enter.
4. Type `py transcribe.py --download-only`, press Enter. Wait for **"ready"** (± 1.6 GB; add `--model small` for ± 0.5 GB).
5. Optional, faster: `winget install Gyan.FFmpeg`.

**Both:** put the path to `Tools/whisper` under **WHISPER FOLDER** in your Creator Profile.

From then on the video editor transcribes all spoken footage before Version 1, into a `_Transcripties` folder next to your footage. Skip this step and the editor simply works on image.

## Part F — Connect your socials

### Step 10 — Sign in in the built-in browser
The desktop app has a **built-in browser**. Open it and sign in **yourself** to:
- **Instagram** (instagram.com)
- **TikTok** (tiktok.com — then open TikTok Studio once)
- **YouTube Studio**, if you use YouTube

You stay signed in, so you only do this once. Claude can then **read** your posts, videos and statistics.

> 🔒 Claude never types passwords, and never posts, likes, comments or DMs on your behalf. Read-only.

### Step 11 (optional) — Metricool
Already using **Metricool**? Connect it in Claude's **connectors** and put your Metricool brand ID in the Creator Profile — faster stats with a longer history. Not using it? Skip this step.

---

## Part G — Test it

### Step 12 — Try every role
| Role | Try |
|---|---|
| 🔍 Content strategist | "Analyze my content of this week and make a plan for next week." |
| 🎨 Creative designer | "Make a 5-slide carousel about [topic]." or "Make a thumbnail for my latest video." |
| ✨ Motion designer | "Make an animated title for my next video." |
| 📑 Presentation designer | "Make a media kit I can send to brands." |
| 📊 Data designer | "Turn my numbers of the last 30 days into a clear infographic." |
| 🎬 Video editor | See below ⬇️ |

### How to have Claude edit a video
1. In **CapCut**, create a new project and **import your clips**. Give it a clear name, e.g. `New video`.
2. In your Claude Project, ask: **"Edit my new video."**
3. Claude asks the editing briefing (project name, video type, platform, length, style, music, extra notes).
4. Claude opens CapCut and builds **Version 1** — editing only, no captions or effects.
5. You review V1 **in CapCut** and give feedback, or clearly say "V1 approved". Every round of feedback becomes a new timeline (V2, V3 …) in the same project, so earlier versions stay untouched.
6. Only after approval does Claude do the finishing: subtitles (the Whisper `.srt`, imported straight into CapCut, whenever there's speech), animations, music, effects.
7. Claude **doesn't export** until you ask.

> 💡 Keep the desktop app open and your computer awake. Claude works in the background and never takes over your whole screen — just don't click around in CapCut while it's editing.

---

## Part H (optional) — Weekly scan on autopilot
In your Project, ask: *"Create a scheduled task for my weekly content scan"* and paste the prompt from **`scheduled-tasks/weekly-content-scan.md`** with your details filled in. Keep the desktop app open at that time. Create it only once.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Claude says it can't access a folder | Check the folder is connected to the Project (step 8) and the desktop app is open. |
| Claude can't control CapCut | Check computer use is on (step 2). 🍎 Mac: Accessibility + Screen Recording allowed (step 9)? Restart the app. |
| Claude says Whisper isn't installed | Do step 9b, or leave it: the editor then works on image. |
| Claude says it needs to sign in to Instagram/TikTok | Sign in again in the built-in browser (step 10). |
| No statistics | Your account must be a creator/business account; check you can see insights in the app yourself. |
| A skill isn't used | Check it's on in **Customize → Skills**, or name it: "Use studio-video-editor". |
| Skill upload fails | Upload the ZIP from `install/` (not the folder) and don't rename it. |
| Wrong language or name | Check your Creator Profile in the Project instructions. |

---

## Good to know
- **Your data stays yours.** This package contains no one's personal data. Skills run only inside your own Claude account.
- **You stay in control.** Claude only sees folders you connect, only reads your socials, and never exports or posts without your request.
- **Customize freely.** Edit the skill files in `skills/`, re-zip the *folder* (not its contents) or run `make-zips.sh`, and re-upload.

## Updating
See [CHANGELOG.md](CHANGELOG.md) for what changed in each version.

Download the new version, delete the old skills in **Customize → Skills**, upload the new ZIPs. Your Project, profile and Creator Studio folder stay as they are.
