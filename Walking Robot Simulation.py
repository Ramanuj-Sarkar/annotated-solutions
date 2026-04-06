# The robot understands the following commands:
# -2 means turn 90 degrees left, -1 means turn 90 degrees right, 1 <= k <= 9 means move k steps forward
# the robot starts facing north
# the robot can't go on obstacles and stops behind them, in whatever direction it arrived from
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # position is the position
        # max_dist is the maximum distance away
        # ne is whether north/south or east/west is changing
        # ns is whether change is positive or negative
        pos, max_dist, ne, ns = [0, 0], 0, 1, 1

        # for x-coords and y-coords respectively
        zero_dict, one_dict = defaultdict(set), defaultdict(set)

        for zero, one in obstacles:
            zero_dict[zero].add(one)
            one_dict[one].add(zero)

        for k in commands:
            if k > 0:
                # original positions
                # moving coordinate, stationary coordinate
                s, stay = pos[ne], pos[(ne + 1) % 2]

                # ideal final position
                e = s + (k * ns)

                # which direction is changing?
                imp_dict = zero_dict if ne else one_dict
                
                # range from e to s because s doesn't count
                steps = range(e, s) if ns < 0 else range(e, s, -1)

                # find obstacles within this range
                # on the line
                imp_obst = imp_dict[stay].intersection(steps)

                # find the furthest it can go
                e = min(imp_obst) - ns if imp_obst else e
                pos[ne] = e

                # add to the maximum distance if applicable
                max_dist = max(max_dist, e * e + stay * stay)
            else:
                #      1, 1
                #0, -1       0, 1
                #      1, -1

                # It will always be like this
                # if turning 90 degrees anywhere
                ne = (ne + 1) % 2

                if k+2:
                    # if k == -1, this is true
                    # you turn right
                    # if ne is 1, then ns changes
                    ns *= -1 if ne else 1
                else:
                    # if k == -2, this is true
                    # you turn left
                    # if ne is 0, then ns changes
                    ns *= 1 if ne else -1
        return max_dist
