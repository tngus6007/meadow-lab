from pathlib import Path
import json
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1];(root/'evidence').mkdir(exist_ok=True)
results=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='C:/Program Files/Google/Chrome/Application/chrome.exe')
 for width in [360,768,1280]:
  page=b.new_page(viewport={'width':width,'height':900},has_touch=True,reduced_motion='reduce');errors=[]
  page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto('http://127.0.0.1:4182');page.locator('#start').click()
  page.locator('[data-organism=grass]').tap();page.locator('#step').click()
  page.locator('[data-organism=grass]').tap();page.locator('#step').click()
  page.locator('input[value=food]').check();page.locator('#check').click();assert '1 / 4' in page.locator('#progress').inner_text()
  page.screenshot(path=str(root/'evidence'/f'01-build-{width}.png'),full_page=True)
  page.locator('nav [data-page="2"]').click();page.locator('#scenario').select_option('dry');page.locator('#prediction').select_option('down');page.locator('#step').click()
  assert 'matched' in page.locator('#comparison').inner_text();assert page.locator('#meter-grass').get_attribute('value')=='4'
  page.locator('#step').click();assert page.locator('#meter-grass').get_attribute('value')=='2'
  page.locator('input[value=plants]').check();page.locator('#check').click();assert '2 / 4' in page.locator('#progress').inner_text()
  page.screenshot(path=str(root/'evidence'/f'02-experiment-{width}.png'),full_page=True)
  page.locator('#reset').click();assert page.locator('#water').input_value()=='1';assert page.locator('#prediction').input_value()=='skip';assert 'Step 0' in page.locator('#habitat').inner_text()
  page.locator('#scenario').select_option('shade');page.locator('#step').click();assert page.locator('#meter-clover').get_attribute('value')=='4'
  page.locator('nav [data-page="3"]').click();page.locator('input[value=grass]').check();page.locator('#check').click();assert 'apply it' in page.locator('#feedback').inner_text()
  page.locator('[data-organism=grass]').click()
  for _ in range(3):page.locator('#step').click()
  page.locator('input[value=grass]').check();page.locator('#check').click();assert '3 / 4' in page.locator('#progress').inner_text()
  page.screenshot(path=str(root/'evidence'/f'03-restore-{width}.png'),full_page=True)
  page.locator('nav [data-page="4"]').click();page.locator('#water').select_option('6');page.locator('#light').select_option('6')
  for _ in range(12):page.locator('#step').click()
  page.locator('input[value=both]').check();page.locator('#check').click();assert page.locator('#complete').is_visible();assert '4 / 4' in page.locator('#progress').inner_text()
  page.screenshot(path=str(root/'evidence'/f'04-final-{width}.png'),full_page=True)
  page.locator('#reset').click();page.locator('#play').click();page.wait_for_timeout(2800);page.locator('#play').click()
  text=page.locator('#habitat').inner_text();page.wait_for_timeout(2700);assert text==page.locator('#habitat').inner_text()
  for i in range(5):
   page.locator(f'nav [data-page="{i}"]').click();assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),(width,i)
   assert page.evaluate('matchMedia("(prefers-reduced-motion: reduce)").matches')
  page.locator('#reset-all').tap();page.reload();assert '0 / 4' in page.locator('#progress').inner_text();assert page.evaluate('localStorage.length')==0;assert not errors,errors
  results.append({'width':width,'passed':True,'errors':errors});page.close()
 version=b.version;b.close()
(root/'evidence'/'results.json').write_text(json.dumps({'browser':version,'results':results},indent=2));print(results)
