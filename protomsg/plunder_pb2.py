# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: plunder.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='plunder.proto',
  package='Sanguo.protocol.plunder',
  serialized_pb='\n\rplunder.proto\x12\x17Sanguo.protocol.plunder\x1a\x0c\x63ommon.proto\"/\n\x1cGetPlunderLeaderboardRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\"\xef\x01\n\x1dGetPlunderLeaderboardResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12U\n\x07leaders\x18\x03 \x03(\x0b\x32\x44.Sanguo.protocol.plunder.GetPlunderLeaderboardResponse.PlunderLeader\x1aY\n\rPlunderLeader\x12\x39\n\x04\x63har\x18\x01 \x02(\x0b\x32+.Sanguo.protocol.common.CharacterInfomation\x12\r\n\x05times\x18\x02 \x02(\x05')




_GETPLUNDERLEADERBOARDREQUEST = _descriptor.Descriptor(
  name='GetPlunderLeaderboardRequest',
  full_name='Sanguo.protocol.plunder.GetPlunderLeaderboardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.plunder.GetPlunderLeaderboardRequest.session', index=0,
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
  serialized_start=56,
  serialized_end=103,
)


_GETPLUNDERLEADERBOARDRESPONSE_PLUNDERLEADER = _descriptor.Descriptor(
  name='PlunderLeader',
  full_name='Sanguo.protocol.plunder.GetPlunderLeaderboardResponse.PlunderLeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='char', full_name='Sanguo.protocol.plunder.GetPlunderLeaderboardResponse.PlunderLeader.char', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='times', full_name='Sanguo.protocol.plunder.GetPlunderLeaderboardResponse.PlunderLeader.times', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=256,
  serialized_end=345,
)

_GETPLUNDERLEADERBOARDRESPONSE = _descriptor.Descriptor(
  name='GetPlunderLeaderboardResponse',
  full_name='Sanguo.protocol.plunder.GetPlunderLeaderboardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.plunder.GetPlunderLeaderboardResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.plunder.GetPlunderLeaderboardResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='leaders', full_name='Sanguo.protocol.plunder.GetPlunderLeaderboardResponse.leaders', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GETPLUNDERLEADERBOARDRESPONSE_PLUNDERLEADER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=106,
  serialized_end=345,
)

_GETPLUNDERLEADERBOARDRESPONSE_PLUNDERLEADER.fields_by_name['char'].message_type = common_pb2._CHARACTERINFOMATION
_GETPLUNDERLEADERBOARDRESPONSE_PLUNDERLEADER.containing_type = _GETPLUNDERLEADERBOARDRESPONSE;
_GETPLUNDERLEADERBOARDRESPONSE.fields_by_name['leaders'].message_type = _GETPLUNDERLEADERBOARDRESPONSE_PLUNDERLEADER
DESCRIPTOR.message_types_by_name['GetPlunderLeaderboardRequest'] = _GETPLUNDERLEADERBOARDREQUEST
DESCRIPTOR.message_types_by_name['GetPlunderLeaderboardResponse'] = _GETPLUNDERLEADERBOARDRESPONSE

class GetPlunderLeaderboardRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETPLUNDERLEADERBOARDREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.plunder.GetPlunderLeaderboardRequest)

class GetPlunderLeaderboardResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class PlunderLeader(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _GETPLUNDERLEADERBOARDRESPONSE_PLUNDERLEADER

    # @@protoc_insertion_point(class_scope:Sanguo.protocol.plunder.GetPlunderLeaderboardResponse.PlunderLeader)
  DESCRIPTOR = _GETPLUNDERLEADERBOARDRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.plunder.GetPlunderLeaderboardResponse)


# @@protoc_insertion_point(module_scope)
