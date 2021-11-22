from sys import platform
from ursina import *
from ursina import texture
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from ursina.prefabs.sprite import Sprite
from ursina import Ursina, printvar
from PIL import Image
from ursina.prefabs.file_browser_save import FileBrowserSave
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
from ursina.prefabs.memory_counter import MemoryCounter
block_pick = 1
world_size = 30

app = Ursina()
window.fullscreen = True

grass_texture = load_texture('assets/blocks/grass.png')

stone_texture = load_texture('assets/blocks/stone.png')

stone_brick_texture = load_texture('assets/blocks/stonebrick.png')

chiseled_stone_brick_texture = load_texture('assets/blocks/stonebrickchiseled.png')

dirt_texture = load_texture('assets/blocks/dirt.png')

sand_texture = load_texture('assets/blocks/sand.png')

dogface_texture = load_texture('assets/blocks/dogface.png')

fyou_texture = load_texture('assets/blocks/fyou.png')

log_texture = load_texture('assets/blocks/oaklogside.png')

kiara_pretty = load_texture('assets/blocks/kiara.png')

sky_texture = load_texture('assets/misc/sky2.png')

break_sound = Audio('assets/sfx/blockbreak.wav', loop = False, autoplay = False)

block_pick = 1

def update():
    global block_pick

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['5']: block_pick = 5
    if held_keys['6']: block_pick = 6
    if held_keys['7']: block_pick = 7
    if held_keys['8']: block_pick = 8
    if held_keys['9']: block_pick = 9
    if held_keys['0']: block_pick = 0

class Voxel(Button):
    def __init__(self, position=(0,0,0), texture = kiara_pretty):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y =.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                break_sound.play()
                if block_pick == 1: voxel = Voxel(position=self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, texture = stone_texture)
                if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal, texture = stone_brick_texture)
                if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal, texture = chiseled_stone_brick_texture)
                if block_pick == 5: voxel = Voxel(position=self.position + mouse.normal, texture = dirt_texture)
                if block_pick == 6: voxel = Voxel(position=self.position + mouse.normal, texture = sand_texture)
                if block_pick == 7: voxel = Voxel(position=self.position + mouse.normal, texture = dogface_texture)
                if block_pick == 8: voxel = Voxel(position=self.position + mouse.normal, texture = fyou_texture)
                if block_pick == 9: voxel = Voxel(position=self.position + mouse.normal, texture = log_texture)
                if block_pick == 0: voxel = Voxel(position=self.position + mouse.normal, texture = kiara_pretty)

            if key == 'left mouse down':
                break_sound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True
            )

for z in range(world_size):
    for x in range(world_size):
        voxel = Voxel(position=(x,0,z))

DropdownMenu('File', buttons=(
    DropdownMenuButton('New'),
    DropdownMenuButton('Open'),
    DropdownMenu('Reopen Project', buttons=(
        DropdownMenuButton('Project 1'),
        DropdownMenuButton('Project 2'),
        )),
    DropdownMenuButton('Save'),
    DropdownMenu('Options', buttons=(
        DropdownMenuButton('Option a'),
        DropdownMenuButton('Option b'),
        )),
    DropdownMenuButton('Exit'),
    ))

#player = PlatformerController2d()
player = FirstPersonController()



sky = Sky()
app.run()