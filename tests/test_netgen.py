import pathlib
import tempfile

import numpy as np
import pytest

import meshio

from . import helpers

test_set = [
    helpers.empty_mesh,
    helpers.line_mesh,
    helpers.tri_mesh_2d,
    helpers.tri_mesh,
    helpers.triangle6_mesh,
    helpers.quad_mesh,
    helpers.quad8_mesh,
    helpers.tri_quad_mesh,
    helpers.tet_mesh,
    helpers.tet10_mesh,
    helpers.hex_mesh,
    helpers.hex20_mesh,
    helpers.pyramid_mesh,
    helpers.wedge_mesh,
]


@pytest.mark.parametrize("mesh", test_set)
def test(mesh):
    helpers.write_read(
        meshio.netgen.write, meshio.netgen.read, mesh, 1.0e-13, extension=".vol"
    )
    helpers.write_read(
        meshio.netgen.write, meshio.netgen.read, mesh, 1.0e-13, extension=".vol.gz"
    )


periodic_1d = """
# Generated by NETGEN v6.2.2103-39-g3165e042

mesh3d
dimension
1
geomtype
0

# surfnr    bcnr   domin  domout      np      p1      p2      p3
surfaceelements
0


#  matnr      np      p1      p2      p3      p4
volumeelements
0


# surfid  0   p1   p2   trignum1    trignum2   domin/surfnr1    domout/surfnr2   ednr1   dist1   ednr2   dist2
edgesegmentsgi2
50
       1       0       1       2       -1       -1       -1       -1        1            0        1            0
       1       0       2       3       -1       -1       -1       -1        1            0        1            0
       1       0       3       4       -1       -1       -1       -1        1            0        1            0
       1       0       4       5       -1       -1       -1       -1        1            0        1            0
       1       0       5       6       -1       -1       -1       -1        1            0        1            0
       1       0       6       7       -1       -1       -1       -1        1            0        1            0
       1       0       7       8       -1       -1       -1       -1        1            0        1            0
       1       0       8       9       -1       -1       -1       -1        1            0        1            0
       1       0       9      10       -1       -1       -1       -1        1            0        1            0
       1       0      10      11       -1       -1       -1       -1        1            0        1            0
       1       0      11      12       -1       -1       -1       -1        1            0        1            0
       1       0      12      13       -1       -1       -1       -1        1            0        1            0
       1       0      13      14       -1       -1       -1       -1        1            0        1            0
       1       0      14      15       -1       -1       -1       -1        1            0        1            0
       1       0      15      16       -1       -1       -1       -1        1            0        1            0
       1       0      16      17       -1       -1       -1       -1        1            0        1            0
       1       0      17      18       -1       -1       -1       -1        1            0        1            0
       1       0      18      19       -1       -1       -1       -1        1            0        1            0
       1       0      19      20       -1       -1       -1       -1        1            0        1            0
       1       0      20      21       -1       -1       -1       -1        1            0        1            0
       1       0      21      22       -1       -1       -1       -1        1            0        1            0
       1       0      22      23       -1       -1       -1       -1        1            0        1            0
       1       0      23      24       -1       -1       -1       -1        1            0        1            0
       1       0      24      25       -1       -1       -1       -1        1            0        1            0
       1       0      25      26       -1       -1       -1       -1        1            0        1            0
       1       0      26      27       -1       -1       -1       -1        1            0        1            0
       1       0      27      28       -1       -1       -1       -1        1            0        1            0
       1       0      28      29       -1       -1       -1       -1        1            0        1            0
       1       0      29      30       -1       -1       -1       -1        1            0        1            0
       1       0      30      31       -1       -1       -1       -1        1            0        1            0
       1       0      31      32       -1       -1       -1       -1        1            0        1            0
       1       0      32      33       -1       -1       -1       -1        1            0        1            0
       1       0      33      34       -1       -1       -1       -1        1            0        1            0
       1       0      34      35       -1       -1       -1       -1        1            0        1            0
       1       0      35      36       -1       -1       -1       -1        1            0        1            0
       1       0      36      37       -1       -1       -1       -1        1            0        1            0
       1       0      37      38       -1       -1       -1       -1        1            0        1            0
       1       0      38      39       -1       -1       -1       -1        1            0        1            0
       1       0      39      40       -1       -1       -1       -1        1            0        1            0
       1       0      40      41       -1       -1       -1       -1        1            0        1            0
       1       0      41      42       -1       -1       -1       -1        1            0        1            0
       1       0      42      43       -1       -1       -1       -1        1            0        1            0
       1       0      43      44       -1       -1       -1       -1        1            0        1            0
       1       0      44      45       -1       -1       -1       -1        1            0        1            0
       1       0      45      46       -1       -1       -1       -1        1            0        1            0
       1       0      46      47       -1       -1       -1       -1        1            0        1            0
       1       0      47      48       -1       -1       -1       -1        1            0        1            0
       1       0      48      49       -1       -1       -1       -1        1            0        1            0
       1       0      49      50       -1       -1       -1       -1        1            0        1            0
       1       0      50      51       -1       -1       -1       -1        1            0        1            0


#          X             Y             Z
points
51
    0.0000000000000000      0.0000000000000000      0.0000000000000000
    0.0200000000000000      0.0000000000000000      0.0000000000000000
    0.0400000000000000      0.0000000000000000      0.0000000000000000
    0.0600000000000000      0.0000000000000000      0.0000000000000000
    0.0800000000000000      0.0000000000000000      0.0000000000000000
    0.1000000000000000      0.0000000000000000      0.0000000000000000
    0.1200000000000000      0.0000000000000000      0.0000000000000000
    0.1400000000000000      0.0000000000000000      0.0000000000000000
    0.1600000000000000      0.0000000000000000      0.0000000000000000
    0.1800000000000000      0.0000000000000000      0.0000000000000000
    0.2000000000000000      0.0000000000000000      0.0000000000000000
    0.2200000000000000      0.0000000000000000      0.0000000000000000
    0.2400000000000000      0.0000000000000000      0.0000000000000000
    0.2600000000000000      0.0000000000000000      0.0000000000000000
    0.2800000000000000      0.0000000000000000      0.0000000000000000
    0.3000000000000000      0.0000000000000000      0.0000000000000000
    0.3200000000000000      0.0000000000000000      0.0000000000000000
    0.3400000000000000      0.0000000000000000      0.0000000000000000
    0.3600000000000000      0.0000000000000000      0.0000000000000000
    0.3800000000000000      0.0000000000000000      0.0000000000000000
    0.4000000000000000      0.0000000000000000      0.0000000000000000
    0.4200000000000000      0.0000000000000000      0.0000000000000000
    0.4400000000000000      0.0000000000000000      0.0000000000000000
    0.4600000000000000      0.0000000000000000      0.0000000000000000
    0.4800000000000000      0.0000000000000000      0.0000000000000000
    0.5000000000000000      0.0000000000000000      0.0000000000000000
    0.5200000000000000      0.0000000000000000      0.0000000000000000
    0.5400000000000000      0.0000000000000000      0.0000000000000000
    0.5600000000000001      0.0000000000000000      0.0000000000000000
    0.5800000000000000      0.0000000000000000      0.0000000000000000
    0.6000000000000000      0.0000000000000000      0.0000000000000000
    0.6200000000000000      0.0000000000000000      0.0000000000000000
    0.6400000000000000      0.0000000000000000      0.0000000000000000
    0.6600000000000000      0.0000000000000000      0.0000000000000000
    0.6800000000000000      0.0000000000000000      0.0000000000000000
    0.7000000000000000      0.0000000000000000      0.0000000000000000
    0.7200000000000000      0.0000000000000000      0.0000000000000000
    0.7400000000000000      0.0000000000000000      0.0000000000000000
    0.7600000000000000      0.0000000000000000      0.0000000000000000
    0.7800000000000000      0.0000000000000000      0.0000000000000000
    0.8000000000000000      0.0000000000000000      0.0000000000000000
    0.8200000000000000      0.0000000000000000      0.0000000000000000
    0.8400000000000000      0.0000000000000000      0.0000000000000000
    0.8600000000000000      0.0000000000000000      0.0000000000000000
    0.8800000000000000      0.0000000000000000      0.0000000000000000
    0.9000000000000000      0.0000000000000000      0.0000000000000000
    0.9200000000000000      0.0000000000000000      0.0000000000000000
    0.9399999999999999      0.0000000000000000      0.0000000000000000
    0.9600000000000000      0.0000000000000000      0.0000000000000000
    0.9800000000000000      0.0000000000000000      0.0000000000000000
    1.0000000000000000      0.0000000000000000      0.0000000000000000


#          pnum             index
pointelements
2
       1         1
      51         2
identifications
1
       1      51       1
identificationtypes
1
 2


endmesh
"""

periodic_2d = """
# Generated by NETGEN v6.2.2103-39-g3165e042

mesh3d
dimension
2
geomtype
0

# surfnr    bcnr   domin  domout      np      p1      p2      p3
surfaceelements
58
 2 1 0 0 3 1 5 17
 2 1 0 0 3 5 6 21
 2 1 0 0 3 6 7 22
 2 1 0 0 3 6 22 21
 2 1 0 0 3 7 8 23
 2 1 0 0 3 7 23 22
 2 1 0 0 3 2 24 8
 2 1 0 0 3 8 24 23
 2 1 0 0 3 2 9 24
 2 1 0 0 3 9 10 25
 2 1 0 0 3 9 25 24
 2 1 0 0 3 10 11 26
 2 1 0 0 3 10 26 25
 2 1 0 0 3 11 12 27
 2 1 0 0 3 11 27 26
 2 1 0 0 3 3 13 12
 2 1 0 0 3 13 14 28
 2 1 0 0 3 14 15 29
 2 1 0 0 3 14 29 28
 2 1 0 0 3 15 16 30
 2 1 0 0 3 15 30 29
 2 1 0 0 3 4 31 16
 2 1 0 0 3 16 31 30
 2 1 0 0 3 4 20 31
 2 1 0 0 3 17 32 18
 2 1 0 0 3 18 33 19
 2 1 0 0 3 18 32 33
 2 1 0 0 3 19 34 20
 2 1 0 0 3 20 34 31
 2 1 0 0 3 19 33 34
 2 1 0 0 3 12 13 27
 2 1 0 0 3 13 28 27
 2 1 0 0 3 5 21 17
 2 1 0 0 3 22 23 35
 2 1 0 0 3 21 22 36
 2 1 0 0 3 22 35 36
 2 1 0 0 3 26 27 37
 2 1 0 0 3 27 28 37
 2 1 0 0 3 23 24 25
 2 1 0 0 3 23 25 35
 2 1 0 0 3 30 31 38
 2 1 0 0 3 31 34 38
 2 1 0 0 3 29 30 38
 2 1 0 0 3 28 29 39
 2 1 0 0 3 28 39 37
 2 1 0 0 3 29 38 39
 2 1 0 0 3 17 21 32
 2 1 0 0 3 21 36 32
 2 1 0 0 3 25 26 40
 2 1 0 0 3 32 36 33
 2 1 0 0 3 26 37 40
 2 1 0 0 3 33 38 34
 2 1 0 0 3 33 36 38
 2 1 0 0 3 25 40 35
 2 1 0 0 3 36 39 38
 2 1 0 0 3 35 39 36
 2 1 0 0 3 35 40 39
 2 1 0 0 3 37 39 40


#  matnr      np      p1      p2      p3      p4
volumeelements
0


# surfid  0   p1   p2   trignum1    trignum2   domin/surfnr1    domout/surfnr2   ednr1   dist1   ednr2   dist2
edgesegmentsgi2
20
       1       0       1       5       -1       -1        1        0        1            0        1          0.2
       1       0       5       6       -1       -1        1        0        1          0.2        1          0.4
       1       0       6       7       -1       -1        1        0        1          0.4        1          0.6
       1       0       7       8       -1       -1        1        0        1          0.6        1          0.8
       1       0       8       2       -1       -1        1        0        1          0.8        1            1
       2       0       2       9       -1       -1        1        0        2            0        2          0.2
       2       0       9      10       -1       -1        1        0        2          0.2        2          0.4
       2       0      10      11       -1       -1        1        0        2          0.4        2          0.6
       2       0      11      12       -1       -1        1        0        2          0.6        2          0.8
       2       0      12       3       -1       -1        1        0        2          0.8        2            1
       3       0       3      13       -1       -1        1        0        3            0        3          0.2
       3       0      13      14       -1       -1        1        0        3          0.2        3          0.4
       3       0      14      15       -1       -1        1        0        3          0.4        3          0.6
       3       0      15      16       -1       -1        1        0        3          0.6        3          0.8
       3       0      16       4       -1       -1        1        0        3          0.8        3            1
       4       0       1      17       -1       -1        0        1        4            0        4          0.2
       4       0      17      18       -1       -1        0        1        4          0.2        4          0.4
       4       0      18      19       -1       -1        0        1        4          0.4        4          0.6
       4       0      19      20       -1       -1        0        1        4          0.6        4          0.8
       4       0      20       4       -1       -1        0        1        4          0.8        4            1


#          X             Y             Z
points
40
    0.0000000000000000      0.0000000000000000      0.0000000000000000
    1.0000000000000000      0.0000000000000000      0.0000000000000000
    1.0000000000000000      1.0000000000000000      0.0000000000000000
    0.0000000000000000      1.0000000000000000      0.0000000000000000
    0.2000000000000000      0.0000000000000000      0.0000000000000000
    0.4000000000000000      0.0000000000000000      0.0000000000000000
    0.6000000000000000      0.0000000000000000      0.0000000000000000
    0.8000000000000000      0.0000000000000000      0.0000000000000000
    1.0000000000000000      0.2000000000000000      0.0000000000000000
    1.0000000000000000      0.4000000000000000      0.0000000000000000
    1.0000000000000000      0.6000000000000000      0.0000000000000000
    1.0000000000000000      0.8000000000000000      0.0000000000000000
    0.7999999999999999      1.0000000000000000      0.0000000000000000
    0.6000000000000000      1.0000000000000000      0.0000000000000000
    0.4000000000000000      1.0000000000000000      0.0000000000000000
    0.2000000000000000      1.0000000000000000      0.0000000000000000
    0.0000000000000000      0.2000000000000000      0.0000000000000000
    0.0000000000000000      0.4000000000000000      0.0000000000000000
    0.0000000000000000      0.6000000000000000      0.0000000000000000
    0.0000000000000000      0.8000000000000000      0.0000000000000000
    0.2737029466317127      0.1811747818216966      0.0000000000000000
    0.4805348579459315      0.1852935472807671      0.0000000000000000
    0.6827590117435046      0.1702890061939871      0.0000000000000000
    0.8575695844442716      0.1419063764469471      0.0000000000000000
    0.8111112850985802      0.3258703253208415      0.0000000000000000
    0.8493339534816288      0.5262364626047286      0.0000000000000000
    0.8421283897191041      0.7318614438631723      0.0000000000000000
    0.6601606467397222      0.8032633168034399      0.0000000000000000
    0.4765343016929663      0.8179836454001187      0.0000000000000000
    0.3132853271934791      0.8629930180472398      0.0000000000000000
    0.1584925502078927      0.8390807603910830      0.0000000000000000
    0.1662260298847409      0.3347019222223993      0.0000000000000000
    0.1698338083646673      0.5130730339035593      0.0000000000000000
    0.1324637082656786      0.6819019947250892      0.0000000000000000
    0.5818135591952022      0.3542155081169817      0.0000000000000000
    0.3642445694293263      0.4057099958862074      0.0000000000000000
    0.7111939984221883      0.6337182845699614      0.0000000000000000
    0.3154224090519101      0.6697496604451058      0.0000000000000000
    0.5278793480475702      0.5943130585988371      0.0000000000000000
    0.6923017137632204      0.4803955670550934      0.0000000000000000


#          pnum             index
pointelements
4
       1         1
       2         2
       3         3
       4         4
identifications
6
       2       1       4
       3       4       4
       9      17       4
      10      18       4
      11      19       4
      12      20       4
identificationtypes
4
 1 1 1 2


bcnames
4
1	outer
2	periodic
3	outer
4	periodic




cd2names
4
1
2
3
4




#   Surfnr     Red     Green     Blue
face_colours
1
       2   0.00000000   1.00000000   0.00000000


endmesh
"""

periodic_3d = """
# Generated by NETGEN v6.2.2103-39-g3165e042

mesh3d
dimension
3
geomtype
0

# surfnr    bcnr   domin  domout      np      p1      p2      p3
surfaceelements
108
 1 1 1 0 3 1 9 32
 1 1 1 0 3 9 10 33
 1 1 1 0 3 4 34 10
 1 1 1 0 3 10 34 33
 1 1 1 0 3 4 28 34
 1 1 1 0 3 3 31 11
 1 1 1 0 3 11 35 12
 1 1 1 0 3 7 12 36
 1 1 1 0 3 7 36 27
 1 1 1 0 3 12 35 36
 1 1 1 0 3 27 37 28
 1 1 1 0 3 28 37 34
 1 1 1 0 3 27 36 37
 3 6 1 0 3 49 51 53
 1 1 1 0 3 9 33 32
 3 6 1 0 3 30 51 49
 1 1 1 0 3 35 37 36
 1 1 1 0 3 33 34 37
 1 1 1 0 3 31 32 33
 1 1 1 0 3 11 31 35
 1 1 1 0 3 31 33 35
 1 1 1 0 3 33 37 35
 7 2 1 0 3 1 22 9
 7 2 1 0 3 9 38 10
 7 2 1 0 3 4 10 16
 3 6 1 0 3 49 53 50
 7 2 1 0 3 10 38 16
 7 2 1 0 3 6 15 26
 7 2 1 0 3 15 16 39
 7 2 1 0 3 15 39 26
 3 6 1 0 3 51 52 53
 7 2 1 0 3 2 25 21
 7 2 1 0 3 21 40 22
 7 2 1 0 3 25 26 39
 7 2 1 0 3 9 22 40
 7 2 1 0 3 21 25 40
 7 2 1 0 3 25 39 40
 7 2 1 0 3 9 40 38
 7 2 1 0 3 16 38 39
 7 2 1 0 3 38 40 39
 4 4 1 0 3 8 13 17
 4 4 1 0 3 13 14 41
 4 4 1 0 3 7 42 14
 4 4 1 0 3 14 42 41
 4 4 1 0 3 7 27 42
 3 6 1 0 3 29 30 49
 4 4 1 0 3 15 43 16
 4 4 1 0 3 4 16 44
 4 4 1 0 3 4 44 28
 4 4 1 0 3 16 43 44
 3 6 1 0 3 19 29 49
 4 4 1 0 3 6 18 15
 4 4 1 0 3 27 28 45
 4 4 1 0 3 27 45 42
 4 4 1 0 3 28 44 45
 4 4 1 0 3 13 41 17
 4 4 1 0 3 43 45 44
 4 4 1 0 3 41 42 45
 4 4 1 0 3 15 18 43
 4 4 1 0 3 17 41 18
 4 4 1 0 3 18 41 43
 4 4 1 0 3 41 45 43
 2 5 1 0 3 8 17 24
 2 5 1 0 3 17 18 46
 2 5 1 0 3 6 26 18
 2 5 1 0 3 18 26 46
 3 6 1 0 3 31 50 53
 2 5 1 0 3 5 23 47
 2 5 1 0 3 23 24 47
 2 5 1 0 3 2 30 25
 2 5 1 0 3 25 48 26
 2 5 1 0 3 25 30 48
 2 5 1 0 3 5 47 29
 2 5 1 0 3 29 48 30
 2 5 1 0 3 17 46 24
 2 5 1 0 3 29 47 48
 2 5 1 0 3 24 46 47
 2 5 1 0 3 46 48 47
 3 6 1 0 3 32 53 52
 2 5 1 0 3 26 48 46
 3 6 1 0 3 5 29 19
 3 6 1 0 3 19 49 20
 3 6 1 0 3 3 20 50
 3 6 1 0 3 3 50 31
 3 6 1 0 3 20 49 50
 3 6 1 0 3 2 21 30
 3 6 1 0 3 21 22 51
 3 6 1 0 3 1 52 22
 3 6 1 0 3 22 52 51
 3 6 1 0 3 1 32 52
 3 6 1 0 3 21 51 30
 3 6 1 0 3 31 53 32
 8 3 1 0 3 3 11 20
 8 3 1 0 3 11 12 54
 8 3 1 0 3 7 14 12
 8 3 1 0 3 12 14 54
 8 3 1 0 3 8 24 13
 8 3 1 0 3 13 55 14
 8 3 1 0 3 13 24 55
 8 3 1 0 3 5 19 23
 8 3 1 0 3 19 20 56
 8 3 1 0 3 23 55 24
 8 3 1 0 3 11 56 20
 8 3 1 0 3 19 56 23
 8 3 1 0 3 23 56 55
 8 3 1 0 3 11 54 56
 8 3 1 0 3 14 55 54
 8 3 1 0 3 54 55 56


#  matnr      np      p1      p2      p3      p4
volumeelements
166
1 4 33 57 59 61
1 4 12 14 54 36
1 4 33 38 59 57
1 4 21 40 51 60
1 4 49 51 53 57
1 4 11 35 54 58
1 4 57 59 61 64
1 4 11 20 58 56
1 4 54 55 56 61
1 4 15 39 62 43
1 4 39 43 59 62
1 4 55 56 61 64
1 4 1 9 65 22
1 4 49 57 63 60
1 4 41 45 59 61
1 4 29 47 60 63
1 4 29 47 48 60
1 4 46 47 60 48
1 4 9 38 65 40
1 4 24 46 47 64
1 4 39 40 62 59
1 4 21 30 60 51
1 4 1 9 32 65
1 4 57 59 64 62
1 4 56 58 61 64
1 4 38 39 59 40
1 4 20 49 58 56
1 4 36 37 42 61
1 4 35 36 61 37
1 4 27 36 37 42
1 4 35 36 54 61
1 4 37 42 61 45
1 4 5 19 23 63
1 4 14 41 55 61
1 4 23 47 63 64
1 4 9 22 40 65
1 4 31 32 33 53
1 4 25 26 62 48
1 4 23 24 47 64
1 4 40 57 62 59
1 4 56 58 64 63
1 4 22 51 65 52
1 4 29 49 63 60
1 4 34 37 59 45
1 4 33 53 57 58
1 4 23 24 64 55
1 4 32 33 53 65
1 4 11 12 54 35
1 4 43 44 59 45
1 4 21 25 60 30
1 4 40 51 57 65
1 4 13 14 41 55
1 4 22 40 65 51
1 4 41 46 64 62
1 4 3 11 20 58
1 4 41 43 59 45
1 4 10 33 38 34
1 4 31 33 35 58
1 4 21 25 40 60
1 4 2 21 30 25
1 4 24 41 46 64
1 4 17 18 46 41
1 4 49 57 58 63
1 4 4 10 16 44
1 4 10 34 38 44
1 4 17 24 41 46
1 4 19 29 49 63
1 4 33 37 61 59
1 4 33 38 57 65
1 4 11 31 35 58
1 4 38 40 59 57
1 4 7 12 36 14
1 4 30 49 60 51
1 4 27 37 45 42
1 4 14 36 42 61
1 4 15 18 43 62
1 4 19 20 56 49
1 4 41 55 61 64
1 4 21 22 51 40
1 4 10 16 44 38
1 4 57 58 63 64
1 4 15 16 39 43
1 4 25 30 48 60
1 4 46 48 60 62
1 4 12 35 36 54
1 4 33 35 61 37
1 4 26 46 62 48
1 4 33 35 58 61
1 4 25 48 62 60
1 4 3 20 50 58
1 4 18 41 62 46
1 4 25 40 60 62
1 4 37 45 61 59
1 4 40 57 60 62
1 4 23 55 64 56
1 4 38 40 57 65
1 4 41 59 62 64
1 4 49 50 58 53
1 4 14 36 61 54
1 4 51 52 53 65
1 4 25 26 39 62
1 4 34 38 44 59
1 4 9 32 65 33
1 4 51 53 57 65
1 4 16 38 59 44
1 4 23 56 64 63
1 4 14 54 61 55
1 4 6 15 26 18
1 4 15 18 62 26
1 4 54 56 58 61
1 4 3 31 58 50
1 4 49 56 63 58
1 4 5 19 63 29
1 4 1 32 52 65
1 4 4 28 34 44
1 4 35 54 58 61
1 4 4 10 44 34
1 4 49 53 58 57
1 4 1 22 65 52
1 4 41 59 64 61
1 4 29 30 49 60
1 4 5 29 63 47
1 4 9 10 33 38
1 4 40 51 60 57
1 4 18 41 43 62
1 4 46 47 64 60
1 4 49 51 57 60
1 4 16 43 44 59
1 4 16 39 43 59
1 4 57 60 64 63
1 4 7 14 36 42
1 4 33 53 65 57
1 4 15 26 62 39
1 4 33 34 37 59
1 4 33 34 59 38
1 4 47 60 63 64
1 4 7 27 42 36
1 4 13 17 24 41
1 4 13 24 55 41
1 4 46 60 64 62
1 4 41 43 62 59
1 4 57 58 64 61
1 4 9 33 65 38
1 4 18 26 46 62
1 4 16 38 39 59
1 4 19 49 56 63
1 4 24 41 64 55
1 4 8 13 17 24
1 4 25 39 40 62
1 4 11 54 56 58
1 4 29 30 60 48
1 4 3 11 58 31
1 4 5 23 47 63
1 4 31 50 53 58
1 4 32 52 65 53
1 4 28 34 44 45
1 4 34 44 45 59
1 4 57 60 62 64
1 4 19 23 63 56
1 4 14 41 61 42
1 4 20 49 50 58
1 4 41 42 45 61
1 4 31 33 58 53
1 4 33 57 61 58
1 4 27 28 45 37
1 4 28 34 45 37


# surfid  0   p1   p2   trignum1    trignum2   domin/surfnr1    domout/surfnr2   ednr1   dist1   ednr2   dist2
edgesegmentsgi2
72
       1       0       1       9       -1       -1        1        7        1            0        0            0
       2       0       9       1       -1       -1        1        7        1            0        0            0
       1       0       9      10       -1       -1        1        7        1            0        0            0
       2       0      10       9       -1       -1        1        7        1            0        0            0
       1       0      10       4       -1       -1        1        7        1            0        0            0
       2       0       4      10       -1       -1        1        7        1            0        0            0
       1       0      11       3       -1       -1        8        1        2            0        0            0
       3       0       3      11       -1       -1        8        1        2            0        0            0
       1       0      12      11       -1       -1        8        1        2            0        0            0
       3       0      11      12       -1       -1        8        1        2            0        0            0
       1       0       7      12       -1       -1        8        1        2            0        0            0
       3       0      12       7       -1       -1        8        1        2            0        0            0
       4       0       8      13       -1       -1        4        8        3            0        0            0
       3       0      13       8       -1       -1        4        8        3            0        0            0
       4       0      13      14       -1       -1        4        8        3            0        0            0
       3       0      14      13       -1       -1        4        8        3            0        0            0
       4       0      14       7       -1       -1        4        8        3            0        0            0
       3       0       7      14       -1       -1        4        8        3            0        0            0
       4       0      15       6       -1       -1        7        4        4            0        0            0
       2       0       6      15       -1       -1        7        4        4            0        0            0
       4       0      16      15       -1       -1        7        4        4            0        0            0
       2       0      15      16       -1       -1        7        4        4            0        0            0
       4       0       4      16       -1       -1        7        4        4            0        0            0
       2       0      16       4       -1       -1        7        4        4            0        0            0
       5       0       8      17       -1       -1        2        4        5            0        0            0
       4       0      17       8       -1       -1        2        4        5            0        0            0
       5       0      17      18       -1       -1        2        4        5            0        0            0
       4       0      18      17       -1       -1        2        4        5            0        0            0
       5       0      18       6       -1       -1        2        4        5            0        0            0
       4       0       6      18       -1       -1        2        4        5            0        0            0
       6       0      19       5       -1       -1        8        3        6            0        0            0
       3       0       5      19       -1       -1        8        3        6            0        0            0
       6       0      20      19       -1       -1        8        3        6            0        0            0
       3       0      19      20       -1       -1        8        3        6            0        0            0
       6       0       3      20       -1       -1        8        3        6            0        0            0
       3       0      20       3       -1       -1        8        3        6            0        0            0
       6       0       2      21       -1       -1        3        7        7            0        0            0
       2       0      21       2       -1       -1        3        7        7            0        0            0
       6       0      21      22       -1       -1        3        7        7            0        0            0
       2       0      22      21       -1       -1        3        7        7            0        0            0
       6       0      22       1       -1       -1        3        7        7            0        0            0
       2       0       1      22       -1       -1        3        7        7            0        0            0
       5       0       5      23       -1       -1        2        8        8            0        0            0
       3       0      23       5       -1       -1        2        8        8            0        0            0
       5       0      23      24       -1       -1        2        8        8            0        0            0
       3       0      24      23       -1       -1        2        8        8            0        0            0
       5       0      24       8       -1       -1        2        8        8            0        0            0
       3       0       8      24       -1       -1        2        8        8            0        0            0
       5       0      25       2       -1       -1        7        2        9            0        0            0
       2       0       2      25       -1       -1        7        2        9            0        0            0
       5       0      26      25       -1       -1        7        2        9            0        0            0
       2       0      25      26       -1       -1        7        2        9            0        0            0
       5       0       6      26       -1       -1        7        2        9            0        0            0
       2       0      26       6       -1       -1        7        2        9            0        0            0
       1       0      27       7       -1       -1        4        1       10            0        0            0
       4       0       7      27       -1       -1        4        1       10            0        0            0
       1       0      28      27       -1       -1        4        1       10            0        0            0
       4       0      27      28       -1       -1        4        1       10            0        0            0
       1       0       4      28       -1       -1        4        1       10            0        0            0
       4       0      28       4       -1       -1        4        1       10            0        0            0
       5       0      29       5       -1       -1        3        2       11            0        0            0
       6       0       5      29       -1       -1        3        2       11            0        0            0
       5       0      30      29       -1       -1        3        2       11            0        0            0
       6       0      29      30       -1       -1        3        2       11            0        0            0
       5       0       2      30       -1       -1        3        2       11            0        0            0
       6       0      30       2       -1       -1        3        2       11            0        0            0
       1       0       3      31       -1       -1        1        3       12            0        0            0
       6       0      31       3       -1       -1        1        3       12            0        0            0
       1       0      31      32       -1       -1        1        3       12            0        0            0
       6       0      32      31       -1       -1        1        3       12            0        0            0
       1       0      32       1       -1       -1        1        3       12            0        0            0
       6       0       1      32       -1       -1        1        3       12            0        0            0


#          X             Y             Z
points
65
    0.0000000000000000      0.0000000000000000      0.0000000000000000
    0.0000000000000000      0.0000000000000000      1.0000000000000000
    1.0000000000000000      0.0000000000000000      0.0000000000000000
    0.0000000000000000      1.0000000000000000      0.0000000000000000
    1.0000000000000000      0.0000000000000000      1.0000000000000000
    0.0000000000000000      1.0000000000000000      1.0000000000000000
    1.0000000000000000      1.0000000000000000      0.0000000000000000
    1.0000000000000000      1.0000000000000000      1.0000000000000000
    0.0000000000000000      0.3333333333333333      0.0000000000000000
    0.0000000000000000      0.6666666666666666      0.0000000000000000
    1.0000000000000000      0.3333333333333333      0.0000000000000000
    1.0000000000000000      0.6666666666666666      0.0000000000000000
    1.0000000000000000      1.0000000000000000      0.6666666666666666
    1.0000000000000000      1.0000000000000000      0.3333333333333332
    0.0000000000000000      1.0000000000000000      0.6666666666666666
    0.0000000000000000      1.0000000000000000      0.3333333333333332
    0.6666666666666666      1.0000000000000000      1.0000000000000000
    0.3333333333333332      1.0000000000000000      1.0000000000000000
    1.0000000000000000      0.0000000000000000      0.6666666666666666
    1.0000000000000000      0.0000000000000000      0.3333333333333332
    0.0000000000000000      0.0000000000000000      0.6666666666666666
    0.0000000000000000      0.0000000000000000      0.3333333333333332
    1.0000000000000000      0.3333333333333333      1.0000000000000000
    1.0000000000000000      0.6666666666666666      1.0000000000000000
    0.0000000000000000      0.3333333333333333      1.0000000000000000
    0.0000000000000000      0.6666666666666666      1.0000000000000000
    0.6666666666666666      1.0000000000000000      0.0000000000000000
    0.3333333333333332      1.0000000000000000      0.0000000000000000
    0.6666666666666666      0.0000000000000000      1.0000000000000000
    0.3333333333333332      0.0000000000000000      1.0000000000000000
    0.6666666666666666      0.0000000000000000      0.0000000000000000
    0.3333333333333332      0.0000000000000000      0.0000000000000000
    0.3453764872152520      0.4289616495406477      0.0000000000000000
    0.2363722957339057      0.7629978630944177      0.0000000000000000
    0.7093903868425258      0.4777271339652773      0.0000000000000000
    0.7767853874295251      0.7740629504580570      0.0000000000000000
    0.5093916952832738      0.7373846519656869      0.0000000000000000
    0.0000000000000000      0.5848322921574791      0.2973390248238796
    0.0000000000000000      0.6376771832790789      0.6256884212430072
    0.0000000000000000      0.3078273776201016      0.4901690889415314
    0.6546235127847480      1.0000000000000000      0.5710383504593523
    0.7636277042660942      1.0000000000000000      0.2370021369055823
    0.2906096131574742      1.0000000000000000      0.5222728660347228
    0.2232146125704748      1.0000000000000000      0.2259370495419430
    0.4906083047167261      1.0000000000000000      0.2626153480343131
    0.5226154526972956      0.6723847618372673      1.0000000000000000
    0.7303054535238108      0.3470956979891270      1.0000000000000000
    0.3846043860484825      0.3457533069880933      1.0000000000000000
    0.6545492698511188      0.0000000000000000      0.5710115507028192
    0.7635147493753501      0.0000000000000000      0.2370411648783929
    0.2904642514608775      0.0000000000000000      0.5222189640348618
    0.2231265594790997      0.0000000000000000      0.2258767298015257
    0.4905217481815927      0.0000000000000000      0.2626047101435547
    1.0000000000000000      0.5848322921574791      0.2973390248238796
    1.0000000000000000      0.6376771832790789      0.6256884212430072
    1.0000000000000000      0.3078273776201016      0.4901690889415314
    0.4272276804008159      0.3426052995823172      0.4176406498588326
    0.7299469195459262      0.2730082184471636      0.2789191388190804
    0.3202369865656342      0.7063322531411742      0.4178510398137523
    0.4187321713884653      0.2791900408384976      0.7467956942298275
    0.6883019035327874      0.6532015011171384      0.3389153362395730
    0.2848826858717337      0.6291905246270143      0.7492446890085234
    0.7505520006346695      0.2364072052628841      0.7265283730519375
    0.6904080728530597      0.5313023561184044      0.6778821530260029
    0.2153574046463540      0.2182196460363049      0.2340094009251045


#          pnum             index
pointelements
0
identifications
15
       1       3       1
       2       5       1
       4       7       1
       6       8       1
       9      11       1
      10      12       1
      15      13       1
      16      14       1
      21      19       1
      22      20       1
      25      23       1
      26      24       1
      38      54       1
      39      55       1
      40      56       1
identificationtypes
1
 2


bcnames
6
1	outer
2	default
3	default
4	outer
5	outer
6	outer




#   Surfnr     Red     Green     Blue
face_colours
6
       1   0.00000000   1.00000000   0.00000000
       7   0.00000000   1.00000000   0.00000000
       8   0.00000000   1.00000000   0.00000000
       4   0.00000000   1.00000000   0.00000000
       2   0.00000000   1.00000000   0.00000000
       3   0.00000000   1.00000000   0.00000000


endmesh

csgsurfaces 8
plane 6
-1.00000000 0.00000000 0.00000000 0.00000000 0.00000000 -1.00000000
plane 6
-1.00000000 0.00000000 1.00000000 0.00000000 0.00000000 1.00000000
plane 6
-1.00000000 0.00000000 0.00000000 0.00000000 -1.00000000 0.00000000
plane 6
-1.00000000 1.00000000 0.00000000 0.00000000 1.00000000 0.00000000
plane 6
-1.00000000 0.00000000 0.00000000 -1.00000000 0.00000000 0.00000000
plane 6
2.00000000 0.00000000 0.00000000 1.00000000 0.00000000 0.00000000
plane 6
0.00000000 0.00000000 0.00000000 -1.00000000 0.00000000 0.00000000
plane 6
1.00000000 0.00000000 0.00000000 1.00000000 0.00000000 0.00000000
"""


expected_identifications = {
    id(periodic_1d): np.array([[1, 51, 1]]),
    id(periodic_2d): np.array(
        [[2, 1, 4], [3, 4, 4], [9, 17, 4], [10, 18, 4], [11, 19, 4], [12, 20, 4]]
    ),
    id(periodic_3d): np.array(
        [
            [1, 3, 1],
            [2, 5, 1],
            [4, 7, 1],
            [6, 8, 1],
            [9, 11, 1],
            [10, 12, 1],
            [15, 13, 1],
            [16, 14, 1],
            [21, 19, 1],
            [22, 20, 1],
            [25, 23, 1],
            [26, 24, 1],
            [38, 54, 1],
            [39, 55, 1],
            [40, 56, 1],
        ]
    ),
}

expected_identificationtypes = {
    id(periodic_1d): np.array([[2]]),
    id(periodic_2d): np.array([[1, 1, 1, 2]]),
    id(periodic_3d): np.array([[2]]),
}

expected_field_data = {
    id(periodic_1d): {},
    id(periodic_2d): {"outer": [3, 1], "periodic": [4, 1]},
    id(periodic_3d): {"outer": [6, 2], "default": [3, 2]},
}


@pytest.mark.parametrize("netgen_str", [periodic_1d, periodic_2d, periodic_3d])
def test_advanced(netgen_str):
    with tempfile.TemporaryDirectory() as temp_dir:
        p = pathlib.Path(temp_dir) / ("test.vol")
        with open(p, "w") as tf:
            tf.write(netgen_str)
        mesh = meshio.read(p)
        p2 = pathlib.Path(temp_dir) / ("test_out.vol")
        mesh.write(p2)
        mesh_out = meshio.read(p2)

    assert np.all(
        mesh.info["netgen:identifications"] == expected_identifications[id(netgen_str)]
    )
    assert np.all(
        mesh.info["netgen:identifications"] == mesh_out.info["netgen:identifications"]
    )
    assert np.all(
        mesh.info["netgen:identificationtypes"]
        == expected_identificationtypes[id(netgen_str)]
    )
    assert np.all(
        mesh.info["netgen:identificationtypes"]
        == mesh_out.info["netgen:identificationtypes"]
    )
    for kk, vv in mesh.field_data.items():
        assert np.all(vv == expected_field_data[id(netgen_str)][kk])
        assert np.all(vv == mesh_out.field_data[kk])
    for cd, cd_out in zip(
        mesh.cell_data["netgen:index"], mesh_out.cell_data["netgen:index"]
    ):
        assert np.all(cd == cd_out)
