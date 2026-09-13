# Test report

Executed September 12–13, 2026 on Windows. Node 20.15.0/npm 10.7.0; Chrome 152.0.7977.83; Playwright 1.55.0. Adult agent-operated simulation only; no children involved.

`npm test`: **six tests passed**. `npm run build`: four-file static build passed. `tests/browser.py`: full journey passed at 360×900, 768×900 and 1280×900 (raw results evidence/results.json). `tests/keyboard.py`: keyboard-only navigation, condition changes, food-source restoration, final recovery and replay passed.

## Acceptance mapping

| Requirement | Actual evidence |
|---|---|
| Lower water changes plant growth | Domain dry scenario: grass 6→4→2→0 across steps; first-step rabbit can still rise because it reads prior food support. Browser dry scenario asserts 4 then 2 and matches a downward prediction. |
| Consumer without food cannot thrive | Remove both plants, advance twelve steps: rabbit, vole and fox support all reach zero. This is a support indicator, not a population model. |
| Restoration follows model rules | Final resource repair does not immediately pass viability. First plant support 2→3 while rabbit 3→1; subsequent steps rebuild support and satisfy viability. Browser repairs missing grass and both-resource final scenario. |
| Determinism | Two identical scenario/action sequences deep-equal. No random generator or external data used. |
| Bounded values | Tested 200 steps for each of nine low/threshold/high resource combinations; all five species stay finite in 0–10. Controls only offer integer 0…10. |
| Reset complete | Browser dry-scenario reset restores water1, prediction Skip, step0 and starting indicators. Model fresh snapshot restores missing species correctly. Reset lesson and refresh yield zero progress. |
| Meaningful habitat construction | Browser removes grass, steps, adds it back and steps again; completion requires actual support plus a valid food-link answer. |
| Three scenarios and unfamiliar application | Sunny/dry/shade supplied; dry and shade exercised; final low-light/low-water patch needs multiple steps after repair. |
| Inspectable steps and food arrows | Every present/absent species gets a before/after/reason row. Numerical meters and journal are text alternatives to species icons. Food paths explicitly label arrow direction food→consumer. |
| Pause/step/reset | Browser starts Run slowly, waits for a step, pauses and verifies no change over another interval. Manual Step advances exactly one and stops auto-run. Navigation/reset stop timers. |
| Keyboard/touch | Browser taps species/reset controls; separate Tab/Enter/Space/Home/End-only route reaches all four completions and replay. No pointer activation/direct focus in that script. |
| Responsive/reduced motion/privacy | Every screen checked for document width ≤viewport at 360/768/1280. Journal is an explicitly scrollable region. Reduced-motion preference active; no animation/audio autoplay. No uncaught JS errors; localStorage empty. Source contains no analytics, network grading, login or learner information fields. |

## Numbered screenshot walkthrough

1. [Build desktop](evidence/01-build-1280.png): five roles, support meters and actual step journal after grass removal/reintroduction.
2. [Experiment desktop](evidence/02-experiment-1280.png): dry spell, downward prediction and explainable changes.
3. [Restore desktop](evidence/03-restore-1280.png): missing food source repaired by learner action and steps.
4. [Final desktop](evidence/04-final-1280.png): new scenario repaired and explained.
5. Mobile examples: [build](evidence/01-build-360.png), [experiment](evidence/02-experiment-360.png), [restore](evidence/03-restore-360.png), [final](evidence/04-final-360.png). Equivalent 768px screenshots included.
6. [Keyboard focus](evidence/keyboard.png): final explanation after keyboard-only operation.

Desktop build and mobile restore screenshots visually inspected: controls and journal fit; species use labels and numeric indicators as well as colour. Content is intentionally vertically scrollable. No formal WCAG certification, screen-reader audit, physical touch-device or other-browser testing. Touch/reduced-motion are emulated, not human studies. No measured learning gains. Initial server handle was no longer live after turn continuation; completed browser evidence was read, local server restarted for keyboard testing. No active test was duplicated solely on an observation timeout.
