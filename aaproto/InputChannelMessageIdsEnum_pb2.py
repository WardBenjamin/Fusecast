# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: InputChannelMessageIdsEnum.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='InputChannelMessageIdsEnum.proto',
  package='gb.xxy.trial.proto.ids',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n InputChannelMessageIdsEnum.proto\x12\x16gb.xxy.trial.proto.ids\"t\n\x13InputChannelMessage\"]\n\x04\x45num\x12\x08\n\x04NONE\x10\x00\x12\x1c\n\x16INPUT_EVENT_INDICATION\x10\x81\x80\x02\x12\x15\n\x0f\x42INDING_REQUEST\x10\x82\x80\x02\x12\x16\n\x10\x42INDING_RESPONSE\x10\x83\x80\x02')
)



_INPUTCHANNELMESSAGE_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='gb.xxy.trial.proto.ids.InputChannelMessage.Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INPUT_EVENT_INDICATION', index=1, number=32769,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BINDING_REQUEST', index=2, number=32770,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BINDING_RESPONSE', index=3, number=32771,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=83,
  serialized_end=176,
)
_sym_db.RegisterEnumDescriptor(_INPUTCHANNELMESSAGE_ENUM)


_INPUTCHANNELMESSAGE = _descriptor.Descriptor(
  name='InputChannelMessage',
  full_name='gb.xxy.trial.proto.ids.InputChannelMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INPUTCHANNELMESSAGE_ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=176,
)

_INPUTCHANNELMESSAGE_ENUM.containing_type = _INPUTCHANNELMESSAGE
DESCRIPTOR.message_types_by_name['InputChannelMessage'] = _INPUTCHANNELMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputChannelMessage = _reflection.GeneratedProtocolMessageType('InputChannelMessage', (_message.Message,), {
  'DESCRIPTOR' : _INPUTCHANNELMESSAGE,
  '__module__' : 'InputChannelMessageIdsEnum_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.ids.InputChannelMessage)
  })
_sym_db.RegisterMessage(InputChannelMessage)


# @@protoc_insertion_point(module_scope)