class ApiServiceKeys:
    def __init__(self):
        self.service_keys={
            'googlemaps':'<overwrite>'
        }
    
    def get_service_key(self):
        return self.service_keys