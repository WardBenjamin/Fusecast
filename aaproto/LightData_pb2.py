# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LightData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import HeadlightStatusEnum_pb2 as HeadlightStatusEnum__pb2
from . import IndicatorStatusEnum_pb2 as IndicatorStatusEnum__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='LightData.proto',
  package='gb.xxy.trial.proto.data',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0fLightData.proto\x12\x17gb.xxy.trial.proto.data\x1a\x19HeadlightStatusEnum.proto\x1a\x19IndicatorStatusEnum.proto\"\xa6\x01\n\x05Light\x12\x41\n\theadlight\x18\x01 \x02(\x0e\x32..gb.xxy.trial.proto.enums.HeadlightStatus.Enum\x12\x41\n\tindicator\x18\x02 \x02(\x0e\x32..gb.xxy.trial.proto.enums.IndicatorStatus.Enum\x12\x17\n\x0fhazard_light_on\x18\x03 \x02(\x08')
  ,
  dependencies=[HeadlightStatusEnum__pb2.DESCRIPTOR,IndicatorStatusEnum__pb2.DESCRIPTOR,])




_LIGHT = _descriptor.Descriptor(
  name='Light',
  full_name='gb.xxy.trial.proto.data.Light',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='headlight', full_name='gb.xxy.trial.proto.data.Light.headlight', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indicator', full_name='gb.xxy.trial.proto.data.Light.indicator', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hazard_light_on', full_name='gb.xxy.trial.proto.data.Light.hazard_light_on', index=2,
      number=3, type=8, cpp_type=7, label=2,
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
  serialized_start=99,
  serialized_end=265,
)

_LIGHT.fields_by_name['headlight'].enum_type = HeadlightStatusEnum__pb2._HEADLIGHTSTATUS_ENUM
_LIGHT.fields_by_name['indicator'].enum_type = IndicatorStatusEnum__pb2._INDICATORSTATUS_ENUM
DESCRIPTOR.message_types_by_name['Light'] = _LIGHT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Light = _reflection.GeneratedProtocolMessageType('Light', (_message.Message,), {
  'DESCRIPTOR' : _LIGHT,
  '__module__' : 'LightData_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.data.Light)
  })
_sym_db.RegisterMessage(Light)


# @@protoc_insertion_point(module_scope)