# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v4.proto.resources import campaign_budget_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_campaign__budget__pb2
from google.ads.google_ads.v4.proto.services import campaign_budget_service_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_campaign__budget__service__pb2


class CampaignBudgetServiceStub(object):
  """Proto file describing the Campaign Budget service.

  Service to manage campaign budgets.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCampaignBudget = channel.unary_unary(
        '/google.ads.googleads.v4.services.CampaignBudgetService/GetCampaignBudget',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_campaign__budget__service__pb2.GetCampaignBudgetRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_campaign__budget__pb2.CampaignBudget.FromString,
        )
    self.MutateCampaignBudgets = channel.unary_unary(
        '/google.ads.googleads.v4.services.CampaignBudgetService/MutateCampaignBudgets',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_campaign__budget__service__pb2.MutateCampaignBudgetsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_campaign__budget__service__pb2.MutateCampaignBudgetsResponse.FromString,
        )


class CampaignBudgetServiceServicer(object):
  """Proto file describing the Campaign Budget service.

  Service to manage campaign budgets.
  """

  def GetCampaignBudget(self, request, context):
    """Returns the requested Campaign Budget in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateCampaignBudgets(self, request, context):
    """Creates, updates, or removes campaign budgets. Operation statuses are
    returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CampaignBudgetServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCampaignBudget': grpc.unary_unary_rpc_method_handler(
          servicer.GetCampaignBudget,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_campaign__budget__service__pb2.GetCampaignBudgetRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_campaign__budget__pb2.CampaignBudget.SerializeToString,
      ),
      'MutateCampaignBudgets': grpc.unary_unary_rpc_method_handler(
          servicer.MutateCampaignBudgets,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_campaign__budget__service__pb2.MutateCampaignBudgetsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_campaign__budget__service__pb2.MutateCampaignBudgetsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v4.services.CampaignBudgetService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
