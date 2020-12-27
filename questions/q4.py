import random


def answers():
    # age 13-15 ปี
    return [
        "อยากได้คอมพิวเตอร์ใหม่",
        "อยากให้คุณพ่อคุณแม่พาไปเที่ยว",
        "อยากได้โทรศัพท์ หรือ ipad ใหม่ เพื่อใช่ในการเรียน",
        "จะตั้งใจเรียน",
        "จะเป็นเด็กดี",
        "จะประหยัด ไม่ใช้จ่ายฟุ่มเฟือย",
    ]


def response(responses, answers):
    return random.choices(answers, [4, 3, 5, 5, 6, 3], k=responses)
