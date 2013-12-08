#!/usr/bin/python
# A solution for this puzzle:
# * http://programmingpraxis.com/2013/11/15/twitter-puddle/


# *   
# **  
# *** *
# *****
def compute_volume(walls):
    """Compute the volume of all puddles formed by the walls.

    Args:
        walls: a list of wall heights in integers.
    Returns:
        an integer of the total volume
    """
    if len(walls) < 1:
        return 0
    walls_length = len(walls)

    start_peak = walls[0]
    end_peak = None
    lowest_peak = None

    depths = []
    volumes = []
    air_volumes = []

    volume = 0
    total_volume = 0

    for i in range(1, len(walls)):

        if len(depths) == 0:
            if walls[i] >= start_peak:
                start_peak = walls[i]
            else:
                depths.append(walls[i])
                lowest_valley = walls[i]
                air_volumes.append(start_peak - walls[i])
        else:
            if walls[i] >= start_peak:
                end_peak = walls[i]
                lowest_peak = start_peak

                # Compute
                volume = sum([lowest_peak - depth for depth in depths])
                volumes.append(volume)

                start_peak = walls[i]
                end_peak = None
                lowest_peak = None
                depths = []
            else:
                if walls[i] <= lowest_valley:
                    depths.append(walls[i])
                    lowest_valley = walls[i]
                    air_volumes.append(start_peak - walls[i])
                else:
                    if i + 1 == walls_length:
                        end_peak = walls[i]
                        lowest_peak = end_peak
                        # compute
                        # reset
                    else:
                        if walls[i + 1] <= walls[i]:
                            end_peak = walls[i]# end peak is found
                            lowest_peak = end_peak
                            # compute
                            # reset
                        else:
                            depths.append(walls[i])
                            air_volumes.append(start_peak - walls[i])




        # # The next peak is found, add up all the depths
        # # to compute the volume so far and save it.
        # if walls[i] > walls[i - 1]:
        #
        #     # Figure out the lowest peak
        #     if walls[i] >=
        #     next_peak = walls[i]
        #     lowest_peak = next_peak if next_peak < peak else peak
        #
        #     print 'peak', peak, 'next_peak', next_peak, 'lowest_peak', lowest_peak, depths
        #     # Calculate the volume
        #     volume = sum([lowest_peak - depth for depth in depths])
        #     volumes.append(volume)
        #
        #     # Reset
        #     depths = []
        #     peak = next_peak
        #
        # else:
        #     # A peak was found, save the current wall.
        #     depths.append(walls[i])

    # Add up all the volumes to return the total volume.
    return sum(volumes)
