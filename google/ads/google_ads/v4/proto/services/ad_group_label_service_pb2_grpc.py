# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v4.proto.resources import ad_group_label_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__group__label__pb2
from google.ads.google_ads.v4.proto.services import ad_group_label_service_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_ad__group__label__service__pb2


class AdGroupLabelServiceStub(object):
  """Proto file describing the Ad Group Label service.

  Service to manage labels on ad groups.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAdGroupLabel = channel.unary_unary(
        '/google.ads.googleads.v4.services.AdGroupLabelService/GetAdGroupLabel',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_ad__group__label__service__pb2.GetAdGroupLabelRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__group__label__pb2.AdGroupLabel.FromString,
        )
    self.MutateAdGroupLabels = channel.unary_unary(
        '/google.ads.googleads.v4.services.AdGroupLabelService/MutateAdGroupLabels',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_ad__group__label__service__pb2.MutateAdGroupLabelsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_ad__group__label__service__pb2.MutateAdGroupLabelsResponse.FromString,
        )


class AdGroupLabelServiceServicer(object):
  """Proto file describing the Ad Group Label service.

  Service to manage labels on ad groups.
  """

  def GetAdGroupLabel(self, request, context):
    """Returns the requested ad group label in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateAdGroupLabels(self, request, context):
    """Creates and removes ad group labels.
    Operation statuses are returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AdGroupLabelServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAdGroupLabel': grpc.unary_unary_rpc_method_handler(
          servicer.GetAdGroupLabel,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_ad__group__label__service__pb2.GetAdGroupLabelRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__group__label__pb2.AdGroupLabel.SerializeToString,
      ),
      'MutateAdGroupLabels': grpc.unary_unary_rpc_method_handler(
          servicer.MutateAdGroupLabels,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_ad__group__label__service__pb2.MutateAdGroupLabelsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_ad__group__label__service__pb2.MutateAdGroupLabelsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v4.services.AdGroupLabelService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
