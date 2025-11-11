# %%
import math
from build123d import *
from ocp_vscode import show
import lasercut_tools
from auto_finger_joint import auto_finger_joint, FingerType
# %%

INF = 1000 * M

thickness = 3 * MM
glass_thickness = 2 * MM
height = 20 * CM + thickness * 2
length = 30 * CM + thickness * 2
width = 20 * CM + thickness * 2

front_height_addition = 2 * CM
front_height = height - thickness * 2 + front_height_addition
front_length = length - thickness * 2

stand_width = 7 * CM + thickness * 2
stand_height = 5 * CM + thickness * 2

glass_holder_width = 5 * MM

# %%
def finger_joint(a, b, min_finger_width = 30 * MM, swap = False, FingerType = None):
    return auto_finger_joint(a, b, min_finger_width, swap, FingerType)

def finger_joint_all(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            arr[i], arr[j] = finger_joint(arr[i], arr[j])

    return arr

def align_face_to_xy(face: Face):
    center = face.center()
    normal = face.normal_at(center)
    target_normal = Vector(0, 0, 1)
    axis_vector = normal.cross(target_normal)
    
    if axis_vector.length < 1e-6:
        return face # return if already aligned
    
    angle = math.degrees(math.atan2(axis_vector.length, normal.dot(target_normal)))
    axis = Axis(center, axis_vector)
    
    return face.rotate(axis, angle)

def flatten_parts(parts):
    res = []
    print(parts)
    for part in parts:
        face = part.faces().sort_by(SortBy.AREA)[-1]
        aligned_face = align_face_to_xy(face)
        res.append(aligned_face)

    return res

def make_svg(parts, filename = "out.svg"):
    if not isinstance(parts, list):
        parts = [parts]

    new_faces = flatten_parts(parts)
    arranged = lasercut_tools.arrange1d(new_faces)

    exporter = ExportSVG(scale=1)
    exporter.add_layer("Visible")
    exporter.add_shape(arranged, layer="Visible")
    exporter.write(filename)
# %%

glass_offset = glass_holder_width + glass_thickness

# create parts
bottom = Box(length, width, thickness)
top = Box(length, width - glass_offset, thickness)
back = Box(length, thickness, height)
side = Box(thickness, width, height)
front = Box(front_length, glass_thickness, front_height)

stand_front = Box(length, thickness, stand_height)
stand_top = Box(length, stand_width, thickness)

# %% remove holes
incut_height = .33 * CM
incut_width = 2 * CM
front_incut = Location((0, INF/2, front_height/2 - front_height_addition / 2)) * Rotation(90, 0, 0) * extrude(Ellipse(incut_width, incut_height), INF)
front = front - (Location((-length / 4, 0, 0)) * front_incut + Location((front_length / 4, 0, 0)) * front_incut)

back_hole = Location((0, INF/2, height / 3)) * Rotation(90, 0, 0) * extrude(Circle(5 * MM), INF)
back = back - Location((-width / 3, 0, 0)) * back_hole - Location((width / 3, 0, 0)) * back_hole

side_hole = Location((-INF/2, 0, 0)) * Rotation(0, 90, 0) * extrude(Circle(5 * MM), INF)
side_holes = Location((0, 0, -2.5 * CM)) * side_hole + Location((0, width / 3, height / 3)) * side_hole
side = side - side_holes - Location((0, -3 * CM, 0)) * side_holes

incut_height = stand_height * 0.75
incut_width = stand_width * 0.75
left_side = side - Location((0, width / 2 - stand_width / 2 , -height / 2 + stand_height / 2)) * Box(INF, incut_width, incut_height)
right_side = side

# %% move parts
back = Location((0, width / 2 - thickness/2, height / 2 - thickness/2)) * back
top = Location((0, glass_offset/2, height - thickness)) * top
left_side = Location((-length / 2 + thickness/2, 0, height / 2 - thickness/2)) * left_side
right_side = Location((length / 2 - thickness/2, 0, height / 2 - thickness/2)) * right_side
front = Location((0, -width/2 + glass_thickness*1.5 + thickness, front_height / 2 )) * front

side_stripe = Box(thickness, glass_holder_width, height)
side_stripe_l1 = Location((-length / 2 + thickness * 1.5, -width / 2 + glass_holder_width/2, height/2 - thickness/2)) * side_stripe
side_stripe_l2 = Location((0, glass_offset, 0)) * side_stripe_l1
side_stripe_r1 = Location((length - thickness * 3, 0, 0)) * side_stripe_l1
side_stripe_r2 = Location((length - thickness * 3, 0, 0)) * side_stripe_l2

stand_front = Location((0, width/ 2 - stand_width + thickness/2, stand_height / 2 - thickness/2)) * stand_front
stand_top = Location((0, width / 2 - stand_width/2, stand_height - thickness)) * stand_top

# res = bottom + back + left_side + right_side + top + side_stripe_l1 + side_stripe_l2 + side_stripe_r1 + side_stripe_r2 + stand_front + stand_top + front
res = finger_joint_all([bottom, back, left_side, right_side, top, side_stripe_l1, side_stripe_l2, side_stripe_r1, side_stripe_r2, stand_front, stand_top])

# %%

make_svg(res, "box.svg")
# %%
make_svg([front], "front.svg")
