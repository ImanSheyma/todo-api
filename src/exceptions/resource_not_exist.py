class ResourceNotExist(Exception):
    def __init__(self, resource: str):
        super().__init__(f"{resource} does not exist")