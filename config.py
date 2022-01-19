# This file MUST be configured in order for the code to run properly

# Make sure you put all your input images into an 'assets' folder. 
# Each layer (or category) of images must be put in a folder of its own.

# CONFIG is an array of objects where each object represents a layer
# THESE LAYERS MUST BE ORDERED.

# Each layer needs to specify the following
# 1. id: A number representing a particular layer
# 2. name: The name of the layer. Does not necessarily have to be the same as the directory name containing the layer images.
# 3. directory: The folder inside assets that contain traits for the particular layer
# 4. required: If the particular layer is required (True) or optional (False). The first layer must always be set to true.
# 5. rarity_weights: Denotes the rarity distribution of traits. It can take on three types of values.
#       - None: This makes all the traits defined in the layer equally rare (or common)
#       - "random": Assigns rarity weights at random. 
#       - array: An array of numbers where each number represents a weight. 
#                If required is True, this array must be equal to the number of images in the layer directory. The first number is  the weight of the first image (in alphabetical order) and so on...
#                If required is False, this array must be equal to one plus the number of images in the layer directory. The first number is the weight of having no image at all for this layer. The second number is the weight of the first image and so on...

# Be sure to check out the tutorial in the README for more details.                

CONFIG = [
    {
        'id': 1,
        'name': 'asset1',
        'directory': 'asset1',
        'required': True,
        'rarity_weights': [20, 16, 17, 8, 18, 15, 9, 6],
    },
    {
        'id': 2,
        'name': 'asset2',
        'directory': 'asset2',
        'required': True,
        'rarity_weights': [8, 24, 16, 20, 13, 19, 6],
    },
    {
        'id': 3,
        'name': 'asset3',
        'directory': 'asset3',
        'required': True,
        'rarity_weights': [6, 25, 15, 12, 20, 9, 16, 7, 15, 19, 5],
    },
    {
        'id': 4,
        'name': 'asset4',
        'directory': 'asset4',
        'required': False,
        'rarity_weights': [100, 9, 30, 20, 19, 25, 22, 33, 19, 12, 14, 18, 7, 3, 10, 24],
    },
    {
        'id': 5,
        'name': 'asset5',
        'directory': 'asset5',
        'required': True,
        'rarity_weights': [19, 12, 6, 12, 20, 24, 9, 8],
    },
    {
        'id': 5,
        'name': 'asset6',
        'directory': 'asset6',
        'required': False,
        'rarity_weights': [100, 24, 19, 6, 14, 20, 24, 12, 16],
    },
]
