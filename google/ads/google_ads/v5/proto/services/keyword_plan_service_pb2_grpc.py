# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v5.proto.resources import keyword_plan_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_keyword__plan__pb2
from google.ads.google_ads.v5.proto.services import keyword_plan_service_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2


class KeywordPlanServiceStub(object):
    """Proto file describing the keyword plan service.

    Service to manage keyword plans.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetKeywordPlan = channel.unary_unary(
                '/google.ads.googleads.v5.services.KeywordPlanService/GetKeywordPlan',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GetKeywordPlanRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_keyword__plan__pb2.KeywordPlan.FromString,
                )
        self.MutateKeywordPlans = channel.unary_unary(
                '/google.ads.googleads.v5.services.KeywordPlanService/MutateKeywordPlans',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.MutateKeywordPlansRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.MutateKeywordPlansResponse.FromString,
                )
        self.GenerateForecastCurve = channel.unary_unary(
                '/google.ads.googleads.v5.services.KeywordPlanService/GenerateForecastCurve',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastCurveRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastCurveResponse.FromString,
                )
        self.GenerateForecastTimeSeries = channel.unary_unary(
                '/google.ads.googleads.v5.services.KeywordPlanService/GenerateForecastTimeSeries',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastTimeSeriesRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastTimeSeriesResponse.FromString,
                )
        self.GenerateForecastMetrics = channel.unary_unary(
                '/google.ads.googleads.v5.services.KeywordPlanService/GenerateForecastMetrics',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastMetricsRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastMetricsResponse.FromString,
                )
        self.GenerateHistoricalMetrics = channel.unary_unary(
                '/google.ads.googleads.v5.services.KeywordPlanService/GenerateHistoricalMetrics',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateHistoricalMetricsRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateHistoricalMetricsResponse.FromString,
                )


class KeywordPlanServiceServicer(object):
    """Proto file describing the keyword plan service.

    Service to manage keyword plans.
    """

    def GetKeywordPlan(self, request, context):
        """Returns the requested plan in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MutateKeywordPlans(self, request, context):
        """Creates, updates, or removes keyword plans. Operation statuses are
        returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateForecastCurve(self, request, context):
        """Returns the requested Keyword Plan forecast curve.
        Only the bidding strategy is considered for generating forecast curve.
        The bidding strategy value specified in the plan is ignored.

        To generate a forecast at a value specified in the plan, use
        KeywordPlanService.GenerateForecastMetrics.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateForecastTimeSeries(self, request, context):
        """Returns a forecast in the form of a time series for the Keyword Plan over
        the next 52 weeks.
        (1) Forecasts closer to the current date are generally more accurate than
        further out.

        (2) The forecast reflects seasonal trends using current and
        prior traffic patterns. The forecast period of the plan is ignored.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateForecastMetrics(self, request, context):
        """Returns the requested Keyword Plan forecasts.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateHistoricalMetrics(self, request, context):
        """Returns the requested Keyword Plan historical metrics.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KeywordPlanServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetKeywordPlan': grpc.unary_unary_rpc_method_handler(
                    servicer.GetKeywordPlan,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GetKeywordPlanRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_keyword__plan__pb2.KeywordPlan.SerializeToString,
            ),
            'MutateKeywordPlans': grpc.unary_unary_rpc_method_handler(
                    servicer.MutateKeywordPlans,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.MutateKeywordPlansRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.MutateKeywordPlansResponse.SerializeToString,
            ),
            'GenerateForecastCurve': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateForecastCurve,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastCurveRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastCurveResponse.SerializeToString,
            ),
            'GenerateForecastTimeSeries': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateForecastTimeSeries,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastTimeSeriesRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastTimeSeriesResponse.SerializeToString,
            ),
            'GenerateForecastMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateForecastMetrics,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastMetricsRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastMetricsResponse.SerializeToString,
            ),
            'GenerateHistoricalMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateHistoricalMetrics,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateHistoricalMetricsRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateHistoricalMetricsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v5.services.KeywordPlanService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KeywordPlanService(object):
    """Proto file describing the keyword plan service.

    Service to manage keyword plans.
    """

    @staticmethod
    def GetKeywordPlan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.KeywordPlanService/GetKeywordPlan',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GetKeywordPlanRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_keyword__plan__pb2.KeywordPlan.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MutateKeywordPlans(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.KeywordPlanService/MutateKeywordPlans',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.MutateKeywordPlansRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.MutateKeywordPlansResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenerateForecastCurve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.KeywordPlanService/GenerateForecastCurve',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastCurveRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastCurveResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenerateForecastTimeSeries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.KeywordPlanService/GenerateForecastTimeSeries',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastTimeSeriesRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastTimeSeriesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenerateForecastMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.KeywordPlanService/GenerateForecastMetrics',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastMetricsRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateForecastMetricsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenerateHistoricalMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.KeywordPlanService/GenerateHistoricalMetrics',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateHistoricalMetricsRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__service__pb2.GenerateHistoricalMetricsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
