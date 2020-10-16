# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/errors/feed_item_error.proto

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
  name='google/ads/googleads_v4/proto/errors/feed_item_error.proto',
  package='google.ads.googleads.v4.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v4.errorsB\022FeedItemErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v4/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V4.Errors\312\002\036Google\\Ads\\GoogleAds\\V4\\Errors\352\002\"Google::Ads::GoogleAds::V4::Errors'),
  serialized_pb=_b('\n:google/ads/googleads_v4/proto/errors/feed_item_error.proto\x12\x1egoogle.ads.googleads.v4.errors\x1a\x1cgoogle/api/annotations.proto\"\x87\x03\n\x11\x46\x65\x65\x64ItemErrorEnum\"\xf1\x02\n\rFeedItemError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12.\n*CANNOT_CONVERT_ATTRIBUTE_VALUE_FROM_STRING\x10\x02\x12\'\n#CANNOT_OPERATE_ON_REMOVED_FEED_ITEM\x10\x03\x12*\n&DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE\x10\x04\x12\x1c\n\x18KEY_ATTRIBUTES_NOT_FOUND\x10\x05\x12\x0f\n\x0bINVALID_URL\x10\x06\x12\x1a\n\x16MISSING_KEY_ATTRIBUTES\x10\x07\x12\x1d\n\x19KEY_ATTRIBUTES_NOT_UNIQUE\x10\x08\x12%\n!CANNOT_MODIFY_KEY_ATTRIBUTE_VALUE\x10\t\x12,\n(SIZE_TOO_LARGE_FOR_MULTI_VALUE_ATTRIBUTE\x10\nB\xed\x01\n\"com.google.ads.googleads.v4.errorsB\x12\x46\x65\x65\x64ItemErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v4/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V4.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V4\\Errors\xea\x02\"Google::Ads::GoogleAds::V4::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FEEDITEMERRORENUM_FEEDITEMERROR = _descriptor.EnumDescriptor(
  name='FeedItemError',
  full_name='google.ads.googleads.v4.errors.FeedItemErrorEnum.FeedItemError',
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
      name='CANNOT_CONVERT_ATTRIBUTE_VALUE_FROM_STRING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_OPERATE_ON_REMOVED_FEED_ITEM', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEY_ATTRIBUTES_NOT_FOUND', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_URL', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_KEY_ATTRIBUTES', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEY_ATTRIBUTES_NOT_UNIQUE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_MODIFY_KEY_ATTRIBUTE_VALUE', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIZE_TOO_LARGE_FOR_MULTI_VALUE_ATTRIBUTE', index=10, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=147,
  serialized_end=516,
)
_sym_db.RegisterEnumDescriptor(_FEEDITEMERRORENUM_FEEDITEMERROR)


_FEEDITEMERRORENUM = _descriptor.Descriptor(
  name='FeedItemErrorEnum',
  full_name='google.ads.googleads.v4.errors.FeedItemErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEEDITEMERRORENUM_FEEDITEMERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=516,
)

_FEEDITEMERRORENUM_FEEDITEMERROR.containing_type = _FEEDITEMERRORENUM
DESCRIPTOR.message_types_by_name['FeedItemErrorEnum'] = _FEEDITEMERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedItemErrorEnum = _reflection.GeneratedProtocolMessageType('FeedItemErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _FEEDITEMERRORENUM,
  __module__ = 'google.ads.googleads_v4.proto.errors.feed_item_error_pb2'
  ,
  __doc__ = """Container for enum describing possible feed item errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.errors.FeedItemErrorEnum)
  ))
_sym_db.RegisterMessage(FeedItemErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
