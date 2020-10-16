# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v4.proto.resources import account_budget_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_account__budget__pb2
from google.ads.google_ads.v4.proto.services import account_budget_service_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_account__budget__service__pb2


class AccountBudgetServiceStub(object):
  """Proto file describing the AccountBudget service.

  A service for fetching an account-level budget.

  Account-level budgets are mutated by creating proposal resources.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAccountBudget = channel.unary_unary(
        '/google.ads.googleads.v4.services.AccountBudgetService/GetAccountBudget',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_account__budget__service__pb2.GetAccountBudgetRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_account__budget__pb2.AccountBudget.FromString,
        )


class AccountBudgetServiceServicer(object):
  """Proto file describing the AccountBudget service.

  A service for fetching an account-level budget.

  Account-level budgets are mutated by creating proposal resources.
  """

  def GetAccountBudget(self, request, context):
    """Returns an account-level budget in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AccountBudgetServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAccountBudget': grpc.unary_unary_rpc_method_handler(
          servicer.GetAccountBudget,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_account__budget__service__pb2.GetAccountBudgetRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_account__budget__pb2.AccountBudget.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v4.services.AccountBudgetService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
