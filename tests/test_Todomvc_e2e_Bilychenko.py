from Todomvc_testing.Model import todos

def test_Todo_clear():
    todos.open()
    todos.add('101', '202', '303', '404')
    todos.should('101', '202', '303', '404')
    todos.start_editing('202', '77')
    todos.edit('404', '88')
    todos.edit_by_focus_change('101', '99')
    todos.cancel_edit('303', '55')
    todos.toggle('88')
    todos.toggle('77')
    todos.should_be_completed('77', '88')
    todos.clear_completed()
    todos.should_be_active('99', '303')
    todos.should_be_items_left(2)
    todos.delete('99')
    todos.delete('303')
    todos.should_be_empty()
