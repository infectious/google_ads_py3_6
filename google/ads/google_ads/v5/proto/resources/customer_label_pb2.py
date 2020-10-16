# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/resources/customer_label.proto

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
  name='google/ads/googleads_v5/proto/resources/customer_label.proto',
  package='google.ads.googleads.v5.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v5.resourcesB\022CustomerLabelProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v5/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V5.Resources\312\002!Google\\Ads\\GoogleAds\\V5\\Resources\352\002%Google::Ads::GoogleAds::V5::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n<google/ads/googleads_v5/proto/resources/customer_label.proto\x12!google.ads.googleads.v5.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xa0\x02\n\rCustomerLabel\x12\x45\n\rresource_name\x18\x01 \x01(\tB.\xe0\x41\x05\xfa\x41(\n&googleads.googleapis.com/CustomerLabel\x12\x33\n\x08\x63ustomer\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x03\xe0\x41\x03\x12\x30\n\x05label\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x03\xe0\x41\x03:a\xea\x41^\n&googleads.googleapis.com/CustomerLabel\x12\x34\x63ustomers/{customer}/customerLabels/{customer_label}B\xff\x01\n%com.google.ads.googleads.v5.resourcesB\x12\x43ustomerLabelProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v5/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V5.Resources\xca\x02!Google\\Ads\\GoogleAds\\V5\\Resources\xea\x02%Google::Ads::GoogleAds::V5::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CUSTOMERLABEL = _descriptor.Descriptor(
  name='CustomerLabel',
  full_name='google.ads.googleads.v5.resources.CustomerLabel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v5.resources.CustomerLabel.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A(\n&googleads.googleapis.com/CustomerLabel', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='customer', full_name='google.ads.googleads.v5.resources.CustomerLabel.customer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='google.ads.googleads.v5.resources.CustomerLabel.label', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A^\n&googleads.googleapis.com/CustomerLabel\0224customers/{customer}/customerLabels/{customer_label}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=510,
)

_CUSTOMERLABEL.fields_by_name['customer'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CUSTOMERLABEL.fields_by_name['label'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['CustomerLabel'] = _CUSTOMERLABEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomerLabel = _reflection.GeneratedProtocolMessageType('CustomerLabel', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERLABEL,
  '__module__' : 'google.ads.googleads_v5.proto.resources.customer_label_pb2'
  ,
  '__doc__': """Represents a relationship between a customer and a label. This
  customer may not have access to all the labels attached to it.
  Additional CustomerLabels may be returned by increasing permissions
  with login-customer-id.
  
  Attributes:
      resource_name:
          Immutable. Name of the resource. Customer label resource names
          have the form:
          ``customers/{customer_id}/customerLabels/{label_id}``
      customer:
          Output only. The resource name of the customer to which the
          label is attached. Read only.
      label:
          Output only. The resource name of the label assigned to the
          customer.  Note: the Customer ID portion of the label resource
          name is not validated when creating a new CustomerLabel.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.resources.CustomerLabel)
  })
_sym_db.RegisterMessage(CustomerLabel)


DESCRIPTOR._options = None
_CUSTOMERLABEL.fields_by_name['resource_name']._options = None
_CUSTOMERLABEL.fields_by_name['customer']._options = None
_CUSTOMERLABEL.fields_by_name['label']._options = None
_CUSTOMERLABEL._options = None
# @@protoc_insertion_point(module_scope)
