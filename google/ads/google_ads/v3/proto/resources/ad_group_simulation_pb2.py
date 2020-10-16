# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/resources/ad_group_simulation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.common import simulation_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_common_dot_simulation__pb2
from google.ads.google_ads.v3.proto.enums import simulation_modification_method_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_simulation__modification__method__pb2
from google.ads.google_ads.v3.proto.enums import simulation_type_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_simulation__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/resources/ad_group_simulation.proto',
  package='google.ads.googleads.v3.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v3.resourcesB\026AdGroupSimulationProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V3.Resources\312\002!Google\\Ads\\GoogleAds\\V3\\Resources\352\002%Google::Ads::GoogleAds::V3::Resources'),
  serialized_pb=_b('\nAgoogle/ads/googleads_v3/proto/resources/ad_group_simulation.proto\x12!google.ads.googleads.v3.resources\x1a\x35google/ads/googleads_v3/proto/common/simulation.proto\x1aHgoogle/ads/googleads_v3/proto/enums/simulation_modification_method.proto\x1a\x39google/ads/googleads_v3/proto/enums/simulation_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xf4\x06\n\x11\x41\x64GroupSimulation\x12I\n\rresource_name\x18\x01 \x01(\tB2\xe0\x41\x03\xfa\x41,\n*googleads.googleapis.com/AdGroupSimulation\x12\x35\n\x0b\x61\x64_group_id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x03\xe0\x41\x03\x12S\n\x04type\x18\x03 \x01(\x0e\x32@.google.ads.googleads.v3.enums.SimulationTypeEnum.SimulationTypeB\x03\xe0\x41\x03\x12~\n\x13modification_method\x18\x04 \x01(\x0e\x32\\.google.ads.googleads.v3.enums.SimulationModificationMethodEnum.SimulationModificationMethodB\x03\xe0\x41\x03\x12\x35\n\nstart_date\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x03\xe0\x41\x03\x12\x33\n\x08\x65nd_date\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x03\xe0\x41\x03\x12\\\n\x12\x63pc_bid_point_list\x18\x08 \x01(\x0b\x32\x39.google.ads.googleads.v3.common.CpcBidSimulationPointListB\x03\xe0\x41\x03H\x00\x12\\\n\x12\x63pv_bid_point_list\x18\n \x01(\x0b\x32\x39.google.ads.googleads.v3.common.CpvBidSimulationPointListB\x03\xe0\x41\x03H\x00\x12\x62\n\x15target_cpa_point_list\x18\t \x01(\x0b\x32<.google.ads.googleads.v3.common.TargetCpaSimulationPointListB\x03\xe0\x41\x03H\x00:n\xea\x41k\n*googleads.googleapis.com/AdGroupSimulation\x12=customers/{customer}/adGroupSimulations/{ad_group_simulation}B\x0c\n\npoint_listB\x83\x02\n%com.google.ads.googleads.v3.resourcesB\x16\x41\x64GroupSimulationProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V3.Resources\xca\x02!Google\\Ads\\GoogleAds\\V3\\Resources\xea\x02%Google::Ads::GoogleAds::V3::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_common_dot_simulation__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_simulation__modification__method__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_simulation__type__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ADGROUPSIMULATION = _descriptor.Descriptor(
  name='AdGroupSimulation',
  full_name='google.ads.googleads.v3.resources.AdGroupSimulation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.resources.AdGroupSimulation.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003\372A,\n*googleads.googleapis.com/AdGroupSimulation'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_group_id', full_name='google.ads.googleads.v3.resources.AdGroupSimulation.ad_group_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.ads.googleads.v3.resources.AdGroupSimulation.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modification_method', full_name='google.ads.googleads.v3.resources.AdGroupSimulation.modification_method', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='google.ads.googleads.v3.resources.AdGroupSimulation.start_date', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='google.ads.googleads.v3.resources.AdGroupSimulation.end_date', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_point_list', full_name='google.ads.googleads.v3.resources.AdGroupSimulation.cpc_bid_point_list', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpv_bid_point_list', full_name='google.ads.googleads.v3.resources.AdGroupSimulation.cpv_bid_point_list', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_cpa_point_list', full_name='google.ads.googleads.v3.resources.AdGroupSimulation.target_cpa_point_list', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\352Ak\n*googleads.googleapis.com/AdGroupSimulation\022=customers/{customer}/adGroupSimulations/{ad_group_simulation}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='point_list', full_name='google.ads.googleads.v3.resources.AdGroupSimulation.point_list',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=415,
  serialized_end=1299,
)

_ADGROUPSIMULATION.fields_by_name['ad_group_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_ADGROUPSIMULATION.fields_by_name['type'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_simulation__type__pb2._SIMULATIONTYPEENUM_SIMULATIONTYPE
_ADGROUPSIMULATION.fields_by_name['modification_method'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_simulation__modification__method__pb2._SIMULATIONMODIFICATIONMETHODENUM_SIMULATIONMODIFICATIONMETHOD
_ADGROUPSIMULATION.fields_by_name['start_date'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ADGROUPSIMULATION.fields_by_name['end_date'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ADGROUPSIMULATION.fields_by_name['cpc_bid_point_list'].message_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_common_dot_simulation__pb2._CPCBIDSIMULATIONPOINTLIST
_ADGROUPSIMULATION.fields_by_name['cpv_bid_point_list'].message_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_common_dot_simulation__pb2._CPVBIDSIMULATIONPOINTLIST
_ADGROUPSIMULATION.fields_by_name['target_cpa_point_list'].message_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_common_dot_simulation__pb2._TARGETCPASIMULATIONPOINTLIST
_ADGROUPSIMULATION.oneofs_by_name['point_list'].fields.append(
  _ADGROUPSIMULATION.fields_by_name['cpc_bid_point_list'])
_ADGROUPSIMULATION.fields_by_name['cpc_bid_point_list'].containing_oneof = _ADGROUPSIMULATION.oneofs_by_name['point_list']
_ADGROUPSIMULATION.oneofs_by_name['point_list'].fields.append(
  _ADGROUPSIMULATION.fields_by_name['cpv_bid_point_list'])
_ADGROUPSIMULATION.fields_by_name['cpv_bid_point_list'].containing_oneof = _ADGROUPSIMULATION.oneofs_by_name['point_list']
_ADGROUPSIMULATION.oneofs_by_name['point_list'].fields.append(
  _ADGROUPSIMULATION.fields_by_name['target_cpa_point_list'])
_ADGROUPSIMULATION.fields_by_name['target_cpa_point_list'].containing_oneof = _ADGROUPSIMULATION.oneofs_by_name['point_list']
DESCRIPTOR.message_types_by_name['AdGroupSimulation'] = _ADGROUPSIMULATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupSimulation = _reflection.GeneratedProtocolMessageType('AdGroupSimulation', (_message.Message,), dict(
  DESCRIPTOR = _ADGROUPSIMULATION,
  __module__ = 'google.ads.googleads_v3.proto.resources.ad_group_simulation_pb2'
  ,
  __doc__ = """An ad group simulation. Supported combinations of advertising channel
  type, simulation type and simulation modification method is detailed
  below respectively.
  
  1. SEARCH - CPC\_BID - DEFAULT
  2. SEARCH - CPC\_BID - UNIFORM
  3. SEARCH - TARGET\_CPA - UNIFORM
  4. DISPLAY - CPC\_BID - DEFAULT
  5. DISPLAY - CPC\_BID - UNIFORM
  6. DISPLAY - TARGET\_CPA - UNIFORM
  7. VIDEO - CPV\_BID - DEFAULT
  8. VIDEO - CPV\_BID - UNIFORM
  
  
  Attributes:
      resource_name:
          Output only. The resource name of the ad group simulation. Ad
          group simulation resource names have the form:  ``customers/{c
          ustomer_id}/adGroupSimulations/{ad_group_id}~{type}~{modificat
          ion_method}~{start_date}~{end_date}``
      ad_group_id:
          Output only. Ad group id of the simulation.
      type:
          Output only. The field that the simulation modifies.
      modification_method:
          Output only. How the simulation modifies the field.
      start_date:
          Output only. First day on which the simulation is based, in
          YYYY-MM-DD format.
      end_date:
          Output only. Last day on which the simulation is based, in
          YYYY-MM-DD format
      point_list:
          List of simulation points.
      cpc_bid_point_list:
          Output only. Simulation points if the simulation type is
          CPC\_BID.
      cpv_bid_point_list:
          Output only. Simulation points if the simulation type is
          CPV\_BID.
      target_cpa_point_list:
          Output only. Simulation points if the simulation type is
          TARGET\_CPA.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.resources.AdGroupSimulation)
  ))
_sym_db.RegisterMessage(AdGroupSimulation)


DESCRIPTOR._options = None
_ADGROUPSIMULATION.fields_by_name['resource_name']._options = None
_ADGROUPSIMULATION.fields_by_name['ad_group_id']._options = None
_ADGROUPSIMULATION.fields_by_name['type']._options = None
_ADGROUPSIMULATION.fields_by_name['modification_method']._options = None
_ADGROUPSIMULATION.fields_by_name['start_date']._options = None
_ADGROUPSIMULATION.fields_by_name['end_date']._options = None
_ADGROUPSIMULATION.fields_by_name['cpc_bid_point_list']._options = None
_ADGROUPSIMULATION.fields_by_name['cpv_bid_point_list']._options = None
_ADGROUPSIMULATION.fields_by_name['target_cpa_point_list']._options = None
_ADGROUPSIMULATION._options = None
# @@protoc_insertion_point(module_scope)
