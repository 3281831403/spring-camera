"""弹簧相机：碰撞、阻尼与 FOV 的核心计算。"""

import math


def capsule_margin(radius, near_plane):
    """弹簧臂最小距离为胶囊半径加近裁剪面。

    角色的肩部/胶囊半径再加上相机近裁剪面，保证贴墙时相机不会把近裁剪
    面推进墙体内部。
    """
    return float(radius) + float(near_plane)


def clamp_pitch(pitch, limit):
    """俯仰角钳制到 ±limit。

    limit 取绝对值，避免传入负值时把范围写反。
    """
    limit = abs(float(limit))
    pitch = float(pitch)
    if pitch > limit:
        return limit
    if pitch < -limit:
        return -limit
    return pitch


def damped_return(current, target, dt, damping):
    """碰撞后按阻尼系数回弹。

    使用基于阻尼系数的线性插值：alpha = damping * dt，并钳制到 [0, 1]，
    使回弹在有限步内收敛且不会越过目标点。
    """
    current = float(current)
    target = float(target)
    alpha = float(damping) * float(dt)
    if alpha <= 0.0:
        return current
    if alpha > 1.0:
        alpha = 1.0
    return current + (target - current) * alpha


def smooth_target(previous, current, alpha):
    """相机目标点按 alpha 平滑。

    对目标点的每个分量做线性插值，alpha 钳制到 [0, 1]。
    """
    alpha = max(0.0, min(1.0, float(alpha)))
    return [
        float(p) + (float(c) - float(p)) * alpha
        for p, c in zip(previous, current)
    ]


def segment_lengths(total, ratios):
    """多段弹簧臂按段长比例分配总长。

    各段长度与比例成正比，保证所有段长之和等于 total。
    """
    total = float(total)
    ratios = [float(r) for r in ratios]
    ratio_sum = sum(ratios)
    if ratio_sum <= 0.0:
        return [0.0 for _ in ratios]
    return [total * r / ratio_sum for r in ratios]


def occlusion_alpha(distance, radius):
    """遮挡距离换算淡出透明度。

    遮挡物越近越透明：distance 为 0 时完全不透明（alpha=1），达到 radius
    时完全淡出（alpha=0），超出范围保持 0。
    """
    radius = float(radius)
    if radius <= 0.0:
        return 0.0
    alpha = 1.0 - float(distance) / radius
    return max(0.0, min(1.0, alpha))


def lock_lerp(current, target, t):
    """锁定目标切换时按 t 插值。

    在旧目标与新目标之间平滑过渡，避免切换瞬间镜头甩动。
    """
    t = max(0.0, min(1.0, float(t)))
    return float(current) + (float(target) - float(current)) * t


def fov_distance(base_distance, base_fov, fov):
    """FOV 改变后重算碰撞距离。

    保持相机在屏幕上覆盖的垂直范围不变：距离与 tan(FOV/2) 成反比。
    """
    base_distance = float(base_distance)
    base_half = math.radians(float(base_fov)) * 0.5
    half = math.radians(float(fov)) * 0.5
    denominator = math.tan(half)
    if denominator <= 0.0:
        return base_distance
    return base_distance * math.tan(base_half) / denominator


def apply_deadzone(value, deadzone):
    """输入死区内归零。

    幅值不超过死区的输入直接丢弃，避免轻微推动导致视角漂移。
    """
    if abs(float(value)) <= abs(float(deadzone)):
        return 0.0
    return float(value)


def apply_sensitivity(value, sensitivity):
    """死区外再乘灵敏度。"""
    return float(value) * float(sensitivity)
