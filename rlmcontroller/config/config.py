# Class containing values for the configuration of 
# this app. Below are the default values provided,
# but they can be overwritten by placing a 'config.json' 
# file in the app instance path
#
# A 'sample.config.json' file is provided in this
# directory as a template for what the 'config.json'
# file should look like, should you choose to override
# these default values, which you'll probably want to do
class Config:
    # TODO: Are these all the options?
    SECRET_KEY = "dev"
    #DATABASE

    # Since we haven't given an absolute path for these
    # folders, it will default to using the instance path
    # as a root folder
    RLM_SOCKET_PATH = "socket"
    RESOURCES_DIR = "resources"

    # RGB LED Matrix image/video viewer specific options
    IMAGE_FILETYPES = ["png", "jpg", "gif"]

    # Currently trying to get images working first,
    # will add video support later
    VIDEO_FILETYPES = []

    MATRIX_COLS = 32
    MATRIX_ROWS = 32
    CENTER_IMAGES = True
    IMG_WAIT_SECS = 10
    ANIM_STOP_SECS = 30
    ANIM_LOOP_COUNT = 5
    ANIM_DELAY_MS = -1
    LOOP_FOREVER = True
    SHUFFLE = False

