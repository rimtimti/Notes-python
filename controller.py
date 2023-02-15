import function as f
import ui


def run():
    input_from_user = ''
    while input_from_user != '7':
        ui.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            f.show()
        if input_from_user == '2':
            f.add()
        if input_from_user == '3':
            f.edit_del('del')
        if input_from_user == '4':
            f.edit_del('edit')
        if input_from_user == '5':
            f.show_date()
        if input_from_user == '6':
            f.show_id()
        if input_from_user == '7':
            ui.goodbuy()
            break
