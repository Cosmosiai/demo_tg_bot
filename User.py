from status import user_status
class User:
    def __init__(self, name, tg_id):
        self.name=name
        self.tg_id=tg_id
        self.status = user_status.active
        self.role = "user"
    
    def delete_user(self):
        self.status = user_status.deactivated
    
class User_DTO:
    def __init__(self, name):
        self.name=name
    
    def __repr__(self):
        return f"User_DTO(name={self.name})"