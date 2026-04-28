---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawable-descriptor-h
title: drawable_descriptor.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > drawable_descriptor.h
category: harmonyos-references
scraped_at: 2026-04-28T08:03:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3f1fec4766eff585786457e9ca50b0fca29d238ef15ee8081f7786c6bd941e9a
---

## 概述

PhonePC/2in1TabletTVWearable

提供NativeDrawableDescriptor接口的类型定义。

**引用文件：** <arkui/drawable\_descriptor.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [DrawableDescriptorSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/DrawableDescriptorSample)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md) | ArkUI\_DrawableDescriptor | 定义DrawableDescriptor对象。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) | - | 使用Image Kit定义的Native侧的OH\_PixelmapNative对象。 |
| [OH\_PixelmapNative\*](capi-arkui-nativemodule-oh-pixelmapnative8h.md) | OH\_PixelmapNativeHandle | 定义OH\_PixelmapNative对象指针类型。 |
| [ArkUI\_Node](capi-arkui-nativemodule-arkui-node-descriptor.md) | - | 定义ArkUI native组件实例对象。  **起始版本：** 22 |
| [ArkUI\_Node\*](capi-arkui-nativemodule-arkui-node8h.md) | ArkUI\_NodeHandle | 定义ArkUI native组件实例对象指针定义。  **起始版本：** 22 |
| [ArkUI\_DrawableDescriptor\_AnimationController](module-arkui-drawabledescriptoranimationcontroller.md) | ArkUI\_DrawableDescriptor\_AnimationController | 定义DrawableDescriptor动图控制器对象。  **起始版本：** 22 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [DrawableDescriptor\_AnimationStatus](capi-drawable-descriptor-h.md#drawabledescriptor_animationstatus) | DrawableDescriptor\_AnimationStatus | 定义DrawableDescriptor动图的播放状态。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor\* OH\_ArkUI\_DrawableDescriptor\_CreateFromPixelMap(OH\_PixelmapNativeHandle pixelMap)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_createfrompixelmap) | 使用PixelMap创建DrawableDescriptor对象。 |
| [ArkUI\_DrawableDescriptor\* OH\_ArkUI\_DrawableDescriptor\_CreateFromAnimatedPixelMap(OH\_PixelmapNativeHandle\* array, int32\_t size)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_createfromanimatedpixelmap) | 使用PixelMap图片数组创建DrawableDescriptor对象。 |
| [void OH\_ArkUI\_DrawableDescriptor\_Dispose(ArkUI\_DrawableDescriptor\* drawableDescriptor)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_dispose) | 销毁DrawableDescriptor对象指针。 |
| [OH\_PixelmapNativeHandle OH\_ArkUI\_DrawableDescriptor\_GetStaticPixelMap(ArkUI\_DrawableDescriptor\* drawableDescriptor)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_getstaticpixelmap) | 获取PixelMap图片对象指针。 |
| [OH\_PixelmapNativeHandle\* OH\_ArkUI\_DrawableDescriptor\_GetAnimatedPixelMapArray(ArkUI\_DrawableDescriptor\* drawableDescriptor)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_getanimatedpixelmaparray) | 获取用于播放动画的PixelMap图片数组数据。 |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimatedPixelMapArraySize(ArkUI\_DrawableDescriptor\* drawableDescriptor)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_getanimatedpixelmaparraysize) | 获取用于播放动画的PixelMap图片数组数据。 |
| [void OH\_ArkUI\_DrawableDescriptor\_SetAnimationDuration(ArkUI\_DrawableDescriptor\* drawableDescriptor, int32\_t duration)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_setanimationduration) | 设置PixelMap图片数组播放总时长。 |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimationDuration(ArkUI\_DrawableDescriptor\* drawableDescriptor)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_getanimationduration) | 获取PixelMap图片数组播放总时长。 |
| [void OH\_ArkUI\_DrawableDescriptor\_SetAnimationIteration(ArkUI\_DrawableDescriptor\* drawableDescriptor, int32\_t iteration)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_setanimationiteration) | 设置PixelMap图片数组播放次数。 |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimationIteration(ArkUI\_DrawableDescriptor\* drawableDescriptor)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_getanimationiteration) | 获取PixelMap图片数组播放次数。 |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_SetAnimationFrameDurations(ArkUI\_DrawableDescriptor\* drawableDescriptor, uint32\_t\* durations, size\_t size)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_setanimationframedurations) | 设置动图中的单帧播放时间。 |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimationFrameDurations(ArkUI\_DrawableDescriptor\* drawableDescriptor, uint32\_t\* durations, size\_t\* size)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_getanimationframedurations) | 获取动图中的单帧播放时间。 |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_SetAnimationAutoPlay(ArkUI\_DrawableDescriptor\* drawableDescriptor, uint32\_t autoPlay)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_setanimationautoplay) | 设置动图是否自动播放。 |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimationAutoPlay(ArkUI\_DrawableDescriptor\* drawableDescriptor, uint32\_t\* autoPlay)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_getanimationautoplay) | 获取动图是否自动播放。 |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_CreateAnimationController(ArkUI\_DrawableDescriptor\* drawableDescriptor, ArkUI\_NodeHandle node, ArkUI\_DrawableDescriptor\_AnimationController\*\* controller)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_createanimationcontroller) | 创建动图控制器。 |
| [void OH\_ArkUI\_DrawableDescriptor\_DisposeAnimationController( ArkUI\_DrawableDescriptor\_AnimationController\* controller)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_disposeanimationcontroller) | 销毁动图控制器。 |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_StartAnimation(ArkUI\_DrawableDescriptor\_AnimationController\* controller)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_startanimation) | 从首帧开始播放。 |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_StopAnimation(ArkUI\_DrawableDescriptor\_AnimationController\* controller)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_stopanimation) | 停止动图播放并回到首帧。 |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_ResumeAnimation(ArkUI\_DrawableDescriptor\_AnimationController\* controller)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_resumeanimation) | 从当前帧恢复动图播放。 |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_PauseAnimation(ArkUI\_DrawableDescriptor\_AnimationController\* controller)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_pauseanimation) | 暂停动图的播放，保持在当前帧。 |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimationStatus(ArkUI\_DrawableDescriptor\_AnimationController\* controller, DrawableDescriptor\_AnimationStatus\* status)](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_getanimationstatus) | 获取动图的播放状态。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### DrawableDescriptor\_AnimationStatus

PhonePC/2in1TabletTVWearable

```
1. enum DrawableDescriptor_AnimationStatus
```

**描述：**

定义DrawableDescriptor动图的播放状态。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| DRAWABLE\_DESCRIPTOR\_ANIMATION\_STATUS\_INITIAL = 0 | 动画初始状态。 |
| DRAWABLE\_DESCRIPTOR\_ANIMATION\_STATUS\_RUNNING = 1 | 动画处于播放状态。 |
| DRAWABLE\_DESCRIPTOR\_ANIMATION\_STATUS\_PAUSED = 2 | 动画处于暂停状态。 |
| DRAWABLE\_DESCRIPTOR\_ANIMATION\_STATUS\_STOPPED = 3 | 动画处于停止状态。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ArkUI\_DrawableDescriptor\_CreateFromPixelMap()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_DrawableDescriptor* OH_ArkUI_DrawableDescriptor_CreateFromPixelMap(OH_PixelmapNativeHandle pixelMap)
```

**描述：**

使用PixelMap创建DrawableDescriptor对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNativeHandle](capi-arkui-nativemodule-oh-pixelmapnative8h.md) pixelMap | [OH\_PixelmapNative](capi-struct.md)对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* | 返回DrawableDescriptor对象指针。 |

### OH\_ArkUI\_DrawableDescriptor\_CreateFromAnimatedPixelMap()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_DrawableDescriptor* OH_ArkUI_DrawableDescriptor_CreateFromAnimatedPixelMap(OH_PixelmapNativeHandle* array, int32_t size)
```

**描述：**

使用PixelMap图片数组创建DrawableDescriptor对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNativeHandle](capi-arkui-nativemodule-oh-pixelmapnative8h.md)\* array | PixelMap图片数组对象指针。 |
| int32\_t size | PixelMap图片数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* | 返回DrawableDescriptor对象指针。 |

### OH\_ArkUI\_DrawableDescriptor\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_DrawableDescriptor_Dispose(ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

销毁DrawableDescriptor对象指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* drawableDescriptor | DrawableDescriptor对象指针。 |

### OH\_ArkUI\_DrawableDescriptor\_GetStaticPixelMap()

PhonePC/2in1TabletTVWearable

```
1. OH_PixelmapNativeHandle OH_ArkUI_DrawableDescriptor_GetStaticPixelMap(ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

获取PixelMap图片对象指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* drawableDescriptor | DrawableDescriptor对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_PixelmapNativeHandle](capi-arkui-nativemodule-oh-pixelmapnative8h.md) | [OH\_PixelmapNative](capi-struct.md)对象指针。 |

### OH\_ArkUI\_DrawableDescriptor\_GetAnimatedPixelMapArray()

PhonePC/2in1TabletTVWearable

```
1. OH_PixelmapNativeHandle* OH_ArkUI_DrawableDescriptor_GetAnimatedPixelMapArray(ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

获取用于播放动画的PixelMap图片数组数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* drawableDescriptor | DrawableDescriptor对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_PixelmapNativeHandle](capi-arkui-nativemodule-oh-pixelmapnative8h.md)\* | PixelMap图片数组指针。 |

### OH\_ArkUI\_DrawableDescriptor\_GetAnimatedPixelMapArraySize()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DrawableDescriptor_GetAnimatedPixelMapArraySize(ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

获取用于播放动画的PixelMap图片数组数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* drawableDescriptor | DrawableDescriptor对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | PixelMap图片数组大小。 |

### OH\_ArkUI\_DrawableDescriptor\_SetAnimationDuration()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_DrawableDescriptor_SetAnimationDuration(ArkUI_DrawableDescriptor* drawableDescriptor, int32_t duration)
```

**描述：**

设置PixelMap图片数组播放总时长。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* drawableDescriptor | DrawableDescriptor对象指针。 |
| int32\_t duration | 播放总时长，单位ms。取值范围：[0, +∞)。传入负数时按0处理。 |

### OH\_ArkUI\_DrawableDescriptor\_GetAnimationDuration()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DrawableDescriptor_GetAnimationDuration(ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

获取PixelMap图片数组播放总时长。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* drawableDescriptor | DrawableDescriptor对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 播放总时长，单位ms。 |

### OH\_ArkUI\_DrawableDescriptor\_SetAnimationIteration()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_DrawableDescriptor_SetAnimationIteration(ArkUI_DrawableDescriptor* drawableDescriptor, int32_t iteration)
```

**描述：**

设置PixelMap图片数组播放次数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* drawableDescriptor | DrawableDescriptor对象指针。 |
| int32\_t iteration | 播放次数。取值范围：[0, +∞)，0表示无限循环播放。传入负数时按0处理。 |

### OH\_ArkUI\_DrawableDescriptor\_GetAnimationIteration()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DrawableDescriptor_GetAnimationIteration(ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

获取PixelMap图片数组播放次数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* drawableDescriptor | DrawableDescriptor对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 播放次数。 |

### OH\_ArkUI\_DrawableDescriptor\_SetAnimationFrameDurations()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DrawableDescriptor_SetAnimationFrameDurations(ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t* durations, size_t size)
```

**描述：**

设置动图中的单帧播放时间。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* drawableDescriptor | DrawableDescriptor对象指针。 |
| uint32\_t\* durations | 动图中的单帧播放时间数组，单位ms。  不设置则按照总时间播放。设置的优先级高于[OH\_ArkUI\_DrawableDescriptor\_SetAnimationDuration](capi-drawable-descriptor-h.md#oh_arkui_drawabledescriptor_setanimationduration)，即同时设置了OH\_ArkUI\_DrawableDescriptor\_SetAnimationDuration和OH\_ArkUI\_DrawableDescriptor\_SetAnimationFrameDurations时，OH\_ArkUI\_DrawableDescriptor\_SetAnimationDuration不生效。  数组大小必须与PixelMap图片数组大小相同。  每帧播放时间取值范围：[0, +∞)。默认值：均匀分配总时长。 |
| size\_t size | 数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 输入参数错误。 |

### OH\_ArkUI\_DrawableDescriptor\_GetAnimationFrameDurations()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DrawableDescriptor_GetAnimationFrameDurations(ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t* durations, size_t* size)
```

**描述：**

获取动图中的单帧播放时间。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* drawableDescriptor | DrawableDescriptor对象指针。 |
| uint32\_t\* durations | 动图中的单帧播放时间数组。 |
| size\_t\* size | 数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 输入参数错误。 |

### OH\_ArkUI\_DrawableDescriptor\_SetAnimationAutoPlay()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DrawableDescriptor_SetAnimationAutoPlay(ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t autoPlay)
```

**描述：**

设置动图是否自动播放。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* drawableDescriptor | DrawableDescriptor对象指针。 |
| uint32\_t autoPlay | 是否自动播放。  1表示自动播放，0表示不自动播放。  默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 输入参数错误。 |

### OH\_ArkUI\_DrawableDescriptor\_GetAnimationAutoPlay()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DrawableDescriptor_GetAnimationAutoPlay(ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t* autoPlay)
```

**描述：**

获取动图是否自动播放。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* drawableDescriptor | DrawableDescriptor对象指针。 |
| uint32\_t\* autoPlay | 是否自动播放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 输入参数错误。 |

### OH\_ArkUI\_DrawableDescriptor\_CreateAnimationController()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DrawableDescriptor_CreateAnimationController(ArkUI_DrawableDescriptor* drawableDescriptor, ArkUI_NodeHandle node, ArkUI_DrawableDescriptor_AnimationController** controller)
```

**描述：**

创建动图控制器。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* drawableDescriptor | DrawableDescriptor对象指针。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 组件节点指针。 |
| [ArkUI\_DrawableDescriptor\_AnimationController](module-arkui-drawabledescriptoranimationcontroller.md)\*\* controller | DrawableDescriptor动图控制器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 输入参数错误。 |

### OH\_ArkUI\_DrawableDescriptor\_DisposeAnimationController()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_DrawableDescriptor_DisposeAnimationController(ArkUI_DrawableDescriptor_AnimationController* controller)
```

**描述：**

销毁动图控制器。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor\_AnimationController](module-arkui-drawabledescriptoranimationcontroller.md)\* controller | DrawableDescriptor动图控制器对象指针。 |

### OH\_ArkUI\_DrawableDescriptor\_StartAnimation()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DrawableDescriptor_StartAnimation(ArkUI_DrawableDescriptor_AnimationController* controller);
```

**描述：**

从首帧开始播放。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor\_AnimationController](module-arkui-drawabledescriptoranimationcontroller.md)\* controller | DrawableDescriptor动图控制器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 输入参数错误。 |

### OH\_ArkUI\_DrawableDescriptor\_StopAnimation()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DrawableDescriptor_StopAnimation(ArkUI_DrawableDescriptor_AnimationController* controller);
```

**描述：**

停止动图播放并回到首帧。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor\_AnimationController](module-arkui-drawabledescriptoranimationcontroller.md)\* controller | DrawableDescriptor动图控制器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 输入参数错误。 |

### OH\_ArkUI\_DrawableDescriptor\_ResumeAnimation()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DrawableDescriptor_ResumeAnimation(ArkUI_DrawableDescriptor_AnimationController* controller);
```

**描述：**

从当前帧恢复动图播放。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor\_AnimationController](module-arkui-drawabledescriptoranimationcontroller.md)\* controller | DrawableDescriptor动图控制器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 输入参数错误。 |

### OH\_ArkUI\_DrawableDescriptor\_PauseAnimation()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DrawableDescriptor_PauseAnimation(ArkUI_DrawableDescriptor_AnimationController* controller);
```

**描述：**

暂停动图的播放，保持在当前帧。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor\_AnimationController](module-arkui-drawabledescriptoranimationcontroller.md)\* controller | DrawableDescriptor动图控制器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 输入参数错误。 |

### OH\_ArkUI\_DrawableDescriptor\_GetAnimationStatus()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DrawableDescriptor_GetAnimationStatus(ArkUI_DrawableDescriptor_AnimationController* controller, DrawableDescriptor_AnimationStatus* status);
```

**描述：**

获取动图的播放状态。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor\_AnimationController](module-arkui-drawabledescriptoranimationcontroller.md)\* controller | DrawableDescriptor动图控制器对象指针。 |
| [DrawableDescriptor\_AnimationStatus](capi-drawable-descriptor-h.md#drawabledescriptor_animationstatus)\* status | DrawableDescriptor动图的播放状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 输入参数错误。 |
