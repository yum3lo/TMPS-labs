from abc import ABC, abstractmethod
from typing import Dict

class EmailService:
  def send_email(self, email_address: str, subject: str, body: str):
    print(f"\nEmail sent to {email_address}")
    print(f"Subject: {subject}")
    print(f"Body:\n{body}")

class SMSService:
  def send_sms(self, phone_number: str, text: str):
    print(f"\nSMS sent to {phone_number}")
    print(f"Message:\n{text}")

class NotificationSystem(ABC):
  @abstractmethod
  def send_notification(self, contact: str, message: str):
    pass

class EmailAdapter(NotificationSystem):
  def __init__(self):
    self.email_service = EmailService()

  def send_notification(self, contact: str, message: str):
    self.email_service.send_email(
      email_address=contact,
      subject="Animal Shelter Update",
      body=message
    )

class SMSAdapter(NotificationSystem):
  def __init__(self):
    self.sms_service = SMSService()

  def send_notification(self, contact: str, message: str):
    sms_message = self._format_for_sms(message)
    self.sms_service.send_sms(
      phone_number=contact,
      text=sms_message
      )

  def _format_for_sms(self, message: str) -> str:
    max_length = 160
    formatted_message = ". ".join(
      line.strip() for line in message.split('\n') if line.strip()
    )
    return (
      formatted_message[:max_length - 3] + "..."
      if len(formatted_message) > max_length
      else formatted_message
    )

class NotificationManager:
  def __init__(self):
    self.email_adapter = EmailAdapter()
    self.sms_adapter = SMSAdapter()
    self.contact_preferences: Dict[str, tuple[str, str]] = {}

  def set_contact_preference(self, role: str, contact_type: str, contact: str):
    if contact_type not in {"email", "sms"}:
      raise ValueError("Contact type must be 'email' or 'sms'.")
    self.contact_preferences[role] = (contact_type, contact)

  def notify(self, role: str, message: str):
    if role not in self.contact_preferences:
      print(f"No contact preference set for role: {role}")
      return

    contact_type, contact = self.contact_preferences[role]

    if contact_type == 'email':
      self.email_adapter.send_notification(contact, message)
    elif contact_type == 'sms':
      self.sms_adapter.send_notification(contact, message)