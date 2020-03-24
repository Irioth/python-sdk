# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/redis/v1/cluster.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2
from yandex.cloud.mdb.redis.v1.config import redis5_0_pb2 as yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_config_dot_redis5__0__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/redis/v1/cluster.proto',
  package='yandex.cloud.mdb.redis.v1',
  syntax='proto3',
  serialized_options=b'\n\035yandex.cloud.api.mdb.redis.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1;redis',
  serialized_pb=b'\n\'yandex/cloud/mdb/redis/v1/cluster.proto\x12\x19yandex.cloud.mdb.redis.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/type/timeofday.proto\x1a/yandex/cloud/mdb/redis/v1/config/redis5_0.proto\"\xc6\x06\n\x07\x43luster\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12>\n\x06labels\x18\x06 \x03(\x0b\x32..yandex.cloud.mdb.redis.v1.Cluster.LabelsEntry\x12\x43\n\x0b\x65nvironment\x18\x07 \x01(\x0e\x32..yandex.cloud.mdb.redis.v1.Cluster.Environment\x12\x39\n\nmonitoring\x18\x08 \x03(\x0b\x32%.yandex.cloud.mdb.redis.v1.Monitoring\x12\x38\n\x06\x63onfig\x18\t \x01(\x0b\x32(.yandex.cloud.mdb.redis.v1.ClusterConfig\x12\x12\n\nnetwork_id\x18\n \x01(\t\x12\x39\n\x06health\x18\x0b \x01(\x0e\x32).yandex.cloud.mdb.redis.v1.Cluster.Health\x12\x39\n\x06status\x18\x0c \x01(\x0e\x32).yandex.cloud.mdb.redis.v1.Cluster.Status\x12\x0f\n\x07sharded\x18\r \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"I\n\x0b\x45nvironment\x12\x1b\n\x17\x45NVIRONMENT_UNSPECIFIED\x10\x00\x12\x0e\n\nPRODUCTION\x10\x01\x12\r\n\tPRESTABLE\x10\x02\"?\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\"y\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x0c\n\x08STOPPING\x10\x05\x12\x0b\n\x07STOPPED\x10\x06\x12\x0c\n\x08STARTING\x10\x07\"=\n\nMonitoring\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\"\xa2\x02\n\rClusterConfig\x12\x0f\n\x07version\x18\x01 \x01(\t\x12O\n\x10redis_config_5_0\x18\x02 \x01(\x0b\x32\x33.yandex.cloud.mdb.redis.v1.config.RedisConfigSet5_0H\x00\x12\x37\n\tresources\x18\x03 \x01(\x0b\x32$.yandex.cloud.mdb.redis.v1.Resources\x12\x33\n\x13\x62\x61\x63kup_window_start\x18\x04 \x01(\x0b\x32\x16.google.type.TimeOfDay\x12\x31\n\x06\x61\x63\x63\x65ss\x18\x05 \x01(\x0b\x32!.yandex.cloud.mdb.redis.v1.AccessB\x0e\n\x0credis_config\")\n\x05Shard\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\"\xaf\x03\n\x04Host\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12\x0f\n\x07zone_id\x18\x03 \x01(\t\x12\x11\n\tsubnet_id\x18\x04 \x01(\t\x12\x37\n\tresources\x18\x05 \x01(\x0b\x32$.yandex.cloud.mdb.redis.v1.Resources\x12\x32\n\x04role\x18\x06 \x01(\x0e\x32$.yandex.cloud.mdb.redis.v1.Host.Role\x12\x36\n\x06health\x18\x07 \x01(\x0e\x32&.yandex.cloud.mdb.redis.v1.Host.Health\x12\x34\n\x08services\x18\x08 \x03(\x0b\x32\".yandex.cloud.mdb.redis.v1.Service\x12\x12\n\nshard_name\x18\t \x01(\t\"1\n\x04Role\x12\x10\n\x0cROLE_UNKNOWN\x10\x00\x12\n\n\x06MASTER\x10\x01\x12\x0b\n\x07REPLICA\x10\x02\"?\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\"\xf7\x01\n\x07Service\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32\'.yandex.cloud.mdb.redis.v1.Service.Type\x12\x39\n\x06health\x18\x02 \x01(\x0e\x32).yandex.cloud.mdb.redis.v1.Service.Health\"G\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05REDIS\x10\x01\x12\x0b\n\x07\x41RBITER\x10\x02\x12\x11\n\rREDIS_CLUSTER\x10\x03\"1\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\":\n\tResources\x12\x1a\n\x12resource_preset_id\x18\x01 \x01(\t\x12\x11\n\tdisk_size\x18\x02 \x01(\x03\"\x1b\n\x06\x41\x63\x63\x65ss\x12\x11\n\tdata_lens\x18\x01 \x01(\x08\x42\x64\n\x1dyandex.cloud.api.mdb.redis.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1;redisb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_type_dot_timeofday__pb2.DESCRIPTOR,yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_config_dot_redis5__0__pb2.DESCRIPTOR,])



_CLUSTER_ENVIRONMENT = _descriptor.EnumDescriptor(
  name='Environment',
  full_name='yandex.cloud.mdb.redis.v1.Cluster.Environment',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENVIRONMENT_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCTION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRESTABLE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=759,
  serialized_end=832,
)
_sym_db.RegisterEnumDescriptor(_CLUSTER_ENVIRONMENT)

_CLUSTER_HEALTH = _descriptor.EnumDescriptor(
  name='Health',
  full_name='yandex.cloud.mdb.redis.v1.Cluster.Health',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HEALTH_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALIVE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEAD', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEGRADED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=834,
  serialized_end=897,
)
_sym_db.RegisterEnumDescriptor(_CLUSTER_HEALTH)

_CLUSTER_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.mdb.redis.v1.Cluster.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATING', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOPPING', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STARTING', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=899,
  serialized_end=1020,
)
_sym_db.RegisterEnumDescriptor(_CLUSTER_STATUS)

_HOST_ROLE = _descriptor.EnumDescriptor(
  name='Role',
  full_name='yandex.cloud.mdb.redis.v1.Host.Role',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROLE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MASTER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPLICA', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1739,
  serialized_end=1788,
)
_sym_db.RegisterEnumDescriptor(_HOST_ROLE)

_HOST_HEALTH = _descriptor.EnumDescriptor(
  name='Health',
  full_name='yandex.cloud.mdb.redis.v1.Host.Health',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HEALTH_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALIVE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEAD', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEGRADED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=834,
  serialized_end=897,
)
_sym_db.RegisterEnumDescriptor(_HOST_HEALTH)

_SERVICE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='yandex.cloud.mdb.redis.v1.Service.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDIS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARBITER', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDIS_CLUSTER', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1981,
  serialized_end=2052,
)
_sym_db.RegisterEnumDescriptor(_SERVICE_TYPE)

_SERVICE_HEALTH = _descriptor.EnumDescriptor(
  name='Health',
  full_name='yandex.cloud.mdb.redis.v1.Service.Health',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HEALTH_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALIVE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEAD', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=834,
  serialized_end=883,
)
_sym_db.RegisterEnumDescriptor(_SERVICE_HEALTH)


_CLUSTER_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.mdb.redis.v1.Cluster.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.mdb.redis.v1.Cluster.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.mdb.redis.v1.Cluster.LabelsEntry.value', index=1,
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
  serialized_start=712,
  serialized_end=757,
)

_CLUSTER = _descriptor.Descriptor(
  name='Cluster',
  full_name='yandex.cloud.mdb.redis.v1.Cluster',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.mdb.redis.v1.Cluster.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.mdb.redis.v1.Cluster.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.mdb.redis.v1.Cluster.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.redis.v1.Cluster.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.mdb.redis.v1.Cluster.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.mdb.redis.v1.Cluster.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='environment', full_name='yandex.cloud.mdb.redis.v1.Cluster.environment', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='monitoring', full_name='yandex.cloud.mdb.redis.v1.Cluster.monitoring', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='yandex.cloud.mdb.redis.v1.Cluster.config', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_id', full_name='yandex.cloud.mdb.redis.v1.Cluster.network_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='health', full_name='yandex.cloud.mdb.redis.v1.Cluster.health', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.mdb.redis.v1.Cluster.status', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sharded', full_name='yandex.cloud.mdb.redis.v1.Cluster.sharded', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CLUSTER_LABELSENTRY, ],
  enum_types=[
    _CLUSTER_ENVIRONMENT,
    _CLUSTER_HEALTH,
    _CLUSTER_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=1020,
)


_MONITORING = _descriptor.Descriptor(
  name='Monitoring',
  full_name='yandex.cloud.mdb.redis.v1.Monitoring',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.redis.v1.Monitoring.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.mdb.redis.v1.Monitoring.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link', full_name='yandex.cloud.mdb.redis.v1.Monitoring.link', index=2,
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
  serialized_start=1022,
  serialized_end=1083,
)


_CLUSTERCONFIG = _descriptor.Descriptor(
  name='ClusterConfig',
  full_name='yandex.cloud.mdb.redis.v1.ClusterConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='yandex.cloud.mdb.redis.v1.ClusterConfig.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='redis_config_5_0', full_name='yandex.cloud.mdb.redis.v1.ClusterConfig.redis_config_5_0', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resources', full_name='yandex.cloud.mdb.redis.v1.ClusterConfig.resources', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backup_window_start', full_name='yandex.cloud.mdb.redis.v1.ClusterConfig.backup_window_start', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access', full_name='yandex.cloud.mdb.redis.v1.ClusterConfig.access', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='redis_config', full_name='yandex.cloud.mdb.redis.v1.ClusterConfig.redis_config',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1086,
  serialized_end=1376,
)


_SHARD = _descriptor.Descriptor(
  name='Shard',
  full_name='yandex.cloud.mdb.redis.v1.Shard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.redis.v1.Shard.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.redis.v1.Shard.cluster_id', index=1,
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
  serialized_start=1378,
  serialized_end=1419,
)


_HOST = _descriptor.Descriptor(
  name='Host',
  full_name='yandex.cloud.mdb.redis.v1.Host',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.redis.v1.Host.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.redis.v1.Host.cluster_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zone_id', full_name='yandex.cloud.mdb.redis.v1.Host.zone_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subnet_id', full_name='yandex.cloud.mdb.redis.v1.Host.subnet_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resources', full_name='yandex.cloud.mdb.redis.v1.Host.resources', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='yandex.cloud.mdb.redis.v1.Host.role', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='health', full_name='yandex.cloud.mdb.redis.v1.Host.health', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='services', full_name='yandex.cloud.mdb.redis.v1.Host.services', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shard_name', full_name='yandex.cloud.mdb.redis.v1.Host.shard_name', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HOST_ROLE,
    _HOST_HEALTH,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1422,
  serialized_end=1853,
)


_SERVICE = _descriptor.Descriptor(
  name='Service',
  full_name='yandex.cloud.mdb.redis.v1.Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.mdb.redis.v1.Service.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='health', full_name='yandex.cloud.mdb.redis.v1.Service.health', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVICE_TYPE,
    _SERVICE_HEALTH,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1856,
  serialized_end=2103,
)


_RESOURCES = _descriptor.Descriptor(
  name='Resources',
  full_name='yandex.cloud.mdb.redis.v1.Resources',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_preset_id', full_name='yandex.cloud.mdb.redis.v1.Resources.resource_preset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_size', full_name='yandex.cloud.mdb.redis.v1.Resources.disk_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=2105,
  serialized_end=2163,
)


_ACCESS = _descriptor.Descriptor(
  name='Access',
  full_name='yandex.cloud.mdb.redis.v1.Access',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_lens', full_name='yandex.cloud.mdb.redis.v1.Access.data_lens', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=2165,
  serialized_end=2192,
)

_CLUSTER_LABELSENTRY.containing_type = _CLUSTER
_CLUSTER.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CLUSTER.fields_by_name['labels'].message_type = _CLUSTER_LABELSENTRY
_CLUSTER.fields_by_name['environment'].enum_type = _CLUSTER_ENVIRONMENT
_CLUSTER.fields_by_name['monitoring'].message_type = _MONITORING
_CLUSTER.fields_by_name['config'].message_type = _CLUSTERCONFIG
_CLUSTER.fields_by_name['health'].enum_type = _CLUSTER_HEALTH
_CLUSTER.fields_by_name['status'].enum_type = _CLUSTER_STATUS
_CLUSTER_ENVIRONMENT.containing_type = _CLUSTER
_CLUSTER_HEALTH.containing_type = _CLUSTER
_CLUSTER_STATUS.containing_type = _CLUSTER
_CLUSTERCONFIG.fields_by_name['redis_config_5_0'].message_type = yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_config_dot_redis5__0__pb2._REDISCONFIGSET5_0
_CLUSTERCONFIG.fields_by_name['resources'].message_type = _RESOURCES
_CLUSTERCONFIG.fields_by_name['backup_window_start'].message_type = google_dot_type_dot_timeofday__pb2._TIMEOFDAY
_CLUSTERCONFIG.fields_by_name['access'].message_type = _ACCESS
_CLUSTERCONFIG.oneofs_by_name['redis_config'].fields.append(
  _CLUSTERCONFIG.fields_by_name['redis_config_5_0'])
_CLUSTERCONFIG.fields_by_name['redis_config_5_0'].containing_oneof = _CLUSTERCONFIG.oneofs_by_name['redis_config']
_HOST.fields_by_name['resources'].message_type = _RESOURCES
_HOST.fields_by_name['role'].enum_type = _HOST_ROLE
_HOST.fields_by_name['health'].enum_type = _HOST_HEALTH
_HOST.fields_by_name['services'].message_type = _SERVICE
_HOST_ROLE.containing_type = _HOST
_HOST_HEALTH.containing_type = _HOST
_SERVICE.fields_by_name['type'].enum_type = _SERVICE_TYPE
_SERVICE.fields_by_name['health'].enum_type = _SERVICE_HEALTH
_SERVICE_TYPE.containing_type = _SERVICE
_SERVICE_HEALTH.containing_type = _SERVICE
DESCRIPTOR.message_types_by_name['Cluster'] = _CLUSTER
DESCRIPTOR.message_types_by_name['Monitoring'] = _MONITORING
DESCRIPTOR.message_types_by_name['ClusterConfig'] = _CLUSTERCONFIG
DESCRIPTOR.message_types_by_name['Shard'] = _SHARD
DESCRIPTOR.message_types_by_name['Host'] = _HOST
DESCRIPTOR.message_types_by_name['Service'] = _SERVICE
DESCRIPTOR.message_types_by_name['Resources'] = _RESOURCES
DESCRIPTOR.message_types_by_name['Access'] = _ACCESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Cluster = _reflection.GeneratedProtocolMessageType('Cluster', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CLUSTER_LABELSENTRY,
    '__module__' : 'yandex.cloud.mdb.redis.v1.cluster_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1.Cluster.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CLUSTER,
  '__module__' : 'yandex.cloud.mdb.redis.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1.Cluster)
  })
_sym_db.RegisterMessage(Cluster)
_sym_db.RegisterMessage(Cluster.LabelsEntry)

Monitoring = _reflection.GeneratedProtocolMessageType('Monitoring', (_message.Message,), {
  'DESCRIPTOR' : _MONITORING,
  '__module__' : 'yandex.cloud.mdb.redis.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1.Monitoring)
  })
_sym_db.RegisterMessage(Monitoring)

ClusterConfig = _reflection.GeneratedProtocolMessageType('ClusterConfig', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTERCONFIG,
  '__module__' : 'yandex.cloud.mdb.redis.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1.ClusterConfig)
  })
_sym_db.RegisterMessage(ClusterConfig)

Shard = _reflection.GeneratedProtocolMessageType('Shard', (_message.Message,), {
  'DESCRIPTOR' : _SHARD,
  '__module__' : 'yandex.cloud.mdb.redis.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1.Shard)
  })
_sym_db.RegisterMessage(Shard)

Host = _reflection.GeneratedProtocolMessageType('Host', (_message.Message,), {
  'DESCRIPTOR' : _HOST,
  '__module__' : 'yandex.cloud.mdb.redis.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1.Host)
  })
_sym_db.RegisterMessage(Host)

Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), {
  'DESCRIPTOR' : _SERVICE,
  '__module__' : 'yandex.cloud.mdb.redis.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1.Service)
  })
_sym_db.RegisterMessage(Service)

Resources = _reflection.GeneratedProtocolMessageType('Resources', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCES,
  '__module__' : 'yandex.cloud.mdb.redis.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1.Resources)
  })
_sym_db.RegisterMessage(Resources)

Access = _reflection.GeneratedProtocolMessageType('Access', (_message.Message,), {
  'DESCRIPTOR' : _ACCESS,
  '__module__' : 'yandex.cloud.mdb.redis.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1.Access)
  })
_sym_db.RegisterMessage(Access)


DESCRIPTOR._options = None
_CLUSTER_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
