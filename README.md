# Meadow Lab

Public preview: https://tngus6007.github.io/meadow-lab/

Source: https://github.com/tngus6007/meadow-lab

An original, inspectable meadow model for learners around age nine. Build food relationships, predict changes in three scenarios, restore a missing food source, then repair a new patch. Source includes guides, tests and screenshot evidence. AI assistance was used and is disclosed.

## Run, test, build and preview

Node **20.15.0** and npm **10.7.0** tested; `.nvmrc` and dependency-free lockfile included.

```sh
npm ci
npm run dev
# http://127.0.0.1:4182
npm test
npm run build
# Stop dev server before using the same port:
npm run preview
# http://127.0.0.1:4182 serves dist/
```

Deploy four files from dist/ to any static HTTPS host. Supplied preview is GitHub Pages from repository root; no requester account or paid service is needed. The full source runs independently if hosting disappears. ES modules need HTTP serving, not double-click file opening.

## Architecture

`model.mjs` defines five species, five scenario snapshots and deterministic updates. `app.mjs` owns lesson state, semantic controls, original SVG species symbols, labelled meters, food paths and a before/after journal. `style.css` provides responsive layout and keyboard focus. Tests are in `tests/`. No application dependencies, secret, external asset, runtime AI, network grading or analytics.

Water/light and species support use **illustrative 0–10 units**, not scientific measurements or population counts. Zero support means the current habitat cannot support that species; it is not a graphic death or extinction model. Presence toggles explicitly add/remove a species. Adding starts its support at four. No model outcome is a prediction about actual field populations.

Each step reads **only the previous state's food indicators**, then updates all five species simultaneously. Absent species stay at zero. Grass needs water≥3 and light≥4; clover needs water≥4 and light≥3. These differing thresholds are invented for teaching, not measured species tolerances. An included plant meeting both thresholds gains one support unit, otherwise loses two. Rabbits require grass OR clover support≥4; field voles require grass≥4; foxes require rabbits OR voles≥4. An included consumer with that food support gains one, otherwise loses two. Every result is clamped to 0–10. Food-dependent responses are delayed by at least a step because prior state is used. Resources remain at their selected settings; no nutrient or water-consumption budget is simulated.

The model omits grazing depletion, predation feedback, competition, reproduction, disease, migration, temperature, soil nutrients, seasons and decomposers. Animals also need water and shelter in reality, but the model isolates indirect resource effects through plants. Support can recover from zero because it describes habitat support, not resurrection or population recovery. The guide explicitly discusses these limitations.

Reset scenario restores all initial species, values, controls, prediction, journal and timer state for that scenario; completed lesson entries persist. Navigation starts each activity's scenario. Reset lesson/refresh clear all memory. Run slowly advances once per 2.5 seconds; Pause, manual stepping, changing conditions/species, navigation and hidden-tab handling stop it. No animation, forced audio or timer-based score. The step count is an inspection aid, not a duration in days.

## Verification and supported environment

Chrome 152.0.7977.83 on Windows tested at 360/768/1280px. Tests use Playwright 1.55.0 with installed Windows Chrome (adjust path for another OS): while server runs, `uv run --no-project --with playwright==1.55.0 python tests/browser.py`, then the same command with `tests/keyboard.py`. Model tests use built-in Node runner.

No children tested; no measured learning outcomes or formal WCAG certification. Other browsers, physical touchscreen hardware and screen readers are untested. Touch/reduced-motion/keyboard checks are agent-operated browser simulations. No accounts or learner information collected. Host may retain ordinary request logs. Initial public loading needs internet; local serving is independently possible. No service worker/offline-install feature claimed.
