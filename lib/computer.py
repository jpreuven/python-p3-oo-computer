class Computer:

    def __init__ (self, brand, model, memory_GB = 8, storage_free = 1000):
        self.brand = brand
        self.model = model
        self.memory_GB = memory_GB
        self.storage_free = storage_free

    def get_brand(self):
        return self._brand ##maybe underscore here? Why yes/no?
    
    def set_brand(self, brand):
        self._brand = brand

    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self._model = model
    
    brand = property(get_brand, set_brand)
    model = property(get_model, set_model)


if __name__ == "__main__":
    # you can write test code here
    # or in debug.py
    Computer("Mac", "Air")
    Computer.brand
    
    pass
