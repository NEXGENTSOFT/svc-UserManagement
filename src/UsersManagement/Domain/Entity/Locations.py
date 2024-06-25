import uuid


class Locations:
    def __init__(self, latitude, altitude, longitude, user_uuid):
        self.uuid = uuid.uuid4()
        self.latitude = latitude
        self.altitude = altitude
        self.longitude = longitude
        self.user_uuid = user_uuid