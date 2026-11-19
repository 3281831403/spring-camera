import pytest

from gameplay import spring_camera as mod

CASES = [
    ('capsule_margin', [0.4, 0.05], 0.45, True),
    ('clamp_pitch', [100, 80], 80, False),
    ('clamp_pitch', [-100, 80], -80, False),
    ('damped_return', [0, 10, 0.1, 5], 5.0, True),
    ('smooth_target', [[0, 0], [10, 20], 0.5], [5.0, 10.0], True),
    ('segment_lengths', [6, [1, 1, 2]], [1.5, 1.5, 3.0], True),
    ('occlusion_alpha', [2, 4], 0.5, True),
    ('occlusion_alpha', [8, 4], 0.0, True),
    ('lock_lerp', [0, 90, 0.5], 45.0, True),
    ('fov_distance', [4, 60, 90], 2.3094010767585034, True),
    ('apply_deadzone', [0.05, 0.1], 0.0, True),
    ('apply_deadzone', [0.3, 0.1], 0.3, True),
    ('apply_sensitivity', [0.3, 2.0], 0.6, True),
    ('capsule_margin', [1.0, 0.1], 1.1, True),
    ('damped_return', [10, 0, 1.0, 1.0], 0.0, True),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_spring_camera_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
