=================
Transition to 2.9
=================

.. warning:: Construct is undergoing heavy changes at the moment, expect unstable API for about a month.

Overall
=======

**Compilation feature for faster performance!** Read `this chapter <https://construct.readthedocs.io/en/latest/compilation.html>`_ for tutorial, particularly its restrictions section.

**Docstrings of all classes were overhauled.** Check the `Core API pages <https://construct.readthedocs.io/en/latest/index.html#api-reference>`_.


General classes
-----------------

All constructs: `parse build sizeof` methods take context entries ONLY as keyword parameters \*\*kw (see `this page <https://construct.readthedocs.io/en/latest/meta.html>`_)

All constructs: `compile benchmark testcompiled` methods were added (see `this page <https://construct.readthedocs.io/en/latest/compilation.html#compiling-schemas>`_)

All constructs: operator * can be used for docstrings (see `this page <https://construct.readthedocs.io/en/latest/advanced.html#documenting-fields>`_)

Compiled CompilableMacro Decompiled added (used internally)

String* classes require explicit encoding (see `this page <https://construct.readthedocs.io/en/latest/advanced.html#strings>`_)

String* classes apply global encoding during ctor (not during parsing and building)

String* classes (all of them) support UTF16 UTF32 encodings, but String CString dropped some parameters and support only encodings explicitly listed in `possiblestringencodings`

Enum FlagsEnum can merge labels from IntEnum IntFlag (enum34 module), but dropped `default` parameter

Enum FlagsEnum can build from integers and labels (see `this page <https://construct.readthedocs.io/en/latest/advanced.html#mappings>`_)

Enum FlagsEnum expose labels as attributes, as bitwisable strings (see `this page <https://construct.readthedocs.io/en/latest/advanced.html#mappings>`_)

Struct Sequence Union FocusedSeq are nesting context (in parse build and sizeof)

Struct Sequence Union FocusedSeq are supporting new embedding semantics (see `this page <https://construct.readthedocs.io/en/latest/meta.html#nesting-and-embedding>`_)

EmbeddedBitStruct removed

Array reimplemented without Range, does not use stream.tell()

Range removed, GreedyRange remains

Index added, in Miscellaneous

Pickled added, in Miscellaneous

Hex HexDump reimplemented (see `this page <https://construct.readthedocs.io/en/latest/misc.html#hex-and-hexdump>`_)

If IfThenElse parameter renamed `predicate` to `condfunc`, and cannot be embedded

Switch dropped `includekey` parameter, and cannot be embedded

EmbeddedSwitch added, in Conditional

RestreamData added, in Tunneling

TransformData added, in Tunneling

ExprAdapter Mapping Restreamed changed parameters order (decoders before encoders)

Adapter-related classes changed parameters, added `path` to `_encode _decode _validate`

LazyStruct LazySequence LazyRange LazyField(OnDemand) removed

LazyBound remains, but changed to parameter-less lambda

FlagsContainer removed

HexString removed


Exceptions
-------------

FieldError was replaced with StreamError (raised when stream returns less than requested amount) and FormatFieldError (raised by FormatField class, for example if building Float from non-float value and struct.pack complains).

StreamError can be raised by most classes, when the stream is not seekable or tellable

StringError can be raised by most classes, when expected bytes but given unicode value

BitIntegerError was replaced with IntegerError

Struct Sequence can raise IndexError KeyError when dictionaries are missing entries

RepeatError added

IndexFieldError added

CheckError added

NamedTupleError added

RawCopyError added
