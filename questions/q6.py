import random


def answers():
    return [1, 2, 3, 4]  # number of answers for each response


def answers_responses(responses, answers):
    return random.choices(answers, [3, 4, 2, 2], k=responses)


def choices():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def response(responses, answers, choices):
    response = []

    for i in range(responses):
        response.append(
            list(
                set(
                    random.choices(
                        choices,
                        [9, 7, 6, 5, 2, 8, 1, 1, 1, 1],
                        k=answers[i],
                    )
                )
            )
        )

    return response


def xpath(web):
    return [
        web.find_element_by_xpath('//*[@id="i32"]'),
        web.find_element_by_xpath('//*[@id="i35"]'),
        web.find_element_by_xpath('//*[@id="i38"]'),
        web.find_element_by_xpath('//*[@id="i41"]'),
        web.find_element_by_xpath('//*[@id="i44"]'),
        web.find_element_by_xpath('//*[@id="i47"]'),
        web.find_element_by_xpath('//*[@id="i50"]'),
        web.find_element_by_xpath('//*[@id="i53"]'),
        web.find_element_by_xpath('//*[@id="i56"]'),
        web.find_element_by_xpath('//*[@id="i59"]'),
    ]
