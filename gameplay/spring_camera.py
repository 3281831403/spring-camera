"""弹簧相机：碰撞、阻尼与 FOV：待实现的核心模块。"""


def capsule_margin(radius, near_plane):
    """弹簧臂最小距离为胶囊半径加近裁剪面。"""
    raise NotImplementedError

def clamp_pitch(pitch, limit):
    """俯仰角钳制到 ±limit。"""
    raise NotImplementedError

def damped_return(current, target, dt, damping):
    """碰撞后按阻尼系数回弹。"""
    raise NotImplementedError

def smooth_target(previous, current, alpha):
    """相机目标点按 alpha 平滑。"""
    raise NotImplementedError

def segment_lengths(total, ratios):
    """多段弹簧臂按段长比例分配总长。"""
    raise NotImplementedError

def occlusion_alpha(distance, radius):
    """遮挡距离换算淡出透明度。"""
    raise NotImplementedError

def lock_lerp(current, target, t):
    """锁定目标切换时按 t 插值。"""
    raise NotImplementedError

def fov_distance(base_distance, base_fov, fov):
    """FOV 改变后重算碰撞距离。"""
    raise NotImplementedError

def apply_deadzone(value, deadzone):
    """输入死区内归零。"""
    raise NotImplementedError

def apply_sensitivity(value, sensitivity):
    """死区外再乘灵敏度。"""
    raise NotImplementedError
