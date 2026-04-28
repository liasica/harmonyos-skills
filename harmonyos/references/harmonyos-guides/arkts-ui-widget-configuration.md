---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-configuration
title: 配置ArkTS卡片的配置文件
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > 配置ArkTS卡片的配置文件
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:91215737e703f5ef9f5576798bef43e7ad735d4f5fddfcce7dd38270eb0ab73d
---

卡片相关的配置文件包括[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)配置和卡片配置。如果是[独立卡片包](arkts-ui-widget-creation.md#方式二独立包方式创建卡片)，还会包含[独立卡片包配置](arkts-ui-widget-configuration.md#独立卡片包配置)。

说明

* 卡片五元组是确认卡片唯一的要素信息。五元组分别为bundleName、moduleName、abilityName、formName、formDimension。其中bundleName是[app.json5配置文件标签](app-configuration-file.md#配置文件标签)中bundleName配置项、moduleName是[module.json5配置文件标签](module-configuration-file.md#配置文件标签)中的name配置项、abilityName是[abilities标签](module-configuration-file.md#abilities标签)中的name配置项、formName是[配置文件字段说明](arkts-ui-widget-configuration.md#配置文件字段说明)中的name配置项、formDimension对应的是[配置文件字段说明](arkts-ui-widget-configuration.md#配置文件字段说明)中的supportDimensions配置项。
* 五元组不建议使用资源文件导入配置。使用资源文件导入时，资源文件新增字段等，对应的ID都会发生改变，会被认为五元组有改变。
* 如果应用升级后五元组有改变，系统中对应的卡片会被删除，在屏幕上会消失。

## FormExtensionAbility配置

卡片需要在[module.json5配置文件](module-configuration-file.md)的extensionAbilities标签下，配置FormExtensionAbility相关信息。FormExtensionAbility需要填写metadata元信息标签，其中键名称为固定字符串 “ohos.extension.form”，资源为[卡片具体配置信息的资源索引](arkts-ui-widget-configuration.md#卡片配置)。

配置示例如下：

```
1. {
2. "module": {
3. // ...
4. "extensionAbilities": [
5. {
6. "name": "EntryFormAbility",
7. "srcEntry": "./ets/entryformability/EntryFormAbility.ets",
8. "label": "$string:EntryFormAbility_label",
9. "description": "$string:EntryFormAbility_desc",
10. "type": "form",
11. "metadata": [
12. {
13. "name": "ohos.extension.form",
14. "resource": "$profile:form_config"
15. }
16. ]
17. }
18. ],
19. // 只在独立卡片包形态中会使用，用来关联卡片包模块。
20. "formWidgetModule": "library"
21. }
22. }
```

## 独立卡片包配置

相对应地，在卡片包的[module.json5配置文件](module-configuration-file.md)中，formExtensionModule字段用来关联应用包的module。

配置示例如下：

```
1. {
2. "module": {
3. "name": "library",
4. "type": "shared",
5. "description": "$string:shared_desc",
6. "deviceTypes": [
7. "phone"
8. ],
9. "deliveryWithInstall": true,
10. // 只在独立卡片包形态中会使用，用来关联应用包模块。
11. "formExtensionModule": "entry"
12. }
13. }
```

## 卡片配置

在上述FormExtensionAbility的元信息metadata配置项中，可以指定卡片具体配置信息的资源索引。例如当resource指定为$profile:form\_config时，会使用开发视图的resources/base/profile/目录下的form\_config.json作为卡片profile配置文件。在[创建卡片](arkts-ui-widget-creation.md)时会自动生成form\_config.json配置文件。

### 配置文件字段说明

**表1** 卡片form\_config.json配置文件

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| forms | 表示应用的全部卡片配置信息。  最多支持配置16个卡片，若超过16个，则保留配置的前16个。 | 数组 | 否 |
| name | 表示卡片的名称，字符串最大长度为127字节。用于开发者区分不同的卡片。  **说明：**  该字段不建议引用资源文件。 | 字符串 | 否 |
| displayName | 表示卡片的展示名称。主要在卡片管理页面显示，对应卡片预览下[卡片管理页面](formkit-overview.md#卡片使用场景)中的"cardName"，用于展示卡片信息，建议能够体现卡片的核心功能或用途。支持字符串或字符串资源索引，建议使用字符串资源索引方式声明，以支持完整多语言能力。字符串最小长度为1字节，最大长度为30字节。 | 字符串 | 否 |
| description | 表示卡片的描述。用于在卡片管理页面展示卡片功能描述，对应卡片预览下[卡片管理页面](formkit-overview.md#卡片使用场景)中的"This is a service widget."。支持字符串或字符串资源索引，建议使用字符串资源索引方式声明，以支持完整多语言能力。字符串最大长度为255字节。 | 字符串 | 可缺省，缺省为空。 |
| src | 表示卡片对应的UI代码的完整路径。当为ArkTS卡片时，完整路径需要包含卡片文件的后缀，如："./ets/widget/pages/WidgetCard.ets"。当为JS卡片时，完整路径无需包含卡片文件的后缀，如："./js/widget/pages/WidgetCard"。 | 字符串 | 否 |
| uiSyntax | 表示该卡片的类型，当前支持如下两种类型：  - arkts：当前卡片为ArkTS卡片。  - hml：当前卡片为JS卡片。 | 字符串 | 可缺省，缺省值为“hml”。 |
| window | 用于定义与显示窗口相关的配置。  **说明：**  该字段仅对JS卡片生效。 | 对象 | 可缺省，缺省值参考[window标签](arkts-ui-widget-configuration.md#window标签)表格。 |
| isDefault | 表示该卡片是否为默认卡片(在卡片中心内希望优先展示的卡片)，每个应用有且只有一个默认卡片。  - true：默认卡片。  - false：非默认卡片。  **说明：**  应用上架时每个应用只允许配置一张默认卡片。 | 布尔值 | 否 |
| colorMode(deprecated) | 表示卡片的主题样式，取值范围如下：  - auto：跟随系统的颜色模式值选取主题。  - dark：深色主题。  - light：浅色主题。  **说明：**  1. 从API version 12开始支持该配置项，从API version 20开始废弃该配置项，卡片主题样式统一跟随系统的颜色模式。  2. 该字段仅对JS卡片生效。 | 字符串 | 可缺省，缺省值为“auto”。 |
| supportDimensions | 表示卡片支持的外观规格，取值范围：  - 1 \* 1：表示1行1列的一宫格。  - 1 \* 2：表示1行2列的二宫格。  - 2 \* 2：表示2行2列的四宫格。  - 2 \* 4：表示2行4列的八宫格。  - 2 \* 3：表示2行3列的六宫格。  - 3 \* 3：表示3行3列的九宫格。  - 4 \* 4：表示4行4列的十六宫格。  - 6 \* 4：表示6行4列的二十四宫格。  **说明**： 2 \* 3和 3 \* 3仅支持手表设备， 1 \* 1只支持在锁屏上使用。 | 字符串数组 | 否 |
| defaultDimension | 表示卡片的默认尺寸，取值必须在该卡片supportDimensions配置的列表中。 | 字符串 | 否 |
| updateEnabled | 表示卡片是否支持周期性刷新（包含定时刷新和定点刷新），取值范围：  - true：表示支持周期性刷新，可以在定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式任选其一，当两者同时配置时，定时刷新优先生效。  - false：表示不支持周期性刷新。 | 布尔类型 | 否 |
| scheduledUpdateTime | 表示卡片的[定点刷新](arkts-ui-widget-passive-refresh.md#卡片定点刷新)的时刻，采用24小时制，精确到分钟，例如："10:30"。  **说明：**  updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 | 字符串 | 可缺省，缺省值为“0:0”，缺省时不进行定点刷新。 |
| updateDuration | 表示[卡片定时刷新](arkts-ui-widget-passive-refresh.md#卡片定时刷新)的更新周期，单位为30分钟，取值为自然数。  当取值为0时，表示该参数不生效。  当取值为正整数N时，表示刷新周期为30\*N分钟。  **说明：**  updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 | 数值 | 可缺省，缺省值为0。 |
| formConfigAbility | 表示桌面点击编辑后，需要拉起的ability路径，采用URI格式。 | 字符串 | 可缺省，缺省值为空。 |
| metadata | 表示卡片的自定义信息，参考[Metadata](../harmonyos-references/js-apis-bundlemanager-metadata.md)数组标签。 | 对象 | 可缺省，缺省值为空。 |
| isDynamic | 表示此卡片是否为动态卡片（仅针对ArkTS卡片生效）。  - true：为[动态卡片](arkts-form-overview.md#动态卡片) 。  - false：为[静态卡片](arkts-form-overview.md#静态卡片)。 | 布尔类型 | 可缺省，缺省值为true。 |
| fontScaleFollowSystem | 表示卡片使用方设置此卡片的字体是否支持跟随系统变化。  - true：支持跟随系统字体大小变化。  - false：不支持跟随系统字体大小变化。 | 布尔类型 | 可缺省，缺省值为true。 |
| supportShapes | 表示卡片的显示形状，取值范围如下：  - rect：表示矩形卡片。  - circle：表示圆形卡片。 | 字符串数组 | 可缺省，缺省值：["rect"]。 |
| previewImages | 表示卡片预览图, 与配置项supportDimensions一一对应。智能穿戴卡片必须配置，当前仅支持在智能穿戴上使用。 | 字符串数组 | 可缺省，缺省值：[]。 |
| transparencyEnabled | 表示是否为背板透明卡片（仅对系统应用或者申请了背板透明卡片能力的ArkTS卡片生效）。  - true：表示是背板透明卡片。  - false：表示不是背板透明卡片。 | 布尔类型 | 可缺省，缺省值为false。 |
| enableBlurBackground | 表示卡片是否使用模糊背板。  - true：开启模糊背板。  - false：关闭模糊背板。  **说明：**  本特性对产品功耗、性能要求较高，从API version 23开始仅在旗舰机型上支持，在不支持的机型上调用后不生效。 | 布尔类型 | 可缺省，缺省值为false。 |
| renderingMode | 表示卡片的渲染模式，取值范围如下：  - autoColor：自动模式，呈现效果可以根据卡片使用方确定最终是全彩模式还是单色模式，具体请参考[卡片色彩](../design-guides/system-features-service-widget-0000002087671904.md#section295mcpsimp)。该模式下卡片中的颜色和图片允许卡片使用方修改，卡片配置了该模式就可以添加到桌面或锁屏上。  - fullColor：全彩模式，具体请参考[卡片色彩](../design-guides/system-features-service-widget-0000002087671904.md#section295mcpsimp)。该模式下卡片中的颜色和图片不允许被卡片使用方修改，卡片配置了该模式就可以添加到桌面上。  - singleColor：单色模式，通过透明度和模糊区分元素，不使用任何色相，具体请参考[卡片色彩](../design-guides/system-features-service-widget-0000002087671904.md#section295mcpsimp)。该模式下卡片中的颜色和图片允许卡片使用方修改，卡片配置了该模式就可以添加到锁屏上。  **说明：**  从API version 15开始，支持该字段。 | 字符串 | 可缺省，缺省值为“fullColor”。 |
| multiScheduledUpdateTime | 表示卡片的多定点刷新的时刻，作为单点刷新的一个附加参数，采用24小时制，精确到分钟，多个时间用英文逗号分隔，最多写24个时间。  **说明：**  从API version 18开始，支持该字段。multiScheduledUpdateTime需要配合scheduledUpdateTime使用。 | 字符串 | 可缺省，缺省时不进行多定点刷新。 |
| conditionUpdate | 表示卡片的支持的条件刷新（仅对系统应用的ArkTS卡片生效）。取值范围如下：  - network：表示支持网络刷新。  **说明：**  从API version 18开始，支持该字段。 | 字符串数组 | 可缺省，缺省值为空字符串数组。 |
| [funInteractionParams](arkts-ui-widget-configuration.md#funinteractionparams标签) | 趣味交互类型互动卡片扩展字段。从API version 20开始，支持该字段。 | 对象 | 可缺省，缺省为空。funInteractionParams 和 sceneAnimationParams 同时配置时识别为趣味交互类型互动卡片。 |
| [sceneAnimationParams](arkts-ui-widget-configuration.md#sceneanimationparams标签) | [场景动效类型互动卡片](arkts-ui-liveform-sceneanimation-overview.md)扩展字段。从API version 20开始，支持该字段。 | 对象 | 可缺省，缺省为空。funInteractionParams 和 sceneAnimationParams 同时配置时识别为趣味交互类型互动卡片。 |
| resizable | 表示是否可以拖拽卡片调整大小。调整值必须在该卡片或者同groupId卡片的supportDimensions配置列表中。  - true：可以调整大小。  - false：不可以调整大小。  **说明：**  从API version 20开始，支持该字段。 | 布尔类型 | 可缺省，缺省值为false。 |
| groupId | 表示一组卡片的共同id。多张卡片的groupId相同且resizable为true时，多张卡片的supportDimensions配置共享，推荐多张卡片功能相同且需要调整卡片尺寸时配置。  示例一：卡片A的groupId配置为'1'，resizeable配置为true，supportDimension为2\*2。卡片B的groupId配置为'1'，resizeable配置为true，supportDimension为2\*4。那么支持卡片A、B之间调整大小。  示例二：当supportDimension存在多个，resizable设置为true时，优先在同一张卡片之间调整大小。卡片A的resizeable配置为true，supportDimension为2\*2、2\*4，支持卡片A的两个尺寸之间调整大小。  示例三：卡片A的groupId配置为'1'，resizeable配置为true，supportDimension为1\*2。卡片B的groupId配置为'1'，resizeable配置为true，supportDimension为2\*2、2\*4、4\*4。卡片A可以调整到卡片B的默认尺寸，卡片B只支持在B卡片支持的三个尺寸之间调整大小，无法调整为卡片A。  **说明：**  从API version 20开始，支持该字段。 | 字符串 | 可缺省，空字符串。 |
| [supportDeviceTypes](arkts-ui-widget-configuration.md#supportdevicetypes标签) | 表示特定卡片支持的设备类型。例如，卡片的supportDeviceTypes字段配置了“phone”、“tablet”、“tv”，那么该卡片就支持在手机、平板、大屏上面显示。  **说明：**  从API version 22开始，支持该字段。 | 字符串数组 | 可缺省，缺省值：["phone", "tablet", "tv", "wearable", "car", "2in1"]。 |
| [supportDevicePerformanceClasses](arkts-ui-widget-configuration.md#supportdeviceperformanceclasses标签) | 表示特定卡片支持的设备性能等级信息。例如，卡片的supportDevicePerformanceClasses字段配置了“high”、“medium”、“low”，那么该卡片就支持在性能等级为“high”、“medium”、“low”设备上面显示。  **说明：**  从API version 22开始，支持该字段。 | 字符串数组 | 可缺省，缺省值：["high", "medium", "low"]。 |
| [standby](arkts-ui-widget-configuration.md#standby标签) | 待机屏保显示页面卡片扩展字段。  **说明：**  从API version 23开始，支持该字段。依赖系统实现待机屏保显示应用后展示 | 对象 | 可缺省，属性缺省值见[standby标签](arkts-ui-widget-configuration.md#standby标签)。 |

### supportDeviceTypes标签

此标签标识卡片支持的设备类型。

| 属性名称 | 含义 | 数据类型 |
| --- | --- | --- |
| phone | 手机设备。 | 字符串 |
| tablet | 平板设备。 | 字符串 |
| tv | 智慧屏设备。 | 字符串 |
| wearable | 智能手表设备。 | 字符串 |
| car | 车机设备。 | 字符串 |
| 2in1 | PC/2in1设备。 | 字符串 |

### supportDevicePerformanceClasses标签

此标签标识卡片支持的设备性能等级信息。

| 属性名称 | 含义 | 数据类型 |
| --- | --- | --- |
| high | 表示设备能力定级为高。 | 字符串 |
| medium | 表示设备能力定级为中。 | 字符串 |
| low | 表示设备能力定级为低。 | 字符串 |

### window标签

此标签标识window对象的内部结构说明。只支持在JS卡片中使用。

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| designWidth | 标识页面设计基准宽度。以此为基准，根据实际设备宽度来缩放元素大小。 | 数值 | 可缺省，缺省值为720px。 |
| autoDesignWidth | 标识页面设计基准宽度是否自动计算。当配置为true时，designWidth将会被忽略，设计基准宽度由设备宽度与屏幕密度计算得出。 | 布尔值 | 可缺省，缺省值为false。 |

### funInteractionParams标签

此标签标识趣味交互类型互动卡片配置。funInteractionParams 和 sceneAnimationParams 同时配置时识别为趣味交互类型互动卡片。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abilityName | 字符串 | 否 | 趣味交互场景LiveFormExtensionAbility名称，默认为空。 |
| targetBundleName | 字符串 | 是 | 趣味交互场景[主包包名](../quickApp-Guides/quickgame-independent-subpackage-0000002076341729.md)。 |
| subBundleName | 字符串 | 否 | 趣味交互场景[独立分包名](../quickApp-Guides/quickgame-independent-subpackage-0000002076341729.md)，默认为空。 |
| keepStateDuration | 数值 | 否 | 趣味交互场景无交互时，激活态保持时长。默认值为10000，单位ms。取值为[0,10000]的整数，超过取值范围则取默认值10000。 |

```
1. {
2. "forms": [
3. {
4. // ...
5. "funInteractionParams": {
6. "targetBundleName": "com.example.funInteraction",
7. "subBundleName": "com.example.subFunInteraction"
8. }
9. }
10. ]
11. }
```

### sceneAnimationParams标签

此标签标识场景动效类型互动卡片配置。funInteractionParams 和 sceneAnimationParams 同时配置时识别为趣味交互类型互动卡片。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abilityName | 字符串 | 是 | 场景动效LiveFormExtensionAbility名称。 |

```
1. {
2. "forms": [
3. {
4. // ...
5. "sceneAnimationParams": {
6. "abilityName": "MyLiveFormExtensionAbility"
7. }
8. }
9. ]
10. }
```

### standby标签

此标签标识standby对象的内部结构说明。应用通过开放能力申请，且卡片isSupported配置为true才支持在待机屏保显示界面展示。

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| isSupported | 标识卡片是否支持在待机屏保显示界面展示。  - true：表示卡片支持在待机屏保显示界面展示。  - false：表示卡片不支持在待机屏保显示界面展示。 | 布尔值 | 可缺省，缺省值为true。 |
| isAdapted | 标识卡片是否针对待机屏保显示界面做过适配，配置成true，会把卡片布局组件中backgroudimage移除。  - true：表示卡片适配过待机屏保显示界面。  - false：表示卡片没有适配过待机屏保显示界面。 | 布尔值 | 可缺省，缺省值为false。 |
| isPrivacySensitive | 标识卡片是否是隐私敏感卡片，隐私敏感卡片在待机屏保显示界面展示会用蒙层覆盖。  - true：表示卡片是隐私敏感卡片。  - false：表示卡片不是隐私敏感卡片。 | 布尔值 | 可缺省，缺省值为false。 |

```
1. {
2. "forms": [
3. {
4. // ...
5. "standby": {
6. "isSupported": true,
7. "isAdapted": false,
8. "isPrivacySensitive": false
9. }
10. }
11. ]
12. }
```

### 配置文件示例

```
1. {
2. "forms": [
3. {
4. "name": "widget",
5. "displayName": "$string:widget_display_name",
6. "description": "$string:widget_desc",
7. "src": "./ets/widget/pages/WidgetCard.ets",
8. "uiSyntax": "arkts",
9. "window": {
10. "designWidth": 720,
11. "autoDesignWidth": true
12. },
13. "renderingMode": "fullColor",
14. "isDefault": true,
15. "updateEnabled": true,
16. "scheduledUpdateTime": "10:30",
17. "updateDuration": 1,
18. "defaultDimension": "2*2",
19. "supportDimensions": [
20. "2*2"
21. ],
22. "formConfigAbility": "ability://EntryAbility",
23. "isDynamic": true,
24. "metadata": []
25. }
26. ]
27. }
```
