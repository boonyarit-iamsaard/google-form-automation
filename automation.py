from selenium import webdriver
import random
import time
from questions import q1, q2, q3, q4, q5, q6, q7


# setting
time_sleep = 2
responses = 31

# url
web = webdriver.Chrome("C:/ProgramData/chocolatey/bin/chromedriver.exe")
web.get(
    "https://docs.google.com/forms/d/e/1FAIpQLScfiQ1e1_vsAtQVZhSYT0DSXzsE0Of_5Zpg_nWrl95YXVnDYw/viewform"
)

# set time delay
time.sleep(time_sleep)

# gender
gender_choices = [0, 1, 2]
gender_responses = random.choices(gender_choices, [11, 9, 1], k=responses)

# age
# age_choices = [13, 14, 15]
age_choices = [16, 17, 18, 19, 20]
age_responses = random.choices(age_choices, [3, 5, 9, 5, 4], k=responses)

# provinces
province_choices = [
    "กระบี่",
    "ชุมพร",
    "พัทลุง",
    "สงขลา",
    "สุราษฎร์ธานี",
    "นครศรีธรรมราช",
]
province_responses = random.choices(province_choices, [1, 2, 5, 4, 3, 6], k=responses)

# Q1
q1_answers = q1.answers()
q1_choices = q1.choices()
q1_answers_responses = q1.answers_responses(responses, q1_answers)
q1_response = q1.response(responses, q1_answers_responses, q1_choices)

# Q2
q2_answers = q2.answers()
q2_reponse = q2.response(responses, q2_answers)

# Q3
q3_answers = q3.answers()
q3_choices = q3.choices()
q3_answers_responses = q3.answers_responses(responses, q3_answers)
q3_response = q3.response(responses, q3_answers_responses, q3_choices)

# Q4
q4_answers = q4.answers()
q4_reponse = q4.response(responses, q4_answers)

# q5
q5_answers = q5.answers()
q5_choices = q5.choices()
q5_answers_responses = q5.answers_responses(responses, q5_answers)
q5_response = q5.response(responses, q5_answers_responses, q5_choices)

# qุ6
q6_answers = q6.answers()
q6_choices = q6.choices()
q6_answers_responses = q6.answers_responses(responses, q6_answers)
q6_response = q6.response(responses, q6_answers_responses, q6_choices)

# q7
q7_answers = q7.answers()
q7_choices = q7.choices()
q7_answers_responses = q7.answers_responses(responses, q7_answers)
q7_response = q7.response(responses, q7_answers_responses, q7_choices)


# automation
for i in range(responses):
    # section 1
    # gender
    gender_xpath = [
        web.find_element_by_xpath('//*[@id="i5"]/div[3]/div'),  # male
        web.find_element_by_xpath('//*[@id="i8"]/div[3]/div'),  # female
        web.find_element_by_xpath('//*[@id="i11"]/div[3]/div'),  # other
    ]
    gender_xpath[gender_responses[i]].click()

    # age
    age_xpath = web.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    age_xpath.send_keys(age_responses[i])

    # province
    province_xpath = web.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    # province_xpath.send_keys(province_responses[i])
    province_xpath.send_keys("สงขลา")

    # Q1
    time.sleep(time_sleep)
    q1_xpath = q1.xpath(web)
    for j in range(len(q1_response[i])):
        for k in range(len(q1_xpath)):
            if q1_response[i][j] == k:
                q1_xpath[k].click()

    # Q2
    q2_xpath = q2.xpath(web)
    for j in range(len(q2_xpath)):
        if q2_reponse[i] == j:
            q2_xpath[j].click()

    # Q3
    q3_xpath = q3.xpath(web)
    for j in range(len(q3_response[i])):
        for k in range(len(q3_xpath)):
            if q3_response[i][j] == k:
                q3_xpath[k].click()

    # Q4
    q4_xpath = web.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea'
    )
    q4_xpath.send_keys(q4_reponse[i])

    # next
    time.sleep(time_sleep)
    next_button = web.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span'
    )
    next_button.click()

    # section 2
    time.sleep(time_sleep)

    # Q5
    q5_xpath = q5.xpath(web)
    for j in range(len(q5_response[i])):
        for k in range(len(q5_xpath)):
            if q5_response[i][j] == k:
                q5_xpath[k].click()

    # Q6
    q6_xpath = q6.xpath(web)
    for j in range(len(q6_response[i])):
        for k in range(len(q6_xpath)):
            if q6_response[i][j] == k:
                q6_xpath[k].click()

    # Q7
    q7_xpath = q7.xpath(web)
    for j in range(len(q7_response[i])):
        for k in range(len(q7_xpath)):
            if q7_response[i][j] == k:
                q7_xpath[k].click()

    # submit
    time.sleep(time_sleep)
    submit_button = web.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span'
    )
    submit_button.click()

    # another response
    another_response = web.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[1]/div/div[4]/a"
    )
    another_response.click()

    print("สงขลา", i + 1)

# close
web.close()
