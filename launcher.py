from multiprocessing import Process, Queue, Pipe

pak_storage_location = "C:/XLab_Projects/PakFileSys/mrsv-pak-storage/"
pak_ID_num = 2

pak_file = open(pak_storage_location + "placeholder" + str(pak_ID_num) + ".txt", "r")
new_pak = pak_file.read()

print(new_pak)

#Sprites = assets
#Condition = environmental conditions
#Data = identification
#Display config = camera viewpoint
#Preset = last saved point

class Pak:
    def __init__(self, sprites, condition, data, display_config, preset):
        self.sprites = sprites
        self.condition = condition
        self.data = data
        self.display_config = display_config
        self.preset = preset
