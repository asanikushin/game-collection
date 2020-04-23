# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: utils/pb/import.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='utils/pb/import.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x15utils/pb/import.proto\"-\n\rImportRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0e\n\x06loaded\x18\x02 \x01(\x08\"\x1e\n\x0eImportResponse\x12\x0c\n\x04\x64one\x18\x01 \x01(\x08\x32\x31\n\x06Import\x12\'\n\x04Load\x12\x0e.ImportRequest\x1a\x0f.ImportResponseb\x06proto3'
)




_IMPORTREQUEST = _descriptor.Descriptor(
  name='ImportRequest',
  full_name='ImportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='ImportRequest.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loaded', full_name='ImportRequest.loaded', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=25,
  serialized_end=70,
)


_IMPORTRESPONSE = _descriptor.Descriptor(
  name='ImportResponse',
  full_name='ImportResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='done', full_name='ImportResponse.done', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=72,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['ImportRequest'] = _IMPORTREQUEST
DESCRIPTOR.message_types_by_name['ImportResponse'] = _IMPORTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImportRequest = _reflection.GeneratedProtocolMessageType('ImportRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTREQUEST,
  '__module__' : 'utils.pb.import_pb2'
  # @@protoc_insertion_point(class_scope:ImportRequest)
  })
_sym_db.RegisterMessage(ImportRequest)

ImportResponse = _reflection.GeneratedProtocolMessageType('ImportResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTRESPONSE,
  '__module__' : 'utils.pb.import_pb2'
  # @@protoc_insertion_point(class_scope:ImportResponse)
  })
_sym_db.RegisterMessage(ImportResponse)



_IMPORT = _descriptor.ServiceDescriptor(
  name='Import',
  full_name='Import',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=104,
  serialized_end=153,
  methods=[
  _descriptor.MethodDescriptor(
    name='Load',
    full_name='Import.Load',
    index=0,
    containing_service=None,
    input_type=_IMPORTREQUEST,
    output_type=_IMPORTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMPORT)

DESCRIPTOR.services_by_name['Import'] = _IMPORT

# @@protoc_insertion_point(module_scope)
