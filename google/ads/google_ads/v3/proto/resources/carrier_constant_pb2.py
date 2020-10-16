# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/resources/carrier_constant.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/resources/carrier_constant.proto',
  package='google.ads.googleads.v3.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v3.resourcesB\024CarrierConstantProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V3.Resources\312\002!Google\\Ads\\GoogleAds\\V3\\Resources\352\002%Google::Ads::GoogleAds::V3::Resources'),
  serialized_pb=_b('\n>google/ads/googleads_v3/proto/resources/carrier_constant.proto\x12!google.ads.googleads.v3.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xc6\x02\n\x0f\x43\x61rrierConstant\x12G\n\rresource_name\x18\x01 \x01(\tB0\xe0\x41\x03\xfa\x41*\n(googleads.googleapis.com/CarrierConstant\x12,\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x03\xe0\x41\x03\x12/\n\x04name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x03\xe0\x41\x03\x12\x37\n\x0c\x63ountry_code\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x03\xe0\x41\x03:R\xea\x41O\n(googleads.googleapis.com/CarrierConstant\x12#carrierConstants/{carrier_constant}B\x81\x02\n%com.google.ads.googleads.v3.resourcesB\x14\x43\x61rrierConstantProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V3.Resources\xca\x02!Google\\Ads\\GoogleAds\\V3\\Resources\xea\x02%Google::Ads::GoogleAds::V3::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CARRIERCONSTANT = _descriptor.Descriptor(
  name='CarrierConstant',
  full_name='google.ads.googleads.v3.resources.CarrierConstant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.resources.CarrierConstant.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003\372A*\n(googleads.googleapis.com/CarrierConstant'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v3.resources.CarrierConstant.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v3.resources.CarrierConstant.name', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='google.ads.googleads.v3.resources.CarrierConstant.country_code', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\352AO\n(googleads.googleapis.com/CarrierConstant\022#carrierConstants/{carrier_constant}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=550,
)

_CARRIERCONSTANT.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CARRIERCONSTANT.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CARRIERCONSTANT.fields_by_name['country_code'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['CarrierConstant'] = _CARRIERCONSTANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CarrierConstant = _reflection.GeneratedProtocolMessageType('CarrierConstant', (_message.Message,), dict(
  DESCRIPTOR = _CARRIERCONSTANT,
  __module__ = 'google.ads.googleads_v3.proto.resources.carrier_constant_pb2'
  ,
  __doc__ = """A carrier criterion that can be used in campaign targeting.
  
  
  Attributes:
      resource_name:
          Output only. The resource name of the carrier criterion.
          Carrier criterion resource names have the form:
          ``carrierConstants/{criterion_id}``
      id:
          Output only. The ID of the carrier criterion.
      name:
          Output only. The full name of the carrier in English.
      country_code:
          Output only. The country code of the country where the carrier
          is located, e.g., "AR", "FR", etc.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.resources.CarrierConstant)
  ))
_sym_db.RegisterMessage(CarrierConstant)


DESCRIPTOR._options = None
_CARRIERCONSTANT.fields_by_name['resource_name']._options = None
_CARRIERCONSTANT.fields_by_name['id']._options = None
_CARRIERCONSTANT.fields_by_name['name']._options = None
_CARRIERCONSTANT.fields_by_name['country_code']._options = None
_CARRIERCONSTANT._options = None
# @@protoc_insertion_point(module_scope)
