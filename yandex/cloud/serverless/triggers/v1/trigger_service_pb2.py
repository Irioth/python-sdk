# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/serverless/triggers/v1/trigger_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.serverless.triggers.v1 import trigger_pb2 as yandex_dot_cloud_dot_serverless_dot_triggers_dot_v1_dot_trigger__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/serverless/triggers/v1/trigger_service.proto',
  package='yandex.cloud.serverless.triggers.v1',
  syntax='proto3',
  serialized_options=_b('\n\'yandex.cloud.api.serverless.triggers.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/triggers/v1;triggers'),
  serialized_pb=_b('\n9yandex/cloud/serverless/triggers/v1/trigger_service.proto\x12#yandex.cloud.serverless.triggers.v1\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a\x31yandex/cloud/serverless/triggers/v1/trigger.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"-\n\x11GetTriggerRequest\x12\x18\n\ntrigger_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"e\n\x13ListTriggersRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\"o\n\x14ListTriggersResponse\x12>\n\x08triggers\x18\x01 \x03(\x0b\x32,.yandex.cloud.serverless.triggers.v1.Trigger\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x8f\x03\n\x14\x43reateTriggerRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x96\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x45.yandex.cloud.serverless.triggers.v1.CreateTriggerRequest.LabelsEntryB?\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0b[-_0-9a-z]*\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x12\x12\x10[a-z][-_0-9a-z]*\x12\x45\n\x04rule\x18\x05 \x01(\x0b\x32\x31.yandex.cloud.serverless.triggers.v1.Trigger.RuleB\x04\xe8\xc7\x31\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x15\x43reateTriggerMetadata\x12\x12\n\ntrigger_id\x18\x01 \x01(\t\"\xfa\x02\n\x14UpdateTriggerRequest\x12\x18\n\ntrigger_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12/\n\x04name\x18\x03 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x96\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x45.yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest.LabelsEntryB?\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0b[-_0-9a-z]*\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x12\x12\x10[a-z][-_0-9a-z]*\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"1\n\x15UpdateTriggerMetadata\x12\x18\n\ntrigger_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"0\n\x14\x44\x65leteTriggerRequest\x12\x18\n\ntrigger_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"1\n\x15\x44\x65leteTriggerMetadata\x12\x18\n\ntrigger_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x92\x01\n\x1cListTriggerOperationsRequest\x12\x18\n\ntrigger_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"o\n\x1dListTriggerOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xca\x08\n\x0eTriggerService\x12\x97\x01\n\x03Get\x12\x36.yandex.cloud.serverless.triggers.v1.GetTriggerRequest\x1a,.yandex.cloud.serverless.triggers.v1.Trigger\"*\x82\xd3\xe4\x93\x02$\x12\"/triggers/v1/triggers/{trigger_id}\x12\x9a\x01\n\x04List\x12\x38.yandex.cloud.serverless.triggers.v1.ListTriggersRequest\x1a\x39.yandex.cloud.serverless.triggers.v1.ListTriggersResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/triggers/v1/triggers\x12\xac\x01\n\x06\x43reate\x12\x39.yandex.cloud.serverless.triggers.v1.CreateTriggerRequest\x1a!.yandex.cloud.operation.Operation\"D\x82\xd3\xe4\x93\x02\x1a\"\x15/triggers/v1/triggers:\x01*\xb2\xd2* \n\x15\x43reateTriggerMetadata\x12\x07Trigger\x12\xb9\x01\n\x06Update\x12\x39.yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest\x1a!.yandex.cloud.operation.Operation\"Q\x82\xd3\xe4\x93\x02\'2\"/triggers/v1/triggers/{trigger_id}:\x01*\xb2\xd2* \n\x15UpdateTriggerMetadata\x12\x07Trigger\x12\xc4\x01\n\x06\x44\x65lete\x12\x39.yandex.cloud.serverless.triggers.v1.DeleteTriggerRequest\x1a!.yandex.cloud.operation.Operation\"\\\x82\xd3\xe4\x93\x02$*\"/triggers/v1/triggers/{trigger_id}\xb2\xd2*.\n\x15\x44\x65leteTriggerMetadata\x12\x15google.protobuf.Empty\x12\xce\x01\n\x0eListOperations\x12\x41.yandex.cloud.serverless.triggers.v1.ListTriggerOperationsRequest\x1a\x42.yandex.cloud.serverless.triggers.v1.ListTriggerOperationsResponse\"5\x82\xd3\xe4\x93\x02/\x12-/triggers/v1/triggers/{trigger_id}/operationsB{\n\'yandex.cloud.api.serverless.triggers.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/triggers/v1;triggersb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_serverless_dot_triggers_dot_v1_dot_trigger__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETTRIGGERREQUEST = _descriptor.Descriptor(
  name='GetTriggerRequest',
  full_name='yandex.cloud.serverless.triggers.v1.GetTriggerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trigger_id', full_name='yandex.cloud.serverless.triggers.v1.GetTriggerRequest.trigger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
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
  serialized_start=318,
  serialized_end=363,
)


_LISTTRIGGERSREQUEST = _descriptor.Descriptor(
  name='ListTriggersRequest',
  full_name='yandex.cloud.serverless.triggers.v1.ListTriggersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.serverless.triggers.v1.ListTriggersRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.serverless.triggers.v1.ListTriggersRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.serverless.triggers.v1.ListTriggersRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='yandex.cloud.serverless.triggers.v1.ListTriggersRequest.filter', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=365,
  serialized_end=466,
)


_LISTTRIGGERSRESPONSE = _descriptor.Descriptor(
  name='ListTriggersResponse',
  full_name='yandex.cloud.serverless.triggers.v1.ListTriggersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='triggers', full_name='yandex.cloud.serverless.triggers.v1.ListTriggersResponse.triggers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.serverless.triggers.v1.ListTriggersResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=468,
  serialized_end=579,
)


_CREATETRIGGERREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.serverless.triggers.v1.CreateTriggerRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.serverless.triggers.v1.CreateTriggerRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.serverless.triggers.v1.CreateTriggerRequest.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=936,
  serialized_end=981,
)

_CREATETRIGGERREQUEST = _descriptor.Descriptor(
  name='CreateTriggerRequest',
  full_name='yandex.cloud.serverless.triggers.v1.CreateTriggerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.serverless.triggers.v1.CreateTriggerRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.serverless.triggers.v1.CreateTriggerRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.serverless.triggers.v1.CreateTriggerRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=256'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.serverless.triggers.v1.CreateTriggerRequest.labels', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202\3101\004<=64\212\3101\004<=63\362\3071\013[-_0-9a-z]*\262\3101\006\032\0041-63\262\3101\022\022\020[a-z][-_0-9a-z]*'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule', full_name='yandex.cloud.serverless.triggers.v1.CreateTriggerRequest.rule', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATETRIGGERREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=582,
  serialized_end=981,
)


_CREATETRIGGERMETADATA = _descriptor.Descriptor(
  name='CreateTriggerMetadata',
  full_name='yandex.cloud.serverless.triggers.v1.CreateTriggerMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trigger_id', full_name='yandex.cloud.serverless.triggers.v1.CreateTriggerMetadata.trigger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=983,
  serialized_end=1026,
)


_UPDATETRIGGERREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=936,
  serialized_end=981,
)

_UPDATETRIGGERREQUEST = _descriptor.Descriptor(
  name='UpdateTriggerRequest',
  full_name='yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trigger_id', full_name='yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest.trigger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=256'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest.labels', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202\3101\004<=64\212\3101\004<=63\362\3071\013[-_0-9a-z]*\262\3101\006\032\0041-63\262\3101\022\022\020[a-z][-_0-9a-z]*'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATETRIGGERREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1029,
  serialized_end=1407,
)


_UPDATETRIGGERMETADATA = _descriptor.Descriptor(
  name='UpdateTriggerMetadata',
  full_name='yandex.cloud.serverless.triggers.v1.UpdateTriggerMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trigger_id', full_name='yandex.cloud.serverless.triggers.v1.UpdateTriggerMetadata.trigger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
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
  serialized_start=1409,
  serialized_end=1458,
)


_DELETETRIGGERREQUEST = _descriptor.Descriptor(
  name='DeleteTriggerRequest',
  full_name='yandex.cloud.serverless.triggers.v1.DeleteTriggerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trigger_id', full_name='yandex.cloud.serverless.triggers.v1.DeleteTriggerRequest.trigger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
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
  serialized_start=1460,
  serialized_end=1508,
)


_DELETETRIGGERMETADATA = _descriptor.Descriptor(
  name='DeleteTriggerMetadata',
  full_name='yandex.cloud.serverless.triggers.v1.DeleteTriggerMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trigger_id', full_name='yandex.cloud.serverless.triggers.v1.DeleteTriggerMetadata.trigger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
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
  serialized_start=1510,
  serialized_end=1559,
)


_LISTTRIGGEROPERATIONSREQUEST = _descriptor.Descriptor(
  name='ListTriggerOperationsRequest',
  full_name='yandex.cloud.serverless.triggers.v1.ListTriggerOperationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trigger_id', full_name='yandex.cloud.serverless.triggers.v1.ListTriggerOperationsRequest.trigger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.serverless.triggers.v1.ListTriggerOperationsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\0060-1000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.serverless.triggers.v1.ListTriggerOperationsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=100'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='yandex.cloud.serverless.triggers.v1.ListTriggerOperationsRequest.filter', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\006<=1000'), file=DESCRIPTOR),
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
  serialized_start=1562,
  serialized_end=1708,
)


_LISTTRIGGEROPERATIONSRESPONSE = _descriptor.Descriptor(
  name='ListTriggerOperationsResponse',
  full_name='yandex.cloud.serverless.triggers.v1.ListTriggerOperationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operations', full_name='yandex.cloud.serverless.triggers.v1.ListTriggerOperationsResponse.operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.serverless.triggers.v1.ListTriggerOperationsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1710,
  serialized_end=1821,
)

_LISTTRIGGERSRESPONSE.fields_by_name['triggers'].message_type = yandex_dot_cloud_dot_serverless_dot_triggers_dot_v1_dot_trigger__pb2._TRIGGER
_CREATETRIGGERREQUEST_LABELSENTRY.containing_type = _CREATETRIGGERREQUEST
_CREATETRIGGERREQUEST.fields_by_name['labels'].message_type = _CREATETRIGGERREQUEST_LABELSENTRY
_CREATETRIGGERREQUEST.fields_by_name['rule'].message_type = yandex_dot_cloud_dot_serverless_dot_triggers_dot_v1_dot_trigger__pb2._TRIGGER_RULE
_UPDATETRIGGERREQUEST_LABELSENTRY.containing_type = _UPDATETRIGGERREQUEST
_UPDATETRIGGERREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_UPDATETRIGGERREQUEST.fields_by_name['labels'].message_type = _UPDATETRIGGERREQUEST_LABELSENTRY
_LISTTRIGGEROPERATIONSRESPONSE.fields_by_name['operations'].message_type = yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION
DESCRIPTOR.message_types_by_name['GetTriggerRequest'] = _GETTRIGGERREQUEST
DESCRIPTOR.message_types_by_name['ListTriggersRequest'] = _LISTTRIGGERSREQUEST
DESCRIPTOR.message_types_by_name['ListTriggersResponse'] = _LISTTRIGGERSRESPONSE
DESCRIPTOR.message_types_by_name['CreateTriggerRequest'] = _CREATETRIGGERREQUEST
DESCRIPTOR.message_types_by_name['CreateTriggerMetadata'] = _CREATETRIGGERMETADATA
DESCRIPTOR.message_types_by_name['UpdateTriggerRequest'] = _UPDATETRIGGERREQUEST
DESCRIPTOR.message_types_by_name['UpdateTriggerMetadata'] = _UPDATETRIGGERMETADATA
DESCRIPTOR.message_types_by_name['DeleteTriggerRequest'] = _DELETETRIGGERREQUEST
DESCRIPTOR.message_types_by_name['DeleteTriggerMetadata'] = _DELETETRIGGERMETADATA
DESCRIPTOR.message_types_by_name['ListTriggerOperationsRequest'] = _LISTTRIGGEROPERATIONSREQUEST
DESCRIPTOR.message_types_by_name['ListTriggerOperationsResponse'] = _LISTTRIGGEROPERATIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetTriggerRequest = _reflection.GeneratedProtocolMessageType('GetTriggerRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTRIGGERREQUEST,
  __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.GetTriggerRequest)
  ))
_sym_db.RegisterMessage(GetTriggerRequest)

ListTriggersRequest = _reflection.GeneratedProtocolMessageType('ListTriggersRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTTRIGGERSREQUEST,
  __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.ListTriggersRequest)
  ))
_sym_db.RegisterMessage(ListTriggersRequest)

ListTriggersResponse = _reflection.GeneratedProtocolMessageType('ListTriggersResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTTRIGGERSRESPONSE,
  __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.ListTriggersResponse)
  ))
_sym_db.RegisterMessage(ListTriggersResponse)

CreateTriggerRequest = _reflection.GeneratedProtocolMessageType('CreateTriggerRequest', (_message.Message,), dict(

  LabelsEntry = _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), dict(
    DESCRIPTOR = _CREATETRIGGERREQUEST_LABELSENTRY,
    __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.CreateTriggerRequest.LabelsEntry)
    ))
  ,
  DESCRIPTOR = _CREATETRIGGERREQUEST,
  __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.CreateTriggerRequest)
  ))
_sym_db.RegisterMessage(CreateTriggerRequest)
_sym_db.RegisterMessage(CreateTriggerRequest.LabelsEntry)

CreateTriggerMetadata = _reflection.GeneratedProtocolMessageType('CreateTriggerMetadata', (_message.Message,), dict(
  DESCRIPTOR = _CREATETRIGGERMETADATA,
  __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.CreateTriggerMetadata)
  ))
_sym_db.RegisterMessage(CreateTriggerMetadata)

UpdateTriggerRequest = _reflection.GeneratedProtocolMessageType('UpdateTriggerRequest', (_message.Message,), dict(

  LabelsEntry = _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), dict(
    DESCRIPTOR = _UPDATETRIGGERREQUEST_LABELSENTRY,
    __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest.LabelsEntry)
    ))
  ,
  DESCRIPTOR = _UPDATETRIGGERREQUEST,
  __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest)
  ))
_sym_db.RegisterMessage(UpdateTriggerRequest)
_sym_db.RegisterMessage(UpdateTriggerRequest.LabelsEntry)

UpdateTriggerMetadata = _reflection.GeneratedProtocolMessageType('UpdateTriggerMetadata', (_message.Message,), dict(
  DESCRIPTOR = _UPDATETRIGGERMETADATA,
  __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.UpdateTriggerMetadata)
  ))
_sym_db.RegisterMessage(UpdateTriggerMetadata)

DeleteTriggerRequest = _reflection.GeneratedProtocolMessageType('DeleteTriggerRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETETRIGGERREQUEST,
  __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.DeleteTriggerRequest)
  ))
_sym_db.RegisterMessage(DeleteTriggerRequest)

DeleteTriggerMetadata = _reflection.GeneratedProtocolMessageType('DeleteTriggerMetadata', (_message.Message,), dict(
  DESCRIPTOR = _DELETETRIGGERMETADATA,
  __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.DeleteTriggerMetadata)
  ))
_sym_db.RegisterMessage(DeleteTriggerMetadata)

ListTriggerOperationsRequest = _reflection.GeneratedProtocolMessageType('ListTriggerOperationsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTTRIGGEROPERATIONSREQUEST,
  __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.ListTriggerOperationsRequest)
  ))
_sym_db.RegisterMessage(ListTriggerOperationsRequest)

ListTriggerOperationsResponse = _reflection.GeneratedProtocolMessageType('ListTriggerOperationsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTTRIGGEROPERATIONSRESPONSE,
  __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.ListTriggerOperationsResponse)
  ))
_sym_db.RegisterMessage(ListTriggerOperationsResponse)


DESCRIPTOR._options = None
_GETTRIGGERREQUEST.fields_by_name['trigger_id']._options = None
_LISTTRIGGERSREQUEST.fields_by_name['folder_id']._options = None
_CREATETRIGGERREQUEST_LABELSENTRY._options = None
_CREATETRIGGERREQUEST.fields_by_name['folder_id']._options = None
_CREATETRIGGERREQUEST.fields_by_name['name']._options = None
_CREATETRIGGERREQUEST.fields_by_name['description']._options = None
_CREATETRIGGERREQUEST.fields_by_name['labels']._options = None
_CREATETRIGGERREQUEST.fields_by_name['rule']._options = None
_UPDATETRIGGERREQUEST_LABELSENTRY._options = None
_UPDATETRIGGERREQUEST.fields_by_name['trigger_id']._options = None
_UPDATETRIGGERREQUEST.fields_by_name['name']._options = None
_UPDATETRIGGERREQUEST.fields_by_name['description']._options = None
_UPDATETRIGGERREQUEST.fields_by_name['labels']._options = None
_UPDATETRIGGERMETADATA.fields_by_name['trigger_id']._options = None
_DELETETRIGGERREQUEST.fields_by_name['trigger_id']._options = None
_DELETETRIGGERMETADATA.fields_by_name['trigger_id']._options = None
_LISTTRIGGEROPERATIONSREQUEST.fields_by_name['trigger_id']._options = None
_LISTTRIGGEROPERATIONSREQUEST.fields_by_name['page_size']._options = None
_LISTTRIGGEROPERATIONSREQUEST.fields_by_name['page_token']._options = None
_LISTTRIGGEROPERATIONSREQUEST.fields_by_name['filter']._options = None

_TRIGGERSERVICE = _descriptor.ServiceDescriptor(
  name='TriggerService',
  full_name='yandex.cloud.serverless.triggers.v1.TriggerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1824,
  serialized_end=2922,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.serverless.triggers.v1.TriggerService.Get',
    index=0,
    containing_service=None,
    input_type=_GETTRIGGERREQUEST,
    output_type=yandex_dot_cloud_dot_serverless_dot_triggers_dot_v1_dot_trigger__pb2._TRIGGER,
    serialized_options=_b('\202\323\344\223\002$\022\"/triggers/v1/triggers/{trigger_id}'),
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.serverless.triggers.v1.TriggerService.List',
    index=1,
    containing_service=None,
    input_type=_LISTTRIGGERSREQUEST,
    output_type=_LISTTRIGGERSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\027\022\025/triggers/v1/triggers'),
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='yandex.cloud.serverless.triggers.v1.TriggerService.Create',
    index=2,
    containing_service=None,
    input_type=_CREATETRIGGERREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\002\032\"\025/triggers/v1/triggers:\001*\262\322* \n\025CreateTriggerMetadata\022\007Trigger'),
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='yandex.cloud.serverless.triggers.v1.TriggerService.Update',
    index=3,
    containing_service=None,
    input_type=_UPDATETRIGGERREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\002\'2\"/triggers/v1/triggers/{trigger_id}:\001*\262\322* \n\025UpdateTriggerMetadata\022\007Trigger'),
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='yandex.cloud.serverless.triggers.v1.TriggerService.Delete',
    index=4,
    containing_service=None,
    input_type=_DELETETRIGGERREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\002$*\"/triggers/v1/triggers/{trigger_id}\262\322*.\n\025DeleteTriggerMetadata\022\025google.protobuf.Empty'),
  ),
  _descriptor.MethodDescriptor(
    name='ListOperations',
    full_name='yandex.cloud.serverless.triggers.v1.TriggerService.ListOperations',
    index=5,
    containing_service=None,
    input_type=_LISTTRIGGEROPERATIONSREQUEST,
    output_type=_LISTTRIGGEROPERATIONSRESPONSE,
    serialized_options=_b('\202\323\344\223\002/\022-/triggers/v1/triggers/{trigger_id}/operations'),
  ),
])
_sym_db.RegisterServiceDescriptor(_TRIGGERSERVICE)

DESCRIPTOR.services_by_name['TriggerService'] = _TRIGGERSERVICE

# @@protoc_insertion_point(module_scope)