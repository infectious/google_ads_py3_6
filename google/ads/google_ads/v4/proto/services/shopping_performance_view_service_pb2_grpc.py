# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v4.proto.resources import shopping_performance_view_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_shopping__performance__view__pb2
from google.ads.google_ads.v4.proto.services import shopping_performance_view_service_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_shopping__performance__view__service__pb2


class ShoppingPerformanceViewServiceStub(object):
  """Proto file describing the ShoppingPerformanceView service.

  Service to fetch Shopping performance views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetShoppingPerformanceView = channel.unary_unary(
        '/google.ads.googleads.v4.services.ShoppingPerformanceViewService/GetShoppingPerformanceView',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_shopping__performance__view__service__pb2.GetShoppingPerformanceViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_shopping__performance__view__pb2.ShoppingPerformanceView.FromString,
        )


class ShoppingPerformanceViewServiceServicer(object):
  """Proto file describing the ShoppingPerformanceView service.

  Service to fetch Shopping performance views.
  """

  def GetShoppingPerformanceView(self, request, context):
    """Returns the requested Shopping performance view in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ShoppingPerformanceViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetShoppingPerformanceView': grpc.unary_unary_rpc_method_handler(
          servicer.GetShoppingPerformanceView,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_shopping__performance__view__service__pb2.GetShoppingPerformanceViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_shopping__performance__view__pb2.ShoppingPerformanceView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v4.services.ShoppingPerformanceViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
