# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/enums/message_placeholder_field.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/enums/message_placeholder_field.proto',
  package='google.ads.googleads.v5.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v5.enumsB\034MessagePlaceholderFieldProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v5/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V5.Enums\312\002\035Google\\Ads\\GoogleAds\\V5\\Enums\352\002!Google::Ads::GoogleAds::V5::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nCgoogle/ads/googleads_v5/proto/enums/message_placeholder_field.proto\x12\x1dgoogle.ads.googleads.v5.enums\x1a\x1cgoogle/api/annotations.proto\"\xbc\x01\n\x1bMessagePlaceholderFieldEnum\"\x9c\x01\n\x17MessagePlaceholderField\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x11\n\rBUSINESS_NAME\x10\x02\x12\x10\n\x0c\x43OUNTRY_CODE\x10\x03\x12\x10\n\x0cPHONE_NUMBER\x10\x04\x12\x1a\n\x16MESSAGE_EXTENSION_TEXT\x10\x05\x12\x10\n\x0cMESSAGE_TEXT\x10\x06\x42\xf1\x01\n!com.google.ads.googleads.v5.enumsB\x1cMessagePlaceholderFieldProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v5/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V5.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V5\\Enums\xea\x02!Google::Ads::GoogleAds::V5::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_MESSAGEPLACEHOLDERFIELDENUM_MESSAGEPLACEHOLDERFIELD = _descriptor.EnumDescriptor(
  name='MessagePlaceholderField',
  full_name='google.ads.googleads.v5.enums.MessagePlaceholderFieldEnum.MessagePlaceholderField',
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
      name='BUSINESS_NAME', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COUNTRY_CODE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PHONE_NUMBER', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE_EXTENSION_TEXT', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE_TEXT', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=165,
  serialized_end=321,
)
_sym_db.RegisterEnumDescriptor(_MESSAGEPLACEHOLDERFIELDENUM_MESSAGEPLACEHOLDERFIELD)


_MESSAGEPLACEHOLDERFIELDENUM = _descriptor.Descriptor(
  name='MessagePlaceholderFieldEnum',
  full_name='google.ads.googleads.v5.enums.MessagePlaceholderFieldEnum',
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
    _MESSAGEPLACEHOLDERFIELDENUM_MESSAGEPLACEHOLDERFIELD,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=321,
)

_MESSAGEPLACEHOLDERFIELDENUM_MESSAGEPLACEHOLDERFIELD.containing_type = _MESSAGEPLACEHOLDERFIELDENUM
DESCRIPTOR.message_types_by_name['MessagePlaceholderFieldEnum'] = _MESSAGEPLACEHOLDERFIELDENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessagePlaceholderFieldEnum = _reflection.GeneratedProtocolMessageType('MessagePlaceholderFieldEnum', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEPLACEHOLDERFIELDENUM,
  '__module__' : 'google.ads.googleads_v5.proto.enums.message_placeholder_field_pb2'
  ,
  '__doc__': """Values for Message placeholder fields.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.enums.MessagePlaceholderFieldEnum)
  })
_sym_db.RegisterMessage(MessagePlaceholderFieldEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
