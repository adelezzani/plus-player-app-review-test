# Plus Player App Review Test Source

This package is ready for static HTTPS hosting.

## What is included
- `review.m3u` — two synthetic test channels.
- `epg.xml` — minimal XMLTV EPG data.
- `streams/channel1/` — original 60-second H.264/AAC HLS test stream.
- `streams/channel2/` — original 60-second H.264/AAC HLS test stream.
- `APP_REVIEW_NOTES.txt` — draft text for App Store Connect.
- `index.html` — optional landing page.

The video/audio is synthetic test material generated specifically for this package. It contains no third-party TV channels, films, series, logos, or provider credentials.

## The only required manual step
Upload this entire folder to a stable public HTTPS host.

Suppose the folder becomes available at:

`https://example.com/plus-player-review/`

Replace this placeholder everywhere in `review.m3u` and `APP_REVIEW_NOTES.txt`:

`https://YOUR-HTTPS-HOST.example/plus-player-review`

with:

`https://example.com/plus-player-review`

Then verify these URLs from a device on mobile/Wi-Fi:
- `/review.m3u`
- `/epg.xml`
- `/streams/channel1/index.m3u8`
- `/streams/channel2/index.m3u8`

Do not bundle this review source into the production app. Give the playlist URL to Apple only in App Review Information / Notes.

## Hosting MIME types
Recommended:
- `.m3u8`: `application/vnd.apple.mpegurl`
- `.m3u`: `audio/mpegurl` or text/plain if your app accepts it
- `.ts`: `video/mp2t`
- `.xml`: `application/xml`

Most modern static hosts configure these adequately.
