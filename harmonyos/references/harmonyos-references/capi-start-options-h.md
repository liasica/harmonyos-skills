---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-start-options-h
title: start_options.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > start_options.h
category: harmonyos-references
scraped_at: 2026-04-28T07:58:59+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:5e90606f75a1fe87332e889c21c5a2a549f8a56c6f64ec34b2846db6c8560301
---

## 概述

PhonePC/2in1TabletTVWearable

提供应用启动参数数据结构[AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md)以及设置和获取相关函数。

**引用文件：** <AbilityKit/ability\_runtime/start\_options.h>

**库：** libability\_runtime.so

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 17

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) | AbilityRuntime\_StartOptions | StartOptions数据结构。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions\* OH\_AbilityRuntime\_CreateStartOptions(void)](capi-start-options-h.md#oh_abilityruntime_createstartoptions) | 创建AbilityRuntime\_StartOptions对象。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_DestroyStartOptions(AbilityRuntime\_StartOptions \*\*startOptions)](capi-start-options-h.md#oh_abilityruntime_destroystartoptions) | 销毁AbilityRuntime\_StartOptions对象。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowMode(AbilityRuntime\_StartOptions \*startOptions,AbilityRuntime\_WindowMode windowMode)](capi-start-options-h.md#oh_abilityruntime_setstartoptionswindowmode) | 设置启动Ability时的窗口模式。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowMode(AbilityRuntime\_StartOptions \*startOptions,AbilityRuntime\_WindowMode &windowMode)](capi-start-options-h.md#oh_abilityruntime_getstartoptionswindowmode) | 获取启动Ability时的窗口模式。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsDisplayId(AbilityRuntime\_StartOptions \*startOptions,int32\_t displayId)](capi-start-options-h.md#oh_abilityruntime_setstartoptionsdisplayid) | 设置启动Ability时窗口所在的屏幕ID。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsDisplayId(AbilityRuntime\_StartOptions \*startOptions,int32\_t &displayId)](capi-start-options-h.md#oh_abilityruntime_getstartoptionsdisplayid) | 获取启动Ability时窗口所在的屏幕ID。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWithAnimation(AbilityRuntime\_StartOptions \*startOptions,bool withAnimation)](capi-start-options-h.md#oh_abilityruntime_setstartoptionswithanimation) | 设置启动Ability时是否具有动画效果。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWithAnimation(AbilityRuntime\_StartOptions \*startOptions,bool &withAnimation)](capi-start-options-h.md#oh_abilityruntime_getstartoptionswithanimation) | 获取启动Ability时是否具有动画效果。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowLeft(AbilityRuntime\_StartOptions \*startOptions,int32\_t windowLeft)](capi-start-options-h.md#oh_abilityruntime_setstartoptionswindowleft) | 设置启动Ability时的窗口左侧位置，单位为px。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowLeft(AbilityRuntime\_StartOptions \*startOptions,int32\_t &windowLeft)](capi-start-options-h.md#oh_abilityruntime_getstartoptionswindowleft) | 获取启动Ability时的窗口左侧位置，单位为px。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowTop(AbilityRuntime\_StartOptions \*startOptions,int32\_t windowTop)](capi-start-options-h.md#oh_abilityruntime_setstartoptionswindowtop) | 设置启动Ability时的窗口顶部位置，单位为px。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowTop(AbilityRuntime\_StartOptions \*startOptions,int32\_t &windowTop)](capi-start-options-h.md#oh_abilityruntime_getstartoptionswindowtop) | 获取启动Ability时的窗口顶部位置，单位为px。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowHeight(AbilityRuntime\_StartOptions \*startOptions,int32\_t windowHeight)](capi-start-options-h.md#oh_abilityruntime_setstartoptionswindowheight) | 设置启动Ability时的窗口高度，单位为px。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowHeight(AbilityRuntime\_StartOptions \*startOptions,int32\_t &windowHeight)](capi-start-options-h.md#oh_abilityruntime_getstartoptionswindowheight) | 获取启动Ability时的窗口高度，单位为px。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowWidth(AbilityRuntime\_StartOptions \*startOptions,int32\_t windowWidth)](capi-start-options-h.md#oh_abilityruntime_setstartoptionswindowwidth) | 设置启动Ability时的窗口宽度，单位为px。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowWidth(AbilityRuntime\_StartOptions \*startOptions,int32\_t &windowWidth)](capi-start-options-h.md#oh_abilityruntime_getstartoptionswindowwidth) | 获取启动Ability时的窗口宽度，单位为px。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsStartVisibility(AbilityRuntime\_StartOptions \*startOptions,AbilityRuntime\_StartVisibility startVisibility)](capi-start-options-h.md#oh_abilityruntime_setstartoptionsstartvisibility) | 设置启动Ability时窗口和dock栏图标的显示模式。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsStartVisibility(AbilityRuntime\_StartOptions \*startOptions,AbilityRuntime\_StartVisibility &startVisibility)](capi-start-options-h.md#oh_abilityruntime_getstartoptionsstartvisibility) | 获取启动Ability时窗口和dock栏图标的显示模式。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsStartWindowIcon(AbilityRuntime\_StartOptions \*startOptions,OH\_PixelmapNative \*startWindowIcon)](capi-start-options-h.md#oh_abilityruntime_setstartoptionsstartwindowicon) | 设置启动Ability时的窗口启动图标。图片数据大小限制为600M。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsStartWindowIcon(AbilityRuntime\_StartOptions \*startOptions,OH\_PixelmapNative \*\*startWindowIcon)](capi-start-options-h.md#oh_abilityruntime_getstartoptionsstartwindowicon) | 获取启动Ability时的窗口启动图标。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsStartWindowBackgroundColor(AbilityRuntime\_StartOptions \*startOptions, const char \*startWindowBackgroundColor)](capi-start-options-h.md#oh_abilityruntime_setstartoptionsstartwindowbackgroundcolor) | 设置启动Ability时的窗口背景颜色。如果未设置该字段，则默认采用module.json5配置文件中abilities标签的startWindowBackground字段的配置。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsStartWindowBackgroundColor(AbilityRuntime\_StartOptions \*startOptions, char \*\*startWindowBackgroundColor, size\_t &size)](capi-start-options-h.md#oh_abilityruntime_getstartoptionsstartwindowbackgroundcolor) | 获取启动Ability时的窗口背景颜色。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsSupportedWindowModes(AbilityRuntime\_StartOptions \*startOptions, AbilityRuntime\_SupportedWindowMode \*supportedWindowModes,size\_t size)](capi-start-options-h.md#oh_abilityruntime_setstartoptionssupportedwindowmodes) | 设置启动Ability时的组件所支持的窗口模式。如果未配置该字段，则默认采用该UIAbility对应的module.json5配置文件中abilities标签的supportWindowMode字段取值。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsSupportedWindowModes(AbilityRuntime\_StartOptions \*startOptions, AbilityRuntime\_SupportedWindowMode \*\*supportedWindowModes,size\_t &size)](capi-start-options-h.md#oh_abilityruntime_getstartoptionssupportedwindowmodes) | 获取启动Ability时的组件所支持的窗口模式。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsMinWindowWidth(AbilityRuntime\_StartOptions \*startOptions, int32\_t minWindowWidth)](capi-start-options-h.md#oh_abilityruntime_setstartoptionsminwindowwidth) | 设置启动Ability时的窗口最小宽度，单位为vp。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsMinWindowWidth(AbilityRuntime\_StartOptions \*startOptions, int32\_t &minWindowWidth)](capi-start-options-h.md#oh_abilityruntime_getstartoptionsminwindowwidth) | 获取启动Ability时的窗口最小宽度，单位为vp。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsMaxWindowWidth(AbilityRuntime\_StartOptions \*startOptions, int32\_t maxWindowWidth)](capi-start-options-h.md#oh_abilityruntime_setstartoptionsmaxwindowwidth) | 设置启动Ability时的窗口最大宽度，单位为vp。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsMaxWindowWidth(AbilityRuntime\_StartOptions \*startOptions, int32\_t &maxWindowWidth)](capi-start-options-h.md#oh_abilityruntime_getstartoptionsmaxwindowwidth) | 获取启动Ability时的窗口最大宽度，单位为vp。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsMinWindowHeight(AbilityRuntime\_StartOptions \*startOptions, int32\_t minWindowHeight)](capi-start-options-h.md#oh_abilityruntime_setstartoptionsminwindowheight) | 设置启动Ability时的窗口最小高度，单位为vp。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsMinWindowHeight(AbilityRuntime\_StartOptions \*startOptions, int32\_t &minWindowHeight)](capi-start-options-h.md#oh_abilityruntime_getstartoptionsminwindowheight) | 获取启动Ability时的窗口最小高度，单位为vp。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsMaxWindowHeight(AbilityRuntime\_StartOptions \*startOptions, int32\_t maxWindowHeight)](capi-start-options-h.md#oh_abilityruntime_setstartoptionsmaxwindowheight) | 设置启动Ability时的窗口最大高度，单位为vp。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsMaxWindowHeight(AbilityRuntime\_StartOptions \*startOptions, int32\_t &maxWindowHeight)](capi-start-options-h.md#oh_abilityruntime_getstartoptionsmaxwindowheight) | 获取启动Ability时的窗口最大高度，单位为vp。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AbilityRuntime\_CreateStartOptions()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_StartOptions* OH_AbilityRuntime_CreateStartOptions(void)
```

**描述**

创建[AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md)对象。

**起始版本：** 17

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md)\* | 返回指针类型AbilityRuntime\_StartOptions对象。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void createStartOptionsTest()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. // 销毁options，防止内存泄漏
12. OH_AbilityRuntime_DestroyStartOptions(&options);
13. }
```

### OH\_AbilityRuntime\_DestroyStartOptions()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_DestroyStartOptions(AbilityRuntime_StartOptions **startOptions)
```

**描述**

销毁[AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md)对象。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*\*startOptions | 需要销毁的AbilityRuntime\_StartOptions对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void destroyStartOptionsTest()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. // 销毁options，防止内存泄漏
12. OH_AbilityRuntime_DestroyStartOptions(&options);
13. }
```

### OH\_AbilityRuntime\_SetStartOptionsWindowMode()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowMode(AbilityRuntime_StartOptions *startOptions,AbilityRuntime_WindowMode windowMode)
```

**描述**

设置启动Ability时的窗口模式。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| [AbilityRuntime\_WindowMode](capi-context-constant-h.md#abilityruntime_windowmode) windowMode | 启动Ability时的窗口模式。取值范围参见AbilityRuntime\_WindowMode。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空或者WindowMode无效。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWindowMode(options,
12. ABILITY_RUNTIME_WINDOW_MODE_FULL_SCREEN);
13. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
14. // 记录错误日志以及其他业务处理
15. }
16. // 销毁options，防止内存泄漏
17. OH_AbilityRuntime_DestroyStartOptions(&options);
18. }
```

### OH\_AbilityRuntime\_GetStartOptionsWindowMode()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowMode(AbilityRuntime_StartOptions *startOptions,AbilityRuntime_WindowMode &windowMode)
```

**描述**

获取启动Ability时的窗口模式。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| [AbilityRuntime\_WindowMode](capi-context-constant-h.md#abilityruntime_windowmode) windowMode | 启动Ability时的窗口模式。取值范围参见AbilityRuntime\_WindowMode。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. AbilityRuntime_WindowMode windowMode = ABILITY_RUNTIME_WINDOW_MODE_UNDEFINED;
12. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWindowMode(options, windowMode);
13. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
14. // 记录错误日志以及其他业务处理
15. }
16. // 销毁options，防止内存泄漏
17. OH_AbilityRuntime_DestroyStartOptions(&options);
18. }
```

### OH\_AbilityRuntime\_SetStartOptionsDisplayId()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsDisplayId(AbilityRuntime_StartOptions *startOptions,int32_t displayId)
```

**描述**

设置启动Ability时窗口所在的屏幕ID。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t displayId | 启动Ability时窗口所在的屏幕ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsDisplayId(options, 1);
12. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
13. // 记录错误日志以及其他业务处理
14. }
15. // 销毁options，防止内存泄漏
16. OH_AbilityRuntime_DestroyStartOptions(&options);
17. }
```

### OH\_AbilityRuntime\_GetStartOptionsDisplayId()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsDisplayId(AbilityRuntime_StartOptions *startOptions,int32_t &displayId)
```

**描述**

获取启动Ability时窗口所在的屏幕ID。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &displayId | 启动Ability时窗口所在的屏幕ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. int32_t displayId = 0;
12. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsDisplayId(options, displayId);
13. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
14. // 记录错误日志以及其他业务处理
15. }
16. // 销毁options，防止内存泄漏
17. OH_AbilityRuntime_DestroyStartOptions(&options);
18. }
```

### OH\_AbilityRuntime\_SetStartOptionsWithAnimation()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWithAnimation(AbilityRuntime_StartOptions *startOptions,bool withAnimation)
```

**描述**

设置启动Ability时是否具有动画效果。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| bool withAnimation | 启动Ability时是否具有动画效果。  true表示启动Ability时具有动画效果；false表示启动Ability时不具有动画效果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWithAnimation(options, true);
12. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
13. // 记录错误日志以及其他业务处理
14. }
15. // 销毁options，防止内存泄漏
16. OH_AbilityRuntime_DestroyStartOptions(&options);
17. }
```

### OH\_AbilityRuntime\_GetStartOptionsWithAnimation()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWithAnimation(AbilityRuntime_StartOptions *startOptions,bool &withAnimation)
```

**描述**

获取启动Ability时是否具有动画效果。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| bool &withAnimation | 启动Ability时是否具有动画效果。  true表示启动Ability时具有动画效果；false表示启动Ability时不具有动画效果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. bool withAnimation = false;
12. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWithAnimation(options, withAnimation);
13. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
14. // 记录错误日志以及其他业务处理
15. }
16. // 销毁options，防止内存泄漏
17. OH_AbilityRuntime_DestroyStartOptions(&options);
18. }
```

### OH\_AbilityRuntime\_SetStartOptionsWindowLeft()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowLeft(AbilityRuntime_StartOptions *startOptions,int32_t windowLeft)
```

**描述**

设置启动Ability时的窗口左侧位置，单位为px。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t windowLeft | 启动Ability时的窗口左侧位置，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWindowLeft(options, 200);
12. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
13. // 记录错误日志以及其他业务处理
14. }
15. // 销毁options，防止内存泄漏
16. OH_AbilityRuntime_DestroyStartOptions(&options);
17. }
```

### OH\_AbilityRuntime\_GetStartOptionsWindowLeft()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowLeft(AbilityRuntime_StartOptions *startOptions,int32_t &windowLeft)
```

**描述**

获取启动Ability时的窗口左侧位置，单位为px。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &windowLeft | 启动Ability时的窗口左侧位置，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. int32_t windowLeft = 0;
12. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWindowLeft(options, windowLeft);
13. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
14. // 记录错误日志以及其他业务处理
15. }
16. // 销毁options，防止内存泄漏
17. OH_AbilityRuntime_DestroyStartOptions(&options);
18. }
```

### OH\_AbilityRuntime\_SetStartOptionsWindowTop()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowTop(AbilityRuntime_StartOptions *startOptions,int32_t windowTop)
```

**描述**

设置启动Ability时的窗口顶部位置，单位为px。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t windowTop | 启动Ability时的窗口顶部位置，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWindowTop(options, 500);
12. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
13. // 记录错误日志以及其他业务处理
14. }
15. // 销毁options，防止内存泄漏
16. OH_AbilityRuntime_DestroyStartOptions(&options);
17. }
```

### OH\_AbilityRuntime\_GetStartOptionsWindowTop()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowTop(AbilityRuntime_StartOptions *startOptions,int32_t &windowTop)
```

**描述**

获取启动Ability时的窗口顶部位置，单位为px。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &windowTop | 启动Ability时的窗口顶部位置，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. int32_t windowTop = 0;
12. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWindowTop(options, windowTop);
13. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
14. // 记录错误日志以及其他业务处理
15. }
16. // 销毁options，防止内存泄漏
17. OH_AbilityRuntime_DestroyStartOptions(&options);
18. }
```

### OH\_AbilityRuntime\_SetStartOptionsWindowHeight()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowHeight(AbilityRuntime_StartOptions *startOptions,int32_t windowHeight)
```

**描述**

设置启动Ability时的窗口高度，单位为px。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t windowHeight | 启动Ability时的窗口高度，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWindowHeight(options, 500);
12. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
13. // 记录错误日志以及其他业务处理
14. }
15. // 销毁options，防止内存泄漏
16. OH_AbilityRuntime_DestroyStartOptions(&options);
17. }
```

### OH\_AbilityRuntime\_GetStartOptionsWindowHeight()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowHeight(AbilityRuntime_StartOptions *startOptions,int32_t &windowHeight)
```

**描述**

获取启动Ability时的窗口高度，单位为px。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &windowHeight | 启动Ability时的窗口高度，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. int32_t windowHeight = 0;
12. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWindowHeight(options, windowHeight);
13. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
14. // 记录错误日志以及其他业务处理
15. }
16. // 销毁options，防止内存泄漏
17. OH_AbilityRuntime_DestroyStartOptions(&options);
18. }
```

### OH\_AbilityRuntime\_SetStartOptionsWindowWidth()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowWidth(AbilityRuntime_StartOptions *startOptions,int32_t windowWidth)
```

**描述**

设置启动Ability时的窗口宽度，单位为px。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t windowWidth | 启动Ability时的窗口宽度，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWindowWidth(options, 500);
12. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
13. // 记录错误日志以及其他业务处理
14. }
15. // 销毁options，防止内存泄漏
16. OH_AbilityRuntime_DestroyStartOptions(&options);
17. }
```

### OH\_AbilityRuntime\_GetStartOptionsWindowWidth()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowWidth(AbilityRuntime_StartOptions *startOptions,int32_t &windowWidth)
```

**描述**

获取启动Ability时的窗口宽度，单位为px。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &windowWidth | 启动Ability时的窗口宽度，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. int32_t windowWidth = 0;
12. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWindowWidth(options, windowWidth);
13. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
14. // 记录错误日志以及其他业务处理
15. }
16. // 销毁options，防止内存泄漏
17. OH_AbilityRuntime_DestroyStartOptions(&options);
18. }
```

### OH\_AbilityRuntime\_SetStartOptionsStartVisibility()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsStartVisibility(AbilityRuntime_StartOptions *startOptions,AbilityRuntime_StartVisibility startVisibility)
```

**描述**

设置启动Ability时窗口和dock栏图标的显示模式。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | StartOptions结构体。 |
| [AbilityRuntime\_StartVisibility](capi-context-constant-h.md#abilityruntime_startvisibility) startVisibility | 需要设置的显示模式。取值范围参见AbilityRuntime\_StartVisibility。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示设置成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空，或startVisibility取值不在枚举类AbilityRuntime\_StartVisibility中。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. AbilityRuntime_StartVisibility visibility = AbilityRuntime_StartVisibility::ABILITY_RUNTIME_SHOW_UPON_START;
12. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsStartVisibility(options, visibility);
13. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
14. // 记录错误日志以及其他业务处理
15. }
16. // 销毁options，防止内存泄漏
17. OH_AbilityRuntime_DestroyStartOptions(&options);
18. }
```

### OH\_AbilityRuntime\_GetStartOptionsStartVisibility()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsStartVisibility(AbilityRuntime_StartOptions *startOptions,AbilityRuntime_StartVisibility &startVisibility)
```

**描述**

获取启动Ability时窗口和dock栏图标的显示模式。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | StartOptions结构体。 |
| [AbilityRuntime\_StartVisibility](capi-context-constant-h.md#abilityruntime_startvisibility) &startVisibility | 获取到的显示模式。取值范围参见AbilityRuntime\_StartVisibility。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示获取成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空，或startVisibility未被设置。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. AbilityRuntime_StartVisibility visibility;
12. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsStartVisibility(options, visibility);
13. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
14. // 记录错误日志以及其他业务处理
15. }
16. // 销毁options，防止内存泄漏
17. OH_AbilityRuntime_DestroyStartOptions(&options);
18. }
```

### OH\_AbilityRuntime\_SetStartOptionsStartWindowIcon()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsStartWindowIcon(AbilityRuntime_StartOptions *startOptions,OH_PixelmapNative *startWindowIcon)
```

**描述**

设置启动Ability时的窗口启动图标。图片数据大小限制为600M。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| OH\_PixelmapNative \*startWindowIcon | 启动Ability时的窗口启动图标。图片数据大小限制为600M。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空，或者startWindowIcon为空指针。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. uint8_t data[96];
6. size_t dataSize = 96;
7. for (int i = 0; i < dataSize; i++) {
8. data[i] = i + 1;
9. }

11. // 创建参数结构体实例，并设置参数
12. OH_Pixelmap_InitializationOptions *createOpts = nullptr;
13. OH_PixelmapInitializationOptions_Create(&createOpts);
14. OH_PixelmapInitializationOptions_SetWidth(createOpts, 6);
15. OH_PixelmapInitializationOptions_SetHeight(createOpts, 4);
16. OH_PixelmapInitializationOptions_SetPixelFormat(createOpts, PIXEL_FORMAT_RGBA_8888);
17. OH_PixelmapInitializationOptions_SetAlphaType(createOpts, PIXELMAP_ALPHA_TYPE_UNKNOWN);

19. // 创建Pixelmap实例
20. OH_PixelmapNative *startWindowIcon = nullptr;
21. Image_ErrorCode errCode = OH_PixelmapNative_CreatePixelmap(data, dataSize, createOpts, &startWindowIcon);
22. if (errCode != IMAGE_SUCCESS) {
23. // 记录错误日志以及其他业务处理

25. // 销毁createOpts，防止内存泄漏
26. OH_PixelmapInitializationOptions_Release(createOpts);
27. return;
28. }

30. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
31. if (options == nullptr) {
32. // 记录错误日志以及其他业务处理

34. // 销毁createOpts，防止内存泄漏
35. OH_PixelmapInitializationOptions_Release(createOpts);

37. // 销毁startWindowIcon，防止内存泄漏
38. OH_PixelmapNative_Release(startWindowIcon);
39. return;
40. }

42. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsStartWindowIcon(options, startWindowIcon);
43. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
44. // 记录错误日志以及其他业务处理
45. }
46. // 销毁createOpts，防止内存泄漏
47. OH_PixelmapInitializationOptions_Release(createOpts);

49. // 销毁startWindowIcon，防止内存泄漏
50. OH_PixelmapNative_Release(startWindowIcon);

52. // 销毁options，防止内存泄漏
53. OH_AbilityRuntime_DestroyStartOptions(&options);
54. }
```

### OH\_AbilityRuntime\_GetStartOptionsStartWindowIcon()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsStartWindowIcon(AbilityRuntime_StartOptions *startOptions,OH_PixelmapNative **startWindowIcon)
```

**描述**

获取启动Ability时的窗口启动图标。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| OH\_PixelmapNative \*\*startWindowIcon | 启动Ability时的窗口启动图标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空，或者startWindowIcon没有设置为空指针。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. OH_PixelmapNative *startWindowIcon = nullptr;
12. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsStartWindowIcon(options, &startWindowIcon);
13. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
14. // 记录错误日志以及其他业务处理
15. }

17. // 销毁startWindowIcon，防止内存泄漏
18. OH_PixelmapNative_Release(startWindowIcon);

20. // 销毁options，防止内存泄漏
21. OH_AbilityRuntime_DestroyStartOptions(&options);
22. }
```

### OH\_AbilityRuntime\_SetStartOptionsStartWindowBackgroundColor()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsStartWindowBackgroundColor(AbilityRuntime_StartOptions *startOptions, const char *startWindowBackgroundColor)
```

**描述**

设置启动Ability时的窗口背景颜色。启动UIAbility时，启动页所显示的背景颜色如果未设置该字段，则默认采用[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)的startWindowBackground字段的配置。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| const char \*startWindowBackgroundColor | 启动Ability时的窗口背景颜色。固定为ARGB格式, 如：#E5FFFFFF。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空，或者StartWindowBackgroundColor没有置为空指针。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsStartWindowBackgroundColor(options, "#00000000");
12. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
13. // 记录错误日志以及其他业务处理
14. }

16. // 销毁options，防止内存泄漏
17. OH_AbilityRuntime_DestroyStartOptions(&options);
18. }
```

### OH\_AbilityRuntime\_GetStartOptionsStartWindowBackgroundColor()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsStartWindowBackgroundColor(AbilityRuntime_StartOptions *startOptions, char **startWindowBackgroundColor, size_t &size)
```

**描述**

获取启动Ability时的窗口背景颜色。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| char \*\*startWindowBackgroundColor | 启动Ability时的窗口背景颜色。固定为ARGB格式, 如：#E5FFFFFF。 |
| size\_t &size | 获取到的窗口背景颜色的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示startOptions为空，或者startWindowBackgroundColor没有置为空指针。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL时，表示开发者无法恢复的内部错误，比如内部调用malloc错误，或者字符串拷贝函数出错。 |

**示例代码：**

```
1. #include <cstdlib>

3. #include <AbilityKit/ability_runtime/start_options.h>

5. void demo()
6. {
7. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
8. if (options == nullptr) {
9. // 记录错误日志以及其他业务处理
10. return;
11. }

13. char *startWindowBackgroundColor = nullptr;
14. size_t size = 0;
15. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsStartWindowBackgroundColor(options,
16. &startWindowBackgroundColor, size);
17. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
18. // 记录错误日志以及其他业务处理
19. }

21. if (startWindowBackgroundColor != nullptr) {
22. // 销毁startWindowBackgroundColor，防止内存泄漏
23. free(startWindowBackgroundColor);
24. startWindowBackgroundColor = nullptr;
25. }

27. // 销毁options，防止内存泄漏
28. OH_AbilityRuntime_DestroyStartOptions(&options);
29. }
```

### OH\_AbilityRuntime\_SetStartOptionsSupportedWindowModes()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsSupportedWindowModes(AbilityRuntime_StartOptions *startOptions, AbilityRuntime_SupportedWindowMode *supportedWindowModes,size_t size)
```

**描述**

设置启动Ability时的组件所支持的窗口模式。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| [AbilityRuntime\_SupportedWindowMode](capi-context-constant-h.md#abilityruntime_supportedwindowmode) \*supportedWindowModes | 启动Ability时的组件所支持的窗口模式。取值范围参见AbilityRuntime\_SupportedWindowMode。 |
| size\_t size | 组件所支持的窗口模式大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions或者SupportedWindowModes为空，或者Size为0。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. size_t supportedWindowModesSize = 3;
12. AbilityRuntime_SupportedWindowMode supportedWindowModes[3] = {
13. ABILITY_RUNTIME_SUPPORTED_WINDOW_MODE_FULL_SCREEN,
14. ABILITY_RUNTIME_SUPPORTED_WINDOW_MODE_SPLIT,
15. ABILITY_RUNTIME_SUPPORTED_WINDOW_MODE_FLOATING,
16. };
17. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsSupportedWindowModes(options,
18. supportedWindowModes, supportedWindowModesSize);
19. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
20. // 记录错误日志以及其他业务处理
21. }

23. // 销毁options，防止内存泄漏
24. OH_AbilityRuntime_DestroyStartOptions(&options);
25. }
```

### OH\_AbilityRuntime\_GetStartOptionsSupportedWindowModes()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsSupportedWindowModes(AbilityRuntime_StartOptions *startOptions, AbilityRuntime_SupportedWindowMode **supportedWindowModes,size_t &size)
```

**描述**

获取启动Ability时的组件所支持的窗口模式。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| [AbilityRuntime\_SupportedWindowMode](capi-context-constant-h.md#abilityruntime_supportedwindowmode) \*\*supportedWindowModes | 启动Ability时的组件所支持的窗口模式。取值范围参见AbilityRuntime\_SupportedWindowMode。 |
| size | 组件所支持的窗口模式大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空，或者SupportWindowMode没有置为空指针。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL时，表示开发者无法恢复的内部错误，比如内部调用malloc错误。 |

**示例代码：**

```
1. #include <cstdlib>

3. #include <AbilityKit/ability_runtime/start_options.h>

5. void demo()
6. {
7. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
8. if (options == nullptr) {
9. // 记录错误日志以及其他业务处理
10. return;
11. }

13. AbilityRuntime_SupportedWindowMode *supportedWindowModes = nullptr;
14. size_t size = 0;
15. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsSupportedWindowModes(options,
16. &supportedWindowModes, size);
17. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
18. // 记录错误日志以及其他业务处理
19. }

21. if (supportedWindowModes != nullptr) {
22. // 销毁supportedWindowModes，防止内存泄漏
23. free(supportedWindowModes);
24. }

26. // 销毁options，防止内存泄漏
27. OH_AbilityRuntime_DestroyStartOptions(&options);
28. }
```

### OH\_AbilityRuntime\_SetStartOptionsMinWindowWidth()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsMinWindowWidth(AbilityRuntime_StartOptions *startOptions, int32_t minWindowWidth)
```

**描述**

设置启动Ability时的窗口最小宽度，单位为vp。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t minWindowWidth | 启动Ability时的窗口最小宽度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsMinWindowWidth(options, 100);
12. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
13. // 记录错误日志以及其他业务处理
14. }

16. // 销毁options，防止内存泄漏
17. OH_AbilityRuntime_DestroyStartOptions(&options);
18. }
```

### OH\_AbilityRuntime\_GetStartOptionsMinWindowWidth()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsMinWindowWidth(AbilityRuntime_StartOptions *startOptions, int32_t &minWindowWidth)
```

**描述**

获取启动Ability时的窗口最小宽度，单位为vp。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &minWindowWidth | 启动Ability时的窗口最小宽度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. int32_t minWindowWidth = 0;
12. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsMinWindowWidth(options, minWindowWidth);
13. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
14. // 记录错误日志以及其他业务处理
15. }

17. // 销毁options，防止内存泄漏
18. OH_AbilityRuntime_DestroyStartOptions(&options);
19. }
```

### OH\_AbilityRuntime\_SetStartOptionsMaxWindowWidth()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsMaxWindowWidth(AbilityRuntime_StartOptions *startOptions, int32_t maxWindowWidth)
```

**描述**

设置启动Ability时的窗口最大宽度，单位为vp。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t maxWindowWidth | 启动Ability时的窗口最大宽度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsMaxWindowWidth(options, 100);
12. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
13. // 记录错误日志以及其他业务处理
14. }

16. // 销毁options，防止内存泄漏
17. OH_AbilityRuntime_DestroyStartOptions(&options);
18. }
```

### OH\_AbilityRuntime\_GetStartOptionsMaxWindowWidth()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsMaxWindowWidth(AbilityRuntime_StartOptions *startOptions, int32_t &maxWindowWidth)
```

**描述**

获取启动Ability时的窗口最大宽度，单位为vp。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &maxWindowWidth | 启动Ability时的窗口最大宽度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. int32_t maxWindowWidth = 0;
12. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsMaxWindowWidth(options, maxWindowWidth);
13. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
14. // 记录错误日志以及其他业务处理
15. }

17. // 销毁options，防止内存泄漏
18. OH_AbilityRuntime_DestroyStartOptions(&options);
19. }
```

### OH\_AbilityRuntime\_SetStartOptionsMinWindowHeight()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsMinWindowHeight(AbilityRuntime_StartOptions *startOptions, int32_t minWindowHeight)
```

**描述**

设置启动Ability时的窗口最小高度，单位为vp。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t minWindowHeight | 启动Ability时的窗口最小高度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsMinWindowHeight(options, 100);
12. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
13. // 记录错误日志以及其他业务处理
14. }

16. // 销毁options，防止内存泄漏
17. OH_AbilityRuntime_DestroyStartOptions(&options);
18. }
```

### OH\_AbilityRuntime\_GetStartOptionsMinWindowHeight()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsMinWindowHeight(AbilityRuntime_StartOptions *startOptions, int32_t &minWindowHeight)
```

**描述**

获取启动Ability时的窗口最小高度，单位为vp。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &minWindowHeight | 启动Ability时的窗口最小高度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. int32_t minWindowHeight = 0;
12. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsMinWindowHeight(options, minWindowHeight);
13. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
14. // 记录错误日志以及其他业务处理
15. }

17. // 销毁options，防止内存泄漏
18. OH_AbilityRuntime_DestroyStartOptions(&options);
19. }
```

### OH\_AbilityRuntime\_SetStartOptionsMaxWindowHeight()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsMaxWindowHeight(AbilityRuntime_StartOptions *startOptions, int32_t maxWindowHeight)
```

**描述**

设置启动Ability时的窗口最大高度，单位为vp。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t maxWindowHeight | 启动Ability时的窗口最大高度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsMaxWindowHeight(options, 100);
12. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
13. // 记录错误日志以及其他业务处理
14. }

16. // 销毁options，防止内存泄漏
17. OH_AbilityRuntime_DestroyStartOptions(&options);
18. }
```

### OH\_AbilityRuntime\_GetStartOptionsMaxWindowHeight()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsMaxWindowHeight(AbilityRuntime_StartOptions *startOptions, int32_t &maxWindowHeight)
```

**描述**

获取启动Ability时的窗口最大高度，单位为vp。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &maxWindowHeight | 启动Ability时的窗口最大高度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。  在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。 |

**示例代码：**

```
1. #include <AbilityKit/ability_runtime/start_options.h>

3. void demo()
4. {
5. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
6. if (options == nullptr) {
7. // 记录错误日志以及其他业务处理
8. return;
9. }

11. int32_t maxWindowHeight = 0;
12. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsMaxWindowHeight(options, maxWindowHeight);
13. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
14. // 记录错误日志以及其他业务处理
15. }

17. // 销毁options，防止内存泄漏
18. OH_AbilityRuntime_DestroyStartOptions(&options);
19. }
```
