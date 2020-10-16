# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/errors/feed_item_validation_error.proto

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
  name='google/ads/googleads_v4/proto/errors/feed_item_validation_error.proto',
  package='google.ads.googleads.v4.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v4.errorsB\034FeedItemValidationErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v4/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V4.Errors\312\002\036Google\\Ads\\GoogleAds\\V4\\Errors\352\002\"Google::Ads::GoogleAds::V4::Errors'),
  serialized_pb=_b('\nEgoogle/ads/googleads_v4/proto/errors/feed_item_validation_error.proto\x12\x1egoogle.ads.googleads.v4.errors\x1a\x1cgoogle/api/annotations.proto\"\xe7\x19\n\x1b\x46\x65\x65\x64ItemValidationErrorEnum\"\xc7\x19\n\x17\x46\x65\x65\x64ItemValidationError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x14\n\x10STRING_TOO_SHORT\x10\x02\x12\x13\n\x0fSTRING_TOO_LONG\x10\x03\x12\x17\n\x13VALUE_NOT_SPECIFIED\x10\x04\x12(\n$INVALID_DOMESTIC_PHONE_NUMBER_FORMAT\x10\x05\x12\x18\n\x14INVALID_PHONE_NUMBER\x10\x06\x12*\n&PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY\x10\x07\x12#\n\x1fPREMIUM_RATE_NUMBER_NOT_ALLOWED\x10\x08\x12\x1a\n\x16\x44ISALLOWED_NUMBER_TYPE\x10\t\x12\x16\n\x12VALUE_OUT_OF_RANGE\x10\n\x12*\n&CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY\x10\x0b\x12-\n)CUSTOMER_NOT_WHITELISTED_FOR_CALLTRACKING\x10\x0c\x12\x18\n\x14INVALID_COUNTRY_CODE\x10\r\x12\x12\n\x0eINVALID_APP_ID\x10\x0e\x12!\n\x1dMISSING_ATTRIBUTES_FOR_FIELDS\x10\x0f\x12\x13\n\x0fINVALID_TYPE_ID\x10\x10\x12\x19\n\x15INVALID_EMAIL_ADDRESS\x10\x11\x12\x15\n\x11INVALID_HTTPS_URL\x10\x12\x12\x1c\n\x18MISSING_DELIVERY_ADDRESS\x10\x13\x12\x1d\n\x19START_DATE_AFTER_END_DATE\x10\x14\x12 \n\x1cMISSING_FEED_ITEM_START_TIME\x10\x15\x12\x1e\n\x1aMISSING_FEED_ITEM_END_TIME\x10\x16\x12\x18\n\x14MISSING_FEED_ITEM_ID\x10\x17\x12#\n\x1fVANITY_PHONE_NUMBER_NOT_ALLOWED\x10\x18\x12$\n INVALID_REVIEW_EXTENSION_SNIPPET\x10\x19\x12\x19\n\x15INVALID_NUMBER_FORMAT\x10\x1a\x12\x17\n\x13INVALID_DATE_FORMAT\x10\x1b\x12\x18\n\x14INVALID_PRICE_FORMAT\x10\x1c\x12\x1d\n\x19UNKNOWN_PLACEHOLDER_FIELD\x10\x1d\x12.\n*MISSING_ENHANCED_SITELINK_DESCRIPTION_LINE\x10\x1e\x12&\n\"REVIEW_EXTENSION_SOURCE_INELIGIBLE\x10\x1f\x12\'\n#HYPHENS_IN_REVIEW_EXTENSION_SNIPPET\x10 \x12-\n)DOUBLE_QUOTES_IN_REVIEW_EXTENSION_SNIPPET\x10!\x12&\n\"QUOTES_IN_REVIEW_EXTENSION_SNIPPET\x10\"\x12\x1f\n\x1bINVALID_FORM_ENCODED_PARAMS\x10#\x12\x1e\n\x1aINVALID_URL_PARAMETER_NAME\x10$\x12\x17\n\x13NO_GEOCODING_RESULT\x10%\x12(\n$SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT\x10&\x12-\n)CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED\x10\'\x12 \n\x1cINVALID_PLACEHOLDER_FIELD_ID\x10(\x12\x13\n\x0fINVALID_URL_TAG\x10)\x12\x11\n\rLIST_TOO_LONG\x10*\x12\"\n\x1eINVALID_ATTRIBUTES_COMBINATION\x10+\x12\x14\n\x10\x44UPLICATE_VALUES\x10,\x12%\n!INVALID_CALL_CONVERSION_ACTION_ID\x10-\x12!\n\x1d\x43\x41NNOT_SET_WITHOUT_FINAL_URLS\x10.\x12$\n APP_ID_DOESNT_EXIST_IN_APP_STORE\x10/\x12\x15\n\x11INVALID_FINAL_URL\x10\x30\x12\x18\n\x14INVALID_TRACKING_URL\x10\x31\x12*\n&INVALID_FINAL_URL_FOR_APP_DOWNLOAD_URL\x10\x32\x12\x12\n\x0eLIST_TOO_SHORT\x10\x33\x12\x17\n\x13INVALID_USER_ACTION\x10\x34\x12\x15\n\x11INVALID_TYPE_NAME\x10\x35\x12\x1f\n\x1bINVALID_EVENT_CHANGE_STATUS\x10\x36\x12\x1b\n\x17INVALID_SNIPPETS_HEADER\x10\x37\x12\x1c\n\x18INVALID_ANDROID_APP_LINK\x10\x38\x12;\n7NUMBER_TYPE_WITH_CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY\x10\x39\x12\x1a\n\x16RESERVED_KEYWORD_OTHER\x10:\x12\x1b\n\x17\x44UPLICATE_OPTION_LABELS\x10;\x12\x1d\n\x19\x44UPLICATE_OPTION_PREFILLS\x10<\x12\x18\n\x14UNEQUAL_LIST_LENGTHS\x10=\x12\x1f\n\x1bINCONSISTENT_CURRENCY_CODES\x10>\x12*\n&PRICE_EXTENSION_HAS_DUPLICATED_HEADERS\x10?\x12.\n*ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION\x10@\x12%\n!PRICE_EXTENSION_HAS_TOO_FEW_ITEMS\x10\x41\x12\x15\n\x11UNSUPPORTED_VALUE\x10\x42\x12\x1c\n\x18INVALID_FINAL_MOBILE_URL\x10\x43\x12%\n!INVALID_KEYWORDLESS_AD_RULE_LABEL\x10\x44\x12\'\n#VALUE_TRACK_PARAMETER_NOT_SUPPORTED\x10\x45\x12*\n&UNSUPPORTED_VALUE_IN_SELECTED_LANGUAGE\x10\x46\x12\x18\n\x14INVALID_IOS_APP_LINK\x10G\x12,\n(MISSING_IOS_APP_LINK_OR_IOS_APP_STORE_ID\x10H\x12\x1a\n\x16PROMOTION_INVALID_TIME\x10I\x12\x39\n5PROMOTION_CANNOT_SET_PERCENT_OFF_AND_MONEY_AMOUNT_OFF\x10J\x12>\n:PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT\x10K\x12%\n!TOO_MANY_DECIMAL_PLACES_SPECIFIED\x10L\x12\x1e\n\x1a\x41\x44_CUSTOMIZERS_NOT_ALLOWED\x10M\x12\x19\n\x15INVALID_LANGUAGE_CODE\x10N\x12\x18\n\x14UNSUPPORTED_LANGUAGE\x10O\x12\x1b\n\x17IF_FUNCTION_NOT_ALLOWED\x10P\x12\x1c\n\x18INVALID_FINAL_URL_SUFFIX\x10Q\x12#\n\x1fINVALID_TAG_IN_FINAL_URL_SUFFIX\x10R\x12#\n\x1fINVALID_FINAL_URL_SUFFIX_FORMAT\x10S\x12\x30\n,CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED\x10T\x12\'\n#ONLY_ONE_DELIVERY_OPTION_IS_ALLOWED\x10U\x12\x1d\n\x19NO_DELIVERY_OPTION_IS_SET\x10V\x12&\n\"INVALID_CONVERSION_REPORTING_STATE\x10W\x12\x14\n\x10IMAGE_SIZE_WRONG\x10X\x12+\n\'EMAIL_DELIVERY_NOT_AVAILABLE_IN_COUNTRY\x10Y\x12\'\n#AUTO_REPLY_NOT_AVAILABLE_IN_COUNTRY\x10Z\x12\x1a\n\x16INVALID_LATITUDE_VALUE\x10[\x12\x1b\n\x17INVALID_LONGITUDE_VALUE\x10\\\x12\x13\n\x0fTOO_MANY_LABELS\x10]\x12\x15\n\x11INVALID_IMAGE_URL\x10^\x12\x1a\n\x16MISSING_LATITUDE_VALUE\x10_\x12\x1b\n\x17MISSING_LONGITUDE_VALUE\x10`\x12\x15\n\x11\x41\x44\x44RESS_NOT_FOUND\x10\x61\x12\x1a\n\x16\x41\x44\x44RESS_NOT_TARGETABLE\x10\x62\x42\xf7\x01\n\"com.google.ads.googleads.v4.errorsB\x1c\x46\x65\x65\x64ItemValidationErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v4/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V4.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V4\\Errors\xea\x02\"Google::Ads::GoogleAds::V4::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FEEDITEMVALIDATIONERRORENUM_FEEDITEMVALIDATIONERROR = _descriptor.EnumDescriptor(
  name='FeedItemValidationError',
  full_name='google.ads.googleads.v4.errors.FeedItemValidationErrorEnum.FeedItemValidationError',
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
      name='STRING_TOO_SHORT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING_TOO_LONG', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE_NOT_SPECIFIED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_DOMESTIC_PHONE_NUMBER_FORMAT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PHONE_NUMBER', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREMIUM_RATE_NUMBER_NOT_ALLOWED', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISALLOWED_NUMBER_TYPE', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE_OUT_OF_RANGE', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_NOT_WHITELISTED_FOR_CALLTRACKING', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_COUNTRY_CODE', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_APP_ID', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_ATTRIBUTES_FOR_FIELDS', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_TYPE_ID', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_EMAIL_ADDRESS', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_HTTPS_URL', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_DELIVERY_ADDRESS', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_DATE_AFTER_END_DATE', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_FEED_ITEM_START_TIME', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_FEED_ITEM_END_TIME', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_FEED_ITEM_ID', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VANITY_PHONE_NUMBER_NOT_ALLOWED', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_REVIEW_EXTENSION_SNIPPET', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_NUMBER_FORMAT', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_DATE_FORMAT', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PRICE_FORMAT', index=28, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_PLACEHOLDER_FIELD', index=29, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_ENHANCED_SITELINK_DESCRIPTION_LINE', index=30, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVIEW_EXTENSION_SOURCE_INELIGIBLE', index=31, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HYPHENS_IN_REVIEW_EXTENSION_SNIPPET', index=32, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE_QUOTES_IN_REVIEW_EXTENSION_SNIPPET', index=33, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUOTES_IN_REVIEW_EXTENSION_SNIPPET', index=34, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FORM_ENCODED_PARAMS', index=35, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_URL_PARAMETER_NAME', index=36, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_GEOCODING_RESULT', index=37, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT', index=38, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED', index=39, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PLACEHOLDER_FIELD_ID', index=40, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_URL_TAG', index=41, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST_TOO_LONG', index=42, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ATTRIBUTES_COMBINATION', index=43, number=43,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_VALUES', index=44, number=44,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CALL_CONVERSION_ACTION_ID', index=45, number=45,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_WITHOUT_FINAL_URLS', index=46, number=46,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APP_ID_DOESNT_EXIST_IN_APP_STORE', index=47, number=47,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FINAL_URL', index=48, number=48,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_TRACKING_URL', index=49, number=49,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FINAL_URL_FOR_APP_DOWNLOAD_URL', index=50, number=50,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST_TOO_SHORT', index=51, number=51,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_USER_ACTION', index=52, number=52,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_TYPE_NAME', index=53, number=53,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_EVENT_CHANGE_STATUS', index=54, number=54,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SNIPPETS_HEADER', index=55, number=55,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ANDROID_APP_LINK', index=56, number=56,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUMBER_TYPE_WITH_CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY', index=57, number=57,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESERVED_KEYWORD_OTHER', index=58, number=58,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_OPTION_LABELS', index=59, number=59,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_OPTION_PREFILLS', index=60, number=60,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNEQUAL_LIST_LENGTHS', index=61, number=61,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCONSISTENT_CURRENCY_CODES', index=62, number=62,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE_EXTENSION_HAS_DUPLICATED_HEADERS', index=63, number=63,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION', index=64, number=64,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE_EXTENSION_HAS_TOO_FEW_ITEMS', index=65, number=65,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_VALUE', index=66, number=66,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FINAL_MOBILE_URL', index=67, number=67,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_KEYWORDLESS_AD_RULE_LABEL', index=68, number=68,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE_TRACK_PARAMETER_NOT_SUPPORTED', index=69, number=69,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_VALUE_IN_SELECTED_LANGUAGE', index=70, number=70,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_IOS_APP_LINK', index=71, number=71,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_IOS_APP_LINK_OR_IOS_APP_STORE_ID', index=72, number=72,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMOTION_INVALID_TIME', index=73, number=73,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMOTION_CANNOT_SET_PERCENT_OFF_AND_MONEY_AMOUNT_OFF', index=74, number=74,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT', index=75, number=75,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_DECIMAL_PLACES_SPECIFIED', index=76, number=76,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AD_CUSTOMIZERS_NOT_ALLOWED', index=77, number=77,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_LANGUAGE_CODE', index=78, number=78,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_LANGUAGE', index=79, number=79,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IF_FUNCTION_NOT_ALLOWED', index=80, number=80,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FINAL_URL_SUFFIX', index=81, number=81,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_TAG_IN_FINAL_URL_SUFFIX', index=82, number=82,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FINAL_URL_SUFFIX_FORMAT', index=83, number=83,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED', index=84, number=84,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONLY_ONE_DELIVERY_OPTION_IS_ALLOWED', index=85, number=85,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_DELIVERY_OPTION_IS_SET', index=86, number=86,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CONVERSION_REPORTING_STATE', index=87, number=87,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_SIZE_WRONG', index=88, number=88,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMAIL_DELIVERY_NOT_AVAILABLE_IN_COUNTRY', index=89, number=89,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTO_REPLY_NOT_AVAILABLE_IN_COUNTRY', index=90, number=90,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_LATITUDE_VALUE', index=91, number=91,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_LONGITUDE_VALUE', index=92, number=92,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_LABELS', index=93, number=93,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_IMAGE_URL', index=94, number=94,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_LATITUDE_VALUE', index=95, number=95,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_LONGITUDE_VALUE', index=96, number=96,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_NOT_FOUND', index=97, number=97,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_NOT_TARGETABLE', index=98, number=98,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=168,
  serialized_end=3439,
)
_sym_db.RegisterEnumDescriptor(_FEEDITEMVALIDATIONERRORENUM_FEEDITEMVALIDATIONERROR)


_FEEDITEMVALIDATIONERRORENUM = _descriptor.Descriptor(
  name='FeedItemValidationErrorEnum',
  full_name='google.ads.googleads.v4.errors.FeedItemValidationErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEEDITEMVALIDATIONERRORENUM_FEEDITEMVALIDATIONERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=3439,
)

_FEEDITEMVALIDATIONERRORENUM_FEEDITEMVALIDATIONERROR.containing_type = _FEEDITEMVALIDATIONERRORENUM
DESCRIPTOR.message_types_by_name['FeedItemValidationErrorEnum'] = _FEEDITEMVALIDATIONERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedItemValidationErrorEnum = _reflection.GeneratedProtocolMessageType('FeedItemValidationErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _FEEDITEMVALIDATIONERRORENUM,
  __module__ = 'google.ads.googleads_v4.proto.errors.feed_item_validation_error_pb2'
  ,
  __doc__ = """Container for enum describing possible validation errors of a feed item.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.errors.FeedItemValidationErrorEnum)
  ))
_sym_db.RegisterMessage(FeedItemValidationErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
