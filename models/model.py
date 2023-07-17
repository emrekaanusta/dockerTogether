class projectService:
    

    def _init_(self):
        self.name = None
        self.description = None
        self.project = None
    
class deviceService:

    def _init_(self):
        self.device_number = None
        self.device_ip = None
        self.device_port = None
        self.device_username = None
        self.device_password = None

projects = projectService()
devices = deviceService()