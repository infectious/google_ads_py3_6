# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v4.proto.resources import ad_group_criterion_simulation_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__group__criterion__simulation__pb2
from google.ads.google_ads.v4.proto.services import ad_group_criterion_simulation_service_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_ad__group__criterion__simulation__service__pb2


class AdGroupCriterionSimulationServiceStub(object):
  """Proto file describing the AdGroupCriterionSimulation service.

  Service to fetch ad group criterion simulations.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAdGroupCriterionSimulation = channel.unary_unary(
        '/google.ads.googleads.v4.services.AdGroupCriterionSimulationService/GetAdGroupCriterionSimulation',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_ad__group__criterion__simulation__service__pb2.GetAdGroupCriterionSimulationRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__group__criterion__simulation__pb2.AdGroupCriterionSimulation.FromString,
        )


class AdGroupCriterionSimulationServiceServicer(object):
  """Proto file describing the AdGroupCriterionSimulation service.

  Service to fetch ad group criterion simulations.
  """

  def GetAdGroupCriterionSimulation(self, request, context):
    """Returns the requested ad group criterion simulation in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AdGroupCriterionSimulationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAdGroupCriterionSimulation': grpc.unary_unary_rpc_method_handler(
          servicer.GetAdGroupCriterionSimulation,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_ad__group__criterion__simulation__service__pb2.GetAdGroupCriterionSimulationRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__group__criterion__simulation__pb2.AdGroupCriterionSimulation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v4.services.AdGroupCriterionSimulationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
