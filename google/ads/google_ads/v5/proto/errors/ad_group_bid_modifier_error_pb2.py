# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/errors/ad_group_bid_modifier_error.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/errors/ad_group_bid_modifier_error.proto',
  package='google.ads.googleads.v5.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v5.errorsB\034AdGroupBidModifierErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v5/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V5.Errors\312\002\036Google\\Ads\\GoogleAds\\V5\\Errors\352\002\"Google::Ads::GoogleAds::V5::Errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nFgoogle/ads/googleads_v5/proto/errors/ad_group_bid_modifier_error.proto\x12\x1egoogle.ads.googleads.v5.errors\x1a\x1cgoogle/api/annotations.proto\"\xb6\x01\n\x1b\x41\x64GroupBidModifierErrorEnum\"\x96\x01\n\x17\x41\x64GroupBidModifierError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1e\n\x1a\x43RITERION_ID_NOT_SUPPORTED\x10\x02\x12=\n9CANNOT_OVERRIDE_OPTED_OUT_CAMPAIGN_CRITERION_BID_MODIFIER\x10\x03\x42\xf7\x01\n\"com.google.ads.googleads.v5.errorsB\x1c\x41\x64GroupBidModifierErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v5/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V5.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V5\\Errors\xea\x02\"Google::Ads::GoogleAds::V5::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_ADGROUPBIDMODIFIERERRORENUM_ADGROUPBIDMODIFIERERROR = _descriptor.EnumDescriptor(
  name='AdGroupBidModifierError',
  full_name='google.ads.googleads.v5.errors.AdGroupBidModifierErrorEnum.AdGroupBidModifierError',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CRITERION_ID_NOT_SUPPORTED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_OVERRIDE_OPTED_OUT_CAMPAIGN_CRITERION_BID_MODIFIER', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=169,
  serialized_end=319,
)
_sym_db.RegisterEnumDescriptor(_ADGROUPBIDMODIFIERERRORENUM_ADGROUPBIDMODIFIERERROR)


_ADGROUPBIDMODIFIERERRORENUM = _descriptor.Descriptor(
  name='AdGroupBidModifierErrorEnum',
  full_name='google.ads.googleads.v5.errors.AdGroupBidModifierErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADGROUPBIDMODIFIERERRORENUM_ADGROUPBIDMODIFIERERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=319,
)

_ADGROUPBIDMODIFIERERRORENUM_ADGROUPBIDMODIFIERERROR.containing_type = _ADGROUPBIDMODIFIERERRORENUM
DESCRIPTOR.message_types_by_name['AdGroupBidModifierErrorEnum'] = _ADGROUPBIDMODIFIERERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupBidModifierErrorEnum = _reflection.GeneratedProtocolMessageType('AdGroupBidModifierErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _ADGROUPBIDMODIFIERERRORENUM,
  '__module__' : 'google.ads.googleads_v5.proto.errors.ad_group_bid_modifier_error_pb2'
  ,
  '__doc__': """Container for enum describing possible ad group bid modifier errors.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.errors.AdGroupBidModifierErrorEnum)
  })
_sym_db.RegisterMessage(AdGroupBidModifierErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
