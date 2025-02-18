# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/elasticsearch/v1/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/elasticsearch/v1/user.proto',
  package='yandex.cloud.mdb.elasticsearch.v1',
  syntax='proto3',
  serialized_options=b'\n%yandex.cloud.api.mdb.elasticsearch.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/elasticsearch/v1;elasticsearch',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,yandex/cloud/mdb/elasticsearch/v1/user.proto\x12!yandex.cloud.mdb.elasticsearch.v1\x1a\x1dyandex/cloud/validation.proto\"(\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\"X\n\x08UserSpec\x12+\n\x04name\x18\x01 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\r[a-zA-Z0-9_]*\x12\x1f\n\x08password\x18\x02 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05\x38-128B|\n%yandex.cloud.api.mdb.elasticsearch.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/elasticsearch/v1;elasticsearchb\x06proto3'
  ,
  dependencies=[yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_USER = _descriptor.Descriptor(
  name='User',
  full_name='yandex.cloud.mdb.elasticsearch.v1.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.elasticsearch.v1.User.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.elasticsearch.v1.User.cluster_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=114,
  serialized_end=154,
)


_USERSPEC = _descriptor.Descriptor(
  name='UserSpec',
  full_name='yandex.cloud.mdb.elasticsearch.v1.UserSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.elasticsearch.v1.UserSpec.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=63\362\3071\r[a-zA-Z0-9_]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='yandex.cloud.mdb.elasticsearch.v1.UserSpec.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\0058-128', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=156,
  serialized_end=244,
)

DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['UserSpec'] = _USERSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.User)
  })
_sym_db.RegisterMessage(User)

UserSpec = _reflection.GeneratedProtocolMessageType('UserSpec', (_message.Message,), {
  'DESCRIPTOR' : _USERSPEC,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.UserSpec)
  })
_sym_db.RegisterMessage(UserSpec)


DESCRIPTOR._options = None
_USERSPEC.fields_by_name['name']._options = None
_USERSPEC.fields_by_name['password']._options = None
# @@protoc_insertion_point(module_scope)
