from plyer import notification

class Notify:
    
    def doNotify(self, title, message, app_name, app_icon):
        notification.notify(
            title=title,
            message=message,
            app_name=app_name,
            app_icon=app_icon
        )