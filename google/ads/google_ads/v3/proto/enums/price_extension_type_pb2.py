# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/enums/price_extension_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/enums/price_extension_type.proto',
  package='google.ads.googleads.v3.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v3.enumsB\027PriceExtensionTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V3.Enums\312\002\035Google\\Ads\\GoogleAds\\V3\\Enums\352\002!Google::Ads::GoogleAds::V3::Enums'),
  serialized_pb=_b('\n>google/ads/googleads_v3/proto/enums/price_extension_type.proto\x12\x1dgoogle.ads.googleads.v3.enums\x1a\x1cgoogle/api/annotations.proto\"\xeb\x01\n\x16PriceExtensionTypeEnum\"\xd0\x01\n\x12PriceExtensionType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\n\n\x06\x42RANDS\x10\x02\x12\n\n\x06\x45VENTS\x10\x03\x12\r\n\tLOCATIONS\x10\x04\x12\x11\n\rNEIGHBORHOODS\x10\x05\x12\x16\n\x12PRODUCT_CATEGORIES\x10\x06\x12\x11\n\rPRODUCT_TIERS\x10\x07\x12\x0c\n\x08SERVICES\x10\x08\x12\x16\n\x12SERVICE_CATEGORIES\x10\t\x12\x11\n\rSERVICE_TIERS\x10\nB\xec\x01\n!com.google.ads.googleads.v3.enumsB\x17PriceExtensionTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V3.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V3\\Enums\xea\x02!Google::Ads::GoogleAds::V3::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_PRICEEXTENSIONTYPEENUM_PRICEEXTENSIONTYPE = _descriptor.EnumDescriptor(
  name='PriceExtensionType',
  full_name='google.ads.googleads.v3.enums.PriceExtensionTypeEnum.PriceExtensionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BRANDS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EVENTS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATIONS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEIGHBORHOODS', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_CATEGORIES', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_TIERS', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVICES', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVICE_CATEGORIES', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVICE_TIERS', index=10, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=155,
  serialized_end=363,
)
_sym_db.RegisterEnumDescriptor(_PRICEEXTENSIONTYPEENUM_PRICEEXTENSIONTYPE)


_PRICEEXTENSIONTYPEENUM = _descriptor.Descriptor(
  name='PriceExtensionTypeEnum',
  full_name='google.ads.googleads.v3.enums.PriceExtensionTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PRICEEXTENSIONTYPEENUM_PRICEEXTENSIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=363,
)

_PRICEEXTENSIONTYPEENUM_PRICEEXTENSIONTYPE.containing_type = _PRICEEXTENSIONTYPEENUM
DESCRIPTOR.message_types_by_name['PriceExtensionTypeEnum'] = _PRICEEXTENSIONTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PriceExtensionTypeEnum = _reflection.GeneratedProtocolMessageType('PriceExtensionTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _PRICEEXTENSIONTYPEENUM,
  __module__ = 'google.ads.googleads_v3.proto.enums.price_extension_type_pb2'
  ,
  __doc__ = """Container for enum describing types for a price extension.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.enums.PriceExtensionTypeEnum)
  ))
_sym_db.RegisterMessage(PriceExtensionTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
