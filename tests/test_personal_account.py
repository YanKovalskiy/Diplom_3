import allure


class TestPersonalAccount:

    @allure.title("Проверка перехода в личный кабинет по ссылке 'Личный кабинет' в шапке")
    def test_go_to_personal_account_by_link_header(self, login_page, header, account_profile_page, login_details):
        login_page.open_login_page()
        login_page.logining(login_details)
        header.click_by_link_personal_account()
        account_profile_page.wait_loading_page()
        assert header.current_url == account_profile_page.ACCOUNT_PROFILE_PAGE_URL

    @allure.title("Проверка переход в раздел личного кабинета 'История заказов'")
    def test_go_to_order_history_section_by_click_link_order_history(self, login_page, header, account_profile_page,
                                                                     account_order_history_page, login_details):
        login_page.open_login_page()
        login_page.logining(login_details)
        header.click_by_link_personal_account()
        account_profile_page.click_link_order_history()
        assert account_profile_page.current_url == account_order_history_page.ACCOUNT_ORDER_HISTORY_PAGE_URL

    @allure.title("Проверка выхода из аккаунта")
    def test_exit_from_personal_account(self, login_page, header, account_profile_page,
                                        account_order_history_page, login_details):
        login_page.open_login_page()
        login_page.logining(login_details)
        header.click_by_link_personal_account()
        account_profile_page.click_button_exit()
        login_page.wait_loading_page()
        assert account_profile_page.current_url == login_page.LOGIN_PAGE_URL
