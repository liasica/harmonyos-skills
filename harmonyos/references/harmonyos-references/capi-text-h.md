---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-text-h
title: text.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > text.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:21+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:2c2aa04f5391a0ac8f84c636b67f6e9a818d24cacdf9a37f190e41d2e139af74
---

## 概述

定义Text相关的枚举和接口，用于配置文本样式、控制跑马灯效果、实现文本实体识别以及管理文本控制器等功能。适用于需要自定义文本显示效果、实现动态文本交互、识别文本中特殊实体（如地址、电话号码）以及精确控制文本字体粗细等场景。通过这些配置接口，开发者可以灵活控制文本组件的显示效果和交互行为，提升用户体验。

**引用文件：** <arkui/node\_attributes/text.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [native\_type\_sample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NativeType/native_type_sample)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_ArkUI\_TextDataDetectorConfig](capi-arkui-nativemodule-oh-arkui-textdatadetectorconfig.md) | OH\_ArkUI\_TextDataDetectorConfig | 定义文本实体识别的配置。文本实体指的是地址、电话号码等特殊内容实体。 |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md) | ArkUI\_TextMarqueeOptions | 定义文本跑马灯模式配置项，用于配置文本跑马灯效果的各项显示参数。适用于需要在有限空间内循环展示较长文本内容的场景，如通知栏滚动消息、标题滚动展示等，可有效解决文本超出显示区域时的展示问题。 |
| [OH\_ArkUI\_FontWeightConfigs](capi-arkui-nativemodule-oh-arkui-fontweightconfigs.md) | OH\_ArkUI\_FontWeightConfigs | 定义文本的字体粗细配置，适用于需要精确控制文本字体粗细或需要文本字体粗细跟随设备字体设置变化的应用场景。可以通过[OH\_ArkUI\_FontWeightConfigs\_Create](capi-text-h.md#oh_arkui_fontweightconfigs_create)接口创建文本字体粗细配置对象，使用完毕后必须调用[OH\_ArkUI\_FontWeightConfigs\_Destroy](capi-text-h.md#oh_arkui_fontweightconfigs_destroy)接口销毁对象以释放资源，避免内存泄漏。配置创建后，可通过以下接口进行设置和查询：通过[OH\_ArkUI\_FontWeightConfigs\_SetEnableVariableFontWeight](capi-text-h.md#oh_arkui_fontweightconfigs_setenablevariablefontweight)接口设置是否启用可变字重调节，通过[OH\_ArkUI\_FontWeightConfigs\_GetEnableVariableFontWeight](capi-text-h.md#oh_arkui_fontweightconfigs_getenablevariablefontweight)接口查看是否启用了可变字重调节，通过[OH\_ArkUI\_FontWeightConfigs\_SetEnableDeviceFontWeightCategory](capi-text-h.md#oh_arkui_fontweightconfigs_setenabledevicefontweightcategory)接口设置文本字体粗细是否跟随设备的字体粗细级别更新，通过[OH\_ArkUI\_FontWeightConfigs\_GetEnableDeviceFontWeightCategory](capi-text-h.md#oh_arkui_fontweightconfigs_getenabledevicefontweightcategory)接口查看文本字体粗细是否跟随设备的字体粗细级别更新。当该配置对象被使用且不为空指针时，若用户未通过接口显式设置，各项配置将使用默认值（可变字重调节默认为禁用，文本字体粗细跟随设备字体粗细级别更新默认为启用）。当该配置为空指针时，不应用默认值，文本字体粗细行为与父组件保持一致。 |
| [OH\_ArkUI\_FontConfigs](capi-arkui-nativemodule-oh-arkui-fontconfigs.md) | OH\_ArkUI\_FontConfigs | 定义文本的字体配置，当前支持通过相关接口设置和获取字体粗细配置，适用于需要自定义字体粗细显示效果的场景。可以通过[OH\_ArkUI\_FontConfigs\_Create](capi-text-h.md#oh_arkui_fontconfigs_create)接口创建字体配置对象，通过[OH\_ArkUI\_FontConfigs\_Destroy](capi-text-h.md#oh_arkui_fontconfigs_destroy)接口销毁字体配置对象。配置创建后，可通过以下接口进行设置和查询：通过[OH\_ArkUI\_FontConfigs\_SetFontWeightConfigs](capi-text-h.md#oh_arkui_fontconfigs_setfontweightconfigs)接口设置字体粗细配置，通过[OH\_ArkUI\_FontConfigs\_GetFontWeightConfigs](capi-text-h.md#oh_arkui_fontconfigs_getfontweightconfigs)接口获取字体粗细配置。 |
| [OH\_ArkUI\_TextController](capi-arkui-nativemodule-oh-arkui-textcontroller.md) | OH\_ArkUI\_TextController | 定义文本组件的控制器，用于在Native侧对文本组件进行控制和交互。控制器需要先通过节点属性绑定到文本组件，才能进行后续操作。一个控制器只能绑定到一个文本组件，绑定后该控制器将管理对应文本组件的样式和内容。可通过[OH\_ArkUI\_TextController\_Create](capi-text-h.md#oh_arkui_textcontroller_create)创建控制器对象，创建后必须在使用完毕后调用[OH\_ArkUI\_TextController\_Destroy](capi-text-h.md#oh_arkui_textcontroller_destroy)接口销毁对象以释放资源，二者必须成对使用，否则会导致内存泄漏。创建控制器后，可通过节点属性将控制器绑定到文本组件，然后使用[OH\_ArkUI\_TextController\_SetStyledString](capi-native-type-h.md#oh_arkui_textcontroller_setstyledstring)等接口设置文本组件的属性字符串，实现对文本内容的动态管理和样式控制。适用于需要在Native层操作文本组件的场景。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_FontStyle](capi-text-h.md#arkui_fontstyle) | ArkUI\_FontStyle | 定义字体样式枚举值。 |
| [ArkUI\_FontWeight](capi-text-h.md#arkui_fontweight) | ArkUI\_FontWeight | 定义字体粗细/字重枚举值。 |
| [ArkUI\_TextHeightAdaptivePolicy](capi-text-h.md#arkui_textheightadaptivepolicy) | ArkUI\_TextHeightAdaptivePolicy | 定义文本自适应高度的方式。 |
| [ArkUI\_TextDataDetectorType](capi-text-h.md#arkui_textdatadetectortype) | ArkUI\_TextDataDetectorType | 定义文本识别的实体类型。 |
| [ArkUI\_MarqueeStartPolicy](capi-text-h.md#arkui_marqueestartpolicy) | ArkUI\_MarqueeStartPolicy | 定义跑马灯启动策略枚举。 |
| [ArkUI\_MarqueeUpdatePolicy](capi-text-h.md#arkui_marqueeupdatepolicy) | ArkUI\_MarqueeUpdatePolicy | 定义跑马灯更新策略枚举。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions\* OH\_ArkUI\_TextMarqueeOptions\_Create()](capi-text-h.md#oh_arkui_textmarqueeoptions_create) | 创建文本跑马灯模式配置项。当该对象不再使用时，请调用[OH\_ArkUI\_TextMarqueeOptions\_Dispose](capi-text-h.md#oh_arkui_textmarqueeoptions_dispose)销毁，以释放资源避免内存泄漏。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_Dispose(ArkUI\_TextMarqueeOptions\* option)](capi-text-h.md#oh_arkui_textmarqueeoptions_dispose) | 销毁文本跑马灯模式配置项对象。与[OH\_ArkUI\_TextMarqueeOptions\_Create](capi-text-h.md#oh_arkui_textmarqueeoptions_create)成对使用，否则会导致内存泄漏。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetStart(ArkUI\_TextMarqueeOptions\* option, bool start)](capi-text-h.md#oh_arkui_textmarqueeoptions_setstart) | 设置文本跑马灯模式配置项是否播放。 |
| [bool OH\_ArkUI\_TextMarqueeOptions\_GetStart(ArkUI\_TextMarqueeOptions\* option)](capi-text-h.md#oh_arkui_textmarqueeoptions_getstart) | 获取文本跑马灯模式配置项是否播放。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetStep(ArkUI\_TextMarqueeOptions\* option, float step)](capi-text-h.md#oh_arkui_textmarqueeoptions_setstep) | 设置文本跑马灯模式配置项的步长。 |
| [float OH\_ArkUI\_TextMarqueeOptions\_GetStep(ArkUI\_TextMarqueeOptions\* option)](capi-text-h.md#oh_arkui_textmarqueeoptions_getstep) | 获取文本跑马灯模式配置项的步长。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetSpacing(ArkUI\_TextMarqueeOptions\* option, float spacing)](capi-text-h.md#oh_arkui_textmarqueeoptions_setspacing) | 设置文本跑马灯模式配置项的首尾间距。 |
| [float OH\_ArkUI\_TextMarqueeOptions\_GetSpacing(ArkUI\_TextMarqueeOptions\* option)](capi-text-h.md#oh_arkui_textmarqueeoptions_getspacing) | 获取文本跑马灯模式配置项的首尾间距。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetLoop(ArkUI\_TextMarqueeOptions\* option, int32\_t loop)](capi-text-h.md#oh_arkui_textmarqueeoptions_setloop) | 设置文本跑马灯模式配置项的重复滚动次数，小于等于零时无限循环。 |
| [int32\_t OH\_ArkUI\_TextMarqueeOptions\_GetLoop(ArkUI\_TextMarqueeOptions\* option)](capi-text-h.md#oh_arkui_textmarqueeoptions_getloop) | 获取文本跑马灯模式配置项的重复滚动的次数。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetFromStart(ArkUI\_TextMarqueeOptions\* option, bool fromStart)](capi-text-h.md#oh_arkui_textmarqueeoptions_setfromstart) | 设置文本跑马灯模式配置项的运行方向。 |
| [bool OH\_ArkUI\_TextMarqueeOptions\_GetFromStart(ArkUI\_TextMarqueeOptions\* option)](capi-text-h.md#oh_arkui_textmarqueeoptions_getfromstart) | 获取文本跑马灯模式配置项的运行方向。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetDelay(ArkUI\_TextMarqueeOptions\* option, int32\_t delay)](capi-text-h.md#oh_arkui_textmarqueeoptions_setdelay) | 设置文本跑马灯模式配置项的每轮滚动延迟时间。 |
| [int32\_t OH\_ArkUI\_TextMarqueeOptions\_GetDelay(ArkUI\_TextMarqueeOptions\* option)](capi-text-h.md#oh_arkui_textmarqueeoptions_getdelay) | 获取文本跑马灯模式配置项的每轮滚动延迟时间。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetFadeout(ArkUI\_TextMarqueeOptions\* option, bool fadeout)](capi-text-h.md#oh_arkui_textmarqueeoptions_setfadeout) | 设置文本跑马灯模式配置项是否支持文字超长时的渐隐效果。当Text内容超出显示范围时，未完全展现的文字边缘将应用渐隐效果。若两端均有文字未完全显示，则两端同时应用渐隐效果。在渐隐效果开启状态下，[ArkUI\_NodeAttributeType](capi-native-node-h.md#arkui_nodeattributetype)中的NODE\_CLIP属性将自动锁定为true，不允许设置为false。 |
| [bool OH\_ArkUI\_TextMarqueeOptions\_GetFadeout(ArkUI\_TextMarqueeOptions\* option)](capi-text-h.md#oh_arkui_textmarqueeoptions_getfadeout) | 获取文本跑马灯模式配置项是否支持文字超长时的渐隐效果。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetStartPolicy(ArkUI\_TextMarqueeOptions\* option, ArkUI\_MarqueeStartPolicy startPolicy)](capi-text-h.md#oh_arkui_textmarqueeoptions_setstartpolicy) | 设置文本跑马灯模式配置项的启动策略。 |
| [ArkUI\_MarqueeStartPolicy OH\_ArkUI\_TextMarqueeOptions\_GetStartPolicy(ArkUI\_TextMarqueeOptions\* option)](capi-text-h.md#oh_arkui_textmarqueeoptions_getstartpolicy) | 获取文本跑马灯模式配置项的启动策略。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetUpdatePolicy(ArkUI\_TextMarqueeOptions\* option, ArkUI\_MarqueeUpdatePolicy updatePolicy)](capi-text-h.md#oh_arkui_textmarqueeoptions_setupdatepolicy) | 设置文本跑马灯模式配置项的更新策略。 |
| [ArkUI\_MarqueeUpdatePolicy OH\_ArkUI\_TextMarqueeOptions\_GetUpdatePolicy(ArkUI\_TextMarqueeOptions\* option)](capi-text-h.md#oh_arkui_textmarqueeoptions_getupdatepolicy) | 获取文本跑马灯模式配置项的更新策略。 |
| [OH\_ArkUI\_TextDataDetectorConfig\* OH\_ArkUI\_TextDataDetectorConfig\_Create()](capi-text-h.md#oh_arkui_textdatadetectorconfig_create) | 创建一个文本实体识别配置对象。当该对象不再使用时，请调用[OH\_ArkUI\_TextDataDetectorConfig\_Destroy](capi-text-h.md#oh_arkui_textdatadetectorconfig_destroy)销毁，以释放资源避免内存泄漏。 |
| [void OH\_ArkUI\_TextDataDetectorConfig\_Destroy(OH\_ArkUI\_TextDataDetectorConfig\* config)](capi-text-h.md#oh_arkui_textdatadetectorconfig_destroy) | 销毁文本实体识别配置对象。与[OH\_ArkUI\_TextDataDetectorConfig\_Create](capi-text-h.md#oh_arkui_textdatadetectorconfig_create)成对使用，否则会导致内存泄漏。 |
| [OH\_ArkUI\_FontWeightConfigs\* OH\_ArkUI\_FontWeightConfigs\_Create()](capi-text-h.md#oh_arkui_fontweightconfigs_create) | 创建文本字体粗细配置对象。当该对象不再使用时，请调用[OH\_ArkUI\_FontWeightConfigs\_Destroy](capi-text-h.md#oh_arkui_fontweightconfigs_destroy)销毁，以释放资源避免内存泄漏。 |
| [void OH\_ArkUI\_FontWeightConfigs\_Destroy(OH\_ArkUI\_FontWeightConfigs\* option)](capi-text-h.md#oh_arkui_fontweightconfigs_destroy) | 销毁文本字体粗细配置对象。与[OH\_ArkUI\_FontWeightConfigs\_Create](capi-text-h.md#oh_arkui_fontweightconfigs_create)成对使用，否则会导致内存泄漏。 |
| [void OH\_ArkUI\_FontWeightConfigs\_SetEnableVariableFontWeight(OH\_ArkUI\_FontWeightConfigs\* option, bool enable)](capi-text-h.md#oh_arkui_fontweightconfigs_setenablevariablefontweight) | 设置是否启用可变字重调节。可变字重调节允许字体在100到900之间以任意整数值显示字重，实现更细腻的字体粗细控制。 |
| [bool OH\_ArkUI\_FontWeightConfigs\_GetEnableVariableFontWeight(OH\_ArkUI\_FontWeightConfigs\* option)](capi-text-h.md#oh_arkui_fontweightconfigs_getenablevariablefontweight) | 获取文本字体粗细配置对象是否启用了可变字重调节。 |
| [void OH\_ArkUI\_FontWeightConfigs\_SetEnableDeviceFontWeightCategory(OH\_ArkUI\_FontWeightConfigs\* option, bool enable)](capi-text-h.md#oh_arkui_fontweightconfigs_setenabledevicefontweightcategory) | 设置设备的字体粗细级别改变时文本字体粗细是否自动更新。设备的字体粗细级别是指系统设置中的全局字体粗细配置，用户可在系统设置中调整。 |
| [bool OH\_ArkUI\_FontWeightConfigs\_GetEnableDeviceFontWeightCategory(OH\_ArkUI\_FontWeightConfigs\* option)](capi-text-h.md#oh_arkui_fontweightconfigs_getenabledevicefontweightcategory) | 获取文本字体粗细是否跟随设备的字体粗细级别更新。 |
| [OH\_ArkUI\_FontConfigs\* OH\_ArkUI\_FontConfigs\_Create()](capi-text-h.md#oh_arkui_fontconfigs_create) | 创建文本字体配置对象。当该对象不再使用时，请调用[OH\_ArkUI\_FontConfigs\_Destroy](capi-text-h.md#oh_arkui_fontconfigs_destroy)销毁，以释放资源避免内存泄漏。 |
| [void OH\_ArkUI\_FontConfigs\_Destroy(OH\_ArkUI\_FontConfigs\* option)](capi-text-h.md#oh_arkui_fontconfigs_destroy) | 销毁文本字体配置对象。与[OH\_ArkUI\_FontConfigs\_Create](capi-text-h.md#oh_arkui_fontconfigs_create)成对使用，否则会导致内存泄漏。 |
| [void OH\_ArkUI\_FontConfigs\_SetFontWeightConfigs(OH\_ArkUI\_FontConfigs\* option, OH\_ArkUI\_FontWeightConfigs\* fontWeightConfigs)](capi-text-h.md#oh_arkui_fontconfigs_setfontweightconfigs) | 设置文本字体配置对象的文本字体粗细配置。 |
| [OH\_ArkUI\_FontWeightConfigs\* OH\_ArkUI\_FontConfigs\_GetFontWeightConfigs(OH\_ArkUI\_FontConfigs\* option)](capi-text-h.md#oh_arkui_fontconfigs_getfontweightconfigs) | 获取文本字体配置对象的文本字体粗细配置。 |
| [OH\_ArkUI\_TextController\* OH\_ArkUI\_TextController\_Create()](capi-text-h.md#oh_arkui_textcontroller_create) | 创建一个文本控制器对象。当该对象不再使用时，请调用[OH\_ArkUI\_TextController\_Destroy](capi-text-h.md#oh_arkui_textcontroller_destroy)销毁，以释放资源避免内存泄漏。 |
| [void OH\_ArkUI\_TextController\_Destroy(OH\_ArkUI\_TextController\* controller)](capi-text-h.md#oh_arkui_textcontroller_destroy) | 销毁文本控制器对象。与[OH\_ArkUI\_TextController\_Create](capi-text-h.md#oh_arkui_textcontroller_create)成对使用，否则会导致内存泄漏。 |

## 枚举类型说明

### ArkUI\_FontStyle

```c
enum ArkUI_FontStyle
```

**描述**

定义字体样式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_FONT\_STYLE\_NORMAL = 0 | 标准字体样式。 |
| ARKUI\_FONT\_STYLE\_ITALIC = 1 | 斜体字体样式。 |

### ArkUI\_FontWeight

```c
enum ArkUI_FontWeight
```

**描述**

定义字体粗细/字重枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_FONT\_WEIGHT\_W100 = 0 | 100 |
| ARKUI\_FONT\_WEIGHT\_W200 = 1 | 200 |
| ARKUI\_FONT\_WEIGHT\_W300 = 2 | 300 |
| ARKUI\_FONT\_WEIGHT\_W400 = 3 | 400 |
| ARKUI\_FONT\_WEIGHT\_W500 = 4 | 500 |
| ARKUI\_FONT\_WEIGHT\_W600 = 5 | 600 |
| ARKUI\_FONT\_WEIGHT\_W700 = 6 | 700 |
| ARKUI\_FONT\_WEIGHT\_W800 = 7 | 800 |
| ARKUI\_FONT\_WEIGHT\_W900 = 8 | 900 |
| ARKUI\_FONT\_WEIGHT\_BOLD = 9 | 字体较粗。 |
| ARKUI\_FONT\_WEIGHT\_NORMAL = 10 | 字体粗细正常，与ARKUI\_FONT\_WEIGHT\_REGULAR相同。 |
| ARKUI\_FONT\_WEIGHT\_BOLDER = 11 | 字体非常粗。 |
| ARKUI\_FONT\_WEIGHT\_LIGHTER = 12 | 字体较细。 |
| ARKUI\_FONT\_WEIGHT\_MEDIUM = 13 | 字体粗细适中。 |
| ARKUI\_FONT\_WEIGHT\_REGULAR = 14 | 字体粗细正常，与ARKUI\_FONT\_WEIGHT\_NORMAL相同。 |

### ArkUI\_TextHeightAdaptivePolicy

```c
enum ArkUI_TextHeightAdaptivePolicy
```

**描述**

定义文本自适应高度的方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXT\_HEIGHT\_ADAPTIVE\_POLICY\_MAX\_LINES\_FIRST = 0 | 设置文本高度自适应方式为以MaxLines优先。优先保持最大行数（maxLines）设置，当文本内容超出显示区域时，优先满足maxLines限制，超出部分可能被截断或通过其他方式处理。 |
| ARKUI\_TEXT\_HEIGHT\_ADAPTIVE\_POLICY\_MIN\_FONT\_SIZE\_FIRST = 1 | 设置文本高度自适应方式为以缩小字体优先。当文本内容超出显示区域时，优先通过缩小字体大小来适应高度限制，确保文本完整显示，字体大小会在允许范围内自动调整。 |
| ARKUI\_TEXT\_HEIGHT\_ADAPTIVE\_POLICY\_LAYOUT\_CONSTRAINT\_FIRST = 2 | 设置文本高度自适应方式为以布局约束（高度）优先。严格遵循布局约束的高度设置，不自动调整文本高度或字体大小，超出部分可能被截断或通过其他方式处理。 |

### ArkUI\_TextDataDetectorType

```c
enum ArkUI_TextDataDetectorType
```

**描述**

定义文本识别的实体类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXT\_DATA\_DETECTOR\_TYPE\_PHONE\_NUMBER = 0 | 电话号码。 |
| ARKUI\_TEXT\_DATA\_DETECTOR\_TYPE\_URL = 1 | 链接。 |
| ARKUI\_TEXT\_DATA\_DETECTOR\_TYPE\_EMAIL = 2 | 邮箱。 |
| ARKUI\_TEXT\_DATA\_DETECTOR\_TYPE\_ADDRESS = 3 | 地址。 |

### ArkUI\_MarqueeStartPolicy

```c
enum ArkUI_MarqueeStartPolicy
```

**描述**

定义跑马灯启动策略枚举。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_MARQUEESTARTPOLICY\_DEFAULT = 0 | 默认持续滚动。 |
| ARKUI\_MARQUEESTARTPOLICY\_ONFOCUS = 1 | 获焦以及鼠标悬浮时开始滚动。 |

### ArkUI\_MarqueeUpdatePolicy

```c
enum ArkUI_MarqueeUpdatePolicy
```

**描述**

定义跑马灯更新策略枚举。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_MARQUEEUPDATEPOLICY\_DEFAULT = 0 | 跑马灯组件属性更新后，从开始位置，运行跑马灯效果。 |
| ARKUI\_MARQUEEUPDATEPOLICY\_PRESERVEPOSITION = 1 | 跑马灯组件属性更新后，保持当前位置，运行跑马灯效果。 |

## 函数说明

### OH\_ArkUI\_TextMarqueeOptions\_Create()

```c
ArkUI_TextMarqueeOptions* OH_ArkUI_TextMarqueeOptions_Create()
```

**描述**

创建文本跑马灯模式配置项。当该对象不再使用时，请调用[OH\_ArkUI\_TextMarqueeOptions\_Dispose](capi-text-h.md#oh_arkui_textmarqueeoptions_dispose)销毁，以释放资源避免内存泄漏。

**起始版本：** 23

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions\*](capi-arkui-nativemodule-arkui-textmarqueeoptions.md) | 返回指向文本跑马灯模式配置项对象的指针。如果创建失败，返回空指针。使用后需调用[OH\_ArkUI\_TextMarqueeOptions\_Dispose](capi-text-h.md#oh_arkui_textmarqueeoptions_dispose)销毁。 |

### OH\_ArkUI\_TextMarqueeOptions\_Dispose()

```c
void OH_ArkUI_TextMarqueeOptions_Dispose(ArkUI_TextMarqueeOptions* option)
```

**描述**

销毁文本跑马灯模式配置项对象。与[OH\_ArkUI\_TextMarqueeOptions\_Create](capi-text-h.md#oh_arkui_textmarqueeoptions_create)成对使用，否则会导致内存泄漏。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 需要销毁的文本跑马灯模式配置项对象指针。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetStart()

```c
void OH_ArkUI_TextMarqueeOptions_SetStart(ArkUI_TextMarqueeOptions* option, bool start)
```

**描述**

设置文本跑马灯模式配置项是否播放。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| bool start | 是否播放。true表示播放，false表示不播放。默认值：true。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetStart()

```c
bool OH_ArkUI_TextMarqueeOptions_GetStart(ArkUI_TextMarqueeOptions* option)
```

**描述**

获取文本跑马灯模式配置项是否播放。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 是否播放。true表示播放，false表示不播放。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetStep()

```c
void OH_ArkUI_TextMarqueeOptions_SetStep(ArkUI_TextMarqueeOptions* option, float step)
```

**描述**

设置文本跑马灯模式配置项的步长。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| float step | 步长。单位：vp。取值范围：(0, 文本长度]，超出取值范围时取4.0vp。默认值：4.0vp。设置步长后，跑马灯每次移动的距离为该步长值，步长越大滚动速度越快。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetStep()

```c
float OH_ArkUI_TextMarqueeOptions_GetStep(ArkUI_TextMarqueeOptions* option)
```

**描述**

获取文本跑马灯模式配置项的步长。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 步长。单位：vp。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetSpacing()

```c
void OH_ArkUI_TextMarqueeOptions_SetSpacing(ArkUI_TextMarqueeOptions* option, float spacing)
```

**描述**

设置文本跑马灯模式配置项的首尾间距。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| float spacing | 首尾间距。单位：vp。取值范围：[0, +∞)，小于0时取默认值48.0vp。默认值：48.0vp。设置后，跑马灯滚动一轮结束时，首尾文字之间的间隔距离为该间距值。建议根据显示区域宽度设置。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetSpacing()

```c
float OH_ArkUI_TextMarqueeOptions_GetSpacing(ArkUI_TextMarqueeOptions* option)
```

**描述**

获取文本跑马灯模式配置项的首尾间距。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 首尾间距。单位：vp。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetLoop()

```c
void OH_ArkUI_TextMarqueeOptions_SetLoop(ArkUI_TextMarqueeOptions* option, int32_t loop)
```

**描述**

设置文本跑马灯模式配置项的重复滚动次数，小于等于零时无限循环。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| int32\_t loop | 重复滚动的次数。小于等于零时无限循环。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetLoop()

```c
int32_t OH_ArkUI_TextMarqueeOptions_GetLoop(ArkUI_TextMarqueeOptions* option)
```

**描述**

获取文本跑马灯模式配置项的重复滚动的次数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 重复滚动的次数。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetFromStart()

```c
void OH_ArkUI_TextMarqueeOptions_SetFromStart(ArkUI_TextMarqueeOptions* option, bool fromStart)
```

**描述**

设置文本跑马灯模式配置项的运行方向。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| bool fromStart | 跑马灯运行方向。true表示从头开始滚动，false表示反向滚动。默认值：true。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetFromStart()

```c
bool OH_ArkUI_TextMarqueeOptions_GetFromStart(ArkUI_TextMarqueeOptions* option)
```

**描述**

获取文本跑马灯模式配置项的运行方向。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 跑马灯运行方向。true表示从头开始滚动，false表示反向滚动。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetDelay()

```c
void OH_ArkUI_TextMarqueeOptions_SetDelay(ArkUI_TextMarqueeOptions* option, int32_t delay)
```

**描述**

设置文本跑马灯模式配置项的每轮滚动延迟时间。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| int32\_t delay | 每轮滚动延迟时间，单位为毫秒。取值范围：[0, +∞)。默认值：0。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetDelay()

```c
int32_t OH_ArkUI_TextMarqueeOptions_GetDelay(ArkUI_TextMarqueeOptions* option)
```

**描述**

获取文本跑马灯模式配置项的每轮滚动延迟时间。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 每轮滚动延迟时间，单位为毫秒。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetFadeout()

```c
void OH_ArkUI_TextMarqueeOptions_SetFadeout(ArkUI_TextMarqueeOptions* option, bool fadeout)
```

**描述**

设置文本跑马灯模式配置项是否支持文字超长时的渐隐效果。当Text内容超出显示范围时，未完全展现的文字边缘将应用渐隐效果。

若两端均有文字未完全显示，则两端同时应用渐隐效果。

在渐隐效果开启状态下，[ArkUI\_NodeAttributeType](capi-native-node-h.md#arkui_nodeattributetype)中的NODE\_CLIP属性将自动锁定为true，不允许设置为false。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| bool fadeout | 跑马灯是否支持文字超长时的渐隐效果。  true表示支持渐隐效果，此时NODE\_CLIP属性将自动锁定为true，不允许设置为false。  false表示不支持渐隐效果。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetFadeout()

```c
bool OH_ArkUI_TextMarqueeOptions_GetFadeout(ArkUI_TextMarqueeOptions* option)
```

**描述**

获取文本跑马灯模式配置项是否支持文字超长时的渐隐效果。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 是否支持文字超长时的渐隐效果。true表示支持渐隐效果，false表示不支持渐隐效果。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetStartPolicy()

```c
void OH_ArkUI_TextMarqueeOptions_SetStartPolicy(ArkUI_TextMarqueeOptions* option, ArkUI_MarqueeStartPolicy startPolicy)
```

**描述**

设置文本跑马灯模式配置项的启动策略。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| [ArkUI\_MarqueeStartPolicy](capi-text-h.md#arkui_marqueestartpolicy) startPolicy | 启动策略。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetStartPolicy()

```c
ArkUI_MarqueeStartPolicy OH_ArkUI_TextMarqueeOptions_GetStartPolicy(ArkUI_TextMarqueeOptions* option)
```

**描述**

获取文本跑马灯模式配置项的启动策略。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_MarqueeStartPolicy](capi-text-h.md#arkui_marqueestartpolicy) | 启动策略。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetUpdatePolicy()

```c
void OH_ArkUI_TextMarqueeOptions_SetUpdatePolicy(ArkUI_TextMarqueeOptions* option, ArkUI_MarqueeUpdatePolicy updatePolicy)
```

**描述**

设置文本跑马灯模式配置项的更新策略。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| [ArkUI\_MarqueeUpdatePolicy](capi-text-h.md#arkui_marqueeupdatepolicy) updatePolicy | 更新策略。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetUpdatePolicy()

```c
ArkUI_MarqueeUpdatePolicy OH_ArkUI_TextMarqueeOptions_GetUpdatePolicy(ArkUI_TextMarqueeOptions* option)
```

**描述**

获取文本跑马灯模式配置项的更新策略。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_MarqueeUpdatePolicy](capi-text-h.md#arkui_marqueeupdatepolicy) | 更新策略。 |

### OH\_ArkUI\_TextDataDetectorConfig\_Create()

```c
OH_ArkUI_TextDataDetectorConfig* OH_ArkUI_TextDataDetectorConfig_Create()
```

**描述**

创建一个文本实体识别配置对象。当该对象不再使用时，请调用[OH\_ArkUI\_TextDataDetectorConfig\_Destroy](capi-text-h.md#oh_arkui_textdatadetectorconfig_destroy)销毁，以释放资源避免内存泄漏。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_TextDataDetectorConfig\*](capi-arkui-nativemodule-oh-arkui-textdatadetectorconfig.md) | 指向[OH\_ArkUI\_TextDataDetectorConfig](capi-arkui-nativemodule-oh-arkui-textdatadetectorconfig.md)对象的指针。如果创建失败，返回空指针。使用后需调用[OH\_ArkUI\_TextDataDetectorConfig\_Destroy](capi-text-h.md#oh_arkui_textdatadetectorconfig_destroy)销毁。 |

### OH\_ArkUI\_TextDataDetectorConfig\_Destroy()

```c
void OH_ArkUI_TextDataDetectorConfig_Destroy(OH_ArkUI_TextDataDetectorConfig* config)
```

**描述**

销毁文本实体识别配置对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_TextDataDetectorConfig](capi-arkui-nativemodule-oh-arkui-textdatadetectorconfig.md)\* config | 指向[OH\_ArkUI\_TextDataDetectorConfig](capi-arkui-nativemodule-oh-arkui-textdatadetectorconfig.md)对象的指针。 |

### OH\_ArkUI\_FontWeightConfigs\_Create()

```c
OH_ArkUI_FontWeightConfigs* OH_ArkUI_FontWeightConfigs_Create()
```

**描述**

创建文本字体粗细配置对象。当该对象不再使用时，请调用[OH\_ArkUI\_FontWeightConfigs\_Destroy](capi-text-h.md#oh_arkui_fontweightconfigs_destroy)销毁，以释放资源避免内存泄漏。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_FontWeightConfigs\*](capi-arkui-nativemodule-oh-arkui-fontweightconfigs.md) | 指向文本字体粗细配置对象的指针。如果创建失败，返回空指针。使用后需调用[OH\_ArkUI\_FontWeightConfigs\_Destroy](capi-text-h.md#oh_arkui_fontweightconfigs_destroy)销毁。当配置对象为空指针时，不应用默认值，文本字体粗细行为与父组件保持一致。 |

### OH\_ArkUI\_FontWeightConfigs\_Destroy()

```c
void OH_ArkUI_FontWeightConfigs_Destroy(OH_ArkUI_FontWeightConfigs* option)
```

**描述**

销毁文本字体粗细配置对象。与[OH\_ArkUI\_FontWeightConfigs\_Create](capi-text-h.md#oh_arkui_fontweightconfigs_create)成对使用，否则会导致内存泄漏。

**说明** 

若该对象已被SetFontWeightConfigs设置到FontConfigs中，应在销毁FontConfigs之后再销毁FontWeightConfigs，或在确保FontConfigs不再使用后再销毁FontWeightConfigs，以避免FontConfigs持有无效指针。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_FontWeightConfigs](capi-arkui-nativemodule-oh-arkui-fontweightconfigs.md)\* option | 指向要销毁的文本字体粗细配置对象的指针。 |

### OH\_ArkUI\_FontWeightConfigs\_SetEnableVariableFontWeight()

```c
void OH_ArkUI_FontWeightConfigs_SetEnableVariableFontWeight(OH_ArkUI_FontWeightConfigs* option, bool enable)
```

**描述**

设置是否启用可变字重调节。可变字重调节允许字体在100到900之间以任意整数值显示字重，实现更细腻的字体粗细控制。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_FontWeightConfigs](capi-arkui-nativemodule-oh-arkui-fontweightconfigs.md)\* option | 指向待修改的文本字体粗细配置对象的指针。 |
| bool enable | 是否启用可变字重调节。默认值为false。true表示启用可变字重调节，此时若设置的字重weight为[100, 900]范围内任意整数，则取该值，否则取默认值400。false表示禁用，此时weight仅支持整百数值[100, 900]，非整百数值时取默认值400。 |

### OH\_ArkUI\_FontWeightConfigs\_GetEnableVariableFontWeight()

```c
bool OH_ArkUI_FontWeightConfigs_GetEnableVariableFontWeight(OH_ArkUI_FontWeightConfigs* option)
```

**描述**

获取文本字体粗细配置对象是否启用了可变字重调节。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_FontWeightConfigs](capi-arkui-nativemodule-oh-arkui-fontweightconfigs.md)\* option | 指向文本字体粗细配置对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 是否启用可变字重调节。  true表示启用可变字重调节。此时如果通过相关接口设置的字重weight取值为[100, 900]范围内任意整数，则字重取值为weight，否则取默认值400。  false表示禁用可变字重调节。此时如果设置的字重weight取值为[100, 900]范围内的整百数值，字重取值为weight；weight是非整百数值时，字重取默认值400。  字重weight取值为[100, 900]范围外的值，字重取默认值400。 |

### OH\_ArkUI\_FontWeightConfigs\_SetEnableDeviceFontWeightCategory()

```c
void OH_ArkUI_FontWeightConfigs_SetEnableDeviceFontWeightCategory(OH_ArkUI_FontWeightConfigs* option, bool enable)
```

**描述**

设置设备的字体粗细级别改变时文本字体粗细是否自动更新。设备的字体粗细级别是指系统设置中的全局字体粗细配置，用户可在系统设置中调整。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_FontWeightConfigs](capi-arkui-nativemodule-oh-arkui-fontweightconfigs.md)\* option | 指向待修改的文本字体粗细配置对象的指针。 |
| bool enable | 是否启用文本字体粗细跟随设备的字体粗细级别更新。true表示当设备的字体粗细级别改变时，文本字体粗细将自动更新。false表示当设备的字体粗细级别改变时，文本字体粗细不会自动更新。默认值为true。 |

### OH\_ArkUI\_FontWeightConfigs\_GetEnableDeviceFontWeightCategory()

```c
bool OH_ArkUI_FontWeightConfigs_GetEnableDeviceFontWeightCategory(OH_ArkUI_FontWeightConfigs* option)
```

**描述**

获取文本字体粗细是否跟随设备的字体粗细级别更新。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_FontWeightConfigs](capi-arkui-nativemodule-oh-arkui-fontweightconfigs.md)\* option | 指向文本字体粗细配置对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 文本字体粗细是否跟随设备的字体粗细级别更新。  true表示当设备的字体粗细级别改变时，文本字体粗细将自动更新。  false表示当设备的字体粗细级别改变时，文本字体粗细不会自动更新。 |

### OH\_ArkUI\_FontConfigs\_Create()

```c
OH_ArkUI_FontConfigs* OH_ArkUI_FontConfigs_Create()
```

**描述**

创建文本字体配置对象。当该对象不再使用时，请调用[OH\_ArkUI\_FontConfigs\_Destroy](capi-text-h.md#oh_arkui_fontconfigs_destroy)销毁，以释放资源避免内存泄漏。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_FontConfigs\*](capi-arkui-nativemodule-oh-arkui-fontconfigs.md) | 返回指向文本字体配置对象的指针。如果创建失败，返回空指针。使用后需调用[OH\_ArkUI\_FontConfigs\_Destroy](capi-text-h.md#oh_arkui_fontconfigs_destroy)销毁。 |

### OH\_ArkUI\_FontConfigs\_Destroy()

```c
void OH_ArkUI_FontConfigs_Destroy(OH_ArkUI_FontConfigs* option)
```

**描述**

销毁文本字体配置对象。与[OH\_ArkUI\_FontConfigs\_Create](capi-text-h.md#oh_arkui_fontconfigs_create)成对使用，否则会导致内存泄漏。

**说明** 

销毁FontConfigs前，应先销毁通过SetFontWeightConfigs设置的FontWeightConfigs对象（如果不再使用），或确保FontWeightConfigs的生命周期长于FontConfigs，以避免悬空指针问题。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_FontConfigs](capi-arkui-nativemodule-oh-arkui-fontconfigs.md)\* option | 指向要销毁的文本字体配置对象的指针。 |

### OH\_ArkUI\_FontConfigs\_SetFontWeightConfigs()

```c
void OH_ArkUI_FontConfigs_SetFontWeightConfigs(OH_ArkUI_FontConfigs* option, OH_ArkUI_FontWeightConfigs* fontWeightConfigs)
```

**描述**

设置文本字体配置对象的文本字体粗细配置。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_FontConfigs](capi-arkui-nativemodule-oh-arkui-fontconfigs.md)\* option | 指向待修改的文本字体配置对象的指针。 |
| [OH\_ArkUI\_FontWeightConfigs](capi-arkui-nativemodule-oh-arkui-fontweightconfigs.md)\* fontWeightConfigs | 文本字体粗细配置。当该配置不为空指针时，若用户未显式设置，各项配置将使用默认值（可变字重调节默认为禁用，文本字体粗细跟随设备字体粗细级别更新默认为启用）。当该配置为空指针时，不应用上述默认值，文本字体粗细行为与父组件保持一致。 |

### OH\_ArkUI\_FontConfigs\_GetFontWeightConfigs()

```c
OH_ArkUI_FontWeightConfigs* OH_ArkUI_FontConfigs_GetFontWeightConfigs(OH_ArkUI_FontConfigs* option)
```

**描述**

获取文本字体配置对象的文本字体粗细配置。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_FontConfigs](capi-arkui-nativemodule-oh-arkui-fontconfigs.md)\* option | 指向文本字体配置对象的指针。若未设置或设置时为空指针，则返回空指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_FontWeightConfigs\*](capi-arkui-nativemodule-oh-arkui-fontweightconfigs.md) | 文本字体粗细配置。 |

### OH\_ArkUI\_TextController\_Create()

```c
OH_ArkUI_TextController* OH_ArkUI_TextController_Create()
```

**描述**

创建一个文本控制器对象。当该对象不再使用时，请调用[OH\_ArkUI\_TextController\_Destroy](capi-text-h.md#oh_arkui_textcontroller_destroy)销毁，以释放资源避免内存泄漏。

**起始版本：** 26.0.0

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_TextController\*](capi-arkui-nativemodule-oh-arkui-textcontroller.md) | 指向文本组件控制器对象的指针。如果创建失败，返回空指针。使用后需调用[OH\_ArkUI\_TextController\_Destroy](capi-text-h.md#oh_arkui_textcontroller_destroy)销毁。 |

### OH\_ArkUI\_TextController\_Destroy()

```c
void OH_ArkUI_TextController_Destroy(OH_ArkUI_TextController* controller)
```

**描述**

销毁文本控制器对象。与[OH\_ArkUI\_TextController\_Create](capi-text-h.md#oh_arkui_textcontroller_create)成对使用，否则会导致内存泄漏。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_TextController](capi-arkui-nativemodule-oh-arkui-textcontroller.md)\* controller | 指向文本组件控制器对象的指针。 |
