# -*- coding: utf-8 -*-

from declarativeunittest import *
from construct import *
from construct.lib import *

pytest.mark.skipif(not PY3, reason="uses bytes()")
pytest.mark.skipif(not supportscompiler, reason="compiler requires Python 3.6")


example = Struct(
    "num" / Byte,

    "bytes1" / Bytes(4),
    "bytes2" / Bytes(this.num),
    "greedybytes" / Prefixed(Byte, GreedyBytes),
    "bitwise1" / Bitwise(BitsInteger(8, swapped=False)),
    "bitwise2" / Bitwise(BitsInteger(8, swapped=True)),
    "bytewise1" / Bitwise(Bytewise(BytesInteger(16, swapped=True))),
    "bytewise2" / Bitwise(Bytewise(BytesInteger(16, swapped=False))),

    "formatfield" / FormatField(">", "B"),
    "bytesinteger1" / BytesInteger(16, swapped=True),
    "bytesinteger2" / BytesInteger(16, swapped=False),
    "bytesinteger3dynamic" / BytesInteger(this.num+1),
    "bitsinteger1" / Bitwise(BitsInteger(8, swapped=False)),
    "bitsinteger2" / Bitwise(BitsInteger(8, swapped=True)),
    "varint" / VarInt,
    "byte" / Byte,
    "float1" / Single,
    "float2" / Double,

    "string1" / String(12, encoding=StringsAsBytes),
    "string2" / String(12, encoding="utf8"),
    "string3" / String(12, encoding="utf16"),
    "string4" / String(12, encoding="utf32"),
    "pascalstring1" / PascalString(Byte, encoding=StringsAsBytes),
    "pascalstring2" / PascalString(Byte, encoding="utf8"),
    "cstring1" / CString(encoding=StringsAsBytes),
    "cstring2" / CString(encoding="utf8"),
    "cstring3" / CString(encoding="utf16"),
    "cstring4" / CString(encoding="utf32"),
    "greedystring1" / Prefixed(Byte, GreedyString(encoding=StringsAsBytes)),
    "greedystring2" / Prefixed(Byte, GreedyString(encoding="utf8")),

    "flag" / Flag,
    "enum" / Enum(Byte, zero=0),
    "flagsenum" / FlagsEnum(Byte, zero=0, one=1),
    # Mapping
    # SymmetricMapping

    "struct" / Struct("field" / Byte),
    "embeddedstruct" / Embedded(Struct("embeddedfield1" / Byte)),
    "sequence1" / Sequence(Byte, Byte),
    "sequence2" / Sequence("num1" / Byte, "num2" / Byte),
    "embeddedsequence1" / Sequence(Embedded(Sequence(Byte, Byte))),
    "embeddedsequence2" / Sequence(Embedded(Sequence("num1" / Byte, "num2" / Byte))),

    "array1" / Array(5, Byte),
    "array2" / Array(this.num, Byte),
    "greedyrange0" / Prefixed(Byte, GreedyRange(Byte)),
    "repeatuntil1" / RepeatUntil(obj_ == 0, Byte),

    "const1" / Const(bytes(4)),
    "const2" / Const(0, Int32ub),
    "computed" / Computed(this.num),

    "index1" / Array(3, Index),
    "index2" / RestreamData(b"\x00", GreedyRange(Byte >> Index)),
    "index3" / RestreamData(b"\x00", RepeatUntil(True, Byte >> Index)),

    "rebuild" / Rebuild(Byte, len_(this.array1)),
    "default" / Default(Byte, 0),
    Check(this.num == 0),
    "error0" / If(False, Error),
    "focusedseq1" / FocusedSeq(1, Const(bytes(4)), Byte),
    "focusedseq2" / FocusedSeq("num", Const(bytes(4)), "num"/Byte),
    "numpy_data" / Computed(b"\x93NUMPY\x01\x00F\x00{'descr': '<i8', 'fortran_order': False, 'shape': (3,), }            \n\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00"),
    "numpy1" / RestreamData(this.numpy_data, Numpy),
    "namedtuple1" / NamedTuple("coord", "x y z", Byte[3]),
    "namedtuple2" / RestreamData(b"\x00\x00\x00", NamedTuple("coord", "x y z", GreedyRange(Byte))),
    "namedtuple3" / NamedTuple("coord", "x y z", Byte >> Byte >> Byte),
    "namedtuple4" / NamedTuple("coord", "x y z", "x"/Byte + "y"/Byte + "z"/Byte),

    "union1" / Union(None, "char"/Byte, "short"/Short, "int"/Int),
    "union2" / Union(1, "char"/Byte, "short"/Short, "int"/Int),
    "union3" / Union(0, "char1"/Byte, "char2"/Byte, "char3"/Byte),
    "union4" / Union("char1", "char1"/Byte, "char2"/Byte, "char3"/Byte),
    "unionembedded" / Union(None, Embedded(Struct("char"/Byte))),
    "select" / Select(Byte, CString(StringsAsBytes)),
    "optional" / Optional(Byte),
    "if1" / If(this.num == 0, Byte),
    "ifthenelse" / IfThenElse(this.num == 0, Byte, Byte),
    "switch1" / Switch(this.num, {0 : Byte, 255 : Error}),
    "switch2" / Switch(this.num, {}, default=Byte),
    "stopif0" / StopIf(this.num == 255),
    "stopif1" / Struct(StopIf(this._.num == 0), Error),
    "stopif2" / Sequence(StopIf(this._.num == 0), Error),
    "stopif3" / GreedyRange(StopIf(this.num == 0)),

    "padding" / Padding(2),
    "paddedbyte" / Padded(4, Byte),
    "alignedbyte" / Aligned(4, Byte),
    "alignedstruct" / AlignedStruct(4, "a"/Byte, "b"/Short),
    "bitstruct" / BitStruct("a"/Octet),

    "pointer" / Pointer(0, Byte),
    "peek" / Peek(Byte),
    "seek0" / Seek(0, 1),
    "tell" / Tell,
    "pass1" / Pass,
    "terminated0" / Prefixed(Byte, Terminated),
    # Restreamed
    # Rebuffered

    "rawcopy1" / RawCopy(Byte),
    "rawcopy2" / RawCopy(RawCopy(RawCopy(Byte))),
    "bytesswapped" / ByteSwapped(BytesInteger(8)),
    "bitsswapped" / BitsSwapped(BytesInteger(8)),
    "prefixed1" / Prefixed(Byte, GreedyBytes),
    "prefixed2" / RestreamData(b"\x01", Prefixed(Byte, GreedyBytes, includelength=True)),
    "prefixedarray" / PrefixedArray(Byte, Byte),
    "restreamdata" / RestreamData(b"\xff", Byte),
    "restreamdata_verify" / Check(this.restreamdata == 255),
    # Checksum
    "compressed_bzip2_data" / Computed(b'BZh91AY&SYSc\x11\x99\x00\x00\x00A\x00@\x00@\x00 \x00!\x00\x82\x83\x17rE8P\x90Sc\x11\x99'),
    "compressed_bzip2" / RestreamData(this.compressed_bzip2_data, Compressed(GreedyBytes, "bzip2", level=9)),

    # LazyField
    # LazyBound

    # adapters and validators

    # Probe(),
    # ProbeInto(this.num),
    # Debugger

    # faulty list_ implementation, compiles into correct code?
    # "items" / Computed([1,2,3]),
    # "len_" / Computed(len_(this.items)),

    # faulty list_ implementation, compiles into correct code
    # "repeatuntil2" / RepeatUntil(list_ == [0], Byte),
    # "repeatuntil3" / RepeatUntil(list_[-1] == 0, Byte),
)
data = bytes(1000)


@pytest.mark.skipif(not supportscompiler, reason="compiler requires Python 3.6")
def test_compiles():
    dc = example.compile()
    if not ontravis:
        dc.tofile("tests/compiled.py")

@pytest.mark.skipif(not supportscompiler, reason="compiler requires Python 3.6")
def test_parsesbuilds():
    d = example
    d.testcompiled(data)

@pytest.mark.skipif(not supportscompiler, reason="compiler requires Python 3.6")
def test_overall_compiling(benchmark):
    d = example
    benchmark(d.compile)

@pytest.mark.skipif(not supportscompiler, reason="compiler requires Python 3.6")
def test_overall_parse(benchmark):
    d = example
    benchmark(d.parse, data)

@pytest.mark.skipif(not supportscompiler, reason="compiler requires Python 3.6")
def test_overall_parse_compiled(benchmark):
    dc = example.compile()
    benchmark(dc.parse, data)

@pytest.mark.skipif(not supportscompiler, reason="compiler requires Python 3.6")
def test_overall_build(benchmark):
    d = example
    obj = d.parse(data)
    benchmark(d.build, obj)

@pytest.mark.skipif(not supportscompiler, reason="compiler requires Python 3.6")
def test_overall_build_compiled(benchmark):
    dc = example.compile()
    obj = dc.parse(data)
    benchmark(dc.build, obj)
