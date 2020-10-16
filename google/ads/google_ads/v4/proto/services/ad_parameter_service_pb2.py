# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/services/ad_parameter_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v4.proto.resources import ad_parameter_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__parameter__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v4/proto/services/ad_parameter_service.proto',
  package='google.ads.googleads.v4.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v4.servicesB\027AdParameterServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v4/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V4.Services\312\002 Google\\Ads\\GoogleAds\\V4\\Services\352\002$Google::Ads::GoogleAds::V4::Services'),
  serialized_pb=_b('\nAgoogle/ads/googleads_v4/proto/services/ad_parameter_service.proto\x12 google.ads.googleads.v4.services\x1a:google/ads/googleads_v4/proto/resources/ad_parameter.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\"\\\n\x15GetAdParameterRequest\x12\x43\n\rresource_name\x18\x01 \x01(\tB,\xe0\x41\x02\xfa\x41&\n$googleads.googleapis.com/AdParameter\"\xb6\x01\n\x19MutateAdParametersRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12O\n\noperations\x18\x02 \x03(\x0b\x32\x36.google.ads.googleads.v4.services.AdParameterOperationB\x03\xe0\x41\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\xea\x01\n\x14\x41\x64ParameterOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12@\n\x06\x63reate\x18\x01 \x01(\x0b\x32..google.ads.googleads.v4.resources.AdParameterH\x00\x12@\n\x06update\x18\x02 \x01(\x0b\x32..google.ads.googleads.v4.resources.AdParameterH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\x9b\x01\n\x1aMutateAdParametersResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12J\n\x07results\x18\x02 \x03(\x0b\x32\x39.google.ads.googleads.v4.services.MutateAdParameterResult\"0\n\x17MutateAdParameterResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xde\x03\n\x12\x41\x64ParameterService\x12\xc1\x01\n\x0eGetAdParameter\x12\x37.google.ads.googleads.v4.services.GetAdParameterRequest\x1a..google.ads.googleads.v4.resources.AdParameter\"F\x82\xd3\xe4\x93\x02\x30\x12./v4/{resource_name=customers/*/adParameters/*}\xda\x41\rresource_name\x12\xe6\x01\n\x12MutateAdParameters\x12;.google.ads.googleads.v4.services.MutateAdParametersRequest\x1a<.google.ads.googleads.v4.services.MutateAdParametersResponse\"U\x82\xd3\xe4\x93\x02\x36\"1/v4/customers/{customer_id=*}/adParameters:mutate:\x01*\xda\x41\x16\x63ustomer_id,operations\x1a\x1b\xca\x41\x18googleads.googleapis.comB\xfe\x01\n$com.google.ads.googleads.v4.servicesB\x17\x41\x64ParameterServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v4/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V4.Services\xca\x02 Google\\Ads\\GoogleAds\\V4\\Services\xea\x02$Google::Ads::GoogleAds::V4::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__parameter__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETADPARAMETERREQUEST = _descriptor.Descriptor(
  name='GetAdParameterRequest',
  full_name='google.ads.googleads.v4.services.GetAdParameterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.services.GetAdParameterRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002\372A&\n$googleads.googleapis.com/AdParameter'), file=DESCRIPTOR),
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
  serialized_start=337,
  serialized_end=429,
)


_MUTATEADPARAMETERSREQUEST = _descriptor.Descriptor(
  name='MutateAdParametersRequest',
  full_name='google.ads.googleads.v4.services.MutateAdParametersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v4.services.MutateAdParametersRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v4.services.MutateAdParametersRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v4.services.MutateAdParametersRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v4.services.MutateAdParametersRequest.validate_only', index=3,
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
  serialized_start=432,
  serialized_end=614,
)


_ADPARAMETEROPERATION = _descriptor.Descriptor(
  name='AdParameterOperation',
  full_name='google.ads.googleads.v4.services.AdParameterOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v4.services.AdParameterOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v4.services.AdParameterOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v4.services.AdParameterOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v4.services.AdParameterOperation.remove', index=3,
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
      name='operation', full_name='google.ads.googleads.v4.services.AdParameterOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=617,
  serialized_end=851,
)


_MUTATEADPARAMETERSRESPONSE = _descriptor.Descriptor(
  name='MutateAdParametersResponse',
  full_name='google.ads.googleads.v4.services.MutateAdParametersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v4.services.MutateAdParametersResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v4.services.MutateAdParametersResponse.results', index=1,
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
  serialized_start=854,
  serialized_end=1009,
)


_MUTATEADPARAMETERRESULT = _descriptor.Descriptor(
  name='MutateAdParameterResult',
  full_name='google.ads.googleads.v4.services.MutateAdParameterResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.services.MutateAdParameterResult.resource_name', index=0,
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
  serialized_start=1011,
  serialized_end=1059,
)

_MUTATEADPARAMETERSREQUEST.fields_by_name['operations'].message_type = _ADPARAMETEROPERATION
_ADPARAMETEROPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_ADPARAMETEROPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__parameter__pb2._ADPARAMETER
_ADPARAMETEROPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__parameter__pb2._ADPARAMETER
_ADPARAMETEROPERATION.oneofs_by_name['operation'].fields.append(
  _ADPARAMETEROPERATION.fields_by_name['create'])
_ADPARAMETEROPERATION.fields_by_name['create'].containing_oneof = _ADPARAMETEROPERATION.oneofs_by_name['operation']
_ADPARAMETEROPERATION.oneofs_by_name['operation'].fields.append(
  _ADPARAMETEROPERATION.fields_by_name['update'])
_ADPARAMETEROPERATION.fields_by_name['update'].containing_oneof = _ADPARAMETEROPERATION.oneofs_by_name['operation']
_ADPARAMETEROPERATION.oneofs_by_name['operation'].fields.append(
  _ADPARAMETEROPERATION.fields_by_name['remove'])
_ADPARAMETEROPERATION.fields_by_name['remove'].containing_oneof = _ADPARAMETEROPERATION.oneofs_by_name['operation']
_MUTATEADPARAMETERSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATEADPARAMETERSRESPONSE.fields_by_name['results'].message_type = _MUTATEADPARAMETERRESULT
DESCRIPTOR.message_types_by_name['GetAdParameterRequest'] = _GETADPARAMETERREQUEST
DESCRIPTOR.message_types_by_name['MutateAdParametersRequest'] = _MUTATEADPARAMETERSREQUEST
DESCRIPTOR.message_types_by_name['AdParameterOperation'] = _ADPARAMETEROPERATION
DESCRIPTOR.message_types_by_name['MutateAdParametersResponse'] = _MUTATEADPARAMETERSRESPONSE
DESCRIPTOR.message_types_by_name['MutateAdParameterResult'] = _MUTATEADPARAMETERRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAdParameterRequest = _reflection.GeneratedProtocolMessageType('GetAdParameterRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETADPARAMETERREQUEST,
  __module__ = 'google.ads.googleads_v4.proto.services.ad_parameter_service_pb2'
  ,
  __doc__ = """Request message for
  [AdParameterService.GetAdParameter][google.ads.googleads.v4.services.AdParameterService.GetAdParameter]
  
  
  Attributes:
      resource_name:
          Required. The resource name of the ad parameter to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.GetAdParameterRequest)
  ))
_sym_db.RegisterMessage(GetAdParameterRequest)

MutateAdParametersRequest = _reflection.GeneratedProtocolMessageType('MutateAdParametersRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEADPARAMETERSREQUEST,
  __module__ = 'google.ads.googleads_v4.proto.services.ad_parameter_service_pb2'
  ,
  __doc__ = """Request message for
  [AdParameterService.MutateAdParameters][google.ads.googleads.v4.services.AdParameterService.MutateAdParameters]
  
  
  Attributes:
      customer_id:
          Required. The ID of the customer whose ad parameters are being
          modified.
      operations:
          Required. The list of operations to perform on individual ad
          parameters.
      partial_failure:
          If true, successful operations will be carried out and invalid
          operations will return errors. If false, all operations will
          be carried out in one transaction if and only if they are all
          valid. Default is false.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.MutateAdParametersRequest)
  ))
_sym_db.RegisterMessage(MutateAdParametersRequest)

AdParameterOperation = _reflection.GeneratedProtocolMessageType('AdParameterOperation', (_message.Message,), dict(
  DESCRIPTOR = _ADPARAMETEROPERATION,
  __module__ = 'google.ads.googleads_v4.proto.services.ad_parameter_service_pb2'
  ,
  __doc__ = """A single operation (create, update, remove) on ad parameter.
  
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new ad
          parameter.
      update:
          Update operation: The ad parameter is expected to have a valid
          resource name.
      remove:
          Remove operation: A resource name for the ad parameter to
          remove is expected in this format:  ``customers/{customer_id}/
          adParameters/{ad_group_id}~{criterion_id}~{parameter_index}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.AdParameterOperation)
  ))
_sym_db.RegisterMessage(AdParameterOperation)

MutateAdParametersResponse = _reflection.GeneratedProtocolMessageType('MutateAdParametersResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEADPARAMETERSRESPONSE,
  __module__ = 'google.ads.googleads_v4.proto.services.ad_parameter_service_pb2'
  ,
  __doc__ = """Response message for an ad parameter mutate.
  
  
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
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.MutateAdParametersResponse)
  ))
_sym_db.RegisterMessage(MutateAdParametersResponse)

MutateAdParameterResult = _reflection.GeneratedProtocolMessageType('MutateAdParameterResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEADPARAMETERRESULT,
  __module__ = 'google.ads.googleads_v4.proto.services.ad_parameter_service_pb2'
  ,
  __doc__ = """The result for the ad parameter mutate.
  
  
  Attributes:
      resource_name:
          The resource name returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.MutateAdParameterResult)
  ))
_sym_db.RegisterMessage(MutateAdParameterResult)


DESCRIPTOR._options = None
_GETADPARAMETERREQUEST.fields_by_name['resource_name']._options = None
_MUTATEADPARAMETERSREQUEST.fields_by_name['customer_id']._options = None
_MUTATEADPARAMETERSREQUEST.fields_by_name['operations']._options = None

_ADPARAMETERSERVICE = _descriptor.ServiceDescriptor(
  name='AdParameterService',
  full_name='google.ads.googleads.v4.services.AdParameterService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312A\030googleads.googleapis.com'),
  serialized_start=1062,
  serialized_end=1540,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAdParameter',
    full_name='google.ads.googleads.v4.services.AdParameterService.GetAdParameter',
    index=0,
    containing_service=None,
    input_type=_GETADPARAMETERREQUEST,
    output_type=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__parameter__pb2._ADPARAMETER,
    serialized_options=_b('\202\323\344\223\0020\022./v4/{resource_name=customers/*/adParameters/*}\332A\rresource_name'),
  ),
  _descriptor.MethodDescriptor(
    name='MutateAdParameters',
    full_name='google.ads.googleads.v4.services.AdParameterService.MutateAdParameters',
    index=1,
    containing_service=None,
    input_type=_MUTATEADPARAMETERSREQUEST,
    output_type=_MUTATEADPARAMETERSRESPONSE,
    serialized_options=_b('\202\323\344\223\0026\"1/v4/customers/{customer_id=*}/adParameters:mutate:\001*\332A\026customer_id,operations'),
  ),
])
_sym_db.RegisterServiceDescriptor(_ADPARAMETERSERVICE)

DESCRIPTOR.services_by_name['AdParameterService'] = _ADPARAMETERSERVICE

# @@protoc_insertion_point(module_scope)
