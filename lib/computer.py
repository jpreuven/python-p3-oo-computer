
class Computer:

    all = []

    def __init__ (self, brand, model, memory_GB = 8, storage_free = 1000):
        self._brand = brand
        self._model = model
        self.memory_GB = memory_GB
        self.storage_free = storage_free
        Computer.all.append(self)


    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model
    
    def get_memory_GB(self):
        return self._memory_GB

    def set_memory_GB(self, memory_GB):
        self._memory_GB = memory_GB

    def get_storage_free(self):
        return self._storage_free
    
    def set_storage_free(self, storage_free):
        if 0 <= storage_free <= 1000:
            self._storage_free = storage_free
        else:
            raise Exception

    memory_GB = property(get_memory_GB, set_memory_GB)
    storage_free = property(get_storage_free, set_storage_free)

    def upgrade_memory(self, RAM):
        if type(RAM) == dict:
            self.memory_GB += RAM["size"]
        else:
            print("RAM needs to be an dictionary")

    def is_disk_full(self, file_size):
        return file_size < self.storage_free

    def save_file(self, file):
        # {"name": "word", "size": 20}
        if type(file) == dict:
            if self.is_disk_full(file["size"]):
                self.storage_free -= file["size"]
                print(f"{file['name']} has been saved!")
            else:
                print(f"There is not enough space on disk to save {file['name']}.")

        else:
            raise Exception

    def delete_file(self, file):
        # {"name": "word", "size": 20}
        if type(file) == dict:
            self.storage_free += file["size"]
            print(f"{file['name']} has been deleted.")
        else:
            raise Exception

    def specs(self):
        print(f"Current memory: {self.memory_GB}GB \nFree Storage: {self.storage_free}GB")
    
    @classmethod
    def brands(cls):
        set_of_brands = ', '.join(set([computer.brand for computer in cls.all]))
        print("Here are our computer brands:", set_of_brands)

    @classmethod
    def models(cls):
        set_of_models = ', '.join(set([computer.model for computer in cls.all]))
        print("Here are our computer models:", set_of_models)

    @classmethod
    def largest_memory(cls):
        largest = sorted([computer for computer in cls.all], key=lambda c:c.memory_GB)
        print(largest[-1].brand)


mac = Computer("Mac", "Earth", 8, 500)
windows = Computer("Windows", "Wind", 15, 500)
linux = Computer("Linux", "Fire", 20, 500)
mac2 = Computer("Mac", "Water", 2, 500)

