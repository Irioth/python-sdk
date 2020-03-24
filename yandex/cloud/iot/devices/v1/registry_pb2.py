# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iot/devices/v1/registry.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/iot/devices/v1/registry.proto',
  package='yandex.cloud.iot.devices.v1',
  syntax='proto3',
  serialized_options=b'\n\037yandex.cloud.api.iot.devices.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/iot/devices/v1;devices',
  serialized_pb=b'\n*yandex/cloud/iot/devices/v1/registry.proto\x12\x1byandex.cloud.iot.devices.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\x8c\x03\n\x08Registry\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x41\n\x06labels\x18\x06 \x03(\x0b\x32\x31.yandex.cloud.iot.devices.v1.Registry.LabelsEntry\x12<\n\x06status\x18\x07 \x01(\x0e\x32,.yandex.cloud.iot.devices.v1.Registry.Status\x12\x14\n\x0clog_group_id\x18\x08 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"H\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08\x44\x45LETING\x10\x03\"\x89\x01\n\x13RegistryCertificate\x12\x13\n\x0bregistry_id\x18\x01 \x01(\t\x12\x13\n\x0b\x66ingerprint\x18\x02 \x01(\t\x12\x18\n\x10\x63\x65rtificate_data\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"E\n\x0b\x44\x65viceAlias\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x14\n\x0ctopic_prefix\x18\x02 \x01(\t\x12\r\n\x05\x61lias\x18\x03 \x01(\t\"c\n\x10RegistryPassword\x12\x13\n\x0bregistry_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampBj\n\x1fyandex.cloud.api.iot.devices.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/iot/devices/v1;devicesb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])



_REGISTRY_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.iot.devices.v1.Registry.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETING', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=464,
  serialized_end=536,
)
_sym_db.RegisterEnumDescriptor(_REGISTRY_STATUS)


_REGISTRY_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.iot.devices.v1.Registry.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.iot.devices.v1.Registry.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.iot.devices.v1.Registry.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=417,
  serialized_end=462,
)

_REGISTRY = _descriptor.Descriptor(
  name='Registry',
  full_name='yandex.cloud.iot.devices.v1.Registry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.iot.devices.v1.Registry.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.iot.devices.v1.Registry.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.iot.devices.v1.Registry.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.iot.devices.v1.Registry.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.iot.devices.v1.Registry.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.iot.devices.v1.Registry.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.iot.devices.v1.Registry.status', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_group_id', full_name='yandex.cloud.iot.devices.v1.Registry.log_group_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REGISTRY_LABELSENTRY, ],
  enum_types=[
    _REGISTRY_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=140,
  serialized_end=536,
)


_REGISTRYCERTIFICATE = _descriptor.Descriptor(
  name='RegistryCertificate',
  full_name='yandex.cloud.iot.devices.v1.RegistryCertificate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registry_id', full_name='yandex.cloud.iot.devices.v1.RegistryCertificate.registry_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fingerprint', full_name='yandex.cloud.iot.devices.v1.RegistryCertificate.fingerprint', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='certificate_data', full_name='yandex.cloud.iot.devices.v1.RegistryCertificate.certificate_data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.iot.devices.v1.RegistryCertificate.created_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=539,
  serialized_end=676,
)


_DEVICEALIAS = _descriptor.Descriptor(
  name='DeviceAlias',
  full_name='yandex.cloud.iot.devices.v1.DeviceAlias',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='yandex.cloud.iot.devices.v1.DeviceAlias.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topic_prefix', full_name='yandex.cloud.iot.devices.v1.DeviceAlias.topic_prefix', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alias', full_name='yandex.cloud.iot.devices.v1.DeviceAlias.alias', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=678,
  serialized_end=747,
)


_REGISTRYPASSWORD = _descriptor.Descriptor(
  name='RegistryPassword',
  full_name='yandex.cloud.iot.devices.v1.RegistryPassword',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registry_id', full_name='yandex.cloud.iot.devices.v1.RegistryPassword.registry_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.iot.devices.v1.RegistryPassword.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.iot.devices.v1.RegistryPassword.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=749,
  serialized_end=848,
)

_REGISTRY_LABELSENTRY.containing_type = _REGISTRY
_REGISTRY.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REGISTRY.fields_by_name['labels'].message_type = _REGISTRY_LABELSENTRY
_REGISTRY.fields_by_name['status'].enum_type = _REGISTRY_STATUS
_REGISTRY_STATUS.containing_type = _REGISTRY
_REGISTRYCERTIFICATE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REGISTRYPASSWORD.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Registry'] = _REGISTRY
DESCRIPTOR.message_types_by_name['RegistryCertificate'] = _REGISTRYCERTIFICATE
DESCRIPTOR.message_types_by_name['DeviceAlias'] = _DEVICEALIAS
DESCRIPTOR.message_types_by_name['RegistryPassword'] = _REGISTRYPASSWORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Registry = _reflection.GeneratedProtocolMessageType('Registry', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _REGISTRY_LABELSENTRY,
    '__module__' : 'yandex.cloud.iot.devices.v1.registry_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.Registry.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _REGISTRY,
  '__module__' : 'yandex.cloud.iot.devices.v1.registry_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.Registry)
  })
_sym_db.RegisterMessage(Registry)
_sym_db.RegisterMessage(Registry.LabelsEntry)

RegistryCertificate = _reflection.GeneratedProtocolMessageType('RegistryCertificate', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRYCERTIFICATE,
  '__module__' : 'yandex.cloud.iot.devices.v1.registry_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.RegistryCertificate)
  })
_sym_db.RegisterMessage(RegistryCertificate)

DeviceAlias = _reflection.GeneratedProtocolMessageType('DeviceAlias', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEALIAS,
  '__module__' : 'yandex.cloud.iot.devices.v1.registry_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.DeviceAlias)
  })
_sym_db.RegisterMessage(DeviceAlias)

RegistryPassword = _reflection.GeneratedProtocolMessageType('RegistryPassword', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRYPASSWORD,
  '__module__' : 'yandex.cloud.iot.devices.v1.registry_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.RegistryPassword)
  })
_sym_db.RegisterMessage(RegistryPassword)


DESCRIPTOR._options = None
_REGISTRY_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
