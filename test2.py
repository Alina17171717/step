
from time import sleep
from selene import have
from selene.support.shared import browser

browser.open('https://www.ecosia.org/')
browser.element('.search-form__input').type('yashaka selene').press_enter()
sleep(2)

#browser.element('.result__link:first-child').click()
browser.all('[data-test-id="mainline-result-web"]')[0].element('a').click()
sleep(2)

browser.all('a[href="/yashaka/selene"]').should(have.size(3))




