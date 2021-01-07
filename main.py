from plyer import notification
import time


def desk_notify(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="clock-icon.ico",
        timeout=2
    )


if __name__ == '__main__':
    while True:
        time.sleep(1800)
        desk_notify("Hey , Take a break babe !", "You should give rest to your mind and eyes for a minute or two.")
