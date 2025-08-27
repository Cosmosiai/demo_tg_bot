from status import user_status
class User:
    def __init__(self, name, tg_id):
        self.name=name
        self.tg_id=tg_id
        self.status = user_status.active
    
    def delete_user(self):
        self.status = user_status.deactivated
        