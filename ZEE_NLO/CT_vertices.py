# This file was automatically created by FeynRules 2.3.36
# Mathematica version: 11.3.0 for Linux x86 (64-bit) (March 7, 2018)
# Date: Fri 13 Dec 2019 21:47:43


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_501_125,(0,0,1):C.R2GC_501_126})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,1,0):C.R2GC_420_71,(2,1,1):C.R2GC_420_72,(0,1,0):C.R2GC_420_71,(0,1,1):C.R2GC_420_72,(6,1,0):C.R2GC_423_76,(6,1,1):C.R2GC_507_133,(4,1,0):C.R2GC_418_67,(4,1,1):C.R2GC_418_68,(3,1,0):C.R2GC_418_67,(3,1,1):C.R2GC_418_68,(8,1,0):C.R2GC_419_69,(8,1,1):C.R2GC_419_70,(7,1,0):C.R2GC_424_78,(7,1,1):C.R2GC_506_132,(5,1,0):C.R2GC_418_67,(5,1,1):C.R2GC_418_68,(1,1,0):C.R2GC_418_67,(1,1,1):C.R2GC_418_68,(11,0,0):C.R2GC_422_74,(11,0,1):C.R2GC_422_75,(10,0,0):C.R2GC_422_74,(10,0,1):C.R2GC_422_75,(9,0,1):C.R2GC_421_73,(2,2,0):C.R2GC_420_71,(2,2,1):C.R2GC_420_72,(0,2,0):C.R2GC_420_71,(0,2,1):C.R2GC_420_72,(4,2,0):C.R2GC_418_67,(4,2,1):C.R2GC_418_68,(3,2,0):C.R2GC_418_67,(3,2,1):C.R2GC_418_68,(8,2,0):C.R2GC_419_69,(8,2,1):C.R2GC_505_131,(6,2,0):C.R2GC_503_128,(6,2,1):C.R2GC_503_129,(7,2,0):C.R2GC_424_78,(7,2,1):C.R2GC_424_79,(5,2,0):C.R2GC_418_67,(5,2,1):C.R2GC_418_68,(1,2,0):C.R2GC_418_67,(1,2,1):C.R2GC_418_68,(2,3,0):C.R2GC_420_71,(2,3,1):C.R2GC_420_72,(0,3,0):C.R2GC_420_71,(0,3,1):C.R2GC_420_72,(4,3,0):C.R2GC_418_67,(4,3,1):C.R2GC_418_68,(3,3,0):C.R2GC_418_67,(3,3,1):C.R2GC_418_68,(8,3,0):C.R2GC_419_69,(8,3,1):C.R2GC_502_127,(6,3,0):C.R2GC_423_76,(6,3,1):C.R2GC_423_77,(7,3,0):C.R2GC_504_130,(7,3,1):C.R2GC_420_72,(5,3,0):C.R2GC_418_67,(5,3,1):C.R2GC_418_68,(1,3,0):C.R2GC_418_67,(1,3,1):C.R2GC_418_68})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.u__tilde__, P.d, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.d, P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_524_145,(0,1,0):C.R2GC_525_146})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.c__tilde__, P.d, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.c, P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_469_104,(0,1,0):C.R2GC_468_103})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.u__tilde__, P.s, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.g, P.s, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_527_148,(0,1,0):C.R2GC_528_149})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.c__tilde__, P.s, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.c, P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_484_114,(0,1,0):C.R2GC_483_113})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_498_123,(0,1,0):C.R2GC_499_124})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_463_98})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.s__tilde__, P.s, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_478_108})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_443_87})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_464_99})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_479_109})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_444_88})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_466_101})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_481_111})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_445_89})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_520_141,(0,1,0):C.R2GC_516_137})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_521_142,(0,1,0):C.R2GC_517_138})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_462_97,(0,1,0):C.R2GC_465_100})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_477_107,(0,1,0):C.R2GC_480_110})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_495_120,(0,1,0):C.R2GC_492_117})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_518_139})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_452_92})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_493_118})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_519_140})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_453_93})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_494_119})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_522_143})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_454_94})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_496_121})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_427_82})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_427_82})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_427_82})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_425_80})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_425_80})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_425_80})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_426_81})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_426_81})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_426_81})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_426_81})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_426_81})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_426_81})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_512_135})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_513_136})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_459_96})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_474_106})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_489_116})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_523_144})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_467_102})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_526_147})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_482_112})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_497_122})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV6 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_450_91,(0,1,0):C.R2GC_442_86})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV6 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_450_91,(0,1,0):C.R2GC_442_86})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_450_91,(0,1,0):C.R2GC_442_86})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_441_85,(0,1,0):C.R2GC_442_86})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_441_85,(0,1,0):C.R2GC_442_86})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_441_85,(0,1,0):C.R2GC_442_86})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_511_134,(0,1,0):C.R2GC_437_83})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_449_90,(0,1,0):C.R2GC_437_83})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_488_115,(0,1,0):C.R2GC_437_83})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_458_95,(0,1,0):C.R2GC_437_83})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_473_105,(0,1,0):C.R2GC_437_83})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_440_84,(0,1,0):C.R2GC_437_83})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV2, L.VV3, L.VV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,2,4):C.R2GC_398_1,(0,0,0):C.R2GC_402_7,(0,0,2):C.R2GC_402_8,(0,0,3):C.R2GC_402_9,(0,0,5):C.R2GC_402_10,(0,0,6):C.R2GC_402_11,(0,0,7):C.R2GC_402_12,(0,1,1):C.R2GC_399_2})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.g, P.g, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_407_21,(0,0,1):C.R2GC_407_22,(0,0,2):C.R2GC_407_23,(0,0,3):C.R2GC_407_24,(0,0,4):C.R2GC_407_25,(0,0,5):C.R2GC_407_26})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.g, P.g, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_408_27,(0,0,1):C.R2GC_408_28,(0,0,2):C.R2GC_408_29,(0,0,3):C.R2GC_408_30,(0,0,4):C.R2GC_408_31,(0,0,5):C.R2GC_408_32})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_403_13,(0,0,1):C.R2GC_403_14})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_406_19,(0,0,1):C.R2GC_406_20})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_413_57,(0,0,1):C.R2GC_413_58,(0,0,2):C.R2GC_413_59,(0,0,3):C.R2GC_413_60,(0,0,4):C.R2GC_413_61})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_400_3,(0,0,1):C.R2GC_400_4})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_405_17,(1,0,1):C.R2GC_405_18,(0,1,0):C.R2GC_404_15,(0,1,1):C.R2GC_404_16})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_401_5,(0,0,1):C.R2GC_401_6})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.g, P.g, P.HL, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_410_39,(0,0,1):C.R2GC_410_40,(0,0,2):C.R2GC_410_41,(0,0,3):C.R2GC_410_42,(0,0,4):C.R2GC_410_43,(0,0,5):C.R2GC_410_44})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.g, P.g, P.HH, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_411_45,(0,0,1):C.R2GC_411_46,(0,0,2):C.R2GC_411_47,(0,0,3):C.R2GC_411_48,(0,0,4):C.R2GC_411_49,(0,0,5):C.R2GC_411_50})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.g, P.g, P.HH, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_412_51,(0,0,1):C.R2GC_412_52,(0,0,2):C.R2GC_412_53,(0,0,3):C.R2GC_412_54,(0,0,4):C.R2GC_412_55,(0,0,5):C.R2GC_412_56})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_409_33,(0,0,1):C.R2GC_409_34,(0,0,2):C.R2GC_409_35,(0,0,3):C.R2GC_409_36,(0,0,4):C.R2GC_409_37,(0,0,5):C.R2GC_409_38})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_414_62,(0,0,1):C.R2GC_414_63,(0,0,2):C.R2GC_414_64,(0,0,3):C.R2GC_414_65,(0,0,4):C.R2GC_414_66})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,1,0):C.UVGC_501_133,(0,1,1):C.UVGC_501_134,(0,1,2):C.UVGC_501_135,(0,1,5):C.UVGC_501_136,(0,1,6):C.UVGC_501_137,(0,1,7):C.UVGC_501_138,(0,2,3):C.UVGC_415_1,(0,0,4):C.UVGC_416_2})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(2,1,4):C.UVGC_419_8,(2,1,5):C.UVGC_419_7,(0,1,4):C.UVGC_419_8,(0,1,5):C.UVGC_419_7,(6,1,0):C.UVGC_506_165,(6,1,2):C.UVGC_506_166,(6,1,3):C.UVGC_506_167,(6,1,4):C.UVGC_507_173,(6,1,5):C.UVGC_507_174,(6,1,6):C.UVGC_506_170,(6,1,7):C.UVGC_506_171,(6,1,8):C.UVGC_506_172,(4,1,4):C.UVGC_418_5,(4,1,5):C.UVGC_418_6,(3,1,4):C.UVGC_418_5,(3,1,5):C.UVGC_418_6,(8,1,4):C.UVGC_419_7,(8,1,5):C.UVGC_419_8,(7,1,0):C.UVGC_506_165,(7,1,2):C.UVGC_506_166,(7,1,3):C.UVGC_506_167,(7,1,4):C.UVGC_506_168,(7,1,5):C.UVGC_506_169,(7,1,6):C.UVGC_506_170,(7,1,7):C.UVGC_506_171,(7,1,8):C.UVGC_506_172,(5,1,4):C.UVGC_418_5,(5,1,5):C.UVGC_418_6,(1,1,4):C.UVGC_418_5,(1,1,5):C.UVGC_418_6,(11,0,4):C.UVGC_422_11,(11,0,5):C.UVGC_422_12,(10,0,4):C.UVGC_422_11,(10,0,5):C.UVGC_422_12,(9,0,4):C.UVGC_421_9,(9,0,5):C.UVGC_421_10,(2,2,4):C.UVGC_419_8,(2,2,5):C.UVGC_419_7,(0,2,4):C.UVGC_419_8,(0,2,5):C.UVGC_419_7,(4,2,4):C.UVGC_418_5,(4,2,5):C.UVGC_418_6,(3,2,4):C.UVGC_418_5,(3,2,5):C.UVGC_418_6,(8,2,0):C.UVGC_505_157,(8,2,2):C.UVGC_505_158,(8,2,3):C.UVGC_505_159,(8,2,4):C.UVGC_505_160,(8,2,5):C.UVGC_505_161,(8,2,6):C.UVGC_505_162,(8,2,7):C.UVGC_505_163,(8,2,8):C.UVGC_505_164,(6,2,0):C.UVGC_503_147,(6,2,2):C.UVGC_503_148,(6,2,3):C.UVGC_503_149,(6,2,4):C.UVGC_503_150,(6,2,5):C.UVGC_503_151,(6,2,6):C.UVGC_503_152,(6,2,7):C.UVGC_503_153,(6,2,8):C.UVGC_503_154,(7,2,1):C.UVGC_423_13,(7,2,4):C.UVGC_424_15,(7,2,5):C.UVGC_424_16,(5,2,4):C.UVGC_418_5,(5,2,5):C.UVGC_418_6,(1,2,4):C.UVGC_418_5,(1,2,5):C.UVGC_418_6,(2,3,4):C.UVGC_419_8,(2,3,5):C.UVGC_419_7,(0,3,4):C.UVGC_419_8,(0,3,5):C.UVGC_419_7,(4,3,4):C.UVGC_418_5,(4,3,5):C.UVGC_418_6,(3,3,4):C.UVGC_418_5,(3,3,5):C.UVGC_418_6,(8,3,0):C.UVGC_502_139,(8,3,2):C.UVGC_502_140,(8,3,3):C.UVGC_502_141,(8,3,4):C.UVGC_502_142,(8,3,5):C.UVGC_502_143,(8,3,6):C.UVGC_502_144,(8,3,7):C.UVGC_502_145,(8,3,8):C.UVGC_502_146,(6,3,1):C.UVGC_423_13,(6,3,4):C.UVGC_423_14,(6,3,5):C.UVGC_421_9,(7,3,0):C.UVGC_503_147,(7,3,2):C.UVGC_503_148,(7,3,3):C.UVGC_503_149,(7,3,4):C.UVGC_504_155,(7,3,5):C.UVGC_504_156,(7,3,6):C.UVGC_503_152,(7,3,7):C.UVGC_503_153,(7,3,8):C.UVGC_503_154,(5,3,4):C.UVGC_418_5,(5,3,5):C.UVGC_418_6,(1,3,4):C.UVGC_418_5,(1,3,5):C.UVGC_418_6})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_524_205,(0,0,2):C.UVGC_524_206,(0,0,1):C.UVGC_524_207,(0,1,0):C.UVGC_525_208,(0,1,2):C.UVGC_525_209,(0,1,1):C.UVGC_525_210})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.c__tilde__, P.d, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_469_70,(0,0,2):C.UVGC_469_71,(0,0,0):C.UVGC_469_72,(0,1,1):C.UVGC_468_67,(0,1,2):C.UVGC_468_68,(0,1,0):C.UVGC_468_69})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.u__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_527_214,(0,0,2):C.UVGC_527_215,(0,0,1):C.UVGC_527_216,(0,1,0):C.UVGC_528_217,(0,1,2):C.UVGC_528_218,(0,1,1):C.UVGC_528_219})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_484_97,(0,0,2):C.UVGC_484_98,(0,0,1):C.UVGC_484_99,(0,1,0):C.UVGC_483_94,(0,1,2):C.UVGC_483_95,(0,1,1):C.UVGC_483_96})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_498_121,(0,0,2):C.UVGC_498_122,(0,0,1):C.UVGC_498_123,(0,1,0):C.UVGC_499_124,(0,1,2):C.UVGC_499_125,(0,1,1):C.UVGC_499_126})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_463_58})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_478_85})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_443_34})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_464_59})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_479_86})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_444_35})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_466_63})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_481_90})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_445_36})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_520_195,(0,0,2):C.UVGC_520_196,(0,0,1):C.UVGC_520_197,(0,1,0):C.UVGC_516_187,(0,1,2):C.UVGC_516_188,(0,1,1):C.UVGC_516_189})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.s__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_521_198,(0,0,2):C.UVGC_521_199,(0,0,1):C.UVGC_521_200,(0,1,0):C.UVGC_517_190,(0,1,2):C.UVGC_517_191,(0,1,1):C.UVGC_517_192})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.d__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_462_55,(0,0,2):C.UVGC_462_56,(0,0,0):C.UVGC_462_57,(0,1,1):C.UVGC_465_60,(0,1,2):C.UVGC_465_61,(0,1,0):C.UVGC_465_62})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_477_82,(0,0,2):C.UVGC_477_83,(0,0,1):C.UVGC_477_84,(0,1,0):C.UVGC_480_87,(0,1,2):C.UVGC_480_88,(0,1,1):C.UVGC_480_89})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_495_114,(0,0,2):C.UVGC_495_115,(0,0,1):C.UVGC_495_116,(0,1,0):C.UVGC_492_109,(0,1,2):C.UVGC_492_110,(0,1,1):C.UVGC_492_111})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_518_193})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_452_43})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_493_112})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.HL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_519_194})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.HL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_453_44})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.HL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_494_113})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.HH ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_522_201})

V_107 = CTVertex(name = 'V_107',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.HH ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_454_45})

V_108 = CTVertex(name = 'V_108',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.HH ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_496_117})

V_109 = CTVertex(name = 'V_109',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_427_19,(0,1,0):C.UVGC_509_176})

V_110 = CTVertex(name = 'V_110',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_427_19,(0,1,0):C.UVGC_447_38})

V_111 = CTVertex(name = 'V_111',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_427_19,(0,1,0):C.UVGC_486_101})

V_112 = CTVertex(name = 'V_112',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_425_17,(0,1,0):C.UVGC_456_47})

V_113 = CTVertex(name = 'V_113',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_425_17,(0,1,0):C.UVGC_471_74})

V_114 = CTVertex(name = 'V_114',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_425_17,(0,1,0):C.UVGC_438_21})

V_115 = CTVertex(name = 'V_115',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_426_18,(0,1,0):C.UVGC_439_22,(0,1,1):C.UVGC_439_23,(0,1,2):C.UVGC_439_24,(0,1,3):C.UVGC_439_25,(0,1,4):C.UVGC_439_26,(0,1,6):C.UVGC_439_27,(0,1,7):C.UVGC_439_28,(0,1,8):C.UVGC_439_29,(0,1,5):C.UVGC_510_177})

V_116 = CTVertex(name = 'V_116',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,2):C.UVGC_426_18,(0,1,0):C.UVGC_439_22,(0,1,1):C.UVGC_439_23,(0,1,3):C.UVGC_439_24,(0,1,4):C.UVGC_439_25,(0,1,5):C.UVGC_439_26,(0,1,6):C.UVGC_439_27,(0,1,7):C.UVGC_439_28,(0,1,8):C.UVGC_439_29,(0,1,2):C.UVGC_448_39})

V_117 = CTVertex(name = 'V_117',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_426_18,(0,1,0):C.UVGC_439_22,(0,1,1):C.UVGC_439_23,(0,1,2):C.UVGC_439_24,(0,1,3):C.UVGC_439_25,(0,1,4):C.UVGC_439_26,(0,1,6):C.UVGC_439_27,(0,1,7):C.UVGC_439_28,(0,1,8):C.UVGC_439_29,(0,1,5):C.UVGC_487_102})

V_118 = CTVertex(name = 'V_118',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,3):C.UVGC_426_18,(0,1,0):C.UVGC_439_22,(0,1,1):C.UVGC_439_23,(0,1,2):C.UVGC_439_24,(0,1,4):C.UVGC_439_25,(0,1,5):C.UVGC_439_26,(0,1,6):C.UVGC_439_27,(0,1,7):C.UVGC_439_28,(0,1,8):C.UVGC_439_29,(0,1,3):C.UVGC_457_48})

V_119 = CTVertex(name = 'V_119',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_426_18,(0,1,0):C.UVGC_439_22,(0,1,1):C.UVGC_439_23,(0,1,2):C.UVGC_439_24,(0,1,3):C.UVGC_439_25,(0,1,4):C.UVGC_439_26,(0,1,6):C.UVGC_439_27,(0,1,7):C.UVGC_439_28,(0,1,8):C.UVGC_439_29,(0,1,5):C.UVGC_472_75})

V_120 = CTVertex(name = 'V_120',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,1):C.UVGC_426_18,(0,1,0):C.UVGC_439_22,(0,1,2):C.UVGC_439_23,(0,1,3):C.UVGC_439_24,(0,1,4):C.UVGC_439_25,(0,1,5):C.UVGC_439_26,(0,1,6):C.UVGC_439_27,(0,1,7):C.UVGC_439_28,(0,1,8):C.UVGC_439_29,(0,1,1):C.UVGC_439_30})

V_121 = CTVertex(name = 'V_121',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_512_179,(0,0,2):C.UVGC_512_180,(0,0,1):C.UVGC_512_181})

V_122 = CTVertex(name = 'V_122',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_513_182,(0,0,2):C.UVGC_513_183,(0,0,1):C.UVGC_513_184})

V_123 = CTVertex(name = 'V_123',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_459_50,(0,0,2):C.UVGC_459_51,(0,0,0):C.UVGC_459_52})

V_124 = CTVertex(name = 'V_124',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_474_77,(0,0,2):C.UVGC_474_78,(0,0,1):C.UVGC_474_79})

V_125 = CTVertex(name = 'V_125',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_489_104,(0,0,2):C.UVGC_489_105,(0,0,1):C.UVGC_489_106})

V_126 = CTVertex(name = 'V_126',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_523_202,(0,0,2):C.UVGC_523_203,(0,0,1):C.UVGC_523_204})

V_127 = CTVertex(name = 'V_127',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_467_64,(0,0,2):C.UVGC_467_65,(0,0,0):C.UVGC_467_66})

V_128 = CTVertex(name = 'V_128',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_526_211,(0,0,2):C.UVGC_526_212,(0,0,1):C.UVGC_526_213})

V_129 = CTVertex(name = 'V_129',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_482_91,(0,0,2):C.UVGC_482_92,(0,0,1):C.UVGC_482_93})

V_130 = CTVertex(name = 'V_130',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_497_118,(0,0,2):C.UVGC_497_119,(0,0,1):C.UVGC_497_120})

V_131 = CTVertex(name = 'V_131',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV6 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_514_185,(0,1,0):C.UVGC_515_186})

V_132 = CTVertex(name = 'V_132',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV6 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_450_41,(0,1,0):C.UVGC_451_42})

V_133 = CTVertex(name = 'V_133',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV6 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_490_107,(0,1,0):C.UVGC_491_108})

V_134 = CTVertex(name = 'V_134',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_460_53,(0,1,0):C.UVGC_461_54})

V_135 = CTVertex(name = 'V_135',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_475_80,(0,1,0):C.UVGC_476_81})

V_136 = CTVertex(name = 'V_136',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_441_32,(0,1,0):C.UVGC_442_33})

V_137 = CTVertex(name = 'V_137',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_511_178,(0,1,0):C.UVGC_508_175})

V_138 = CTVertex(name = 'V_138',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_449_40,(0,1,0):C.UVGC_446_37})

V_139 = CTVertex(name = 'V_139',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_488_103,(0,1,0):C.UVGC_485_100})

V_140 = CTVertex(name = 'V_140',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_458_49,(0,1,0):C.UVGC_455_46})

V_141 = CTVertex(name = 'V_141',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_473_76,(0,1,0):C.UVGC_470_73})

V_142 = CTVertex(name = 'V_142',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_440_31,(0,1,0):C.UVGC_437_20})

V_143 = CTVertex(name = 'V_143',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,1,0):C.UVGC_500_127,(0,1,1):C.UVGC_500_128,(0,1,2):C.UVGC_500_129,(0,1,5):C.UVGC_500_130,(0,1,6):C.UVGC_500_131,(0,1,7):C.UVGC_500_132,(0,0,3):C.UVGC_417_3,(0,0,4):C.UVGC_417_4})

