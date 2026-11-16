# Scheduled task — Weekly Content Scan

**Suggested schedule:** every Sunday evening or Monday morning (your local time).
**Needs:** the `studio-content-scan` skill · the Claude desktop app open with the built-in browser, signed in to TikTok and Instagram · optional extra: Metricool connector · Docs (Claude docs) for the report.

## Prompt to paste into the scheduled task
(Replace the `[ ]` parts.)

```
Run my weekly content scan with the studio-content-scan skill.

Creator: [CREATOR NAME] — Instagram [@handle], TikTok [@handle]
Language of the report: [Dutch / English / …]
Region for trends: [country]
Time zone: [e.g. Europe/Amsterdam]
Metricool (optional extra): [brand ID, or "not connected"]
My recurring formats: [1. … 2. … 3. …]
Brands that often boost my posts (exclude from medians): [names or "none"]

Follow the skill step by step: read last week's report, create the new report doc first,
fetch the numbers, analyze the 3 best and 3 weakest videos, update the idea list,
check real trends, and finish with a plan for next week.
Read only — never post, like, comment, DM or change settings. Never type passwords.
Never invent numbers; anything you couldn't check goes in "Couldn't check".
End with a push notification and a short summary with the link to the report.
```
