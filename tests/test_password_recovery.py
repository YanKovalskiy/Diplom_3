import allure


class TestPasswordRecovery:

    @allure.title("Проверка перехода на страницу восстановления пароля по ссылке 'Восстановить пароль'")
    def test_go_to_password_recovery_page_by_clicking_recover_password_link(self, login_page, forgot_password_page):
        login_page.open_login_page()
        login_page.click_link_recovery_password()
        with allure.step(f'Проверяем текущий url (URL = {login_page.current_url})'):
            assert login_page.current_url == forgot_password_page.FORGOT_PASSWORD_PAGE_URL
