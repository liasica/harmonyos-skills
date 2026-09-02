---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term-native
title: 相机旋转角度的术语
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 相机旋转 > 相机旋转角度的术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:14f309e59207cea2456406bf21cb4a68ae104ec7e592ef8bb46251cc7429e48c
---

在适配相机旋转角度中涉及设备方向、镜头角度、屏幕显示角度等多个术语，开发者可以了解相关概念，帮助理解框架的运作机制。

## 设备自然方向

**设备自然方向**指设备默认的使用方向，以手机为例，如图所示，手机的自然方向为竖屏且充电口向下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/vmJpP0VIRgaIkekHSTVTXw/zh-cn_image_0000002706834548.png)

## 屏幕显示方向

**屏幕显示方向**指当前用户视角下，设备正确的显示方向。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/Rk_XUTuPR5u6wWE-AggnPg/zh-cn_image_0000002736313655.png)

## 屏幕旋转角度

显示设备的屏幕顺时针旋转角度，简称为**屏幕旋转角度**，即设备从自然方向到当前方向的顺时针夹角。

如图所示，图示夹角即为屏幕旋转角度，可通过[OH\_NativeDisplayManager\_GetDefaultDisplayRotation](../harmonyos-references/capi-oh-display-manager-h.md#oh_nativedisplaymanager_getdefaultdisplayrotation)获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/tajDwDdTTjeE1b4XyjFVNQ/zh-cn_image_0000002706674612.png)

## 相机镜头安装角度

**相机镜头安装角度**指相机采集图像方向到设备自然方向在顺时针方向的夹角。

以手机为例，手机后置相机传感器是横屏安装的，当手机在竖屏方向使用后置相机镜头拍摄时，相机采集到的原始图像方向如图所示。

此时图像需要顺时针旋转90度，才能与设备自然方向保持一致，所以**后置相机的镜头角度为90度**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/51LWazgzTHCaNrS_iCNJjQ/zh-cn_image_0000002736433701.png)

而手机前置镜头，是朝向使用者的，当手机在竖屏方向使用前置相机镜头拍摄时，出图方向与后置出图方向互为镜像，如下图所示，**前置相机的镜头角度为270度**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/RZ4m79PMTRW0A2ixBgby2w/zh-cn_image_0000002706834550.png)

## 预览旋转角度

**说明** 

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
