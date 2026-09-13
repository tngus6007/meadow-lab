from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='C:/Program Files/Google/Chrome/Application/chrome.exe');page=b.new_page()
 page.goto('http://127.0.0.1:4182')
 def tab(s):
  for _ in range(100):
   if page.locator(s).evaluate('(e)=>e===document.activeElement'):return
   page.keyboard.press('Tab')
  raise AssertionError(s)
 def enter(s):tab(s);page.keyboard.press('Enter')
 enter('#start');enter('#step');tab('input[value=food]');page.keyboard.press('Space');enter('#check')
 assert '1 / 4' in page.locator('#progress').inner_text()
 enter('nav [data-page="2"]');tab('#water');page.keyboard.press('Home');page.keyboard.press('Enter');enter('#step')
 tab('input[value=plants]');page.keyboard.press('Space');enter('#check')
 enter('nav [data-page="3"]');enter('[data-organism=grass]')
 for _ in range(3):enter('#step')
 tab('input[value=grass]');page.keyboard.press('Space');enter('#check')
 enter('nav [data-page="4"]')
 for s in ['#water','#light']:tab(s);page.keyboard.press('End');page.keyboard.press('Enter')
 for _ in range(12):enter('#step')
 tab('input[value=both]');page.keyboard.press('Space');enter('#check')
 assert '4 / 4' in page.locator('#progress').inner_text();assert page.locator('#complete').is_visible()
 page.screenshot(path=str(root/'evidence'/'keyboard.png'),full_page=True)
 enter('#replay');assert '0 / 4' in page.locator('#progress').inner_text();b.close()
print('PASS keyboard-only all activities, model repair and reset')
