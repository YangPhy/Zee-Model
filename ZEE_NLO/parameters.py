# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.0.0 for Linux x86 (64-bit) (April 7, 2019)
# Date: Sun 10 Nov 2019 01:09:20



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# This is a default parameter object representing the renormalization scale (MU_R).
MU_R = Parameter(name = 'MU_R',
                 nature = 'external',
                 type = 'real',
                 value = 91.188,
                 texname = '\\text{\\mu_r}',
                 lhablock = 'LOOP',
                 lhacode = [1])

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

beta = Parameter(name = 'beta',
                 nature = 'external',
                 type = 'real',
                 value = 0.7854,
                 texname = '\\beta',
                 lhablock = 'ZEEINPUTS',
                 lhacode = [ 1 ])

alpha = Parameter(name = 'alpha',
                  nature = 'external',
                  type = 'real',
                  value = 0.7854,
                  texname = '\\alpha',
                  lhablock = 'ZEEINPUTS',
                  lhacode = [ 2 ])

alphabeta = Parameter(name = 'alphabeta',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\alpha -\\beta',
                      lhablock = 'ZEEINPUTS',
                      lhacode = [ 3 ])

phi = Parameter(name = 'phi',
                nature = 'external',
                type = 'real',
                value = 0.2013579207903308,
                texname = '\\phi',
                lhablock = 'ZEEINPUTS',
                lhacode = [ 4 ])

lam2 = Parameter(name = 'lam2',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\lambda _2',
                 lhablock = 'ZEELAMS',
                 lhacode = [ 1 ])

lam3 = Parameter(name = 'lam3',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\lambda _3',
                 lhablock = 'ZEELAMS',
                 lhacode = [ 2 ])

lam7 = Parameter(name = 'lam7',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\lambda _7',
                 lhablock = 'ZEELAMS',
                 lhacode = [ 3 ])

lam8 = Parameter(name = 'lam8',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\lambda _8',
                 lhablock = 'ZEELAMS',
                 lhacode = [ 4 ])

lam9 = Parameter(name = 'lam9',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\lambda _9',
                 lhablock = 'ZEELAMS',
                 lhacode = [ 5 ])

lam10 = Parameter(name = 'lam10',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\lambda _{10}',
                  lhablock = 'ZEELAMS',
                  lhacode = [ 6 ])

lameta = Parameter(name = 'lameta',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\lambda _{\\eta }',
                   lhablock = 'ZEELAMS',
                   lhacode = [ 7 ])

fem = Parameter(name = 'fem',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = 'f_{e \\mu }',
                lhablock = 'ZEEYUKAWAF',
                lhacode = [ 1 ])

fet = Parameter(name = 'fet',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = 'f_{e \\tau }',
                lhablock = 'ZEEYUKAWAF',
                lhacode = [ 2 ])

fmt = Parameter(name = 'fmt',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = 'f_{\\mu  \\tau }',
                lhablock = 'ZEEYUKAWAF',
                lhacode = [ 3 ])

ylzee = Parameter(name = 'ylzee',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = 'Y_e',
                  lhablock = 'ZEEYUKAWAY',
                  lhacode = [ 1 ])

ylzem = Parameter(name = 'ylzem',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = 'Y_{e \\mu }',
                  lhablock = 'ZEEYUKAWAY',
                  lhacode = [ 2 ])

ylzet = Parameter(name = 'ylzet',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = 'Y_{e \\tau }',
                  lhablock = 'ZEEYUKAWAY',
                  lhacode = [ 3 ])

ylzme = Parameter(name = 'ylzme',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = 'Y_{e \\mu }',
                  lhablock = 'ZEEYUKAWAY',
                  lhacode = [ 4 ])

ylzmm = Parameter(name = 'ylzmm',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = 'Y_{\\mu ^2}',
                  lhablock = 'ZEEYUKAWAY',
                  lhacode = [ 5 ])

ylzmt = Parameter(name = 'ylzmt',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = 'Y_{\\mu  \\tau }',
                  lhablock = 'ZEEYUKAWAY',
                  lhacode = [ 6 ])

ylzte = Parameter(name = 'ylzte',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = 'Y_{e \\tau }',
                  lhablock = 'ZEEYUKAWAY',
                  lhacode = [ 7 ])

ylztm = Parameter(name = 'ylztm',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = 'Y_{\\mu  \\tau }',
                  lhablock = 'ZEEYUKAWAY',
                  lhacode = [ 8 ])

ylztt = Parameter(name = 'ylztt',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = 'Y_{\\tau ^2}',
                  lhablock = 'ZEEYUKAWAY',
                  lhacode = [ 9 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MHL = Parameter(name = 'MHL',
                nature = 'external',
                type = 'real',
                value = 125,
                texname = '\\text{MHL}',
                lhablock = 'MASS',
                lhacode = [ 25 ])

MHH = Parameter(name = 'MHH',
                nature = 'external',
                type = 'real',
                value = 400,
                texname = '\\text{MHH}',
                lhablock = 'MASS',
                lhacode = [ 225 ])

MHA = Parameter(name = 'MHA',
                nature = 'external',
                type = 'real',
                value = 500,
                texname = '\\text{MHA}',
                lhablock = 'MASS',
                lhacode = [ 226 ])

MHpH = Parameter(name = 'MHpH',
                 nature = 'external',
                 type = 'real',
                 value = 2000,
                 texname = '\\text{MHpH}',
                 lhablock = 'MASS',
                 lhacode = [ 227 ])

MHp = Parameter(name = 'MHp',
                nature = 'external',
                type = 'real',
                value = 120,
                texname = '\\text{MHp}',
                lhablock = 'MASS',
                lhacode = [ 228 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WHL = Parameter(name = 'WHL',
                nature = 'external',
                type = 'real',
                value = 0.00407,
                texname = '\\text{WHL}',
                lhablock = 'DECAY',
                lhacode = [ 25 ])

WHH = Parameter(name = 'WHH',
                nature = 'external',
                type = 'real',
                value = 0.0107,
                texname = '\\text{WHH}',
                lhablock = 'DECAY',
                lhacode = [ 225 ])

WHA = Parameter(name = 'WHA',
                nature = 'external',
                type = 'real',
                value = 0.0107,
                texname = '\\text{WHA}',
                lhablock = 'DECAY',
                lhacode = [ 226 ])

WHpH = Parameter(name = 'WHpH',
                 nature = 'external',
                 type = 'real',
                 value = 0.0107,
                 texname = '\\text{WHpH}',
                 lhablock = 'DECAY',
                 lhacode = [ 227 ])

WHp = Parameter(name = 'WHp',
                nature = 'external',
                type = 'real',
                value = 0.0107,
                texname = '\\text{WHp}',
                lhablock = 'DECAY',
                lhacode = [ 228 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

cb = Parameter(name = 'cb',
               nature = 'internal',
               type = 'real',
               value = 'cmath.cos(beta)',
               texname = 'c_{\\beta }')

sb = Parameter(name = 'sb',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sin(beta)',
               texname = 's_{\\beta }')

ca = Parameter(name = 'ca',
               nature = 'internal',
               type = 'real',
               value = 'cmath.cos(alpha)',
               texname = 'c_{\\alpha }')

sa = Parameter(name = 'sa',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sin(alpha)',
               texname = 's_{\\alpha }')

cab = Parameter(name = 'cab',
                nature = 'internal',
                type = 'real',
                value = 'cmath.cos(alphabeta)',
                texname = 'c_{\\alpha -\\beta }')

sab = Parameter(name = 'sab',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sin(alphabeta)',
                texname = 's_{\\alpha -\\beta }')

cphi = Parameter(name = 'cphi',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.cos(phi)',
                 texname = 'c_{\\phi }')

sphi = Parameter(name = 'sphi',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sin(phi)',
                 texname = 's_{\\phi }')

yzee = Parameter(name = 'yzee',
                 nature = 'internal',
                 type = 'real',
                 value = 'ylzee',
                 texname = '\\text{yzee}')

yzem = Parameter(name = 'yzem',
                 nature = 'internal',
                 type = 'real',
                 value = 'ylzem',
                 texname = '\\text{yzem}')

yzet = Parameter(name = 'yzet',
                 nature = 'internal',
                 type = 'real',
                 value = 'ylzet',
                 texname = '\\text{yzet}')

yzme = Parameter(name = 'yzme',
                 nature = 'internal',
                 type = 'real',
                 value = 'ylzme',
                 texname = '\\text{yzme}')

yzmm = Parameter(name = 'yzmm',
                 nature = 'internal',
                 type = 'real',
                 value = 'ylzmm',
                 texname = '\\text{yzmm}')

yzmt = Parameter(name = 'yzmt',
                 nature = 'internal',
                 type = 'real',
                 value = 'ylzmt',
                 texname = '\\text{yzmt}')

yzte = Parameter(name = 'yzte',
                 nature = 'internal',
                 type = 'real',
                 value = 'ylzte',
                 texname = '\\text{yzte}')

yztm = Parameter(name = 'yztm',
                 nature = 'internal',
                 type = 'real',
                 value = 'ylztm',
                 texname = '\\text{yztm}')

yztt = Parameter(name = 'yztt',
                 nature = 'internal',
                 type = 'real',
                 value = 'ylztt',
                 texname = '\\text{yztt}')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

mu12 = Parameter(name = 'mu12',
                 nature = 'internal',
                 type = 'real',
                 value = '(MHL**2*(1 + cab**2 - sab**2) + MHH**2*(1 - cab**2 + sab**2))/4.',
                 texname = '\\text{mu12}')

mu32 = Parameter(name = 'mu32',
                 nature = 'internal',
                 type = 'real',
                 value = '(cab*(-MHH**2 + MHL**2)*sab)/2.',
                 texname = '\\text{mu32}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

mu22 = Parameter(name = 'mu22',
                 nature = 'internal',
                 type = 'real',
                 value = '(MHpH**2*(1 + cphi**2 - sphi**2) + MHp**2*(1 - cphi**2 + sphi**2) - lam3*vev**2)/2.',
                 texname = '\\text{mu22}')

mueta2 = Parameter(name = 'mueta2',
                   nature = 'internal',
                   type = 'real',
                   value = '(MHp**2*(1 + cphi**2 - sphi**2) + MHpH**2*(1 - cphi**2 + sphi**2) - lam8*vev**2)/2.',
                   texname = '\\text{mueta2}')

GHL = Parameter(name = 'GHL',
                nature = 'internal',
                type = 'real',
                value = '-(G**2*(1 + (13*MHL**6)/(16800.*MT**6) + MHL**4/(168.*MT**4) + (7*MHL**2)/(120.*MT**2)))/(12.*cmath.pi**2*vev)',
                texname = 'G_{\\text{HL}}')

lam1 = Parameter(name = 'lam1',
                 nature = 'internal',
                 type = 'real',
                 value = '(MHL**2*(1 + cab**2 - sab**2) + MHH**2*(1 - cab**2 + sab**2))/(2.*vev**2)',
                 texname = '\\text{lam1}')

lam4 = Parameter(name = 'lam4',
                 nature = 'internal',
                 type = 'real',
                 value = '(2*MHA**2 + MHH**2*(1 + cab**2 - sab**2) + MHL**2*(1 - cab**2 + sab**2) + 2*MHp**2*(-1 + cphi**2 - sphi**2) - 2*MHpH**2*(1 + cphi**2 - sphi**2))/(2.*vev**2)',
                 texname = '\\text{lam4}')

lam5 = Parameter(name = 'lam5',
                 nature = 'internal',
                 type = 'real',
                 value = '(-2*MHA**2 + MHH**2*(1 + cab**2 - sab**2) + MHL**2*(1 - cab**2 + sab**2))/(2.*vev**2)',
                 texname = '\\text{lam5}')

lam6 = Parameter(name = 'lam6',
                 nature = 'internal',
                 type = 'real',
                 value = '(cab*(-MHH**2 + MHL**2)*sab)/vev**2',
                 texname = '\\text{lam6}')

muzee = Parameter(name = 'muzee',
                  nature = 'internal',
                  type = 'real',
                  value = '(cphi*(-MHp**2 + MHpH**2)*sphi*cmath.sqrt(2))/vev',
                  texname = '\\text{muzee}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

I1a11 = Parameter(name = 'I1a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM1x1)',
                  texname = '\\text{I1a11}')

I1a12 = Parameter(name = 'I1a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM2x1)',
                  texname = '\\text{I1a12}')

I1a13 = Parameter(name = 'I1a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM3x1)',
                  texname = '\\text{I1a13}')

I1a21 = Parameter(name = 'I1a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM1x2)',
                  texname = '\\text{I1a21}')

I1a22 = Parameter(name = 'I1a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM2x2)',
                  texname = '\\text{I1a22}')

I1a23 = Parameter(name = 'I1a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM3x2)',
                  texname = '\\text{I1a23}')

I1a31 = Parameter(name = 'I1a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM1x3)',
                  texname = '\\text{I1a31}')

I1a32 = Parameter(name = 'I1a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM2x3)',
                  texname = '\\text{I1a32}')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM3x3)',
                  texname = '\\text{I1a33}')

I2a11 = Parameter(name = 'I2a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x1)',
                  texname = '\\text{I2a11}')

I2a12 = Parameter(name = 'I2a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x1)',
                  texname = '\\text{I2a12}')

I2a13 = Parameter(name = 'I2a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x1)',
                  texname = '\\text{I2a13}')

I2a21 = Parameter(name = 'I2a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x2)',
                  texname = '\\text{I2a21}')

I2a22 = Parameter(name = 'I2a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x2)',
                  texname = '\\text{I2a22}')

I2a23 = Parameter(name = 'I2a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x2)',
                  texname = '\\text{I2a23}')

I2a31 = Parameter(name = 'I2a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x3)',
                  texname = '\\text{I2a31}')

I2a32 = Parameter(name = 'I2a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x3)',
                  texname = '\\text{I2a32}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x3)',
                  texname = '\\text{I2a33}')

I3a11 = Parameter(name = 'I3a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yup',
                  texname = '\\text{I3a11}')

I3a12 = Parameter(name = 'I3a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*yup',
                  texname = '\\text{I3a12}')

I3a13 = Parameter(name = 'I3a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yup',
                  texname = '\\text{I3a13}')

I3a21 = Parameter(name = 'I3a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*yc',
                  texname = '\\text{I3a21}')

I3a22 = Parameter(name = 'I3a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*yc',
                  texname = '\\text{I3a22}')

I3a23 = Parameter(name = 'I3a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yc',
                  texname = '\\text{I3a23}')

I3a31 = Parameter(name = 'I3a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*yt',
                  texname = '\\text{I3a31}')

I3a32 = Parameter(name = 'I3a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*yt',
                  texname = '\\text{I3a32}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yt',
                  texname = '\\text{I3a33}')

I4a11 = Parameter(name = 'I4a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*ydo',
                  texname = '\\text{I4a11}')

I4a12 = Parameter(name = 'I4a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*ys',
                  texname = '\\text{I4a12}')

I4a13 = Parameter(name = 'I4a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yb',
                  texname = '\\text{I4a13}')

I4a21 = Parameter(name = 'I4a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*ydo',
                  texname = '\\text{I4a21}')

I4a22 = Parameter(name = 'I4a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*ys',
                  texname = '\\text{I4a22}')

I4a23 = Parameter(name = 'I4a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yb',
                  texname = '\\text{I4a23}')

I4a31 = Parameter(name = 'I4a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*ydo',
                  texname = '\\text{I4a31}')

I4a32 = Parameter(name = 'I4a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*ys',
                  texname = '\\text{I4a32}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yb',
                  texname = '\\text{I4a33}')

