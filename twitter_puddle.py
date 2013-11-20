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
        if walls[i] > walls[i - 1]:

            # Figure out the lowest peak
            if walls[i] >=
            next_peak = walls[i]
            lowest_peak = next_peak if next_peak < peak else peak

            print 'peak', peak, 'next_peak', next_peak, 'lowest_peak', lowest_peak, depths
            # Calculate the volume
            volume = sum([lowest_peak - depth for depth in depths])
            volumes.append(volume)

            # Reset
            depths = []
            peak = next_peak

        else:
            # A peak was found, save the current wall.
            depths.append(walls[i])

    # Add up all the volumes to return the total volume.
    return sum(volumes)


if __name__ == '__main__':
    print compute_volume(walls)
