import os
from selene import browser, have
from selene.core.command import js
import allure
import tests

@allure.title('Успешное заполнение формы регистарции')
def test_fill_registration_form():
    with allure.step("Открываем главну страницу"):
        browser.open('https://demoqa.com/automation-practice-form')

    with allure.step("Заполняем имя"):
        browser.element('#firstName').type("Test_Name")
    with allure.step("Заполняем фамилию"):
        browser.element('#lastName').type("Test_LastName")
    with allure.step("Заполняем email"):
        browser.element('#userEmail').type("ak_test@test.ru")
    with allure.step("Заполняем поле пол"):
        browser.all("[for^=gender-radio]").element_by(have.exact_text('Female')).click()
    with allure.step("Вводим номер телефона"):
        browser.element('#userNumber').type('89991232123')

    with allure.step("Заполняем дату рождения"):
        browser.element('#dateOfBirthInput').click()
        browser.all('.react-datepicker__month-select>option').element_by(have.exact_text('September')).click()
        browser.all('.react-datepicker__year-select>option').element_by(have.exact_text('2002')).click()
        browser.element('.react-datepicker__day--007').click()

    with allure.step("Заполняем поле предмет"):
        browser.element('#subjectsInput').type('History').press_enter()

    with allure.step("Отмечаем хобби"):
        browser.all(".custom-checkbox").element_by(have.exact_text("Sports")).click()

    with allure.step("Загружаем фотографию"):
        browser.element("#uploadPicture").send_keys(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), f"resources/student.jpeg")
            )
        )

    with allure.step("Вводим текущий адрес"):
        browser.element('#currentAddress').type('Testovaya st. 43-33')

    with allure.step("Выбираем штат"):
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text("NCR")
        ).click()

    with allure.step("Выбираем город"):
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text("Delhi")
        ).click()

        browser.element('#submit').perform(command=js.click)

    with allure.step( 'Проверяем таблицу с данными'):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element(".table").all("td").even.should(
            have.exact_texts(
                "Test_Name Test_LastName",
                "ak_test@test.ru",
                "Female",
                "8999123212",
                "07 September,2002",
                "History",
                "Sports",
                "student.jpeg",
                "Testovaya st. 43-33",
                "NCR Delhi",
            )
        )