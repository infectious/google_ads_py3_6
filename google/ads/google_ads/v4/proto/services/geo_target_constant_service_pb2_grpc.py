# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v4.proto.resources import geo_target_constant_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_geo__target__constant__pb2
from google.ads.google_ads.v4.proto.services import geo_target_constant_service_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_geo__target__constant__service__pb2


class GeoTargetConstantServiceStub(object):
  """Proto file describing the Geo target constant service.

  Service to fetch geo target constants.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetGeoTargetConstant = channel.unary_unary(
        '/google.ads.googleads.v4.services.GeoTargetConstantService/GetGeoTargetConstant',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_geo__target__constant__service__pb2.GetGeoTargetConstantRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_geo__target__constant__pb2.GeoTargetConstant.FromString,
        )
    self.SuggestGeoTargetConstants = channel.unary_unary(
        '/google.ads.googleads.v4.services.GeoTargetConstantService/SuggestGeoTargetConstants',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_geo__target__constant__service__pb2.SuggestGeoTargetConstantsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_geo__target__constant__service__pb2.SuggestGeoTargetConstantsResponse.FromString,
        )


class GeoTargetConstantServiceServicer(object):
  """Proto file describing the Geo target constant service.

  Service to fetch geo target constants.
  """

  def GetGeoTargetConstant(self, request, context):
    """Returns the requested geo target constant in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SuggestGeoTargetConstants(self, request, context):
    """Returns GeoTargetConstant suggestions by location name or by resource name.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GeoTargetConstantServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetGeoTargetConstant': grpc.unary_unary_rpc_method_handler(
          servicer.GetGeoTargetConstant,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_geo__target__constant__service__pb2.GetGeoTargetConstantRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_geo__target__constant__pb2.GeoTargetConstant.SerializeToString,
      ),
      'SuggestGeoTargetConstants': grpc.unary_unary_rpc_method_handler(
          servicer.SuggestGeoTargetConstants,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_geo__target__constant__service__pb2.SuggestGeoTargetConstantsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_geo__target__constant__service__pb2.SuggestGeoTargetConstantsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v4.services.GeoTargetConstantService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
