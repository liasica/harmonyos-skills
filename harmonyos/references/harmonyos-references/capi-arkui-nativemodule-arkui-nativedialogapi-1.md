---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1
title: ArkUI_NativeDialogAPI_1
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_NativeDialogAPI_1
category: harmonyos-references
scraped_at: 2026-04-28T08:04:05+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:3850f59b16a797dac17928a413d8d423471f8323ba75761d0302e5c93a1471bb
---

```
1. typedef struct {...} ArkUI_NativeDialogAPI_1
```

## 概述

PhonePC/2in1TabletTVWearable

ArkUI提供的Native侧自定义弹窗接口集合。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_dialog.h](capi-native-dialog-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle (\*create)()](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#create) | 创建自定义弹窗并返回指向自定义弹窗的指针。 |
| [void (\*dispose)(ArkUI\_NativeDialogHandle handle)](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#dispose) | 销毁自定义弹窗。 |
| [int32\_t (\*setContent)(ArkUI\_NativeDialogHandle handle, ArkUI\_NodeHandle content)](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#setcontent) | 挂载自定义弹窗内容。 |
| [int32\_t (\*removeContent)(ArkUI\_NativeDialogHandle handle)](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#removecontent) | 卸载自定义弹窗内容。 |
| [int32\_t (\*setContentAlignment)(ArkUI\_NativeDialogHandle handle, int32\_t alignment, float offsetX, float offsetY)](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#setcontentalignment) | 设置自定义弹窗对齐方式。 |
| [int32\_t (\*resetContentAlignment)(ArkUI\_NativeDialogHandle handle)](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#resetcontentalignment) | 重置setContentAlignment方法设置的属性，使用系统默认的对齐方式。 |
| [int32\_t (\*setModalMode)(ArkUI\_NativeDialogHandle handle, bool isModal)](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#setmodalmode) | 设置自定义弹窗是否开启模态样式的弹窗。 |
| [int32\_t (\*setAutoCancel)(ArkUI\_NativeDialogHandle handle, bool autoCancel)](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#setautocancel) | 设置自定义弹窗是否允许通过点击遮罩层退出。 |
| [int32\_t (\*setMask)(ArkUI\_NativeDialogHandle handle, uint32\_t maskColor, const ArkUI\_Rect\* maskRect)](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#setmask) | 设置自定义弹窗遮罩属性。 |
| [int32\_t (\*setBackgroundColor)(ArkUI\_NativeDialogHandle handle, uint32\_t backgroundColor)](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#setbackgroundcolor) | 设置弹窗背景色。 |
| [int32\_t (\*setCornerRadius)(ArkUI\_NativeDialogHandle handle, float topLeft, float topRight,float bottomLeft, float bottomRight)](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#setcornerradius) | 设置弹窗背板圆角半径。 |
| [int32\_t (\*setGridColumnCount)(ArkUI\_NativeDialogHandle handle, int32\_t gridCount)](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#setgridcolumncount) | 设置弹窗宽度占栅格宽度的个数。 |
| [int32\_t (\*enableCustomStyle)(ArkUI\_NativeDialogHandle handle, bool enableCustomStyle)](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#enablecustomstyle) | 弹窗容器样式是否可以自定义。 |
| [int32\_t (\*enableCustomAnimation)(ArkUI\_NativeDialogHandle handle, bool enableCustomAnimation)](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#enablecustomanimation) | 弹窗容器是否使用自定义弹窗动画。 |
| [int32\_t (\*registerOnWillDismiss)(ArkUI\_NativeDialogHandle handle, ArkUI\_OnWillDismissEvent eventHandler)](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#registeronwilldismiss) | 当触发系统定义的返回操作、键盘ESC关闭交互操作时，如果注册了该回调函数，弹窗不会立即关闭，而是由用户决定是否关闭。 |
| [int32\_t (\*show)(ArkUI\_NativeDialogHandle handle, bool showInSubWindow)](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show) | 显示自定义弹窗。 |
| [int32\_t (\*close)(ArkUI\_NativeDialogHandle handle)](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#close) | 关闭自定义弹窗，如已关闭，则不生效。该接口后台执行是异步的，在关闭动画执行完成后弹窗节点才会下树。如需关闭后再次打开弹窗，请在延迟300ms以后再执行。 |
| [int32\_t (\*registerOnWillDismissWithUserData)(ArkUI\_NativeDialogHandle handle, void\* userData, void (\*callback)(ArkUI\_DialogDismissEvent\* event))](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#registeronwilldismisswithuserdata) | 注册系统关闭自定义弹窗的监听事件。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NativeDialogHandle (*create)()
```

**描述：**

创建自定义弹窗并返回指向自定义弹窗的指针。

说明

create方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) | 返回指向自定义弹窗的指针，如果创建失败，则返回空指针。 |

### dispose()

PhonePC/2in1TabletTVWearable

```
1. void (*dispose)(ArkUI_NativeDialogHandle handle)
```

**描述：**

销毁自定义弹窗。

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |

### setContent()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*setContent)(ArkUI_NativeDialogHandle handle, ArkUI_NodeHandle content)
```

**描述：**

挂载自定义弹窗内容。

说明

setContent方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) content | 弹窗内容根节点指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### removeContent()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*removeContent)(ArkUI_NativeDialogHandle handle)
```

**描述：**

卸载自定义弹窗内容。

说明

removeContent方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### setContentAlignment()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*setContentAlignment)(ArkUI_NativeDialogHandle handle, int32_t alignment, float offsetX, float offsetY)
```

**描述：**

设置自定义弹窗对齐方式。

说明

setContentAlignment方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| int32\_t alignment | 对齐方式，参数类型[ArkUI\_Alignment](capi-native-type-h.md#arkui_alignment)。 |
| float offsetX | 弹窗的水平偏移量，浮点型，单位：vp。 |
| float offsetY | 弹窗的垂直偏移量，浮点型，单位：vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### resetContentAlignment()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*resetContentAlignment)(ArkUI_NativeDialogHandle handle)
```

**描述：**

重置setContentAlignment方法设置的属性，使用系统默认的对齐方式，默认值：ARKUI\_ALIGNMENT\_TOP\_START，参考[ArkUI\_Alignment](capi-native-type-h.md#arkui_alignment)。

说明

resetContentAlignment方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### setModalMode()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*setModalMode)(ArkUI_NativeDialogHandle handle, bool isModal)
```

**描述：**

设置自定义弹窗是否开启模态样式的弹窗。

说明

setModalMode方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| bool isModal | 设置是否开启模态窗口，模态窗口有蒙层，非模态窗口无蒙层。为true时开启模态窗口，为false时不开启模态窗口。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### setAutoCancel()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*setAutoCancel)(ArkUI_NativeDialogHandle handle, bool autoCancel)
```

**描述：**

设置自定义弹窗是否允许通过点击遮罩层退出。

说明

setAutoCancel方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| bool autoCancel | 设置是否允许通过点击遮罩层退出，true表示关闭弹窗，false表示不关闭弹窗。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### setMask()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*setMask)(ArkUI_NativeDialogHandle handle, uint32_t maskColor, const ArkUI_Rect* maskRect)
```

**描述：**

设置自定义弹窗遮罩属性。

说明

setMask方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| uint32\_t maskColor | 设置遮罩颜色，0xargb格式。 |
| const [ArkUI\_Rect](capi-arkui-nativemodule-arkui-rect.md)\* maskRect | 遮蔽层区域范围的指针，遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。参数类型[ArkUI\_Rect](capi-arkui-nativemodule-arkui-rect.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### setBackgroundColor()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*setBackgroundColor)(ArkUI_NativeDialogHandle handle, uint32_t backgroundColor)
```

**描述：**

设置弹窗背景色。

说明

setBackgroundColor方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| uint32\_t backgroundColor | 设置弹窗背景颜色，0xargb格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### setCornerRadius()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*setCornerRadius)(ArkUI_NativeDialogHandle handle, float topLeft, float topRight,float bottomLeft, float bottomRight)
```

**描述：**

设置弹窗背板圆角半径。

说明

setCornerRadius方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| float topLeft | 设置弹窗背板左上角圆角半径，单位：vp。默认值：从API version 12开始，为32vp。API version 11及之前版本，为24vp。 |
| float topRight | 设置弹窗背板右上角圆角半径，单位：vp。默认值：从API version 12开始，为32vp。API version 11及之前版本，为24vp。 |
| float bottomLeft | 设置弹窗背板左下圆角半径，单位：vp。默认值：从API version 12开始，为32vp。API version 11及之前版本，为24vp。 |
| float bottomRight | 设置弹窗背板右下角圆角半径，单位：vp。默认值：从API version 12开始，为32vp。API version 11及之前版本，为24vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### setGridColumnCount()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*setGridColumnCount)(ArkUI_NativeDialogHandle handle, int32_t gridCount)
```

**描述：**

设置弹窗宽度占栅格宽度的个数。

说明

setGridColumnCount方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| int32\_t gridCount | 默认为按照窗口大小自适应，最大栅格数为[系统最大栅格数](../harmonyos-guides/arkts-layout-development-grid-layout.md#布局的总列数)。  取值范围：大于等于0的整数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### enableCustomStyle()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*enableCustomStyle)(ArkUI_NativeDialogHandle handle, bool enableCustomStyle)
```

**描述：**

弹窗容器样式是否可以自定义。

说明

enableCustomStyle方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| bool enableCustomStyle | 弹窗容器样式是否可以自定义。  默认值：false  true：弹窗容器样式不能自定义，宽度自适应子节点，圆角为0，弹窗背景色透明；false：弹窗容器样式可以自定义，高度自适应子节点，宽度由栅格系统定义，圆角半径24vp，PC/2in1设备避让屏幕边缘以及窗口标题栏。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### enableCustomAnimation()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*enableCustomAnimation)(ArkUI_NativeDialogHandle handle, bool enableCustomAnimation)
```

**描述：**

弹窗容器是否使用自定义弹窗动画。

说明

enableCustomAnimation方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| bool enableCustomAnimation | true:使用自定义动画，关闭系统默认动画；false:使用系统默认动画。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### registerOnWillDismiss()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*registerOnWillDismiss)(ArkUI_NativeDialogHandle handle, ArkUI_OnWillDismissEvent eventHandler)
```

**描述：**

当触发系统定义的返回操作、键盘ESC关闭交互操作时，如果注册了该回调函数，弹窗不会立即关闭，而是由用户决定是否关闭。

说明

registerOnWillDismiss方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| [ArkUI\_OnWillDismissEvent](capi-native-dialog-h.md#arkui_onwilldismissevent) eventHandler | 弹窗关闭的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### show()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*show)(ArkUI_NativeDialogHandle handle, bool showInSubWindow)
```

**描述：**

显示自定义弹窗。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| bool showInSubWindow | 是否在子窗口显示弹窗。true表示在子窗显示弹窗。false表示不在子窗显示弹窗。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### close()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*close)(ArkUI_NativeDialogHandle handle)
```

**描述：**

关闭自定义弹窗，如已关闭，则不生效。该接口后台执行是异步的，在关闭动画执行完成后弹窗节点才会下树。如需关闭后再次打开弹窗，请在延迟300ms以后再执行。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。此时仅表示关闭指令下发成功，不代表弹窗完全关闭。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### registerOnWillDismissWithUserData()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*registerOnWillDismissWithUserData)(ArkUI_NativeDialogHandle handle, void* userData, void (*callback)(ArkUI_DialogDismissEvent* event))
```

**描述：**

注册系统关闭自定义弹窗的监听事件。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| void\* userData | 用户自定义数据指针。 |
| callback | 监听自定义弹窗关闭的回调事件。  - event: 回调函数的入参，捕获关闭原因。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |
