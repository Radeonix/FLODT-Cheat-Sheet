menu:
    s "I am Scarlett saying something during a selection menu."

    "Blank":
        jump label
    "Blank":
        jump label

#Slide on-screen
#easeinright is also viable
show s flirt at pos35s with easeinleft

#Slide off-screen
#Note that the offset may vary +/- 100 based on the character AND THE OFFSET WILL REMAIN WHILE THE SPRITE DOES
#Not intended for long scenes: use for character exit frame into hide
#Never hide a character immediately after anything using "linear #.#" as renpy is fast enough that it will start the movement and then instantly hide the character
    #Hide after one ling of dialogue
show y blush:
    linear 0.2 offscreenright yoffset 900

#twitch/vjump
show y dizzy:
    twitch

#General movement across the screen
show y dizzy:
    linear 0.2 ypos 1.76 xpos 0.65

#Camera function (by default points to "master" layer which only has character sprites on it)

#Perspective is always needed or it borks for me
#zpos 100 is the starting position of the camera, remove it to just default to where the camera already is
#"linear 0.5 zpos -100" moves linearly for 0.5 seconds to zpos -100
#Remember that the camera is looking ALONG the z axis, so a higher number zooms out (moves things away)
camera:
    perspective True
    zpos 100
    linear 0.5 zpos -100
#calling camera again will close the camera as it can bork some transitions as stated in RenPy documentation
#Just think of it as a resource like an open/read file and ensure it is also closed when not in use
camera

#the same as before except the camera is now affecting only the background and not character sprites
camera background:
    perspective True
    zpos 100
    linear 0.5 zpos -100
camera

#Layers

#Here is showing a predefined image on the layer "extra"
#Keep in mind that when using "onlayer", "with dissolve" will tend to fail and I haven't found the correct syntax for it yet
    #ie "show FakeRenpyCrash1 onlayer extra with dissolve" will NOT display as expected
show FakeRenpyCrash1 onlayer extra

#Use python to call renpy directly to clear a specific layer
#No pre-defined clear method, but "scene" will clear a layer before pasting an image whereas "show" would just slap it overtop
    #so scene with no image attatched just clears
$ renpy.scene("master")

#enables developer console and settings inside FLODT
#ensure to set to False before ANY release
#use Shift+d to access some of the menues
define config.developer = True

#a note I'd like to remind people about
#jump vs call on a label:
    #jump will go to the specified label with no path back
    #call will allow renpy to return to the original script at the point the call was made if it ever hits a "Return()" in the called label