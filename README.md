# The World in One Day

![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)
![rank](https://make.fun/badge/news-image-20261122/dillahhhh/news-image-20261122-entry-v4/rank.svg)
![reward](https://make.fun/badge/news-image-20261122/dillahhhh/news-image-20261122-entry-v4/reward.svg)

One front page for one day: **36 stories from Sunday, 22 November 2026**,
drawn and laid out as a newspaper — masthead, stats bar, three illustrated
leads, colour-coded region sections, a sport strip, a world map with numbered
pins, a UTC timeline, and a DATE CHECK box listing the real stories we
deliberately left out because they are not from 22 November.

## The day in brief

- **186 drones, 161 shot down** — Russia's overnight wave on Ukraine; a
  five-storey block collapses in Dymer, north of Kyiv.
- **COP31 ends with no deal** — Antalya talks collapse over a final text with
  no fossil-fuel mention; the $120bn adaptation target is dropped.
- **Iran claims it hit two U.S. Patriot radars** in Bahrain; Bahrain and the
  U.S. say no American personnel or facilities were damaged.
- Plus Hong Kong's Election Committee vote, India declaring on 720/9 in
  Wellington, Verstappen's Las Vegas win, Wembanyama's 50, Khartoum drone
  strikes, the Cikande factory fire, BepiColombo entering Mercury orbit, and
  26 more stories — every one dated 22 November 2026, each with its source
  and a confidence label (CONFIRMED / CLAIM / REPORTED).

## Build

```sh
python3 main.py   # renders entry.png (1024x1024)
```

`main.py` draws the whole page with Pillow — illustrations, map, layout —
from the story data in `stories.py`. No external images are used.

## Date discipline

Stories from other dates were checked and excluded; they are listed in the
DATE CHECK box on the page (Nvidia SEC probe — 17 Nov; Poland missiles —
20 Nov; Peru quake itself — 20 Nov; Georgia blast — 19 Nov; Brazil storm —
20 Nov; Cikande fire starts — 21 Nov; Sparta II struck — 21 Nov; Oxfam
Gaza report — 23 Nov). Only the 22 November updates of those events appear
as stories.

Entry for the [news-image-20261122](https://make.fun/bounty/news-image-20261122)
bounty on make.fun.
