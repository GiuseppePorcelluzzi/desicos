r"""
Cone/Cylinders (:mod:`desicos.conecylDB.ccs`)
======================================================

.. currentmodule:: desicos.conecylDB.ccs

This static database stores all entries in the dictionary ``ccs`` which can be
imported as::

    from desicos.conecylDB.ccs import ccs

More entries can be added here if one wishes to update the static database.

The entries shown in the Plug-In for Abaqus are those with the corresponding
keys listed in ``include_in_GUI``.

"""
from math import pi

def in2mm(value):
    return value * 25.4

ccs = {
    'astrium_des1': {
        'rbot': 2702.5,
        'H': 2064.0,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.125,
        'alphadeg': 41.28796038,
        'laminapropKey': 'mat_huehne_2008',
        'stack': [24., -24., 41., -41.],
        'axial_displ': 0.5,
        'pload': 10.,
        'database': 'desicos',
        },
    'astrium_des2': {
        'rbot': 1968,
        'H': 783,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.125,
        'alphadeg': 39.9563869,
        'laminapropKey': 'mat_huehne_2008',
        'stack': [24., -24., 41., -41.],
        'axial_displ': 0.5,
        'pload': 10.,
        'database': 'desicos',
        },
    'wp2_dlr_des_01': {
        'rbot': 250.,
        'H': 500.,
        'elem_type': 'S4R',
        'numel_r':  192,
        'artificial_damping': True,
        'plyt':0.125,
        'laminapropKey': 'degenhardt_2010_IM78552_isa',
        'allowablesKey': 'degenhardt_2010_IM78552_isa',
        'stack': [24.,-24.,41.,-41.],
        'axial_displ': 1.,
        'ploads': [1,2,3,4,5,10],
        },
    'wp2_dlr_des_02': {
        'rbot': 400.,
        'H': 800.,
        'elem_type': 'S4R',
        'numel_r':  192,
        'artificial_damping': True,
        'plyt':0.125,
        'laminapropKey': 'degenhardt_2010_IM78552_isa',
        'allowablesKey': 'degenhardt_2010_IM78552_isa',
        'stack': [34, -34, 0, 0, 53, -53],
        'axial_displ': 0.6,
        'ploads': [4,5,10,11,12,13,14,15,20,30],
        },
    'desicos_2014_c17': {
        'alphadeg': 35.,
        'rbot': 400.,
        'H': 300.,
        'artificial_damping': True,
        'plyt':0.125,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [30, 0, -30, -30, 0, 30],
        'database': 'desicos',
        'elem_type': 'S8R',
        'numel_r': 140,
        'ploads': [0.5, 1, 2, 5, 7, 10, 15],
        'axial_displ': 0.5,
        },
    'desicos_2014_c18': {
        'alphadeg': 35.,
        'rbot': 400.,
        'H': 300.,
        'artificial_damping': True,
        'plyt':0.125,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [30, -30, 0, 0, 30, -30],
        'database': 'desicos',
        'elem_type': 'S8R',
        'numel_r': 140,
        'ploads': [0.5, 1, 2, 5, 7, 10, 15],
        'axial_displ': 0.5,
        },
    'astrium_ESC-A_Cone3936': {
        'rbot': 1968.,
        'H': 776.27117054125858,
        'alphadeg': 40.2,
        'elem_type': 'S4R',
        'numel_r':  240,
        'plyt':0.250,
        'laminapropKey': 'M40J/77-2',
        'stack': [0]*28,
        'axial_displ': 1.0,
        'pload': 20.,
        'database': 'desicos',
        },
    'astrium_1': {
        'rbot': 400.,
        'H': 150.,
        'alphadeg': 45.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.125,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [0,45,0,-45,90,90,-45,0,45,0],
        'axial_displ': 1.0,
        'pload': 20.,
        'database': 'desicos',
        },
    'astrium_1_less_2x0_plies': {
        'rbot': 400.,
        'H': 150.,
        'alphadeg': 45.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.125,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [0,45,-45,90,90,-45,45,0],
        'axial_displ': 1.0,
        'pload': 20.,
        'database': 'desicos',
        },
    'astrium_1_less_2x0_plies_45_out': {
        'rbot': 400.,
        'H': 150.,
        'alphadeg': 45.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.125,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [45,-45,0,90,90,0,-45,45],
        'axial_displ': 1.0,
        'pload': 20.,
        'damping_factor':4.e-7,
        'database': 'desicos',
        },
    'astrium_1_less_3x0_plies': {
        'rbot': 400.,
        'H': 150.,
        'alphadeg': 45.,
        'elem_type': 'S4R5',
        'numel_r': 360,
        'plyt':0.125,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [45,-45,90,0,90,-45,45],
        'axial_displ': 0.6,
        'ploads': [0.2,0.5,1.,5.,10.,15.,30.],
        'damping_factor':4.e-7,
        'database': 'desicos',
        },
    'astrium_3': {
        'rbot': 400.,
        'H': 200.,
        'alphadeg': 45.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.125,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [0,45,0,-45,90,0,0,90,-45,0,45,0],
        'axial_displ': 1.0,
        'pload': 20.,
        'database': 'desicos',
        },
    'astrium_3_less_2x0_plies_45_out': {
        'rbot': 400.,
        'H': 200.,
        'alphadeg': 45.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.125,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [45,-45,0,90,0,0,90,0,-45,45],
        'axial_displ': 1.0,
        'pload': 20.,
        'database': 'desicos',
        },
    'astrium_3_less_4x0_plies_45_out': {
        'rbot': 400.,
        'H': 200.,
        'alphadeg': 45.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.125,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [45,-45,90,0,0,90,-45,45],
        'axial_displ': 1.0,
        'pload': 20.,
        'database': 'desicos',
        },
    'astrium_3_less_5x0_plies_45_out': {
        'rbot': 400.,
        'H': 200.,
        'alphadeg': 45.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.125,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [45,-45,90,0,90,-45,45],
        'axial_displ': 1.0,
        'pload': 20.,
        'database': 'desicos',
        },
    'astrium_3_7a_original': {
        'rbot': 400.,
        'H': 200.,
        'alphadeg': 45.,
        'elem_type': 'S8R5',
        'numel_r': 120,
        'plyt':0.125,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [30, -30,-60, 60, 0 ,60,-60,-30, 30],
        'axial_displ': 0.6,
        'ploads': [0.5,1.,2.,10.,20.,30.,35.,40.,70.],
        'database': 'desicos',
        },
    'astrium_3_7b_original': {
        'rbot': 400.,
        'H': 200.,
        'alphadeg': 45.,
        'elem_type': 'S8R5',
        'numel_r': 120,
        'plyt':0.125,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [45,30,-45,-30, 0 ,-30,-45,30,45],
        'axial_displ': 1.0,
        'pload': 20.,
        'database': 'desicos',
        },
    'quasi_isotropic_cylinder': {
        'rbot': 400.,
        'H': 800.,
        'elem_type': 'S8R5',
        'numel_r': 120,
        'plyt':0.125,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [45,-45,90,0,0,90,-45,45],
        'axial_displ': 1.0,
        'database': 'desicos',
        },
    'wp2_rtu_d796': {
        'rbot': 398.,
        'H': 600.,
        'elem_type': 'S8R5',
        'numel_r': 120,
        'plyt':0.5,
        'laminapropKey': 'aisi_304_from_asm_aerospace',
        'stack': [0],
        'axial_displ': 1.0,
        'database': 'desicos',
        },
    'wp2_rtu_d796L': { # L stays for long...
        'rbot': 398.,
        'H': 1200.,
        'elem_type': 'S8R5',
        'numel_r': 120,
        'plyt':0.5,
        'laminapropKey': 'aisi_304_from_asm_aerospace',
        'stack': [0],
        'axial_displ': 1.0,
        'database': 'desicos',
        },
    'sosa_2006_steel': {
        'rbot': 15240.,
        'H': 13100.,
        'elem_type': 'S8R5',
        'numel_r': 220,
        'plyt':7.9,
        'laminapropKey': 'sosa_2006_steel',
        'stack': [0],
        'axial_displ': 1.0,
        'database': 'desicos',
        },
    'wp3_t04_02_zsym': {
        'rbot': 400.,
        'H': 800.,
        'elem_type': 'S8R5',
        'numel_r': 120,
        'plyt':0.125,
        'laminapropKey': 'geier_2002',
        'stack': [ 45, -45, 0, 0, -45, 45 ],
        'axial_displ': 0.5,
        'ploads': [1.,2.,3.,8.,8.5,9.,10.],
        'database': 'desicos',
        },
    'efre_2014_r04': {
        'msi': 'efre_2014_r04',
        'ti': 'efre_2014_r04',
        'rbot': 150.,
        'H': 300.,
        'elem_type': 'S8R5',
        'numel_r': 140,
        'plyt':0.1044,
        'laminapropKey': 'efre_2014',
        'allowablesKey': 'efre_2014',
        'stack': [0, 0, +45, -45, +45, -45],
        'axial_displ': 0.5,
        'ploads': [1.,2.,3.,5.,10.],
        'database': 'efre',
        },
    'efre_2014_r05': {
        'msi': 'efre_2014_r05',
        'ti': 'efre_2014_r05',
        'rbot': 150.,
        'H': 300.,
        'elem_type': 'S8R5',
        'numel_r': 140,
        'plyt':0.1044,
        'laminapropKey': 'efre_2014',
        'allowablesKey': 'efre_2014',
        'stack': [0, 0, +45, -45, +45, -45],
        'axial_displ': 0.5,
        'ploads': [1.,2.,3.,5.,10.],
        'database': 'efre',
        },
    'efre_2014_r07': {
        'msi': 'efre_2014_r07',
        'ti': 'efre_2014_r07',
        'rbot': 250.,
        'H': 500.,
        'elem_type': 'S8R5',
        'numel_r': 140,
        'plyt':0.1044,
        'laminapropKey': 'efre_2014',
        'allowablesKey': 'efre_2014',
        'stack': [0, 0, +45, -45, +45, -45],
        'axial_displ': 0.5,
        'ploads': [1.,2.,3.,5.,10.],
        'database': 'efre',
        },
    'efre_2014_r08': {
        'msi': 'efre_2014_r08',
        'ti': 'efre_2014_r08',
        'rbot': 250.,
        'H': 500.,
        'elem_type': 'S8R5',
        'numel_r': 140,
        'plyt':0.1044,
        'laminapropKey': 'efre_2014',
        'allowablesKey': 'efre_2014',
        'stack': [0, 0, +45, -45, +45, -45],
        'axial_displ': 0.5,
        'ploads': [1.,2.,3.,5.,10.],
        'database': 'efre',
        },
    'efre_2014_r09': {
        'msi': 'efre_2014_r09',
        'ti': 'efre_2014_r09',
        'rbot': 250.,
        'H': 500.,
        'elem_type': 'S8R5',
        'numel_r': 140,
        'plyt':0.1044,
        'laminapropKey': 'efre_2014',
        'allowablesKey': 'efre_2014',
        'stack': [0, 0, +45, -45, +45, -45],
        'axial_displ': 0.5,
        'ploads': [1.,2.,3.,5.,10.],
        'database': 'efre',
        },
    'efre_2014_r07_laser': {
        'msi': 'efre_2014_r07_laser',
        'rbot': 250.,
        'H': 500.,
        'elem_type': 'S8R5',
        'numel_r': 140,
        'plyt':0.1044,
        'laminapropKey': 'efre_2014',
        'allowablesKey': 'efre_2014',
        'stack': [0, 0, +45, -45, +45, -45],
        'axial_displ': 0.5,
        'ploads': [1.,2.,3.,5.,10.],
        'database': 'efre',
        },
    'efre_2014_r08_laser': {
        'msi': 'efre_2014_r08_laser',
        'rbot': 250.,
        'H': 500.,
        'elem_type': 'S8R5',
        'numel_r': 140,
        'plyt':0.1044,
        'laminapropKey': 'efre_2014',
        'allowablesKey': 'efre_2014',
        'stack': [0, 0, +45, -45, +45, -45],
        'axial_displ': 0.5,
        'ploads': [1.,2.,3.,5.,10.],
        'database': 'efre',
        },
    'efre_2014_r09_laser': {
        'msi': 'efre_2014_r09_laser',
        'rbot': 250.,
        'H': 500.,
        'elem_type': 'S8R5',
        'numel_r': 140,
        'plyt':0.1044,
        'laminapropKey': 'efre_2014',
        'allowablesKey': 'efre_2014',
        'stack': [0, 0, +45, -45, +45, -45],
        'axial_displ': 0.5,
        'ploads': [1.,2.,3.,5.,10.],
        'database': 'efre',
        },
    'afp': {
        'msi': 'afp',
        'rbot': 1000.96, # outer-surface radius
        'H': 677.82,
        'elem_type': 'S4R5',
        'numel_r': 420,
        'plyt': 0.12111,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [0, +60, -60, 0, +60, -60, 0, +60, -60],
        'axial_displ': 0.5,
        'ploads': [1., 2., 3., 4., 5., 6., 7., 8., 9., 10.],
        'database': 'desicos',
        },
    'desicos_2014_z36': {
        'rbot': 400., # outer-surface radius
        'H': 800.,
        'elem_type': 'S8R5',
        'numel_r': 140,
        'plyt': 0.125,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [34, -34, 0, 0, 53, -53],
        'axial_displ': 0.5,
        'ploads': [1., 2., 3., 5., 10., 15., 20., 25.],
        'database': 'desicos',
        },
    'huehne_2002_z26': {
        'rbot': (250.+2*0.125),
        'H': 510.,
        'numel_r': 180,
        'elem_type': 'S4R',
        'plyt':0.125,
        'laminapropKey': 'geier_2002',
        'stack': [+24,-24,+41,-41],
        'axial_displ': 1.,
        'ploads': [1, 2, 3, 4, 5, 10],
        'database': 'dlr',
        },
    'huehne_2002_z27': {
        'rbot': (250.+2*0.125),
        'H': 510.,
        'numel_r': 180,
        'elem_type': 'S4R',
        'plyt':0.125,
        'laminapropKey': 'geier_2002',
        'stack': [+75,-75,+75,-75],
        'axial_displ': 1.,
        'ploads': [1, 2, 3, 4, 5, 10],
        'database': 'dlr',
        },
    'huehne_2002_z14': {
        'rbot': (250.+3*0.125),
        'H': 510.,
        'numel_r': 180,
        'elem_type': 'S4R',
        'plyt':0.125,
        'laminapropKey': 'geier_2002',
        'stack': [+51,-51,90,90,+40,-40],
        'axial_displ': 1.,
        'ploads': [1, 2, 3, 4, 5, 10,20,30],
        'database': 'dlr',
        },
    'huehne_2002_z22': {
        'rbot': (250.+3*0.125),
        'H': 510.,
        'numel_r': 180,
        'elem_type': 'S4R',
        'plyt':0.125,
        'laminapropKey': 'geier_2002',
        'stack': [+49,-49,+36,-36,0.,0.],
        'axial_displ': 1.,
        'ploads': [1, 2, 3, 4, 5, 10,20,30],
        'database': 'dlr',
        },
    'huehne_2002_z23': {
        'rbot': (250.+5*0.125),
        'H': 510.,
        'numel_r': 180,
        'elem_type': 'S4R',
        'plyt':0.125,
        'laminapropKey': 'geier_2002',
        'stack': [+60,-60,0,0,+68,-68,+52,-52,+37,-37],
        'axial_displ': 1.,
        'ploads': [1, 10, 20, 30, 40, 50, 70, 90],
        'database': 'dlr',
        },
    # laminate minimum of classical buckling load
    'huehne_2002_z24': {
        'rbot': (250.+5*0.125),
        'H': 510.,
        'numel_r': 180,
        'elem_type': 'S4R',
        'plyt':0.125,
        'laminapropKey': 'geier_2002',
        'stack': [-51., 51., -45., 45., -37., 37., -19., 19., 0., 0.],
        'axial_displ': 1.,
        'ploads': [1, 10, 20, 30, 40, 50, 70, 90],
        'database': 'dlr',
        },
    # laminate maximum of classical buckling load
    'huehne_2002_z30': {
        'rbot': (250.+5*0.125),
        'H': 510.,
        'numel_r': 180,
        'elem_type': 'S4R',
        'plyt':0.125,
        'laminapropKey': 'geier_2002',
        'stack': [30., -30., 90., 90., 22., -22., 38., -38., 53., -53. ],
        'axial_displ': 1.,
        'ploads': [1, 10, 20, 30, 40, 50, 70, 90],
        'database': 'dlr',
        },
    # laminate far from minimum and maximum classical buckling load
    'huehne_2002_z33': {
        'rbot': (250.+5*0.125),
        'H': 510.,
        'numel_r': 180,
        'elem_type': 'S4R',
        'plyt':0.125,
        'laminapropKey': 'geier_2002',
        'stack': [0.,0.,19.,-19.,37.,-37.,45.,-45.,51.,-51.],
        'axial_displ': 1.,
        'ploads': [1, 10, 20, 30, 40, 50, 70, 90],
        'database': 'dlr',
        },
    'huehne_2008_z07': {
        'rbot': 250.,
        'H': 510.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.125,
        'laminapropKey': 'mat_huehne_2008',
        'stack': [24., -24., 41., -41.],
        'axial_displ': 1.,
        'reflimitdisp': 0.24,
        'reflimitload': 16200.,
        'ploads': [1., 2., 3., 4., 5., 10.],
        'database': 'dlr',
        },
    'dinkler_2010': {
        'rbot': 100.,
        'H': 100.,
        'elsize': 5.,
        'plyt': 0.125,
        'stack': [ 0., 0., 0., 90.],
        'reflimitload': (145.3 * 2 * pi * 100.),
        'laminapropKey': 'mat_huehne_2008',
        'database': 'dlr',
        },
    'degenhardt_2010_z15': {
        'msi': 'degenhardt_2010_z15',
        'ti': 'degenhardt_2010_z15',
        'rbot': 250.27,
        'H': 500.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.11575,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [24,-24,41,-41],
        'axial_displ': 1.,
        'ploads': [1,2,3,4,5,10],
        'database': 'dlr',
        },
    'degenhardt_2010_z17': {
        'msi': 'degenhardt_2010_z17',
        'ti': 'degenhardt_2010_z17',
        'rbot': 250.35,
        'H': 500.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.11525,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [24,-24,41,-41],
        'axial_displ': 1.,
        'ploads': [1,2,3,4,5,10],
        'database': 'dlr',
        },
    'degenhardt_2010_z18': {
        'msi': 'degenhardt_2010_z18',
        'ti': 'degenhardt_2010_z18',
        'rbot': 250.30,
        'H': 500.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.1195,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [24,-24,41,-41],
        'axial_displ': 1.,
        'ploads': [1,2,3,4,5,10],
        'database': 'dlr',
        },
    'degenhardt_2010_z20': {
        'msi': 'degenhardt_2010_z20',
        'ti': 'degenhardt_2010_z20',
        'rbot': 250.30,
        'H': 500.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.12225,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [24,-24,41,-41],
        'axial_displ': 1.,
        'ploads': [1,2,3,4,5,10],
        'database': 'dlr',
        },
    'degenhardt_2010_z21': {
        'msi': 'degenhardt_2010_z21',
        'ti': 'degenhardt_2010_z21',
        'rbot': 250.24,
        'H': 500.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.12125,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [24,-24,41,-41],
        'axial_displ': 1.,
        'ploads': [1,2,3,4,5,10],
        'database': 'dlr',
        },
    'degenhardt_2010_z22': {
        'msi': 'degenhardt_2010_z22',
        'ti': 'degenhardt_2010_z22',
        'rbot': 250.30,
        'H': 500.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.1215,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [24,-24,41,-41],
        'axial_displ': 1.,
        'ploads': [1,2,3,4,5,10],
        'database': 'dlr',
        },
    'degenhardt_2010_z23': {
        'msi': 'degenhardt_2010_z23',
        'ti': 'degenhardt_2010_z23',
        'rbot': 250.23,
        'H': 500.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.1195,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [24,-24,41,-41],
        'axial_displ': 1.,
        'ploads': [1,2,3,4,5,10],
        'database': 'dlr',
        },
    'degenhardt_2010_z24': {
        'msi': 'degenhardt_2010_z24',
        'ti': 'degenhardt_2010_z24',
        'rbot': 250.22,
        'H': 500.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.12375,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [24,-24,41,-41],
        'axial_displ': 1.,
        'ploads': [1,2,3,4,5,10],
        'database': 'dlr',
        },
    'degenhardt_2010_z25': {
        'msi': 'degenhardt_2010_z25',
        'ti': 'degenhardt_2010_z25',
        'rbot': 250.24,
        'H': 500.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.117,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [24,-24,41,-41],
        'axial_displ': 1.,
        'ploads': [1,2,3,4,5,10],
        'database': 'dlr',
        },
    'degenhardt_2010_z26': {
        'msi': 'degenhardt_2010_z26',
        'ti': 'degenhardt_2010_z26',
        'rbot': 250.27,
        'H': 500.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.1195,
        'laminapropKey': 'degenhardt_2010_IM78552_cocomat',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [24,-24,41,-41],
        'axial_displ': 1.,
        'ploads': [1,2,3,4,5,10],
        'database': 'dlr',
        },
    'zimmermann_1992_z32': {
        'rbot': 250.,
        'H': 510.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.125,
        'laminapropKey': 'geier_2002',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [-51,51,-45,45,-37,37,-19,19,0,0],
        'axial_displ': 1.,
        'ploads': [1., 20., 30., 35., 50., 75],
        'database': 'dlr',
        },
    'zimmermann_1992_z33': {
        'msi': 'zimmermann_1992_z33',
        'rbot': 250.,
        'H': 510.,
        'elem_type': 'S4R',
        'numel_r': 240,
        'plyt':0.125,
        'laminapropKey': 'geier_2002',
        'allowablesKey': 'degenhardt_2010_IM78552_cocomat',
        'stack': [0,0,19,-19,37,-37,45,-45,51,-51],
        'axial_displ': 1.,
        'ploads': [1, 10, 20, 30, 40, 46.5, 70, 90],
        'database': 'dlr',
        },
    'geier_1991_z11': {
        'elem_type': 'S8R5',
        'numel_r': 140,
        'rbot': 250.,
        'H': 510.,
        'plyt':0.125,
        'laminapropKey': 'geier_1997',
        'stack': [60, -60, 0, 0, 68, -68, 52, -52, 37, -37],
        'database': 'dlr',
        },
    'geier_1991_z12': {
        'elem_type': 'S8R5',
        'numel_r': 140,
        'rbot': 250.,
        'H': 510.,
        'plyt':0.125,
        'laminapropKey': 'geier_1997',
        'stack': [51, -51, 45, -45, 37, -37, 19, -19, 0, 0],
        'database': 'dlr',
        },
    'geier_1991_z14': {
        'elem_type': 'S8R5',
        'numel_r': 140,
        'rbot': 250.,
        'H': 510.,
        'plyt':0.125,
        'laminapropKey': 'geier_1997',
        'stack': [51, -51, 90, 90, 40, -40],
        'database': 'dlr',
        },
    'geier_1991_z17': {
        'elem_type': 'S8R5',
        'numel_r': 140,
        'rbot': 250.,
        'H': 510.,
        'plyt':0.125,
        'laminapropKey': 'geier_1997',
        'stack': [30, -30, 90, 90, 22, -22, 38, -38, 53, -53],
        'database': 'dlr',
        },
    'geier_1991_z18': {
        'elem_type': 'S8R5',
        'numel_r': 140,
        'rbot': 250.,
        'H': 510.,
        'plyt':0.125,
        'laminapropKey': 'geier_1997',
        'stack': [-37, 37, -52, 52, -68, 68, 0, 0, -60, 60],
        'database': 'dlr',
        },
    'geier_1991_z21': {
        'elem_type': 'S8R5',
        'numel_r': 140,
        'rbot': 250.,
        'H': 510.,
        'plyt':0.125,
        'laminapropKey': 'geier_1997',
        'stack': [39, -39, 0, 0, 50, -50],
        'database': 'dlr',
        },
    'geier_1991_z22': {
        'elem_type': 'S8R5',
        'numel_r': 140,
        'rbot': 250.,
        'H': 510.,
        'plyt':0.125,
        'laminapropKey': 'geier_1997',
        'stack': [49, -49, 36, -36, 0, 0],
        'database': 'dlr',
        },
    'hilburger_2002_c1': {
        'msi': 'awcyl9201',
        'ti': 'awcyl9201',
        'rbot': in2mm(8.),
        'H': in2mm(16.),
        'plyt': in2mm(0.005),
        'elem_type': 'S4R',
        'numel_r': 252,
        'laminapropKey': 'hilburger_2002',
        'stack': [+45,-45,0,0,0,0,-45,+45],
        'ploads': [1,2,5,10,30],
        'database': 'nasa',
        },
    'hilburger_2002_c2': {
        'msi': 'awcyl9202',
        'ti': 'awcyl9202',
        'rbot': in2mm(8.),
        'H': in2mm(16.),
        'plyt': in2mm(0.005),
        'elem_type': 'S4R',
        'numel_r': 252,
        'laminapropKey': 'hilburger_2002',
        'stack': [+45,-45,90,90,90,90,-45,+45],
        'ploads': [1,2,5,10,30],
        'database': 'nasa',
        },
    'hilburger_2002_c3': {
        'msi': 'awcyl9203',
        'ti': 'awcyl9203',
        'rbot': in2mm(8.),
        'H': in2mm(16.),
        'plyt': in2mm(0.005),
        'elem_type': 'S4R',
        'numel_r': 252,
        'laminapropKey': 'hilburger_2002',
        'stack': [+45,-45,0,90,90,0,-45,+45],
        'ploads': [1,2,5,10,30],
        'database': 'nasa',
        },
    'hilburger_2004_c1': {
        'msi': 'awcyl9201',
        'ti': 'awcyl9201',
        'rbot': in2mm(8.),
        'H': in2mm(16.),
        'plyt': in2mm(0.005),
        'elem_type': 'S4R',
        'numel_r': 252,
        'laminapropKey': 'hilburger_2004',
        'stack': [+45,-45,0,0,0,0,-45,+45],
        'ploads': [1,2,5,10,30],
        'database': 'nasa',
        },
    'hilburger_2004_c2': {
        'msi': 'awcyl9202',
        'ti': 'awcyl9202',
        'rbot': in2mm(8.),
        'H': in2mm(16.),
        'plyt': in2mm(0.005),
        'elem_type': 'S4R',
        'numel_r': 252,
        'laminapropKey': 'hilburger_2004',
        'stack': [+45,-45,90,90,90,90,-45,+45],
        'ploads': [1,2,5,10,30],
        'database': 'nasa',
        },
    'hilburger_2004_c3': {
        'msi': 'awcyl9203',
        'ti': 'awcyl9203',
        'rbot': in2mm(8.),
        'H': in2mm(16.),
        'plyt': in2mm(0.005),
        'elem_type': 'S4R',
        'numel_r': 252,
        'laminapropKey': 'hilburger_2004',
        'stack': [+45,-45,0,90,90,0,-45,+45],
        'ploads': [1,2,5,10,30],
        'database': 'nasa',
        },
    'hilburger_2002_c6': {
        'msi': 'awcyl111',
        'ti': 'awcyl111',
        'rbot': in2mm(8.),
        'H': in2mm(16.),
        'plyt': in2mm(0.005),
        'elem_type': 'S4R',
        'numel_r': 252,
        'laminapropKey': 'hilburger_2004',
        'stack': [+45,-45,0,90,+45,-45,0,90,90,0,-45,+45,90,0,-45,+45],
        'ploads': [1,2,5,10,30,40,50,70,100],
        'database': 'nasa',
        },
    'hilburger_2014_c1': {
        'rbot': 406.4,
        'plyt': in2mm(0.032),
        'H': 1219.2,
        'numel_r': 128,
        'elem_type': 'S8R5',
        'laminapropKey': 'hilburger_2014_AlLi',
        'stack': [0],
        'allowablesKey': 'hilburger_2014_AlLi',
        },

        }

ccs['wp2_pfh_des_01'] = ccs['astrium_1_less_3x0_plies']
ccs['wp2_pfh_des_02'] = ccs['astrium_3_7a_original']
ccs['castro_2014_c02'] = ccs['astrium_3_7a_original']
ccs['desicos_2014_z37'] = ccs['desicos_2014_z36']

include_in_GUI = ['desicos_2014_z36',
                  'desicos_2014_c17',
                  'desicos_2014_c18',
                  'wp2_pfh_des_01',
                  'wp2_pfh_des_02',
                  'wp2_dlr_des_01',
                  'wp2_dlr_des_02',
                  'efre_2014_r04',
                  'efre_2014_r05',
                  'efre_2014_r07',
                  'efre_2014_r08',
                  'efre_2014_r09',
                  'afp',
                  'zimmermann_1992_z32',
                  'zimmermann_1992_z33',
                  'huehne_2002_z14',
                  'huehne_2002_z22',
                  'huehne_2002_z24',
                  'huehne_2002_z27',
                  'huehne_2002_z30',
                  'huehne_2002_z33',
                  'huehne_2008_z07',
                  'degenhardt_2010_z15',
                  'degenhardt_2010_z17',
                  'degenhardt_2010_z18',
                  'degenhardt_2010_z20',
                  'degenhardt_2010_z21',
                  'degenhardt_2010_z22',
                  'degenhardt_2010_z23',
                  'degenhardt_2010_z24',
                  'degenhardt_2010_z25',
                  'degenhardt_2010_z26',
                  'geier_1991_z11',
                  'geier_1991_z12',
                  'geier_1991_z14',
                  'geier_1991_z17',
                  'geier_1991_z18',
                  'geier_1991_z21',
                  'geier_1991_z22',
                  'dinkler_2010',
                  ]

include_in_GUI += [k for k in ccs.keys() if 'hilburger' in k]


include_in_GUI = sorted(set(include_in_GUI))

