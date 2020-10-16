# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/resources/operating_system_version_constant.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v4.proto.enums import operating_system_version_operator_type_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_enums_dot_operating__system__version__operator__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v4/proto/resources/operating_system_version_constant.proto',
  package='google.ads.googleads.v4.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v4.resourcesB#OperatingSystemVersionConstantProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v4/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V4.Resources\312\002!Google\\Ads\\GoogleAds\\V4\\Resources\352\002%Google::Ads::GoogleAds::V4::Resources'),
  serialized_pb=_b('\nOgoogle/ads/googleads_v4/proto/resources/operating_system_version_constant.proto\x12!google.ads.googleads.v4.resources\x1aPgoogle/ads/googleads_v4/proto/enums/operating_system_version_operator_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xda\x04\n\x1eOperatingSystemVersionConstant\x12V\n\rresource_name\x18\x01 \x01(\tB?\xe0\x41\x03\xfa\x41\x39\n7googleads.googleapis.com/OperatingSystemVersionConstant\x12,\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x03\xe0\x41\x03\x12/\n\x04name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x03\xe0\x41\x03\x12:\n\x10os_major_version\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueB\x03\xe0\x41\x03\x12:\n\x10os_minor_version\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueB\x03\xe0\x41\x03\x12\x84\x01\n\roperator_type\x18\x06 \x01(\x0e\x32h.google.ads.googleads.v4.enums.OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorTypeB\x03\xe0\x41\x03:\x81\x01\xea\x41~\n7googleads.googleapis.com/OperatingSystemVersionConstant\x12\x43operatingSystemVersionConstants/{operating_system_version_constant}B\x90\x02\n%com.google.ads.googleads.v4.resourcesB#OperatingSystemVersionConstantProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v4/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V4.Resources\xca\x02!Google\\Ads\\GoogleAds\\V4\\Resources\xea\x02%Google::Ads::GoogleAds::V4::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v4_dot_proto_dot_enums_dot_operating__system__version__operator__type__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_OPERATINGSYSTEMVERSIONCONSTANT = _descriptor.Descriptor(
  name='OperatingSystemVersionConstant',
  full_name='google.ads.googleads.v4.resources.OperatingSystemVersionConstant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.resources.OperatingSystemVersionConstant.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003\372A9\n7googleads.googleapis.com/OperatingSystemVersionConstant'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v4.resources.OperatingSystemVersionConstant.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v4.resources.OperatingSystemVersionConstant.name', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='os_major_version', full_name='google.ads.googleads.v4.resources.OperatingSystemVersionConstant.os_major_version', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='os_minor_version', full_name='google.ads.googleads.v4.resources.OperatingSystemVersionConstant.os_minor_version', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operator_type', full_name='google.ads.googleads.v4.resources.OperatingSystemVersionConstant.operator_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\352A~\n7googleads.googleapis.com/OperatingSystemVersionConstant\022CoperatingSystemVersionConstants/{operating_system_version_constant}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=323,
  serialized_end=925,
)

_OPERATINGSYSTEMVERSIONCONSTANT.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_OPERATINGSYSTEMVERSIONCONSTANT.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_OPERATINGSYSTEMVERSIONCONSTANT.fields_by_name['os_major_version'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_OPERATINGSYSTEMVERSIONCONSTANT.fields_by_name['os_minor_version'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_OPERATINGSYSTEMVERSIONCONSTANT.fields_by_name['operator_type'].enum_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_enums_dot_operating__system__version__operator__type__pb2._OPERATINGSYSTEMVERSIONOPERATORTYPEENUM_OPERATINGSYSTEMVERSIONOPERATORTYPE
DESCRIPTOR.message_types_by_name['OperatingSystemVersionConstant'] = _OPERATINGSYSTEMVERSIONCONSTANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OperatingSystemVersionConstant = _reflection.GeneratedProtocolMessageType('OperatingSystemVersionConstant', (_message.Message,), dict(
  DESCRIPTOR = _OPERATINGSYSTEMVERSIONCONSTANT,
  __module__ = 'google.ads.googleads_v4.proto.resources.operating_system_version_constant_pb2'
  ,
  __doc__ = """A mobile operating system version or a range of versions, depending on
  ``operator_type``. List of available mobile platforms at
  https://developers.google.com/adwords/api/docs/appendix/codes-formats#mobile-platforms
  
  
  Attributes:
      resource_name:
          Output only. The resource name of the operating system version
          constant. Operating system version constant resource names
          have the form:
          ``operatingSystemVersionConstants/{criterion_id}``
      id:
          Output only. The ID of the operating system version.
      name:
          Output only. Name of the operating system.
      os_major_version:
          Output only. The OS Major Version number.
      os_minor_version:
          Output only. The OS Minor Version number.
      operator_type:
          Output only. Determines whether this constant represents a
          single version or a range of versions.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.resources.OperatingSystemVersionConstant)
  ))
_sym_db.RegisterMessage(OperatingSystemVersionConstant)


DESCRIPTOR._options = None
_OPERATINGSYSTEMVERSIONCONSTANT.fields_by_name['resource_name']._options = None
_OPERATINGSYSTEMVERSIONCONSTANT.fields_by_name['id']._options = None
_OPERATINGSYSTEMVERSIONCONSTANT.fields_by_name['name']._options = None
_OPERATINGSYSTEMVERSIONCONSTANT.fields_by_name['os_major_version']._options = None
_OPERATINGSYSTEMVERSIONCONSTANT.fields_by_name['os_minor_version']._options = None
_OPERATINGSYSTEMVERSIONCONSTANT.fields_by_name['operator_type']._options = None
_OPERATINGSYSTEMVERSIONCONSTANT._options = None
# @@protoc_insertion_point(module_scope)
