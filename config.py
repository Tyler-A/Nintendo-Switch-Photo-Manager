
# The directory to the SD card from your Switch (Nintendo folder).  # TODO: Rewords better
SOURCE_FILEPATH = ""


# This tells the program whether or not to keep the image files on the SD card
# or not. If this is `False`, then you must specify a `TARGET_FILEPATH`, if no
# `TARGET_FILEPATH` is specified, then the software will error.
#
#   VALID OPTIONS:
#       False   - This will cause the software to output the organized images
#                 and videos to the corresponding folder specified in the
#                 `TARGET_FILEPATH` option.
#       True    - This will tell the software to output the images and videos
#                 into the same folder where the Switch stores the Album on the
#                 SD card directly.
KEEP_ON_SD_CARD = False


# This is the filepath of where you want the images and videos to be sent to.
# It is only used if the `KEEP_ON_SD_CARD` option is set to `True`. This can be
# anywhere on your computer so long as the directory already exists.
TARGET_FILEPATH = ""


FILENAME_FORMAT = "{YYYY}-{RMM}-{DD}.{4hh}-{mm}-{ss}"


#################################################################
#               DO NOT CHANGE BEYOND THIS POINT
VERSION = "0.1.0"