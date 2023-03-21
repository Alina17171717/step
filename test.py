from time import sleep

from selene import have, query, by
from selene.support.shared import browser
browser.open('https://duckduckgo.com/')
browser.element('[name="q"]').type('itstep').press_enter()
browser.all('.nrn-react-div')[0].element('[data-testid="result-title-a"]').click()
browser.elements('.menu__link')[0].click()
sleep(2)
#або page_text = browser.driver.page_source.lower()
#count = page_text.count('step')
#або page_text = browser.driver.page_source.lower()
#count = len([word for word in page_text.split() if 'step' in word.lower()])
x = browser.all(by.partial_text('Step')).get(query.size)
print('Слово Step повторюється на цій сторінці:', x, 'раз')
#assert x == 7




