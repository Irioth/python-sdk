# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/containerregistry/v1/repository.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/containerregistry/v1/repository.proto',
  package='yandex.cloud.containerregistry.v1',
  syntax='proto3',
  serialized_options=b'\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistry',
  serialized_pb=b'\n2yandex/cloud/containerregistry/v1/repository.proto\x12!yandex.cloud.containerregistry.v1\"&\n\nRepository\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\tB\x80\x01\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistryb\x06proto3'
)




_REPOSITORY = _descriptor.Descriptor(
  name='Repository',
  full_name='yandex.cloud.containerregistry.v1.Repository',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.containerregistry.v1.Repository.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.containerregistry.v1.Repository.id', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=127,
)

DESCRIPTOR.message_types_by_name['Repository'] = _REPOSITORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Repository = _reflection.GeneratedProtocolMessageType('Repository', (_message.Message,), {
  'DESCRIPTOR' : _REPOSITORY,
  '__module__' : 'yandex.cloud.containerregistry.v1.repository_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.Repository)
  })
_sym_db.RegisterMessage(Repository)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
