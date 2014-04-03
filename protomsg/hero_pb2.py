# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hero.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hero.proto',
  package='Sanguo.protocol.hero',
  serialized_pb='\n\nhero.proto\x12\x14Sanguo.protocol.hero\"\x92\x01\n\x04Hero\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x13\n\x0boriginal_id\x18\x02 \x02(\x05\x12\x0e\n\x06\x61ttack\x18\x03 \x02(\x05\x12\x0f\n\x07\x64\x65\x66\x65nse\x18\x04 \x02(\x05\x12\n\n\x02hp\x18\x05 \x02(\x05\x12\x0c\n\x04\x63irt\x18\x06 \x02(\x05\x12\x0c\n\x04step\x18\x07 \x02(\x05\x12\x11\n\tstep_cost\x18\x08 \x02(\x05\x12\r\n\x05power\x18\t \x02(\x05\"&\n\x08HeroSoul\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x02(\x05\"T\n\x0eHeroSoulNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x31\n\therosouls\x18\x02 \x03(\x0b\x32\x1e.Sanguo.protocol.hero.HeroSoul\"W\n\x11\x41\x64\x64HeroSoulNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x31\n\therosouls\x18\x02 \x03(\x0b\x32\x1e.Sanguo.protocol.hero.HeroSoul\"Z\n\x14UpdateHeroSoulNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x31\n\therosouls\x18\x02 \x03(\x0b\x32\x1e.Sanguo.protocol.hero.HeroSoul\"4\n\x14RemoveHeroSoulNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0b\n\x03ids\x18\x02 \x03(\x05\"H\n\nHeroNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12)\n\x05heros\x18\x02 \x03(\x0b\x32\x1a.Sanguo.protocol.hero.Hero\"K\n\rAddHeroNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12)\n\x05heros\x18\x02 \x03(\x0b\x32\x1a.Sanguo.protocol.hero.Hero\"0\n\x10RemoveHeroNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0b\n\x03ids\x18\x02 \x03(\x05\"N\n\x10UpdateHeroNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12)\n\x05heros\x18\x02 \x03(\x0b\x32\x1a.Sanguo.protocol.hero.Hero\"\x83\x02\n\x12GetHeroPanelNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x17\n\x0frefresh_seconds\x18\x02 \x02(\x05\x12\x12\n\nfree_times\x18\x03 \x02(\x05\x12\x12\n\nopen_sycee\x18\x04 \x02(\x05\x12\x15\n\rrefresh_sycee\x18\x05 \x02(\x05\x12\x45\n\x07sockets\x18\x06 \x03(\x0b\x32\x34.Sanguo.protocol.hero.GetHeroPanelNotify.PanelSocket\x12\x11\n\tnew_start\x18\x07 \x02(\x08\x1a*\n\x0bPanelSocket\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0f\n\x07hero_id\x18\x02 \x02(\x05\"-\n\x0eGetHeroRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\x05\"M\n\x0fGetHeroResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12\n\n\x02id\x18\x03 \x01(\x05\x12\x10\n\x08hero_oid\x18\x04 \x01(\x05\"&\n\x13GetHeroStartRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\"4\n\x14GetHeroStartResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"(\n\x15GetHeroRefreshRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\"6\n\x16GetHeroRefreshResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"0\n\x11HeroStepUpRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\x05\"2\n\x12HeroStepUpResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\";\n\x10MergeHeroRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x16\n\x0eusing_hero_ids\x18\x02 \x03(\x05\"1\n\x11MergeHeroResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c')




_HERO = _descriptor.Descriptor(
  name='Hero',
  full_name='Sanguo.protocol.hero.Hero',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Sanguo.protocol.hero.Hero.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='original_id', full_name='Sanguo.protocol.hero.Hero.original_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attack', full_name='Sanguo.protocol.hero.Hero.attack', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='defense', full_name='Sanguo.protocol.hero.Hero.defense', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hp', full_name='Sanguo.protocol.hero.Hero.hp', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cirt', full_name='Sanguo.protocol.hero.Hero.cirt', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step', full_name='Sanguo.protocol.hero.Hero.step', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_cost', full_name='Sanguo.protocol.hero.Hero.step_cost', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power', full_name='Sanguo.protocol.hero.Hero.power', index=8,
      number=9, type=5, cpp_type=1, label=2,
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
  serialized_start=37,
  serialized_end=183,
)


_HEROSOUL = _descriptor.Descriptor(
  name='HeroSoul',
  full_name='Sanguo.protocol.hero.HeroSoul',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Sanguo.protocol.hero.HeroSoul.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='Sanguo.protocol.hero.HeroSoul.amount', index=1,
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
  serialized_start=185,
  serialized_end=223,
)


_HEROSOULNOTIFY = _descriptor.Descriptor(
  name='HeroSoulNotify',
  full_name='Sanguo.protocol.hero.HeroSoulNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.HeroSoulNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='herosouls', full_name='Sanguo.protocol.hero.HeroSoulNotify.herosouls', index=1,
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
  serialized_start=225,
  serialized_end=309,
)


_ADDHEROSOULNOTIFY = _descriptor.Descriptor(
  name='AddHeroSoulNotify',
  full_name='Sanguo.protocol.hero.AddHeroSoulNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.AddHeroSoulNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='herosouls', full_name='Sanguo.protocol.hero.AddHeroSoulNotify.herosouls', index=1,
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
  serialized_start=311,
  serialized_end=398,
)


_UPDATEHEROSOULNOTIFY = _descriptor.Descriptor(
  name='UpdateHeroSoulNotify',
  full_name='Sanguo.protocol.hero.UpdateHeroSoulNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.UpdateHeroSoulNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='herosouls', full_name='Sanguo.protocol.hero.UpdateHeroSoulNotify.herosouls', index=1,
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
  serialized_start=400,
  serialized_end=490,
)


_REMOVEHEROSOULNOTIFY = _descriptor.Descriptor(
  name='RemoveHeroSoulNotify',
  full_name='Sanguo.protocol.hero.RemoveHeroSoulNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.RemoveHeroSoulNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ids', full_name='Sanguo.protocol.hero.RemoveHeroSoulNotify.ids', index=1,
      number=2, type=5, cpp_type=1, label=3,
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
  serialized_start=492,
  serialized_end=544,
)


_HERONOTIFY = _descriptor.Descriptor(
  name='HeroNotify',
  full_name='Sanguo.protocol.hero.HeroNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.HeroNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heros', full_name='Sanguo.protocol.hero.HeroNotify.heros', index=1,
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
  serialized_start=546,
  serialized_end=618,
)


_ADDHERONOTIFY = _descriptor.Descriptor(
  name='AddHeroNotify',
  full_name='Sanguo.protocol.hero.AddHeroNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.AddHeroNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heros', full_name='Sanguo.protocol.hero.AddHeroNotify.heros', index=1,
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
  serialized_start=620,
  serialized_end=695,
)


_REMOVEHERONOTIFY = _descriptor.Descriptor(
  name='RemoveHeroNotify',
  full_name='Sanguo.protocol.hero.RemoveHeroNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.RemoveHeroNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ids', full_name='Sanguo.protocol.hero.RemoveHeroNotify.ids', index=1,
      number=2, type=5, cpp_type=1, label=3,
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
  serialized_start=697,
  serialized_end=745,
)


_UPDATEHERONOTIFY = _descriptor.Descriptor(
  name='UpdateHeroNotify',
  full_name='Sanguo.protocol.hero.UpdateHeroNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.UpdateHeroNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heros', full_name='Sanguo.protocol.hero.UpdateHeroNotify.heros', index=1,
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
  serialized_start=747,
  serialized_end=825,
)


_GETHEROPANELNOTIFY_PANELSOCKET = _descriptor.Descriptor(
  name='PanelSocket',
  full_name='Sanguo.protocol.hero.GetHeroPanelNotify.PanelSocket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Sanguo.protocol.hero.GetHeroPanelNotify.PanelSocket.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_id', full_name='Sanguo.protocol.hero.GetHeroPanelNotify.PanelSocket.hero_id', index=1,
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
  serialized_start=1045,
  serialized_end=1087,
)

_GETHEROPANELNOTIFY = _descriptor.Descriptor(
  name='GetHeroPanelNotify',
  full_name='Sanguo.protocol.hero.GetHeroPanelNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.GetHeroPanelNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refresh_seconds', full_name='Sanguo.protocol.hero.GetHeroPanelNotify.refresh_seconds', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='free_times', full_name='Sanguo.protocol.hero.GetHeroPanelNotify.free_times', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open_sycee', full_name='Sanguo.protocol.hero.GetHeroPanelNotify.open_sycee', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refresh_sycee', full_name='Sanguo.protocol.hero.GetHeroPanelNotify.refresh_sycee', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sockets', full_name='Sanguo.protocol.hero.GetHeroPanelNotify.sockets', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_start', full_name='Sanguo.protocol.hero.GetHeroPanelNotify.new_start', index=6,
      number=7, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GETHEROPANELNOTIFY_PANELSOCKET, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=828,
  serialized_end=1087,
)


_GETHEROREQUEST = _descriptor.Descriptor(
  name='GetHeroRequest',
  full_name='Sanguo.protocol.hero.GetHeroRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.GetHeroRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Sanguo.protocol.hero.GetHeroRequest.id', index=1,
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
  serialized_start=1089,
  serialized_end=1134,
)


_GETHERORESPONSE = _descriptor.Descriptor(
  name='GetHeroResponse',
  full_name='Sanguo.protocol.hero.GetHeroResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.hero.GetHeroResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.GetHeroResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Sanguo.protocol.hero.GetHeroResponse.id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_oid', full_name='Sanguo.protocol.hero.GetHeroResponse.hero_oid', index=3,
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
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1136,
  serialized_end=1213,
)


_GETHEROSTARTREQUEST = _descriptor.Descriptor(
  name='GetHeroStartRequest',
  full_name='Sanguo.protocol.hero.GetHeroStartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.GetHeroStartRequest.session', index=0,
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
  serialized_start=1215,
  serialized_end=1253,
)


_GETHEROSTARTRESPONSE = _descriptor.Descriptor(
  name='GetHeroStartResponse',
  full_name='Sanguo.protocol.hero.GetHeroStartResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.hero.GetHeroStartResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.GetHeroStartResponse.session', index=1,
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
  serialized_start=1255,
  serialized_end=1307,
)


_GETHEROREFRESHREQUEST = _descriptor.Descriptor(
  name='GetHeroRefreshRequest',
  full_name='Sanguo.protocol.hero.GetHeroRefreshRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.GetHeroRefreshRequest.session', index=0,
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
  serialized_start=1309,
  serialized_end=1349,
)


_GETHEROREFRESHRESPONSE = _descriptor.Descriptor(
  name='GetHeroRefreshResponse',
  full_name='Sanguo.protocol.hero.GetHeroRefreshResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.hero.GetHeroRefreshResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.GetHeroRefreshResponse.session', index=1,
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
  serialized_start=1351,
  serialized_end=1405,
)


_HEROSTEPUPREQUEST = _descriptor.Descriptor(
  name='HeroStepUpRequest',
  full_name='Sanguo.protocol.hero.HeroStepUpRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.HeroStepUpRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Sanguo.protocol.hero.HeroStepUpRequest.id', index=1,
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
  serialized_start=1407,
  serialized_end=1455,
)


_HEROSTEPUPRESPONSE = _descriptor.Descriptor(
  name='HeroStepUpResponse',
  full_name='Sanguo.protocol.hero.HeroStepUpResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.hero.HeroStepUpResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.HeroStepUpResponse.session', index=1,
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
  serialized_start=1457,
  serialized_end=1507,
)


_MERGEHEROREQUEST = _descriptor.Descriptor(
  name='MergeHeroRequest',
  full_name='Sanguo.protocol.hero.MergeHeroRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.MergeHeroRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='using_hero_ids', full_name='Sanguo.protocol.hero.MergeHeroRequest.using_hero_ids', index=1,
      number=2, type=5, cpp_type=1, label=3,
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
  serialized_start=1509,
  serialized_end=1568,
)


_MERGEHERORESPONSE = _descriptor.Descriptor(
  name='MergeHeroResponse',
  full_name='Sanguo.protocol.hero.MergeHeroResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.hero.MergeHeroResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.hero.MergeHeroResponse.session', index=1,
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
  serialized_start=1570,
  serialized_end=1619,
)

_HEROSOULNOTIFY.fields_by_name['herosouls'].message_type = _HEROSOUL
_ADDHEROSOULNOTIFY.fields_by_name['herosouls'].message_type = _HEROSOUL
_UPDATEHEROSOULNOTIFY.fields_by_name['herosouls'].message_type = _HEROSOUL
_HERONOTIFY.fields_by_name['heros'].message_type = _HERO
_ADDHERONOTIFY.fields_by_name['heros'].message_type = _HERO
_UPDATEHERONOTIFY.fields_by_name['heros'].message_type = _HERO
_GETHEROPANELNOTIFY_PANELSOCKET.containing_type = _GETHEROPANELNOTIFY;
_GETHEROPANELNOTIFY.fields_by_name['sockets'].message_type = _GETHEROPANELNOTIFY_PANELSOCKET
DESCRIPTOR.message_types_by_name['Hero'] = _HERO
DESCRIPTOR.message_types_by_name['HeroSoul'] = _HEROSOUL
DESCRIPTOR.message_types_by_name['HeroSoulNotify'] = _HEROSOULNOTIFY
DESCRIPTOR.message_types_by_name['AddHeroSoulNotify'] = _ADDHEROSOULNOTIFY
DESCRIPTOR.message_types_by_name['UpdateHeroSoulNotify'] = _UPDATEHEROSOULNOTIFY
DESCRIPTOR.message_types_by_name['RemoveHeroSoulNotify'] = _REMOVEHEROSOULNOTIFY
DESCRIPTOR.message_types_by_name['HeroNotify'] = _HERONOTIFY
DESCRIPTOR.message_types_by_name['AddHeroNotify'] = _ADDHERONOTIFY
DESCRIPTOR.message_types_by_name['RemoveHeroNotify'] = _REMOVEHERONOTIFY
DESCRIPTOR.message_types_by_name['UpdateHeroNotify'] = _UPDATEHERONOTIFY
DESCRIPTOR.message_types_by_name['GetHeroPanelNotify'] = _GETHEROPANELNOTIFY
DESCRIPTOR.message_types_by_name['GetHeroRequest'] = _GETHEROREQUEST
DESCRIPTOR.message_types_by_name['GetHeroResponse'] = _GETHERORESPONSE
DESCRIPTOR.message_types_by_name['GetHeroStartRequest'] = _GETHEROSTARTREQUEST
DESCRIPTOR.message_types_by_name['GetHeroStartResponse'] = _GETHEROSTARTRESPONSE
DESCRIPTOR.message_types_by_name['GetHeroRefreshRequest'] = _GETHEROREFRESHREQUEST
DESCRIPTOR.message_types_by_name['GetHeroRefreshResponse'] = _GETHEROREFRESHRESPONSE
DESCRIPTOR.message_types_by_name['HeroStepUpRequest'] = _HEROSTEPUPREQUEST
DESCRIPTOR.message_types_by_name['HeroStepUpResponse'] = _HEROSTEPUPRESPONSE
DESCRIPTOR.message_types_by_name['MergeHeroRequest'] = _MERGEHEROREQUEST
DESCRIPTOR.message_types_by_name['MergeHeroResponse'] = _MERGEHERORESPONSE

class Hero(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HERO

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.Hero)

class HeroSoul(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEROSOUL

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.HeroSoul)

class HeroSoulNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEROSOULNOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.HeroSoulNotify)

class AddHeroSoulNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ADDHEROSOULNOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.AddHeroSoulNotify)

class UpdateHeroSoulNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UPDATEHEROSOULNOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.UpdateHeroSoulNotify)

class RemoveHeroSoulNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REMOVEHEROSOULNOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.RemoveHeroSoulNotify)

class HeroNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HERONOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.HeroNotify)

class AddHeroNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ADDHERONOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.AddHeroNotify)

class RemoveHeroNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REMOVEHERONOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.RemoveHeroNotify)

class UpdateHeroNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UPDATEHERONOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.UpdateHeroNotify)

class GetHeroPanelNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class PanelSocket(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _GETHEROPANELNOTIFY_PANELSOCKET

    # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.GetHeroPanelNotify.PanelSocket)
  DESCRIPTOR = _GETHEROPANELNOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.GetHeroPanelNotify)

class GetHeroRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETHEROREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.GetHeroRequest)

class GetHeroResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETHERORESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.GetHeroResponse)

class GetHeroStartRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETHEROSTARTREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.GetHeroStartRequest)

class GetHeroStartResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETHEROSTARTRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.GetHeroStartResponse)

class GetHeroRefreshRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETHEROREFRESHREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.GetHeroRefreshRequest)

class GetHeroRefreshResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETHEROREFRESHRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.GetHeroRefreshResponse)

class HeroStepUpRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEROSTEPUPREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.HeroStepUpRequest)

class HeroStepUpResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEROSTEPUPRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.HeroStepUpResponse)

class MergeHeroRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MERGEHEROREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.MergeHeroRequest)

class MergeHeroResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MERGEHERORESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.hero.MergeHeroResponse)


# @@protoc_insertion_point(module_scope)
