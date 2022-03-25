class trivet:

    def __init__(self, size, identification, position, lockedStatus):
        self.size = size
        self.identification = identification
        self.position = position
        self.lockedStatus = lockedStatus

    def get_id(self):
        return self.identification

    def get_position(self):
        return self.position

    def get_locked(self):
        return self.lockedStatus