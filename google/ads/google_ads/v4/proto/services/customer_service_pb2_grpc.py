# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v4.proto.resources import customer_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_customer__pb2
from google.ads.google_ads.v4.proto.services import customer_service_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_customer__service__pb2


class CustomerServiceStub(object):
  """Proto file describing the Customer service.

  Service to manage customers.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCustomer = channel.unary_unary(
        '/google.ads.googleads.v4.services.CustomerService/GetCustomer',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_customer__service__pb2.GetCustomerRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_customer__pb2.Customer.FromString,
        )
    self.MutateCustomer = channel.unary_unary(
        '/google.ads.googleads.v4.services.CustomerService/MutateCustomer',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_customer__service__pb2.MutateCustomerRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_customer__service__pb2.MutateCustomerResponse.FromString,
        )
    self.ListAccessibleCustomers = channel.unary_unary(
        '/google.ads.googleads.v4.services.CustomerService/ListAccessibleCustomers',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_customer__service__pb2.ListAccessibleCustomersRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_customer__service__pb2.ListAccessibleCustomersResponse.FromString,
        )
    self.CreateCustomerClient = channel.unary_unary(
        '/google.ads.googleads.v4.services.CustomerService/CreateCustomerClient',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_customer__service__pb2.CreateCustomerClientRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_customer__service__pb2.CreateCustomerClientResponse.FromString,
        )


class CustomerServiceServicer(object):
  """Proto file describing the Customer service.

  Service to manage customers.
  """

  def GetCustomer(self, request, context):
    """Returns the requested customer in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateCustomer(self, request, context):
    """Updates a customer. Operation statuses are returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListAccessibleCustomers(self, request, context):
    """Returns resource names of customers directly accessible by the
    user authenticating the call.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateCustomerClient(self, request, context):
    """Creates a new client under manager. The new client customer is returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CustomerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCustomer': grpc.unary_unary_rpc_method_handler(
          servicer.GetCustomer,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_customer__service__pb2.GetCustomerRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_customer__pb2.Customer.SerializeToString,
      ),
      'MutateCustomer': grpc.unary_unary_rpc_method_handler(
          servicer.MutateCustomer,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_customer__service__pb2.MutateCustomerRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_customer__service__pb2.MutateCustomerResponse.SerializeToString,
      ),
      'ListAccessibleCustomers': grpc.unary_unary_rpc_method_handler(
          servicer.ListAccessibleCustomers,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_customer__service__pb2.ListAccessibleCustomersRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_customer__service__pb2.ListAccessibleCustomersResponse.SerializeToString,
      ),
      'CreateCustomerClient': grpc.unary_unary_rpc_method_handler(
          servicer.CreateCustomerClient,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_customer__service__pb2.CreateCustomerClientRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_customer__service__pb2.CreateCustomerClientResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v4.services.CustomerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
