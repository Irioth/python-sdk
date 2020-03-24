# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iam/v1/key.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/iam/v1/key.proto',
  package='yandex.cloud.iam.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iam',
  serialized_pb=b'\n\x1dyandex/cloud/iam/v1/key.proto\x12\x13yandex.cloud.iam.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xad\x02\n\x03Key\x12\n\n\x02id\x18\x01 \x01(\t\x12\x19\n\x0fuser_account_id\x18\x02 \x01(\tH\x00\x12\x1c\n\x12service_account_id\x18\x03 \x01(\tH\x00\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x39\n\rkey_algorithm\x18\x06 \x01(\x0e\x32\".yandex.cloud.iam.v1.Key.Algorithm\x12\x12\n\npublic_key\x18\x07 \x01(\t\"B\n\tAlgorithm\x12\x19\n\x15\x41LGORITHM_UNSPECIFIED\x10\x00\x12\x0c\n\x08RSA_2048\x10\x01\x12\x0c\n\x08RSA_4096\x10\x02\x42\t\n\x07subjectBV\n\x17yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iamb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_KEY_ALGORITHM = _descriptor.EnumDescriptor(
  name='Algorithm',
  full_name='yandex.cloud.iam.v1.Key.Algorithm',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALGORITHM_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RSA_2048', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RSA_4096', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=312,
  serialized_end=378,
)
_sym_db.RegisterEnumDescriptor(_KEY_ALGORITHM)


_KEY = _descriptor.Descriptor(
  name='Key',
  full_name='yandex.cloud.iam.v1.Key',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.iam.v1.Key.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_account_id', full_name='yandex.cloud.iam.v1.Key.user_account_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.iam.v1.Key.service_account_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.iam.v1.Key.created_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.iam.v1.Key.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_algorithm', full_name='yandex.cloud.iam.v1.Key.key_algorithm', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public_key', full_name='yandex.cloud.iam.v1.Key.public_key', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _KEY_ALGORITHM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='subject', full_name='yandex.cloud.iam.v1.Key.subject',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=88,
  serialized_end=389,
)

_KEY.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_KEY.fields_by_name['key_algorithm'].enum_type = _KEY_ALGORITHM
_KEY_ALGORITHM.containing_type = _KEY
_KEY.oneofs_by_name['subject'].fields.append(
  _KEY.fields_by_name['user_account_id'])
_KEY.fields_by_name['user_account_id'].containing_oneof = _KEY.oneofs_by_name['subject']
_KEY.oneofs_by_name['subject'].fields.append(
  _KEY.fields_by_name['service_account_id'])
_KEY.fields_by_name['service_account_id'].containing_oneof = _KEY.oneofs_by_name['subject']
DESCRIPTOR.message_types_by_name['Key'] = _KEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Key = _reflection.GeneratedProtocolMessageType('Key', (_message.Message,), {
  'DESCRIPTOR' : _KEY,
  '__module__' : 'yandex.cloud.iam.v1.key_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.Key)
  })
_sym_db.RegisterMessage(Key)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
