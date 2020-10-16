# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/services/ad_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v5.proto.enums import response_content_type_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_response__content__type__pb2
from google.ads.google_ads.v5.proto.resources import ad_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_ad__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/services/ad_service.proto',
  package='google.ads.googleads.v5.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v5.servicesB\016AdServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v5/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V5.Services\312\002 Google\\Ads\\GoogleAds\\V5\\Services\352\002$Google::Ads::GoogleAds::V5::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7google/ads/googleads_v5/proto/services/ad_service.proto\x12 google.ads.googleads.v5.services\x1a?google/ads/googleads_v5/proto/enums/response_content_type.proto\x1a\x30google/ads/googleads_v5/proto/resources/ad.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"J\n\x0cGetAdRequest\x12:\n\rresource_name\x18\x01 \x01(\tB#\xe0\x41\x02\xfa\x41\x1d\n\x1bgoogleads.googleapis.com/Ad\"\xdf\x01\n\x10MutateAdsRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x46\n\noperations\x18\x02 \x03(\x0b\x32-.google.ads.googleads.v5.services.AdOperationB\x03\xe0\x41\x02\x12i\n\x15response_content_type\x18\x05 \x01(\x0e\x32J.google.ads.googleads.v5.enums.ResponseContentTypeEnum.ResponseContentType\"\x84\x01\n\x0b\x41\x64Operation\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x37\n\x06update\x18\x01 \x01(\x0b\x32%.google.ads.googleads.v5.resources.AdH\x00\x42\x0b\n\toperation\"V\n\x11MutateAdsResponse\x12\x41\n\x07results\x18\x02 \x03(\x0b\x32\x30.google.ads.googleads.v5.services.MutateAdResult\"Z\n\x0eMutateAdResult\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x31\n\x02\x61\x64\x18\x02 \x01(\x0b\x32%.google.ads.googleads.v5.resources.Ad2\x8d\x03\n\tAdService\x12\x9d\x01\n\x05GetAd\x12..google.ads.googleads.v5.services.GetAdRequest\x1a%.google.ads.googleads.v5.resources.Ad\"=\x82\xd3\xe4\x93\x02\'\x12%/v5/{resource_name=customers/*/ads/*}\xda\x41\rresource_name\x12\xc2\x01\n\tMutateAds\x12\x32.google.ads.googleads.v5.services.MutateAdsRequest\x1a\x33.google.ads.googleads.v5.services.MutateAdsResponse\"L\x82\xd3\xe4\x93\x02-\"(/v5/customers/{customer_id=*}/ads:mutate:\x01*\xda\x41\x16\x63ustomer_id,operations\x1a\x1b\xca\x41\x18googleads.googleapis.comB\xf5\x01\n$com.google.ads.googleads.v5.servicesB\x0e\x41\x64ServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v5/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V5.Services\xca\x02 Google\\Ads\\GoogleAds\\V5\\Services\xea\x02$Google::Ads::GoogleAds::V5::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_response__content__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_ad__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_GETADREQUEST = _descriptor.Descriptor(
  name='GetAdRequest',
  full_name='google.ads.googleads.v5.services.GetAdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v5.services.GetAdRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\035\n\033googleads.googleapis.com/Ad', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=357,
  serialized_end=431,
)


_MUTATEADSREQUEST = _descriptor.Descriptor(
  name='MutateAdsRequest',
  full_name='google.ads.googleads.v5.services.MutateAdsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v5.services.MutateAdsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v5.services.MutateAdsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_content_type', full_name='google.ads.googleads.v5.services.MutateAdsRequest.response_content_type', index=2,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=434,
  serialized_end=657,
)


_ADOPERATION = _descriptor.Descriptor(
  name='AdOperation',
  full_name='google.ads.googleads.v5.services.AdOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v5.services.AdOperation.update_mask', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v5.services.AdOperation.update', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v5.services.AdOperation.operation',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=660,
  serialized_end=792,
)


_MUTATEADSRESPONSE = _descriptor.Descriptor(
  name='MutateAdsResponse',
  full_name='google.ads.googleads.v5.services.MutateAdsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v5.services.MutateAdsResponse.results', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=794,
  serialized_end=880,
)


_MUTATEADRESULT = _descriptor.Descriptor(
  name='MutateAdResult',
  full_name='google.ads.googleads.v5.services.MutateAdResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v5.services.MutateAdResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad', full_name='google.ads.googleads.v5.services.MutateAdResult.ad', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=882,
  serialized_end=972,
)

_MUTATEADSREQUEST.fields_by_name['operations'].message_type = _ADOPERATION
_MUTATEADSREQUEST.fields_by_name['response_content_type'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_response__content__type__pb2._RESPONSECONTENTTYPEENUM_RESPONSECONTENTTYPE
_ADOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_ADOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_ad__pb2._AD
_ADOPERATION.oneofs_by_name['operation'].fields.append(
  _ADOPERATION.fields_by_name['update'])
_ADOPERATION.fields_by_name['update'].containing_oneof = _ADOPERATION.oneofs_by_name['operation']
_MUTATEADSRESPONSE.fields_by_name['results'].message_type = _MUTATEADRESULT
_MUTATEADRESULT.fields_by_name['ad'].message_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_ad__pb2._AD
DESCRIPTOR.message_types_by_name['GetAdRequest'] = _GETADREQUEST
DESCRIPTOR.message_types_by_name['MutateAdsRequest'] = _MUTATEADSREQUEST
DESCRIPTOR.message_types_by_name['AdOperation'] = _ADOPERATION
DESCRIPTOR.message_types_by_name['MutateAdsResponse'] = _MUTATEADSRESPONSE
DESCRIPTOR.message_types_by_name['MutateAdResult'] = _MUTATEADRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAdRequest = _reflection.GeneratedProtocolMessageType('GetAdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETADREQUEST,
  '__module__' : 'google.ads.googleads_v5.proto.services.ad_service_pb2'
  ,
  '__doc__': """Request message for
  [AdService.GetAd][google.ads.googleads.v5.services.AdService.GetAd].
  
  Attributes:
      resource_name:
          Required. The resource name of the ad to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.GetAdRequest)
  })
_sym_db.RegisterMessage(GetAdRequest)

MutateAdsRequest = _reflection.GeneratedProtocolMessageType('MutateAdsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEADSREQUEST,
  '__module__' : 'google.ads.googleads_v5.proto.services.ad_service_pb2'
  ,
  '__doc__': """Request message for [AdService.MutateAds][google.ads.googleads.v5.serv
  ices.AdService.MutateAds].
  
  Attributes:
      customer_id:
          Required. The ID of the customer whose ads are being modified.
      operations:
          Required. The list of operations to perform on individual ads.
      response_content_type:
          The response content type setting. Determines whether the
          mutable resource or just the resource name should be returned
          post mutation.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.MutateAdsRequest)
  })
_sym_db.RegisterMessage(MutateAdsRequest)

AdOperation = _reflection.GeneratedProtocolMessageType('AdOperation', (_message.Message,), {
  'DESCRIPTOR' : _ADOPERATION,
  '__module__' : 'google.ads.googleads_v5.proto.services.ad_service_pb2'
  ,
  '__doc__': """A single update operation on an ad.
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The mutate operation.
      update:
          Update operation: The ad is expected to have a valid resource
          name in this format:  ``customers/{customer_id}/ads/{ad_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.AdOperation)
  })
_sym_db.RegisterMessage(AdOperation)

MutateAdsResponse = _reflection.GeneratedProtocolMessageType('MutateAdsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEADSRESPONSE,
  '__module__' : 'google.ads.googleads_v5.proto.services.ad_service_pb2'
  ,
  '__doc__': """Response message for an ad mutate.
  
  Attributes:
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.MutateAdsResponse)
  })
_sym_db.RegisterMessage(MutateAdsResponse)

MutateAdResult = _reflection.GeneratedProtocolMessageType('MutateAdResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEADRESULT,
  '__module__' : 'google.ads.googleads_v5.proto.services.ad_service_pb2'
  ,
  '__doc__': """The result for the ad mutate.
  
  Attributes:
      resource_name:
          The resource name returned for successful operations.
      ad:
          The mutated ad with only mutable fields after mutate. The
          field will only be returned when response\_content\_type is
          set to "MUTABLE\_RESOURCE".
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.MutateAdResult)
  })
_sym_db.RegisterMessage(MutateAdResult)


DESCRIPTOR._options = None
_GETADREQUEST.fields_by_name['resource_name']._options = None
_MUTATEADSREQUEST.fields_by_name['customer_id']._options = None
_MUTATEADSREQUEST.fields_by_name['operations']._options = None

_ADSERVICE = _descriptor.ServiceDescriptor(
  name='AdService',
  full_name='google.ads.googleads.v5.services.AdService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  create_key=_descriptor._internal_create_key,
  serialized_start=975,
  serialized_end=1372,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAd',
    full_name='google.ads.googleads.v5.services.AdService.GetAd',
    index=0,
    containing_service=None,
    input_type=_GETADREQUEST,
    output_type=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_ad__pb2._AD,
    serialized_options=b'\202\323\344\223\002\'\022%/v5/{resource_name=customers/*/ads/*}\332A\rresource_name',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MutateAds',
    full_name='google.ads.googleads.v5.services.AdService.MutateAds',
    index=1,
    containing_service=None,
    input_type=_MUTATEADSREQUEST,
    output_type=_MUTATEADSRESPONSE,
    serialized_options=b'\202\323\344\223\002-\"(/v5/customers/{customer_id=*}/ads:mutate:\001*\332A\026customer_id,operations',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ADSERVICE)

DESCRIPTOR.services_by_name['AdService'] = _ADSERVICE

# @@protoc_insertion_point(module_scope)
