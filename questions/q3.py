import random


def answers():
    return [1, 2, 3]  # number of answers for each response


def answers_responses(responses, answers):
    return random.choices(answers, [2, 3, 1], k=responses)


def choices():
    return [0, 1, 2, 3, 4, 5]


def response(responses, answers, choices):
    response = []

    for i in range(responses):
        response.append(
            list(
                set(
                    random.choices(
                        choices,
                        [10, 5, 8, 1, 4, 4],
                        k=answers[i],
                    )
                )
            )
        )

    return response


def xpath(web):
    return [
        web.find_element_by_xpath('//*[@id="i81"]'),
        web.find_element_by_xpath('//*[@id="i84"]'),
        web.find_element_by_xpath('//*[@id="i87"]'),
        web.find_element_by_xpath('//*[@id="i90"]'),
        web.find_element_by_xpath('//*[@id="i93"]'),
        web.find_element_by_xpath('//*[@id="i96"]'),
    ]
