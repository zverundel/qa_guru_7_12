import allure
from qa_guru_7_12.data import users
from qa_guru_7_12.pages.registration_page import RegistrationPage


@allure.tag('registration')
@allure.label("owner", "AlterAyrol")
@allure.epic('Тестирование вкладок в боковом меню')
@allure.feature('Раздел Practice Form')
@allure.story("Пользователь заполняет форму регистрации тестовыми данными.")
def test_successful_student_registration_form(browser_open_url):
    registration_page = RegistrationPage()

    registration_page.open()

    # WHEN
    registration_page.register_user(users.student)

    # THEN
    registration_page.should_register_user(users.student)