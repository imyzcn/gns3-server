# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

QEMU_PLATFORMS = ["aarch64", "alpha", "arm", "cris", "i386", "lm32", "m68k", "microblaze", "microblazeel", "mips", "mips64", "mips64el", "mipsel", "moxie", "or32", "ppc", "ppc64", "ppcemb", "s390x", "sh4", "sh4eb", "sparc", "sparc64", "tricore", "unicore32", "x86_64", "xtensa", "xtensaeb"]


QEMU_CREATE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Request validation to create a new QEMU VM instance",
    "type": "object",
    "properties": {
        "vm_id": {
            "description": "QEMU VM identifier",
            "oneOf": [
                {"type": "string",
                 "minLength": 36,
                 "maxLength": 36,
                 "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"},
                {"type": "integer"}  # for legacy projects
            ]
        },
        "name": {
            "description": "QEMU VM instance name",
            "type": "string",
            "minLength": 1,
        },
        "usage": {
            "description": "How to use the qemu VM",
            "type": "string",
        },
        "linked_clone": {
            "description": "either the VM is a linked clone or not",
            "type": "boolean"
        },
        "qemu_path": {
            "description": "Path to QEMU",
            "type": ["string", "null"],
            "minLength": 1,
        },
        "platform": {
            "description": "Platform to emulate",
            "enum": QEMU_PLATFORMS + ["null"]
        },
        "console": {
            "description": "console TCP port",
            "minimum": 1,
            "maximum": 65535,
            "type": ["integer", "null"]
        },
        "console_type": {
            "description": "console type",
            "enum": ["telnet", "vnc"]
        },
        "hda_disk_image": {
            "description": "QEMU hda disk image path",
            "type": "string",
        },
        "hda_disk_interface": {
            "description": "QEMU hda interface",
            "type": "string",
        },
        "hda_disk_image_md5sum": {
            "description": "QEMU hda disk image checksum",
            "type": ["string", "null"]
        },
        "hdb_disk_image": {
            "description": "QEMU hdb disk image path",
            "type": "string",
        },
        "hdb_disk_interface": {
            "description": "QEMU hdb interface",
            "type": "string",
        },
        "hdb_disk_image_md5sum": {
            "description": "QEMU hdb disk image checksum",
            "type": ["string", "null"],
        },
        "hdc_disk_image": {
            "description": "QEMU hdc disk image path",
            "type": "string",
        },
        "hdc_disk_interface": {
            "description": "QEMU hdc interface",
            "type": "string",
        },
        "hdc_disk_image_md5sum": {
            "description": "QEMU hdc disk image checksum",
            "type": ["string", "null"],
        },
        "hdd_disk_image": {
            "description": "QEMU hdd disk image path",
            "type": "string",
        },
        "hdd_disk_interface": {
            "description": "QEMU hdd interface",
            "type": "string",
        },
        "hdd_disk_image_md5sum": {
            "description": "QEMU hdd disk image checksum",
            "type": ["string", "null"],
        },
        "cdrom_image": {
            "description": "QEMU cdrom image path",
            "type": "string",
        },
        "cdrom_image_md5sum": {
            "description": "QEMU cdrom image checksum",
            "type": ["string", "null"],
        },
        "boot_priority": {
            "description": "QEMU boot priority",
            "enum": ["c", "d", "n", "cn", "cd"]
        },
        "ram": {
            "description": "amount of RAM in MB",
            "type": ["integer", "null"]
        },
        "cpus": {
            "description": "number of vCPUs",
            "type": ["integer", "null"],
            "minimum": 1,
            "maximum": 255,
        },
        "adapters": {
            "description": "number of adapters",
            "type": ["integer", "null"],
            "minimum": 0,
            "maximum": 32,
        },
        "adapter_type": {
            "description": "QEMU adapter type",
            "type": ["string", "null"],
            "minLength": 1,
        },
        "mac_address": {
            "description": "QEMU MAC address",
            "type": ["string", "null"],
            "minLength": 1,
            "pattern": "^([0-9a-fA-F]{2}[:]){5}([0-9a-fA-F]{2})$"
        },
        "initrd": {
            "description": "QEMU initrd path",
            "type": "string",
        },
        "initrd_md5sum": {
            "description": "QEMU initrd path",
            "type": ["string", "null"],
        },
        "kernel_image": {
            "description": "QEMU kernel image path",
            "type": "string",
        },
        "kernel_image_md5sum": {
            "description": "QEMU kernel image checksum",
            "type": ["string", "null"],
        },
        "kernel_command_line": {
            "description": "QEMU kernel command line",
            "type": ["string", "null"],
        },
        "legacy_networking": {
            "description": "Use QEMU legagy networking commands (-net syntax)",
            "type": ["boolean", "null"],
        },
        "acpi_shutdown": {
            "description": "ACPI shutdown support",
            "type": ["boolean", "null"],
        },
        "cpu_throttling": {
            "description": "Percentage of CPU allowed for QEMU",
            "minimum": 0,
            "maximum": 800,
            "type": ["integer", "null"],
        },
        "process_priority": {
            "description": "Process priority for QEMU",
            "enum": ["realtime",
                     "very high",
                     "high",
                     "normal",
                     "low",
                     "very low",
                     "null"]
        },
        "options": {
            "description": "Additional QEMU options",
            "type": ["string", "null"],
        },
    },
    "additionalProperties": False,
    "required": ["name"],
}

QEMU_UPDATE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Request validation to update a QEMU VM instance",
    "type": "object",
    "properties": {
        "name": {
            "description": "QEMU VM instance name",
            "type": ["string", "null"],
            "minLength": 1,
        },
        "usage": {
            "description": "How to use the qemu VM",
            "type": "string",
        },
        "qemu_path": {
            "description": "Path to QEMU",
            "type": ["string", "null"],
            "minLength": 1,
        },
        "platform": {
            "description": "Platform to emulate",
            "enum": QEMU_PLATFORMS + ["null"]
        },
        "console": {
            "description": "console TCP port",
            "minimum": 1,
            "maximum": 65535,
            "type": ["integer", "null"]
        },
        "console_type": {
            "description": "console type",
            "enum": ["telnet", "vnc"]
        },
        "hda_disk_image": {
            "description": "QEMU hda disk image path",
            "type": "string",
        },
        "hda_disk_interface": {
            "description": "QEMU hda interface",
            "type": "string",
        },
        "hda_disk_image_md5sum": {
            "description": "QEMU hda disk image checksum",
            "type": ["string", "null"]
        },
        "hdb_disk_image": {
            "description": "QEMU hdb disk image path",
            "type": "string",
        },
        "hdb_disk_interface": {
            "description": "QEMU hdb interface",
            "type": "string",
        },
        "hdb_disk_image_md5sum": {
            "description": "QEMU hdb disk image checksum",
            "type": ["string", "null"],
        },
        "hdc_disk_image": {
            "description": "QEMU hdc disk image path",
            "type": "string",
        },
        "hdc_disk_interface": {
            "description": "QEMU hdc interface",
            "type": "string",
        },
        "hdc_disk_image_md5sum": {
            "description": "QEMU hdc disk image checksum",
            "type": ["string", "null"],
        },
        "hdd_disk_image": {
            "description": "QEMU hdd disk image path",
            "type": "string",
        },
        "hdd_disk_interface": {
            "description": "QEMU hdd interface",
            "type": "string",
        },
        "hdd_disk_image_md5sum": {
            "description": "QEMU hdd disk image checksum",
            "type": ["string", "null"],
        },
        "cdrom_image": {
            "description": "QEMU cdrom image path",
            "type": "string",
        },
        "cdrom_image_md5sum": {
            "description": "QEMU cdrom image checksum",
            "type": ["string", "null"],
        },
        "boot_priority": {
            "description": "QEMU boot priority",
            "enum": ["c", "d", "n", "cn", "cd"]
        },
        "ram": {
            "description": "amount of RAM in MB",
            "type": ["integer", "null"]
        },
        "cpus": {
            "description": "number of vCPUs",
            "type": ["integer", "null"],
            "minimum": 1,
            "maximum": 255,
        },
        "adapters": {
            "description": "number of adapters",
            "type": ["integer", "null"],
            "minimum": 0,
            "maximum": 32,
        },
        "adapter_type": {
            "description": "QEMU adapter type",
            "type": ["string", "null"],
            "minLength": 1,
        },
        "mac_address": {
            "description": "QEMU MAC address",
            "type": ["string", "null"],
            "minLength": 1,
            "pattern": "^([0-9a-fA-F]{2}[:]){5}([0-9a-fA-F]{2})$"
        },
        "initrd": {
            "description": "QEMU initrd path",
            "type": "string",
        },
        "initrd_md5sum": {
            "description": "QEMU initrd path",
            "type": ["string", "null"],
        },
        "kernel_image": {
            "description": "QEMU kernel image path",
            "type": "string",
        },
        "kernel_image_md5sum": {
            "description": "QEMU kernel image checksum",
            "type": ["string", "null"],
        },
        "kernel_command_line": {
            "description": "QEMU kernel command line",
            "type": ["string", "null"],
        },
        "legacy_networking": {
            "description": "Use QEMU legagy networking commands (-net syntax)",
            "type": ["boolean", "null"],
        },
        "acpi_shutdown": {
            "description": "ACPI shutdown support",
            "type": ["boolean", "null"],
        },
        "cpu_throttling": {
            "description": "Percentage of CPU allowed for QEMU",
            "minimum": 0,
            "maximum": 800,
            "type": ["integer", "null"],
        },
        "process_priority": {
            "description": "Process priority for QEMU",
            "enum": ["realtime",
                     "very high",
                     "high",
                     "normal",
                     "low",
                     "very low",
                     "null"]
        },
        "options": {
            "description": "Additional QEMU options",
            "type": ["string", "null"],
        },
    },
    "additionalProperties": False,
}

QEMU_OBJECT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Request validation for a QEMU VM instance",
    "type": "object",
    "properties": {
        "vm_id": {
            "description": "QEMU VM uuid",
            "type": "string",
            "minLength": 1,
        },
        "project_id": {
            "description": "Project uuid",
            "type": "string",
            "minLength": 1,
        },
        "name": {
            "description": "QEMU VM instance name",
            "type": "string",
            "minLength": 1,
        },
        "usage": {
            "description": "How to use the qemu VM",
            "type": "string",
        },
        "qemu_path": {
            "description": "path to QEMU",
            "type": "string",
            "minLength": 1,
        },
        "platform": {
            "description": "Platform to emulate",
            "enum": QEMU_PLATFORMS
        },
        "hda_disk_image": {
            "description": "QEMU hda disk image path",
            "type": "string",
        },
        "hda_disk_interface": {
            "description": "QEMU hda interface",
            "type": "string",
        },
        "hda_disk_image_md5sum": {
            "description": "QEMU hda disk image checksum",
            "type": ["string", "null"]
        },
        "hdb_disk_image": {
            "description": "QEMU hdb disk image path",
            "type": "string",
        },
        "hdb_disk_interface": {
            "description": "QEMU hdb interface",
            "type": "string",
        },
        "hdb_disk_image_md5sum": {
            "description": "QEMU hdb disk image checksum",
            "type": ["string", "null"],
        },
        "hdc_disk_image": {
            "description": "QEMU hdc disk image path",
            "type": "string",
        },
        "hdc_disk_interface": {
            "description": "QEMU hdc interface",
            "type": "string",
        },
        "hdc_disk_image_md5sum": {
            "description": "QEMU hdc disk image checksum",
            "type": ["string", "null"],
        },
        "hdd_disk_image": {
            "description": "QEMU hdd disk image path",
            "type": "string",
        },
        "hdd_disk_interface": {
            "description": "QEMU hdd interface",
            "type": "string",
        },
        "hdd_disk_image_md5sum": {
            "description": "QEMU hdd disk image checksum",
            "type": ["string", "null"],
        },
        "cdrom_image": {
            "description": "QEMU cdrom image path",
            "type": "string",
        },
        "cdrom_image_md5sum": {
            "description": "QEMU cdrom image checksum",
            "type": ["string", "null"],
        },
        "boot_priority": {
            "description": "QEMU boot priority",
            "enum": ["c", "d", "n", "cn", "cd"]
        },
        "vm_directory": {
            "decription": "Path to the VM working directory",
            "type": "string"
        },
        "ram": {
            "description": "amount of RAM in MB",
            "type": "integer"
        },
        "cpus": {
            "description": "number of vCPUs",
            "type": ["integer", "null"],
            "minimum": 1,
            "maximum": 255,
        },
        "adapters": {
            "description": "number of adapters",
            "type": "integer",
            "minimum": 0,
            "maximum": 32,
        },
        "adapter_type": {
            "description": "QEMU adapter type",
            "type": "string",
            "minLength": 1,
        },
        "mac_address": {
            "description": "QEMU MAC address",
            "type": "string",
            "minLength": 1,
            "pattern": "^([0-9a-fA-F]{2}[:]){5}([0-9a-fA-F]{2})$"
        },
        "console": {
            "description": "console TCP port",
            "minimum": 1,
            "maximum": 65535,
            "type": "integer"
        },
        "console_type": {
            "description": "console type",
            "enum": ["telnet", "vnc"]
        },
        "initrd": {
            "description": "QEMU initrd path",
            "type": "string",
        },
        "initrd_md5sum": {
            "description": "QEMU initrd path",
            "type": ["string", "null"],
        },
        "kernel_image": {
            "description": "QEMU kernel image path",
            "type": "string",
        },
        "kernel_image_md5sum": {
            "description": "QEMU kernel image checksum",
            "type": ["string", "null"],
        },
        "kernel_command_line": {
            "description": "QEMU kernel command line",
            "type": "string",
        },
        "legacy_networking": {
            "description": "Use QEMU legagy networking commands (-net syntax)",
            "type": "boolean",
        },
        "acpi_shutdown": {
            "description": "ACPI shutdown support",
            "type": "boolean",
        },
        "cpu_throttling": {
            "description": "Percentage of CPU allowed for QEMU",
            "minimum": 0,
            "maximum": 800,
            "type": "integer",
        },
        "process_priority": {
            "description": "Process priority for QEMU",
            "enum": ["realtime",
                     "very high",
                     "high",
                     "normal",
                     "low",
                     "very low"]
        },
        "options": {
            "description": "Additional QEMU options",
            "type": "string",
        },
        "command_line": {
            "description": "Last command line used by GNS3 to start QEMU",
            "type": "string"
        }
    },
    "additionalProperties": False,
    "required": ["vm_id",
                 "project_id",
                 "name",
                 "usage",
                 "qemu_path",
                 "platform",
                 "console_type",
                 "hda_disk_image",
                 "hdb_disk_image",
                 "hdc_disk_image",
                 "hdd_disk_image",
                 "hda_disk_image_md5sum",
                 "hdb_disk_image_md5sum",
                 "hdc_disk_image_md5sum",
                 "hdd_disk_image_md5sum",
                 "hda_disk_interface",
                 "hdb_disk_interface",
                 "hdc_disk_interface",
                 "hdd_disk_interface",
                 "cdrom_image",
                 "cdrom_image_md5sum",
                 "boot_priority",
                 "ram",
                 "cpus",
                 "adapters",
                 "adapter_type",
                 "mac_address",
                 "console",
                 "initrd",
                 "kernel_image",
                 "initrd_md5sum",
                 "kernel_image_md5sum",
                 "kernel_command_line",
                 "legacy_networking",
                 "acpi_shutdown",
                 "cpu_throttling",
                 "process_priority",
                 "options",
                 "vm_directory",
                 "command_line"]
}

QEMU_BINARY_FILTER_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Request validation for a list of qemu capabilities",
    "properties": {
        "archs": {
            "description": "Architectures to filter binaries by",
            "type": "array",
            "items": {
                "enum": QEMU_PLATFORMS
            }
        }
    },
    "additionalProperties": False,
}

QEMU_BINARY_LIST_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Request validation for a list of qemu binaries",
    "type": "array",
    "items": {
        "$ref": "#/definitions/QemuPath"
    },
    "definitions": {
        "QemuPath": {
            "description": "Qemu path object",
            "properties": {
                "path": {
                    "description": "Qemu path",
                    "type": "string",
                },
                "version": {
                    "description": "Qemu version",
                    "type": "string",
                },
            },
        }
    },
    "additionalProperties": False,
}

QEMU_CAPABILITY_LIST_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Request validation for a list of qemu capabilities",
    "properties": {
        "kvm": {
            "description": "Architectures that KVM is enabled for",
            "type": "array",
            "items": {
                "enum": QEMU_PLATFORMS
            }
        }
    },
    "additionalProperties": False,
}

QEMU_IMAGE_CREATE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Create a new qemu image. Options can be specific to a format. Read qemu-img manual for more information",
    "type": "object",
    "properties": {
        "qemu_img": {
            "description": "Path to the qemu-img binary",
            "type": "string"
        },
        "path": {
            "description": "Absolute or relative path of the image",
            "type": "string"
        },
        "format": {
            "description": "Image format type",
            "enum": ["qcow2", "qcow", "vpc", "vdi", "vmdk", "raw"]
        },
        "size": {
            "description": "Image size in M",
            "type": "integer"
        },
        "preallocation": {
            "enum": ["off", "metadata", "falloc", "full"]
        },
        "cluster_size": {
            "type": "integer"
        },
        "refcount_bits": {
            "type": "integer"
        },
        "lazy_refcounts": {
            "enum": ["on", "off"]
        },
        "subformat": {
            "enum": [
                "dynamic",
                "fixed",
                "streamOptimized",
                "twoGbMaxExtentSparse",
                "twoGbMaxExtentFlat",
                "monolithicSparse",
                "monolithicFlat",
            ]
        },
        "static": {
            "enum": ["on", "off"]
        },
        "zeroed_grain": {
            "enum": ["on", "off"]
        },
        "adapter_type": {
            "enum": [
                "ide",
                "lsilogic",
                "buslogic",
                "legacyESX"
            ]
        }
    },
    "required": ["qemu_img", "path", "format", "size"],
    "additionalProperties": False
}
