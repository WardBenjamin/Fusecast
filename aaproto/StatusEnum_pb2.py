# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: StatusEnum.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='StatusEnum.proto',
  package='gb.xxy.trial.proto.enums',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x10StatusEnum.proto\x12\x18gb.xxy.trial.proto.enums\"\"\n\x06Status\"\x18\n\x04\x45num\x12\x06\n\x02OK\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01')
)



_STATUS_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='gb.xxy.trial.proto.enums.Status.Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=56,
  serialized_end=80,
)
_sym_db.RegisterEnumDescriptor(_STATUS_ENUM)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='gb.xxy.trial.proto.enums.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATUS_ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=80,
)

_STATUS_ENUM.containing_type = _STATUS
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'StatusEnum_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.enums.Status)
  })
_sym_db.RegisterMessage(Status)


# @@protoc_insertion_point(module_scope)