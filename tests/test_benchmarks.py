# -*- coding: utf-8 -*-

from declarativeunittest import *
from construct import *
from construct.lib import *

pytest.mark.skipif(not PY3, reason="uses bytes()")
pytest.mark.skipif(not supportscompiler, reason="compiler requires Python 3.6")


def test_class_bytes_parse(benchmark):
    d = Bytes(100)
    benchmark(d.parse, bytes(100))

def test_class_bytes_parse_compiled(benchmark):
    d = Bytes(100).compile()
    benchmark(d.parse, bytes(100))

def test_class_bytes_build(benchmark):
    d = Bytes(100)
    benchmark(d.build, bytes(100))

def test_class_greedybytes_parse(benchmark):
    d = GreedyBytes
    benchmark(d.parse, bytes(100))

def test_class_greedybytes_parse_compiled(benchmark):
    d = GreedyBytes.compile()
    benchmark(d.parse, bytes(100))

def test_class_greedybytes_build(benchmark):
    d = GreedyBytes
    benchmark(d.build, bytes(100))

def test_class_bitwise_parse(benchmark):
    d = Bitwise(Bytes(800))
    benchmark(d.parse, bytes(100))

def test_class_bitwise_parse_compiled(benchmark):
    d = Bitwise(Bytes(800)).compile()
    benchmark(d.parse, bytes(100))

def test_class_bitwise_build(benchmark):
    d = Bitwise(Bytes(800))
    benchmark(d.build, bytes(800))

def test_class_bytewise_parse(benchmark):
    d = Bitwise(Bytewise(Bytes(100)))
    benchmark(d.parse, bytes(100))

def test_class_bytewise_parse_compiled(benchmark):
    d = Bitwise(Bytewise(Bytes(100))).compile()
    benchmark(d.parse, bytes(100))

def test_class_bytewise_build(benchmark):
    d = Bitwise(Bytewise(Bytes(100)))
    benchmark(d.build, bytes(100))

def test_class_formatfield_parse(benchmark):
    d = FormatField(">", "L")
    benchmark(d.parse, bytes(4))

def test_class_formatfield_parse_compiled(benchmark):
    d = FormatField(">", "L").compile()
    benchmark(d.parse, bytes(4))

def test_class_formatfield_build(benchmark):
    d = FormatField(">", "L")
    benchmark(d.build, 0)

def test_class_bytesinteger_parse(benchmark):
    d = BytesInteger(4)
    benchmark(d.parse, bytes(4))

def test_class_bytesinteger_parse_compiled(benchmark):
    d = BytesInteger(4).compile()
    benchmark(d.parse, bytes(4))

def test_class_bytesinteger_build(benchmark):
    d = BytesInteger(4)
    benchmark(d.build, 0)

def test_class_bitsinteger_parse(benchmark):
    d = Bitwise(BitsInteger(32, swapped=True))
    benchmark(d.parse, bytes(4))

def test_class_bitsinteger_parse_compiled(benchmark):
    d = Bitwise(BitsInteger(32, swapped=True)).compile()
    benchmark(d.parse, bytes(4))

def test_class_bitsinteger_build(benchmark):
    d = Bitwise(BitsInteger(32, swapped=True))
    benchmark(d.build, 0)

def test_class_varint_parse(benchmark):
    d = VarInt
    benchmark(d.parse, b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x04')

def test_class_varint_parse_compiled(benchmark):
    d = VarInt.compile()
    benchmark(d.parse, b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x04')

def test_class_varint_build(benchmark):
    d = VarInt
    benchmark(d.build, 2**64)

def test_class_struct_parse(benchmark):
    d = Struct("a"/Byte, "b"/Byte, "c"/Byte, "d"/Byte, "e"/Byte)
    benchmark(d.parse, bytes(5))

def test_class_struct_parse_compiled(benchmark):
    d = Struct("a"/Byte, "b"/Byte, "c"/Byte, "d"/Byte, "e"/Byte).compile()
    benchmark(d.parse, bytes(5))

def test_class_struct_build(benchmark):
    d = Struct("a"/Byte, "b"/Byte, "c"/Byte, "d"/Byte, "e"/Byte)
    benchmark(d.build, dict(a=0, b=0, c=0, d=0, e=0))

def test_class_sequence_parse(benchmark):
    d = Sequence(Byte, Byte, Byte, Byte, Byte)
    benchmark(d.parse, bytes(5))

def test_class_sequence_parse_compiled(benchmark):
    d = Sequence(Byte, Byte, Byte, Byte, Byte).compile()
    benchmark(d.parse, bytes(5))

def test_class_sequence_build(benchmark):
    d = Sequence(Byte, Byte, Byte, Byte, Byte)
    benchmark(d.build, [0]*5)

def test_class_array_parse(benchmark):
    d = Array(100, Byte)
    benchmark(d.parse, bytes(100))

def test_class_array_parse_compiled(benchmark):
    d = Array(100, Byte).compile()
    benchmark(d.parse, bytes(100))

def test_class_array_build(benchmark):
    d = Array(100, Byte)
    benchmark(d.build, [0]*100)

def test_class_greedyrange_parse(benchmark):
    d = GreedyRange(Byte)
    benchmark(d.parse, bytes(100))

def test_class_greedyrange_parse_compiled(benchmark):
    d = GreedyRange(Byte).compile()
    benchmark(d.parse, bytes(100))

def test_class_greedyrange_build(benchmark):
    d = GreedyRange(Byte)
    benchmark(d.build, [0]*100)

def test_class_repeatuntil_parse(benchmark):
    d = RepeatUntil(obj_ > 0, Byte)
    benchmark(d.parse, bytes(i<10 for i in range(10)))

def test_class_repeatuntil_parse_compiled(benchmark):
    d = RepeatUntil(obj_ > 0, Byte).compile()
    benchmark(d.parse, bytes(i<10 for i in range(10)))

def test_class_repeatuntil_build(benchmark):
    d = RepeatUntil(obj_ > 0, Byte)
    benchmark(d.build, [int(i<9) for i in range(10)])

def test_class_const_parse(benchmark):
    d = Const(bytes(4))
    benchmark(d.parse, bytes(4))

def test_class_const_parse_compiled(benchmark):
    d = Const(bytes(4)).compile()
    benchmark(d.parse, bytes(4))

def test_class_const_build(benchmark):
    d = Const(bytes(4))
    benchmark(d.build, bytes(4))

def test_class_computed_parse(benchmark):
    d = Computed(this.entry)
    benchmark(d.parse, bytes(), entry=1)

def test_class_computed_parse_compiled(benchmark):
    d = Computed(this.entry).compile()
    benchmark(d.parse, bytes(), entry=1)

def test_class_computed_build(benchmark):
    d = Computed(this.entry)
    benchmark(d.build, None, entry=1)

def test_class_rebuild_parse(benchmark):
    d = Rebuild(Int32ub, 0)
    benchmark(d.parse, bytes(4))

def test_class_rebuild_parse_compiled(benchmark):
    d = Rebuild(Int32ub, 0).compile()
    benchmark(d.parse, bytes(4))

def test_class_rebuild_build(benchmark):
    d = Rebuild(Int32ub, 0)
    benchmark(d.build, None)

def test_class_default_parse(benchmark):
    d = Default(Int32ub, 0)
    benchmark(d.parse, bytes(4))

def test_class_default_parse_compiled(benchmark):
    d = Default(Int32ub, 0).compile()
    benchmark(d.parse, bytes(4))

def test_class_default_build(benchmark):
    d = Default(Int32ub, 0)
    benchmark(d.build, None)

def test_class_check_parse(benchmark):
    d = Check(this.entry == 1)
    benchmark(d.parse, bytes(4), entry=1)

def test_class_check_parse_compiled(benchmark):
    d = Check(this.entry == 1).compile()
    benchmark(d.parse, bytes(4), entry=1)

def test_class_check_build(benchmark):
    d = Check(this.entry == 1)
    benchmark(d.build, None, entry=1)

# Error

# -----------------------------------------------
# above have parse-compiled version (3), below have not (2)

def test_class_focusedseq_parse(benchmark):
    d = FocusedSeq("num", Const(bytes(2)), "num"/Byte, Terminated)
    benchmark(d.parse, bytes(3))

def test_class_focusedseq_build(benchmark):
    d = FocusedSeq("num", Const(bytes(2)), "num"/Byte, Terminated)
    benchmark(d.build, 0)

def test_class_numpy_parse(benchmark):
    d = Numpy
    benchmark(d.parse, b"\x93NUMPY\x01\x00F\x00{'descr': '<i8', 'fortran_order': False, 'shape': (3,), }            \n\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00")

# NamedTuple

def test_class_hex_parse(benchmark):
    d = Hex(GreedyBytes)
    benchmark(d.parse, bytes(100))

def test_class_hex_build(benchmark):
    d = Hex(GreedyBytes)
    benchmark(d.build, bytes(100))

def test_class_hexdump_parse(benchmark):
    d = HexDump(GreedyBytes)
    benchmark(d.parse, bytes(100))

def test_class_hexdump_build(benchmark):
    d = HexDump(GreedyBytes)
    benchmark(d.build, bytes(100))

# Padding

def test_class_padded_parse(benchmark):
    d = Padded(4, Byte)
    benchmark(d.parse, bytes(4))

def test_class_padded_build(benchmark):
    d = Padded(4, Byte)
    benchmark(d.build, 0)

def test_class_aligned_parse(benchmark):
    d = Aligned(4, Byte)
    benchmark(d.parse, bytes(4))

def test_class_aligned_build(benchmark):
    d = Aligned(4, Byte)
    benchmark(d.build, 0)

# AlignedStruct
# BitStruct

def test_class_union_parse(benchmark):
    d = Union(0, "raw"/Bytes(8), "ints"/Int32ub[2], "shorts"/Int16ub[4], "chars"/Byte[8])
    benchmark(d.parse, bytes(8))

def test_class_union_build(benchmark):
    d = Union(0, "raw"/Bytes(8), "ints"/Int32ub[2], "shorts"/Int16ub[4], "chars"/Byte[8])
    benchmark(d.build, dict(chars=[0]*8))

def test_class_select_parse(benchmark):
    d = Select(Int32ub, CString(encoding="utf8"))
    benchmark(d.parse, bytes(20))

def test_class_select_build(benchmark):
    d = Select(Int32ub, CString(encoding="utf8"))
    benchmark(d.build, "")

# Optional
# If
# IfThenElse

def test_class_switch_parse(benchmark):
    d = Switch(this.n, { 1:Int8ub, 2:Int16ub, 4:Int32ub })
    benchmark(d.parse, bytes(4), n=4)

def test_class_switch_build(benchmark):
    d = Switch(this.n, { 1:Int8ub, 2:Int16ub, 4:Int32ub })
    benchmark(d.build, 0, n=4)

# StopIf

def test_class_pointer_parse(benchmark):
    d = Pointer(8, Bytes(4))
    benchmark(d.parse, bytes(12))

def test_class_pointer_build(benchmark):
    d = Pointer(8, Bytes(4))
    benchmark(d.build, bytes(4))

def test_class_peek_parse(benchmark):
    d = Sequence(Peek(Int8ub), Peek(Int16ub))
    benchmark(d.parse, bytes(2))

def test_class_peek_build(benchmark):
    d = Sequence(Peek(Int8ub), Peek(Int16ub))
    benchmark(d.build, [0,0])

# Seek
# Tell
# Pass
# Terminated
# Restreamed
# Rebuffered

def test_class_rawcopy_parse(benchmark):
    d = RawCopy(Byte)
    benchmark(d.parse, bytes(1))

def test_class_rawcopy_build1(benchmark):
    d = RawCopy(Byte)
    benchmark(d.build, dict(data=bytes(1)))

def test_class_rawcopy_build2(benchmark):
    d = RawCopy(Byte)
    benchmark(d.build, dict(value=0))

def test_class_byteswapped_parse(benchmark):
    d = ByteSwapped(Bytes(100))
    benchmark(d.parse, bytes(100))

def test_class_byteswapped_parse_compiled(benchmark):
    d = ByteSwapped(Bytes(100)).compile()
    benchmark(d.parse, bytes(100))

def test_class_byteswapped_build(benchmark):
    d = ByteSwapped(Bytes(100))
    benchmark(d.build, bytes(100))

def test_class_bitsswapped_parse(benchmark):
    d = BitsSwapped(Bytes(100))
    benchmark(d.parse, bytes(100))

def test_class_bitsswapped_parse_compiled(benchmark):
    d = BitsSwapped(Bytes(100)).compile()
    benchmark(d.parse, bytes(100))

def test_class_bitsswapped_build(benchmark):
    d = BitsSwapped(Bytes(100))
    benchmark(d.build, bytes(100))

def test_class_prefixed_parse(benchmark):
    d = Prefixed(Byte, GreedyBytes)
    benchmark(d.parse, b"\x08"+bytes(8))

def test_class_prefixed_build(benchmark):
    d = Prefixed(Byte, GreedyBytes)
    benchmark(d.build, bytes(8))

def test_class_prefixedarray_parse(benchmark):
    d = PrefixedArray(Byte, Byte)
    benchmark(d.parse, b"\x08"+bytes(8))

def test_class_prefixedarray_build(benchmark):
    d = PrefixedArray(Byte, Byte)
    benchmark(d.build, [0]*8)

# Checksum
# Compressed

# LazyField
# LazyBound

def test_class_flag_parse(benchmark):
    d = Flag
    benchmark(d.parse, bytes(1))

def test_class_flag_build(benchmark):
    d = Flag
    benchmark(d.build, False)

def test_class_enum_parse(benchmark):
    d = Enum(Byte, zero=0, one=1)
    benchmark(d.parse, bytes(1))

def test_class_enum_build(benchmark):
    d = Enum(Byte, zero=0, one=1)
    benchmark(d.build, 0)

def test_class_flagsenum_parse(benchmark):
    d = FlagsEnum(Byte, a=1, b=2, c=4, d=8)
    benchmark(d.parse, bytes(1))

def test_class_flagsenum_build(benchmark):
    d = FlagsEnum(Byte, a=1, b=2, c=4, d=8)
    benchmark(d.build, Container(a=False, b=False, c=False, d=False))

# Mapping
# SymmetricMapping

# ExprAdapter
# ExprSymmetricAdapter
# ExprValidator
# OneOf
# NoneOf
# Filter
# Slicing
# Indexing

def test_class_string_parse(benchmark):
    d = String(10, encoding="utf8")
    benchmark(d.parse, b'\xd0\x90\xd1\x84\xd0\xbe\xd0\xbd\x00\x00')

def test_class_string_build(benchmark):
    d = String(10, encoding="utf8")
    benchmark(d.build, u"Афон")

def test_class_pascalstring_parse(benchmark):
    d = PascalString(VarInt, encoding="utf8")
    benchmark(d.parse, b'\x08\xd0\x90\xd1\x84\xd0\xbe\xd0\xbd')

def test_class_pascalstring_build(benchmark):
    d = PascalString(VarInt, encoding="utf8")
    benchmark(d.build, u"Афон")

def test_class_cstring_parse(benchmark):
    d = CString(encoding="utf8")
    benchmark(d.parse, b'\xd0\x90\xd1\x84\xd0\xbe\xd0\xbd\x00')

def test_class_cstring_build(benchmark):
    d = CString(encoding="utf8")
    benchmark(d.build, u"Афон")

# GreedyString
