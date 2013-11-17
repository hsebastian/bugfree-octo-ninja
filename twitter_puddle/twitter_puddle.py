#!/usr/bin/python
# http://programmingpraxis.com/2013/11/15/twitter-puddle/


walls = [2, 5, 1, 2, 3, 4, 7, 7, 6]


def compute_volume(walls):
    """Compute the volume of all puddles formed by the walls.

    Args:
        walls: a list of wall heights in integers.
    Returns:
        an integer of the total volume
    """
    if len(walls) < 1:
        return 0

    peak = walls[0]
    depths = []
    volumes = []

    for i in range(1, len(walls)):

        # The next peak is found, add up all the depths
        # to compute the volume so far and save it.
        if walls[i] >= peak:
            volume = sum(depths)
            volumes.append(volume)
            depths = []
            peak = walls[i]

        # A peak was found, calculate the depth between
        # the peak and this current wall and save it.
        depths.append(peak - walls[i])

    # Add up all the volumes to return the total volume.
    return sum(volumes)


if __name__ == '__main__':
    print compute_volume(walls)
