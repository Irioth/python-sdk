# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/serverless/functions/v1/function.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/serverless/functions/v1/function.proto',
  package='yandex.cloud.serverless.functions.v1',
  syntax='proto3',
  serialized_options=b'\n(yandex.cloud.api.serverless.functions.v1ZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/functions/v1;functions',
  serialized_pb=b'\n3yandex/cloud/serverless/functions/v1/function.proto\x12$yandex.cloud.serverless.functions.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xe1\x03\n\x08\x46unction\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x04name\x18\x04 \x01(\tB\x08\x8a\xc8\x31\x04\x33-63\x12\x1e\n\x0b\x64\x65scription\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05\x30-256\x12T\n\x06labels\x18\x06 \x03(\x0b\x32:.yandex.cloud.serverless.functions.v1.Function.LabelsEntryB\x08\x82\xc8\x31\x04<=64\x12\x14\n\x0clog_group_id\x18\x07 \x01(\t\x12\x17\n\x0fhttp_invoke_url\x18\x08 \x01(\t\x12\x45\n\x06status\x18\t \x01(\x0e\x32\x35.yandex.cloud.serverless.functions.v1.Function.Status\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"S\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08\x44\x45LETING\x10\x03\x12\t\n\x05\x45RROR\x10\x04\"\xfe\x04\n\x07Version\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x66unction_id\x18\x02 \x01(\t\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05\x30-256\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07runtime\x18\x06 \x01(\t\x12\x12\n\nentrypoint\x18\x07 \x01(\t\x12\x42\n\tresources\x18\x08 \x01(\x0b\x32/.yandex.cloud.serverless.functions.v1.Resources\x12\x34\n\x11\x65xecution_timeout\x18\t \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1a\n\x12service_account_id\x18\n \x01(\t\x12\x12\n\nimage_size\x18\x0c \x01(\x03\x12\x44\n\x06status\x18\r \x01(\x0e\x32\x34.yandex.cloud.serverless.functions.v1.Version.Status\x12\x0c\n\x04tags\x18\x0e \x03(\t\x12\x14\n\x0clog_group_id\x18\x0f \x01(\t\x12S\n\x0b\x65nvironment\x18\x10 \x03(\x0b\x32>.yandex.cloud.serverless.functions.v1.Version.EnvironmentEntry\x1a\x32\n\x10\x45nvironmentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\":\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02J\x04\x08\x0b\x10\x0c\"4\n\tResources\x12\'\n\x06memory\x18\x01 \x01(\x03\x42\x17\xfa\xc7\x31\x13\x33\x33\x35\x35\x34\x34\x33\x32-1073741824\"O\n\x07Package\x12\x19\n\x0b\x62ucket_name\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x19\n\x0bobject_name\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x0e\n\x06sha256\x18\x03 \x01(\tB~\n(yandex.cloud.api.serverless.functions.v1ZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/functions/v1;functionsb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])



_FUNCTION_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.serverless.functions.v1.Function.Status',
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
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=588,
  serialized_end=671,
)
_sym_db.RegisterEnumDescriptor(_FUNCTION_STATUS)

_VERSION_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.serverless.functions.v1.Version.Status',
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
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=588,
  serialized_end=646,
)
_sym_db.RegisterEnumDescriptor(_VERSION_STATUS)


_FUNCTION_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.serverless.functions.v1.Function.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.serverless.functions.v1.Function.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.serverless.functions.v1.Function.LabelsEntry.value', index=1,
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
  serialized_start=541,
  serialized_end=586,
)

_FUNCTION = _descriptor.Descriptor(
  name='Function',
  full_name='yandex.cloud.serverless.functions.v1.Function',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.serverless.functions.v1.Function.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.serverless.functions.v1.Function.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.serverless.functions.v1.Function.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.serverless.functions.v1.Function.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\0043-63', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.serverless.functions.v1.Function.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\0050-256', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.serverless.functions.v1.Function.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\004<=64', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_group_id', full_name='yandex.cloud.serverless.functions.v1.Function.log_group_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http_invoke_url', full_name='yandex.cloud.serverless.functions.v1.Function.http_invoke_url', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.serverless.functions.v1.Function.status', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FUNCTION_LABELSENTRY, ],
  enum_types=[
    _FUNCTION_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=671,
)


_VERSION_ENVIRONMENTENTRY = _descriptor.Descriptor(
  name='EnvironmentEntry',
  full_name='yandex.cloud.serverless.functions.v1.Version.EnvironmentEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.serverless.functions.v1.Version.EnvironmentEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.serverless.functions.v1.Version.EnvironmentEntry.value', index=1,
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
  serialized_start=1196,
  serialized_end=1246,
)

_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='yandex.cloud.serverless.functions.v1.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.serverless.functions.v1.Version.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='function_id', full_name='yandex.cloud.serverless.functions.v1.Version.function_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.serverless.functions.v1.Version.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\0050-256', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.serverless.functions.v1.Version.created_at', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runtime', full_name='yandex.cloud.serverless.functions.v1.Version.runtime', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entrypoint', full_name='yandex.cloud.serverless.functions.v1.Version.entrypoint', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resources', full_name='yandex.cloud.serverless.functions.v1.Version.resources', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execution_timeout', full_name='yandex.cloud.serverless.functions.v1.Version.execution_timeout', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.serverless.functions.v1.Version.service_account_id', index=8,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_size', full_name='yandex.cloud.serverless.functions.v1.Version.image_size', index=9,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.serverless.functions.v1.Version.status', index=10,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='yandex.cloud.serverless.functions.v1.Version.tags', index=11,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_group_id', full_name='yandex.cloud.serverless.functions.v1.Version.log_group_id', index=12,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='environment', full_name='yandex.cloud.serverless.functions.v1.Version.environment', index=13,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VERSION_ENVIRONMENTENTRY, ],
  enum_types=[
    _VERSION_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=674,
  serialized_end=1312,
)


_RESOURCES = _descriptor.Descriptor(
  name='Resources',
  full_name='yandex.cloud.serverless.functions.v1.Resources',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='memory', full_name='yandex.cloud.serverless.functions.v1.Resources.memory', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\02333554432-1073741824', file=DESCRIPTOR),
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
  serialized_start=1314,
  serialized_end=1366,
)


_PACKAGE = _descriptor.Descriptor(
  name='Package',
  full_name='yandex.cloud.serverless.functions.v1.Package',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bucket_name', full_name='yandex.cloud.serverless.functions.v1.Package.bucket_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_name', full_name='yandex.cloud.serverless.functions.v1.Package.object_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sha256', full_name='yandex.cloud.serverless.functions.v1.Package.sha256', index=2,
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
  serialized_start=1368,
  serialized_end=1447,
)

_FUNCTION_LABELSENTRY.containing_type = _FUNCTION
_FUNCTION.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FUNCTION.fields_by_name['labels'].message_type = _FUNCTION_LABELSENTRY
_FUNCTION.fields_by_name['status'].enum_type = _FUNCTION_STATUS
_FUNCTION_STATUS.containing_type = _FUNCTION
_VERSION_ENVIRONMENTENTRY.containing_type = _VERSION
_VERSION.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_VERSION.fields_by_name['resources'].message_type = _RESOURCES
_VERSION.fields_by_name['execution_timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_VERSION.fields_by_name['status'].enum_type = _VERSION_STATUS
_VERSION.fields_by_name['environment'].message_type = _VERSION_ENVIRONMENTENTRY
_VERSION_STATUS.containing_type = _VERSION
DESCRIPTOR.message_types_by_name['Function'] = _FUNCTION
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.message_types_by_name['Resources'] = _RESOURCES
DESCRIPTOR.message_types_by_name['Package'] = _PACKAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Function = _reflection.GeneratedProtocolMessageType('Function', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FUNCTION_LABELSENTRY,
    '__module__' : 'yandex.cloud.serverless.functions.v1.function_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.functions.v1.Function.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _FUNCTION,
  '__module__' : 'yandex.cloud.serverless.functions.v1.function_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.functions.v1.Function)
  })
_sym_db.RegisterMessage(Function)
_sym_db.RegisterMessage(Function.LabelsEntry)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {

  'EnvironmentEntry' : _reflection.GeneratedProtocolMessageType('EnvironmentEntry', (_message.Message,), {
    'DESCRIPTOR' : _VERSION_ENVIRONMENTENTRY,
    '__module__' : 'yandex.cloud.serverless.functions.v1.function_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.functions.v1.Version.EnvironmentEntry)
    })
  ,
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'yandex.cloud.serverless.functions.v1.function_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.functions.v1.Version)
  })
_sym_db.RegisterMessage(Version)
_sym_db.RegisterMessage(Version.EnvironmentEntry)

Resources = _reflection.GeneratedProtocolMessageType('Resources', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCES,
  '__module__' : 'yandex.cloud.serverless.functions.v1.function_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.functions.v1.Resources)
  })
_sym_db.RegisterMessage(Resources)

Package = _reflection.GeneratedProtocolMessageType('Package', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGE,
  '__module__' : 'yandex.cloud.serverless.functions.v1.function_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.functions.v1.Package)
  })
_sym_db.RegisterMessage(Package)


DESCRIPTOR._options = None
_FUNCTION_LABELSENTRY._options = None
_FUNCTION.fields_by_name['name']._options = None
_FUNCTION.fields_by_name['description']._options = None
_FUNCTION.fields_by_name['labels']._options = None
_VERSION_ENVIRONMENTENTRY._options = None
_VERSION.fields_by_name['description']._options = None
_RESOURCES.fields_by_name['memory']._options = None
_PACKAGE.fields_by_name['bucket_name']._options = None
_PACKAGE.fields_by_name['object_name']._options = None
# @@protoc_insertion_point(module_scope)
