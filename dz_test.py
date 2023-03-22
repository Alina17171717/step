from time import sleep
from selene import have
from selene.support.shared import browser


def test_complete_todo():
    browser.open('https://todomvc.com/examples/emberjs/')
    browser.element('#new-todo').set_value('a').press_enter()
    browser.element('#new-todo').set_value('b').press_enter()
    browser.element('#new-todo').set_value('c').press_enter()

    browser.all('#todo-list li').should(have.exact_texts('a', 'b', 'c'))
    browser.all('#todo-list li .toggle')[1].click()
    browser.element('#todo-list li.completed').should(have.exact_text('b'))
    browser.all('#todo-list li:not(.completed)').should(have.exact_texts('a', 'c'))

