
import os

print(type(os.environ.keys()))


for key in os.environ.keys():
    print(key, os.environ[key])
