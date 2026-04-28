---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativegestureapi-1
title: ArkUI_NativeGestureAPI_1
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_NativeGestureAPI_1
category: harmonyos-references
scraped_at: 2026-04-28T08:04:07+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:d0d8c4279ca7409a61fcd3803f0933982234b35e8cb09b1a8782beac88a551cd
---

```
1. typedef struct {...} ArkUI_NativeGestureAPI_1
```

## 概述

PhonePC/2in1TabletTVWearable

手势模块接口集合。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_gesture.h](capi-native-gesture-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t version | 结构版本号 = 1。 |

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer\* (\*createTapGesture)(int32\_t countNum, int32\_t fingersNum)](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#createtapgesture) | 创建敲击手势。1. 支持单击、双击和多次点击事件的识别。  2. 当配置多击时，上一次的最后一根手指抬起和下一次的第一根手指按下的超时时间为300毫秒。  3. 当上次点击的位置与当前点击的位置距离超过60vp等效像素点时，手势识别失败。  4. 当配置多指时，第一根手指按下后300毫秒内未有足够的手指数按下，手势识别失败，  第一根手指抬起后300毫秒内未有足够的手指抬起，手势识别失败。  5. 实际点击手指数超过配置值，手势识别成功。 |
| [ArkUI\_GestureRecognizer\* (\*createLongPressGesture)(int32\_t fingersNum, bool repeatResult, int32\_t durationNum)](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#createlongpressgesture) | 创建长按手势。1. 用于触发长按手势事件，触发长按手势的最少手指数为1，最短长按时间为500毫秒。  2. 当组件默认支持可拖拽时，如Text、TextInput、TextArea、HyperLink、Image和RichEditor等组件。  长按手势与拖拽会出现冲突，事件优先级如下：  长按触发时间 < 500ms，长按事件优先拖拽事件响应。  长按触发时间 >= 500ms，拖拽事件优先长按事件响应。  3. 手指按下后若发生超过15px的移动，则判定当前长按手势识别失败。 |
| [ArkUI\_GestureRecognizer\* (\*createPanGesture)(int32\_t fingersNum, ArkUI\_GestureDirectionMask directions, double distanceNum)](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#createpangesture) | 创建滑动手势。1. 当滑动的最小距离超过设定的最小值时触发滑动手势事件。  2. Tabs组件滑动与该滑动手势事件同时存在时，可将distanceNum值设为1，使拖动更灵敏，避免造成事件错乱。 |
| [ArkUI\_GestureRecognizer\* (\*createPinchGesture)(int32\_t fingersNum, double distanceNum)](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#createpinchgesture) | 创建捏合手势。1. 触发捏合手势的最少手指为2指，最大为5指，最小识别距离为distanceNum 像素点。  2. 触发手势手指可以多于fingersNum数目，但只有先落下的与fingersNum相同数目的手指参与手势计算。 |
| [ArkUI\_GestureRecognizer\* (\*createRotationGesture)(int32\_t fingersNum, double angleNum)](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#createrotationgesture) | 创建旋转手势。1. 触发旋转手势的最少手指为2指，最大为5指，最小改变度数为1度。  2. 触发手势手指可以多于fingersNum数目，但只有先落下的两指参与手势计算。 |
| [ArkUI\_GestureRecognizer\* (\*createSwipeGesture)(int32\_t fingersNum, ArkUI\_GestureDirectionMask directions, double speedNum)](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#createswipegesture) | 创建快滑手势。1. 用于触发快滑事件，滑动速度大于speedNum px/s时可识别成功。 |
| [ArkUI\_GestureRecognizer\* (\*createGroupGesture)(ArkUI\_GroupGestureMode gestureMode)](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#creategroupgesture) | 创建手势组。 |
| [void (\*dispose)(ArkUI\_GestureRecognizer\* recognizer)](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#dispose) | 销毁手势，释放资源。 |
| [int32\_t (\*addChildGesture)(ArkUI\_GestureRecognizer\* group, ArkUI\_GestureRecognizer\* child)](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#addchildgesture) | 手势组增加子手势。 |
| [int32\_t (\*removeChildGesture)(ArkUI\_GestureRecognizer\* group, ArkUI\_GestureRecognizer\* child)](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#removechildgesture) | 删除子手势。 |
| [int32\_t (\*setGestureEventTarget)(ArkUI\_GestureRecognizer\* recognizer, ArkUI\_GestureEventActionTypeMask actionTypeMask, void\* extraParams,void (\*targetReceiver)(ArkUI\_GestureEvent\* event, void\* extraParams))](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#setgestureeventtarget) | 创建手势关联回调方法。 |
| [int32\_t (\*addGestureToNode)(ArkUI\_NodeHandle node, ArkUI\_GestureRecognizer\* recognizer, ArkUI\_GesturePriority mode, ArkUI\_GestureMask mask)](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#addgesturetonode) | 将手势添加到UI组件。 |
| [int32\_t (\*removeGestureFromNode)(ArkUI\_NodeHandle node, ArkUI\_GestureRecognizer\* recognizer)](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#removegesturefromnode) | 在节点中移除手势。 |
| [int32\_t (\*setGestureInterrupterToNode)(ArkUI\_NodeHandle node, ArkUI\_GestureInterruptResult (\*interrupter)(ArkUI\_GestureInterruptInfo\* info))](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#setgestureinterruptertonode) | 设置节点手势打断回调。 |
| [ArkUI\_GestureRecognizerType (\*getGestureType)(ArkUI\_GestureRecognizer\* recognizer)](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#getgesturetype) | 获取手势类别。 |
| [int32\_t (\*setInnerGestureParallelTo)(ArkUI\_NodeHandle node, void\* userData, ArkUI\_GestureRecognizer\* (\*parallelInnerGesture)(ArkUI\_ParallelInnerGestureEvent\* event))](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#setinnergestureparallelto) | 设置并行内部手势事件回调。 |
| [ArkUI\_GestureRecognizer\* (\*createTapGestureWithDistanceThreshold)(int32\_t countNum, int32\_t fingersNum, double distanceThreshold)](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#createtapgesturewithdistancethreshold) | 创建带移动范围限制的敲击手势。1. 支持单击、双击和多次点击事件的识别。  2. 当配置多击时，上一次的最后一根手指抬起和下一次的第一根手指按下的超时时间为300毫秒。  3. 当上次点击的位置与当前点击的位置距离超过60vp等效像素点时，手势识别失败。  4. 当配置多指时，第一根手指按下后300毫秒内未有足够的手指数按下，手势识别失败，  第一根手指抬起后300毫秒内未有足够的手指抬起，手势识别失败。  5. 实际点击手指数超过配置值，手势识别成功。  6. 当手指移动距离超出所设置的距离值时，手势识别失败。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### createTapGesture()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_GestureRecognizer* (*createTapGesture)(int32_t countNum, int32_t fingersNum)
```

**描述：**

创建敲击手势。

1. 支持单击、双击和多次点击事件的识别。
2. 当配置多击时，上一次的最后一根手指抬起和下一次的第一根手指按下的超时时间为300毫秒。
3. 当上次点击的位置与当前点击的位置距离超过60vp等效像素点时，手势识别失败。
4. 当配置多指时，第一根手指按下后300毫秒内未有足够的手指数按下，手势识别失败，第一根手指抬起后300毫秒内未有足够的手指抬起，手势识别失败。
5. 实际点击手指数超过配置值，手势识别成功。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t countNum | 识别的连续点击次数。当设置的值小于1或不设置时，会被转化为默认值 1。 |
| int32\_t fingersNum | 触发点击的手指数，最小为1指， 最大为10指。当设置小于1的值或不设置时，会被转化为默认值 1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* | 返回创建的敲击手势指针。 |

### createLongPressGesture()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_GestureRecognizer* (*createLongPressGesture)(int32_t fingersNum, bool repeatResult, int32_t durationNum)
```

**描述：**

创建长按手势。

1. 用于触发长按手势事件，触发长按手势的最少手指数为1，最短长按时间为500毫秒。
2. 当组件默认支持可拖拽时，如Text、TextInput、TextArea、HyperLink、Image和RichEditor等组件。

   长按手势与拖拽会出现冲突，事件优先级如下：

   长按触发时间 < 500ms，长按事件优先拖拽事件响应。

   长按触发时间 >= 500ms，拖拽事件优先长按事件响应。
3. 手指按下后若发生超过15px的移动，则判定当前长按手势识别失败。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t fingersNum | 触发长按的最少手指数，最小为1指，最大取值为10指。超出取值范围时按照默认值1处理。 |
| bool repeatResult | 是否连续触发事件回调。  true：连续触发；false：不连续触发。 |
| int32\_t durationNum | 触发长按的最短时间，单位为毫秒（ms）。设置小于等于0时，按照默认值500处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* | 返回创建的敲击手势指针。 |

### createPanGesture()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_GestureRecognizer* (*createPanGesture)(int32_t fingersNum, ArkUI_GestureDirectionMask directions, double distanceNum)
```

**描述：**

创建滑动手势。

1. 当滑动的最小距离超过设定的最小值时触发滑动手势事件。
2. Tabs组件滑动与该滑动手势事件同时存在时，可将distanceNum值设为1，使拖动更灵敏，避免造成事件错乱。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t fingersNum | 用于指定触发滑动的最少手指数，最小为1指，最大取值为10指。当设置的值小于1或不设置时，会被转化为默认值 1。 |
| [ArkUI\_GestureDirectionMask](capi-native-gesture-h.md#变量) directions | 用于指定触发滑动的手势方向，此枚举值支持逻辑与(&)和逻辑或（|）运算。 |
| double distanceNum | 用于指定触发滑动手势事件的最小拖动距离，单位为px。当设定的值小于等于0时，按默认值5px处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* | 返回创建的滑动手势指针。 |

### createPinchGesture()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_GestureRecognizer* (*createPinchGesture)(int32_t fingersNum, double distanceNum)
```

**描述：**

创建捏合手势。

1. 触发捏合手势的最少手指为2指，最大为5指，最小识别距离为distanceNum 像素点。
2. 触发手势手指可以多于fingersNum数目，但只有先落下的与fingersNum相同数目的手指参与手势计算。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t fingersNum | 触发捏合的最少手指数，最小为2指，最大为5指。超出取值范围时按照默认值2处理。 |
| double distanceNum | 最小识别距离，单位为px。当设置识别距离的值小于等于0时，会被转化为默认值5px处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* | 返回创建的手势指针。 |

### createRotationGesture()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_GestureRecognizer* (*createRotationGesture)(int32_t fingersNum, double angleNum)
```

**描述：**

创建旋转手势。

1. 触发旋转手势的最少手指为2指，最大为5指，最小改变度数为1度。
2. 触发手势手指可以多于fingersNum数目，但只有先落下的两指参与手势计算。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t fingersNum | 触发旋转的最少手指数，最小为2指，最大为5指。超出取值范围时按照默认值2处理。 |
| double angleNum | 触发旋转手势的最小改变度数，单位为deg。默认值：1。当改变度数的值小于等于0或大于360时，会被转化为默认值 1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* | 返回创建的手势指针。 |

### createSwipeGesture()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_GestureRecognizer* (*createSwipeGesture)(int32_t fingersNum, ArkUI_GestureDirectionMask directions, double speedNum)
```

**描述：**

创建快滑手势。

1. 用于触发快滑事件，滑动速度大于speedNum px/s时可识别成功。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t fingersNum | 触发滑动的最少手指数，默认为1，最小为1指，最大为10指。 |
| [ArkUI\_GestureDirectionMask](capi-native-gesture-h.md#变量) directions | 触发快滑手势的滑动方向。 |
| double speedNum | 识别滑动的最小速度，单位 px/s。当设置滑动速度的值小于等于0时，会被转化为默认值100px/s。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* | 返回创建的手势指针。 |

### createGroupGesture()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_GestureRecognizer* (*createGroupGesture)(ArkUI_GroupGestureMode gestureMode)
```

**描述：**

创建手势组。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GroupGestureMode](capi-native-gesture-h.md#arkui_groupgesturemode) gestureMode | 手势组模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* | 返回创建的手势组指针。 |

### dispose()

PhonePC/2in1TabletTVWearable

```
1. void (*dispose)(ArkUI_GestureRecognizer* recognizer)
```

**描述：**

销毁手势，释放资源。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 需要销毁的手势的指针。 |

### addChildGesture()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*addChildGesture)(ArkUI_GestureRecognizer* group, ArkUI_GestureRecognizer* child)
```

**描述：**

手势组增加子手势。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* group | 需要被关联子手势的手势组。 |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* child | 子手势。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 参数错误。比如添加手势到非手势组对象内。 |

### removeChildGesture()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*removeChildGesture)(ArkUI_GestureRecognizer* group, ArkUI_GestureRecognizer* child)
```

**描述：**

删除子手势。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* group | 需要被删除子手势的手势组。 |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* child | 子手势。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 参数错误。 |

### setGestureEventTarget()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*setGestureEventTarget)(ArkUI_GestureRecognizer* recognizer, ArkUI_GestureEventActionTypeMask actionTypeMask, void* extraParams,void (*targetReceiver)(ArkUI_GestureEvent* event, void* extraParams))
```

**描述：**

创建手势关联回调方法。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 需要被绑定回调事件的各类手势指针。 |
| [ArkUI\_GestureEventActionTypeMask](capi-native-gesture-h.md#变量) actionTypeMask | 需要相应的手势事件类型集合，一次性可以注册多个回调，在回调中区分回调事件类型。例：actionTypeMask = GESTURE\_EVENT\_ACTION\_ACCEPT | GESTURE\_EVENT\_ACTION\_UPDATE; |
| void\* extraParams | targetReceiver 回调时传入的上下文数据。 |
| targetReceiver | 对应注册手势类型的事件回调处理， event 返回手势回调数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 参数错误。 |

### addGestureToNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*addGestureToNode)(ArkUI_NodeHandle node, ArkUI_GestureRecognizer* recognizer, ArkUI_GesturePriority mode, ArkUI_GestureMask mask)
```

**描述：**

将手势添加到UI组件。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 需要被绑定手势的ArkUI组件节点指针。 |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 绑定此节点的手势。 |
| [ArkUI\_GesturePriority](capi-native-gesture-h.md#arkui_gesturepriority) mode | 标识此手势的模式。 |
| [ArkUI\_GestureMask](capi-native-gesture-h.md#arkui_gesturemask) mask | 手势屏蔽模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 参数错误。 |

### removeGestureFromNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*removeGestureFromNode)(ArkUI_NodeHandle node, ArkUI_GestureRecognizer* recognizer)
```

**描述：**

在节点中移除手势。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 需要被移除手势的节点指针。 |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 需要被移除的手势。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 参数错误。 |

### setGestureInterrupterToNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*setGestureInterrupterToNode)(ArkUI_NodeHandle node, ArkUI_GestureInterruptResult (*interrupter)(ArkUI_GestureInterruptInfo* info))
```

**描述：**

设置节点手势打断回调。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 需要被设置手势打断回调的ArkUI节点指针。 |
| [ArkUI\_GestureInterruptResult](capi-native-gesture-h.md#arkui_gestureinterruptresult) (\*interrupter)([ArkUI\_GestureInterruptInfo](capi-arkui-nativemodule-arkui-gestureinterruptinfo.md)\* info) | 打断回调，info返回手势打断数据。interrupter返回GESTURE\_INTERRUPT\_RESULT\_CONTINUE，手势正常进行；返回GESTURE\_INTERRUPT\_RESULT\_REJECT，手势打断。设置此参数为nullptr时将取消注册回调函数。  **说明：** 该事件中断回调注册后，后续在单次手势处理流程中都会存在。即使在单次事件处理流程中使用setGestureInterrupterToNode接口将手势打断回调重置为undefined，或者使用[dispose](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#dispose)接口使即将被触发的手势销毁，该回调在满足触发条件后仍会响应。如果在该回调中使用到的对象，在回调触发前已被释放，需要对该对象进行保护。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 参数错误。 |

### getGestureType()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_GestureRecognizerType (*getGestureType)(ArkUI_GestureRecognizer* recognizer)
```

**描述：**

获取手势类别。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GestureRecognizerType](capi-native-gesture-h.md#arkui_gesturerecognizertype) | 手势类型。 |

### setInnerGestureParallelTo()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*setInnerGestureParallelTo)(ArkUI_NodeHandle node, void* userData, ArkUI_GestureRecognizer* (*parallelInnerGesture)(ArkUI_ParallelInnerGestureEvent* event))
```

**描述：**

设置并行内部手势事件回调。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 需要被设置并行内部手势事件回调的ArkUI节点指针。 |
| void\* userData | 用户自定义数据。 |
| parallelInnerGesture | 并行内部手势事件，event 返回并行内部手势事件数据。parallelInnerGesture 返回 需要并行的手势识别器指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 参数错误。 |

### createTapGestureWithDistanceThreshold()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_GestureRecognizer* (*createTapGestureWithDistanceThreshold)(int32_t countNum, int32_t fingersNum, double distanceThreshold)
```

**描述：**

创建带移动范围限制的敲击手势。

1. 支持单击、双击和多次点击事件的识别。
2. 当配置多击时，上一次的最后一根手指抬起和下一次的第一根手指按下的超时时间为300毫秒。
3. 当上次点击的位置与当前点击的位置距离超过60vp等效像素点时，手势识别失败。
4. 当配置多指时，第一根手指按下后300毫秒内未有足够的手指数按下，手势识别失败，第一根手指抬起后300毫秒内未有足够的手指抬起，手势识别失败。
5. 实际点击手指数超过配置值，手势识别成功。
6. 当手指移动距离超出所设置的距离值时，手势识别失败。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t countNum | 识别的连续点击次数。当设置的值小于1或不设置时，会被转化为默认值 1。 |
| int32\_t fingersNum | 触发点击的手指数，最小为1指， 最大为10指。当设置小于1的值或不设置时，会被转化为默认值 1。 |
| double distanceThreshold | 手指允许的移动距离范围。当设置的值小于0或者不设置时，会被转化为默认值无穷大。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* | 返回创建的敲击手势指针。 |
