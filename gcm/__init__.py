from . import gcm

for key in dir(gcm):
    if key not in globals():
        globals()[key] = gcm.__dict__[key]
