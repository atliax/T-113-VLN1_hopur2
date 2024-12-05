from StorageLayer.property_storage import PropertyStorage
from Model import Property

test = PropertyStorage('StorageLayer/test.json')

test2 = test.load_from_file(Property)

print(test2)
