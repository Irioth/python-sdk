# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/dataproc/v1/resource_preset_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.dataproc.v1 import resource_preset_pb2 as yandex_dot_cloud_dot_dataproc_dot_v1_dot_resource__preset__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/dataproc/v1/resource_preset_service.proto',
  package='yandex.cloud.dataproc.v1',
  syntax='proto3',
  serialized_options=b'\n\034yandex.cloud.api.dataproc.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1;dataproc',
  serialized_pb=b'\n6yandex/cloud/dataproc/v1/resource_preset_service.proto\x12\x18yandex.cloud.dataproc.v1\x1a\x1cgoogle/api/annotations.proto\x1a.yandex/cloud/dataproc/v1/resource_preset.proto\x1a\x1dyandex/cloud/validation.proto\"<\n\x18GetResourcePresetRequest\x12 \n\x12resource_preset_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"Z\n\x1aListResourcePresetsRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\x85\x01\n\x1bListResourcePresetsResponse\x12\x42\n\x10resource_presets\x18\x01 \x03(\x0b\x32(.yandex.cloud.dataproc.v1.ResourcePreset\x12\"\n\x0fnext_page_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=1002\xd4\x02\n\x15ResourcePresetService\x12\x9e\x01\n\x03Get\x12\x32.yandex.cloud.dataproc.v1.GetResourcePresetRequest\x1a(.yandex.cloud.dataproc.v1.ResourcePreset\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/dataproc/v1/resourcePresets/{resource_preset_id}\x12\x99\x01\n\x04List\x12\x34.yandex.cloud.dataproc.v1.ListResourcePresetsRequest\x1a\x35.yandex.cloud.dataproc.v1.ListResourcePresetsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/dataproc/v1/resourcePresetsBe\n\x1cyandex.cloud.api.dataproc.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1;dataprocb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_dataproc_dot_v1_dot_resource__preset__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETRESOURCEPRESETREQUEST = _descriptor.Descriptor(
  name='GetResourcePresetRequest',
  full_name='yandex.cloud.dataproc.v1.GetResourcePresetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_preset_id', full_name='yandex.cloud.dataproc.v1.GetResourcePresetRequest.resource_preset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR),
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
  serialized_start=193,
  serialized_end=253,
)


_LISTRESOURCEPRESETSREQUEST = _descriptor.Descriptor(
  name='ListResourcePresetsRequest',
  full_name='yandex.cloud.dataproc.v1.ListResourcePresetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.dataproc.v1.ListResourcePresetsRequest.page_size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\006<=1000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.dataproc.v1.ListResourcePresetsRequest.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=100', file=DESCRIPTOR),
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
  serialized_start=255,
  serialized_end=345,
)


_LISTRESOURCEPRESETSRESPONSE = _descriptor.Descriptor(
  name='ListResourcePresetsResponse',
  full_name='yandex.cloud.dataproc.v1.ListResourcePresetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_presets', full_name='yandex.cloud.dataproc.v1.ListResourcePresetsResponse.resource_presets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.dataproc.v1.ListResourcePresetsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=100', file=DESCRIPTOR),
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
  serialized_start=348,
  serialized_end=481,
)

_LISTRESOURCEPRESETSRESPONSE.fields_by_name['resource_presets'].message_type = yandex_dot_cloud_dot_dataproc_dot_v1_dot_resource__preset__pb2._RESOURCEPRESET
DESCRIPTOR.message_types_by_name['GetResourcePresetRequest'] = _GETRESOURCEPRESETREQUEST
DESCRIPTOR.message_types_by_name['ListResourcePresetsRequest'] = _LISTRESOURCEPRESETSREQUEST
DESCRIPTOR.message_types_by_name['ListResourcePresetsResponse'] = _LISTRESOURCEPRESETSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetResourcePresetRequest = _reflection.GeneratedProtocolMessageType('GetResourcePresetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETRESOURCEPRESETREQUEST,
  '__module__' : 'yandex.cloud.dataproc.v1.resource_preset_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.v1.GetResourcePresetRequest)
  })
_sym_db.RegisterMessage(GetResourcePresetRequest)

ListResourcePresetsRequest = _reflection.GeneratedProtocolMessageType('ListResourcePresetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESOURCEPRESETSREQUEST,
  '__module__' : 'yandex.cloud.dataproc.v1.resource_preset_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.v1.ListResourcePresetsRequest)
  })
_sym_db.RegisterMessage(ListResourcePresetsRequest)

ListResourcePresetsResponse = _reflection.GeneratedProtocolMessageType('ListResourcePresetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESOURCEPRESETSRESPONSE,
  '__module__' : 'yandex.cloud.dataproc.v1.resource_preset_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.v1.ListResourcePresetsResponse)
  })
_sym_db.RegisterMessage(ListResourcePresetsResponse)


DESCRIPTOR._options = None
_GETRESOURCEPRESETREQUEST.fields_by_name['resource_preset_id']._options = None
_LISTRESOURCEPRESETSREQUEST.fields_by_name['page_size']._options = None
_LISTRESOURCEPRESETSREQUEST.fields_by_name['page_token']._options = None
_LISTRESOURCEPRESETSRESPONSE.fields_by_name['next_page_token']._options = None

_RESOURCEPRESETSERVICE = _descriptor.ServiceDescriptor(
  name='ResourcePresetService',
  full_name='yandex.cloud.dataproc.v1.ResourcePresetService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=484,
  serialized_end=824,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.dataproc.v1.ResourcePresetService.Get',
    index=0,
    containing_service=None,
    input_type=_GETRESOURCEPRESETREQUEST,
    output_type=yandex_dot_cloud_dot_dataproc_dot_v1_dot_resource__preset__pb2._RESOURCEPRESET,
    serialized_options=b'\202\323\344\223\0023\0221/dataproc/v1/resourcePresets/{resource_preset_id}',
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.dataproc.v1.ResourcePresetService.List',
    index=1,
    containing_service=None,
    input_type=_LISTRESOURCEPRESETSREQUEST,
    output_type=_LISTRESOURCEPRESETSRESPONSE,
    serialized_options=b'\202\323\344\223\002\036\022\034/dataproc/v1/resourcePresets',
  ),
])
_sym_db.RegisterServiceDescriptor(_RESOURCEPRESETSERVICE)

DESCRIPTOR.services_by_name['ResourcePresetService'] = _RESOURCEPRESETSERVICE

# @@protoc_insertion_point(module_scope)
