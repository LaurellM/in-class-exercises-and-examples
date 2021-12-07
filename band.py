# dictionary where the keys are the band names and the values are info
bands_dict = {
#    'key': 'value', 
#   'key2': 'value2',
    'Jimmy Eat World': {'members': 5},
    'Queen': {'members': 4},
    'Andrew Bird': {'members': 4},
    'The Band': {'members': 4},
    'Led Zepplin': {'members': 4},
}
# add a band to this dictionary
bands_dict["Mac Miller"] = {'members': 1}
# obtain vaflues by foding Name-of-dict['key']
print(f'The band "Led Zepplin" has {bands_dict["Led Zepplin"]["members"]} members')

# print(f'The band "Andrew Bird" has {bands_dict["Andrew Bird"]["members"]} members')
