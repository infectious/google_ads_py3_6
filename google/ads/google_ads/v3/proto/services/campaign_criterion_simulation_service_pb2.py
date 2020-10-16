# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/services/campaign_criterion_simulation_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.resources import campaign_criterion_simulation_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_campaign__criterion__simulation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/services/campaign_criterion_simulation_service.proto',
  package='google.ads.googleads.v3.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v3.servicesB\'CampaignCriterionSimulationServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v3/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V3.Services\312\002 Google\\Ads\\GoogleAds\\V3\\Services\352\002$Google::Ads::GoogleAds::V3::Services'),
  serialized_pb=_b('\nRgoogle/ads/googleads_v3/proto/services/campaign_criterion_simulation_service.proto\x12 google.ads.googleads.v3.services\x1aKgoogle/ads/googleads_v3/proto/resources/campaign_criterion_simulation.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"|\n%GetCampaignCriterionSimulationRequest\x12S\n\rresource_name\x18\x01 \x01(\tB<\xe0\x41\x02\xfa\x41\x36\n4googleads.googleapis.com/CampaignCriterionSimulation2\xc5\x02\n\"CampaignCriterionSimulationService\x12\x81\x02\n\x1eGetCampaignCriterionSimulation\x12G.google.ads.googleads.v3.services.GetCampaignCriterionSimulationRequest\x1a>.google.ads.googleads.v3.resources.CampaignCriterionSimulation\"V\x82\xd3\xe4\x93\x02@\x12>/v3/{resource_name=customers/*/campaignCriterionSimulations/*}\xda\x41\rresource_name\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x8e\x02\n$com.google.ads.googleads.v3.servicesB\'CampaignCriterionSimulationServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v3/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V3.Services\xca\x02 Google\\Ads\\GoogleAds\\V3\\Services\xea\x02$Google::Ads::GoogleAds::V3::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_campaign__criterion__simulation__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,])




_GETCAMPAIGNCRITERIONSIMULATIONREQUEST = _descriptor.Descriptor(
  name='GetCampaignCriterionSimulationRequest',
  full_name='google.ads.googleads.v3.services.GetCampaignCriterionSimulationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.services.GetCampaignCriterionSimulationRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002\372A6\n4googleads.googleapis.com/CampaignCriterionSimulation'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=312,
  serialized_end=436,
)

DESCRIPTOR.message_types_by_name['GetCampaignCriterionSimulationRequest'] = _GETCAMPAIGNCRITERIONSIMULATIONREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCampaignCriterionSimulationRequest = _reflection.GeneratedProtocolMessageType('GetCampaignCriterionSimulationRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCAMPAIGNCRITERIONSIMULATIONREQUEST,
  __module__ = 'google.ads.googleads_v3.proto.services.campaign_criterion_simulation_service_pb2'
  ,
  __doc__ = """Request message for
  [CampaignCriterionSimulationService.GetCampaignCriterionSimulation][google.ads.googleads.v3.services.CampaignCriterionSimulationService.GetCampaignCriterionSimulation].
  
  
  Attributes:
      resource_name:
          Required. The resource name of the campaign criterion
          simulation to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.GetCampaignCriterionSimulationRequest)
  ))
_sym_db.RegisterMessage(GetCampaignCriterionSimulationRequest)


DESCRIPTOR._options = None
_GETCAMPAIGNCRITERIONSIMULATIONREQUEST.fields_by_name['resource_name']._options = None

_CAMPAIGNCRITERIONSIMULATIONSERVICE = _descriptor.ServiceDescriptor(
  name='CampaignCriterionSimulationService',
  full_name='google.ads.googleads.v3.services.CampaignCriterionSimulationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312A\030googleads.googleapis.com'),
  serialized_start=439,
  serialized_end=764,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCampaignCriterionSimulation',
    full_name='google.ads.googleads.v3.services.CampaignCriterionSimulationService.GetCampaignCriterionSimulation',
    index=0,
    containing_service=None,
    input_type=_GETCAMPAIGNCRITERIONSIMULATIONREQUEST,
    output_type=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_campaign__criterion__simulation__pb2._CAMPAIGNCRITERIONSIMULATION,
    serialized_options=_b('\202\323\344\223\002@\022>/v3/{resource_name=customers/*/campaignCriterionSimulations/*}\332A\rresource_name'),
  ),
])
_sym_db.RegisterServiceDescriptor(_CAMPAIGNCRITERIONSIMULATIONSERVICE)

DESCRIPTOR.services_by_name['CampaignCriterionSimulationService'] = _CAMPAIGNCRITERIONSIMULATIONSERVICE

# @@protoc_insertion_point(module_scope)
