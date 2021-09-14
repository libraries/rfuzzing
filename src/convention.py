# Rate of generating best numbers
p_best_numbers = 0.05
# Rate of generating mop instructions
p_instruction_imc = 0
# Rate of generating mop instructions
p_instruction_b = 1
# Rate of generating mop instructions
p_instruction_mop = 1

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

instruction_rule_imc = [
    ['add', [['add', 'rd', 'r?', 'r?']]],
    ['addi', [['addi', 'rd', 'r?', 'i12']]],
    ['addiw', [['addiw', 'rd', 'r?', 'i12']]],
    ['addw', [['addw', 'rd', 'r?', 'r?']]],
    ['and', [['and', 'rd', 'r?', 'r?']]],
    ['andi', [['andi', 'rd', 'r?', 'i12']]],
    ['auipc', [['auipc', 'a0', '0'], ['auipc', 'rd', 'u20'], ['sub', 'rd', 'rd', 'a0'], ['li', 'a0', 'u64']]],
    ['beq', [['.byte', '01100011', 'b0000100', 'bbbbbbbb', '0000000b']]],
    ['bge', [['.byte', '01100011', 'b1010100', 'bbbbbbbb', '0000000b']]],
    ['bgeu', [['.byte', '01100011', 'b1110100', 'bbbbbbbb', '0000000b']]],
    ['blt', [['.byte', '01100011', 'b1000100', 'bbbbbbbb', '0000000b']]],
    ['bltu', [['.byte', '01100011', 'b1100100', 'bbbbbbbb', '0000000b']]],
    ['bne', [['.byte', '01100011', 'b0010100', 'bbbbbbbb', '0000000b']]],
    ['div', [['div', 'rd', 'r?', 'r?']]],
    ['divu', [['divu', 'rd', 'r?', 'r?']]],
    ['divuw', [['divuw', 'rd', 'r?', 'r?']]],
    ['divw', [['divw', 'rd', 'r?', 'r?']]],
    ['ebreak', [['nop']]],
    ['ecall', [['nop']]],
    ['fence', [['fence']]],
    ['fencei', [['fence']]],
    ['jal', [['.byte', '01101111', '00000000', '01000000', '00000000']]],
    ['jalr', [['auipc', 'a0', '0'],  ['.byte', '01100111', '00000000', '10000101', '00000000'], ['li', 'a0', 'u64']]],
    ['lb', [['la', 'a0', 'number'], ['lb', 'rd', '0(a0)'], ['li', 'a0', 'u64']]],
    ['lbu', [['la', 'a0', 'number'], ['lbu', 'rd', '0(a0)'], ['li', 'a0', 'u64']]],
    ['ld', [['la', 'a0', 'number'], ['ld', 'rd', '0(a0)'], ['li', 'a0', 'u64']]],
    ['lh', [['la', 'a0', 'number'], ['lh', 'rd', '0(a0)'], ['li', 'a0', 'u64']]],
    ['lhu', [['la', 'a0', 'number'], ['lhu', 'rd', '0(a0)'], ['li', 'a0', 'u64']]],
    ['lui', [['lui', 'rd', 'u20']]],
    ['lw', [['la', 'a0', 'number'], ['lw', 'rd', '0(a0)'], ['li', 'a0', 'u64']]],
    ['lwu', [['la', 'a0', 'number'], ['lwu', 'rd', '0(a0)'], ['li', 'a0', 'u64']]],
    ['mul', [['mul', 'rd', 'r?', 'r?']]],
    ['mulh', [['mulh', 'rd', 'r?', 'r?']]],
    ['mulhsu', [['mulhsu', 'rd', 'r?', 'r?']]],
    ['mulhu', [['mulhu', 'rd', 'r?', 'r?']]],
    ['mulw', [['mulw', 'rd', 'r?', 'r?']]],
    ['or', [['or', 'rd', 'r?', 'r?']]],
    ['ori', [['ori', 'rd', 'r?', 'i12']]],
    ['rem', [['rem', 'rd', 'r?', 'r?']]],
    ['remu', [['remu', 'rd', 'r?', 'r?']]],
    ['remuw', [['remuw', 'rd', 'r?', 'r?']]],
    ['remw', [['remw', 'rd', 'r?', 'r?']]],
    ['sb', [['la', 'a0', 'number'], ['sb', 'rd', '0(a0)'], ['li', 'a0', 'u64']]],
    ['sd', [['la', 'a0', 'number'], ['sd', 'rd', '0(a0)'], ['li', 'a0', 'u64']]],
    ['sh', [['la', 'a0', 'number'], ['sh', 'rd', '0(a0)'], ['li', 'a0', 'u64']]],
    ['sll', [['sll', 'rd', 'r?', 'r?']]],
    ['slli', [['slli', 'rd', 'r?', 'u6']]],
    ['slliw', [['slliw', 'rd', 'r?', 'u5']]],
    ['sllw', [['sllw', 'rd', 'r?', 'r?']]],
    ['slt', [['slt', 'rd', 'r?', 'r?']]],
    ['slti', [['slti', 'rd', 'r?', 'i12']]],
    ['sltiu', [['sltiu', 'rd', 'r?', 'i12']]],
    ['sltu', [['sltu', 'rd', 'r?', 'r?']]],
    ['sra', [['sra', 'rd', 'r?', 'r?']]],
    ['srai', [['srai', 'rd', 'r?', 'u6']]],
    ['sraiw', [['sraiw', 'rd', 'r?', 'u5']]],
    ['sraw', [['sraw', 'rd', 'r?', 'r?']]],
    ['srl', [['srl', 'rd', 'r?', 'r?']]],
    ['srli', [['srli', 'rd', 'r?', 'u6']]],
    ['srliw', [['srliw', 'rd', 'r?', 'u5']]],
    ['srlw', [['srlw', 'rd', 'r?', 'r?']]],
    ['sub', [['sub', 'rd', 'r?', 'r?']]],
    ['subw', [['subw', 'rd', 'r?', 'r?']]],
    ['sw', [['la', 'a0', 'number'], ['sw', 'rd', '0(a0)'], ['li', 'a0', 'u64']]],
    ['xor', [['xor', 'rd', 'r?', 'r?']]],
    ['xori', [['xori', 'rd', 'r?', 'i12']]],
]

instruction_rule_b = [
    ['add.uw', ['r', 'r', 'r']],
    ['andn', ['r', 'r', 'r']],
    ['clmul', ['r', 'r', 'r']],
    ['clmulh', ['r', 'r', 'r']],
    ['clmulr', ['r', 'r', 'r']],
    ['clz', ['r', 'r']],
    ['clzw', ['r', 'r']],
    ['cpop', ['r', 'r']],
    ['cpopw', ['r', 'r']],
    ['ctz', ['r', 'r']],
    ['ctzw', ['r', 'r']],
    ['max', ['r', 'r', 'r']],
    ['maxu', ['r', 'r', 'r']],
    ['min', ['r', 'r', 'r']],
    ['minu', ['r', 'r', 'r']],
    ['orc.b', ['r', 'r']],
    ['orn', ['r', 'r', 'r']],
    ['rev8', ['r', 'r']],
    ['rol', ['r', 'r', 'r']],
    ['rolw', ['r', 'r', 'r']],
    ['ror', ['r', 'r', 'r']],
    ['rori', ['r', 'r', 'u6']],
    ['roriw', ['r', 'r', 'u5']],
    ['rorw', ['r', 'r', 'r']],
    ['bclr', ['r', 'r', 'r']],
    ['bclri', ['r', 'r', 'u6']],
    ['bext', ['r', 'r', 'r']],
    ['bexti', ['r', 'r', 'u6']],
    ['binv', ['r', 'r', 'r']],
    ['binvi', ['r', 'r', 'u6']],
    ['bset', ['r', 'r', 'r']],
    ['bseti', ['r', 'r', 'u6']],
    ['sext.b', ['r', 'r']],
    ['sext.h', ['r', 'r']],
    ['sh1add', ['r', 'r', 'r']],
    ['sh1add.uw', ['r', 'r', 'r']],
    ['sh2add', ['r', 'r', 'r']],
    ['sh2add.uw', ['r', 'r', 'r']],
    ['sh3add', ['r', 'r', 'r']],
    ['sh3add.uw', ['r', 'r', 'r']],
    ['slli.uw', ['r', 'r', 'u6']],
    ['xnor', ['r', 'r', 'r']],
    ['zext.h', ['r', 'r']],
]

instruction_rule_mop = {
    'wide_mul': ['mulh r2, r0, r1', 'mul r3, r0, r1'],
    'wide_mulu': ['mulhu r2, r0, r1', 'mul r3, r0, r1'],
    'wide_mulsu': ['mulhsu r2, r0, r1', 'mul r3, r0, r1'],
    'wide_div': ['div r2, r0, r1', 'rem r3, r0, r1'],
    'wide_divu': ['divu r2, r0, r1', 'remu r3, r0, r1'],
    'adc': ['add r0, r0, r1', 'sltu r1, r0, r1', 'add r0, r0, r2', 'sltu r2, r0, r2', 'or r1, r1, r2'],
    'sbb': ['sub r1, r0, r1', 'sltu r3, r0, r1', 'sub r0, r1, r2', 'sltu r2, r1, r0', 'or r1, r2, r3'],
    'twins_ld_0': ['li sp, 0x3ff000', 'ld r0, 0(sp)', 'ld r1, 8(sp)'],
    'twins_ld_1': ['li sp, 0x3ff000', 'ld r1, 8(sp)', 'ld r0, 0(sp)'],
    'twins_ld_2': ['li sp, 0x3ff008', 'ld r1, -8(sp)', 'ld r0, 0(sp)'],
    'twins_sd_0': ['li sp, 0x3ff000', 'sd r0, 0(sp)', 'sd r1, 8(sp)'],
    'twins_sd_1': ['li sp, 0x3ff000', 'sd r1, 8(sp)', 'sd r0, 0(sp)'],
    'twins_sd_2': ['li sp, 0x3ff008', 'sd r1, -8(sp)', 'sd r0, 0(sp)'],
}
