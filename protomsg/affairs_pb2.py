# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: affairs.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import world_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='affairs.proto',
  package='Sanguo.protocol.affairs',
  serialized_pb='\n\raffairs.proto\x12\x17Sanguo.protocol.affairs\x1a\x0bworld.proto\"o\n\x04\x43ity\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x38\n\x06status\x18\x02 \x02(\x0e\x32(.Sanguo.protocol.affairs.City.CityStatus\"!\n\nCityStatus\x12\x08\n\x04OPEN\x10\x01\x12\t\n\x05\x43LOSE\x10\x02\"L\n\nCityNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12-\n\x06\x63ities\x18\x02 \x03(\x0b\x32\x1d.Sanguo.protocol.affairs.City\"p\n\nHangNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07\x63ity_id\x18\x02 \x02(\x05\x12\x12\n\nstart_time\x18\x03 \x02(\x05\x12\x0c\n\x04gold\x18\x04 \x02(\x05\x12\x10\n\x08\x66inished\x18\x05 \x02(\x08\x12\x0c\n\x04logs\x18\x06 \x03(\t\"\"\n\x0fHangSyncRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\"0\n\x10HangSyncResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"\'\n\x14HangGetRewardRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\"f\n\x15HangGetRewardResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12/\n\x04\x64rop\x18\x03 \x01(\x0b\x32!.Sanguo.protocol.world.Attachment\"4\n\x10HangStartRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07\x63ity_id\x18\x02 \x02(\x05\"b\n\x11HangStartResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12/\n\x04\x64rop\x18\x03 \x01(\x0b\x32!.Sanguo.protocol.world.Attachment')



_CITY_CITYSTATUS = _descriptor.EnumDescriptor(
  name='CityStatus',
  full_name='Sanguo.protocol.affairs.City.CityStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPEN', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=133,
  serialized_end=166,
)


_CITY = _descriptor.Descriptor(
  name='City',
  full_name='Sanguo.protocol.affairs.City',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Sanguo.protocol.affairs.City.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Sanguo.protocol.affairs.City.status', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CITY_CITYSTATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=55,
  serialized_end=166,
)


_CITYNOTIFY = _descriptor.Descriptor(
  name='CityNotify',
  full_name='Sanguo.protocol.affairs.CityNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.affairs.CityNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cities', full_name='Sanguo.protocol.affairs.CityNotify.cities', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=168,
  serialized_end=244,
)


_HANGNOTIFY = _descriptor.Descriptor(
  name='HangNotify',
  full_name='Sanguo.protocol.affairs.HangNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.affairs.HangNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='city_id', full_name='Sanguo.protocol.affairs.HangNotify.city_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='Sanguo.protocol.affairs.HangNotify.start_time', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold', full_name='Sanguo.protocol.affairs.HangNotify.gold', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finished', full_name='Sanguo.protocol.affairs.HangNotify.finished', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logs', full_name='Sanguo.protocol.affairs.HangNotify.logs', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=246,
  serialized_end=358,
)


_HANGSYNCREQUEST = _descriptor.Descriptor(
  name='HangSyncRequest',
  full_name='Sanguo.protocol.affairs.HangSyncRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.affairs.HangSyncRequest.session', index=0,
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
  serialized_start=360,
  serialized_end=394,
)


_HANGSYNCRESPONSE = _descriptor.Descriptor(
  name='HangSyncResponse',
  full_name='Sanguo.protocol.affairs.HangSyncResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.affairs.HangSyncResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.affairs.HangSyncResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
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
  serialized_start=396,
  serialized_end=444,
)


_HANGGETREWARDREQUEST = _descriptor.Descriptor(
  name='HangGetRewardRequest',
  full_name='Sanguo.protocol.affairs.HangGetRewardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.affairs.HangGetRewardRequest.session', index=0,
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
  serialized_start=446,
  serialized_end=485,
)


_HANGGETREWARDRESPONSE = _descriptor.Descriptor(
  name='HangGetRewardResponse',
  full_name='Sanguo.protocol.affairs.HangGetRewardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.affairs.HangGetRewardResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.affairs.HangGetRewardResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop', full_name='Sanguo.protocol.affairs.HangGetRewardResponse.drop', index=2,
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
  serialized_start=487,
  serialized_end=589,
)


_HANGSTARTREQUEST = _descriptor.Descriptor(
  name='HangStartRequest',
  full_name='Sanguo.protocol.affairs.HangStartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.affairs.HangStartRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='city_id', full_name='Sanguo.protocol.affairs.HangStartRequest.city_id', index=1,
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
  serialized_start=591,
  serialized_end=643,
)


_HANGSTARTRESPONSE = _descriptor.Descriptor(
  name='HangStartResponse',
  full_name='Sanguo.protocol.affairs.HangStartResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.affairs.HangStartResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.affairs.HangStartResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop', full_name='Sanguo.protocol.affairs.HangStartResponse.drop', index=2,
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
  serialized_start=645,
  serialized_end=743,
)

_CITY.fields_by_name['status'].enum_type = _CITY_CITYSTATUS
_CITY_CITYSTATUS.containing_type = _CITY;
_CITYNOTIFY.fields_by_name['cities'].message_type = _CITY
_HANGGETREWARDRESPONSE.fields_by_name['drop'].message_type = world_pb2._ATTACHMENT
_HANGSTARTRESPONSE.fields_by_name['drop'].message_type = world_pb2._ATTACHMENT
DESCRIPTOR.message_types_by_name['City'] = _CITY
DESCRIPTOR.message_types_by_name['CityNotify'] = _CITYNOTIFY
DESCRIPTOR.message_types_by_name['HangNotify'] = _HANGNOTIFY
DESCRIPTOR.message_types_by_name['HangSyncRequest'] = _HANGSYNCREQUEST
DESCRIPTOR.message_types_by_name['HangSyncResponse'] = _HANGSYNCRESPONSE
DESCRIPTOR.message_types_by_name['HangGetRewardRequest'] = _HANGGETREWARDREQUEST
DESCRIPTOR.message_types_by_name['HangGetRewardResponse'] = _HANGGETREWARDRESPONSE
DESCRIPTOR.message_types_by_name['HangStartRequest'] = _HANGSTARTREQUEST
DESCRIPTOR.message_types_by_name['HangStartResponse'] = _HANGSTARTRESPONSE

class City(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CITY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.affairs.City)

class CityNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CITYNOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.affairs.CityNotify)

class HangNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HANGNOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.affairs.HangNotify)

class HangSyncRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HANGSYNCREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.affairs.HangSyncRequest)

class HangSyncResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HANGSYNCRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.affairs.HangSyncResponse)

class HangGetRewardRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HANGGETREWARDREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.affairs.HangGetRewardRequest)

class HangGetRewardResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HANGGETREWARDRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.affairs.HangGetRewardResponse)

class HangStartRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HANGSTARTREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.affairs.HangStartRequest)

class HangStartResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HANGSTARTRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.affairs.HangStartResponse)


# @@protoc_insertion_point(module_scope)
