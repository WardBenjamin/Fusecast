# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BluetoothPairingStatusEnum.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='BluetoothPairingStatusEnum.proto',
  package='gb.xxy.trial.proto.enums',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n BluetoothPairingStatusEnum.proto\x12\x18gb.xxy.trial.proto.enums\"<\n\x16\x42luetoothPairingStatus\"\"\n\x04\x45num\x12\x08\n\x04NONE\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x08\n\x04\x46\x41IL\x10\x02')
)



_BLUETOOTHPAIRINGSTATUS_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='gb.xxy.trial.proto.enums.BluetoothPairingStatus.Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=88,
  serialized_end=122,
)
_sym_db.RegisterEnumDescriptor(_BLUETOOTHPAIRINGSTATUS_ENUM)


_BLUETOOTHPAIRINGSTATUS = _descriptor.Descriptor(
  name='BluetoothPairingStatus',
  full_name='gb.xxy.trial.proto.enums.BluetoothPairingStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BLUETOOTHPAIRINGSTATUS_ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=122,
)

_BLUETOOTHPAIRINGSTATUS_ENUM.containing_type = _BLUETOOTHPAIRINGSTATUS
DESCRIPTOR.message_types_by_name['BluetoothPairingStatus'] = _BLUETOOTHPAIRINGSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BluetoothPairingStatus = _reflection.GeneratedProtocolMessageType('BluetoothPairingStatus', (_message.Message,), {
  'DESCRIPTOR' : _BLUETOOTHPAIRINGSTATUS,
  '__module__' : 'BluetoothPairingStatusEnum_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.enums.BluetoothPairingStatus)
  })
_sym_db.RegisterMessage(BluetoothPairingStatus)


# @@protoc_insertion_point(module_scope)
