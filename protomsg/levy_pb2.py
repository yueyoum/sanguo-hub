# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: levy.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import world_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='levy.proto',
  package='Sanguo.protocol.levy',
  serialized_pb='\n\nlevy.proto\x12\x14Sanguo.protocol.levy\x1a\x0bworld.proto\"W\n\nLevyNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x12\n\ncost_sycee\x18\x02 \x02(\x05\x12\x11\n\tcur_times\x18\x03 \x02(\x05\x12\x11\n\tmax_times\x18\x04 \x02(\x05\"\x1e\n\x0bLevyRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\"]\n\x0cLevyResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12/\n\x04\x64rop\x18\x03 \x01(\x0b\x32!.Sanguo.protocol.world.Attachment')




_LEVYNOTIFY = _descriptor.Descriptor(
  name='LevyNotify',
  full_name='Sanguo.protocol.levy.LevyNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.levy.LevyNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cost_sycee', full_name='Sanguo.protocol.levy.LevyNotify.cost_sycee', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cur_times', full_name='Sanguo.protocol.levy.LevyNotify.cur_times', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_times', full_name='Sanguo.protocol.levy.LevyNotify.max_times', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=49,
  serialized_end=136,
)


_LEVYREQUEST = _descriptor.Descriptor(
  name='LevyRequest',
  full_name='Sanguo.protocol.levy.LevyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.levy.LevyRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=138,
  serialized_end=168,
)


_LEVYRESPONSE = _descriptor.Descriptor(
  name='LevyResponse',
  full_name='Sanguo.protocol.levy.LevyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.levy.LevyResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.levy.LevyResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop', full_name='Sanguo.protocol.levy.LevyResponse.drop', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=170,
  serialized_end=263,
)

_LEVYRESPONSE.fields_by_name['drop'].message_type = world_pb2._ATTACHMENT
DESCRIPTOR.message_types_by_name['LevyNotify'] = _LEVYNOTIFY
DESCRIPTOR.message_types_by_name['LevyRequest'] = _LEVYREQUEST
DESCRIPTOR.message_types_by_name['LevyResponse'] = _LEVYRESPONSE

class LevyNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LEVYNOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.levy.LevyNotify)

class LevyRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LEVYREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.levy.LevyRequest)

class LevyResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LEVYRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.levy.LevyResponse)


# @@protoc_insertion_point(module_scope)
