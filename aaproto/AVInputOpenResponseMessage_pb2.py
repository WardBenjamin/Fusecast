# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AVInputOpenResponseMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='AVInputOpenResponseMessage.proto',
  package='gb.xxy.trial.proto.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n AVInputOpenResponseMessage.proto\x12\x1bgb.xxy.trial.proto.messages\"5\n\x13\x41VInputOpenResponse\x12\x0f\n\x07session\x18\x01 \x02(\x05\x12\r\n\x05value\x18\x02 \x02(\r')
)




_AVINPUTOPENRESPONSE = _descriptor.Descriptor(
  name='AVInputOpenResponse',
  full_name='gb.xxy.trial.proto.messages.AVInputOpenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='gb.xxy.trial.proto.messages.AVInputOpenResponse.session', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='gb.xxy.trial.proto.messages.AVInputOpenResponse.value', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=118,
)

DESCRIPTOR.message_types_by_name['AVInputOpenResponse'] = _AVINPUTOPENRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AVInputOpenResponse = _reflection.GeneratedProtocolMessageType('AVInputOpenResponse', (_message.Message,), {
  'DESCRIPTOR' : _AVINPUTOPENRESPONSE,
  '__module__' : 'AVInputOpenResponseMessage_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.messages.AVInputOpenResponse)
  })
_sym_db.RegisterMessage(AVInputOpenResponse)


# @@protoc_insertion_point(module_scope)