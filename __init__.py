bl_info = {
    "name" : "ShapeSmith",
    "author" : "AdiGunturu",
    "description" : "Free form and guided shape maker for blender",
    "blender" : (2, 80, 0),
    "version": (0, 1, 0, 0),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from .guided_shape_maker import OT_draw_operator

addon_keymaps = []

def register():
    bpy.utils.register_class(OT_draw_operator)

    kcfg = bpy.context.window_manager.keyconfigs.addon
    if kcfg:
        km = kcfg.keymaps.new(name='3D View', space_type='VIEW_3D')
   
        kmi = km.keymap_items.new("object.draw_op", 'F', 'PRESS', shift=True, ctrl=True)
        
        addon_keymaps.append((km, kmi))


def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    addon_keymaps.clear()

    bpy.utils.unregister_class(OT_draw_operator)

if __name__ == "__main__":
    register()
