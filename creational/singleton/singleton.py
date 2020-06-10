class Singleton:
    INSTANCE = None
    init_count = 0

    def __init__(self):
        self.init_count += 1

    @staticmethod
    def get_instance():
        # Uses lazy initialization for creating the singleton object
        if Singleton.INSTANCE is None:
            Singleton.INSTANCE = Singleton()
        return Singleton.INSTANCE

    def get_init_count(self):
        return self.init_count
