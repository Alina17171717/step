from time import sleep

from selene.support.shared import browser
from selene import have, query, command


def test_e2e():
    browser.open('https://book-ye.com.ua/')
    browser.element('.header-bottom__login').click()
    # browser.element('#login-modal .auth-popup__bottom-link').click()
    # sleep(3)
    # browser.element('[name="REGISTER[NAME]"]').set_value('Alina').press_tab()
    # browser.element('[name="REGISTER[EMAIL]"]').set_value('alinagvrn@gmail.com').press_tab()
    # browser.element('[name="REGISTER[PERSONAL_PHONE]"]').set_value('502099399').press_tab()
    # browser.element('[name="REGISTER[PASSWORD]"]').set_value('al2210').press_tab()
    # sleep(5)
    # browser.element('#register-modal .auth-popup__submit').click()
    # sleep(5)
    # browser.element('.header-bottom__login-txt').should(have.text('Alina'))

    browser.element('[name="USER_LOGIN"]').type('alinagvrn@gmail.com').press_tab()
    browser.element('[name="USER_PASSWORD"]').type('al2210').press_tab()
    browser.element('#login-modal .auth-popup__submit.button').click()
    sleep(10)
    if browser.all('.om-overlay .om-wheel-canvas').get(query.size) > 0:
        browser.element('.om-overlay .om-wheel-canvas .om-popup-close-x').click()
    sleep(5)
    browser.element('#title-search-input').click()
    sleep(2)
    browser.element('#q').type('Проєктування').click()
    browser.all('.multi-grid .multi-item')[1].click()
    browser.element('.card-section .button').perform(command.js.click)
    sleep(2)
    browser.element('.number-picker__btn.number-picker__btn--plus').click()
    sleep(2)
    browser.element('.modal-content__close').click()
    browser.element('.header-bottom__basket-icon').click()
    browser.element('.checkout__name').should(have.text('Head First. Патерни проєктування....'))
    browser.element('.modal-content__btn-secondary').click()

    browser.element('[name="ORDER_PROP_31"]').type('Біличенко').press_tab()
    browser.element('[name="ORDER_PROP_30"]').type('Аліна').press_tab()
    browser.element('[name="ORDER_PROP_46"]').type('Миколаївна').press_tab()
    #browser.element('#delivery-13 .fieldset-radio__label').click()



