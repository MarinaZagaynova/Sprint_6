import allure
import pytest

import data


class Testorder_pagePage:

    @allure.title("Проверка оформления заказа и проверка перехода к блоку оформленния заказа с 2 мест")
    @pytest.mark.parametrize('name, family_name, address, metro, phone, comment',
                             [[data.name, data.family_name, data.address, data.metro,
                               data.phone, data.comment],
                              [data.name, data.family_name, data.address, data.metro, data.phone,
                               data.comment],
                              [data.name, data.family_name, data.address, data.metro, data.phone,
                               data.comment]])
    def test_order_page(self, name, family_name, address, metro, phone, comment, order_page):
        order_page.click_main_button_order()
        order_page.check_open_page_order()
        order_page.click_logo_scooter()
        order_page.check_open_main_page()
        order_page.scrool_subheader()
        order_page.click_element_order()
        order_page.check_open_page_order()
        order_page.set_name(name)
        order_page.set_family_name(family_name)
        order_page.set_address(address)
        order_page.set_metro(metro)
        order_page.set_phone(phone)
        order_page.click_next()
        order_page.set_when()
        order_page.set_term()
        order_page.set_color()
        order_page.set_comment(comment)
        order_page.click_order()
        order_page.click_yes()
        order_page.check_order()

