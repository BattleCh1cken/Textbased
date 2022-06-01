#perlin noise for terrain generation
#generate a 25 by 25 matrix <<List[List[]]>> that is centered with player in the middle
#0-water,1-flat,2-forest,3-mountain
'''[
[0, 0, 1, 1, 2, 3, 3],
[0, 1, 1, 2, 2, 2, 3],
[0, 1, 1, 1, 2, 2, 2],
[0, 0, 1, P, 1, 2, 1],
[0, 0, 0, 0, 1, 1, 1],
[1, 1, 1, 0, 0, 1, 1],
[2, 1, 1, 1, 0, 0, 0],
]'''