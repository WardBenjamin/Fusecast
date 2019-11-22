# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AVInputChannelData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import AVStreamTypeEnum_pb2 as AVStreamTypeEnum__pb2
from . import AudioConfigData_pb2 as AudioConfigData__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='AVInputChannelData.proto',
  package='gb.xxy.trial.proto.data',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x18\x41VInputChannelData.proto\x12\x17gb.xxy.trial.proto.data\x1a\x16\x41VStreamTypeEnum.proto\x1a\x15\x41udioConfigData.proto\"\xaf\x01\n\x0e\x41VInputChannel\x12@\n\x0bstream_type\x18\x01 \x02(\x0e\x32+.gb.xxy.trial.proto.enums.AVStreamType.Enum\x12:\n\x0c\x61udio_config\x18\x02 \x02(\x0b\x32$.gb.xxy.trial.proto.data.AudioConfig\x12\x1f\n\x17\x61vailable_while_in_call\x18\x03 \x01(\x08')
  ,
  dependencies=[AVStreamTypeEnum__pb2.DESCRIPTOR,AudioConfigData__pb2.DESCRIPTOR,])




_AVINPUTCHANNEL = _descriptor.Descriptor(
  name='AVInputChannel',
  full_name='gb.xxy.trial.proto.data.AVInputChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_type', full_name='gb.xxy.trial.proto.data.AVInputChannel.stream_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audio_config', full_name='gb.xxy.trial.proto.data.AVInputChannel.audio_config', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available_while_in_call', full_name='gb.xxy.trial.proto.data.AVInputChannel.available_while_in_call', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=276,
)

_AVINPUTCHANNEL.fields_by_name['stream_type'].enum_type = AVStreamTypeEnum__pb2._AVSTREAMTYPE_ENUM
_AVINPUTCHANNEL.fields_by_name['audio_config'].message_type = AudioConfigData__pb2._AUDIOCONFIG
DESCRIPTOR.message_types_by_name['AVInputChannel'] = _AVINPUTCHANNEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AVInputChannel = _reflection.GeneratedProtocolMessageType('AVInputChannel', (_message.Message,), {
  'DESCRIPTOR' : _AVINPUTCHANNEL,
  '__module__' : 'AVInputChannelData_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.data.AVInputChannel)
  })
_sym_db.RegisterMessage(AVInputChannel)


# @@protoc_insertion_point(module_scope)