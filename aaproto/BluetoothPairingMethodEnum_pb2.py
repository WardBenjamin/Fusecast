# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BluetoothPairingMethodEnum.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='BluetoothPairingMethodEnum.proto',
  package='gb.xxy.trial.proto.enums',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n BluetoothPairingMethodEnum.proto\x12\x18gb.xxy.trial.proto.enums\"S\n\x16\x42luetoothPairingMethod\"9\n\x04\x45num\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05UNK_1\x10\x01\x12\x08\n\x04\x41\x32\x44P\x10\x02\x12\t\n\x05UNK_3\x10\x03\x12\x07\n\x03HFP\x10\x04')
)



_BLUETOOTHPAIRINGMETHOD_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='gb.xxy.trial.proto.enums.BluetoothPairingMethod.Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNK_1', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='A2DP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNK_3', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HFP', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=88,
  serialized_end=145,
)
_sym_db.RegisterEnumDescriptor(_BLUETOOTHPAIRINGMETHOD_ENUM)


_BLUETOOTHPAIRINGMETHOD = _descriptor.Descriptor(
  name='BluetoothPairingMethod',
  full_name='gb.xxy.trial.proto.enums.BluetoothPairingMethod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BLUETOOTHPAIRINGMETHOD_ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=145,
)

_BLUETOOTHPAIRINGMETHOD_ENUM.containing_type = _BLUETOOTHPAIRINGMETHOD
DESCRIPTOR.message_types_by_name['BluetoothPairingMethod'] = _BLUETOOTHPAIRINGMETHOD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BluetoothPairingMethod = _reflection.GeneratedProtocolMessageType('BluetoothPairingMethod', (_message.Message,), {
  'DESCRIPTOR' : _BLUETOOTHPAIRINGMETHOD,
  '__module__' : 'BluetoothPairingMethodEnum_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.enums.BluetoothPairingMethod)
  })
_sym_db.RegisterMessage(BluetoothPairingMethod)


# @@protoc_insertion_point(module_scope)
