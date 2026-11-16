---
name: studio-content-scan
description: Weekly Instagram + TikTok content scan: stats, video analysis, idea list, trends and a weekly plan in a report doc. Use for the scheduled scan or when asked to analyze content or plan the week.
---

# Studio Content Scan — Instagram + TikTok

Read the **Creator Profile** in the project instructions for: creator name (exact spelling), handles, chat and content language, country/region, time zone, recurring formats, analytics source (e.g. Metricool brand ID) and known boosted partners. Write the report in the creator's chat language.

## Ground rules (always)

- **Read only.** Never post, schedule, like, comment, follow, DM, boost, create drafts or change settings. If Metricool is connected, use only its analytics tools (`getBrandSettings`, `getAnalyticsAvailableMetrics`, `getAnalyticsDataByMetrics`), never `createScheduledPost` / `updateScheduledPost`.
- **Never type passwords or codes.** On a login screen: continue with what's possible and put "please log in again on <platform>" at the top of the report.
- Use the normal interface. No calls to private APIs, no downloading videos from TikTok/Instagram.
- Never invent figures or observations. Anything you couldn't check goes in "Couldn't check".

## Definitions

- Like rate = likes / views.
- **Boosted posts:** signals = paid-partnership/"ad" label or a partner from the profile + views far above normal + like rate below ~0.5%. Report them separately and exclude them from all medians.

## Weekly mode

### 1. Read the previous report
Find the most recent doc "Content report [CREATOR NAME] — week of …" and read it fully: formats, idea list + statuses, plan, known boosted posts, median baseline. No previous report → full first scan (90 days); say so at the top.

### 2. Create the report doc first
New doc "Content report [CREATOR NAME] — week of <date of the coming Monday>" with the skeleton below, before the research. Fill it section by section.

### 3. Get the numbers
**Standard — via the browser (always available):**
- **TikTok:** TikTok Studio (`tiktok.com/tiktokstudio/content`) — per video: views, likes, comments, shares, saves, post date; open analytics for the overview of the last 7, 28 and 60 days. Skip pinned videos at the top of the list.
- **Instagram:** the professional dashboard / Insights on the profile (Reels and posts: views, likes, comments, shares, saves, reach where visible). Scroll back far enough to cover 90 days where possible.
- **YouTube** (if in the profile): YouTube Studio → Content / Analytics.
Write the numbers into a table as you go (with the date you read them), so medians can be computed afterwards. If a platform shows fewer days than needed, use what's available and say so in "Alerts".

**Optional extra — Metricool** (only if the connector is connected and a brand ID is in the profile): faster and with a longer history. Use `getAnalyticsDataByMetrics` for the last 90 days (baseline) and the last 7 days; check codes with `getAnalyticsAvailableMetrics`. Typical sets:
- IG Reels: IGRE02, IGRE03, IGRE06, IGRE23 (views), IGRE11, IGRE10, IGRE07, IGRE12, IGRE21, IGRE16, IGRE20, IGRE24, IGRE27
- IG Feed: IGPO02, IGPO03, IGPO06, IGPO07, IGPO28, IGPO14, IGPO13, IGPO08, IGPO15, IGPO27, IGPO19, IGPO26
- TikTok: TKPO02, TKPO05, TKPO03, TKPO07, TKPO08, TKPO09, TKPO10, TKPO11, TKPO13, TKPO15, TKPO16
Still check the browser for the newest videos Metricool hasn't synced yet.

Compute medians with a script (organic only, boosted posts excluded): median views and like rate per platform for (a) the last 30 days and (b) 90 days. Carousels separately.

### 4. Video analysis
Pick the **3 best and 3 weakest videos of the week** (views vs. median; tie → like rate). First scan: also the 3 best organic videos of the 90 days as reference.

Per video, in the browser, only watching:
1. **Frames:** open the video, pause and screenshot around **0 s, 1 s, 3 s, 7 s** and the end. Zoom in on on-screen text.
2. **Retention (TikTok):** in TikTok Studio analytics read average watch time, % watched fully, retention curve (where do people drop?), traffic sources (For You / followers / search). IG: average watch time and view rate where visible.
3. **Assess** (only what you actually see): hook 0–3 s (first image, creator on screen, text, tension/question/number/score?) · on-screen text (present, readable, word count) · pace (cuts in the first 7 s) · length and drop-off point linked to what's on screen · format.
4. **Subtitles & text:**
   - **Subtitles:** turn on TikTok captions if available (viewing only, no account settings) and read them; note the **first spoken sentence** (verbal hook) verbatim.
   - **On-screen text:** verbatim overlay of the first 3 s and later overlays; readability, language.
   - **Caption:** first line, length, question/CTA, tags, number of hashtags.
   - **Cover:** text on the cover; does it match the hook?
   - **Match:** do image, spoken hook, overlay and caption tell the same story? Is the hook's promise paid off before the drop-off?
   - Compare these elements between strong and weak videos.
5. **Audio without subtitles** can't be heard; report only what's visible. If exports exist in a shared folder (named in the previous report or by the creator), you may stage them, extract frames with ffmpeg and transcribe the audio — otherwise not.

End with **2–3 patterns**: what strong videos share in the first 3 seconds and what weak ones do differently. These patterns drive the hooks in the weekly plan.

### 5. Follow up on used ideas
For each idea in the previous list: was it posted? Link, numbers vs. median, verdict **works / doesn't work / too early (<72 h)**. Include video-analysis insights.

### 6. Update the idea list
Keep the existing list (no brand-new list), set statuses (New, Planned, Used – works, Used – doesn't work, Too early, Dropped), update notes, add at most **3–5 new ideas**. Formats stay the same (profile's Recurring Formats / previous report) unless the data clearly says otherwise.

### 7. Hashtags & trends
Short: what worked on the creator's own posts + this week's trends. **Always actually check trends:**
1. TikTok Studio → Inspiration → Trending (`tiktok.com/tiktokstudio/inspiration`), filter on the creator's region; if it's not listed, say so and use "All regions" only as a signal.
2. Search the web for this week's trend list and open the page itself (no snippets as source).
3. Search for upcoming dates and moments in the creator's country that fit their formats (holidays, events, seasonal topics in the coming week).
Only include trends that fit the creator's formats, with hashtag/sound, source link and matching format. Instagram: 1–3 tags.

### 8. Plan for the coming week
3–5 concrete videos with day, platform, idea, hook (spoken first line + on-screen text), first caption line and hashtags, based on the step-4 patterns. No full scripts.

## Report structure

1. **Alerts** — re-login needed, skill/report issues, first scan
2. **Lesson of the week** — one bold sentence + a number
3. **Last 7 days** — table (date, platform, link, views, likes, like rate, × median, verdict) + median baseline (30 d and 90 d)
4. **Video analysis** — per video: link, numbers, image 0–3 s, spoken hook, on-screen text, caption, cover, pace, drop-off, verdict; then 2–3 patterns
5. **Boosted posts** — separate, with like rate
6. **Formats**
7. **Idea list** — table with status
8. **Hashtags & trends**
9. **Plan for the coming week** — table
10. **Couldn't check**

## Wrap-up
In a scheduled run, send a push notification. End with a 3–5 sentence message: the main lesson of the week, the plan for next week and the link to the report.
