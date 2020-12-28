import random


def answers():
    return [1, 2, 3, 4]  # number of answers for each response


def answers_responses(responses, answers):
    return random.choices(answers, [4, 3, 2, 1], k=responses)


def choices():
    return [0, 1, 2, 3, 4, 5, 6, 7]


def response(responses, answers, choices):
    response = []

    for i in range(responses):
        response.append(
            list(
                set(
                    random.choices(
                        choices,
                        [4, 7, 6, 5, 8, 1, 1, 1],
                        k=answers[i],
                    )
                )
            )
        )

    return response


def xpath(web):
    return [
        web.find_element_by_xpath('//*[@id="i67"]'),
        web.find_element_by_xpath('//*[@id="i70"]'),
        web.find_element_by_xpath('//*[@id="i73"]'),
        web.find_element_by_xpath('//*[@id="i76"]'),
        web.find_element_by_xpath('//*[@id="i79"]'),
        web.find_element_by_xpath('//*[@id="i82"]'),
        web.find_element_by_xpath('//*[@id="i85"]'),
        web.find_element_by_xpath('//*[@id="i88"]'),
    ]
