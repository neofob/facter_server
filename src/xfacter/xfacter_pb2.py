# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xfacter/xfacter.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xfacter/xfacter.proto',
  package='xfacter',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15xfacter/xfacter.proto\x12\x07xfacter\"\x1d\n\rRequestMethod\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1f\n\x0eResponseMethod\x12\r\n\x05value\x18\x01 \x01(\t\"\x1f\n\x0fRequestHasCache\x12\x0c\n\x04name\x18\x01 \x01(\t\"!\n\x10ResponseHasCache\x12\r\n\x05value\x18\x01 \x01(\x08\x32\x88\x01\n\x07XFacter\x12?\n\x08HasCache\x12\x18.xfacter.RequestHasCache\x1a\x19.xfacter.ResponseHasCache\x12<\n\tGetMethod\x12\x16.xfacter.RequestMethod\x1a\x17.xfacter.ResponseMethodb\x06proto3')
)




_REQUESTMETHOD = _descriptor.Descriptor(
  name='RequestMethod',
  full_name='xfacter.RequestMethod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='xfacter.RequestMethod.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=63,
)


_RESPONSEMETHOD = _descriptor.Descriptor(
  name='ResponseMethod',
  full_name='xfacter.ResponseMethod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='xfacter.ResponseMethod.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=96,
)


_REQUESTHASCACHE = _descriptor.Descriptor(
  name='RequestHasCache',
  full_name='xfacter.RequestHasCache',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='xfacter.RequestHasCache.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=129,
)


_RESPONSEHASCACHE = _descriptor.Descriptor(
  name='ResponseHasCache',
  full_name='xfacter.ResponseHasCache',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='xfacter.ResponseHasCache.value', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=164,
)

DESCRIPTOR.message_types_by_name['RequestMethod'] = _REQUESTMETHOD
DESCRIPTOR.message_types_by_name['ResponseMethod'] = _RESPONSEMETHOD
DESCRIPTOR.message_types_by_name['RequestHasCache'] = _REQUESTHASCACHE
DESCRIPTOR.message_types_by_name['ResponseHasCache'] = _RESPONSEHASCACHE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestMethod = _reflection.GeneratedProtocolMessageType('RequestMethod', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTMETHOD,
  __module__ = 'xfacter.xfacter_pb2'
  # @@protoc_insertion_point(class_scope:xfacter.RequestMethod)
  ))
_sym_db.RegisterMessage(RequestMethod)

ResponseMethod = _reflection.GeneratedProtocolMessageType('ResponseMethod', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEMETHOD,
  __module__ = 'xfacter.xfacter_pb2'
  # @@protoc_insertion_point(class_scope:xfacter.ResponseMethod)
  ))
_sym_db.RegisterMessage(ResponseMethod)

RequestHasCache = _reflection.GeneratedProtocolMessageType('RequestHasCache', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTHASCACHE,
  __module__ = 'xfacter.xfacter_pb2'
  # @@protoc_insertion_point(class_scope:xfacter.RequestHasCache)
  ))
_sym_db.RegisterMessage(RequestHasCache)

ResponseHasCache = _reflection.GeneratedProtocolMessageType('ResponseHasCache', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEHASCACHE,
  __module__ = 'xfacter.xfacter_pb2'
  # @@protoc_insertion_point(class_scope:xfacter.ResponseHasCache)
  ))
_sym_db.RegisterMessage(ResponseHasCache)



_XFACTER = _descriptor.ServiceDescriptor(
  name='XFacter',
  full_name='xfacter.XFacter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=167,
  serialized_end=303,
  methods=[
  _descriptor.MethodDescriptor(
    name='HasCache',
    full_name='xfacter.XFacter.HasCache',
    index=0,
    containing_service=None,
    input_type=_REQUESTHASCACHE,
    output_type=_RESPONSEHASCACHE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetMethod',
    full_name='xfacter.XFacter.GetMethod',
    index=1,
    containing_service=None,
    input_type=_REQUESTMETHOD,
    output_type=_RESPONSEMETHOD,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_XFACTER)

DESCRIPTOR.services_by_name['XFacter'] = _XFACTER

# @@protoc_insertion_point(module_scope)