# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/resources/shared_criterion.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v4.proto.common import criteria_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_common_dot_criteria__pb2
from google.ads.google_ads.v4.proto.enums import criterion_type_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_enums_dot_criterion__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v4/proto/resources/shared_criterion.proto',
  package='google.ads.googleads.v4.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v4.resourcesB\024SharedCriterionProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v4/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V4.Resources\312\002!Google\\Ads\\GoogleAds\\V4\\Resources\352\002%Google::Ads::GoogleAds::V4::Resources'),
  serialized_pb=_b('\n>google/ads/googleads_v4/proto/resources/shared_criterion.proto\x12!google.ads.googleads.v4.resources\x1a\x33google/ads/googleads_v4/proto/common/criteria.proto\x1a\x38google/ads/googleads_v4/proto/enums/criterion_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\x9e\x07\n\x0fSharedCriterion\x12G\n\rresource_name\x18\x01 \x01(\tB0\xe0\x41\x05\xfa\x41*\n(googleads.googleapis.com/SharedCriterion\x12\\\n\nshared_set\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueB*\xe0\x41\x05\xfa\x41$\n\"googleads.googleapis.com/SharedSet\x12\x36\n\x0c\x63riterion_id\x18\x1a \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x03\xe0\x41\x03\x12Q\n\x04type\x18\x04 \x01(\x0e\x32>.google.ads.googleads.v4.enums.CriterionTypeEnum.CriterionTypeB\x03\xe0\x41\x03\x12\x43\n\x07keyword\x18\x03 \x01(\x0b\x32+.google.ads.googleads.v4.common.KeywordInfoB\x03\xe0\x41\x05H\x00\x12N\n\ryoutube_video\x18\x05 \x01(\x0b\x32\x30.google.ads.googleads.v4.common.YouTubeVideoInfoB\x03\xe0\x41\x05H\x00\x12R\n\x0fyoutube_channel\x18\x06 \x01(\x0b\x32\x32.google.ads.googleads.v4.common.YouTubeChannelInfoB\x03\xe0\x41\x05H\x00\x12G\n\tplacement\x18\x07 \x01(\x0b\x32-.google.ads.googleads.v4.common.PlacementInfoB\x03\xe0\x41\x05H\x00\x12Y\n\x13mobile_app_category\x18\x08 \x01(\x0b\x32\x35.google.ads.googleads.v4.common.MobileAppCategoryInfoB\x03\xe0\x41\x05H\x00\x12X\n\x12mobile_application\x18\t \x01(\x0b\x32\x35.google.ads.googleads.v4.common.MobileApplicationInfoB\x03\xe0\x41\x05H\x00:e\xea\x41\x62\n(googleads.googleapis.com/SharedCriterion\x12\x36\x63ustomers/{customer}/sharedCriteria/{shared_criterion}B\x0b\n\tcriterionB\x81\x02\n%com.google.ads.googleads.v4.resourcesB\x14SharedCriterionProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v4/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V4.Resources\xca\x02!Google\\Ads\\GoogleAds\\V4\\Resources\xea\x02%Google::Ads::GoogleAds::V4::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v4_dot_proto_dot_common_dot_criteria__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v4_dot_proto_dot_enums_dot_criterion__type__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_SHAREDCRITERION = _descriptor.Descriptor(
  name='SharedCriterion',
  full_name='google.ads.googleads.v4.resources.SharedCriterion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.resources.SharedCriterion.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005\372A*\n(googleads.googleapis.com/SharedCriterion'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shared_set', full_name='google.ads.googleads.v4.resources.SharedCriterion.shared_set', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005\372A$\n\"googleads.googleapis.com/SharedSet'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='criterion_id', full_name='google.ads.googleads.v4.resources.SharedCriterion.criterion_id', index=2,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.ads.googleads.v4.resources.SharedCriterion.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword', full_name='google.ads.googleads.v4.resources.SharedCriterion.keyword', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='youtube_video', full_name='google.ads.googleads.v4.resources.SharedCriterion.youtube_video', index=5,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='youtube_channel', full_name='google.ads.googleads.v4.resources.SharedCriterion.youtube_channel', index=6,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='placement', full_name='google.ads.googleads.v4.resources.SharedCriterion.placement', index=7,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mobile_app_category', full_name='google.ads.googleads.v4.resources.SharedCriterion.mobile_app_category', index=8,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mobile_application', full_name='google.ads.googleads.v4.resources.SharedCriterion.mobile_application', index=9,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\352Ab\n(googleads.googleapis.com/SharedCriterion\0226customers/{customer}/sharedCriteria/{shared_criterion}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='criterion', full_name='google.ads.googleads.v4.resources.SharedCriterion.criterion',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=335,
  serialized_end=1261,
)

_SHAREDCRITERION.fields_by_name['shared_set'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SHAREDCRITERION.fields_by_name['criterion_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SHAREDCRITERION.fields_by_name['type'].enum_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_enums_dot_criterion__type__pb2._CRITERIONTYPEENUM_CRITERIONTYPE
_SHAREDCRITERION.fields_by_name['keyword'].message_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_common_dot_criteria__pb2._KEYWORDINFO
_SHAREDCRITERION.fields_by_name['youtube_video'].message_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_common_dot_criteria__pb2._YOUTUBEVIDEOINFO
_SHAREDCRITERION.fields_by_name['youtube_channel'].message_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_common_dot_criteria__pb2._YOUTUBECHANNELINFO
_SHAREDCRITERION.fields_by_name['placement'].message_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_common_dot_criteria__pb2._PLACEMENTINFO
_SHAREDCRITERION.fields_by_name['mobile_app_category'].message_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_common_dot_criteria__pb2._MOBILEAPPCATEGORYINFO
_SHAREDCRITERION.fields_by_name['mobile_application'].message_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_common_dot_criteria__pb2._MOBILEAPPLICATIONINFO
_SHAREDCRITERION.oneofs_by_name['criterion'].fields.append(
  _SHAREDCRITERION.fields_by_name['keyword'])
_SHAREDCRITERION.fields_by_name['keyword'].containing_oneof = _SHAREDCRITERION.oneofs_by_name['criterion']
_SHAREDCRITERION.oneofs_by_name['criterion'].fields.append(
  _SHAREDCRITERION.fields_by_name['youtube_video'])
_SHAREDCRITERION.fields_by_name['youtube_video'].containing_oneof = _SHAREDCRITERION.oneofs_by_name['criterion']
_SHAREDCRITERION.oneofs_by_name['criterion'].fields.append(
  _SHAREDCRITERION.fields_by_name['youtube_channel'])
_SHAREDCRITERION.fields_by_name['youtube_channel'].containing_oneof = _SHAREDCRITERION.oneofs_by_name['criterion']
_SHAREDCRITERION.oneofs_by_name['criterion'].fields.append(
  _SHAREDCRITERION.fields_by_name['placement'])
_SHAREDCRITERION.fields_by_name['placement'].containing_oneof = _SHAREDCRITERION.oneofs_by_name['criterion']
_SHAREDCRITERION.oneofs_by_name['criterion'].fields.append(
  _SHAREDCRITERION.fields_by_name['mobile_app_category'])
_SHAREDCRITERION.fields_by_name['mobile_app_category'].containing_oneof = _SHAREDCRITERION.oneofs_by_name['criterion']
_SHAREDCRITERION.oneofs_by_name['criterion'].fields.append(
  _SHAREDCRITERION.fields_by_name['mobile_application'])
_SHAREDCRITERION.fields_by_name['mobile_application'].containing_oneof = _SHAREDCRITERION.oneofs_by_name['criterion']
DESCRIPTOR.message_types_by_name['SharedCriterion'] = _SHAREDCRITERION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SharedCriterion = _reflection.GeneratedProtocolMessageType('SharedCriterion', (_message.Message,), dict(
  DESCRIPTOR = _SHAREDCRITERION,
  __module__ = 'google.ads.googleads_v4.proto.resources.shared_criterion_pb2'
  ,
  __doc__ = """A criterion belonging to a shared set.
  
  
  Attributes:
      resource_name:
          Immutable. The resource name of the shared criterion. Shared
          set resource names have the form:  ``customers/{customer_id}/s
          haredCriteria/{shared_set_id}~{criterion_id}``
      shared_set:
          Immutable. The shared set to which the shared criterion
          belongs.
      criterion_id:
          Output only. The ID of the criterion.  This field is ignored
          for mutates.
      type:
          Output only. The type of the criterion.
      criterion:
          The criterion.  Exactly one must be set.
      keyword:
          Immutable. Keyword.
      youtube_video:
          Immutable. YouTube Video.
      youtube_channel:
          Immutable. YouTube Channel.
      placement:
          Immutable. Placement.
      mobile_app_category:
          Immutable. Mobile App Category.
      mobile_application:
          Immutable. Mobile application.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.resources.SharedCriterion)
  ))
_sym_db.RegisterMessage(SharedCriterion)


DESCRIPTOR._options = None
_SHAREDCRITERION.fields_by_name['resource_name']._options = None
_SHAREDCRITERION.fields_by_name['shared_set']._options = None
_SHAREDCRITERION.fields_by_name['criterion_id']._options = None
_SHAREDCRITERION.fields_by_name['type']._options = None
_SHAREDCRITERION.fields_by_name['keyword']._options = None
_SHAREDCRITERION.fields_by_name['youtube_video']._options = None
_SHAREDCRITERION.fields_by_name['youtube_channel']._options = None
_SHAREDCRITERION.fields_by_name['placement']._options = None
_SHAREDCRITERION.fields_by_name['mobile_app_category']._options = None
_SHAREDCRITERION.fields_by_name['mobile_application']._options = None
_SHAREDCRITERION._options = None
# @@protoc_insertion_point(module_scope)
