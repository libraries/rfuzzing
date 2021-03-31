registers = [
    'zero', 'ra', 'sp', 'gp',
    'tp', 't0', 't1', 't2',
    's0', 's1', 'a0', 'a1',
    'a2', 'a3', 'a4', 'a5',
    'a6', 'a7', 's2', 's3',
    's4', 's5', 's6', 's7',
    's8', 's9', 's10', 's11',
    't3', 't4', 't5', 't6',
]

idle_registers = registers[:-1]

# Some special numbers for boundary value testing.
best_numbers = [
    0x0000000000000000,
    0x0000000000000001,
    0xffffffffffffffff,
    0x8000000000000000,
    0x0000000000000004,
    0x0000000000000040,
    0x0000000000000080,
    0x0000000000002000,
    0x0000000000010000,
    0x0000000000400000,
    0x0000000001000000,
    0x0000000100000000,
    0x0000008000000000,
    0x0000020000000000,
    0x0000800000000000,
    0x0010000000000000,
    0x0100000000000000,
    0x1000000000000000,
    0x000000000000000d,
    0x0000000000000000,
    0x0000000000000067,
    0x2e00000000000000,
    0x000000000000015b,
    0x9420000000000000,
    0x00000000000075da,
    0xe35a000000000000,
    0x000000000003ed82,
    0x8b4eb00000000000,
    0x000000000000714c,
    0xfad4dc0000000000,
    0x000000000dd2966b,
    0x686f332000000000,
    0x00000000a865d7d4,
    0x6edd225600000000,
    0x0000000380f3cf69,
    0xaf29109cc0000000,
    0x000000a3714b9ad2,
    0x7dc2ae94e4000000,
    0x00000bea6a6af755,
    0xea2177d8d5100000,
    0x00004a9e26b7f794,
    0x6d159abfb3030000,
    0x00020e6dfbb7c441,
    0xd251a40a022b9000,
    0x00129af7f2440efe,
    0xc7dee68fffbaf900,
    0x05ada4e53975b451,
    0x63eb500cce126b70,
    0x314320aa7da5b1ef,
    0xd27d2fde3497614c,
    0xbe55668178139c8e,
    0x9480583abdfb5837,
    0x9d8dbb3a5bde4347,
    0x61fd04828c93ce01,
    0xdf9a26c8470349dd,
    0xca9d54bd4e78980e,
    0xb1db9b0fecbfaabe,
    0xe79541e25d0dba6b,
    0xff98837fda2a5bdf,
    0xc3bd5e2cd52318a8,
    0x02ab7bb54e687499,
    0xbebf0929f41aa230,
    0x58aee9fdc3f41b74,
    0x62daff171a9fae42,
    0xe5baa16ee5b5419e,
    0x16b3a918e4278c9d,
    0x4ab9cfc9a41744c4,
    0x86ddce906c8cdb4d,
    0x867e3492977cb1bb,
    0x3d0e482377794618,
    0x90e1bc8ba22d3294,
    0xf48119b103954df1,
    0x79780d4e5b2b3b2a,
    0xb36eb1caa58ee7dc,
    0xf0fe55be95a18d13,
    0x1234769364d9eac9,
    0x31a7445bdf8bcb5c,
    0x1735808ee4398bca,
    0x8f09996552504a5d,
    0x4fcf7212bebfdd89,
    0xdfd3a0870f60e072,
    0x25474d793f2c7d32,
    0xb9e2a99fdb7b2948,
    0x0da24e08451a8d1a,
    0x44a705073f90be80,
    0x7f2e6910bdea3ffd,
    0x7fc92593c865b4c2,
    0x0f812a265e560f2b,
    0xfecee737556609f5,
    0x996d1b60923c18a6,
    0x2c1fb5204d248917,
    0x4cf560811e3465c5,
    0xf2a6b292a535dc4e,
    0x3b4de2fabe6d6476,
    0xa6a669d1baba633e,
    0xa73c905bcbc01878,
    0x38be984c83ce8648,
    0x262a15662b298944,
    0xdf09e5c90a990b56,
    0xa8519a5b46242cc0,
    0x14d93f0c55095499,
    0xbad28e0ca5854070,
    0x93d7d7a9d87056f0,
    0x3b0d936889b10a5d,
    0x0ec6680cabb95f09,
    0x27429c30e8b6cff7,
    0x6465f271027abfa8,
    0xd0abd7d3688aa0d7,
    0x986a686578456056,
    0xc10a152d71cb3f16,
    0x4a6c986967d5ace8,
    0x37269c228e8e3db1,
    0xf5bad73c74be6d8a,
    0x68323fe289df33d1,
    0xcb9848f06e9659f6,
    0x5052886f7169c8c5,
    0xb040414dd8c98a14,
    0xea59a91078581c00,
    0x7c6bcb08155fac38,
    0xbd6192029dd91d60,
    0x8a4a182923bdf75a,
    0x8c91e2fe14041a34,
    0xc9d368e6546c1f00,
    0xdfd83d690e5f073e,
    0x34f2a050c605b6b0,
    0xf3fbe985738811dd,
    0x2d21e3da342cd6be,
    0x31523358d080e093,
]

# Rate of generating best numbers
p_best_numbers = 0.05

instruction_rule_32 = [
    ['clz', ['r', 'r']],
    ['ctz', ['r', 'r']],
    ['pcnt', ['r', 'r']],
    ['andn', ['r', 'r', 'r']],
    ['orn', ['r', 'r', 'r']],
    ['xnor', ['r', 'r', 'r']],
    ['pack', ['r', 'r', 'r']],
    ['packu', ['r', 'r', 'r']],
    ['packh', ['r', 'r', 'r']],
    ['min', ['r', 'r', 'r']],
    ['max', ['r', 'r', 'r']],
    ['minu', ['r', 'r', 'r']],
    ['maxu', ['r', 'r', 'r']],
    ['sext.b', ['r', 'r']],
    ['sext.h', ['r', 'r']],
    ['sbset', ['r', 'r', 'r']],
    ['sbclr', ['r', 'r', 'r']],
    ['sbinv', ['r', 'r', 'r']],
    ['sbext', ['r', 'r', 'r']],
    ['sbseti', ['r', 'r', 'xlen']],
    ['sbclri', ['r', 'r', 'xlen']],
    ['sbinvi', ['r', 'r', 'xlen']],
    ['sbexti', ['r', 'r', 'xlen']],
    ['slo', ['r', 'r', 'r']],
    ['sro', ['r', 'r', 'r']],
    ['sloi', ['r', 'r', 'xlen']],
    ['sroi', ['r', 'r', 'xlen']],
    ['ror', ['r', 'r', 'r']],
    ['rol', ['r', 'r', 'r']],
    ['rori', ['r', 'r', 'xlen']],
    ['grev', ['r', 'r', 'r']],
    ['grevi', ['r', 'r', 'xlen']],
    ['shfl', ['r', 'r', 'r']],
    ['unshfl', ['r', 'r', 'r']],
    ['shfli', ['r', 'r', 'half']],
    ['unshfli', ['r', 'r', 'half']],
    ['gorc', ['r', 'r', 'r']],
    ['gorci', ['r', 'r', 'xlen']],
    ['bfp', ['r', 'r', 'r']],
    ['bext', ['r', 'r', 'r']],
    ['bdep', ['r', 'r', 'r']],
    ['clmul', ['r', 'r', 'r']],
    ['clmulh', ['r', 'r', 'r']],
    ['clmulr', ['r', 'r', 'r']],
    ['crc32.b', ['r', 'r']],
    ['crc32.h', ['r', 'r']],
    ['crc32.w', ['r', 'r']],
    ['crc32c.b', ['r', 'r']],
    ['crc32c.h', ['r', 'r']],
    ['crc32c.w', ['r', 'r']],
    ['cmix', ['r', 'r', 'r', 'r']],
    ['cmov', ['r', 'r', 'r', 'r']],
    ['fsl', ['r', 'r', 'r', 'r']],
    ['fsr', ['r', 'r', 'r', 'r']],
    ['fsri', ['r', 'r', 'r', 'xlen']],
    ['sh1add', ['r', 'r', 'r']],
    ['sh2add', ['r', 'r', 'r']],
    ['sh3add', ['r', 'r', 'r']],
]

instruction_rule_64 = [
    *instruction_rule_32,
    ['clzw', ['r', 'r']],
    ['ctzw', ['r', 'r']],
    ['pcntw', ['r', 'r']],
    ['packw', ['r', 'r', 'r']],
    ['packuw', ['r', 'r', 'r']],
    ['sbsetw', ['r', 'r', 'r']],
    ['sbclrw', ['r', 'r', 'r']],
    ['sbinvw', ['r', 'r', 'r']],
    ['sbextw', ['r', 'r', 'r']],
    ['sbsetiw', ['r', 'r', 'half']],
    ['sbclriw', ['r', 'r', 'half']],
    ['sbinviw', ['r', 'r', 'half']],
    ['slow', ['r', 'r', 'r']],
    ['srow', ['r', 'r', 'r']],
    ['sloiw', ['r', 'r', 'half']],
    ['sroiw', ['r', 'r', 'half']],
    ['rorw', ['r', 'r', 'r']],
    ['rolw', ['r', 'r', 'r']],
    ['roriw', ['r', 'r', 'half']],
    ['grevw', ['r', 'r', 'r']],
    ['greviw', ['r', 'r', 'half']],
    ['shflw', ['r', 'r', 'r']],
    ['unshflw', ['r', 'r', 'r']],
    ['gorcw', ['r', 'r', 'r']],
    ['gorciw', ['r', 'r', 'half']],
    ['bfpw', ['r', 'r', 'r']],
    ['bextw', ['r', 'r', 'r']],
    ['bdepw', ['r', 'r', 'r']],
    ['clmulw', ['r', 'r', 'r']],
    ['clmulhw', ['r', 'r', 'r']],
    ['clmulrw', ['r', 'r', 'r']],
    ['crc32.d', ['r', 'r']],
    ['crc32c.d', ['r', 'r']],
    ['bmator', ['r', 'r', 'r']],
    ['bmatxor', ['r', 'r', 'r']],
    ['bmatflip', ['r', 'r']],
    ['fslw', ['r', 'r', 'r', 'r']],
    ['fsrw', ['r', 'r', 'r', 'r']],
    ['fsriw', ['r', 'r', 'r', 'half']],
    ['addwu', ['r', 'r', 'r']],
    ['subwu', ['r', 'r', 'r']],
    ['addiwu', ['r', 'r', 'i12']],
    ['addu.w', ['r', 'r', 'r']],
    ['subu.w', ['r', 'r', 'r']],
    ['slliu.w', ['r', 'r', 'xlen']],
    ['sh1addu.w', ['r', 'r', 'r']],
    ['sh2addu.w', ['r', 'r', 'r']],
    ['sh3addu.w', ['r', 'r', 'r']],
]

instruction_rule_mop = [
    [['mulh', ['r', 'r', 'r']], ['mul', ['r', 'r', 'r']]],
    [['mulhu', ['r', 'r', 'r']], ['mul', ['r', 'r', 'r']]],
    [['mulhsu', ['r', 'r', 'r']], ['mul', ['r', 'r', 'r']]],
    [['div', ['r', 'r', 'r']], ['rem', ['r', 'r', 'r']]],
    [['divu', ['r', 'r', 'r']], ['remu', ['r', 'r', 'r']]],
]
