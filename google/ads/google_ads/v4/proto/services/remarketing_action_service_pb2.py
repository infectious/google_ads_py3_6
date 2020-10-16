# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/services/remarketing_action_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v4.proto.resources import remarketing_action_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_remarketing__action__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v4/proto/services/remarketing_action_service.proto',
  package='google.ads.googleads.v4.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v4.servicesB\035RemarketingActionServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v4/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V4.Services\312\002 Google\\Ads\\GoogleAds\\V4\\Services\352\002$Google::Ads::GoogleAds::V4::Services'),
  serialized_pb=_b('\nGgoogle/ads/googleads_v4/proto/services/remarketing_action_service.proto\x12 google.ads.googleads.v4.services\x1a@google/ads/googleads_v4/proto/resources/remarketing_action.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\"h\n\x1bGetRemarketingActionRequest\x12I\n\rresource_name\x18\x01 \x01(\tB2\xe0\x41\x02\xfa\x41,\n*googleads.googleapis.com/RemarketingAction\"\xc2\x01\n\x1fMutateRemarketingActionsRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12U\n\noperations\x18\x02 \x03(\x0b\x32<.google.ads.googleads.v4.services.RemarketingActionOperationB\x03\xe0\x41\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\xea\x01\n\x1aRemarketingActionOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x46\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x34.google.ads.googleads.v4.resources.RemarketingActionH\x00\x12\x46\n\x06update\x18\x02 \x01(\x0b\x32\x34.google.ads.googleads.v4.resources.RemarketingActionH\x00\x42\x0b\n\toperation\"\xa7\x01\n MutateRemarketingActionsResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12P\n\x07results\x18\x02 \x03(\x0b\x32?.google.ads.googleads.v4.services.MutateRemarketingActionResult\"6\n\x1dMutateRemarketingActionResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\x94\x04\n\x18RemarketingActionService\x12\xd9\x01\n\x14GetRemarketingAction\x12=.google.ads.googleads.v4.services.GetRemarketingActionRequest\x1a\x34.google.ads.googleads.v4.resources.RemarketingAction\"L\x82\xd3\xe4\x93\x02\x36\x12\x34/v4/{resource_name=customers/*/remarketingActions/*}\xda\x41\rresource_name\x12\xfe\x01\n\x18MutateRemarketingActions\x12\x41.google.ads.googleads.v4.services.MutateRemarketingActionsRequest\x1a\x42.google.ads.googleads.v4.services.MutateRemarketingActionsResponse\"[\x82\xd3\xe4\x93\x02<\"7/v4/customers/{customer_id=*}/remarketingActions:mutate:\x01*\xda\x41\x16\x63ustomer_id,operations\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x84\x02\n$com.google.ads.googleads.v4.servicesB\x1dRemarketingActionServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v4/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V4.Services\xca\x02 Google\\Ads\\GoogleAds\\V4\\Services\xea\x02$Google::Ads::GoogleAds::V4::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_remarketing__action__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETREMARKETINGACTIONREQUEST = _descriptor.Descriptor(
  name='GetRemarketingActionRequest',
  full_name='google.ads.googleads.v4.services.GetRemarketingActionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.services.GetRemarketingActionRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002\372A,\n*googleads.googleapis.com/RemarketingAction'), file=DESCRIPTOR),
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
  serialized_start=349,
  serialized_end=453,
)


_MUTATEREMARKETINGACTIONSREQUEST = _descriptor.Descriptor(
  name='MutateRemarketingActionsRequest',
  full_name='google.ads.googleads.v4.services.MutateRemarketingActionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v4.services.MutateRemarketingActionsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v4.services.MutateRemarketingActionsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v4.services.MutateRemarketingActionsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v4.services.MutateRemarketingActionsRequest.validate_only', index=3,
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
  serialized_start=456,
  serialized_end=650,
)


_REMARKETINGACTIONOPERATION = _descriptor.Descriptor(
  name='RemarketingActionOperation',
  full_name='google.ads.googleads.v4.services.RemarketingActionOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v4.services.RemarketingActionOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v4.services.RemarketingActionOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v4.services.RemarketingActionOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
      name='operation', full_name='google.ads.googleads.v4.services.RemarketingActionOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=653,
  serialized_end=887,
)


_MUTATEREMARKETINGACTIONSRESPONSE = _descriptor.Descriptor(
  name='MutateRemarketingActionsResponse',
  full_name='google.ads.googleads.v4.services.MutateRemarketingActionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v4.services.MutateRemarketingActionsResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v4.services.MutateRemarketingActionsResponse.results', index=1,
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
  serialized_start=890,
  serialized_end=1057,
)


_MUTATEREMARKETINGACTIONRESULT = _descriptor.Descriptor(
  name='MutateRemarketingActionResult',
  full_name='google.ads.googleads.v4.services.MutateRemarketingActionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.services.MutateRemarketingActionResult.resource_name', index=0,
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
  serialized_start=1059,
  serialized_end=1113,
)

_MUTATEREMARKETINGACTIONSREQUEST.fields_by_name['operations'].message_type = _REMARKETINGACTIONOPERATION
_REMARKETINGACTIONOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_REMARKETINGACTIONOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_remarketing__action__pb2._REMARKETINGACTION
_REMARKETINGACTIONOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_remarketing__action__pb2._REMARKETINGACTION
_REMARKETINGACTIONOPERATION.oneofs_by_name['operation'].fields.append(
  _REMARKETINGACTIONOPERATION.fields_by_name['create'])
_REMARKETINGACTIONOPERATION.fields_by_name['create'].containing_oneof = _REMARKETINGACTIONOPERATION.oneofs_by_name['operation']
_REMARKETINGACTIONOPERATION.oneofs_by_name['operation'].fields.append(
  _REMARKETINGACTIONOPERATION.fields_by_name['update'])
_REMARKETINGACTIONOPERATION.fields_by_name['update'].containing_oneof = _REMARKETINGACTIONOPERATION.oneofs_by_name['operation']
_MUTATEREMARKETINGACTIONSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATEREMARKETINGACTIONSRESPONSE.fields_by_name['results'].message_type = _MUTATEREMARKETINGACTIONRESULT
DESCRIPTOR.message_types_by_name['GetRemarketingActionRequest'] = _GETREMARKETINGACTIONREQUEST
DESCRIPTOR.message_types_by_name['MutateRemarketingActionsRequest'] = _MUTATEREMARKETINGACTIONSREQUEST
DESCRIPTOR.message_types_by_name['RemarketingActionOperation'] = _REMARKETINGACTIONOPERATION
DESCRIPTOR.message_types_by_name['MutateRemarketingActionsResponse'] = _MUTATEREMARKETINGACTIONSRESPONSE
DESCRIPTOR.message_types_by_name['MutateRemarketingActionResult'] = _MUTATEREMARKETINGACTIONRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetRemarketingActionRequest = _reflection.GeneratedProtocolMessageType('GetRemarketingActionRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREMARKETINGACTIONREQUEST,
  __module__ = 'google.ads.googleads_v4.proto.services.remarketing_action_service_pb2'
  ,
  __doc__ = """Request message for
  [RemarketingActionService.GetRemarketingAction][google.ads.googleads.v4.services.RemarketingActionService.GetRemarketingAction].
  
  
  Attributes:
      resource_name:
          Required. The resource name of the remarketing action to
          fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.GetRemarketingActionRequest)
  ))
_sym_db.RegisterMessage(GetRemarketingActionRequest)

MutateRemarketingActionsRequest = _reflection.GeneratedProtocolMessageType('MutateRemarketingActionsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEREMARKETINGACTIONSREQUEST,
  __module__ = 'google.ads.googleads_v4.proto.services.remarketing_action_service_pb2'
  ,
  __doc__ = """Request message for
  [RemarketingActionService.MutateRemarketingActions][google.ads.googleads.v4.services.RemarketingActionService.MutateRemarketingActions].
  
  
  Attributes:
      customer_id:
          Required. The ID of the customer whose remarketing actions are
          being modified.
      operations:
          Required. The list of operations to perform on individual
          remarketing actions.
      partial_failure:
          If true, successful operations will be carried out and invalid
          operations will return errors. If false, all operations will
          be carried out in one transaction if and only if they are all
          valid. Default is false.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.MutateRemarketingActionsRequest)
  ))
_sym_db.RegisterMessage(MutateRemarketingActionsRequest)

RemarketingActionOperation = _reflection.GeneratedProtocolMessageType('RemarketingActionOperation', (_message.Message,), dict(
  DESCRIPTOR = _REMARKETINGACTIONOPERATION,
  __module__ = 'google.ads.googleads_v4.proto.services.remarketing_action_service_pb2'
  ,
  __doc__ = """A single operation (create, update) on a remarketing action.
  
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          remarketing action.
      update:
          Update operation: The remarketing action is expected to have a
          valid resource name.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.RemarketingActionOperation)
  ))
_sym_db.RegisterMessage(RemarketingActionOperation)

MutateRemarketingActionsResponse = _reflection.GeneratedProtocolMessageType('MutateRemarketingActionsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEREMARKETINGACTIONSRESPONSE,
  __module__ = 'google.ads.googleads_v4.proto.services.remarketing_action_service_pb2'
  ,
  __doc__ = """Response message for remarketing action mutate.
  
  
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
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.MutateRemarketingActionsResponse)
  ))
_sym_db.RegisterMessage(MutateRemarketingActionsResponse)

MutateRemarketingActionResult = _reflection.GeneratedProtocolMessageType('MutateRemarketingActionResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEREMARKETINGACTIONRESULT,
  __module__ = 'google.ads.googleads_v4.proto.services.remarketing_action_service_pb2'
  ,
  __doc__ = """The result for the remarketing action mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.MutateRemarketingActionResult)
  ))
_sym_db.RegisterMessage(MutateRemarketingActionResult)


DESCRIPTOR._options = None
_GETREMARKETINGACTIONREQUEST.fields_by_name['resource_name']._options = None
_MUTATEREMARKETINGACTIONSREQUEST.fields_by_name['customer_id']._options = None
_MUTATEREMARKETINGACTIONSREQUEST.fields_by_name['operations']._options = None

_REMARKETINGACTIONSERVICE = _descriptor.ServiceDescriptor(
  name='RemarketingActionService',
  full_name='google.ads.googleads.v4.services.RemarketingActionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312A\030googleads.googleapis.com'),
  serialized_start=1116,
  serialized_end=1648,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRemarketingAction',
    full_name='google.ads.googleads.v4.services.RemarketingActionService.GetRemarketingAction',
    index=0,
    containing_service=None,
    input_type=_GETREMARKETINGACTIONREQUEST,
    output_type=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_remarketing__action__pb2._REMARKETINGACTION,
    serialized_options=_b('\202\323\344\223\0026\0224/v4/{resource_name=customers/*/remarketingActions/*}\332A\rresource_name'),
  ),
  _descriptor.MethodDescriptor(
    name='MutateRemarketingActions',
    full_name='google.ads.googleads.v4.services.RemarketingActionService.MutateRemarketingActions',
    index=1,
    containing_service=None,
    input_type=_MUTATEREMARKETINGACTIONSREQUEST,
    output_type=_MUTATEREMARKETINGACTIONSRESPONSE,
    serialized_options=_b('\202\323\344\223\002<\"7/v4/customers/{customer_id=*}/remarketingActions:mutate:\001*\332A\026customer_id,operations'),
  ),
])
_sym_db.RegisterServiceDescriptor(_REMARKETINGACTIONSERVICE)

DESCRIPTOR.services_by_name['RemarketingActionService'] = _REMARKETINGACTIONSERVICE

# @@protoc_insertion_point(module_scope)
