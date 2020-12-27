import random


def answers():
    return [1, 2, 3, 4]  # number of answers for each response


def answers_responses(responses, answers):
    return random.choices(answers, [4, 3, 2, 1], k=responses)


def choices():
    return [0, 1, 2, 3, 4, 5, 6]


def response(responses, answers, choices):
    response = []

    for i in range(responses):
        response.append(
            list(
                set(
                    random.choices(
                        choices,
                        [1, 4, 5, 1, 3, 7, 6],
                        k=answers[i],
                    )
                )
            )
        )

    return response


def xpath(web):
    return [
        web.find_element_by_xpath('//*[@id="i6"]'),
        web.find_element_by_xpath('//*[@id="i9"]'),
        web.find_element_by_xpath('//*[@id="i12"]'),
        web.find_element_by_xpath('//*[@id="i15"]'),
        web.find_element_by_xpath('//*[@id="i18"]'),
        web.find_element_by_xpath('//*[@id="i21"]'),
        web.find_element_by_xpath('//*[@id="i24"]'),
    ]
