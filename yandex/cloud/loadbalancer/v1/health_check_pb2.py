# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/loadbalancer/v1/health_check.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/loadbalancer/v1/health_check.proto',
  package='yandex.cloud.loadbalancer.v1',
  syntax='proto3',
  serialized_options=b'\n yandex.cloud.api.loadbalancer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadbalancer/v1;loadbalancer',
  serialized_pb=b'\n/yandex/cloud/loadbalancer/v1/health_check.proto\x12\x1cyandex.cloud.loadbalancer.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1dyandex/cloud/validation.proto\"\xf5\x03\n\x0bHealthCheck\x12\x33\n\x04name\x18\x01 \x01(\tB%\xe8\xc7\x31\x01\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12+\n\x08interval\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12*\n\x07timeout\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12%\n\x13unhealthy_threshold\x18\x04 \x01(\x03\x42\x08\xfa\xc7\x31\x04\x32-10\x12#\n\x11healthy_threshold\x18\x05 \x01(\x03\x42\x08\xfa\xc7\x31\x04\x32-10\x12K\n\x0btcp_options\x18\x06 \x01(\x0b\x32\x34.yandex.cloud.loadbalancer.v1.HealthCheck.TcpOptionsH\x00\x12M\n\x0chttp_options\x18\x07 \x01(\x0b\x32\x35.yandex.cloud.loadbalancer.v1.HealthCheck.HttpOptionsH\x00\x1a\'\n\nTcpOptions\x12\x19\n\x04port\x18\x01 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x31-65535\x1a\x36\n\x0bHttpOptions\x12\x19\n\x04port\x18\x01 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x31-65535\x12\x0c\n\x04path\x18\x02 \x01(\tB\x0f\n\x07options\x12\x04\xc0\xc1\x31\x01\x42q\n yandex.cloud.api.loadbalancer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadbalancer/v1;loadbalancerb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_HEALTHCHECK_TCPOPTIONS = _descriptor.Descriptor(
  name='TcpOptions',
  full_name='yandex.cloud.loadbalancer.v1.HealthCheck.TcpOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='yandex.cloud.loadbalancer.v1.HealthCheck.TcpOptions.port', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0071-65535', file=DESCRIPTOR),
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
  serialized_start=534,
  serialized_end=573,
)

_HEALTHCHECK_HTTPOPTIONS = _descriptor.Descriptor(
  name='HttpOptions',
  full_name='yandex.cloud.loadbalancer.v1.HealthCheck.HttpOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='yandex.cloud.loadbalancer.v1.HealthCheck.HttpOptions.port', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0071-65535', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='yandex.cloud.loadbalancer.v1.HealthCheck.HttpOptions.path', index=1,
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
  serialized_start=575,
  serialized_end=629,
)

_HEALTHCHECK = _descriptor.Descriptor(
  name='HealthCheck',
  full_name='yandex.cloud.loadbalancer.v1.HealthCheck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.loadbalancer.v1.HealthCheck.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interval', full_name='yandex.cloud.loadbalancer.v1.HealthCheck.interval', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='yandex.cloud.loadbalancer.v1.HealthCheck.timeout', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unhealthy_threshold', full_name='yandex.cloud.loadbalancer.v1.HealthCheck.unhealthy_threshold', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0042-10', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='healthy_threshold', full_name='yandex.cloud.loadbalancer.v1.HealthCheck.healthy_threshold', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0042-10', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tcp_options', full_name='yandex.cloud.loadbalancer.v1.HealthCheck.tcp_options', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http_options', full_name='yandex.cloud.loadbalancer.v1.HealthCheck.http_options', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HEALTHCHECK_TCPOPTIONS, _HEALTHCHECK_HTTPOPTIONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='options', full_name='yandex.cloud.loadbalancer.v1.HealthCheck.options',
      index=0, containing_type=None, fields=[], serialized_options=b'\300\3011\001'),
  ],
  serialized_start=145,
  serialized_end=646,
)

_HEALTHCHECK_TCPOPTIONS.containing_type = _HEALTHCHECK
_HEALTHCHECK_HTTPOPTIONS.containing_type = _HEALTHCHECK
_HEALTHCHECK.fields_by_name['interval'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_HEALTHCHECK.fields_by_name['timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_HEALTHCHECK.fields_by_name['tcp_options'].message_type = _HEALTHCHECK_TCPOPTIONS
_HEALTHCHECK.fields_by_name['http_options'].message_type = _HEALTHCHECK_HTTPOPTIONS
_HEALTHCHECK.oneofs_by_name['options'].fields.append(
  _HEALTHCHECK.fields_by_name['tcp_options'])
_HEALTHCHECK.fields_by_name['tcp_options'].containing_oneof = _HEALTHCHECK.oneofs_by_name['options']
_HEALTHCHECK.oneofs_by_name['options'].fields.append(
  _HEALTHCHECK.fields_by_name['http_options'])
_HEALTHCHECK.fields_by_name['http_options'].containing_oneof = _HEALTHCHECK.oneofs_by_name['options']
DESCRIPTOR.message_types_by_name['HealthCheck'] = _HEALTHCHECK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HealthCheck = _reflection.GeneratedProtocolMessageType('HealthCheck', (_message.Message,), {

  'TcpOptions' : _reflection.GeneratedProtocolMessageType('TcpOptions', (_message.Message,), {
    'DESCRIPTOR' : _HEALTHCHECK_TCPOPTIONS,
    '__module__' : 'yandex.cloud.loadbalancer.v1.health_check_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.loadbalancer.v1.HealthCheck.TcpOptions)
    })
  ,

  'HttpOptions' : _reflection.GeneratedProtocolMessageType('HttpOptions', (_message.Message,), {
    'DESCRIPTOR' : _HEALTHCHECK_HTTPOPTIONS,
    '__module__' : 'yandex.cloud.loadbalancer.v1.health_check_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.loadbalancer.v1.HealthCheck.HttpOptions)
    })
  ,
  'DESCRIPTOR' : _HEALTHCHECK,
  '__module__' : 'yandex.cloud.loadbalancer.v1.health_check_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.loadbalancer.v1.HealthCheck)
  })
_sym_db.RegisterMessage(HealthCheck)
_sym_db.RegisterMessage(HealthCheck.TcpOptions)
_sym_db.RegisterMessage(HealthCheck.HttpOptions)


DESCRIPTOR._options = None
_HEALTHCHECK_TCPOPTIONS.fields_by_name['port']._options = None
_HEALTHCHECK_HTTPOPTIONS.fields_by_name['port']._options = None
_HEALTHCHECK.oneofs_by_name['options']._options = None
_HEALTHCHECK.fields_by_name['name']._options = None
_HEALTHCHECK.fields_by_name['unhealthy_threshold']._options = None
_HEALTHCHECK.fields_by_name['healthy_threshold']._options = None
# @@protoc_insertion_point(module_scope)
