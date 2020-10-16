# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/errors/extension_setting_error.proto

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
  name='google/ads/googleads_v3/proto/errors/extension_setting_error.proto',
  package='google.ads.googleads.v3.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v3.errorsB\032ExtensionSettingErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v3/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V3.Errors\312\002\036Google\\Ads\\GoogleAds\\V3\\Errors\352\002\"Google::Ads::GoogleAds::V3::Errors'),
  serialized_pb=_b('\nBgoogle/ads/googleads_v3/proto/errors/extension_setting_error.proto\x12\x1egoogle.ads.googleads.v3.errors\x1a\x1cgoogle/api/annotations.proto\"\x98\x14\n\x19\x45xtensionSettingErrorEnum\"\xfa\x13\n\x15\x45xtensionSettingError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x17\n\x13\x45XTENSIONS_REQUIRED\x10\x02\x12%\n!FEED_TYPE_EXTENSION_TYPE_MISMATCH\x10\x03\x12\x15\n\x11INVALID_FEED_TYPE\x10\x04\x12\x34\n0INVALID_FEED_TYPE_FOR_CUSTOMER_EXTENSION_SETTING\x10\x05\x12%\n!CANNOT_CHANGE_FEED_ITEM_ON_CREATE\x10\x06\x12)\n%CANNOT_UPDATE_NEWLY_CREATED_EXTENSION\x10\x07\x12\x33\n/NO_EXISTING_AD_GROUP_EXTENSION_SETTING_FOR_TYPE\x10\x08\x12\x33\n/NO_EXISTING_CAMPAIGN_EXTENSION_SETTING_FOR_TYPE\x10\t\x12\x33\n/NO_EXISTING_CUSTOMER_EXTENSION_SETTING_FOR_TYPE\x10\n\x12-\n)AD_GROUP_EXTENSION_SETTING_ALREADY_EXISTS\x10\x0b\x12-\n)CAMPAIGN_EXTENSION_SETTING_ALREADY_EXISTS\x10\x0c\x12-\n)CUSTOMER_EXTENSION_SETTING_ALREADY_EXISTS\x10\r\x12\x35\n1AD_GROUP_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE\x10\x0e\x12\x35\n1CAMPAIGN_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE\x10\x0f\x12\x35\n1CUSTOMER_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE\x10\x10\x12\x16\n\x12VALUE_OUT_OF_RANGE\x10\x11\x12$\n CANNOT_SET_FIELD_WITH_FINAL_URLS\x10\x12\x12\x16\n\x12\x46INAL_URLS_NOT_SET\x10\x13\x12\x18\n\x14INVALID_PHONE_NUMBER\x10\x14\x12*\n&PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY\x10\x15\x12-\n)CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED\x10\x16\x12#\n\x1fPREMIUM_RATE_NUMBER_NOT_ALLOWED\x10\x17\x12\x1a\n\x16\x44ISALLOWED_NUMBER_TYPE\x10\x18\x12(\n$INVALID_DOMESTIC_PHONE_NUMBER_FORMAT\x10\x19\x12#\n\x1fVANITY_PHONE_NUMBER_NOT_ALLOWED\x10\x1a\x12\x18\n\x14INVALID_COUNTRY_CODE\x10\x1b\x12#\n\x1fINVALID_CALL_CONVERSION_TYPE_ID\x10\x1c\x12-\n)CUSTOMER_NOT_WHITELISTED_FOR_CALLTRACKING\x10\x1d\x12*\n&CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY\x10\x1e\x12\x12\n\x0eINVALID_APP_ID\x10\x1f\x12&\n\"QUOTES_IN_REVIEW_EXTENSION_SNIPPET\x10 \x12\'\n#HYPHENS_IN_REVIEW_EXTENSION_SNIPPET\x10!\x12(\n$REVIEW_EXTENSION_SOURCE_NOT_ELIGIBLE\x10\"\x12(\n$SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT\x10#\x12\x11\n\rMISSING_FIELD\x10$\x12\x1f\n\x1bINCONSISTENT_CURRENCY_CODES\x10%\x12*\n&PRICE_EXTENSION_HAS_DUPLICATED_HEADERS\x10&\x12\x34\n0PRICE_ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION\x10\'\x12%\n!PRICE_EXTENSION_HAS_TOO_FEW_ITEMS\x10(\x12&\n\"PRICE_EXTENSION_HAS_TOO_MANY_ITEMS\x10)\x12\x15\n\x11UNSUPPORTED_VALUE\x10*\x12\x1d\n\x19INVALID_DEVICE_PREFERENCE\x10+\x12\x18\n\x14INVALID_SCHEDULE_END\x10-\x12*\n&DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE\x10/\x12%\n!OVERLAPPING_SCHEDULES_NOT_ALLOWED\x10\x30\x12 \n\x1cSCHEDULE_END_NOT_AFTER_START\x10\x31\x12\x1e\n\x1aTOO_MANY_SCHEDULES_PER_DAY\x10\x32\x12&\n\"DUPLICATE_EXTENSION_FEED_ITEM_EDIT\x10\x33\x12\x1b\n\x17INVALID_SNIPPETS_HEADER\x10\x34\x12<\n8PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY\x10\x35\x12\x1f\n\x1b\x43\x41MPAIGN_TARGETING_MISMATCH\x10\x36\x12\"\n\x1e\x43\x41NNOT_OPERATE_ON_REMOVED_FEED\x10\x37\x12\x1b\n\x17\x45XTENSION_TYPE_REQUIRED\x10\x38\x12-\n)INCOMPATIBLE_UNDERLYING_MATCHING_FUNCTION\x10\x39\x12\x1d\n\x19START_DATE_AFTER_END_DATE\x10:\x12\x18\n\x14INVALID_PRICE_FORMAT\x10;\x12\x1a\n\x16PROMOTION_INVALID_TIME\x10<\x12<\n8PROMOTION_CANNOT_SET_PERCENT_DISCOUNT_AND_MONEY_DISCOUNT\x10=\x12>\n:PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT\x10>\x12%\n!TOO_MANY_DECIMAL_PLACES_SPECIFIED\x10?\x12\x19\n\x15INVALID_LANGUAGE_CODE\x10@\x12\x18\n\x14UNSUPPORTED_LANGUAGE\x10\x41\x12\x30\n,CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED\x10\x42\x12&\n\"EXTENSION_SETTING_UPDATE_IS_A_NOOP\x10\x43\x42\xf5\x01\n\"com.google.ads.googleads.v3.errorsB\x1a\x45xtensionSettingErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v3/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V3.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V3\\Errors\xea\x02\"Google::Ads::GoogleAds::V3::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_EXTENSIONSETTINGERRORENUM_EXTENSIONSETTINGERROR = _descriptor.EnumDescriptor(
  name='ExtensionSettingError',
  full_name='google.ads.googleads.v3.errors.ExtensionSettingErrorEnum.ExtensionSettingError',
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
      name='EXTENSIONS_REQUIRED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEED_TYPE_EXTENSION_TYPE_MISMATCH', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FEED_TYPE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FEED_TYPE_FOR_CUSTOMER_EXTENSION_SETTING', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_CHANGE_FEED_ITEM_ON_CREATE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_UPDATE_NEWLY_CREATED_EXTENSION', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_EXISTING_AD_GROUP_EXTENSION_SETTING_FOR_TYPE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_EXISTING_CAMPAIGN_EXTENSION_SETTING_FOR_TYPE', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_EXISTING_CUSTOMER_EXTENSION_SETTING_FOR_TYPE', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AD_GROUP_EXTENSION_SETTING_ALREADY_EXISTS', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_EXTENSION_SETTING_ALREADY_EXISTS', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_EXTENSION_SETTING_ALREADY_EXISTS', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AD_GROUP_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE_OUT_OF_RANGE', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_FIELD_WITH_FINAL_URLS', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINAL_URLS_NOT_SET', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PHONE_NUMBER', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREMIUM_RATE_NUMBER_NOT_ALLOWED', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISALLOWED_NUMBER_TYPE', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_DOMESTIC_PHONE_NUMBER_FORMAT', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VANITY_PHONE_NUMBER_NOT_ALLOWED', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_COUNTRY_CODE', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CALL_CONVERSION_TYPE_ID', index=28, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_NOT_WHITELISTED_FOR_CALLTRACKING', index=29, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY', index=30, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_APP_ID', index=31, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUOTES_IN_REVIEW_EXTENSION_SNIPPET', index=32, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HYPHENS_IN_REVIEW_EXTENSION_SNIPPET', index=33, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVIEW_EXTENSION_SOURCE_NOT_ELIGIBLE', index=34, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT', index=35, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_FIELD', index=36, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCONSISTENT_CURRENCY_CODES', index=37, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE_EXTENSION_HAS_DUPLICATED_HEADERS', index=38, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE_ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION', index=39, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE_EXTENSION_HAS_TOO_FEW_ITEMS', index=40, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE_EXTENSION_HAS_TOO_MANY_ITEMS', index=41, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_VALUE', index=42, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_DEVICE_PREFERENCE', index=43, number=43,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SCHEDULE_END', index=44, number=45,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE', index=45, number=47,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERLAPPING_SCHEDULES_NOT_ALLOWED', index=46, number=48,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCHEDULE_END_NOT_AFTER_START', index=47, number=49,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_SCHEDULES_PER_DAY', index=48, number=50,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_EXTENSION_FEED_ITEM_EDIT', index=49, number=51,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SNIPPETS_HEADER', index=50, number=52,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY', index=51, number=53,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_TARGETING_MISMATCH', index=52, number=54,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_OPERATE_ON_REMOVED_FEED', index=53, number=55,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTENSION_TYPE_REQUIRED', index=54, number=56,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCOMPATIBLE_UNDERLYING_MATCHING_FUNCTION', index=55, number=57,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_DATE_AFTER_END_DATE', index=56, number=58,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PRICE_FORMAT', index=57, number=59,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMOTION_INVALID_TIME', index=58, number=60,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMOTION_CANNOT_SET_PERCENT_DISCOUNT_AND_MONEY_DISCOUNT', index=59, number=61,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT', index=60, number=62,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_DECIMAL_PLACES_SPECIFIED', index=61, number=63,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_LANGUAGE_CODE', index=62, number=64,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_LANGUAGE', index=63, number=65,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED', index=64, number=66,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTENSION_SETTING_UPDATE_IS_A_NOOP', index=65, number=67,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=163,
  serialized_end=2717,
)
_sym_db.RegisterEnumDescriptor(_EXTENSIONSETTINGERRORENUM_EXTENSIONSETTINGERROR)


_EXTENSIONSETTINGERRORENUM = _descriptor.Descriptor(
  name='ExtensionSettingErrorEnum',
  full_name='google.ads.googleads.v3.errors.ExtensionSettingErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXTENSIONSETTINGERRORENUM_EXTENSIONSETTINGERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=2717,
)

_EXTENSIONSETTINGERRORENUM_EXTENSIONSETTINGERROR.containing_type = _EXTENSIONSETTINGERRORENUM
DESCRIPTOR.message_types_by_name['ExtensionSettingErrorEnum'] = _EXTENSIONSETTINGERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExtensionSettingErrorEnum = _reflection.GeneratedProtocolMessageType('ExtensionSettingErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _EXTENSIONSETTINGERRORENUM,
  __module__ = 'google.ads.googleads_v3.proto.errors.extension_setting_error_pb2'
  ,
  __doc__ = """Container for enum describing validation errors of extension settings.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.errors.ExtensionSettingErrorEnum)
  ))
_sym_db.RegisterMessage(ExtensionSettingErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
