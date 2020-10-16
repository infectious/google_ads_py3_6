# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v2.proto.resources import feed_placeholder_view_pb2 as google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_feed__placeholder__view__pb2
from google.ads.google_ads.v2.proto.services import feed_placeholder_view_service_pb2 as google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_feed__placeholder__view__service__pb2


class FeedPlaceholderViewServiceStub(object):
  """Proto file describing the FeedPlaceholderView service.

  Service to fetch feed placeholder views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFeedPlaceholderView = channel.unary_unary(
        '/google.ads.googleads.v2.services.FeedPlaceholderViewService/GetFeedPlaceholderView',
        request_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_feed__placeholder__view__service__pb2.GetFeedPlaceholderViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_feed__placeholder__view__pb2.FeedPlaceholderView.FromString,
        )


class FeedPlaceholderViewServiceServicer(object):
  """Proto file describing the FeedPlaceholderView service.

  Service to fetch feed placeholder views.
  """

  def GetFeedPlaceholderView(self, request, context):
    """Returns the requested feed placeholder view in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FeedPlaceholderViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFeedPlaceholderView': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeedPlaceholderView,
          request_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_feed__placeholder__view__service__pb2.GetFeedPlaceholderViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_feed__placeholder__view__pb2.FeedPlaceholderView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v2.services.FeedPlaceholderViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
