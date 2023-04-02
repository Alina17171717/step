from time import sleep

from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

def test_e2e():
    browser.open('https://todomvc.com/examples/emberjs/')
    s('#new-todo').type('11').press_enter()
    s('#new-todo').type('22').press_enter()
    s('#new-todo').type('33').press_enter()
    s('#new-todo').type('44').press_enter()
    ss('#todo-list>li').should(have.exact_texts('11', '22', '33', '44'))
    #ss('#todo-list>li').should(have.size(4))
    ss('#todo-list>li').element_by(have.exact_text('22')).element('.toggle').click()
    ss('#todo-list>li').element_by(have.exact_text('33')).element('.toggle').click()
    ss('#todo-list>li').element_by(have.exact_text('22')).element('.toggle').click()
    s('[href="#/active"]').click()
    ss('#todo-list>li').should(have.exact_texts('11', '22', '44'))
    # ss('#todo-list>li').should(have.size(3))
    s('[href="#/completed"]').click()
    ss('#todo-list>li').should(have.exact_texts('33'))
    #ss('#todo-list>li').should(have.size(1))
    ss('#todo-list>li').element_by(have.exact_text('33')).hover().element('.toggle').click()
    ss('#todo-list>li').should(have.size(0))
    s('[href = "#/"]').click()
    ss('#todo-list>li').element_by(have.exact_text('22')).double_click()
    ss('#todo-list>li').element_by(have.css_class('editing')).element('.edit')\
        .perform(command.js.set_value('11223344')).press_enter()
    sleep(3)
    s('#toggle-all').click()
    ss('#todo-list>li').element_by(have.exact_text('11')).element('.toggle').click()
    s('#clear-completed').click()
    ss('#todo-list>li').should(have.size(1))
    sleep(3)


