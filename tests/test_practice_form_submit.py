from qa_guru_7_12.data import users
from qa_guru_7_12.pages.registration_page import RegistrationPage
import allure
from allure_commons.types import Severity


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Registration form')
@allure.story('Assert registered user')
@allure.link('https://demoqa.com/automation-practice-form')
def test_successful_student_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()

    # WHEN
    registration_page.register_user(users.student)

    # THEN
    registration_page.should_register_user(users.student)