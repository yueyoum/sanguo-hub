# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cmd.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cmd.proto',
  package='Sanguo.protocol.cmd',
  serialized_pb='\n\tcmd.proto\x12\x13Sanguo.protocol.cmd\"I\n\x0bTestRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0e\n\x06\x61\x63tion\x18\x02 \x02(\x05\x12\n\n\x02tp\x18\x03 \x02(\x05\x12\r\n\x05param\x18\x04 \x02(\x05')




_TESTREQUEST = _descriptor.Descriptor(
  name='TestRequest',
  full_name='Sanguo.protocol.cmd.TestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.cmd.TestRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='Sanguo.protocol.cmd.TestRequest.action', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tp', full_name='Sanguo.protocol.cmd.TestRequest.tp', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param', full_name='Sanguo.protocol.cmd.TestRequest.param', index=3,
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
  serialized_start=34,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['TestRequest'] = _TESTREQUEST

class TestRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TESTREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.cmd.TestRequest)


# @@protoc_insertion_point(module_scope)
