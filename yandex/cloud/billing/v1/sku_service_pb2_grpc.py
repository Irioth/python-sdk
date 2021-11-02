# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.billing.v1 import sku_pb2 as yandex_dot_cloud_dot_billing_dot_v1_dot_sku__pb2
from yandex.cloud.billing.v1 import sku_service_pb2 as yandex_dot_cloud_dot_billing_dot_v1_dot_sku__service__pb2


class SkuServiceStub(object):
    """A set of methods for managing Sku resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.billing.v1.SkuService/Get',
                request_serializer=yandex_dot_cloud_dot_billing_dot_v1_dot_sku__service__pb2.GetSkuRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_billing_dot_v1_dot_sku__pb2.Sku.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.billing.v1.SkuService/List',
                request_serializer=yandex_dot_cloud_dot_billing_dot_v1_dot_sku__service__pb2.ListSkusRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_billing_dot_v1_dot_sku__service__pb2.ListSkusResponse.FromString,
                )


class SkuServiceServicer(object):
    """A set of methods for managing Sku resources.
    """

    def Get(self, request, context):
        """Returns the specified SKU.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of SKUs.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SkuServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_billing_dot_v1_dot_sku__service__pb2.GetSkuRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_billing_dot_v1_dot_sku__pb2.Sku.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_billing_dot_v1_dot_sku__service__pb2.ListSkusRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_billing_dot_v1_dot_sku__service__pb2.ListSkusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.billing.v1.SkuService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SkuService(object):
    """A set of methods for managing Sku resources.
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.billing.v1.SkuService/Get',
            yandex_dot_cloud_dot_billing_dot_v1_dot_sku__service__pb2.GetSkuRequest.SerializeToString,
            yandex_dot_cloud_dot_billing_dot_v1_dot_sku__pb2.Sku.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.billing.v1.SkuService/List',
            yandex_dot_cloud_dot_billing_dot_v1_dot_sku__service__pb2.ListSkusRequest.SerializeToString,
            yandex_dot_cloud_dot_billing_dot_v1_dot_sku__service__pb2.ListSkusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)