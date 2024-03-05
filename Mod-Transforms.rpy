#linear (speed of movement, lower being faster) (y/x)offset distance
#for "twitch" and "vjump", simply use the same way of showing a character but do "at twitch, (position)"
#ex: show k surprised at twitch, mid
    #or:
        #show k:
            #twitch
            #mid

#Custom twitch for an image
transform twitch:
    xoffset 0
    #block not 100% needed, just looks neater
    block:
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        repeat 2
    #resets back to original position if not already there
    linear 0.05 xoffset 0

#Custom larger twitch for an image
#Smaller twitch can be much harder to see if a camera/sprite moves at the same time
transform twitchL:
    xoffset 0
    #block not 100% needed, just looks neater for the loop
    block:
        linear 0.05 xoffset 10
        linear 0.05 xoffset -10
        repeat 2
    #easeout
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    #resets back to original position if not already there
    linear 0.05 xoffset 0

#Custom jump for an image
#"jump" cannot be used as a variable name as it is a renpy keyword, so vjumnp is used instead
transform vjump:
    yoffset 0
    linear 0.1 yoffset -20
    linear 0.15 yoffset -25
    linear 0.15 yoffset -20
    linear 0.1 yoffset 0
    #resets back to original position

#Camera + 3D setup
#FLODT will now function in a 3d space, allowing images to move along the z-axis
#higher the number, the further the image is
#used the exact same way as xpos, ypos, xalign, y align, etc
define config.perspective = (0, 1251, 100000)

#Layers

#This broke the initial chapter bg from being shown, needed scene to clear "background" for some reason
#It breaks most things actually I think because most bg's use show instead of scene 
#It started working so *shrug*
init:
    #Redefine layers to match renpy but with an additional "extra" layer which will never be used by baked-in renpy functions
    define config.layers = [ 'background', 'extra', 'master', 'transient', 'screens', 'overlay' ]
    #any bg shown (show bg black) will always appear on the background layer now instead of master
    $ config.tag_layer["bg"] = "background"
    #Note that character sprites and camera default to the master layer