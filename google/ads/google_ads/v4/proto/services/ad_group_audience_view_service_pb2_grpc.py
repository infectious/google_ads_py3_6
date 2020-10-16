# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v4.proto.resources import ad_group_audience_view_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__group__audience__view__pb2
from google.ads.google_ads.v4.proto.services import ad_group_audience_view_service_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_ad__group__audience__view__service__pb2


class AdGroupAudienceViewServiceStub(object):
  """Proto file describing the AdGroup Audience View service.

  Service to manage ad group audience views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAdGroupAudienceView = channel.unary_unary(
        '/google.ads.googleads.v4.services.AdGroupAudienceViewService/GetAdGroupAudienceView',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_ad__group__audience__view__service__pb2.GetAdGroupAudienceViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__group__audience__view__pb2.AdGroupAudienceView.FromString,
        )


class AdGroupAudienceViewServiceServicer(object):
  """Proto file describing the AdGroup Audience View service.

  Service to manage ad group audience views.
  """

  def GetAdGroupAudienceView(self, request, context):
    """Returns the requested ad group audience view in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AdGroupAudienceViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAdGroupAudienceView': grpc.unary_unary_rpc_method_handler(
          servicer.GetAdGroupAudienceView,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_ad__group__audience__view__service__pb2.GetAdGroupAudienceViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__group__audience__view__pb2.AdGroupAudienceView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v4.services.AdGroupAudienceViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
