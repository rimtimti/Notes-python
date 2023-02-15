import function
import ui


def run():
    input_from_user = ''
    while input_from_user != '7':
        ui.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            function.show()
        if input_from_user == '2':
            function.add()
        if input_from_user == '3':
            function.delete()
        if input_from_user == '4':
            function.edit()
        if input_from_user == '5':
            function.show_date()
        if input_from_user == '6':
            function.show_id()
        if input_from_user == '7':
            ui.goodbuy()
            break
