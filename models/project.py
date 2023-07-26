
from typing import Optional


class Project:    
    name: str
    description: Optional[str]
    device: str

    def __init__(self,name,description,device):
        self.name = name
        self.description = description
        self.device = device

    
