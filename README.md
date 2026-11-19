# 弹簧相机：碰撞、阻尼与 FOV

第三人称相机贴墙走时穿墙又弹回：弹簧臂单射线、近裁剪面太小、碰撞后瞬移、俯仰不钳制、目标点滞后、多段臂不按比例、遮挡不淡出、锁定切换不插值、FOV 变化不重算距离、死区与灵敏度未分离。

## 目录结构

```
README.md
conftest.py
.gitignore
gameplay/__init__.py
gameplay/spring_camera.py
tests/test_spring_camera.py
```

## 当前状态

`gameplay/spring_camera.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_spring_camera.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 弹簧臂按胶囊体半径留余量
2. 近裁剪面约束碰撞半径
3. 碰撞后按阻尼回弹
4. 俯仰角钳制
5. 目标点平滑跟随
6. 多段弹簧臂按段长比例分配
7. 遮挡物淡出
8. 锁定目标切换插值
9. FOV 变化重算碰撞距离
10. 死区与灵敏度分离

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `gameplay/spring_camera.py`
后 15 条用例应全部通过。
