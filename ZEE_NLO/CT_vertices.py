# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.0.0 for Linux x86 (64-bit) (April 7, 2019)
# Date: Sun 10 Nov 2019 01:09:22


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
               couplings = {(0,0,0):C.R2GC_470_127,(0,0,1):C.R2GC_470_128})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV9 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_388_69,(2,0,1):C.R2GC_388_70,(0,0,0):C.R2GC_388_69,(0,0,1):C.R2GC_388_70,(6,0,0):C.R2GC_391_74,(6,0,1):C.R2GC_476_135,(4,0,0):C.R2GC_386_65,(4,0,1):C.R2GC_386_66,(3,0,0):C.R2GC_386_65,(3,0,1):C.R2GC_386_66,(8,0,0):C.R2GC_387_67,(8,0,1):C.R2GC_387_68,(7,0,0):C.R2GC_392_76,(7,0,1):C.R2GC_475_134,(5,0,0):C.R2GC_386_65,(5,0,1):C.R2GC_386_66,(1,0,0):C.R2GC_386_65,(1,0,1):C.R2GC_386_66,(11,3,0):C.R2GC_390_72,(11,3,1):C.R2GC_390_73,(10,3,0):C.R2GC_390_72,(10,3,1):C.R2GC_390_73,(9,3,1):C.R2GC_389_71,(2,1,0):C.R2GC_388_69,(2,1,1):C.R2GC_388_70,(0,1,0):C.R2GC_388_69,(0,1,1):C.R2GC_388_70,(4,1,0):C.R2GC_386_65,(4,1,1):C.R2GC_386_66,(3,1,0):C.R2GC_386_65,(3,1,1):C.R2GC_386_66,(8,1,0):C.R2GC_387_67,(8,1,1):C.R2GC_474_133,(6,1,0):C.R2GC_472_130,(6,1,1):C.R2GC_472_131,(7,1,0):C.R2GC_392_76,(7,1,1):C.R2GC_392_77,(5,1,0):C.R2GC_386_65,(5,1,1):C.R2GC_386_66,(1,1,0):C.R2GC_386_65,(1,1,1):C.R2GC_386_66,(2,2,0):C.R2GC_388_69,(2,2,1):C.R2GC_388_70,(0,2,0):C.R2GC_388_69,(0,2,1):C.R2GC_388_70,(4,2,0):C.R2GC_386_65,(4,2,1):C.R2GC_386_66,(3,2,0):C.R2GC_386_65,(3,2,1):C.R2GC_386_66,(8,2,0):C.R2GC_387_67,(8,2,1):C.R2GC_471_129,(6,2,0):C.R2GC_391_74,(6,2,1):C.R2GC_391_75,(7,2,0):C.R2GC_473_132,(7,2,1):C.R2GC_388_70,(5,2,0):C.R2GC_386_65,(5,2,1):C.R2GC_386_66,(1,2,0):C.R2GC_386_65,(1,2,1):C.R2GC_386_66})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.u__tilde__, P.d, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.d, P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_493_147,(0,1,0):C.R2GC_494_148})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.c__tilde__, P.d, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.c, P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_437_103,(0,1,0):C.R2GC_436_102})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.u__tilde__, P.s, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.g, P.s, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_496_150,(0,1,0):C.R2GC_497_151})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.c__tilde__, P.s, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.c, P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_452_113,(0,1,0):C.R2GC_451_112})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_466_122,(0,1,0):C.R2GC_467_123})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_431_97})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.s__tilde__, P.s, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_446_107})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_411_85})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_432_98})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_447_108})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_412_86})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_434_100})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_449_110})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_413_87})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_489_143,(0,1,0):C.R2GC_485_139})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_490_144,(0,1,0):C.R2GC_486_140})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_430_96,(0,1,0):C.R2GC_433_99})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_445_106,(0,1,0):C.R2GC_448_109})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_463_119,(0,1,0):C.R2GC_460_116})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_487_141})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_420_91})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_461_117})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_488_142})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_421_92})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_462_118})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_491_145})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_422_93})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_464_120})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_395_80})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_395_80})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_395_80})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_393_78})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_393_78})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_393_78})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_394_79})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_394_79})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_394_79})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_394_79})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_394_79})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_394_79})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_481_137})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_482_138})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_427_95})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_442_105})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_457_115})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_492_146})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_435_101})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_495_149})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_450_111})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_465_121})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_418_89,(0,1,0):C.R2GC_419_90})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_418_89,(0,1,0):C.R2GC_419_90})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_418_89,(0,1,0):C.R2GC_419_90})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_409_83,(0,1,0):C.R2GC_410_84})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_409_83,(0,1,0):C.R2GC_410_84})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_409_83,(0,1,0):C.R2GC_410_84})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_480_136,(0,2,0):C.R2GC_480_136,(0,1,0):C.R2GC_405_81,(0,3,0):C.R2GC_405_81})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_417_88,(0,2,0):C.R2GC_417_88,(0,1,0):C.R2GC_405_81,(0,3,0):C.R2GC_405_81})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_456_114,(0,2,0):C.R2GC_456_114,(0,1,0):C.R2GC_405_81,(0,3,0):C.R2GC_405_81})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_426_94,(0,2,0):C.R2GC_426_94,(0,1,0):C.R2GC_405_81,(0,3,0):C.R2GC_405_81})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_441_104,(0,2,0):C.R2GC_441_104,(0,1,0):C.R2GC_405_81,(0,3,0):C.R2GC_405_81})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_408_82,(0,2,0):C.R2GC_408_82,(0,1,0):C.R2GC_405_81,(0,3,0):C.R2GC_405_81})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,4):C.R2GC_469_126,(0,1,0):C.R2GC_371_5,(0,1,2):C.R2GC_371_6,(0,1,3):C.R2GC_371_7,(0,1,5):C.R2GC_371_8,(0,1,6):C.R2GC_371_9,(0,1,7):C.R2GC_371_10,(0,2,1):C.R2GC_468_124,(0,2,4):C.R2GC_468_125})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.g, P.g, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_376_19,(0,0,1):C.R2GC_376_20,(0,0,2):C.R2GC_376_21,(0,0,3):C.R2GC_376_22,(0,0,4):C.R2GC_376_23,(0,0,5):C.R2GC_376_24})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.g, P.g, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_377_25,(0,0,1):C.R2GC_377_26,(0,0,2):C.R2GC_377_27,(0,0,3):C.R2GC_377_28,(0,0,4):C.R2GC_377_29,(0,0,5):C.R2GC_377_30})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_372_11,(0,0,1):C.R2GC_372_12,(0,1,0):C.R2GC_372_11,(0,1,1):C.R2GC_372_12,(0,2,0):C.R2GC_372_11,(0,2,1):C.R2GC_372_12})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_375_17,(0,0,1):C.R2GC_375_18,(0,1,0):C.R2GC_375_17,(0,1,1):C.R2GC_375_18,(0,2,0):C.R2GC_375_17,(0,2,1):C.R2GC_375_18})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_382_55,(0,0,1):C.R2GC_382_56,(0,0,2):C.R2GC_382_57,(0,0,3):C.R2GC_382_58,(0,0,4):C.R2GC_382_59,(0,1,0):C.R2GC_382_55,(0,1,1):C.R2GC_382_56,(0,1,2):C.R2GC_382_57,(0,1,3):C.R2GC_382_58,(0,1,4):C.R2GC_382_59,(0,2,0):C.R2GC_382_55,(0,2,1):C.R2GC_382_56,(0,2,2):C.R2GC_382_57,(0,2,3):C.R2GC_382_58,(0,2,4):C.R2GC_382_59})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_369_1,(0,0,1):C.R2GC_369_2,(0,1,0):C.R2GC_369_1,(0,1,1):C.R2GC_369_2,(0,2,0):C.R2GC_369_1,(0,2,1):C.R2GC_369_2})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_374_15,(1,0,1):C.R2GC_374_16,(0,1,0):C.R2GC_373_13,(0,1,1):C.R2GC_373_14,(0,2,0):C.R2GC_373_13,(0,2,1):C.R2GC_373_14,(0,3,0):C.R2GC_373_13,(0,3,1):C.R2GC_373_14})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_370_3,(0,0,1):C.R2GC_370_4,(0,1,0):C.R2GC_370_3,(0,1,1):C.R2GC_370_4,(0,2,0):C.R2GC_370_3,(0,2,1):C.R2GC_370_4})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.g, P.g, P.HL, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_379_37,(0,0,1):C.R2GC_379_38,(0,0,2):C.R2GC_379_39,(0,0,3):C.R2GC_379_40,(0,0,4):C.R2GC_379_41,(0,0,5):C.R2GC_379_42})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.g, P.g, P.HH, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_380_43,(0,0,1):C.R2GC_380_44,(0,0,2):C.R2GC_380_45,(0,0,3):C.R2GC_380_46,(0,0,4):C.R2GC_380_47,(0,0,5):C.R2GC_380_48})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.g, P.g, P.HH, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_381_49,(0,0,1):C.R2GC_381_50,(0,0,2):C.R2GC_381_51,(0,0,3):C.R2GC_381_52,(0,0,4):C.R2GC_381_53,(0,0,5):C.R2GC_381_54})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_378_31,(0,0,1):C.R2GC_378_32,(0,0,2):C.R2GC_378_33,(0,0,3):C.R2GC_378_34,(0,0,4):C.R2GC_378_35,(0,0,5):C.R2GC_378_36})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_383_60,(0,0,1):C.R2GC_383_61,(0,0,2):C.R2GC_383_62,(0,0,3):C.R2GC_383_63,(0,0,4):C.R2GC_383_64})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,1,0):C.UVGC_470_139,(0,1,1):C.UVGC_470_140,(0,1,2):C.UVGC_470_141,(0,1,5):C.UVGC_470_142,(0,1,6):C.UVGC_470_143,(0,1,7):C.UVGC_470_144,(0,2,3):C.UVGC_384_1,(0,0,4):C.UVGC_385_2})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV9 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(2,0,4):C.UVGC_387_6,(2,0,5):C.UVGC_387_5,(0,0,4):C.UVGC_387_6,(0,0,5):C.UVGC_387_5,(6,0,0):C.UVGC_475_171,(6,0,2):C.UVGC_475_172,(6,0,3):C.UVGC_475_173,(6,0,4):C.UVGC_476_179,(6,0,5):C.UVGC_476_180,(6,0,6):C.UVGC_475_176,(6,0,7):C.UVGC_475_177,(6,0,8):C.UVGC_475_178,(4,0,4):C.UVGC_386_3,(4,0,5):C.UVGC_386_4,(3,0,4):C.UVGC_386_3,(3,0,5):C.UVGC_386_4,(8,0,4):C.UVGC_387_5,(8,0,5):C.UVGC_387_6,(7,0,0):C.UVGC_475_171,(7,0,2):C.UVGC_475_172,(7,0,3):C.UVGC_475_173,(7,0,4):C.UVGC_475_174,(7,0,5):C.UVGC_475_175,(7,0,6):C.UVGC_475_176,(7,0,7):C.UVGC_475_177,(7,0,8):C.UVGC_475_178,(5,0,4):C.UVGC_386_3,(5,0,5):C.UVGC_386_4,(1,0,4):C.UVGC_386_3,(1,0,5):C.UVGC_386_4,(11,3,4):C.UVGC_390_9,(11,3,5):C.UVGC_390_10,(10,3,4):C.UVGC_390_9,(10,3,5):C.UVGC_390_10,(9,3,4):C.UVGC_389_7,(9,3,5):C.UVGC_389_8,(2,1,4):C.UVGC_387_6,(2,1,5):C.UVGC_387_5,(0,1,4):C.UVGC_387_6,(0,1,5):C.UVGC_387_5,(4,1,4):C.UVGC_386_3,(4,1,5):C.UVGC_386_4,(3,1,4):C.UVGC_386_3,(3,1,5):C.UVGC_386_4,(8,1,0):C.UVGC_474_163,(8,1,2):C.UVGC_474_164,(8,1,3):C.UVGC_474_165,(8,1,4):C.UVGC_474_166,(8,1,5):C.UVGC_474_167,(8,1,6):C.UVGC_474_168,(8,1,7):C.UVGC_474_169,(8,1,8):C.UVGC_474_170,(6,1,0):C.UVGC_472_153,(6,1,2):C.UVGC_472_154,(6,1,3):C.UVGC_472_155,(6,1,4):C.UVGC_472_156,(6,1,5):C.UVGC_472_157,(6,1,6):C.UVGC_472_158,(6,1,7):C.UVGC_472_159,(6,1,8):C.UVGC_472_160,(7,1,1):C.UVGC_391_11,(7,1,4):C.UVGC_392_13,(7,1,5):C.UVGC_392_14,(5,1,4):C.UVGC_386_3,(5,1,5):C.UVGC_386_4,(1,1,4):C.UVGC_386_3,(1,1,5):C.UVGC_386_4,(2,2,4):C.UVGC_387_6,(2,2,5):C.UVGC_387_5,(0,2,4):C.UVGC_387_6,(0,2,5):C.UVGC_387_5,(4,2,4):C.UVGC_386_3,(4,2,5):C.UVGC_386_4,(3,2,4):C.UVGC_386_3,(3,2,5):C.UVGC_386_4,(8,2,0):C.UVGC_471_145,(8,2,2):C.UVGC_471_146,(8,2,3):C.UVGC_471_147,(8,2,4):C.UVGC_471_148,(8,2,5):C.UVGC_471_149,(8,2,6):C.UVGC_471_150,(8,2,7):C.UVGC_471_151,(8,2,8):C.UVGC_471_152,(6,2,1):C.UVGC_391_11,(6,2,4):C.UVGC_391_12,(6,2,5):C.UVGC_389_7,(7,2,0):C.UVGC_472_153,(7,2,2):C.UVGC_472_154,(7,2,3):C.UVGC_472_155,(7,2,4):C.UVGC_473_161,(7,2,5):C.UVGC_473_162,(7,2,6):C.UVGC_472_158,(7,2,7):C.UVGC_472_159,(7,2,8):C.UVGC_472_160,(5,2,4):C.UVGC_386_3,(5,2,5):C.UVGC_386_4,(1,2,4):C.UVGC_386_3,(1,2,5):C.UVGC_386_4})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_493_211,(0,0,2):C.UVGC_493_212,(0,0,1):C.UVGC_493_213,(0,1,0):C.UVGC_494_214,(0,1,2):C.UVGC_494_215,(0,1,1):C.UVGC_494_216})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.c__tilde__, P.d, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_437_68,(0,0,2):C.UVGC_437_69,(0,0,0):C.UVGC_437_70,(0,1,1):C.UVGC_436_65,(0,1,2):C.UVGC_436_66,(0,1,0):C.UVGC_436_67})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.u__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_496_220,(0,0,2):C.UVGC_496_221,(0,0,1):C.UVGC_496_222,(0,1,0):C.UVGC_497_223,(0,1,2):C.UVGC_497_224,(0,1,1):C.UVGC_497_225})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_452_95,(0,0,2):C.UVGC_452_96,(0,0,1):C.UVGC_452_97,(0,1,0):C.UVGC_451_92,(0,1,2):C.UVGC_451_93,(0,1,1):C.UVGC_451_94})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_466_119,(0,0,2):C.UVGC_466_120,(0,0,1):C.UVGC_466_121,(0,1,0):C.UVGC_467_122,(0,1,2):C.UVGC_467_123,(0,1,1):C.UVGC_467_124})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_431_56})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_446_83})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_411_32})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_432_57})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_447_84})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_412_33})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_434_61})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_449_88})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_413_34})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_489_201,(0,0,2):C.UVGC_489_202,(0,0,1):C.UVGC_489_203,(0,1,0):C.UVGC_485_193,(0,1,2):C.UVGC_485_194,(0,1,1):C.UVGC_485_195})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.s__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_490_204,(0,0,2):C.UVGC_490_205,(0,0,1):C.UVGC_490_206,(0,1,0):C.UVGC_486_196,(0,1,2):C.UVGC_486_197,(0,1,1):C.UVGC_486_198})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.d__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_430_53,(0,0,2):C.UVGC_430_54,(0,0,0):C.UVGC_430_55,(0,1,1):C.UVGC_433_58,(0,1,2):C.UVGC_433_59,(0,1,0):C.UVGC_433_60})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_445_80,(0,0,2):C.UVGC_445_81,(0,0,1):C.UVGC_445_82,(0,1,0):C.UVGC_448_85,(0,1,2):C.UVGC_448_86,(0,1,1):C.UVGC_448_87})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_463_112,(0,0,2):C.UVGC_463_113,(0,0,1):C.UVGC_463_114,(0,1,0):C.UVGC_460_107,(0,1,2):C.UVGC_460_108,(0,1,1):C.UVGC_460_109})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_487_199})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_420_41})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_461_110})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.HL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_488_200})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.HL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_421_42})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.HL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_462_111})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.HH ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_491_207})

V_107 = CTVertex(name = 'V_107',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.HH ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_422_43})

V_108 = CTVertex(name = 'V_108',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.HH ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_464_115})

V_109 = CTVertex(name = 'V_109',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_395_17,(0,1,0):C.UVGC_478_182,(0,2,0):C.UVGC_478_182})

V_110 = CTVertex(name = 'V_110',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_395_17,(0,1,0):C.UVGC_415_36,(0,2,0):C.UVGC_415_36})

V_111 = CTVertex(name = 'V_111',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_395_17,(0,1,0):C.UVGC_454_99,(0,2,0):C.UVGC_454_99})

V_112 = CTVertex(name = 'V_112',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_393_15,(0,1,0):C.UVGC_424_45,(0,2,0):C.UVGC_424_45})

V_113 = CTVertex(name = 'V_113',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_393_15,(0,1,0):C.UVGC_439_72,(0,2,0):C.UVGC_439_72})

V_114 = CTVertex(name = 'V_114',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_393_15,(0,1,0):C.UVGC_406_19,(0,2,0):C.UVGC_406_19})

V_115 = CTVertex(name = 'V_115',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_394_16,(0,1,0):C.UVGC_407_20,(0,1,1):C.UVGC_407_21,(0,1,2):C.UVGC_407_22,(0,1,3):C.UVGC_407_23,(0,1,4):C.UVGC_407_24,(0,1,6):C.UVGC_407_25,(0,1,7):C.UVGC_407_26,(0,1,8):C.UVGC_407_27,(0,1,5):C.UVGC_479_183,(0,2,0):C.UVGC_407_20,(0,2,1):C.UVGC_407_21,(0,2,2):C.UVGC_407_22,(0,2,3):C.UVGC_407_23,(0,2,4):C.UVGC_407_24,(0,2,6):C.UVGC_407_25,(0,2,7):C.UVGC_407_26,(0,2,8):C.UVGC_407_27,(0,2,5):C.UVGC_479_183})

V_116 = CTVertex(name = 'V_116',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,2):C.UVGC_394_16,(0,1,0):C.UVGC_407_20,(0,1,1):C.UVGC_407_21,(0,1,3):C.UVGC_407_22,(0,1,4):C.UVGC_407_23,(0,1,5):C.UVGC_407_24,(0,1,6):C.UVGC_407_25,(0,1,7):C.UVGC_407_26,(0,1,8):C.UVGC_407_27,(0,1,2):C.UVGC_416_37,(0,2,0):C.UVGC_407_20,(0,2,1):C.UVGC_407_21,(0,2,3):C.UVGC_407_22,(0,2,4):C.UVGC_407_23,(0,2,5):C.UVGC_407_24,(0,2,6):C.UVGC_407_25,(0,2,7):C.UVGC_407_26,(0,2,8):C.UVGC_407_27,(0,2,2):C.UVGC_416_37})

V_117 = CTVertex(name = 'V_117',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_394_16,(0,1,0):C.UVGC_407_20,(0,1,1):C.UVGC_407_21,(0,1,2):C.UVGC_407_22,(0,1,3):C.UVGC_407_23,(0,1,4):C.UVGC_407_24,(0,1,6):C.UVGC_407_25,(0,1,7):C.UVGC_407_26,(0,1,8):C.UVGC_407_27,(0,1,5):C.UVGC_455_100,(0,2,0):C.UVGC_407_20,(0,2,1):C.UVGC_407_21,(0,2,2):C.UVGC_407_22,(0,2,3):C.UVGC_407_23,(0,2,4):C.UVGC_407_24,(0,2,6):C.UVGC_407_25,(0,2,7):C.UVGC_407_26,(0,2,8):C.UVGC_407_27,(0,2,5):C.UVGC_455_100})

V_118 = CTVertex(name = 'V_118',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,3):C.UVGC_394_16,(0,1,0):C.UVGC_407_20,(0,1,1):C.UVGC_407_21,(0,1,2):C.UVGC_407_22,(0,1,4):C.UVGC_407_23,(0,1,5):C.UVGC_407_24,(0,1,6):C.UVGC_407_25,(0,1,7):C.UVGC_407_26,(0,1,8):C.UVGC_407_27,(0,1,3):C.UVGC_425_46,(0,2,0):C.UVGC_407_20,(0,2,1):C.UVGC_407_21,(0,2,2):C.UVGC_407_22,(0,2,4):C.UVGC_407_23,(0,2,5):C.UVGC_407_24,(0,2,6):C.UVGC_407_25,(0,2,7):C.UVGC_407_26,(0,2,8):C.UVGC_407_27,(0,2,3):C.UVGC_425_46})

V_119 = CTVertex(name = 'V_119',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_394_16,(0,1,0):C.UVGC_407_20,(0,1,1):C.UVGC_407_21,(0,1,2):C.UVGC_407_22,(0,1,3):C.UVGC_407_23,(0,1,4):C.UVGC_407_24,(0,1,6):C.UVGC_407_25,(0,1,7):C.UVGC_407_26,(0,1,8):C.UVGC_407_27,(0,1,5):C.UVGC_440_73,(0,2,0):C.UVGC_407_20,(0,2,1):C.UVGC_407_21,(0,2,2):C.UVGC_407_22,(0,2,3):C.UVGC_407_23,(0,2,4):C.UVGC_407_24,(0,2,6):C.UVGC_407_25,(0,2,7):C.UVGC_407_26,(0,2,8):C.UVGC_407_27,(0,2,5):C.UVGC_440_73})

V_120 = CTVertex(name = 'V_120',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,1):C.UVGC_394_16,(0,1,0):C.UVGC_407_20,(0,1,2):C.UVGC_407_21,(0,1,3):C.UVGC_407_22,(0,1,4):C.UVGC_407_23,(0,1,5):C.UVGC_407_24,(0,1,6):C.UVGC_407_25,(0,1,7):C.UVGC_407_26,(0,1,8):C.UVGC_407_27,(0,1,1):C.UVGC_407_28,(0,2,0):C.UVGC_407_20,(0,2,2):C.UVGC_407_21,(0,2,3):C.UVGC_407_22,(0,2,4):C.UVGC_407_23,(0,2,5):C.UVGC_407_24,(0,2,6):C.UVGC_407_25,(0,2,7):C.UVGC_407_26,(0,2,8):C.UVGC_407_27,(0,2,1):C.UVGC_407_28})

V_121 = CTVertex(name = 'V_121',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_481_185,(0,0,2):C.UVGC_481_186,(0,0,1):C.UVGC_481_187})

V_122 = CTVertex(name = 'V_122',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_482_188,(0,0,2):C.UVGC_482_189,(0,0,1):C.UVGC_482_190})

V_123 = CTVertex(name = 'V_123',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_427_48,(0,0,2):C.UVGC_427_49,(0,0,0):C.UVGC_427_50})

V_124 = CTVertex(name = 'V_124',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_442_75,(0,0,2):C.UVGC_442_76,(0,0,1):C.UVGC_442_77})

V_125 = CTVertex(name = 'V_125',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_457_102,(0,0,2):C.UVGC_457_103,(0,0,1):C.UVGC_457_104})

V_126 = CTVertex(name = 'V_126',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_492_208,(0,0,2):C.UVGC_492_209,(0,0,1):C.UVGC_492_210})

V_127 = CTVertex(name = 'V_127',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_435_62,(0,0,2):C.UVGC_435_63,(0,0,0):C.UVGC_435_64})

V_128 = CTVertex(name = 'V_128',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_495_217,(0,0,2):C.UVGC_495_218,(0,0,1):C.UVGC_495_219})

V_129 = CTVertex(name = 'V_129',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_450_89,(0,0,2):C.UVGC_450_90,(0,0,1):C.UVGC_450_91})

V_130 = CTVertex(name = 'V_130',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_465_116,(0,0,2):C.UVGC_465_117,(0,0,1):C.UVGC_465_118})

V_131 = CTVertex(name = 'V_131',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_483_191,(0,1,0):C.UVGC_484_192})

V_132 = CTVertex(name = 'V_132',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_418_39,(0,1,0):C.UVGC_419_40})

V_133 = CTVertex(name = 'V_133',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_458_105,(0,1,0):C.UVGC_459_106})

V_134 = CTVertex(name = 'V_134',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_428_51,(0,1,0):C.UVGC_429_52})

V_135 = CTVertex(name = 'V_135',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_443_78,(0,1,0):C.UVGC_444_79})

V_136 = CTVertex(name = 'V_136',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_409_30,(0,1,0):C.UVGC_410_31})

V_137 = CTVertex(name = 'V_137',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_480_184,(0,2,0):C.UVGC_480_184,(0,1,0):C.UVGC_477_181,(0,3,0):C.UVGC_477_181})

V_138 = CTVertex(name = 'V_138',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_417_38,(0,2,0):C.UVGC_417_38,(0,1,0):C.UVGC_414_35,(0,3,0):C.UVGC_414_35})

V_139 = CTVertex(name = 'V_139',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_456_101,(0,2,0):C.UVGC_456_101,(0,1,0):C.UVGC_453_98,(0,3,0):C.UVGC_453_98})

V_140 = CTVertex(name = 'V_140',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_426_47,(0,2,0):C.UVGC_426_47,(0,1,0):C.UVGC_423_44,(0,3,0):C.UVGC_423_44})

V_141 = CTVertex(name = 'V_141',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_441_74,(0,2,0):C.UVGC_441_74,(0,1,0):C.UVGC_438_71,(0,3,0):C.UVGC_438_71})

V_142 = CTVertex(name = 'V_142',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_408_29,(0,2,0):C.UVGC_408_29,(0,1,0):C.UVGC_405_18,(0,3,0):C.UVGC_405_18})

V_143 = CTVertex(name = 'V_143',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_469_131,(0,0,1):C.UVGC_469_132,(0,0,2):C.UVGC_469_133,(0,0,3):C.UVGC_469_134,(0,0,4):C.UVGC_469_135,(0,0,5):C.UVGC_469_136,(0,0,6):C.UVGC_469_137,(0,0,7):C.UVGC_469_138,(0,1,0):C.UVGC_468_125,(0,1,1):C.UVGC_468_126,(0,1,2):C.UVGC_468_127,(0,1,5):C.UVGC_468_128,(0,1,6):C.UVGC_468_129,(0,1,7):C.UVGC_468_130})

