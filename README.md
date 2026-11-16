# 🎬 Creator Studio for Claude

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
- [ ] A **Mac** (recommended) or Windows PC.
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
2. Inside: `01 Designs`, `02 Presentations`, `03 Motion`, `04 Content reports` (Claude saves its work here), `05 My logo & fonts` (optional: your logo and fonts) and `EDITING-PLAYBOOK.md` (your editing preferences — leave it empty, Claude fills it in after your first approved video).

### Step 6 — Find your folder paths
You need them in step 7. On a Mac: in Finder, **right-click** a folder, **hold Option (⌥)** and choose **"Copy … as Pathname"**.

| Folder | Where | Example |
|---|---|---|
| Your Creator Studio folder | Documents | `/Users/yourname/Documents/Creator Studio` |
| Your raw footage | Usually Downloads | `/Users/yourname/Downloads` |
| Your CapCut projects | Finder → **Go** → **Go to Folder…** → `~/Movies/CapCut` | `/Users/yourname/Movies/CapCut` |

---

## Part D — Your Claude Project

### Step 7 — Create the Project and fill in your profile
1. In Claude, create a new **Project**, e.g. "My Creative Studio".
2. Open **`project-instructions.md`** in a text editor (TextEdit is fine).
3. Fill in the **CREATOR PROFILE** at the top: replace everything between `[ ]` — name, accounts, language, region, recurring formats, tone of voice, editing software and the three paths from step 6.
4. Copy **the whole file** into the Project's **instructions**.

> 💡 The better you describe your formats and tone of voice, the better Claude matches your style.

---

## Part E — Give Claude access to your computer

### Step 8 — Connect your folders to the Project
Open the Project in the **desktop app** and add these three folders as connected folders:
1. Your **Creator Studio** folder
2. Your **raw footage** folder (e.g. Downloads)
3. Your **CapCut** folder (`~/Movies/CapCut`)

Claude only sees folders you connect, and only while the desktop app is open. If Claude asks for access to a folder later, you'll get a prompt to approve. Remove a folder any time in the same menu.

### Step 9 — Grant the macOS permissions
The first time Claude uses your screen (e.g. your first edit), macOS asks for two permissions:
- **Accessibility** — so Claude can click, type and scroll
- **Screen Recording** — so Claude can see your screen

Allow both in **System Settings → Privacy & Security** (switch on **Claude**), and restart the app if asked. Claude then asks permission **per app** (e.g. CapCut) — allow it.

---

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
5. You review V1 **in CapCut** and give feedback, or clearly say "V1 approved".
6. Only then does Claude build **Version 2**: captions, animations, music, effects.
7. Claude **doesn't export** until you ask.

> 💡 Keep the desktop app open, keep your computer awake, and don't use your mouse/keyboard while Claude is controlling CapCut.

---

## Part H (optional) — Weekly scan on autopilot
In your Project, ask: *"Create a scheduled task for my weekly content scan"* and paste the prompt from **`scheduled-tasks/weekly-content-scan.md`** with your details filled in. Keep the desktop app open at that time. Create it only once.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Claude says it can't access a folder | Check the folder is connected to the Project (step 8) and the desktop app is open. |
| Claude can't control CapCut | Check computer use is on (step 2) and Accessibility + Screen Recording are allowed (step 9). Restart the app. |
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
Download the new version, delete the old skills in **Customize → Skills**, upload the new ZIPs. Your Project, profile and Creator Studio folder stay as they are.
