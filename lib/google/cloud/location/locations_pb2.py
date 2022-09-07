# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/location/locations.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/location/locations.proto",
    package="google.cloud.location",
    syntax="proto3",
    serialized_options=b"\n\031com.google.cloud.locationB\016LocationsProtoP\001Z=google.golang.org/genproto/googleapis/cloud/location;location\370\001\001",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n%google/cloud/location/locations.proto\x12\x15google.cloud.location\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x17google/api/client.proto"[\n\x14ListLocationsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"d\n\x15ListLocationsResponse\x12\x32\n\tlocations\x18\x01 \x03(\x0b\x32\x1f.google.cloud.location.Location\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t""\n\x12GetLocationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\xd7\x01\n\x08Location\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0blocation_id\x18\x04 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x05 \x01(\t\x12;\n\x06labels\x18\x02 \x03(\x0b\x32+.google.cloud.location.Location.LabelsEntry\x12&\n\x08metadata\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\xa4\x03\n\tLocations\x12\xab\x01\n\rListLocations\x12+.google.cloud.location.ListLocationsRequest\x1a,.google.cloud.location.ListLocationsResponse"?\x82\xd3\xe4\x93\x02\x39\x12\x14/v1/{name=locations}Z!\x12\x1f/v1/{name=projects/*}/locations\x12\x9e\x01\n\x0bGetLocation\x12).google.cloud.location.GetLocationRequest\x1a\x1f.google.cloud.location.Location"C\x82\xd3\xe4\x93\x02=\x12\x16/v1/{name=locations/*}Z#\x12!/v1/{name=projects/*/locations/*}\x1aH\xca\x41\x14\x63loud.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformBo\n\x19\x63om.google.cloud.locationB\x0eLocationsProtoP\x01Z=google.golang.org/genproto/googleapis/cloud/location;location\xf8\x01\x01\x62\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_any__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
    ],
)


_LISTLOCATIONSREQUEST = _descriptor.Descriptor(
    name="ListLocationsRequest",
    full_name="google.cloud.location.ListLocationsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.location.ListLocationsRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="filter",
            full_name="google.cloud.location.ListLocationsRequest.filter",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="google.cloud.location.ListLocationsRequest.page_size",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="page_token",
            full_name="google.cloud.location.ListLocationsRequest.page_token",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=146,
    serialized_end=237,
)


_LISTLOCATIONSRESPONSE = _descriptor.Descriptor(
    name="ListLocationsResponse",
    full_name="google.cloud.location.ListLocationsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="locations",
            full_name="google.cloud.location.ListLocationsResponse.locations",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="next_page_token",
            full_name="google.cloud.location.ListLocationsResponse.next_page_token",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=239,
    serialized_end=339,
)


_GETLOCATIONREQUEST = _descriptor.Descriptor(
    name="GetLocationRequest",
    full_name="google.cloud.location.GetLocationRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.location.GetLocationRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=341,
    serialized_end=375,
)


_LOCATION_LABELSENTRY = _descriptor.Descriptor(
    name="LabelsEntry",
    full_name="google.cloud.location.Location.LabelsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.location.Location.LabelsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.location.Location.LabelsEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=548,
    serialized_end=593,
)

_LOCATION = _descriptor.Descriptor(
    name="Location",
    full_name="google.cloud.location.Location",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.location.Location.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="location_id",
            full_name="google.cloud.location.Location.location_id",
            index=1,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.cloud.location.Location.display_name",
            index=2,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="labels",
            full_name="google.cloud.location.Location.labels",
            index=3,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="metadata",
            full_name="google.cloud.location.Location.metadata",
            index=4,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[_LOCATION_LABELSENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=378,
    serialized_end=593,
)

_LISTLOCATIONSRESPONSE.fields_by_name["locations"].message_type = _LOCATION
_LOCATION_LABELSENTRY.containing_type = _LOCATION
_LOCATION.fields_by_name["labels"].message_type = _LOCATION_LABELSENTRY
_LOCATION.fields_by_name[
    "metadata"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name["ListLocationsRequest"] = _LISTLOCATIONSREQUEST
DESCRIPTOR.message_types_by_name["ListLocationsResponse"] = _LISTLOCATIONSRESPONSE
DESCRIPTOR.message_types_by_name["GetLocationRequest"] = _GETLOCATIONREQUEST
DESCRIPTOR.message_types_by_name["Location"] = _LOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListLocationsRequest = _reflection.GeneratedProtocolMessageType(
    "ListLocationsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTLOCATIONSREQUEST,
        "__module__": "google.cloud.location.locations_pb2"
        # @@protoc_insertion_point(class_scope:google.cloud.location.ListLocationsRequest)
    },
)
_sym_db.RegisterMessage(ListLocationsRequest)

ListLocationsResponse = _reflection.GeneratedProtocolMessageType(
    "ListLocationsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTLOCATIONSRESPONSE,
        "__module__": "google.cloud.location.locations_pb2"
        # @@protoc_insertion_point(class_scope:google.cloud.location.ListLocationsResponse)
    },
)
_sym_db.RegisterMessage(ListLocationsResponse)

GetLocationRequest = _reflection.GeneratedProtocolMessageType(
    "GetLocationRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETLOCATIONREQUEST,
        "__module__": "google.cloud.location.locations_pb2"
        # @@protoc_insertion_point(class_scope:google.cloud.location.GetLocationRequest)
    },
)
_sym_db.RegisterMessage(GetLocationRequest)

Location = _reflection.GeneratedProtocolMessageType(
    "Location",
    (_message.Message,),
    {
        "LabelsEntry": _reflection.GeneratedProtocolMessageType(
            "LabelsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _LOCATION_LABELSENTRY,
                "__module__": "google.cloud.location.locations_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.location.Location.LabelsEntry)
            },
        ),
        "DESCRIPTOR": _LOCATION,
        "__module__": "google.cloud.location.locations_pb2"
        # @@protoc_insertion_point(class_scope:google.cloud.location.Location)
    },
)
_sym_db.RegisterMessage(Location)
_sym_db.RegisterMessage(Location.LabelsEntry)


DESCRIPTOR._options = None
_LOCATION_LABELSENTRY._options = None

_LOCATIONS = _descriptor.ServiceDescriptor(
    name="Locations",
    full_name="google.cloud.location.Locations",
    file=DESCRIPTOR,
    index=0,
    serialized_options=b"\312A\024cloud.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform",
    create_key=_descriptor._internal_create_key,
    serialized_start=596,
    serialized_end=1016,
    methods=[
        _descriptor.MethodDescriptor(
            name="ListLocations",
            full_name="google.cloud.location.Locations.ListLocations",
            index=0,
            containing_service=None,
            input_type=_LISTLOCATIONSREQUEST,
            output_type=_LISTLOCATIONSRESPONSE,
            serialized_options=b"\202\323\344\223\0029\022\024/v1/{name=locations}Z!\022\037/v1/{name=projects/*}/locations",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GetLocation",
            full_name="google.cloud.location.Locations.GetLocation",
            index=1,
            containing_service=None,
            input_type=_GETLOCATIONREQUEST,
            output_type=_LOCATION,
            serialized_options=b"\202\323\344\223\002=\022\026/v1/{name=locations/*}Z#\022!/v1/{name=projects/*/locations/*}",
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_LOCATIONS)

DESCRIPTOR.services_by_name["Locations"] = _LOCATIONS

# @@protoc_insertion_point(module_scope)
