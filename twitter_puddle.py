#!/usr/bin/python
# A solution for this puzzle:
# * http://programmingpraxis.com/2013/11/15/twitter-puddle/
import logging


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
    air_depths = []
    water_depths = []
    volumes = []
    total_volume = 0

    for i in range(1, len(walls)):

        # No new puddle
        if len(water_depths) == 0:
            # New peak is found because this wall is as high as the start peak
            if walls[i] >= start_peak:
                start_peak = walls[i]
            else:
                water_depths.append(walls[i])
                base = walls[i]
                air_depths.append(walls[i])
        else:
            # New peak is found because this wall is as high as the start peak,
            # air depths become water depths in this case
            if walls[i] >= start_peak:
                lowest_peak = start_peak

                # Compute
                water_volume = sum([lowest_peak - ad for ad in air_depths])
                total_volume += water_volume

                # Reset
                volumes = []
                start_peak = walls[i]
                water_depths = []
                air_depths = []
            else:
                # Goes deeper
                if walls[i] <= base:
                    base = walls[i]
                    water_depths.append(walls[i])
                    air_depths.append(walls[i])
                else:
                    # This is the last wall
                    if i + 1 == walls_length:
                        lowest_peak = walls[i]

                        # Compute
                        lower_depths = [
                            wd for wd in water_depths if wd < lowest_peak]
                        volume = sum(
                            [lowest_peak - ld for ld in lower_depths])
                        volumes.append(volume)

                        # Reset
                        water_depths = []
                        air_depths.append(walls[i])
                    else:
                        # New peak is found because the next wall is deeper
                        if walls[i + 1] <= walls[i]:
                            lowest_peak = walls[i]

                            # Compute
                            lower_depths = [
                                wd for wd in water_depths if wd < lowest_peak]
                            volume = sum(
                                [lowest_peak - ld for ld in lower_depths])
                            volumes.append(volume)

                            # Reset
                            water_depths = []
                            air_depths.append(walls[i])
                        else:
                            water_depths.append(walls[i])
                            air_depths.append(walls[i])

        logging.info(
            "water_depths=%s air_depths=%s volumes=%s total_volume=%s" % (
                water_depths, air_depths, volumes, total_volume))

    # Add up all the volumes to the total volume
    total_volume += sum(volumes)
    return total_volume
