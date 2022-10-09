# Function 1
def hello(greeting):
    print(greeting)
hello('Howdy!')

music_artists = ('Nas', '2Pac', 'The Notorious B.I.G.')
print(music_artists)

# Function 2
def pack(item1, item2, item3):
    return [item1, item2, item3]
print (pack('shirts', 'pants', 'shoes'))

# Function 3
def eat_lunch(lunchbox):
    if len(lunchbox) == 0:
        print('My lunchbox is empty!')
    else:
        for i in range(len(lunchbox)):
            if i == 0:
                print(f"First I eat {lunchbox[0]}")
            else:
                print(f"Next I eat {lunchbox[i]}")
eat_lunch([])
eat_lunch(['sandwhich', 'chips', 'apple', 'cookie'])
