# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.mdb.mysql.v1 import cluster_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__pb2
from yandex.cloud.mdb.mysql.v1 import cluster_service_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class ClusterServiceStub(object):
    """A set of methods for managing MySQL clusters.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/Get',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.GetClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__pb2.Cluster.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/List',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClustersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClustersResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/Create',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.CreateClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/Update',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.UpdateClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/Delete',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.DeleteClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Start = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/Start',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.StartClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Stop = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/Stop',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.StopClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Move = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/Move',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.MoveClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Backup = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/Backup',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.BackupClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Restore = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/Restore',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.RestoreClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.RescheduleMaintenance = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/RescheduleMaintenance',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.RescheduleMaintenanceRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.StartFailover = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/StartFailover',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.StartClusterFailoverRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListLogs = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/ListLogs',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterLogsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterLogsResponse.FromString,
                )
        self.StreamLogs = channel.unary_stream(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/StreamLogs',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.StreamClusterLogsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.StreamLogRecord.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterOperationsResponse.FromString,
                )
        self.ListBackups = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/ListBackups',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterBackupsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterBackupsResponse.FromString,
                )
        self.ListHosts = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/ListHosts',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterHostsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterHostsResponse.FromString,
                )
        self.AddHosts = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/AddHosts',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.AddClusterHostsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.UpdateHosts = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/UpdateHosts',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.UpdateClusterHostsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.DeleteHosts = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1.ClusterService/DeleteHosts',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.DeleteClusterHostsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class ClusterServiceServicer(object):
    """A set of methods for managing MySQL clusters.
    """

    def Get(self, request, context):
        """Returns the specified MySQL cluster.

        To get the list of available MySQL clusters, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of MySQL clusters that belong to the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a MySQL cluster in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Modifies the specified MySQL cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified MySQL cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Start(self, request, context):
        """Starts the specified MySQL cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stop(self, request, context):
        """Stops the specified MySQL cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Move(self, request, context):
        """Moves the specified MySQL cluster to the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Backup(self, request, context):
        """Creates a backup for the specified MySQL cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Restore(self, request, context):
        """Creates a new MySQL cluster using the specified backup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RescheduleMaintenance(self, request, context):
        """Reschedules planned maintenance operation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartFailover(self, request, context):
        """Start a manual failover on the specified MySQL cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListLogs(self, request, context):
        """Retrieves logs for the specified MySQL cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamLogs(self, request, context):
        """Same as ListLogs but using server-side streaming. Also allows for 'tail -f' semantics.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Retrieves the list of operations for the specified MySQL cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBackups(self, request, context):
        """Retrieves the list of available backups for the specified MySQL cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListHosts(self, request, context):
        """Retrieves a list of hosts for the specified MySQL cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddHosts(self, request, context):
        """Creates new hosts for a cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateHosts(self, request, context):
        """Updates the specified hosts.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteHosts(self, request, context):
        """Deletes the specified hosts for a cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClusterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.GetClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__pb2.Cluster.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClustersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClustersResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.CreateClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.UpdateClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.DeleteClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.StartClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Stop': grpc.unary_unary_rpc_method_handler(
                    servicer.Stop,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.StopClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Move': grpc.unary_unary_rpc_method_handler(
                    servicer.Move,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.MoveClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Backup': grpc.unary_unary_rpc_method_handler(
                    servicer.Backup,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.BackupClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Restore': grpc.unary_unary_rpc_method_handler(
                    servicer.Restore,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.RestoreClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'RescheduleMaintenance': grpc.unary_unary_rpc_method_handler(
                    servicer.RescheduleMaintenance,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.RescheduleMaintenanceRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'StartFailover': grpc.unary_unary_rpc_method_handler(
                    servicer.StartFailover,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.StartClusterFailoverRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListLogs': grpc.unary_unary_rpc_method_handler(
                    servicer.ListLogs,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterLogsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterLogsResponse.SerializeToString,
            ),
            'StreamLogs': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamLogs,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.StreamClusterLogsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.StreamLogRecord.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterOperationsResponse.SerializeToString,
            ),
            'ListBackups': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBackups,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterBackupsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterBackupsResponse.SerializeToString,
            ),
            'ListHosts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListHosts,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterHostsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterHostsResponse.SerializeToString,
            ),
            'AddHosts': grpc.unary_unary_rpc_method_handler(
                    servicer.AddHosts,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.AddClusterHostsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateHosts': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateHosts,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.UpdateClusterHostsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeleteHosts': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteHosts,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.DeleteClusterHostsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.mdb.mysql.v1.ClusterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClusterService(object):
    """A set of methods for managing MySQL clusters.
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/Get',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.GetClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__pb2.Cluster.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/List',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClustersRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClustersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/Create',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.CreateClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/Update',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.UpdateClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/Delete',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.DeleteClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Start(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/Start',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.StartClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/Stop',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.StopClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Move(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/Move',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.MoveClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Backup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/Backup',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.BackupClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Restore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/Restore',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.RestoreClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RescheduleMaintenance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/RescheduleMaintenance',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.RescheduleMaintenanceRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartFailover(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/StartFailover',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.StartClusterFailoverRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListLogs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/ListLogs',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterLogsRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterLogsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamLogs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/StreamLogs',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.StreamClusterLogsRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.StreamLogRecord.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/ListOperations',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListBackups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/ListBackups',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterBackupsRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterBackupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListHosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/ListHosts',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterHostsRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.ListClusterHostsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddHosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/AddHosts',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.AddClusterHostsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateHosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/UpdateHosts',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.UpdateClusterHostsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteHosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.mysql.v1.ClusterService/DeleteHosts',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_cluster__service__pb2.DeleteClusterHostsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
