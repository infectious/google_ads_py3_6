# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/services/campaign_draft_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v5.proto.enums import response_content_type_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_response__content__type__pb2
from google.ads.google_ads.v5.proto.resources import campaign_draft_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_campaign__draft__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/services/campaign_draft_service.proto',
  package='google.ads.googleads.v5.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v5.servicesB\031CampaignDraftServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v5/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V5.Services\312\002 Google\\Ads\\GoogleAds\\V5\\Services\352\002$Google::Ads::GoogleAds::V5::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nCgoogle/ads/googleads_v5/proto/services/campaign_draft_service.proto\x12 google.ads.googleads.v5.services\x1a?google/ads/googleads_v5/proto/enums/response_content_type.proto\x1a<google/ads/googleads_v5/proto/resources/campaign_draft.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\"`\n\x17GetCampaignDraftRequest\x12\x45\n\rresource_name\x18\x01 \x01(\tB.\xe0\x41\x02\xfa\x41(\n&googleads.googleapis.com/CampaignDraft\"\xa5\x02\n\x1bMutateCampaignDraftsRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12Q\n\noperations\x18\x02 \x03(\x0b\x32\x38.google.ads.googleads.v5.services.CampaignDraftOperationB\x03\xe0\x41\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12i\n\x15response_content_type\x18\x05 \x01(\x0e\x32J.google.ads.googleads.v5.enums.ResponseContentTypeEnum.ResponseContentType\":\n\x1bPromoteCampaignDraftRequest\x12\x1b\n\x0e\x63\x61mpaign_draft\x18\x01 \x01(\tB\x03\xe0\x41\x02\"\xf0\x01\n\x16\x43\x61mpaignDraftOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x42\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x30.google.ads.googleads.v5.resources.CampaignDraftH\x00\x12\x42\n\x06update\x18\x02 \x01(\x0b\x32\x30.google.ads.googleads.v5.resources.CampaignDraftH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\x9f\x01\n\x1cMutateCampaignDraftsResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12L\n\x07results\x18\x02 \x03(\x0b\x32;.google.ads.googleads.v5.services.MutateCampaignDraftResult\"|\n\x19MutateCampaignDraftResult\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12H\n\x0e\x63\x61mpaign_draft\x18\x02 \x01(\x0b\x32\x30.google.ads.googleads.v5.resources.CampaignDraft\"\x93\x01\n#ListCampaignDraftAsyncErrorsRequest\x12\x45\n\rresource_name\x18\x01 \x01(\tB.\xe0\x41\x02\xfa\x41(\n&googleads.googleapis.com/CampaignDraft\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\"c\n$ListCampaignDraftAsyncErrorsResponse\x12\"\n\x06\x65rrors\x18\x01 \x03(\x0b\x32\x12.google.rpc.Status\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xfa\x07\n\x14\x43\x61mpaignDraftService\x12\xc9\x01\n\x10GetCampaignDraft\x12\x39.google.ads.googleads.v5.services.GetCampaignDraftRequest\x1a\x30.google.ads.googleads.v5.resources.CampaignDraft\"H\x82\xd3\xe4\x93\x02\x32\x12\x30/v5/{resource_name=customers/*/campaignDrafts/*}\xda\x41\rresource_name\x12\xee\x01\n\x14MutateCampaignDrafts\x12=.google.ads.googleads.v5.services.MutateCampaignDraftsRequest\x1a>.google.ads.googleads.v5.services.MutateCampaignDraftsResponse\"W\x82\xd3\xe4\x93\x02\x38\"3/v5/customers/{customer_id=*}/campaignDrafts:mutate:\x01*\xda\x41\x16\x63ustomer_id,operations\x12\xfd\x01\n\x14PromoteCampaignDraft\x12=.google.ads.googleads.v5.services.PromoteCampaignDraftRequest\x1a\x1d.google.longrunning.Operation\"\x86\x01\x82\xd3\xe4\x93\x02>\"9/v5/{campaign_draft=customers/*/campaignDrafts/*}:promote:\x01*\xda\x41\x0e\x63\x61mpaign_draft\xca\x41.\n\x15google.protobuf.Empty\x12\x15google.protobuf.Empty\x12\x87\x02\n\x1cListCampaignDraftAsyncErrors\x12\x45.google.ads.googleads.v5.services.ListCampaignDraftAsyncErrorsRequest\x1a\x46.google.ads.googleads.v5.services.ListCampaignDraftAsyncErrorsResponse\"X\x82\xd3\xe4\x93\x02\x42\x12@/v5/{resource_name=customers/*/campaignDrafts/*}:listAsyncErrors\xda\x41\rresource_name\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x80\x02\n$com.google.ads.googleads.v5.servicesB\x19\x43\x61mpaignDraftServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v5/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V5.Services\xca\x02 Google\\Ads\\GoogleAds\\V5\\Services\xea\x02$Google::Ads::GoogleAds::V5::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_response__content__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_campaign__draft__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_longrunning_dot_operations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETCAMPAIGNDRAFTREQUEST = _descriptor.Descriptor(
  name='GetCampaignDraftRequest',
  full_name='google.ads.googleads.v5.services.GetCampaignDraftRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v5.services.GetCampaignDraftRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A(\n&googleads.googleapis.com/CampaignDraft', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=443,
  serialized_end=539,
)


_MUTATECAMPAIGNDRAFTSREQUEST = _descriptor.Descriptor(
  name='MutateCampaignDraftsRequest',
  full_name='google.ads.googleads.v5.services.MutateCampaignDraftsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v5.services.MutateCampaignDraftsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v5.services.MutateCampaignDraftsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v5.services.MutateCampaignDraftsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v5.services.MutateCampaignDraftsRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_content_type', full_name='google.ads.googleads.v5.services.MutateCampaignDraftsRequest.response_content_type', index=4,
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
  serialized_start=542,
  serialized_end=835,
)


_PROMOTECAMPAIGNDRAFTREQUEST = _descriptor.Descriptor(
  name='PromoteCampaignDraftRequest',
  full_name='google.ads.googleads.v5.services.PromoteCampaignDraftRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='campaign_draft', full_name='google.ads.googleads.v5.services.PromoteCampaignDraftRequest.campaign_draft', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=837,
  serialized_end=895,
)


_CAMPAIGNDRAFTOPERATION = _descriptor.Descriptor(
  name='CampaignDraftOperation',
  full_name='google.ads.googleads.v5.services.CampaignDraftOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v5.services.CampaignDraftOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v5.services.CampaignDraftOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v5.services.CampaignDraftOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v5.services.CampaignDraftOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
      name='operation', full_name='google.ads.googleads.v5.services.CampaignDraftOperation.operation',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=898,
  serialized_end=1138,
)


_MUTATECAMPAIGNDRAFTSRESPONSE = _descriptor.Descriptor(
  name='MutateCampaignDraftsResponse',
  full_name='google.ads.googleads.v5.services.MutateCampaignDraftsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v5.services.MutateCampaignDraftsResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v5.services.MutateCampaignDraftsResponse.results', index=1,
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
  serialized_start=1141,
  serialized_end=1300,
)


_MUTATECAMPAIGNDRAFTRESULT = _descriptor.Descriptor(
  name='MutateCampaignDraftResult',
  full_name='google.ads.googleads.v5.services.MutateCampaignDraftResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v5.services.MutateCampaignDraftResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign_draft', full_name='google.ads.googleads.v5.services.MutateCampaignDraftResult.campaign_draft', index=1,
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
  serialized_start=1302,
  serialized_end=1426,
)


_LISTCAMPAIGNDRAFTASYNCERRORSREQUEST = _descriptor.Descriptor(
  name='ListCampaignDraftAsyncErrorsRequest',
  full_name='google.ads.googleads.v5.services.ListCampaignDraftAsyncErrorsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v5.services.ListCampaignDraftAsyncErrorsRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A(\n&googleads.googleapis.com/CampaignDraft', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.ads.googleads.v5.services.ListCampaignDraftAsyncErrorsRequest.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.ads.googleads.v5.services.ListCampaignDraftAsyncErrorsRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=1429,
  serialized_end=1576,
)


_LISTCAMPAIGNDRAFTASYNCERRORSRESPONSE = _descriptor.Descriptor(
  name='ListCampaignDraftAsyncErrorsResponse',
  full_name='google.ads.googleads.v5.services.ListCampaignDraftAsyncErrorsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='errors', full_name='google.ads.googleads.v5.services.ListCampaignDraftAsyncErrorsResponse.errors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.ads.googleads.v5.services.ListCampaignDraftAsyncErrorsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1578,
  serialized_end=1677,
)

_MUTATECAMPAIGNDRAFTSREQUEST.fields_by_name['operations'].message_type = _CAMPAIGNDRAFTOPERATION
_MUTATECAMPAIGNDRAFTSREQUEST.fields_by_name['response_content_type'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_response__content__type__pb2._RESPONSECONTENTTYPEENUM_RESPONSECONTENTTYPE
_CAMPAIGNDRAFTOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_CAMPAIGNDRAFTOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_campaign__draft__pb2._CAMPAIGNDRAFT
_CAMPAIGNDRAFTOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_campaign__draft__pb2._CAMPAIGNDRAFT
_CAMPAIGNDRAFTOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNDRAFTOPERATION.fields_by_name['create'])
_CAMPAIGNDRAFTOPERATION.fields_by_name['create'].containing_oneof = _CAMPAIGNDRAFTOPERATION.oneofs_by_name['operation']
_CAMPAIGNDRAFTOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNDRAFTOPERATION.fields_by_name['update'])
_CAMPAIGNDRAFTOPERATION.fields_by_name['update'].containing_oneof = _CAMPAIGNDRAFTOPERATION.oneofs_by_name['operation']
_CAMPAIGNDRAFTOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNDRAFTOPERATION.fields_by_name['remove'])
_CAMPAIGNDRAFTOPERATION.fields_by_name['remove'].containing_oneof = _CAMPAIGNDRAFTOPERATION.oneofs_by_name['operation']
_MUTATECAMPAIGNDRAFTSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATECAMPAIGNDRAFTSRESPONSE.fields_by_name['results'].message_type = _MUTATECAMPAIGNDRAFTRESULT
_MUTATECAMPAIGNDRAFTRESULT.fields_by_name['campaign_draft'].message_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_campaign__draft__pb2._CAMPAIGNDRAFT
_LISTCAMPAIGNDRAFTASYNCERRORSRESPONSE.fields_by_name['errors'].message_type = google_dot_rpc_dot_status__pb2._STATUS
DESCRIPTOR.message_types_by_name['GetCampaignDraftRequest'] = _GETCAMPAIGNDRAFTREQUEST
DESCRIPTOR.message_types_by_name['MutateCampaignDraftsRequest'] = _MUTATECAMPAIGNDRAFTSREQUEST
DESCRIPTOR.message_types_by_name['PromoteCampaignDraftRequest'] = _PROMOTECAMPAIGNDRAFTREQUEST
DESCRIPTOR.message_types_by_name['CampaignDraftOperation'] = _CAMPAIGNDRAFTOPERATION
DESCRIPTOR.message_types_by_name['MutateCampaignDraftsResponse'] = _MUTATECAMPAIGNDRAFTSRESPONSE
DESCRIPTOR.message_types_by_name['MutateCampaignDraftResult'] = _MUTATECAMPAIGNDRAFTRESULT
DESCRIPTOR.message_types_by_name['ListCampaignDraftAsyncErrorsRequest'] = _LISTCAMPAIGNDRAFTASYNCERRORSREQUEST
DESCRIPTOR.message_types_by_name['ListCampaignDraftAsyncErrorsResponse'] = _LISTCAMPAIGNDRAFTASYNCERRORSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCampaignDraftRequest = _reflection.GeneratedProtocolMessageType('GetCampaignDraftRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCAMPAIGNDRAFTREQUEST,
  '__module__' : 'google.ads.googleads_v5.proto.services.campaign_draft_service_pb2'
  ,
  '__doc__': """Request message for [CampaignDraftService.GetCampaignDraft][google.ads
  .googleads.v5.services.CampaignDraftService.GetCampaignDraft].
  
  Attributes:
      resource_name:
          Required. The resource name of the campaign draft to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.GetCampaignDraftRequest)
  })
_sym_db.RegisterMessage(GetCampaignDraftRequest)

MutateCampaignDraftsRequest = _reflection.GeneratedProtocolMessageType('MutateCampaignDraftsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNDRAFTSREQUEST,
  '__module__' : 'google.ads.googleads_v5.proto.services.campaign_draft_service_pb2'
  ,
  '__doc__': """Request message for [CampaignDraftService.MutateCampaignDrafts][google
  .ads.googleads.v5.services.CampaignDraftService.MutateCampaignDrafts].
  
  Attributes:
      customer_id:
          Required. The ID of the customer whose campaign drafts are
          being modified.
      operations:
          Required. The list of operations to perform on individual
          campaign drafts.
      partial_failure:
          If true, successful operations will be carried out and invalid
          operations will return errors. If false, all operations will
          be carried out in one transaction if and only if they are all
          valid. Default is false.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
      response_content_type:
          The response content type setting. Determines whether the
          mutable resource or just the resource name should be returned
          post mutation.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.MutateCampaignDraftsRequest)
  })
_sym_db.RegisterMessage(MutateCampaignDraftsRequest)

PromoteCampaignDraftRequest = _reflection.GeneratedProtocolMessageType('PromoteCampaignDraftRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROMOTECAMPAIGNDRAFTREQUEST,
  '__module__' : 'google.ads.googleads_v5.proto.services.campaign_draft_service_pb2'
  ,
  '__doc__': """Request message for [CampaignDraftService.PromoteCampaignDraft][google
  .ads.googleads.v5.services.CampaignDraftService.PromoteCampaignDraft].
  
  Attributes:
      campaign_draft:
          Required. The resource name of the campaign draft to promote.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.PromoteCampaignDraftRequest)
  })
_sym_db.RegisterMessage(PromoteCampaignDraftRequest)

CampaignDraftOperation = _reflection.GeneratedProtocolMessageType('CampaignDraftOperation', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNDRAFTOPERATION,
  '__module__' : 'google.ads.googleads_v5.proto.services.campaign_draft_service_pb2'
  ,
  '__doc__': """A single operation (create, update, remove) on a campaign draft.
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          campaign draft.
      update:
          Update operation: The campaign draft is expected to have a
          valid resource name.
      remove:
          Remove operation: The campaign draft is expected to have a
          valid resource name, in this format:  ``customers/{customer_id
          }/campaignDrafts/{base_campaign_id}~{draft_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.CampaignDraftOperation)
  })
_sym_db.RegisterMessage(CampaignDraftOperation)

MutateCampaignDraftsResponse = _reflection.GeneratedProtocolMessageType('MutateCampaignDraftsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNDRAFTSRESPONSE,
  '__module__' : 'google.ads.googleads_v5.proto.services.campaign_draft_service_pb2'
  ,
  '__doc__': """Response message for campaign draft mutate.
  
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
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.MutateCampaignDraftsResponse)
  })
_sym_db.RegisterMessage(MutateCampaignDraftsResponse)

MutateCampaignDraftResult = _reflection.GeneratedProtocolMessageType('MutateCampaignDraftResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNDRAFTRESULT,
  '__module__' : 'google.ads.googleads_v5.proto.services.campaign_draft_service_pb2'
  ,
  '__doc__': """The result for the campaign draft mutate.
  
  Attributes:
      resource_name:
          Returned for successful operations.
      campaign_draft:
          The mutated campaign draft with only mutable fields after
          mutate. The field will only be returned when
          response\_content\_type is set to "MUTABLE\_RESOURCE".
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.MutateCampaignDraftResult)
  })
_sym_db.RegisterMessage(MutateCampaignDraftResult)

ListCampaignDraftAsyncErrorsRequest = _reflection.GeneratedProtocolMessageType('ListCampaignDraftAsyncErrorsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCAMPAIGNDRAFTASYNCERRORSREQUEST,
  '__module__' : 'google.ads.googleads_v5.proto.services.campaign_draft_service_pb2'
  ,
  '__doc__': """Request message for [CampaignDraftService.ListCampaignDraftAsyncErrors
  ][google.ads.googleads.v5.services.CampaignDraftService.ListCampaignDr
  aftAsyncErrors].
  
  Attributes:
      resource_name:
          Required. The name of the campaign draft from which to
          retrieve the async errors.
      page_token:
          Token of the page to retrieve. If not specified, the first
          page of results will be returned. Use the value obtained from
          ``next_page_token`` in the previous response in order to
          request the next page of results.
      page_size:
          Number of elements to retrieve in a single page. When a page
          request is too large, the server may decide to further limit
          the number of returned resources.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.ListCampaignDraftAsyncErrorsRequest)
  })
_sym_db.RegisterMessage(ListCampaignDraftAsyncErrorsRequest)

ListCampaignDraftAsyncErrorsResponse = _reflection.GeneratedProtocolMessageType('ListCampaignDraftAsyncErrorsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCAMPAIGNDRAFTASYNCERRORSRESPONSE,
  '__module__' : 'google.ads.googleads_v5.proto.services.campaign_draft_service_pb2'
  ,
  '__doc__': """Response message for [CampaignDraftService.ListCampaignDraftAsyncError
  s][google.ads.googleads.v5.services.CampaignDraftService.ListCampaignD
  raftAsyncErrors].
  
  Attributes:
      errors:
          Details of the errors when performing the asynchronous
          operation.
      next_page_token:
          Pagination token used to retrieve the next page of results.
          Pass the content of this string as the ``page_token``
          attribute of the next request. ``next_page_token`` is not
          returned for the last page.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.ListCampaignDraftAsyncErrorsResponse)
  })
_sym_db.RegisterMessage(ListCampaignDraftAsyncErrorsResponse)


DESCRIPTOR._options = None
_GETCAMPAIGNDRAFTREQUEST.fields_by_name['resource_name']._options = None
_MUTATECAMPAIGNDRAFTSREQUEST.fields_by_name['customer_id']._options = None
_MUTATECAMPAIGNDRAFTSREQUEST.fields_by_name['operations']._options = None
_PROMOTECAMPAIGNDRAFTREQUEST.fields_by_name['campaign_draft']._options = None
_LISTCAMPAIGNDRAFTASYNCERRORSREQUEST.fields_by_name['resource_name']._options = None

_CAMPAIGNDRAFTSERVICE = _descriptor.ServiceDescriptor(
  name='CampaignDraftService',
  full_name='google.ads.googleads.v5.services.CampaignDraftService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  create_key=_descriptor._internal_create_key,
  serialized_start=1680,
  serialized_end=2698,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCampaignDraft',
    full_name='google.ads.googleads.v5.services.CampaignDraftService.GetCampaignDraft',
    index=0,
    containing_service=None,
    input_type=_GETCAMPAIGNDRAFTREQUEST,
    output_type=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_campaign__draft__pb2._CAMPAIGNDRAFT,
    serialized_options=b'\202\323\344\223\0022\0220/v5/{resource_name=customers/*/campaignDrafts/*}\332A\rresource_name',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MutateCampaignDrafts',
    full_name='google.ads.googleads.v5.services.CampaignDraftService.MutateCampaignDrafts',
    index=1,
    containing_service=None,
    input_type=_MUTATECAMPAIGNDRAFTSREQUEST,
    output_type=_MUTATECAMPAIGNDRAFTSRESPONSE,
    serialized_options=b'\202\323\344\223\0028\"3/v5/customers/{customer_id=*}/campaignDrafts:mutate:\001*\332A\026customer_id,operations',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PromoteCampaignDraft',
    full_name='google.ads.googleads.v5.services.CampaignDraftService.PromoteCampaignDraft',
    index=2,
    containing_service=None,
    input_type=_PROMOTECAMPAIGNDRAFTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002>\"9/v5/{campaign_draft=customers/*/campaignDrafts/*}:promote:\001*\332A\016campaign_draft\312A.\n\025google.protobuf.Empty\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListCampaignDraftAsyncErrors',
    full_name='google.ads.googleads.v5.services.CampaignDraftService.ListCampaignDraftAsyncErrors',
    index=3,
    containing_service=None,
    input_type=_LISTCAMPAIGNDRAFTASYNCERRORSREQUEST,
    output_type=_LISTCAMPAIGNDRAFTASYNCERRORSRESPONSE,
    serialized_options=b'\202\323\344\223\002B\022@/v5/{resource_name=customers/*/campaignDrafts/*}:listAsyncErrors\332A\rresource_name',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CAMPAIGNDRAFTSERVICE)

DESCRIPTOR.services_by_name['CampaignDraftService'] = _CAMPAIGNDRAFTSERVICE

# @@protoc_insertion_point(module_scope)
