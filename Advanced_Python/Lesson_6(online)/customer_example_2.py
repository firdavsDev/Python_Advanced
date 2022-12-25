from dataclasses import dataclass


def send_email(to: str, subject: str, body: str) -> None:
    """Send an email."""
    print(f"Sending email to {to}.")
    print(f"Subject: {subject}")
    print("Body:")
    print(body)


@dataclass
class Customer:
    """Customer"""
    id: str # customer id
    name: str # customer name
    email_address: str # customer email address

    def __post_init__(self): # call send email func
        self._send_welcome_email()

    def _send_welcome_email(self): # send welcome email is provided
        subject = "Welcome to our platform!"
        body = (
            f"Hi, {self.name}, we're so glad you joined our platform."
        )
        send_email(self.email_address, subject, body) # call send email func

"""
Xulosa:

BU yerda Customer classini yaratib, unga id, name va email_address parametrlarini berib,
post_init methodida _send_welcome_email methodini chaqirib, uning ichida send_email funcsiyasi chaqiriladi. 
Chunki  uning ichida send_email funcsiyasi chaqiriladi. 
send_email funcsiyasi emailni jo'natadi.

SMS yoki email yulash uchun asosan bir tashqari servisdan foydalaniladi. 
Tashqari servisga bog'laniladigan url endpointlarni foydalanuvchi kursatilmaydi.
        
"""
