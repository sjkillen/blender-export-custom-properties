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

"""
Walk the scene tree and export custom properties as a .json file
"""

# References:
# https://github.com/sobotka/blender/blob/b964f73e7dc435b8b455b4ffbef7132aaeef1e0d/release/scripts/modules/bpy_extras/io_utils.py#L55
# https://github.com/EdyJ/blender-to-unity-fbx-exporter/blob/master/blender-to-unity-fbx-exporter.py
# https://addam.github.io/Export-Paper-Model-from-Blender/

import bpy
from bpy.types import Operator, Context, Scene
from bpy.props import StringProperty, BoolProperty
from bpy_extras.io_utils import ExportHelper
import json


def export_custom_props(filepath: str, scenes):
    data = json.dumps(
        tuple(
            type_wrap_data(scene, export_custom_props_scene(filepath, scene))
            for scene in scenes
        )
    )
    with open(filepath, "wt", encoding="utf8") as fo:
        print(data, file=fo)


def export_custom_props_scene(filepath: str, scene: Scene):
    return tuple(
        type_wrap_data(obj, data)
        for obj in scene.objects
        if (data := get_custom_data(obj))
    )


def type_wrap_data(obj, data):
    """Remove the wrapper in a type string like
    <class '__main__.Foo'> -> Foo"""
    typestring = str(type(obj))[8:-2]
    if "." in typestring:
        typestring = typestring[typestring.rfind(".") + 1 :]
    return {
        "type": typestring,
        "name": obj.name_full,
        "data": data,
    }


def get_custom_data(obj):
    if not hasattr(obj, "keys"):
        return None
    keys = tuple(obj.keys())
    if not len(keys):
        return None
    return tuple((key, str(obj[key])) for key in obj.keys())


class CustomPropExporterJSONOperator(Operator, ExportHelper):
    bl_idname = "export_scene.custompropexporterjson"
    bl_label = "Export Props"

    # ExportHelper uses property
    filename_ext = ".json"

    # Not sure who uses this
    filter_glob: StringProperty(
        default="*.json",
        options={"HIDDEN"},
    )

    current_scene_only: BoolProperty(
        default=True,
        name="Current Scene Only",
        description="Do not export properties for other scenes. If disabled, all scenes in blendata will be exported",
    )

    def execute(self, context: Context):
        if self.current_scene_only:
            scenes = (context.scene,)
        else:
            scenes = tuple(bpy.data.scenes)
        export_custom_props(self.filepath, scenes)
        self.report({"INFO"}, f"Exported to {self.filepath}")
        return {"FINISHED"}


def menu_func_export(self, context):
    self.layout.operator(
        CustomPropExporterJSONOperator.bl_idname, text="Custom Properties (.json)"
    )


def register():
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
