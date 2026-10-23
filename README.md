# TransitPulse

**Responsive bus services for better-connected townships.**

TransitPulse is a bus coordination platform for townships. It combines advance journey registrations, digital "I'm waiting here" requests, computer-vision crowd estimates and bus capacity data, so operators can spot service gaps before passengers are left behind.

It helps operators answer three questions:

1. Where are passengers waiting, and which services do they need?
2. Can existing buses and driver duties take them?
3. If not, what extra service, staffing and funding is needed?

This repository contains an interactive prototype dashboard. It is modelled on RapidKL feeder route **T815 (MRT Phileo Damansara – Universiti Malaya)**.

> **Demo data:** stop names, stop positions, the route shape and timetable figures come from RapidKL's official GTFS feed. Passenger numbers, crowding, drivers and costs are simulated for the demo.

---

## Run it

The dashboard is a single static web page (HTML, CSS and JavaScript). It needs no build step and no backend.

### Option A: open it in a browser
Download or clone the repository and open `index.html`. Keep `t815-map.webp` next to it.

### Option B: GitHub Pages
In the repository go to **Settings → Pages → Deploy from a branch → `main` / root**.
The dashboard will be served at `https://ruizhe2004.github.io/TransitPulse/`.

### Option C: Streamlit
```bash
pip install -r streamlit_app/requirements.txt
streamlit run streamlit_app/app.py
```
To get a public link, deploy `streamlit_app/app.py` on [Streamlit Community Cloud](https://share.streamlit.io).
In this version the map image is embedded in `streamlit_app/transitpulse.html`, so the folder works on its own.

---

## What's in the dashboard

| View | What it shows |
|---|---|
| **Live operations** | Route map of all 27 T815 stops at their official GPS positions, with buses moving along the official route. Each stop's colour shows whether the next bus has room, and a yellow centre marks an active boarding request. Also shows the stop demand table, predicted left-behind passengers, the event feed, **next bus trips** (planned vs expected departures from MRT Phileo Damansara) and **suggested next trips** (relief trips, holds, short trips). |
| **Decision support** | Compares responses for the most crowded stop: keep the timetable, hold a bus, run a relief trip, run a short supplementary trip, or call contracted overflow transport. Each option is checked against vehicle, driver, duty and route rules. Nothing happens until a dispatcher approves. |
| **Service gaps** | Flags possible missed pickups, repeated denied boarding and persistent shortages. Each flag is checked against occupancy and disruption data before review. |
| **Passenger app** | Phone mock-ups for registering a journey, sending a boarding request and requesting a supplementary trip (with a QR boarding pass). Also an accessible shelter display with a physical request button. |
| **Reservations** | Proposed and confirmed supplementary trips. Shows the no-show policy and how disputes are handled, and that operator cancellations never count as passenger no-shows. |
| **Crowd estimation** | Camera tiles that count people in each stop's waiting area (no facial recognition), with confidence and visibility flags. Shows the **person-detection model's accuracy** and how camera counts, requests and registrations are combined into one waiting figure. |
| **Driver display** | Onboard screen that highlights upcoming stops with boarding requests. Needs at most one tap. |
| **Capacity planner** | Three planning levels (use existing resources better, target the crowded section, add funded capacity). Includes a scenario comparison, demand vs capacity chart, resource check and driver duty roster. |
| **Township planning** | Unmet-need index by area, recommended investments (feeders, shelters, walking access) and a weekly demand heatmap. |

**Simulation speed:** the dashboard runs in **real time** by default. Use **10×** or **60×** in the top bar for demos, or **Pause**.

---

## Crowd estimation model

People are detected with **Ultralytics YOLO11n** (pretrained on COCO, run at 960 px). It was tested on 329 held-out street and outdoor photos containing 1,194 people, from Open Images V7 (CC BY 2.0):

| Precision | Recall | mAP50 | mAP50-95 | Speed (laptop CPU) |
|---|---|---|---|---|
| 81.5% | 64.3% | 73.5% | 48.2% | ~0.1 s / image |

The model file is submitted separately and is not in this repository.

Because some people are missed in dense crowds, the dashboard shows camera counts as a range. It combines them with boarding requests and registrations rather than relying on the camera alone.

---

## Repository layout

```
index.html                  # the dashboard (open directly or serve with GitHub Pages)
t815-map.webp               # base map for the route view
streamlit_app/
  app.py                    # Streamlit wrapper
  requirements.txt
  transitpulse.html         # dashboard with the map embedded, for Streamlit
```

---

## Data sources and credits

- **Route, stops and timetable:** RapidKL MRT feeder GTFS feed, published by Prasarana on [data.gov.my](https://data.gov.my) (`api.data.gov.my/gtfs-static/prasarana?category=rapid-bus-mrtfeeder`).
- **Base map:** © [OpenStreetMap](https://www.openstreetmap.org/copyright) contributors.
- **Model test photos:** [Open Images V7](https://storage.googleapis.com/openimages/web/index.html), CC BY 2.0.
- **Detection model:** [Ultralytics YOLO11](https://docs.ultralytics.com), AGPL-3.0. A commercial deployment would need an Ultralytics Enterprise licence or another model.
- **Fonts:** Barlow, Barlow Semi Condensed and IBM Plex Mono, from Google Fonts.

The transport operator keeps responsibility for dispatch, driver management and service commitments. TransitPulse only recommends, and a dispatcher approves.
