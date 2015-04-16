# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: purchase.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='purchase.proto',
  package='Sanguo.protocol.purchase',
  serialized_pb='\n\x0epurchase.proto\x12\x18Sanguo.protocol.purchase\"\xc0\x01\n\x14PurchaseStatusNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12M\n\x06status\x18\x02 \x03(\x0b\x32=.Sanguo.protocol.purchase.PurchaseStatusNotify.PurchaseStatus\x12\x1b\n\x13yueka_remained_days\x18\x03 \x02(\x05\x1a+\n\x0ePurchaseStatus\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05\x66irst\x18\x02 \x02(\x08\"<\n\x18PurchaseIOSVerifyRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07receipt\x18\x02 \x02(\t\"K\n\x19PurchaseIOSVerifyResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12\x10\n\x08goods_id\x18\x03 \x01(\x05\"^\n\x1bPurchaseAllSDKVerifyRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02sn\x18\x02 \x02(\t\x12\x10\n\x08goods_id\x18\x03 \x02(\x05\x12\x10\n\x08platform\x18\x04 \x02(\t\"N\n\x1cPurchaseAllSDKVerifyResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12\x10\n\x08goods_id\x18\x03 \x01(\x05\"P\n\x19PurchaseGetOrderIdRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x10\n\x08goods_id\x18\x02 \x02(\x05\x12\x10\n\x08platform\x18\x03 \x02(\t\"L\n\x1aPurchaseGetOrderIdResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12\x10\n\x08order_id\x18\x03 \x01(\t\";\n\x16PurchaseConfirmRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x10\n\x08platform\x18\x02 \x02(\t\"\xd5\x01\n\x17PurchaseConfirmResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12W\n\x06reason\x18\x03 \x01(\x0e\x32G.Sanguo.protocol.purchase.PurchaseConfirmResponse.PurchaseFailureReason\x12\x10\n\x08goods_id\x18\x04 \x01(\x05\"1\n\x15PurchaseFailureReason\x12\x0b\n\x07WAITING\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02')



_PURCHASECONFIRMRESPONSE_PURCHASEFAILUREREASON = _descriptor.EnumDescriptor(
  name='PurchaseFailureReason',
  full_name='Sanguo.protocol.purchase.PurchaseConfirmResponse.PurchaseFailureReason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WAITING', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=940,
  serialized_end=989,
)


_PURCHASESTATUSNOTIFY_PURCHASESTATUS = _descriptor.Descriptor(
  name='PurchaseStatus',
  full_name='Sanguo.protocol.purchase.PurchaseStatusNotify.PurchaseStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Sanguo.protocol.purchase.PurchaseStatusNotify.PurchaseStatus.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first', full_name='Sanguo.protocol.purchase.PurchaseStatusNotify.PurchaseStatus.first', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=194,
  serialized_end=237,
)

_PURCHASESTATUSNOTIFY = _descriptor.Descriptor(
  name='PurchaseStatusNotify',
  full_name='Sanguo.protocol.purchase.PurchaseStatusNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.PurchaseStatusNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Sanguo.protocol.purchase.PurchaseStatusNotify.status', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='yueka_remained_days', full_name='Sanguo.protocol.purchase.PurchaseStatusNotify.yueka_remained_days', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PURCHASESTATUSNOTIFY_PURCHASESTATUS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=45,
  serialized_end=237,
)


_PURCHASEIOSVERIFYREQUEST = _descriptor.Descriptor(
  name='PurchaseIOSVerifyRequest',
  full_name='Sanguo.protocol.purchase.PurchaseIOSVerifyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.PurchaseIOSVerifyRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receipt', full_name='Sanguo.protocol.purchase.PurchaseIOSVerifyRequest.receipt', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=239,
  serialized_end=299,
)


_PURCHASEIOSVERIFYRESPONSE = _descriptor.Descriptor(
  name='PurchaseIOSVerifyResponse',
  full_name='Sanguo.protocol.purchase.PurchaseIOSVerifyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.purchase.PurchaseIOSVerifyResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.PurchaseIOSVerifyResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goods_id', full_name='Sanguo.protocol.purchase.PurchaseIOSVerifyResponse.goods_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=301,
  serialized_end=376,
)


_PURCHASEALLSDKVERIFYREQUEST = _descriptor.Descriptor(
  name='PurchaseAllSDKVerifyRequest',
  full_name='Sanguo.protocol.purchase.PurchaseAllSDKVerifyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.PurchaseAllSDKVerifyRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sn', full_name='Sanguo.protocol.purchase.PurchaseAllSDKVerifyRequest.sn', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goods_id', full_name='Sanguo.protocol.purchase.PurchaseAllSDKVerifyRequest.goods_id', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='platform', full_name='Sanguo.protocol.purchase.PurchaseAllSDKVerifyRequest.platform', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=378,
  serialized_end=472,
)


_PURCHASEALLSDKVERIFYRESPONSE = _descriptor.Descriptor(
  name='PurchaseAllSDKVerifyResponse',
  full_name='Sanguo.protocol.purchase.PurchaseAllSDKVerifyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.purchase.PurchaseAllSDKVerifyResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.PurchaseAllSDKVerifyResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goods_id', full_name='Sanguo.protocol.purchase.PurchaseAllSDKVerifyResponse.goods_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=474,
  serialized_end=552,
)


_PURCHASEGETORDERIDREQUEST = _descriptor.Descriptor(
  name='PurchaseGetOrderIdRequest',
  full_name='Sanguo.protocol.purchase.PurchaseGetOrderIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.PurchaseGetOrderIdRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goods_id', full_name='Sanguo.protocol.purchase.PurchaseGetOrderIdRequest.goods_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='platform', full_name='Sanguo.protocol.purchase.PurchaseGetOrderIdRequest.platform', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=554,
  serialized_end=634,
)


_PURCHASEGETORDERIDRESPONSE = _descriptor.Descriptor(
  name='PurchaseGetOrderIdResponse',
  full_name='Sanguo.protocol.purchase.PurchaseGetOrderIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.purchase.PurchaseGetOrderIdResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.PurchaseGetOrderIdResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='Sanguo.protocol.purchase.PurchaseGetOrderIdResponse.order_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=636,
  serialized_end=712,
)


_PURCHASECONFIRMREQUEST = _descriptor.Descriptor(
  name='PurchaseConfirmRequest',
  full_name='Sanguo.protocol.purchase.PurchaseConfirmRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.PurchaseConfirmRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='platform', full_name='Sanguo.protocol.purchase.PurchaseConfirmRequest.platform', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=714,
  serialized_end=773,
)


_PURCHASECONFIRMRESPONSE = _descriptor.Descriptor(
  name='PurchaseConfirmResponse',
  full_name='Sanguo.protocol.purchase.PurchaseConfirmResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.purchase.PurchaseConfirmResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.PurchaseConfirmResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='Sanguo.protocol.purchase.PurchaseConfirmResponse.reason', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goods_id', full_name='Sanguo.protocol.purchase.PurchaseConfirmResponse.goods_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PURCHASECONFIRMRESPONSE_PURCHASEFAILUREREASON,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=776,
  serialized_end=989,
)

_PURCHASESTATUSNOTIFY_PURCHASESTATUS.containing_type = _PURCHASESTATUSNOTIFY;
_PURCHASESTATUSNOTIFY.fields_by_name['status'].message_type = _PURCHASESTATUSNOTIFY_PURCHASESTATUS
_PURCHASECONFIRMRESPONSE.fields_by_name['reason'].enum_type = _PURCHASECONFIRMRESPONSE_PURCHASEFAILUREREASON
_PURCHASECONFIRMRESPONSE_PURCHASEFAILUREREASON.containing_type = _PURCHASECONFIRMRESPONSE;
DESCRIPTOR.message_types_by_name['PurchaseStatusNotify'] = _PURCHASESTATUSNOTIFY
DESCRIPTOR.message_types_by_name['PurchaseIOSVerifyRequest'] = _PURCHASEIOSVERIFYREQUEST
DESCRIPTOR.message_types_by_name['PurchaseIOSVerifyResponse'] = _PURCHASEIOSVERIFYRESPONSE
DESCRIPTOR.message_types_by_name['PurchaseAllSDKVerifyRequest'] = _PURCHASEALLSDKVERIFYREQUEST
DESCRIPTOR.message_types_by_name['PurchaseAllSDKVerifyResponse'] = _PURCHASEALLSDKVERIFYRESPONSE
DESCRIPTOR.message_types_by_name['PurchaseGetOrderIdRequest'] = _PURCHASEGETORDERIDREQUEST
DESCRIPTOR.message_types_by_name['PurchaseGetOrderIdResponse'] = _PURCHASEGETORDERIDRESPONSE
DESCRIPTOR.message_types_by_name['PurchaseConfirmRequest'] = _PURCHASECONFIRMREQUEST
DESCRIPTOR.message_types_by_name['PurchaseConfirmResponse'] = _PURCHASECONFIRMRESPONSE

class PurchaseStatusNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class PurchaseStatus(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _PURCHASESTATUSNOTIFY_PURCHASESTATUS

    # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.PurchaseStatusNotify.PurchaseStatus)
  DESCRIPTOR = _PURCHASESTATUSNOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.PurchaseStatusNotify)

class PurchaseIOSVerifyRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PURCHASEIOSVERIFYREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.PurchaseIOSVerifyRequest)

class PurchaseIOSVerifyResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PURCHASEIOSVERIFYRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.PurchaseIOSVerifyResponse)

class PurchaseAllSDKVerifyRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PURCHASEALLSDKVERIFYREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.PurchaseAllSDKVerifyRequest)

class PurchaseAllSDKVerifyResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PURCHASEALLSDKVERIFYRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.PurchaseAllSDKVerifyResponse)

class PurchaseGetOrderIdRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PURCHASEGETORDERIDREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.PurchaseGetOrderIdRequest)

class PurchaseGetOrderIdResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PURCHASEGETORDERIDRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.PurchaseGetOrderIdResponse)

class PurchaseConfirmRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PURCHASECONFIRMREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.PurchaseConfirmRequest)

class PurchaseConfirmResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PURCHASECONFIRMRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.PurchaseConfirmResponse)


# @@protoc_insertion_point(module_scope)
