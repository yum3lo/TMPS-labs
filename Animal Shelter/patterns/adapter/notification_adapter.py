from abc import ABC, abstractmethod

class NotificationSystem(ABC):
  @abstractmethod
  def send_notification(self, recipient: str, message: str):
    pass

class EmailNotification(NotificationSystem):
  def send_notification(self, recipient: str, message: str):
    print(f"Email sent to {recipient}: \n{message}")

class SMSNotification(NotificationSystem):
  def send_notification(self, recipient: str, message: str):
    print(f"SMS sent to {recipient}: {message}")

class NotificationAdapter:
  def __init__(self, notification_system: NotificationSystem):
    self.notification_system = notification_system

  def notify(self, recipient: str, message: str):
    self.notification_system.send_notification(recipient, message)