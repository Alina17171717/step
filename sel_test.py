# selene-intro/tests/test_todomvc.py #
from selene.support.shared import config, browser


def test_complete_todo():
    # open TodoMVC page

    # add todos: 'a', 'b', 'c'
    # todos should be 'a', 'b', 'c'

    # toggle 'b'
    # completed todos should be 'b'
    # active todos should be 'a', 'c'
    pass

from selene import browser, by, have, be


def test_complete_todo():
    #1) open TodoMVC page
    browser.open('http://todomvc.com/examples/emberjs/')
    # add todo 'a':
    # 2)  1) find "new todo" edit field 2) set value to 'a' 3) press Enter
    #browser.element(by.id('new-todo')).type('a').press_enter()
    browser.element('#new-todo').type('a').press_enter()
    # add todos 'b', 'c'
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    # todos should be 'a', 'b', 'c'
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))
    #або browser.element('#new-todo').should(be.visible).type('a').press_enter()
    browser.config.timeout = 6
    config.browser_name = "firefox"

    #3) toggle 'b'
    # 1. among all todos 2. find the one with 'b' text
    # 3. find its 'toggle' checkbox 4. click it
    browser.all('#todo-list>li').element_by(have.exact_text('b')) \
        .element('.toggle').click()
    #4) completed todos should be 'b'
    # among all todos
    # filter only completed ones
    browser.all('#todo-list>li').filtered_by(have.css_class('completed')) \
        .should(have.exact_texts('b'))
    #5) active todos should be 'a', 'c'

    # among all todos
    # filter only not completed ones
    browser.all('#todo-list>li').filtered_by(have.no.css_class('completed')) \
        .should(have.exact_texts('a', 'c'))



