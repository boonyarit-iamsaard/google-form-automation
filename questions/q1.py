import random


def answers():
    return [1, 2, 3, 4, 5]  # number of answers for each response


def answers_responses(responses, answers):
    return random.choices(answers, [1, 5, 4, 3, 2], k=responses)


def choices():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def response(responses, answers, choices):
    response = []

    for i in range(responses):
        response.append(
            list(
                set(
                    random.choices(
                        choices,
                        [11, 10, 9, 2, 4, 3, 8, 6, 5, 7, 1],  # 16-20 years old
                        k=answers[i],
                    )
                )
            )
        )

    return response


def xpath(web):
    return [
        web.find_element_by_xpath('//*[@id="i27"]'),
        web.find_element_by_xpath('//*[@id="i30"]'),
        web.find_element_by_xpath('//*[@id="i33"]'),
        web.find_element_by_xpath('//*[@id="i36"]'),
        web.find_element_by_xpath('//*[@id="i39"]'),
        web.find_element_by_xpath('//*[@id="i42"]'),
        web.find_element_by_xpath('//*[@id="i45"]'),
        web.find_element_by_xpath('//*[@id="i48"]'),
        web.find_element_by_xpath('//*[@id="i51"]'),
        web.find_element_by_xpath('//*[@id="i54"]'),
        web.find_element_by_xpath('//*[@id="i57"]'),
    ]
