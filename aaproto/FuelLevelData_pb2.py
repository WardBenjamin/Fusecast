# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FuelLevelData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='FuelLevelData.proto',
  package='gb.xxy.trial.proto.data',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x13\x46uelLevelData.proto\x12\x17gb.xxy.trial.proto.data\"@\n\tFuelLevel\x12\x12\n\nfuel_level\x18\x01 \x02(\x05\x12\r\n\x05range\x18\x02 \x02(\x05\x12\x10\n\x08low_fuel\x18\x03 \x02(\x08')
)




_FUELLEVEL = _descriptor.Descriptor(
  name='FuelLevel',
  full_name='gb.xxy.trial.proto.data.FuelLevel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fuel_level', full_name='gb.xxy.trial.proto.data.FuelLevel.fuel_level', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='gb.xxy.trial.proto.data.FuelLevel.range', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low_fuel', full_name='gb.xxy.trial.proto.data.FuelLevel.low_fuel', index=2,
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
  serialized_start=48,
  serialized_end=112,
)

DESCRIPTOR.message_types_by_name['FuelLevel'] = _FUELLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FuelLevel = _reflection.GeneratedProtocolMessageType('FuelLevel', (_message.Message,), {
  'DESCRIPTOR' : _FUELLEVEL,
  '__module__' : 'FuelLevelData_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.data.FuelLevel)
  })
_sym_db.RegisterMessage(FuelLevel)


# @@protoc_insertion_point(module_scope)