# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/services/feed_mapping_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.resources import feed_mapping_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_feed__mapping__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/services/feed_mapping_service.proto',
  package='google.ads.googleads.v3.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v3.servicesB\027FeedMappingServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v3/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V3.Services\312\002 Google\\Ads\\GoogleAds\\V3\\Services\352\002$Google::Ads::GoogleAds::V3::Services'),
  serialized_pb=_b('\nAgoogle/ads/googleads_v3/proto/services/feed_mapping_service.proto\x12 google.ads.googleads.v3.services\x1a:google/ads/googleads_v3/proto/resources/feed_mapping.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto\"\\\n\x15GetFeedMappingRequest\x12\x43\n\rresource_name\x18\x01 \x01(\tB,\xe0\x41\x02\xfa\x41&\n$googleads.googleapis.com/FeedMapping\"\xb6\x01\n\x19MutateFeedMappingsRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12O\n\noperations\x18\x02 \x03(\x0b\x32\x36.google.ads.googleads.v3.services.FeedMappingOperationB\x03\xe0\x41\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"w\n\x14\x46\x65\x65\x64MappingOperation\x12@\n\x06\x63reate\x18\x01 \x01(\x0b\x32..google.ads.googleads.v3.resources.FeedMappingH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\x9b\x01\n\x1aMutateFeedMappingsResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12J\n\x07results\x18\x02 \x03(\x0b\x32\x39.google.ads.googleads.v3.services.MutateFeedMappingResult\"0\n\x17MutateFeedMappingResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xde\x03\n\x12\x46\x65\x65\x64MappingService\x12\xc1\x01\n\x0eGetFeedMapping\x12\x37.google.ads.googleads.v3.services.GetFeedMappingRequest\x1a..google.ads.googleads.v3.resources.FeedMapping\"F\x82\xd3\xe4\x93\x02\x30\x12./v3/{resource_name=customers/*/feedMappings/*}\xda\x41\rresource_name\x12\xe6\x01\n\x12MutateFeedMappings\x12;.google.ads.googleads.v3.services.MutateFeedMappingsRequest\x1a<.google.ads.googleads.v3.services.MutateFeedMappingsResponse\"U\x82\xd3\xe4\x93\x02\x36\"1/v3/customers/{customer_id=*}/feedMappings:mutate:\x01*\xda\x41\x16\x63ustomer_id,operations\x1a\x1b\xca\x41\x18googleads.googleapis.comB\xfe\x01\n$com.google.ads.googleads.v3.servicesB\x17\x46\x65\x65\x64MappingServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v3/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V3.Services\xca\x02 Google\\Ads\\GoogleAds\\V3\\Services\xea\x02$Google::Ads::GoogleAds::V3::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_feed__mapping__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETFEEDMAPPINGREQUEST = _descriptor.Descriptor(
  name='GetFeedMappingRequest',
  full_name='google.ads.googleads.v3.services.GetFeedMappingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.services.GetFeedMappingRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002\372A&\n$googleads.googleapis.com/FeedMapping'), file=DESCRIPTOR),
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
  serialized_start=303,
  serialized_end=395,
)


_MUTATEFEEDMAPPINGSREQUEST = _descriptor.Descriptor(
  name='MutateFeedMappingsRequest',
  full_name='google.ads.googleads.v3.services.MutateFeedMappingsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v3.services.MutateFeedMappingsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v3.services.MutateFeedMappingsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v3.services.MutateFeedMappingsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v3.services.MutateFeedMappingsRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=398,
  serialized_end=580,
)


_FEEDMAPPINGOPERATION = _descriptor.Descriptor(
  name='FeedMappingOperation',
  full_name='google.ads.googleads.v3.services.FeedMappingOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v3.services.FeedMappingOperation.create', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v3.services.FeedMappingOperation.remove', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
      name='operation', full_name='google.ads.googleads.v3.services.FeedMappingOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=582,
  serialized_end=701,
)


_MUTATEFEEDMAPPINGSRESPONSE = _descriptor.Descriptor(
  name='MutateFeedMappingsResponse',
  full_name='google.ads.googleads.v3.services.MutateFeedMappingsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v3.services.MutateFeedMappingsResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v3.services.MutateFeedMappingsResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=704,
  serialized_end=859,
)


_MUTATEFEEDMAPPINGRESULT = _descriptor.Descriptor(
  name='MutateFeedMappingResult',
  full_name='google.ads.googleads.v3.services.MutateFeedMappingResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.services.MutateFeedMappingResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=861,
  serialized_end=909,
)

_MUTATEFEEDMAPPINGSREQUEST.fields_by_name['operations'].message_type = _FEEDMAPPINGOPERATION
_FEEDMAPPINGOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_feed__mapping__pb2._FEEDMAPPING
_FEEDMAPPINGOPERATION.oneofs_by_name['operation'].fields.append(
  _FEEDMAPPINGOPERATION.fields_by_name['create'])
_FEEDMAPPINGOPERATION.fields_by_name['create'].containing_oneof = _FEEDMAPPINGOPERATION.oneofs_by_name['operation']
_FEEDMAPPINGOPERATION.oneofs_by_name['operation'].fields.append(
  _FEEDMAPPINGOPERATION.fields_by_name['remove'])
_FEEDMAPPINGOPERATION.fields_by_name['remove'].containing_oneof = _FEEDMAPPINGOPERATION.oneofs_by_name['operation']
_MUTATEFEEDMAPPINGSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATEFEEDMAPPINGSRESPONSE.fields_by_name['results'].message_type = _MUTATEFEEDMAPPINGRESULT
DESCRIPTOR.message_types_by_name['GetFeedMappingRequest'] = _GETFEEDMAPPINGREQUEST
DESCRIPTOR.message_types_by_name['MutateFeedMappingsRequest'] = _MUTATEFEEDMAPPINGSREQUEST
DESCRIPTOR.message_types_by_name['FeedMappingOperation'] = _FEEDMAPPINGOPERATION
DESCRIPTOR.message_types_by_name['MutateFeedMappingsResponse'] = _MUTATEFEEDMAPPINGSRESPONSE
DESCRIPTOR.message_types_by_name['MutateFeedMappingResult'] = _MUTATEFEEDMAPPINGRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFeedMappingRequest = _reflection.GeneratedProtocolMessageType('GetFeedMappingRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFEEDMAPPINGREQUEST,
  __module__ = 'google.ads.googleads_v3.proto.services.feed_mapping_service_pb2'
  ,
  __doc__ = """Request message for
  [FeedMappingService.GetFeedMapping][google.ads.googleads.v3.services.FeedMappingService.GetFeedMapping].
  
  
  Attributes:
      resource_name:
          Required. The resource name of the feed mapping to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.GetFeedMappingRequest)
  ))
_sym_db.RegisterMessage(GetFeedMappingRequest)

MutateFeedMappingsRequest = _reflection.GeneratedProtocolMessageType('MutateFeedMappingsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEFEEDMAPPINGSREQUEST,
  __module__ = 'google.ads.googleads_v3.proto.services.feed_mapping_service_pb2'
  ,
  __doc__ = """Request message for
  [FeedMappingService.MutateFeedMappings][google.ads.googleads.v3.services.FeedMappingService.MutateFeedMappings].
  
  
  Attributes:
      customer_id:
          Required. The ID of the customer whose feed mappings are being
          modified.
      operations:
          Required. The list of operations to perform on individual feed
          mappings.
      partial_failure:
          If true, successful operations will be carried out and invalid
          operations will return errors. If false, all operations will
          be carried out in one transaction if and only if they are all
          valid. Default is false.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.MutateFeedMappingsRequest)
  ))
_sym_db.RegisterMessage(MutateFeedMappingsRequest)

FeedMappingOperation = _reflection.GeneratedProtocolMessageType('FeedMappingOperation', (_message.Message,), dict(
  DESCRIPTOR = _FEEDMAPPINGOPERATION,
  __module__ = 'google.ads.googleads_v3.proto.services.feed_mapping_service_pb2'
  ,
  __doc__ = """A single operation (create, remove) on a feed mapping.
  
  
  Attributes:
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          feed mapping.
      remove:
          Remove operation: A resource name for the removed feed mapping
          is expected, in this format:  ``customers/{customer_id}/feedMa
          ppings/{feed_id}~{feed_mapping_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.FeedMappingOperation)
  ))
_sym_db.RegisterMessage(FeedMappingOperation)

MutateFeedMappingsResponse = _reflection.GeneratedProtocolMessageType('MutateFeedMappingsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEFEEDMAPPINGSRESPONSE,
  __module__ = 'google.ads.googleads_v3.proto.services.feed_mapping_service_pb2'
  ,
  __doc__ = """Response message for a feed mapping mutate.
  
  
  Attributes:
      partial_failure_error:
          Errors that pertain to operation failures in the partial
          failure mode. Returned only when partial\_failure = true and
          all errors occur inside the operations. If any errors occur
          outside the operations (e.g. auth errors), we return an RPC
          level error.
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.MutateFeedMappingsResponse)
  ))
_sym_db.RegisterMessage(MutateFeedMappingsResponse)

MutateFeedMappingResult = _reflection.GeneratedProtocolMessageType('MutateFeedMappingResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEFEEDMAPPINGRESULT,
  __module__ = 'google.ads.googleads_v3.proto.services.feed_mapping_service_pb2'
  ,
  __doc__ = """The result for the feed mapping mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.MutateFeedMappingResult)
  ))
_sym_db.RegisterMessage(MutateFeedMappingResult)


DESCRIPTOR._options = None
_GETFEEDMAPPINGREQUEST.fields_by_name['resource_name']._options = None
_MUTATEFEEDMAPPINGSREQUEST.fields_by_name['customer_id']._options = None
_MUTATEFEEDMAPPINGSREQUEST.fields_by_name['operations']._options = None

_FEEDMAPPINGSERVICE = _descriptor.ServiceDescriptor(
  name='FeedMappingService',
  full_name='google.ads.googleads.v3.services.FeedMappingService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312A\030googleads.googleapis.com'),
  serialized_start=912,
  serialized_end=1390,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeedMapping',
    full_name='google.ads.googleads.v3.services.FeedMappingService.GetFeedMapping',
    index=0,
    containing_service=None,
    input_type=_GETFEEDMAPPINGREQUEST,
    output_type=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_feed__mapping__pb2._FEEDMAPPING,
    serialized_options=_b('\202\323\344\223\0020\022./v3/{resource_name=customers/*/feedMappings/*}\332A\rresource_name'),
  ),
  _descriptor.MethodDescriptor(
    name='MutateFeedMappings',
    full_name='google.ads.googleads.v3.services.FeedMappingService.MutateFeedMappings',
    index=1,
    containing_service=None,
    input_type=_MUTATEFEEDMAPPINGSREQUEST,
    output_type=_MUTATEFEEDMAPPINGSRESPONSE,
    serialized_options=_b('\202\323\344\223\0026\"1/v3/customers/{customer_id=*}/feedMappings:mutate:\001*\332A\026customer_id,operations'),
  ),
])
_sym_db.RegisterServiceDescriptor(_FEEDMAPPINGSERVICE)

DESCRIPTOR.services_by_name['FeedMappingService'] = _FEEDMAPPINGSERVICE

# @@protoc_insertion_point(module_scope)
