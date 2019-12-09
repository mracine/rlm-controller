import os

# Basic utility function for getting the extension of a file
# Useful for determining if we can display a certain type of
# file (image or video)
def get_ext(filename):
    if os.path.exists(filename):
        fname, ext = os.path.splitext(filename)
        return ext
    return None

# Static function that returns the absolute path
# of the specified directory, checking if the directory
# is already an absolute path
# For instance, if the resources directory is not
# specified as an absolute path in the config
# it will assume the resources directory exists in the
# app instance path
def get_absolute_dirname(dirname, instance_path="../instance"):
    # TODO: Maybe implement a directory regex checker instead here
    if dirname.startswith("/"):
        return dirname
    else:
        return os.path.join(instance_path, dirname)
