---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term-native
title: 相机旋转角度的术语
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 相机旋转 > 相机旋转角度的术语
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bb9cd3c463ca205270ceea9c01f47550cf8501f2f25bccf2c5cb5441d2ee6d5d
---

在适配相机旋转角度中涉及设备方向、镜头角度、屏幕显示角度等多个术语，开发者可以了解相关概念，帮助理解框架的运作机制。

## 设备自然方向

**设备自然方向**指设备默认的使用方向，以手机为例，如图所示，手机的自然方向为竖屏且充电口向下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/L5YPZuHPTKSTvxLLW--Bfw/zh-cn_image_0000002589324943.png?HW-CC-KV=V1&HW-CC-Date=20260429T053506Z&HW-CC-Expire=86400&HW-CC-Sign=01A750FAFBC1FAE7490B19CBCEB3A1202B0ADFFED0724F857A5389FA61466096)

## 屏幕显示方向

**屏幕显示方向**指当前用户视角下，设备正确的显示方向。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/_Pae6wAKT6ah2NjR7yHtxw/zh-cn_image_0000002589244879.png?HW-CC-KV=V1&HW-CC-Date=20260429T053506Z&HW-CC-Expire=86400&HW-CC-Sign=DF5F4AC63094034AC9006DE8CCF31D2B2912BA6D3A20AA9CAD06AE7B03453323)

## 屏幕旋转角度

显示设备的屏幕顺时针旋转角度，简称为**屏幕旋转角度**，即设备从自然方向到当前方向的顺时针夹角。

如图所示，图示夹角即为屏幕旋转角度，可通过[OH\_NativeDisplayManager\_GetDefaultDisplayRotation](../harmonyos-references/capi-oh-display-manager-h.md#oh_nativedisplaymanager_getdefaultdisplayrotation)获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/317cwowZSky3eqWzIGqTcA/zh-cn_image_0000002558765074.png?HW-CC-KV=V1&HW-CC-Date=20260429T053506Z&HW-CC-Expire=86400&HW-CC-Sign=FF8ABE9E163F1A938DBE4054E6CEEF1A26CE8F92C5C6982099BB726181C992B6)

## 相机镜头安装角度

**相机镜头安装角度**指相机采集图像方向到设备自然方向在顺时针方向的夹角。

以手机为例，手机后置相机传感器是横屏安装的，当手机在竖屏方向使用后置相机镜头拍摄时，相机采集到的原始图像方向如图所示。

此时图像需要顺时针旋转90度，才能与设备自然方向保持一致，所以**后置相机的镜头角度为90度**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/Gum8FrrgRAejlBrtxhcbvA/zh-cn_image_0000002558605418.png?HW-CC-KV=V1&HW-CC-Date=20260429T053506Z&HW-CC-Expire=86400&HW-CC-Sign=0407CFFA2B9E5AF6B3A1701A04FF2AAB073B9E03692AFBFBAD628C1758A22649)

而手机前置镜头，是朝向使用者的，当手机在竖屏方向使用前置相机镜头拍摄时，出图方向与后置出图方向互为镜像，如下图所示，**前置相机的镜头角度为270度**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/eIXW4GjASlioX5LdYAH9mQ/zh-cn_image_0000002589324945.png?HW-CC-KV=V1&HW-CC-Date=20260429T053506Z&HW-CC-Expire=86400&HW-CC-Sign=41419F9F42D87D6EEA8F10D93CF054A021E3C3FAFC56CA29A4BD92ED447EA641)

## 预览旋转角度

说明

开发者可参考以下章节，了解框架实现的机制，在实际开发过程中，推荐通过接口[获取预览旋转角度](camera-rotation-angle-adaptation-native.md#预览)。

在预览时，图像旋转角度与屏幕显示旋转角度相关。系统将以原始图像方向为基线，根据相机镜头角度和屏幕显示补偿角度，旋转图像。

计算公式：图像旋转角度=镜头安装角度+屏幕显示补偿角度，屏幕显示补偿角度的值与屏幕旋转角度相等。

以手机设备为例展示相机在预览下如何处理图像，计算的角度设置给系统侧，作用于直接送显场景，应用自绘制参考[应用自绘制预览角度处理](camera-rotation-term-native.md#应用自绘制预览角度处理)。

| 设备和镜头方向 | 处理过程示意图 |
| --- | --- |
| **设备条件：**  手机竖屏、充电口向下。  使用后置相机拍摄。  **可得：**  - 后置相机镜头角度 = 90°  - 屏幕旋转角度= 0°，[displayRotation](../harmonyos-references/capi-oh-display-info-h.md#nativedisplaymanager_rotation) = 0  - **图像预览旋转角度 = 90°+0° = 90°** |  |
| **设备条件：**  手机横屏、充电口向左。  使用后置相机拍摄。  **可得：**  - 后置相机镜头角度 = 90°  - 屏幕旋转角度 = 90°，[displayRotation](../harmonyos-references/capi-oh-display-info-h.md#nativedisplaymanager_rotation) = 1  - **图像预览旋转角度 = 90°+90° = 180°** |  |
| **设备条件：**  手机竖屏、充电口向上。  使用后置相机拍摄。  **可得：**  - 后置相机镜头角度 = 90°  - 屏幕旋转角度 = 180°，[displayRotation](../harmonyos-references/capi-oh-display-info-h.md#nativedisplaymanager_rotation) = 2  - **图像预览旋转角度 = 90°+180° = 270°** |  |
| **设备条件：**  手机横屏、充电口向右。  使用后置相机拍摄。  **可得：**  - 后置相机镜头角度 = 90°  - 屏幕旋转角度 = 270°，[displayRotation](../harmonyos-references/capi-oh-display-info-h.md#nativedisplaymanager_rotation) = 3  - **图像预览旋转角度 = 90°+270° = 0°** |  |
| **设备条件：**  手机竖屏、充电口向下。  使用前置相机拍摄。  **可得：**  - 前置相机镜头角度 = 270°  - 前置相机镜像出图  - 屏幕旋转角度= 0°，[displayRotation](../harmonyos-references/capi-oh-display-info-h.md#nativedisplaymanager_rotation) = 0  - **图像预览旋转角度 = 270°+0° = 270°** |  |
| **设备条件：**  手机横屏、充电口向左。  使用前置相机拍摄。  **可得：**  - 前置相机镜头角度 = 270°  - 前置相机镜像出图  - 屏幕旋转角度 = 90°，[displayRotation](../harmonyos-references/capi-oh-display-info-h.md#nativedisplaymanager_rotation) = 1  - **图像预览旋转角度 = 270°+90° =0°** |  |
| **设备条件：**  手机竖屏、充电口向上。  使用前置相机拍摄。  **可得：**  - 前置相机镜头角度 = 270°  - 前置相机镜像出图  - 屏幕旋转角度 = 180°，[displayRotation](../harmonyos-references/capi-oh-display-info-h.md#nativedisplaymanager_rotation) = 2  - **图像预览旋转角度 = 270°+180° = 90°** |  |
| **设备条件：**  手机横屏、充电口向右。  使用前置相机拍摄。  **可得：**  - 前置相机镜头角度 = 270°  - 前置相机镜像出图  - 屏幕旋转角度 = 270°，[displayRotation](../harmonyos-references/capi-oh-display-info-h.md#nativedisplaymanager_rotation) = 3  - **图像预览旋转角度 = 270°+270° = 180°** |  |

## 应用自绘制预览角度处理

应用自绘制场景是指应用获取图片后，通过libyuv、GL等图形处理库进行二次处理，生成新的图像数据并送到显示设备进行渲染绘制。

常见的实现方式是通过使用[image\_receiver\_native.h](../harmonyos-references/capi-image-receiver-native-h.md)创建的回调流，应用层作为消费端，自行处理图片旋转等操作，以适应自绘制场景的预览角度需求。自绘制场景预览角度与[预览旋转角度](camera-rotation-term-native.md#预览旋转角度)中描述的场景存在细微差异。

主要差异体现在使用前置镜头拍摄预览的场景：

* 自绘制场景可以按照[预览旋转角度](camera-rotation-term-native.md#预览旋转角度)中的图示方式，先根据镜头的安装角度进行旋转，随后进行镜像处理，最后再次旋转以适应屏幕角度。然而，这种方式包含多个步骤，较为繁琐，不被推荐。
* 自绘制场景也可以采取先旋转再镜像的方式，这种方式需要考虑水平镜像和垂直镜像，具体的处理步骤如下图所示。

| 设备和镜头方向 | 处理过程示意图 |
| --- | --- |
| **设备条件：**  手机竖屏、充电口向下。  使用前置相机拍摄。  **可得：**  - 前置相机镜头角度 = 270°  - 前置相机镜像出图  - 屏幕旋转角度= 0°，[displayRotation](../harmonyos-references/capi-oh-display-info-h.md#nativedisplaymanager_rotation) = 0  - **图像预览旋转角度 = 270°+0° = 270°** |  |
| **设备条件：**  手机横屏、充电口向左。  使用前置相机拍摄。  **可得：**  - 前置相机镜头角度 = 270°  - 前置相机镜像出图  - 屏幕旋转角度 = 90°，[displayRotation](../harmonyos-references/capi-oh-display-info-h.md#nativedisplaymanager_rotation) = 1  - **图像预览旋转角度 = 270°+90° = 0°** |  |

## 拍照/录像角度

在拍照、录像时，图像旋转角度与设备重力方向（即设备旋转角度）相关。

* 使用后置相机拍摄时，图像旋转角度=[镜头安装角度](camera-rotation-term-native.md#相机镜头安装角度)+重力方向。
* 使用前置相机拍摄时，图像旋转角度=[镜头安装角度](camera-rotation-term-native.md#相机镜头安装角度)-重力方向。

| 设备和镜头方向 | 处理过程示意图 |
| --- | --- |
| **设备条件：**  手机横屏、充电口向左。  使用后置相机拍摄。  **可得：**  - 后置相机镜头角度 = 90°  - 设备旋转角度 = 90°  - **图像预览旋转角度 = 90°+90° = 180°** |  |

应用需要监听[OH\_Sensor\_Subscribe](../harmonyos-references/capi-oh-sensor-h.md#oh_sensor_subscribe)，获取重力传感器在x、y、z三个方向上的数据，计算得出设备旋转角度，请参考[计算设备旋转角度](camera-rotation-angle-adaptation-native.md#计算设备旋转角度)。
