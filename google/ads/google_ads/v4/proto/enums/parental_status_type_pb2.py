# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/enums/parental_status_type.proto

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
  name='google/ads/googleads_v4/proto/enums/parental_status_type.proto',
  package='google.ads.googleads.v4.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v4.enumsB\027ParentalStatusTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v4/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V4.Enums\312\002\035Google\\Ads\\GoogleAds\\V4\\Enums\352\002!Google::Ads::GoogleAds::V4::Enums'),
  serialized_pb=_b('\n>google/ads/googleads_v4/proto/enums/parental_status_type.proto\x12\x1dgoogle.ads.googleads.v4.enums\x1a\x1cgoogle/api/annotations.proto\"\x7f\n\x16ParentalStatusTypeEnum\"e\n\x12ParentalStatusType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x06PARENT\x10\xac\x02\x12\x11\n\x0cNOT_A_PARENT\x10\xad\x02\x12\x11\n\x0cUNDETERMINED\x10\xae\x02\x42\xec\x01\n!com.google.ads.googleads.v4.enumsB\x17ParentalStatusTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v4/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V4.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V4\\Enums\xea\x02!Google::Ads::GoogleAds::V4::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_PARENTALSTATUSTYPEENUM_PARENTALSTATUSTYPE = _descriptor.EnumDescriptor(
  name='ParentalStatusType',
  full_name='google.ads.googleads.v4.enums.ParentalStatusTypeEnum.ParentalStatusType',
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
      name='PARENT', index=2, number=300,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_A_PARENT', index=3, number=301,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNDETERMINED', index=4, number=302,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=153,
  serialized_end=254,
)
_sym_db.RegisterEnumDescriptor(_PARENTALSTATUSTYPEENUM_PARENTALSTATUSTYPE)


_PARENTALSTATUSTYPEENUM = _descriptor.Descriptor(
  name='ParentalStatusTypeEnum',
  full_name='google.ads.googleads.v4.enums.ParentalStatusTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PARENTALSTATUSTYPEENUM_PARENTALSTATUSTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=254,
)

_PARENTALSTATUSTYPEENUM_PARENTALSTATUSTYPE.containing_type = _PARENTALSTATUSTYPEENUM
DESCRIPTOR.message_types_by_name['ParentalStatusTypeEnum'] = _PARENTALSTATUSTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParentalStatusTypeEnum = _reflection.GeneratedProtocolMessageType('ParentalStatusTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _PARENTALSTATUSTYPEENUM,
  __module__ = 'google.ads.googleads_v4.proto.enums.parental_status_type_pb2'
  ,
  __doc__ = """Container for enum describing the type of demographic parental statuses.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.enums.ParentalStatusTypeEnum)
  ))
_sym_db.RegisterMessage(ParentalStatusTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
