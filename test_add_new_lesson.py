from selene import browser, have, be

def test_add_new_individual_lesson():
    browser.open('https://preview.edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('liveUT00mPE8CB7Z').press_enter()
    browser.wait_until(browser.element('form > button:nth-child(4)').should(be.visible))
    browser.element('form > button:nth-child(4)').click()
    browser.wait_until(have.url_containing('/TeacherAccount/'))

    #Добавление нового урока
    browser.element('.tab-item:nth-child(1)').click()
    browser.element('.hour:nth-child(64)').click()
    browser.element('.ui-search > input').type('dima@yandex.ru')
    browser.element('.box-text .long-text').should(have.exact_text('dima@yandex.ru'))
    browser.element('.scroll-content .container-box-sizing').click()
    browser.element('.ui-checkbox .point').click()
    browser.element('.row:nth-child(1) .placeholder').click()
    browser.element('.ui-options.active .option:nth-child(6)').click()
    browser.element('.row:nth-child(3) .ui-select').click()
    browser.element('.ui-options.active .option:nth-child(3)').click()
    browser.element('.pb-0 .ui-button-base').click()

    #Проверка, что урок добавлен и он повторяется
    browser.element('.hour:nth-child(64) .ui-scheduler-table-lesson').should(be.visible)
    i = 0
    while i < 4:
        browser.element('.toggler.next.col').click()
        browser.element('.hour:nth-child(64) .ui-scheduler-table-lesson').should(be.visible)
        i += 1
    browser.element('.toggler.next.col').click()
    browser.element('.hour:nth-child(64) > div > div').should(have.css_class('add-lesson'))

    #Удаление урока
    n = 0
    while n < 5:
        browser.element('.toggler.prev').click()
        n += 1

    browser.wait_until(browser.element('.hour:nth-child(2)').should(have.css_class('past')))
    browser.element('.hour:nth-child(64) .ui-scheduler-table-lesson').click()
    browser.element('.pr-5 .ui-button-base').click()
    browser.element('.item-button:nth-child(1) .ui-button-base').click()
    browser.element('.wrapper:nth-child(3) .item-button:nth-child(2) .ui-button-base').click()

    #Проверка, что повторяющиеся уроки удалены
    browser.element('.hour:nth-child(64) > div > div').should(have.css_class('add-lesson'))
    k = 0
    while k < 4:
        browser.element('.toggler.next.col').click()
        browser.element('.hour:nth-child(64) > div > div').should(have.css_class('add-lesson'))
        k += 1