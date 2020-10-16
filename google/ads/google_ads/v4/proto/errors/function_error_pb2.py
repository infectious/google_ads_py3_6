# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/errors/function_error.proto

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
  name='google/ads/googleads_v4/proto/errors/function_error.proto',
  package='google.ads.googleads.v4.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v4.errorsB\022FunctionErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v4/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V4.Errors\312\002\036Google\\Ads\\GoogleAds\\V4\\Errors\352\002\"Google::Ads::GoogleAds::V4::Errors'),
  serialized_pb=_b('\n9google/ads/googleads_v4/proto/errors/function_error.proto\x12\x1egoogle.ads.googleads.v4.errors\x1a\x1cgoogle/api/annotations.proto\"\xc1\x04\n\x11\x46unctionErrorEnum\"\xab\x04\n\rFunctionError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1b\n\x17INVALID_FUNCTION_FORMAT\x10\x02\x12\x16\n\x12\x44\x41TA_TYPE_MISMATCH\x10\x03\x12 \n\x1cINVALID_CONJUNCTION_OPERANDS\x10\x04\x12\x1e\n\x1aINVALID_NUMBER_OF_OPERANDS\x10\x05\x12\x18\n\x14INVALID_OPERAND_TYPE\x10\x06\x12\x14\n\x10INVALID_OPERATOR\x10\x07\x12 \n\x1cINVALID_REQUEST_CONTEXT_TYPE\x10\x08\x12)\n%INVALID_FUNCTION_FOR_CALL_PLACEHOLDER\x10\t\x12$\n INVALID_FUNCTION_FOR_PLACEHOLDER\x10\n\x12\x13\n\x0fINVALID_OPERAND\x10\x0b\x12\"\n\x1eMISSING_CONSTANT_OPERAND_VALUE\x10\x0c\x12\"\n\x1eINVALID_CONSTANT_OPERAND_VALUE\x10\r\x12\x13\n\x0fINVALID_NESTING\x10\x0e\x12#\n\x1fMULTIPLE_FEED_IDS_NOT_SUPPORTED\x10\x0f\x12/\n+INVALID_FUNCTION_FOR_FEED_WITH_FIXED_SCHEMA\x10\x10\x12\x1a\n\x16INVALID_ATTRIBUTE_NAME\x10\x11\x42\xed\x01\n\"com.google.ads.googleads.v4.errorsB\x12\x46unctionErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v4/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V4.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V4\\Errors\xea\x02\"Google::Ads::GoogleAds::V4::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FUNCTIONERRORENUM_FUNCTIONERROR = _descriptor.EnumDescriptor(
  name='FunctionError',
  full_name='google.ads.googleads.v4.errors.FunctionErrorEnum.FunctionError',
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
      name='INVALID_FUNCTION_FORMAT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_TYPE_MISMATCH', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CONJUNCTION_OPERANDS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_NUMBER_OF_OPERANDS', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_OPERAND_TYPE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_OPERATOR', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_REQUEST_CONTEXT_TYPE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FUNCTION_FOR_CALL_PLACEHOLDER', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FUNCTION_FOR_PLACEHOLDER', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_OPERAND', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_CONSTANT_OPERAND_VALUE', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CONSTANT_OPERAND_VALUE', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_NESTING', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTIPLE_FEED_IDS_NOT_SUPPORTED', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FUNCTION_FOR_FEED_WITH_FIXED_SCHEMA', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ATTRIBUTE_NAME', index=17, number=17,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=146,
  serialized_end=701,
)
_sym_db.RegisterEnumDescriptor(_FUNCTIONERRORENUM_FUNCTIONERROR)


_FUNCTIONERRORENUM = _descriptor.Descriptor(
  name='FunctionErrorEnum',
  full_name='google.ads.googleads.v4.errors.FunctionErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FUNCTIONERRORENUM_FUNCTIONERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=701,
)

_FUNCTIONERRORENUM_FUNCTIONERROR.containing_type = _FUNCTIONERRORENUM
DESCRIPTOR.message_types_by_name['FunctionErrorEnum'] = _FUNCTIONERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FunctionErrorEnum = _reflection.GeneratedProtocolMessageType('FunctionErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONERRORENUM,
  __module__ = 'google.ads.googleads_v4.proto.errors.function_error_pb2'
  ,
  __doc__ = """Container for enum describing possible function errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.errors.FunctionErrorEnum)
  ))
_sym_db.RegisterMessage(FunctionErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
