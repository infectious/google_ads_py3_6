# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/errors/conversion_adjustment_upload_error.proto

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
  name='google/ads/googleads_v2/proto/errors/conversion_adjustment_upload_error.proto',
  package='google.ads.googleads.v2.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v2.errorsB$ConversionAdjustmentUploadErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V2.Errors\312\002\036Google\\Ads\\GoogleAds\\V2\\Errors\352\002\"Google::Ads::GoogleAds::V2::Errors'),
  serialized_pb=_b('\nMgoogle/ads/googleads_v2/proto/errors/conversion_adjustment_upload_error.proto\x12\x1egoogle.ads.googleads.v2.errors\x1a\x1cgoogle/api/annotations.proto\"\xae\x03\n#ConversionAdjustmentUploadErrorEnum\"\x86\x03\n\x1f\x43onversionAdjustmentUploadError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12 \n\x1cTOO_RECENT_CONVERSION_ACTION\x10\x02\x12\x1d\n\x19INVALID_CONVERSION_ACTION\x10\x03\x12 \n\x1c\x43ONVERSION_ALREADY_RETRACTED\x10\x04\x12\x18\n\x14\x43ONVERSION_NOT_FOUND\x10\x05\x12\x16\n\x12\x43ONVERSION_EXPIRED\x10\x06\x12\"\n\x1e\x41\x44JUSTMENT_PRECEDES_CONVERSION\x10\x07\x12!\n\x1dMORE_RECENT_RESTATEMENT_FOUND\x10\x08\x12\x19\n\x15TOO_RECENT_CONVERSION\x10\t\x12N\nJCANNOT_RESTATE_CONVERSION_ACTION_THAT_ALWAYS_USES_DEFAULT_CONVERSION_VALUE\x10\nB\xff\x01\n\"com.google.ads.googleads.v2.errorsB$ConversionAdjustmentUploadErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V2.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V2\\Errors\xea\x02\"Google::Ads::GoogleAds::V2::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CONVERSIONADJUSTMENTUPLOADERRORENUM_CONVERSIONADJUSTMENTUPLOADERROR = _descriptor.EnumDescriptor(
  name='ConversionAdjustmentUploadError',
  full_name='google.ads.googleads.v2.errors.ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError',
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
      name='TOO_RECENT_CONVERSION_ACTION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CONVERSION_ACTION', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONVERSION_ALREADY_RETRACTED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONVERSION_NOT_FOUND', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONVERSION_EXPIRED', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADJUSTMENT_PRECEDES_CONVERSION', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MORE_RECENT_RESTATEMENT_FOUND', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_RECENT_CONVERSION', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_RESTATE_CONVERSION_ACTION_THAT_ALWAYS_USES_DEFAULT_CONVERSION_VALUE', index=10, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=184,
  serialized_end=574,
)
_sym_db.RegisterEnumDescriptor(_CONVERSIONADJUSTMENTUPLOADERRORENUM_CONVERSIONADJUSTMENTUPLOADERROR)


_CONVERSIONADJUSTMENTUPLOADERRORENUM = _descriptor.Descriptor(
  name='ConversionAdjustmentUploadErrorEnum',
  full_name='google.ads.googleads.v2.errors.ConversionAdjustmentUploadErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONVERSIONADJUSTMENTUPLOADERRORENUM_CONVERSIONADJUSTMENTUPLOADERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=574,
)

_CONVERSIONADJUSTMENTUPLOADERRORENUM_CONVERSIONADJUSTMENTUPLOADERROR.containing_type = _CONVERSIONADJUSTMENTUPLOADERRORENUM
DESCRIPTOR.message_types_by_name['ConversionAdjustmentUploadErrorEnum'] = _CONVERSIONADJUSTMENTUPLOADERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConversionAdjustmentUploadErrorEnum = _reflection.GeneratedProtocolMessageType('ConversionAdjustmentUploadErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _CONVERSIONADJUSTMENTUPLOADERRORENUM,
  __module__ = 'google.ads.googleads_v2.proto.errors.conversion_adjustment_upload_error_pb2'
  ,
  __doc__ = """Container for enum describing possible conversion adjustment upload
  errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.errors.ConversionAdjustmentUploadErrorEnum)
  ))
_sym_db.RegisterMessage(ConversionAdjustmentUploadErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
