import requests

# URL to the form you want to fill. formResponse should be used instead of viewform
url = 'https://docs.google.com/forms/d/e/1FAIpQLSe9UadZlyuyKmWvVOFk_McqH-7Yf7GdAgIys-YN8dNx0ttR1g/formResponse'

values = {
    # เพศ
    "entry.2135487583": 'ชาย',
    # อายุ
    "entry.1444539638": 15,
    # จังหวัดที่อาศัย
    "entry.253012881": 'กระบี่',
    # Q1 น้องๆ ใช้สื่อสังคมออนไลน์ เพื่ออะไรบ้าง (ตอบได้หลายข้อ)
    "entry.1723581244": '1.เพื่อเล่าเรื่องราว ความรู้สึก ความคิด ประสบการณ์ของตัวเองผ่านสื่อ',
    # Q2 น้องๆ ใช้เวลาบนโลกสังคมออนไลน์ส่วนใหญ่กับใครมากที่สุด (ตอบได้ข้อเดียว)
    "entry.703307181": '1. ตัวเอง',
    # Q3 น้องๆ ใช้สื่อสังคมออนไลน์ เพื่อสร้างความสัมพันธ์ที่ดีกับคนในครอบครัวอย่างไรบ้าง (ตอบได้หลายข้อ)
    "entry.22863560": '1.ใช้ติดต่อสื่อสารเรื่องทั่วไป เช่น โทร หรือส่งข้อความหากัน บอกธุระ ให้มารับ-ส่ง',
    # Q4 น้องๆ อยากบอกอะไรผู้ปกครองผ่านสื่อสังคมออนไลน์เนื่องในวันเด็กในปีใหม่นี้
    "entry.744610862": 'ทดสอบ',
    # น้องชอบแสดงความสามารถพิเศษอะไรบ้างลงบนสื่อสังคมออนไลน์
    "entry.429400605": '6. การถ่ายภาพ',
    # น้องใช้สื่ออะไรเพื่อโชว์ความสามารถพิเศษของตัวเอง
    "entry.2041938824": '1. Facebook',
    # นน้องคิดว่าฟังค์ชันไหนของสื่อที่น้องใช้เหมาะสมจะโชว์ความสามารถพิเศษของตัวเองมากที่สุด
    "entry.1423677825": ['4. ฟังก์ชัน Story', '5. ฟังก์ชันโพสข้อความ'],
}


def send_form(form, data):
    """It takes google form url which is to be submitted and also data which is a list of data to be submitted in the
    form iteratively. """
    requests.post(form, data)
    print('Submitted')


send_form(url, values)
