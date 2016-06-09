#### GENERIC FUNCTIONS ####
""" Functions I seem to write for every project."""

def toggle (fc, mode):
""" Calls .setAutoDraw(mode) for each component in fc. Useful for conglomerate stimuli."""
    for component in fc:
        component.setAutoDraw(mode)
