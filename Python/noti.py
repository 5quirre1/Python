from plyer import notification

def send_notification(title, message, timeout=5):
    notification.notify(
        title=title,
        message=message,
        timeout=timeout
    )

if __name__ == "__main__":
    print("sending test notification...")
    send_notification("AHHH", "=AHHH", 5)
    print("notification sent..")
