SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone = ''
email = ''
extra_info = ''
# information about entrepreneurs
business_registration_number = ''
tax_identification_number = ''
checking_account = ''
bank = ''
bank_identification_code = ''
correspondent_account = ''
postal_address = ''
postcode = ''


def general_info_user(name_parameter, age_parameter, phone_parameter, email_parameter, extra_info_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    if extra_info:
        print('')
        print('Дополнительная информация:')
        print(extra_info)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        phone += ch

                email = input('Введите адрес электронной почты: ')
                extra_info = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # Information about the entrepreneur
                business_registration_number = input('Введите ОГРНИП (ОГРНИП состоит из 15 цифр): ')
                while len(business_registration_number) != 15:
                    print('Ошибка, ОГРНИП состоит из 15 цифр. Попробуйте снова')
                    business_registration_number = input('Введите ОГРНИП (ОГРНИП состоит из 15 цифр): ')
                tax_identification_number = input('Введите ИНН (ИНН состоит из 12 цифр): ')
                while len(tax_identification_number) != 12:
                    print('Ошибка, ИНН состоит из 12 цифр. Попробуйте снова')
                    tax_identification_number = input('Введите ИНН (ИНН состоит из 12 цифр): ')
                checking_account = input('Введите расчётный счёт (р/с состоит из 20 цифр): ')
                while len(checking_account) != 20:
                    print('Ошибка, р/с  состоит из 20 цифр. Попробуйте снова')
                    checking_account = input('Введите расчётный счёт (р/с состоит из 20 цифр): ')
                bank = input('Введите название банка: ')
                bank_identification_code = input('Введите БИК (БИК состоит из 6 цифр): ')
                while len(bank_identification_code) != 6:
                    print('Ошибка, БИК состоит из 6 цифр. Попробуйте снова')
                bank_identification_code = input('Введите БИК (БИК состоит из 6 цифр): ')
                correspondent_account = input('Введите корреспондентский счет (к/с состоит из 20 цифр): ')
                while len(correspondent_account) != 20:
                    print('Ошибка, к/с состоит из 20 цифр. Попробуйте снова')
                    correspondent_account = input('Введите корреспондентский счет (к/с состоит из 20 цифр): ')

            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone, email, extra_info)

            elif option2 == 2:
                general_info_user(name, age, phone, email, extra_info)

                # print Information about the entrepreneur
                print('')
                print('Информация о предпринимателе')
                print('ОГРНИП', business_registration_number)
                print('ИНН', tax_identification_number)
                print('Расчётный счёт', correspondent_account)
                print('Название банка', bank)
                print('БИК', bank_identification_code)
                print('Корреспондентский счёт', correspondent_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')