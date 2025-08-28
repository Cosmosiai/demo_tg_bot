from status import room_status
class Room:
    def __init__(self, room):
        self.room=room
        self.status = room_status.active
    
    def delete_room(self):
        self.status = room_status.deactivated
    
class Room_DTO:
    def __init__(self, room):
        self.room=room
    
    def __repr__(self):
        return f"Room_DTO(room={self.room})"