# Export Custom Props: Export objects' custom properties as a JSON file
# Copyright (C) 2022  Spencer Killen
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "Export Custom Props (.json)",
    "author": "Spencer Killen",
    "description": "Export objects' custom properties as a JSON file",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "File > Export > Custom Properties (.json)",
    "warning": "",
    "category": "Import-Export",
    "doc_url": "https://github.com/sjkillen/export-scene-custom-props-blender-addon",
    "tracker_url": "https://github.com/sjkillen/export-scene-custom-props-blender-addon/issues",
}

from . import auto_load

auto_load.init()


def register():
    auto_load.register()


def unregister():
    auto_load.unregister()
