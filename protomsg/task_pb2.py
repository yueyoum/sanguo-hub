# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='task.proto',
  package='Sanguo.protocol.task',
  serialized_pb='\n\ntask.proto\x12\x14Sanguo.protocol.task\"\x93\x01\n\x04Task\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x15\n\rcurrent_times\x18\x02 \x02(\x05\x12\x35\n\x06status\x18\x03 \x02(\x0e\x32%.Sanguo.protocol.task.Task.TaskStatus\"1\n\nTaskStatus\x12\t\n\x05\x44OING\x10\x01\x12\n\n\x06REWARD\x10\x02\x12\x0c\n\x08\x43OMPLETE\x10\x03\"H\n\nTaskNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12)\n\x05tasks\x18\x02 \x03(\x0b\x32\x1a.Sanguo.protocol.task.Task')



_TASK_TASKSTATUS = _descriptor.EnumDescriptor(
  name='TaskStatus',
  full_name='Sanguo.protocol.task.Task.TaskStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DOING', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REWARD', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETE', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=135,
  serialized_end=184,
)


_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='Sanguo.protocol.task.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Sanguo.protocol.task.Task.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_times', full_name='Sanguo.protocol.task.Task.current_times', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Sanguo.protocol.task.Task.status', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TASK_TASKSTATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=37,
  serialized_end=184,
)


_TASKNOTIFY = _descriptor.Descriptor(
  name='TaskNotify',
  full_name='Sanguo.protocol.task.TaskNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.task.TaskNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tasks', full_name='Sanguo.protocol.task.TaskNotify.tasks', index=1,
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
  serialized_start=186,
  serialized_end=258,
)

_TASK.fields_by_name['status'].enum_type = _TASK_TASKSTATUS
_TASK_TASKSTATUS.containing_type = _TASK;
_TASKNOTIFY.fields_by_name['tasks'].message_type = _TASK
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['TaskNotify'] = _TASKNOTIFY

class Task(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASK

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.task.Task)

class TaskNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKNOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.task.TaskNotify)


# @@protoc_insertion_point(module_scope)
