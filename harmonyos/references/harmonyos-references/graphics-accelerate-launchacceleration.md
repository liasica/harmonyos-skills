---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-launchacceleration
title: launchAcceleration（游戏启动加速）
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > ArkTS API > launchAcceleration（游戏启动加速）
category: harmonyos-references
scraped_at: 2026-04-29T14:06:15+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:4944ff4280afa6816139a26725392487142b4b22e0b6256ab6e0d8de0e380e7d
---

本模块提供游戏启动加速能力。

**系统能力：** SystemCapability.GraphicsGame.LaunchAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 6.0.0(20)

## 导入模块

PhonePC/2in1Tablet

```
1. import { launchAcceleration } from '@kit.GraphicsAccelerateKit';
```

## isLaunchMirrorEnabled

PhonePC/2in1Tablet

isLaunchMirrorEnabled(): boolean

查询游戏的内存镜像功能是否使能。

**系统能力：** SystemCapability.GraphicsGame.LaunchAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 系统将结合当前设备的游戏热度、内存镜像数、当日磁盘换出量综合判定是否使能内存镜像功能：  - true：游戏使能了内存镜像功能。游戏先切换场景（建议开发者将场景切换至游戏登录界面），系统在退出游戏前自动制作内存镜像，制作内存镜像大概需要4s。  - false：游戏未使能内存镜像功能，系统将直接退出游戏进程。  默认为false。 |

**示例**：

```
1. import { launchAcceleration } from '@kit.GraphicsAccelerateKit';

3. onWindowStageWillDestroy(): void {
4. // 查询当前游戏内存镜像功能是否使能。
5. let enable = launchAcceleration.isLaunchMirrorEnabled()
6. if (enable) {
7. // 切换场景的代码逻辑
8. }
9. }
```
