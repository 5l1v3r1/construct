import declarativeunittest

from construct import *
from construct.lib import LazyContainer
from construct.lib.py3compat import *

import zlib
import codecs

try:
    codecs.lookup("zlib")
    zlibcodecraises = None
except LookupError:
    zlibcodecraises = LookupError



class TestAll(declarativeunittest.TestCase):
    alltests = [

        [Byte.parse, b"\x00", 0, None],
        [Byte.build, 0, b"\x00", None],
        [Byte.parse, b"\xff", 255, None],
        [Byte.build, 255, b"\xff", None],
        [Byte.sizeof, None, 1, None],

        [UBInt8.parse, b"\x01", 0x01, None],
        [UBInt8.build, 0x01, b"\x01", None],
        [UBInt8.sizeof, None, 1, None],
        [UBInt16.parse, b"\x01\x02", 0x0102, None],
        [UBInt16.build, 0x0102, b"\x01\x02", None],
        [UBInt16.sizeof, None, 2, None],
        [UBInt32.parse, b"\x01\x02\x03\x04", 0x01020304, None],
        [UBInt32.build, 0x01020304, b"\x01\x02\x03\x04", None],
        [UBInt32.sizeof, None, 4, None],
        [UBInt64.parse, b"\x01\x02\x03\x04\x05\x06\x07\x08", 0x0102030405060708, None],
        [UBInt64.build, 0x0102030405060708, b"\x01\x02\x03\x04\x05\x06\x07\x08", None],
        [UBInt64.sizeof, None, 8, None],
        [SBInt8.parse, b"\x01", 0x01, None],
        [SBInt8.build, 0x01, b"\x01", None],
        [SBInt8.sizeof, None, 1, None],
        [SBInt16.parse, b"\x01\x02", 0x0102, None],
        [SBInt16.build, 0x0102, b"\x01\x02", None],
        [SBInt16.sizeof, None, 2, None],
        [SBInt32.parse, b"\x01\x02\x03\x04", 0x01020304, None],
        [SBInt32.build, 0x01020304, b"\x01\x02\x03\x04", None],
        [SBInt32.sizeof, None, 4, None],
        [SBInt64.parse, b"\x01\x02\x03\x04\x05\x06\x07\x08", 0x0102030405060708, None],
        [SBInt64.build, 0x0102030405060708, b"\x01\x02\x03\x04\x05\x06\x07\x08", None],
        [SBInt64.sizeof, None, 8, None],
        [ULInt8.parse, b"\x01", 0x01, None],
        [ULInt8.build, 0x01, b"\x01", None],
        [ULInt8.sizeof, None, 1, None],
        [ULInt16.parse, b"\x01\x02", 0x0201, None],
        [ULInt16.build, 0x0201, b"\x01\x02", None],
        [ULInt16.sizeof, None, 2, None],
        [ULInt32.parse, b"\x01\x02\x03\x04", 0x04030201, None],
        [ULInt32.build, 0x04030201, b"\x01\x02\x03\x04", None],
        [ULInt32.sizeof, None, 4, None],
        [ULInt64.parse, b"\x01\x02\x03\x04\x05\x06\x07\x08", 0x0807060504030201, None],
        [ULInt64.build, 0x0807060504030201, b"\x01\x02\x03\x04\x05\x06\x07\x08", None],
        [ULInt64.sizeof, None, 8, None],
        [SLInt8.parse, b"\x01", 0x01, None],
        [SLInt8.build, 0x01, b"\x01", None],
        [SLInt8.sizeof, None, 1, None],
        [SLInt16.parse, b"\x01\x02", 0x0201, None],
        [SLInt16.build, 0x0201, b"\x01\x02", None],
        [SLInt16.sizeof, None, 2, None],
        [SLInt32.parse, b"\x01\x02\x03\x04", 0x04030201, None],
        [SLInt32.build, 0x04030201, b"\x01\x02\x03\x04", None],
        [SLInt32.sizeof, None, 4, None],
        [SLInt64.parse, b"\x01\x02\x03\x04\x05\x06\x07\x08", 0x0807060504030201, None],
        [SLInt64.build, 0x0807060504030201, b"\x01\x02\x03\x04\x05\x06\x07\x08", None],
        [SLInt64.sizeof, None, 8, None],

        [UBInt24.parse, b"\x01\x02\x03", 0x010203, None],
        [UBInt24.build, 0x010203, b"\x01\x02\x03", None],
        [UBInt24.sizeof, None, 3, None],
        [Struct('int24' / UBInt24).parse, b"\x01\x02\x03", Container(int24=0x010203), None],
        [Struct('int24' / UBInt24).build, Container(int24=0x010203), b"\x01\x02\x03", None],
        [Struct('int24' / UBInt24).sizeof, None, 3, None],
        [ULInt24.parse, b"\x01\x02\x03", 0x030201, None],
        [ULInt24.build, 0x030201, b"\x01\x02\x03", None],
        [ULInt24.sizeof, None, 3, None],
        [Struct('int24' / ULInt24).parse, b"\x01\x02\x03", Container(int24=0x030201), None],
        [Struct('int24' / ULInt24).build, Container(int24=0x030201), b"\x01\x02\x03", None],
        [Struct('int24' / ULInt24).sizeof, None, 3, None],

        [VarInt.parse, b"\x05", 5, None],
        [VarInt.parse, b"\x85\x05", 645, None],
        [VarInt.build, 5, b"\x05", None],
        [VarInt.build, 645, b"\x85\x05", None],
        [VarInt.parse, b"", None, FieldError],
        [VarInt.build, -1, None, ValueError],
        [VarInt.sizeof, None, None, SizeofError],

        [Bytes(4).parse, b"12345678", b"1234", None],
        [Bytes(4).build, b"1234", b"1234", None],
        [Bytes(4).parse, b"", None, FieldError],
        [Bytes(4).build, b"toolong", None, FieldError],
        # issue #99
        # [Bytes(4).build, 1, None, FieldError],
        # [Bytes(4).build, 0x01020304, None, FieldError],
        [Bytes(4).sizeof, None, 4, None],

        [Bytes(lambda ctx: ctx.n).parse, (b"12345678",Container(n=4)), b"1234", None],
        [Bytes(lambda ctx: ctx.n).build, (b"1234",Container(n=4)), b"1234", None],
        # issue #99
        # [Bytes(lambda ctx: ctx.n).build, (1,Container(n=4)), b"\x00\x00\x00\x01", None],
        [Bytes(lambda ctx: ctx.n).parse, (b"",Container(n=4)), None, FieldError],
        [Bytes(lambda ctx: ctx.n).build, (b"toolong",Container(n=4)), None, FieldError],
        [Bytes(lambda ctx: ctx.n).sizeof, None, None, AttributeError],
        [Bytes(lambda ctx: ctx.n).sizeof, Container(n=4), 4, None],

        [GreedyBytes.parse, b"1234", b"1234", None],
        [GreedyBytes.build, b"1234", b"1234", None],
        [GreedyBytes.sizeof, None, None, SizeofError],

        [FormatField("<","L").parse, b"\x12\x34\x56\x78", 0x78563412, None],
        [FormatField("<","L").build, 0x78563412, b"\x12\x34\x56\x78", None],
        # issue #115
        # [FormatField("<","L").parse, b"\x12\x34\x56", '\x00\x00\x00\x00', FieldError if not PY26 else None],
        [FormatField("<","L").parse, b"\x12\x34\x56", None, FieldError],
        # issue #115
        # [FormatField("<","L").build, 2**100, None, FieldError if not PY26 else None],
        [FormatField("<","L").build, 9e9999, None, FieldError],
        [FormatField("<","L").build, "string not int", None, FieldError],
        [FormatField("<","L").sizeof, None, 4, None],

        [Array(3,Byte).parse, b"\x01\x02\x03", [1,2,3], None],
        [Array(3,Byte).parse, b"\x01\x02\x03additionalgarbage", [1,2,3], None],
        # issue #101
        # [Array(3,Byte).parse, b"", [1,2,3], ArrayError],
        [Array(3,Byte).build, [1,2,3], b"\x01\x02\x03", None],
        [Array(3,Byte).build, [1,2], None, ArrayError],
        [Array(3,Byte).build, [1,2,3,4,5,6,7,8], None, ArrayError],
        [Array(3,Byte).sizeof, None, 3, None],

        [Array(lambda ctx: 3, Byte).parse, (b"\x01\x02\x03",Container(n=3)), [1,2,3], None],
        [Array(lambda ctx: 3, Byte).parse, (b"\x01\x02\x03additionalgarbage",Container(n=3)), [1,2,3], None],
        # issue #101
        # [Array(lambda ctx: 3, Byte).parse, (b"",Container(n=3)), None, ArrayError],
        [Array(lambda ctx: 3, Byte).build, ([1,2,3],Container(n=3)), b"\x01\x02\x03", None],
        [Array(lambda ctx: 3, Byte).build, ([1,2],Container(n=3)), None, ArrayError],
        [Array(lambda ctx: ctx.n, Byte).parse, (b"\x01\x02\x03",Container(n=3)), [1,2,3], None],
        [Array(lambda ctx: ctx.n, Byte).build, ([1,2,3],Container(n=3)), b"\x01\x02\x03", None],
        [Array(lambda ctx: ctx.n, Byte).sizeof, None, None, AttributeError],
        [Array(lambda ctx: ctx.n, Byte).sizeof, Container(n=4), 4, None],

        [PrefixedArray(Byte,Byte).parse, b"\x02\x0a\x0b", [10,11], None],
        [PrefixedArray(Byte,Byte).build, [10,11], b"\x02\x0a\x0b", None],
        [PrefixedArray(Byte,Byte).sizeof, None, None, SizeofError],

        [Range(3, 5, Byte).parse, b"\x01\x02\x03", [1,2,3], None],
        [Range(3, 5, Byte).parse, b"\x01\x02\x03\x04", [1,2,3,4], None],
        [Range(3, 5, Byte).parse, b"\x01\x02\x03\x04\x05", [1,2,3,4,5], None],
        [Range(3, 5, Byte).parse, b"\x01\x02\x03\x04\x05\x06", [1,2,3,4,5], None],
        [Range(3, 5, Byte).parse, b"", None, RangeError],
        [Range(3, 5, Byte).build, [1,2,3], b"\x01\x02\x03", None],
        [Range(3, 5, Byte).build, [1,2,3,4], b"\x01\x02\x03\x04", None],
        [Range(3, 5, Byte).build, [1,2,3,4,5], b"\x01\x02\x03\x04\x05", None],
        [Range(3, 5, Byte).build, [1,2], None, RangeError],
        [Range(3, 5, Byte).build, [1,2,3,4,5,6], None, RangeError],
        [Range(3, 5, Byte).build, 0, None, RangeError],
        [Range(3, 5, Byte).sizeof, None, None, SizeofError],

        [Range(0,100,Struct("id"/Byte)).parse, b'\x01\x02', [Container(id=1),Container(id=2)], None],
        [Range(0,100,Struct("id"/Byte)).build, [dict(id=i) for i in range(5)], b'\x00\x01\x02\x03\x04', None],
        [Range(0,100,Struct("id"/Byte)).build, dict(id=1), None, RangeError],
        [Range(0,100,Struct("id"/Byte)).sizeof, None, None, SizeofError],
        [lambda none: Range(-2,+7,Byte), None, None, RangeError],
        [lambda none: Range(-2,-7,Byte), None, None, RangeError],
        [lambda none: Range(+2,-7,Byte), None, None, RangeError],

        [GreedyRange(Byte).parse, b"", [], None],
        [GreedyRange(Byte).build, [], b"", None],
        [GreedyRange(Byte).parse, b"\x01\x02", [1,2], None],
        [GreedyRange(Byte).build, [1,2], b"\x01\x02", None],
        [GreedyRange(Byte).sizeof, None, None, SizeofError],

        [RepeatUntil(lambda obj,ctx: obj == 9, Byte).parse, b"\x02\x03\x09garbage", [2,3,9], None],
        [RepeatUntil(lambda obj,ctx: obj == 9, Byte).parse, b"\x02\x03\x08", None, ArrayError],
        [RepeatUntil(lambda obj,ctx: obj == 9, Byte).build, [2,3,9,1,1,1], b"\x02\x03\x09", None],
        [RepeatUntil(lambda obj,ctx: obj == 9, Byte).build, [2,3,8], None, ArrayError],
        [RepeatUntil(lambda obj,ctx: obj == 9, Byte).sizeof, None, None, SizeofError],

        [Struct("a" / ULInt16, "b" / Byte).parse, b"\x01\x00\x02", Container(a=1)(b=2), None],
        [Struct("a" / ULInt16, "b" / Byte).build, Container(a=1)(b=2), b"\x01\x00\x02", None],
        [Struct("a" / Byte, "b" / UBInt16, "inner" / Struct("c" / Byte, "d" / Byte)).parse, b"\x01\x00\x02\x03\x04", Container(a=1)(b=2)(inner=Container(c=3)(d=4)), None],
        [Struct("a" / Byte, "b" / UBInt16, "inner" / Struct("c" / Byte, "d" / Byte)).build, Container(a=1)(b=2)(inner=Container(c=3)(d=4)), b"\x01\x00\x02\x03\x04", None],
        [Struct("a" / Byte, "b" / UBInt16, Embedded("inner" / Struct("c" / Byte, "d" / Byte))).parse, b"\x01\x00\x02\x03\x04", Container(a=1)(b=2)(c=3)(d=4), None],
        [Struct("a" / Byte, "b" / UBInt16, Embedded("inner" / Struct("c" / Byte, "d" / Byte))).build, Container(a=1)(b=2)(c=3)(d=4), b"\x01\x00\x02\x03\x04", None],
        [Struct("a"/Struct("b"/Byte)).parse, b"\x01", Container(a=Container(b=1)), None],
        [Struct("a"/Struct("b"/Byte)).build, Container(a=Container(b=1)), b"\x01", None],
        [Struct("a"/Struct("b"/Byte)).sizeof, None, 1, None],
        [Struct("missingkey"/Byte).build, dict(), None, KeyError],
        [Struct("a"/Byte, "a"/VarInt, "a"/Pass).build, dict(a=1), b"\x01\x01", None],

        [Struct(Padding(2)).parse, b"\x00\x00", Container(), None],
        [Struct(Padding(2)).build, Container(), b"\x00\x00", None],
        [Struct(Padding(2)).sizeof, None, 2, None],

        [Sequence(UBInt8, UBInt16).parse, b"\x01\x00\x02", [1,2], None],
        [Sequence(UBInt8, UBInt16).build, [1,2], b"\x01\x00\x02", None],
        [Sequence(UBInt8, UBInt16, Sequence(UBInt8, UBInt8)).parse, b"\x01\x00\x02\x03\x04", [1,2,[3,4]], None],
        [Sequence(UBInt8, UBInt16, Sequence(UBInt8, UBInt8)).build, [1,2,[3,4]], b"\x01\x00\x02\x03\x04", None],
        [Sequence(UBInt8, UBInt16, Embedded(Sequence(UBInt8, UBInt8))).parse, b"\x01\x00\x02\x03\x04", [1,2,3,4], None],
        [Sequence(UBInt8, UBInt16, Embedded(Sequence(UBInt8, UBInt8))).build, [1,2,3,4], b"\x01\x00\x02\x03\x04", None],

        [Computed(lambda ctx: "moo").parse, b"", "moo", None],
        [Computed(lambda ctx: "moo").build, None, b"", None],
        [Computed(lambda ctx: "moo").sizeof, None, 0, None],
        [Struct("c" / Computed(lambda ctx: "moo")).parse, b"", Container(c="moo"), None],
        [Struct("c" / Computed(lambda ctx: "moo")).build, Container(c=None), b"", None],
        [Struct("c" / Computed(lambda ctx: "moo")).build, Container(), b"", None],
        [Computed(lambda ctx: ctx.missing).parse, None, None, AttributeError],
        [Computed(lambda ctx: ctx["missing"]).parse, None, None, KeyError],

        [RawCopy(Byte).parse, b"\xff", dict(data=b"\xff", value=255, offset1=0, offset2=1, length=1), None],
        [RawCopy(Byte).build, dict(data=b"\xff"), b"\xff", None],
        [RawCopy(Byte).build, dict(value=255), b"\xff", None],
        [RawCopy(Byte).sizeof, None, 1, None],

        [Anchor.parse, b"", 0, None],
        [Anchor.build, None, b"", None],
        [Anchor.sizeof, None, 0, None],
        [Struct("a"/Anchor, "b"/Byte, "c"/Anchor).parse, b"\xff", Container(a=0)(b=255)(c=1), None],
        [Struct("a"/Anchor, "b"/Byte, "c"/Anchor).build, Container(a=0)(b=255)(c=1), b"\xff", None],
        [Struct("a"/Anchor, "b"/Byte, "c"/Anchor).build, dict(b=255), b"\xff", None],

        # [AnchorRange.parse, b"", 0, None],
        # [AnchorRange.build, None, b"", None],
        # [AnchorRange.sizeof, None, 0, None],
        # [Struct("anchorrange"/AnchorRange, "a"/Byte, "anchorrange"/AnchorRange).parse, b"\xff", Container(anchorrange=Container(offset1=0)(offset2=1)(length=1))(a=255), None],
        # [Struct("anchorrange"/AnchorRange, "a"/Byte, "anchorrange"/AnchorRange).build, dict(a=255), b"\xff", None],

        [Pass.parse, b"", None, None],
        [Pass.build, None, b"", None],
        [Pass.sizeof, None, 0, None],
        [Struct("pass"/Pass).build, dict(), b"", None],

        [Terminator.parse, b"", None, None],
        [Terminator.parse, b"x", None, TerminatorError],
        [Terminator.build, None, b"", None],
        [Terminator.sizeof, None, 0, None],
        [Struct("end"/Terminator).build, dict(), b"", None],

        [Pointer(lambda ctx: 2, "pointer" / UBInt8).parse, b"\x00\x00\x07", 7, None],
        [Pointer(lambda ctx: 2, "pointer" / UBInt8).build, 7, b"\x00\x00\x07", None],
        [Pointer(lambda ctx: 2, "pointer" / UBInt8).sizeof, None, 0, None],

        [Const(b"MZ").parse, b"MZ", b"MZ", None],
        [Const(b"MZ").parse, b"ELF", None, ConstError],
        [Const(b"MZ").build, None, b"MZ", None],
        [Const(b"MZ").build, b"MZ", b"MZ", None],
        [Const(b"MZ").sizeof, None, 2, None],
        [Const(ULInt32, 255).parse, b"\xff\x00\x00\x00", 255, None],
        [Const(ULInt32, 255).parse, b"\x00\x00\x00\x00", 255, ConstError],
        [Const(ULInt32, 255).build, None, b"\xff\x00\x00\x00", None],
        [Const(ULInt32, 255).build, 255, b"\xff\x00\x00\x00", None],
        [Const(ULInt32, 255).sizeof, None, 4, None],
        [Struct("sig" / Const(b"MZ")).parse, b"MZ", Container(sig=b"MZ"), None],
        [Struct("sig" / Const(b"MZ")).build, Container(sig=b"MZ"), b"MZ", None],
        [Struct("sig" / Const(b"MZ")).build, Container(), b"MZ", None],
        [Struct("sig" / Const(b"MZ")).sizeof, None, 2, None],

        [Switch(lambda ctx: 5, {1:Byte, 5:UBInt16}).parse, b"\x00\x02", 2, None],
        [Switch(lambda ctx: 6, {1:Byte, 5:UBInt16}).parse, b"\x00\x02", None, SwitchError],
        [Switch(lambda ctx: 6, {1:Byte, 5:UBInt16}, default=Byte).parse, b"\x00\x02", 0, None],
        [Switch(lambda ctx: 5, {1:Byte, 5:UBInt16}, include_key=True).parse, b"\x00\x02", (5, 2), None],
        [Switch(lambda ctx: 5, {1:Byte, 5:UBInt16}).build, 2, b"\x00\x02", None],
        [Switch(lambda ctx: 6, {1:Byte, 5:UBInt16}).build, 9, None, SwitchError],
        [Switch(lambda ctx: 6, {1:Byte, 5:UBInt16}, default=Byte).build, 9, b"\x09", None],
        [Switch(lambda ctx: 5, {1:Byte, 5:UBInt16}, include_key=True).build, ((5, 2),), b"\x00\x02", None],
        [Switch(lambda ctx: 5, {1:Byte, 5:UBInt16}, include_key=True).build, ((89, 2),), None, SwitchError],
        [Switch(lambda ctx: 5, {1:Byte, 5:UBInt16}).sizeof, None, None, SizeofError],

        [IfThenElse(lambda ctx: True,  UBInt8, UBInt16).parse, b"\x01", 1, None],
        [IfThenElse(lambda ctx: False, UBInt8, UBInt16).parse, b"\x00\x01", 1, None],
        [IfThenElse(lambda ctx: True,  UBInt8, UBInt16).build, 1, b"\x01", None],
        [IfThenElse(lambda ctx: False, UBInt8, UBInt16).build, 1, b"\x00\x01", None],
        [IfThenElse(lambda ctx: False, UBInt8, UBInt16).sizeof, None, None, SizeofError],

        [If(lambda ctx: True,  UBInt8).parse, b"\x01", 1, None],
        [If(lambda ctx: False, UBInt8).parse, b"", None, None],
        [If(lambda ctx: True,  UBInt8).build, 1, b"\x01", None],
        [If(lambda ctx: False, UBInt8).build, None, b"", None],
        [If(lambda ctx: False, UBInt8).sizeof, None, None, SizeofError],

        [Padding(4).parse, b"\x00\x00\x00\x00", None, None],
        [Padding(4).build, None, b"\x00\x00\x00\x00", None],
        [Padding(4).sizeof, None, 4, None],
        [Padding(4, strict=True).parse, b"\x00\x00\x00\x00", None, None],
        [Padding(4, strict=True).parse, b"????", None, PaddingError],
        [Padding(4, strict=True).build, None, b"\x00\x00\x00\x00", None],
        [Padding(4, pattern=b'x', strict=True).parse, b"xxxx", None, None],
        [Padding(4, pattern=b'x', strict=True).parse, b"????", None, PaddingError],
        [lambda none: Padding(4, pattern=b"??"), None, None, PaddingError],
        [lambda none: Padding(4, pattern=u"?"), None, None, PaddingError],

        [Padded(4, Byte).parse, b"\x01\x00\x00\x00", 1, None],
        [Padded(4, Byte).build, 1, b"\x01\x00\x00\x00", None],
        [Padded(4, Byte).sizeof, None, 4, None],
        [Padded(4, Byte, strict=True).parse, b"\x01\x00\x00\x00", 1, None],
        [Padded(4, Byte, strict=True).parse, b"\x01???", None, PaddingError],
        [Padded(4, Byte, strict=True).build, 1, b"\x01\x00\x00\x00", None],
        [Padded(4, Byte, pattern=b'x', strict=True).parse, b"\x01xxx", 1, None],
        [Padded(4, Byte, pattern=b'x', strict=True).parse, b"\x01???", None, PaddingError],
        [lambda none: Padded(4, Byte, pattern=b"??"), None, None, PaddingError],
        [lambda none: Padded(4, Byte, pattern=u"?"), None, None, PaddingError],

        [Aligned(Byte, modulus=4).parse, b"\x01\x00\x00\x00", 1, None],
        [Aligned(Byte, modulus=4).build, 1, b"\x01\x00\x00\x00", None],
        [Aligned(Byte, modulus=4).sizeof, None, 4, None],
        [Struct(Aligned("a"/Byte, modulus=4), "b"/Byte).parse, b"\x01\x00\x00\x00\x02", Container(a=1)(b=2), None],
        [Struct(Aligned("a"/Byte, modulus=4), "b"/Byte).build, Container(a=1)(b=2), b"\x01\x00\x00\x00\x02", None],
        [Struct(Aligned("a"/Byte, modulus=4), "b"/Byte).sizeof, None, 5, None],

        # closed issue #87, both b-string and u-string names
        [("string_name" / Byte).parse, b"\x01", 1, None],
        [(u"unicode_name" / Byte).parse, b"\x01", 1, None],
        [(b"bytes_name" / Byte).parse, b"\x01", 1, None],
        [(None / Byte).parse, b"\x01", 1, None],

        # testing / >> [] operators
        [Struct("new" / ("old" / Byte)).parse, b"\x01", Container(new=1), None],
        [Struct("new" / ("old" / Byte)).build, Container(new=1), b"\x01", None],
        [Byte[4].parse, b"\x01\x02\x03\x04", [1,2,3,4], None],
        [Byte[4].build, [1,2,3,4], b"\x01\x02\x03\x04", None],
        [Byte[2:3].parse, b"\x01", None, RangeError],
        [Byte[2:3].parse, b"\x01\x02", [1,2], None],
        [Byte[2:3].parse, b"\x01\x02\x03", [1,2,3], None],
        [Byte[2:3].parse, b"\x01\x02\x03", [1,2,3], None],
        [Byte[2:3].parse, b"\x01\x02\x03\x04", [1,2,3], None],
        [Struct("nums" / Byte[4]).parse, b"\x01\x02\x03\x04", Container(nums=[1,2,3,4]), None],
        [Struct("nums" / Byte[4]).build, Container(nums=[1,2,3,4]), b"\x01\x02\x03\x04", None],
        [(UBInt8 >> UBInt16).parse, b"\x01\x00\x02", [1,2], None],
        [(UBInt8 >> UBInt16 >> UBInt32).parse, b"\x01\x00\x02\x00\x00\x00\x03", [1,2,3], None],
        [(UBInt8[2] >> UBInt16[2]).parse, b"\x01\x02\x00\x03\x00\x04", [[1,2],[3,4]], None],

        # testing underlying Renamed
        [Struct(Renamed("new",Renamed("old",Byte))).parse, b"\x01", Container(new=1), None],
        [Struct(Renamed("new",Renamed("old",Byte))).build, Container(new=1), b"\x01", None],

        [Alias("b","a").parse, (b"",Container(a=1)), 1, None],
        [Alias("b","a").build, (None,Container(a=1)), b"", None],
        [Alias("b","a").sizeof, None, 0, None],
        [Struct("a"/Byte, Alias("b","a")).parse, b"\x01", Container(a=1)(b=1), None],
        [Struct("a"/Byte, Alias("b","a")).build, dict(a=1), b"\x01", None],
        [Struct("a"/Byte, Alias("b","a")).sizeof, None, 1, None],

        [BitField(8).parse, b"\x01\x01\x01\x01\x01\x01\x01\x01", 255, None],
        [BitField(8).build, 255, b"\x01\x01\x01\x01\x01\x01\x01\x01", None],
        [BitField(8).sizeof, None, 8, None],
        [BitField(8, signed=True).parse, b"\x01\x01\x01\x01\x01\x01\x01\x01", -1, None],
        [BitField(8, signed=True).build, -1, b"\x01\x01\x01\x01\x01\x01\x01\x01", None],
        [BitField(8, swapped=True, bytesize=4).parse, b"\x01\x01\x01\x01\x00\x00\x00\x00", 0x0f, None],
        [BitField(8, swapped=True, bytesize=4).build, 0x0f, b"\x01\x01\x01\x01\x00\x00\x00\x00", None],
        [BitField(lambda ctx: 8).parse, b"\x01" * 8, 255, None],
        [BitField(lambda ctx: 8).build, 255, b"\x01" * 8, None],
        [BitField(lambda ctx: 8).sizeof, None, 8, None],

        [Bitwise(Bytes(8)).parse, b"\xff", b"\x01\x01\x01\x01\x01\x01\x01\x01", None],
        [Bitwise(Bytes(8)).build, b"\x01\x01\x01\x01\x01\x01\x01\x01", b"\xff", None],
        [Bitwise(Bytes(8)).sizeof, None, 1, None],
        [Bitwise(Bytes(lambda ctx: 8)).parse, b"\xff", b"\x01\x01\x01\x01\x01\x01\x01\x01", None],
        [Bitwise(Bytes(lambda ctx: 8)).build, b"\x01\x01\x01\x01\x01\x01\x01\x01", b"\xff", None],
        [Bitwise(Bytes(lambda ctx: 8)).sizeof, None, 1, None],

        [BitStruct("a"/BitField(3), "b"/Flag, Padding(3), "c"/Nibble, "d"/BitField(5)).parse, b"\xe1\x1f", Container(a=7)(b=False)(c=8)(d=31), None],
        [BitStruct("a"/BitField(3), "b"/Flag, Padding(3), "c"/Nibble, "d"/BitField(5)).sizeof, None, 2, None],
        [BitStruct("a"/BitField(3), "b"/Flag, Padding(3), "c"/Nibble, "sub"/Struct("d"/Nibble, "e"/Bit)).parse, b"\xe1\x1f", Container(a=7)(b=False)(c=8)(sub=Container(d=15)(e=1)), None],
        [BitStruct("a"/BitField(3), "b"/Flag, Padding(3), "c"/Nibble, "sub"/Struct("d"/Nibble, "e"/Bit)).sizeof, None, 2, None],
        # issue #113
        # [BitStruct("a"/BitField(3), "b"/Flag, Padding(3), "c"/Nibble, "d"/BitField(5)).build, Container(a=7)(b=False)(c=8)(d=31), b"\xe1\x1f", None],
        # [BitStruct("a"/BitField(3), "b"/Flag, Padding(3), "c"/Nibble, "sub"/Struct("d"/Nibble, "e"/Bit)).build, Container(a=7)(b=False)(c=8)(sub=Container(d=15)(e=1)), b"\xe1\x1f", None],

        [Bitwise(Array(8,Bit)).parse, b"\xff", [1,1,1,1,1,1,1,1], None],
        [Bitwise(Array(2,Nibble)).parse, b"\xff", [15,15], None],
        [Bitwise(Array(1,Octet)).parse, b"\xff", [255], None],
        # issue #113
        # [Bitwise(Array(8,Bit)).build, [1,1,1,1,1,1,1,1], b"\xff", None],
        # [Bitwise(Array(2,Nibble)).build, [15,15], b"\xff", None],
        # [Bitwise(Array(1,Octet)).build, [255], b"\xff", None],

        [ByteSwapped(Bytes(5)).parse, b"12345?????", b"54321", None],
        [ByteSwapped(Bytes(5)).build, b"12345", b"54321", None],
        [ByteSwapped(Bytes(5)).sizeof, None, 5, None],
        [ByteSwapped(Struct("a"/Byte,"b"/Byte)).parse, b"\x01\x02", Container(a=2)(b=1), None],
        [ByteSwapped(Struct("a"/Byte,"b"/Byte)).build, Container(a=2)(b=1), b"\x01\x02", None],
        [ByteSwapped(Bytes(5), size=4).parse, b"54321", None, FieldError],
        # closed issue #70
        [ByteSwapped(BitStruct("flag1"/Bit, "flag2"/Bit, Padding(2), "number"/BitField(16), Padding(4))).parse, b'\xd0\xbc\xfa', Container(flag1=1)(flag2=1)(number=0xabcd), None],
        [BitStruct("flag1"/Bit, "flag2"/Bit, Padding(2), "number"/BitField(16), Padding(4)).parse, b'\xfa\xbc\xd1', Container(flag1=1)(flag2=1)(number=0xabcd), None],

        [Slicing(Array(4,Byte), 4, 1, 3, empty=0).parse, b"\x01\x02\x03\x04", [2,3], None],
        [Slicing(Array(4,Byte), 4, 1, 3, empty=0).build, [2,3], b"\x00\x02\x03\x00", None],
        [Slicing(Array(4,Byte), 4, 1, 3, empty=0).sizeof, None, 4, None],

        [Indexing(Array(4,Byte), 4, 2, empty=0).parse, b"\x01\x02\x03\x04", 3, None],
        [Indexing(Array(4,Byte), 4, 2, empty=0).build, 3, b"\x00\x00\x03\x00", None],
        [Indexing(Array(4,Byte), 4, 2, empty=0).sizeof, None, 4, None],

        [Select(UBInt32, UBInt16).parse, b"\x07", None, SelectError],
        [Select(UBInt32, UBInt16, UBInt8).parse, b"\x07", 7, None],
        [Select(UBInt32, UBInt16, UBInt8).build, 7, b"\x00\x00\x00\x07", None],
        [Select(UBInt32, UBInt16, UBInt8).sizeof, None, None, SizeofError],
        [Select("a"/UBInt32, "b"/UBInt16, "c"/UBInt8, includename=True).parse, b"\x07", ("c", 7), None],
        [Select("a"/UBInt32, "b"/UBInt16, "c"/UBInt8, includename=True).build, (("c", 7),), b"\x07", None],
        [Select("a"/UBInt32, "b"/UBInt16, "c"/UBInt8, includename=True).build, (("d", 7),), None, SelectError],
        [Select("a"/UBInt32, "b"/UBInt16, "c"/UBInt8, includename=True).sizeof, None, None, SizeofError],

        [Peek(UBInt8).parse, b"\x01", 1, None],
        [Peek(UBInt8).parse, b"", None, None],
        [Peek(UBInt8).build, 1, b"", None],
        [Peek(UBInt8).build, None, b"", None],
        [Peek(UBInt8).sizeof, None, 0, None],
        [Peek(VarInt).sizeof, None, 0, None],
        [Struct(Peek("a"/UBInt8), "b"/UBInt16).parse, b"\x01\x02", Container(a=1)(b=0x0102), None],
        [Struct(Peek("a"/UBInt8), "b"/UBInt16).build, dict(a=1,b=0x0102), b"\x01\x02", None],
        [Struct(Peek("a"/Byte), Peek("b"/UBInt16),).parse, b"\x01\x02", Container(a=1)(b=0x0102), None],
        [Struct(Peek("a"/Byte), Peek("b"/UBInt16),).build, dict(a=0,b=0x0102), b"", None],
        [Struct(Peek("a"/Byte), Peek("b"/UBInt16),).sizeof, None, 0, None],

        [Optional(ULInt32).parse, b"\x01\x00\x00\x00", 1, None],
        [Optional(ULInt32).build, 1, b"\x01\x00\x00\x00", None],
        [Optional(ULInt32).parse, b"?", None, None],
        [Optional(ULInt32).build, None, b"", None],
        # issue #104
        # [Optional(ULInt32).sizeof, None, 0, None],

        [Union("a"/UBInt16, "b"/Struct("b1"/UBInt8, "b2"/UBInt8)).parse, b"\x01\x02", Container(a=0x0102)(b=Container(b1=1)(b2=2)), None],
        [Union("a"/UBInt16, "b"/Struct("b1"/UBInt8, "b2"/UBInt8)).build, dict(a=0x0102,b=dict(b1=1,b2=2)), b"\x01\x02", None],
        [Union("sub1"/Struct("a"/UBInt8, "b"/UBInt8), "sub2"/Struct("c"/ULInt16), ).build, dict(sub1=dict(a=1,b=2)), b"\x01\x02", None],
        [Union("sub1"/Struct("a"/UBInt8, "b"/UBInt8), "sub2"/Struct("c"/ULInt16), ).build, dict(sub2=dict(c=3)), b"\x03\x00", None],
        [Union("a"/UBInt8, "b"/UBInt16, buildfrom=0).build, dict(a=1,b=2), b"\x01", None],
        [Union("a"/UBInt8, "b"/UBInt16, buildfrom=1).build, dict(a=1,b=2), b"\x00\x02", None],
        [Union(Embedded("sub1"/Struct("a"/Byte, "b"/Byte)), Embedded("sub2"/Struct("c"/UBInt16)), buildfrom="sub1").build, dict(a=1,b=2), b"\x01\x02", None],
        [Union(Embedded("sub1"/Struct("a"/Byte, "b"/Byte)), Embedded("sub2"/Struct("c"/UBInt16)), buildfrom="sub2").build, dict(c=3), b"\x00\x03", None],
        [Union("a"/Byte, "b"/PascalString(Byte), ).build, None, None, SelectError],
        [Union(Byte).sizeof, None, None, SizeofError],
        [Union(VarInt).sizeof, None, None, SizeofError],
        [Union(CString()).sizeof, None, None, SizeofError],

        [PrefixedArray(Byte,Byte).parse, b"\x03\x01\x02\x03", [1,2,3], None],
        [PrefixedArray(Byte,Byte).parse, b"\x00", [], None],
        [PrefixedArray(Byte,Byte).parse, b"", None, ArrayError],
        [PrefixedArray(Byte,Byte).parse, b"\x03\x01", None, ArrayError],
        [PrefixedArray(Byte,Byte).build, [1,2,3], b"\x03\x01\x02\x03", None],
        [PrefixedArray(Byte,Byte).sizeof, None, None, SizeofError],
        [PrefixedArray(Byte,Byte).sizeof, [1,1,1], 4, SizeofError],

        [Prefixed(Byte,ULInt16).parse, b"\x02\xff\xffgarbage", 65535, None],
        [Prefixed(Byte,ULInt16).build, 65535, b"\x02\xff\xff", None],
        [Prefixed(Byte,ULInt16).sizeof, None, None, SizeofError],
        [Prefixed(VarInt,GreedyBytes).parse, b"\x03abcgarbage", b"abc", None],
        [Prefixed(VarInt,GreedyBytes).build, b"abc", b'\x03abc', None],
        [Prefixed(VarInt,GreedyBytes).sizeof, None, None, SizeofError],

        [Prefixed(Byte,Compressed(GreedyBytes,"zlib")).parse, b'\x0cx\x9c30\xa0=\x00\x00\xb3q\x12\xc1???????????', b"0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000", zlibcodecraises],
        [Prefixed(Byte,Compressed(GreedyBytes,"zlib")).build, b"0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000", b'\x0cx\x9c30\xa0=\x00\x00\xb3q\x12\xc1', zlibcodecraises],
        [Prefixed(Byte,Compressed(CString(),"zlib")).parse, b'\rx\x9c30\xa0=`\x00\x00\xc62\x12\xc1??????????????', b"0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000", zlibcodecraises],
        [Prefixed(Byte,Compressed(CString(),"zlib")).build, b"0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000", b'\rx\x9c30\xa0=`\x00\x00\xc62\x12\xc1', zlibcodecraises],
        [Prefixed(Byte,Compressed(CString(),"zlib")).sizeof, None, None, SizeofError],

        [String(5).parse, b"hello", b"hello", None],
        [String(5).build, b"hello", b"hello", None],
        [String(5).parse, b"", None, FieldError],
        [String(5).build, b"", b"\x00\x00\x00\x00\x00", None],
        [String(12, encoding="utf8").parse, b"hello joh\xd4\x83n", u"hello joh\u0503n", None],
        [String(12, encoding="utf8").build, u"hello joh\u0503n", b"hello joh\xd4\x83n", None],
        [String(12, encoding="utf8").sizeof, None, 12, None],
        [String(5).build, u"hello", None, StringError],  # missing encoding
        [String(10, padchar=b"X", paddir="right").parse, b"helloXXXXX", b"hello", None],
        [String(10, padchar=b"X", paddir="left").parse, b"XXXXXhello", b"hello", None],
        [String(10, padchar=b"X", paddir="center").parse, b"XXhelloXXX", b"hello", None],
        [String(10, padchar=b"X", paddir="right").build, b"hello", b"helloXXXXX", None],
        [String(10, padchar=b"X", paddir="left").build, b"hello", b"XXXXXhello", None],
        [String(10, padchar=b"X", paddir="center").build, b"hello", b"XXhelloXXX", None],
        [lambda none: String(10, padchar=u"X"), None, None, StringError],
        [String(5, trimdir="right").build, b"1234567890", b"12345", None],
        [String(5, trimdir="left").build, b"1234567890", b"67890", None],
        [String(5, padchar=b"X", paddir="left", encoding="utf8").sizeof, None, 5, None],
        [String(5).sizeof, None, 5, None],

        [PascalString(Byte).parse, b"\x05hello????????", b"hello", None],
        [PascalString(Byte).build, b"hello", b"\x05hello", None],
        [PascalString(Byte, encoding="utf8").parse, b"\x05hello", u"hello", None],
        [PascalString(Byte, encoding="utf8").build, u"hello", b"\x05hello", None],
        [PascalString(UBInt16).parse, b"\x00\x05hello????????", b"hello", None],
        [PascalString(UBInt16).build, b"hello", b"\x00\x05hello", None],
        [PascalString(Byte).sizeof, None, None, SizeofError],
        [PascalString(VarInt).sizeof, None, None, SizeofError],

        [CString().parse, b"hello\x00", b"hello", None],
        [CString(encoding="utf8").parse, b"hello\x00", u"hello", None],
        [CString().build, b"hello", b"hello\x00", None],
        [CString(encoding="utf8").build, u"hello", b"hello\x00", None],
        [CString(terminators=b"XYZ", encoding="utf8").parse, b"helloX", u"hello", None],
        [CString(terminators=b"XYZ", encoding="utf8").parse, b"helloY", u"hello", None],
        [CString(terminators=b"XYZ", encoding="utf8").parse, b"helloZ", u"hello", None],
        [CString(terminators=b"XYZ", encoding="utf8").build, u"hello", b"helloX", None],
        [CString().sizeof, None, None, SizeofError],
        # issue #111
        # assert CString(encoding="utf16").parse(CString(encoding="utf16").build(u"hello")) == u"hello"

        [GreedyString().parse, b"hello\x00", b"hello\x00", None],
        [GreedyString().parse, b"", b"", None],
        [GreedyString().build, b"hello\x00", b"hello\x00", None],
        [GreedyString().build, b"", b"", None],
        [GreedyString(encoding="utf8").parse, b"hello\x00", u"hello\x00", None],
        [GreedyString(encoding="utf8").parse, b"", u"", None],
        [GreedyString(encoding="utf8").build, u"hello\x00", b"hello\x00", None],
        [GreedyString(encoding="utf8").build, u"", b"", None],
        [GreedyString().sizeof, None, None, SizeofError],

        [LazyBound(lambda ctx: Byte).parse, b"\x01", 1, None],
        [LazyBound(lambda ctx: Byte).build, 1, b"\x01", None],
        [LazyBound(lambda ctx: Byte).sizeof, None, 1, None],

        [Struct("length" / Byte, "inner" / Struct("inner_length" / Byte, "data" / Bytes(lambda ctx: ctx._.length + ctx.inner_length))).parse, b"\x03\x02helloXXX", Container(length=3)(inner=Container(inner_length=2)(data=b"hello")), None],
        [Struct("length" / Byte, "inner" / Struct("inner_length" / Byte, "data" / Bytes(lambda ctx: ctx._.length + ctx.inner_length))).sizeof, Container(inner_length=2)(_=Container(length=3)), 7, None],

        [NoneOf(Byte,[4,5,6,7]).parse, b"\x08", 8, None],
        [NoneOf(Byte,[4,5,6,7]).parse, b"\x06", 8, ValidationError],

        [OneOf(Byte,[4,5,6,7]).parse, b"\x05", 5, None],
        [OneOf(Byte,[4,5,6,7]).parse, b"\x08", 5, ValidationError],
        [OneOf(Byte,[4,5,6,7]).build, 5, b"\x05", None],
        [OneOf(Byte,[4,5,6,7]).build, 8, None, ValidationError],

        [HexDump(Bytes(6)).parse, b'abcdef', '0000   61 62 63 64 65 66                                 abcdef\n', None],
        [HexDump(Bytes(6)).build, b'abcdef', b'abcdef', None],

        [OnDemand(Byte).parse(b"\x01garbage"), None, 1, None],
        [OnDemand(Byte).build, 1, b"\x01", None],
        [OnDemand(Byte).sizeof, None, 1, None],

        [LazyStruct("a"/Byte,"b"/CString()).parse, b"\x01abc\x00", dict(a=1,b=b"abc"), None],
        [LazyStruct("a"/Byte,"b"/CString()).build, dict(a=1,b=b"abc"), b"\x01abc\x00", None],
        [LazyStruct("a"/Byte,"b"/CString()).sizeof, None, None, SizeofError],
        [LazyStruct("a"/Byte).parse, b"\x01", dict(a=1), None],
        [LazyStruct("a"/Byte).build, dict(a=1), b"\x01", None],
        [LazyStruct("a"/Byte).sizeof, None, 1, None],
        [LazyStruct(Pass, Computed(lambda ctx: 0), Terminator).parse, b"", dict(), None],
        [LazyStruct(Pass, Computed(lambda ctx: 0), Terminator).build, dict(), b"", None],
        [LazyStruct(Pass, Computed(lambda ctx: 0), Terminator).sizeof, None, 0, None],
        [LazyStruct("a"/Byte, "b"/LazyStruct("c"/Byte)).parse, b"\x01\x02", dict(a=1,b=dict(c=2)), None],
        [LazyStruct("a"/Byte, "b"/LazyStruct("c"/Byte)).build, dict(a=1,b=dict(c=2)), b"\x01\x02", None],

        [OnDemandPointer(lambda ctx: 2, Byte).parse(b"\x01\x02\x03\x04"), None, 3, None],
        [OnDemandPointer(lambda ctx: 2, Byte).build, 1, b"\x00\x00\x01", None],
        [OnDemandPointer(lambda ctx: 2, Byte).sizeof, None, 0, None],

        # closed issue #76
        [Aligned(Struct("a"/Byte, "f"/Bytes(lambda ctx: ctx.a)), modulus=4).parse, b"\x02\xab\xcd\x00", Container(a=2)(f=b"\xab\xcd"), None],
        [Aligned(Struct("a"/Byte, "f"/Bytes(lambda ctx: ctx.a)), modulus=4).build, Container(a=2)(f=b"\xab\xcd"), b"\x02\xab\xcd\x00", None],

        # [Buffered(UBInt8("buffered"), lambda x:x, lambda x:x, lambda x:x).parse, b"\x07", 7, None],
        # [Buffered(GreedyRange(UBInt8("buffered")), lambda x:x, lambda x:x, lambda x:x).parse, b"\x07", None, SizeofError],
        # [Buffered(UBInt8("buffered"), lambda x:x, lambda x:x, lambda x:x).build, 7, b"\x07", None],
        # [Buffered(GreedyRange(UBInt8("buffered")), lambda x:x, lambda x:x, lambda x:x).build, [7], None, SizeofError],

        # [Restream(UBInt8("restream"), lambda x:x, lambda x:x, lambda x:x).parse, b"\x07", 7, None],
        # [Restream(GreedyRange(UBInt8("restream")), lambda x:x, lambda x:x, lambda x:x).parse, b"\x07", [7], None],
        # [Restream(UBInt8("restream"), lambda x:x, lambda x:x, lambda x:x).parse, b"\x07", 7, None],
        # [Restream(GreedyRange(UBInt8("restream")), lambda x:x, lambda x:x, lambda x:x).parse, b"\x07", [7], None],

        [Flag.parse, b"\x00", False, None],
        [Flag.parse, b"\x01", True, None],
        [Flag.parse, b"\xff", True, None],
        [Flag.build, False, b"\x00", None],
        [Flag.build, True, b"\x01", None],
        [Flag.sizeof, None, 1, None],

        [Enum(Byte,dict(q=3,r=4,t=5)).parse, b"\x04", "r", None],
        [Enum(Byte,dict(q=3,r=4,t=5)).build, "r", b"\x04", None],
        [Enum(Byte,dict(q=3,r=4,t=5)).parse, b"\x07", None, MappingError],
        [Enum(Byte,dict(q=3,r=4,t=5)).build, "spam", None, MappingError],
        [Enum(Byte,dict(q=3,r=4,t=5), default="spam").parse, b"\x07", "spam", None],
        [Enum(Byte,dict(q=3,r=4,t=5), default=9).build, "spam", b"\x09", None],
        [Enum(Byte,dict(q=3,r=4,t=5), default=Pass).parse, b"\x07", 7, None],
        [Enum(Byte,dict(q=3,r=4,t=5), default=Pass).build, 9, b"\x09", None],
        [Enum(Byte,dict(q=3,r=4,t=5)).sizeof, None, 1, None],

        [FlagsEnum(Byte, dict(a=1,b=2,c=4,d=8,e=16,f=32,g=64,h=128)).parse, b'\x81', FlagsContainer(a=True, b=False,c=False,d=False,e=False,f=False,g=False,h=True), None],
        [FlagsEnum(Byte, dict(a=1,b=2,c=4,d=8,e=16,f=32,g=64,h=128)).build, FlagsContainer(a=True, b=False,c=False,d=False,e=False,f=False,g=False,h=True), b'\x81', None],
        [FlagsEnum(Byte, dict(feature=4,output=2,input=1)).parse, b'\x04', FlagsContainer(output=False,feature=True,input=False), None],
        [FlagsEnum(Byte, dict(feature=4,output=2,input=1)).build, dict(feature=True, output=True, input=False), b'\x06', None],
        [FlagsEnum(Byte, dict(feature=4,output=2,input=1)).build, dict(feature=True), b'\x04', None],
        [FlagsEnum(Byte, dict(feature=4,output=2,input=1)).build, dict(), b'\x00', None],
        [FlagsEnum(Byte, dict(feature=4,output=2,input=1)).build, dict(unknown=True), None, MappingError],

    ]


MulDiv = ExprAdapter(Byte,
    encoder = lambda obj,ctx: obj // 7,
    decoder = lambda obj,ctx: obj * 7, )

IpAddress = ExprAdapter(Array(4,Byte), 
    encoder = lambda obj,ctx: list(map(int, obj.split("."))),
    decoder = lambda obj,ctx: "{0}.{1}.{2}.{3}".format(*obj), )

class TestAll2(declarativeunittest.TestCase):
    alltests = [

        [MulDiv.parse, b"\x06", 42, None],
        [MulDiv.build, 42, b"\x06", None],
        [MulDiv.sizeof, None, 1, None],

        [IpAddress.parse, b"\x7f\x80\x81\x82", "127.128.129.130", None],
        [IpAddress.build, "127.1.2.3", b"\x7f\x01\x02\x03", None],
        # issue #107
        # [IpAddress.build, "300.1.2.3", None, FieldError if not PY26 else None],
        [IpAddress.sizeof, None, 4, None],
    ]


Node = Struct(
    "value" / UBInt8,
    "next" / LazyBound(lambda ctx: Node), )

# issue #127
# class TestAll3(declarativeunittest.TestCase):
#     alltests = [

#         [Node.parse, b"\x01", None, FieldError],
#     ]


