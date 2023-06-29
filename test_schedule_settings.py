from selene import browser, have, be

def test_edit_schedule_time():
    browser.open('https://preview.edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('liveUT00mPE8CB7Z').press_enter()
    browser.wait_until(browser.element('form > button:nth-child(4)').should(be.visible))
    browser.element('form > button:nth-child(4)').click()
    browser.wait_until(have.url('https://edvibe.com/TeacherAccount/lessons'))

    #Нажатие на кнопку Настройки
    browser.element('.tab-item:nth-child(1)').click()
    browser.element('.slider-right-menu .ui-button-base').click()

    #Настройка отображаемых часов (9:00-18:00)
    browser.element('.col:nth-child(1) .ui-select').click()
    browser.element('.col:nth-child(1) .option:nth-child(10)').click()
    browser.element('.col:nth-child(3) .ui-select').click()
    browser.element('.col:nth-child(3) .option:nth-child(9)').click()

    #Настройка местного времени (изменение на +5)
    browser.element('.row:nth-child(4) .ui-select').click()
    browser.element('.row:nth-child(4) .option:nth-child(18)').click()
    browser.element('.row:nth-child(1) .ui-button-base').click()

    browser.element('.col:nth-child(1) .ui-select .no-select-text').should(have.exact_text('9:00'))
    browser.element('.col:nth-child(3) .ui-select .no-select-text').should(have.exact_text('18:00'))
    browser.element('.row:nth-child(4) .ui-select .no-select-text').should(have.text('(UTC+5)'))
    browser.element('.tab-item:nth-child(4)').click()
    browser.element('.ui-dropdown.timezone .ui-select .no-select-text').should(have.text('(UTC+5)'))