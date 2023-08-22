def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    name_list = []
    for name in names:
        name_list.append(f'Hello, my name is {name}.')
    return name_list

def assign_rooms(names):
    assign_room = []
    x = 1
    for name in names:
        assign_room.append(f"Hello, {name}! You'll be assigned to room {x}!")
        x+=1
    return assign_room

def printer(names):
  for name in batch_badge_creator(names):
    print(name)

  for name in assign_rooms(names):
    print(name)