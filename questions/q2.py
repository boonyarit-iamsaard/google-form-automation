import random


def answers():
    return [0, 1, 2]


def response(responses, answers):
    return random.choices(answers, [9, 7, 1], k=responses)


def xpath(web):
    return [
        web.find_element_by_xpath('//*[@id="i67"]/div[3]/div'),
        web.find_element_by_xpath('//*[@id="i70"]/div[3]/div'),
        web.find_element_by_xpath('//*[@id="i73"]/div[3]/div'),
    ]
