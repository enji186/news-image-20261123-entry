# news-image-20261123-entry

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/enji186/news-image-20261123-entry/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/enji186/news-image-20261123-entry/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

One image summing up the world news of Monday 23 November 2026: Nvidia reinstating Jensen Huang as CEO, a magnitude 6.5 earthquake in Vanuatu, Virginia and Oregon suing SpaceX over Grok's sexualised images, Ukraine sinking a Russian warship off Libya, the Democrats' 258-seat House majority, and ESA's BepiColombo Mercury probe safe after a thruster glitch. Drawn programmatically with Python + PIL for clean, legible text.

## Sources

- Reuters: Virginia and Oregon sue SpaceX over Grok, 23 Nov 2026; Nvidia reinstates Huang, 23 Nov 2026.
- Xinhua: Vanuatu magnitude 6.5 earthquake, 23 Nov 2026.
- ESA: BepiColombo safely in Mercury orbit, 23 Nov 2026.
- Japan Times / France 24: Ukraine sinks Russian warship off Libya, 23 Nov 2026.
- AP: Democrats clinch 258 House seats, 23 Nov 2026.

Note: the two items first reported late Sunday in the Americas (the Ukraine warship announcement and the Democrats' 258th seat) reached the wires on Monday 23 November in Asia-Pacific time zones, which the rules' "in any time zone" wording covers.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This copies `entry.png` to `out/entry.png`. Python 3.13 standard library only; no network. Running it twice produces byte-identical output. To redraw the image from scratch, run `python3 draw_entry.py` (requires Pillow and DejaVu fonts; used at build time only, not by `main.py`).

---

<sub>Entered on [make.fun](https://make.fun/?ref=sanbg0sm&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
