---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-categories-and-access
title: 资源分类与访问
breadcrumb: 指南 > 基础入门 > 资源分类与访问
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e52f5b01a24bd4495674c75ba837c4b4988163771a167b7cace7dc5aec71bca7
---

## 功能介绍

在应用开发中，常需使用字符串、颜色、字体、间距和图标等资源。为了让应用在不同设备（如手机、平板、车机）和配置（如语言、屏幕密度、颜色模式）下都能提供最佳体验，系统支持通过资源动态匹配机制，自动为各类场景选取最合适的资源。本文档将介绍资源类型与组织方式，并提供资源开发指导。

根据来源差异，资源可分为系统资源和应用资源。系统资源是系统提供的资源，开发者可以通过[主题图标库](../design-guides/system-icons-0000001929854962.md)、[系统色彩全量表](../design-guides/color-0000001776857164.md#section17672143841113)、[字体](../design-guides/font-0000001828772001.md#section107781129418)获取系统图标、颜色、字体等资源信息。其中symbol图标还可通过[SymbolGlyph](../harmonyos-references/ts-basic-components-symbolglyph.md)对图标颜色等进一步设置。应用资源是开发者在应用中自定义的资源，可以利用资源文件管理资源在不同的设备或配置中的表现。

## 资源分类

应用开发中使用的各类资源文件，需要放入特定子目录中存储管理。目录结构如下所示，base目录、限定词目录、rawfile目录、resfile目录称为资源目录，element、media、profile称为资源组目录。

```
1. resources
2. |---base  // 默认存在的目录
3. |   |---element
4. |   |   |---string.json // 字符串资源
5. |   |---media
6. |   |   |---icon.png // 图片、视频等媒体资源文件
7. |   |---profile
8. |   |   |---test_profile.json // 自定义profile文件，文件内容可自定义
9. |---en_GB-vertical-car-mdpi // 自定义限定词目录示例，由开发者创建
10. |   |---element
11. |   |   |---string.json
12. |   |---media
13. |   |   |---icon.png
14. |   |---profile
15. |   |   |---test_profile.json
16. |---rawfile // 其他类型文件，原始文件形式保存，不会被集成到resources.index文件中。文件名可自定义。
17. |---resfile // 其他类型文件，原始文件形式保存，不会被集成到resources.index文件中。文件名可自定义。
```

说明

* 资源目录和资源组目录下的文件均被视为资源文件，在应用打包时不会进行混淆。
* stage模型多工程情况下，共有的资源文件放到AppScope下的resources目录。
* 在编译构建时，AppScope目录下的资源文件会合入到模块下面的资源文件中，如果两个目录下的相同资源目录和资源组目录下存在重名资源，编译打包后只会保留AppScope目录下的资源。
* 非resources目录下资源打包策略请参考[copyCodeResource](ide-hvigor-build-profile.md#table1476161719356)描述。

### 资源目录

表1 资源目录说明

| 目录类型 | 说明 |
| --- | --- |
| base目录 | base目录默认存在。二级子目录element用于存放字符串、颜色、布尔值等基础元素，media和profile子目录存放媒体、动画、布局等资源文件。  目录中的资源文件会被编译成二进制文件，并分配资源ID。通过指定资源类型（type）和资源名称（name）来访问。 |
| 限定词目录 | 限定词目录需要开发者根据开发需要自行创建，二级子目录element用于存放字符串、颜色、布尔值等基础元素，media和profile子目录存放媒体、动画、布局等资源文件。  同样，目录中的资源文件会被编译成二进制文件，并分配资源ID。通过指定资源类型（type）和资源名称（name）来访问。限定词的含义和取值范围以及限定词目录的命名规则请参考下方[限定词目录](resource-categories-and-access.md#限定词目录)中的说明。 |
| rawfile目录 | 支持创建多层子目录，子目录名称可以自定义，文件夹内可以自由放置各类资源文件。  目录中的资源文件会被直接打包进应用，不经过编译，也不会分配资源ID。通过指定文件路径和文件名访问。 |
| resfile目录 | 支持创建多层子目录，子目录名称可以自定义，文件夹内可以自由放置各类资源文件。  目录中的资源文件会被直接打包进应用，不经过编译，也不会分配资源ID。应用安装后，resfile资源会被解压到应用沙箱路径，通过Context属性[resourceDir](../harmonyos-references/js-apis-inner-application-context.md#属性)获取到resfile资源目录后，可通过文件路径访问，且该路径仅能以只读方式访问。 |

### 资源组目录

表2 资源组目录说明

| 目录类型 | 说明 | 资源文件 |
| --- | --- | --- |
| element | 表示元素资源，以下每一类数据都采用相应的JSON文件来表征（目录下仅支持文件类型）。  - boolean，布尔型  - color，颜色  - float，浮点型，范围是-2^128到2^128  - intarray，整型数组  - integer，整型，范围是-2^31到2^31-1  - plural，复数形式  - strarray，字符串数组  - string，字符串，[格式化字符串请参考API文档](../harmonyos-references/js-apis-resource-manager.md#getstringsync10) | element目录中的文件名称建议与下面的文件名保持一致。每个文件中只能包含同一类型的数据。  - boolean.json  - color.json  - float.json  - intarray.json  - integer.json  - plural.json  - strarray.json  - string.json |
| media | 表示媒体资源，包括图片、音频、视频等非文本格式的文件（目录下只支持文件类型）。  图片和音视频的类型说明见表3和表4。 | 文件名可自定义，例如：icon.png。 |
| profile | 表示自定义配置文件，其文件内容可[通过包管理接口](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetprofilebyability)获取（目录下只支持json文件类型）。 | 文件名可自定义，例如：test\_profile.json。 |

**媒体资源类型说明**

表3 图片资源类型说明

| 格式 | 文件后缀名 |
| --- | --- |
| JPEG | .jpg |
| PNG | .png |
| GIF | .gif |
| SVG | .svg |
| WEBP | .webp |
| BMP | .bmp |

表4 音视频资源类型说明

| 格式 | 支持的文件类型 |
| --- | --- |
| H.264 AVC | .3gp |
| Baseline Profile (BP) | .mp4 |

### 限定词目录

限定词目录由一个或多个表征应用场景或设备特征的限定词组合而成，限定词包括移动国家码和移动网络码、语言、文字、国家或地区、横竖屏、设备类型、颜色模式和屏幕密度，限定词之间通过下划线（\_）或者中划线（-）连接。开发者在创建限定词目录时，需要遵守如下限定词目录命名规则。

* 限定词的组合顺序：移动国家码\_移动网络码-语言\_文字\_国家或地区-横竖屏-设备类型-颜色模式-屏幕密度。开发者可以根据应用的使用场景和设备特征，选择其中的一类或几类限定词组成目录名称。
* 限定词的连接方式：移动国家码和移动网络码之间采用下划线（\_）连接，语言、文字、国家或地区之间也采用下划线（\_）连接，除此之外的其他限定词之间均采用中划线（-）连接。例如：**mcc460\_mnc00-zh\_Hant\_CN**、**zh\_CN-car-ldpi**。
* 限定词的取值范围：每类限定词的取值必须符合限定词取值要求表中的条件，如表5。否则，将无法匹配目录中的资源文件。

表5 限定词取值要求

| 限定词类型 | 含义与取值说明 |
| --- | --- |
| 移动国家码和移动网络码 | 移动国家码（MCC）和移动网络码（MNC）的值取自设备注册的网络。  MCC可与MNC合并使用，使用下划线（\_）连接，也可以单独使用。例如：mcc460表示中国，mcc460\_mnc00表示中国\_中国移动。  详细取值范围，请查阅[**ITU-T E.212**](https://www.itu.int/rec/T-REC-E.212)（国际电联相关标准）。 |
| 语言 | 表示设备使用的语言类型，由2~3个小写字母组成。例如：zh表示中文，en表示英语，mai表示迈蒂利语。  详细取值范围，请查阅[**ISO 639**](https://www.iso.org/iso-639-language-code)（ISO制定的语言编码标准）。 |
| 文字 | 表示设备使用的文字类型，由1个大写字母（首字母）和3个小写字母组成。例如：Hans表示简体中文，Hant表示繁体中文。  详细取值范围，请查阅[**ISO 15924**](https://www.iso.org/standard/81905.html)（ISO制定的文字编码标准）。 |
| 国家或地区 | 表示用户所在的国家或地区，由2~3个大写字母或者3个数字组成。例如：CN表示中国，GB表示英国。  详细取值范围，请查阅[**ISO 3166-1**](https://www.iso.org/iso-3166-country-codes.html)（ISO制定的国家和地区编码标准）。 |
| 横竖屏 | 表示设备的屏幕方向，取值如下：  - vertical：竖屏  - horizontal：横屏 |
| 设备类型 | 表示设备的类型，取值如下：  - phone：手机  - car：车机  - tablet：平板  - tv：智慧屏  - wearable：智能穿戴  - 2in1：PC设备 |
| 颜色模式 | 表示设备的颜色模式，取值如下：  - dark：深色模式  - light：浅色模式 |
| 屏幕密度 | 表示设备的屏幕密度（单位为dpi），取值如下：  - sdpi：表示小规模的屏幕密度（Small-scale Dots Per Inch），适用于dpi取值为(0, 120]的设备。  - mdpi：表示中规模的屏幕密度（Medium-scale Dots Per Inch），适用于dpi取值为(120, 160]的设备。  - ldpi：表示大规模的屏幕密度（Large-scale Dots Per Inch），适用于dpi取值为(160, 240]的设备。  - xldpi：表示特大规模的屏幕密度（Extra Large-scale Dots Per Inch），适用于dpi取值为(240, 320]的设备。  - xxldpi：表示超大规模的屏幕密度（Extra Extra Large-scale Dots Per Inch），适用于dpi取值为(320, 480]的设备。  - xxxldpi：表示超特大规模的屏幕密度（Extra Extra Extra Large-scale Dots Per Inch），适用于dpi取值为(480, 640]的设备。 |

### 资源文件示例

color.json文件的内容如下：

标准的十六进制颜色值由八位十六进制数字组成，前两位表示透明度，后六位表示颜色值。

```
1. {
2. "color": [
3. {
4. "name": "color_hello",
5. "value": "#ffff0000"
6. },
7. {
8. "name": "color_world",
9. "value": "#ff0000ff"
10. }
11. ]
12. }
```

float.json文件的内容如下：

```
1. {
2. "float": [
3. {
4. "name": "font_hello",
5. "value": "28.0fp"
6. },
7. {
8. "name": "font_world",
9. "value": "20.0fp"
10. }
11. ]
12. }
```

string.json文件的内容如下：

```
1. {
2. "string": [
3. {
4. "name": "string_hello",
5. "value": "Hello"
6. },
7. {
8. "name": "string_world",
9. "value": "World"
10. },
11. {
12. "name": "message_arrive",
13. "value": "We will arrive at %1$s."
14. },
15. {
16. "name": "message_notification",
17. "value": "Hello, %1$s!,You have %2$d new messages."
18. }
19. ]
20. }
```

plural.json文件的内容如下：

```
1. {
2. "plural": [
3. {
4. "name": "eat_apple",
5. "value": [
6. {
7. "quantity": "one",
8. "value": "%d apple"
9. },
10. {
11. "quantity": "other",
12. "value": "%d apples"
13. }
14. ]
15. }
16. ]
17. }
```

## 创建资源目录和资源文件

在resources目录下，可按照限定词目录命名规则和资源组目录支持的文件类型，创建资源目录和资源组目录，添加特定类型资源。DevEco Studio支持同时创建资源目录和资源文件，也支持单独创建资源目录或资源文件。

### 创建资源目录和资源文件

在resources目录右键菜单选择“New > Resource File”，可同时创建资源目录和资源文件，文件默认创建在base目录的对应资源组中。如果选择了限定词，则会按照命名规范自动生成限定词和资源组目录，并将文件创建在限定词目录中。

不同类型的限定词可以组合，如同时选择Locale为zh\_CN，ColorMode为Dark，将创建zh\_CN-dark目录，具体组合规则参考[限定词目录](resource-categories-and-access.md#限定词目录)。

图中File name为需要创建的文件名。Resource type为资源组类型，默认是element。Root Element为资源类型。Available qualifiers为供选择的限定词目录，通过右边的小箭头可添加或者删除。

创建的目录名自动生成，格式固定为“限定词.资源组”，例如：创建一个限定词为dark的element目录，自动生成的目录名称为“dark/element”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/eqsNJ9AGRwW24qte__6ICA/zh-cn_image_0000002583477483.png?HW-CC-KV=V1&HW-CC-Date=20260427T233733Z&HW-CC-Expire=86400&HW-CC-Sign=C74CFE7F9FB12F39A9137D148137F983F25C08A7694529FA100866F8A8DFF414)

### 创建资源目录

在resources目录右键菜单选择“New > Resource Directory”，可创建资源目录，默认创建的是base目录。如果选择了限定词，则会按照命名规范自动生成限定词和资源组目录。确定限定词后，选择资源组类型，当前资源组类型支持Element、Media、Profile三种，创建后生成资源目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/ohautW_4Tm2pVgO332DRyQ/zh-cn_image_0000002552797834.png?HW-CC-KV=V1&HW-CC-Date=20260427T233733Z&HW-CC-Expire=86400&HW-CC-Sign=30452A1A8BC989354F58805923BBB814071101BA1B9EB8B06DF1ADC2D9ED5DB7)

### 创建资源文件

在资源组目录（element、media、profile）的右键菜单选择“New > XXX Resource File”，可创建对应资源组目录的资源文件。例如，在element目录下可新建Element Resource File。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/MFnAiYETQ8CNNgM0Tzx28Q/zh-cn_image_0000002583437529.png?HW-CC-KV=V1&HW-CC-Date=20260427T233733Z&HW-CC-Expire=86400&HW-CC-Sign=C72606E11C99772D6B9F0339B124F5FD83CA94BECF248DFFD7E7A097B0121E6F)

### 示例

以创建中文和英文字符串资源文件为例，说明如何创建不同限定词的资源。

1. 在resources目录右键菜单选择“New > Resource File”，File name填写为string\_sample，Resource type选择Element，Root Element选择string，Available qualifiers选中Locale，在右侧的语言列表中选择zh，地区列表中选择CN，将会在resources目录下创建zh\_CN/element/string\_sample.json文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/MTI1bnnvR-Wwe_9vIprc_w/zh-cn_image_0000002552957484.png?HW-CC-KV=V1&HW-CC-Date=20260427T233733Z&HW-CC-Expire=86400&HW-CC-Sign=0CE3068E23B9B1E5C1FE954CA5E9ED0CE06860B3AE8288A1B18D009E430A8EAE)
2. 同理，语言选择en，地区选择US，创建en\_US/element/string\_sample.json文件。

   最终创建的资源文件如下。资源文件创建完成后，如何访问资源文件请参见[资源访问](resource-categories-and-access.md#资源访问)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/6RYwEv3eRbeoJb7Hq2TGyQ/zh-cn_image_0000002583477485.png?HW-CC-KV=V1&HW-CC-Date=20260427T233733Z&HW-CC-Expire=86400&HW-CC-Sign=69C41B7C635857AD7A2BFB03C4F4C23E52A187A575EAA1A37576468813F3E510)

## 资源可翻译特性

### 功能介绍

当应用引用的字符串资源需要支持国际化多语言翻译时，可使用attr属性标记字符串翻译范围和翻译状态。attr属性不参与资源编译，只标记字符串是否翻译。

未配置attr属性时，默认需要翻译。

**attr支持属性**

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| translatable | boolean | 标记字符串是否需要翻译。  true：需要翻译。  false：不需要翻译。 |
| priority | string | 标记字符串翻译状态。  code：未翻译。  translate：翻译未验证。  LT：翻译已验证。  customer：用户定制字符串。 |

### 使用约束

可翻译特性使能范围：base目录下string、strarray、plural类型资源。

```
1. resources
2. |---base
3. |   |---element
4. |   |   |---string.json
5. |   |   |---strarray.json
6. |   |   |---plural.json
```

### 示例

string资源配置attr属性示例如下，其中string1字符串被标记为不需要翻译，string2字符串被标记为需要翻译且翻译已验证。

```
1. {
2. "string": [
3. {
4. "name": "string1",
5. "value": "1",
6. "attr": {
7. "translatable": false
8. }
9. },
10. {
11. "name": "string2",
12. "value": "Hello world!",
13. "attr": {
14. "translatable": true,
15. "priority": "LT"
16. }
17. }
18. ]
19. }
```

## 资源访问

### 单HAP包应用资源

* 通过$r或$rawfile访问资源。

  对于color、float、string、plural、media、profile等类型的资源，通过$r('app.type.name')形式访问。其中，app为resources目录中定义的资源，type为资源类型，name为资源名，由开发者定义资源时确定。

  对于string.json中使用多个占位符的情况，例如资源值value中存在%1$s和%2$d两个占位符，需要通过$r('app.string.label', 'aaa', 444)形式访问。其中label为资源名称name，'aaa'和444用来替代占位符。

  对于rawfile目录资源，通过$rawfile('filename')形式访问。其中，filename为rawfile目录下文件的相对路径，文件名需要包含后缀，路径开头不可以"/"开头。

  说明

  + 针对同一个资源，$r获取的资源信息Resource对象中的资源ID在应用重新编译时会发生变化，并非固定值，不建议缓存资源ID。如果确实需要缓存资源ID，需要对资源ID进行固定，具体请参考[固定资源ID](restool.md#固定资源id)。
  + rawfile的native的访问方式请参考[Rawfile开发指导](rawfile-guidelines.md)。

[资源文件示例](resource-categories-and-access.md#资源文件示例)中显示了.json文件内容，包含color.json、string.json和plural.json，访问应用资源时需先了解.json文件的使用规范。

资源的具体使用方法如下：

```
1. // 通过$r('app.type.name')访问
2. // 资源name仅作示例，请替换为实际使用的资源
3. Text($r('app.string.string_hello'))
4. .id('app_resource')
5. .fontColor($r('app.color.color_emphasize'))
6. .fontSize($r('app.float.text_size_headline1'))
7. .fontFamily($r('app.string.font_family_medium'))
8. .backgroundColor($r('app.color.color_palette_aux1'))

10. // 资源name仅作示例，请替换为实际使用的资源
11. Image($r('app.media.app_icon'))
12. .border({
13. color: $r('app.color.color_palette_aux1'),
14. radius: $r('app.float.corner_radius_button'), width: 2
15. })
16. .margin({
17. top: $r('app.float.elements_margin_horizontal_m'),
18. bottom: $r('app.float.elements_margin_horizontal_l')
19. })
20. .height(100)
21. .width(100)

23. // 对于string.json中name为"message_notification"，value为"Hello, %1$s!,You have %2$d new messages."
24. // 该资源存在%1$s、%2$d两个占位符，需要替代为'LiHua'、2，则采用如下方式访问
25. // 资源name仅作示例，请替换为实际使用的资源
26. Text($r('app.string.message_notification', 'LiHua', 2)).id('app_string_resource')

28. // 对于plural.json中name为"eat_apple"，单数的value为"%d apple"，复数的value为"%d apples"
29. // 访问plural.json资源，第一个参数控制字符串显示单数形式或复数形式，传递1表示单数，大于1表示复数，且在中文环境下始终为复数
30. // 该资源存在%d一个占位符，需要替代为2，则采用如下方式访问
31. // 资源name仅作示例，请替换为实际使用的资源
32. Text($r('app.plural.eat_apple', 2, 2)).id('app_plural_resource')
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ResourceManagement/ResourceCategoriesAndAccess/entry/src/main/ets/pages/Index.ets#L28-L60)

* 通过本应用上下文获取ResourceManager后，可调用不同[资源管理接口](../harmonyos-references/js-apis-resource-manager.md)通过资源ID值或资源名称访问各类资源。例如通过getContext().resourceManager.getStringByNameSync('test')可获取字符串资源，通过getContext().resourceManager.getRawFd('rawfilepath')可获取rawfile文件所在HAP包的descriptor信息，再使用其中的{fd, offset, length}可访问rawfile文件。

  在API version 22及之前版本，中间码HAR、字节码HAR通过资源ID相关接口访问资源时，因ID无效会抛出异常；从API version 23开始，若将[compatibleSdkVersion](ide-hvigor-build-profile-app.md#section45865492619)配置为23及以上，则在当前Module的[AbilityStage](abilitystage.md)的onCreate()回调执行后，中间码HAR、字节码HAR通过资源ID相关接口可以正常访问资源。

### 跨HAP/HSP包应用资源

**bundle相同，跨module访问**

* 通过[createModuleContext(context, moduleName)](../harmonyos-references/js-apis-app-ability-application.md#applicationcreatemodulecontext)接口创建同应用中不同module的上下文，获取resourceManager对象后，调用不同[资源管理接口](../harmonyos-references/js-apis-resource-manager.md)通过资源ID值或资源名称访问各类资源。
* 通过$r或$rawfile访问资源。具体操作如下：

  1.在entry的oh-package.json5文件中添加依赖。如"dependencies": {"library": "file:../library"}。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/TFR71cfhRMeHh8MqNI2q-Q/zh-cn_image_0000002552797836.png?HW-CC-KV=V1&HW-CC-Date=20260427T233733Z&HW-CC-Expire=86400&HW-CC-Sign=506617CD7F234D8DC42595B6712CBCFACCCBD4357925EAF87ABD4A943DB9F21D)

  2.使用字面量[模块名].type.name或变量获取资源。其中，模块名为hsp模块的名称，type为资源类型，name为资源名称，示例如下：

  ```
  1. @Entry
  2. @Component
  3. struct Second {
  4. // [library]仅为示例模块名，请替换为实际模块名
  5. // 资源name仅作示例，请替换为实际使用的资源
  6. text: string = '[library].string.test_string';
  7. fontSize: string = '[library].float.font_size';
  8. fontColor: string = '[library].color.font_color';
  9. image: string = '[library].media.image';
  10. rawfile: string = '[library].icon.png';

  12. build() {
  13. Column() {
  14. // 使用字面量[模块名].type.name获取资源
  15. // 资源name仅作示例，请替换为实际使用的资源
  16. Text($r('[library].string.test_string'))
  17. .id('hsp_resource_one')
  18. .fontSize($r('[library].float.font_size'))
  19. .fontColor($r('[library].color.font_color'))
  20. Image($rawfile('[library].icon.png'))
  21. .height(100)
  22. .width(100)

  24. // 使用变量获取资源
  25. Text($r(this.text))
  26. .id('hsp_resource_two')
  27. .fontSize($r(this.fontSize))
  28. .fontColor($r(this.fontColor))

  30. Image($r(this.image))
  31. .height(100)
  32. .width(100)

  34. Image($rawfile(this.rawfile))
  35. .height(100)
  36. .width(100)
  37. }
  38. .height('100%')
  39. .width('100%')
  40. }
  41. }
  ```

  [Second.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ResourceManagement/ResourceCategoriesAndAccess/entry/src/main/ets/pages/Second.ets#L16-L58)

  说明

  hsp包名必须写在[]内，rawfile下有多层目录，需要从rawfile下面第一个目录开始写，如$rawfile('[hsp].firstDir/secondDir/icon.png')，使用$r和$rawfile跨包访问HSP包资源无法提供编译时的资源校验，需要开发者自行保证使用资源存在于对应包中。

### 系统资源

对于系统资源，可以通过$r('sys.type.name')的形式访问。其中，sys表示系统资源，type为资源类型，取值包括“color”、“float”、“string”、“media”、“symbol”，name为资源名称。

说明

* 对于系统预置应用，建议使用系统资源；对于三方应用，可以根据需要选择使用系统资源或自定义应用资源。
* 仅声明式开发范式支持使用系统资源。
* 界面显示时默认使用的系统字体是鸿蒙黑体（HarmonyOS Sans），支持的字符范围是[中文编码字符集GB18030-2022（级别一/级别二）](https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=A1931A578FE14957104988029B0833D3)。若要显示的字符不在鸿蒙黑体支持的字符范围内，系统会在其他支持该字符的字体中选择优先级最高的字体用来显示。关于系统字体的优先级顺序，可以查看设备上的配置文件/system/etc/fontconfig.json。

```
1. Text('Hello')
2. .fontColor($r('sys.color.ohos_id_color_emphasize'))
3. .fontSize($r('sys.float.ohos_id_text_size_headline1'))
4. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
5. .backgroundColor($r('sys.color.ohos_id_color_palette_aux1'))

7. Image($r('sys.media.ohos_app_icon'))
8. .border({
9. color: $r('sys.color.ohos_id_color_palette_aux1'),
10. radius: $r('sys.float.ohos_id_corner_radius_button'), width: 2
11. })
12. .margin({
13. top: $r('sys.float.ohos_id_elements_margin_horizontal_m'),
14. bottom: $r('sys.float.ohos_id_elements_margin_horizontal_l')
15. })
16. .height(100)
17. .width(100)
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ResourceManagement/ResourceCategoriesAndAccess/entry/src/main/ets/pages/Index.ets#L62-L82)

## 资源匹配

应用使用某资源时，系统会根据当前设备状态优先从相匹配的限定词目录中寻找该资源。只有当resources目录中没有与设备状态匹配的限定词目录，或者在限定词目录中找不到该资源时，才会去base目录中查找。rawfile和resfile是原始文件目录，不会根据设备状态去匹配资源。

说明

* 在编译构建时，AppScope目录下的资源文件会合入到模块下面的资源文件中，如果两个目录下的相同资源目录和资源组目录下存在重名资源，编译打包后只会保留AppScope目录下的资源。

### 限定词目录与设备状态的匹配规则

* 在为设备匹配对应的资源文件时，限定词目录匹配的优先级从高到低依次为：移动国家码和移动网络码 > 区域（可选组合：语言、语言\_文字、语言\_国家或地区、语言\_文字\_国家或地区）> 横竖屏 > 设备类型 > 颜色模式 > 屏幕密度。
* 如果限定词目录中包含移动国家码和移动网络码、语言、文字、横竖屏、设备类型、颜色模式限定词，则对应限定词的取值必须与当前的设备状态完全一致，该目录才能够参与设备的资源匹配。例如，限定词目录zh\_CN-car-ldpi不能参与en\_US设备的资源匹配。
* 如果存在多个屏幕密度限定词目录，则优先向上匹配最接近的屏幕密度限定词目录，否则向下匹配最为接近的屏幕密度限定词目录。例如，假设存在限定词目录xldpi和xxldpi，设备屏幕密度为xxldpi，则会匹配xxldpi限定词目录。

关于应用界面加载资源的更多规则，请参考[国际化和本地化](i18n-l10n.md)文档。

### 获取指定配置的资源

**基本概念**

开发者可以在工程的resources目录下添加限定词目录，满足多语言、深浅色模式等不同类型的系统设置。然而，在获取资源时，由于限定词目录匹配规则，只能筛选出最匹配的资源，无法获取其它目录资源。

应用如果有获取指定配置的资源的诉求，可以通过以下方法进行获取。

**接口说明**

| 接口名 | 描述 |
| --- | --- |
| [getOverrideResourceManager](../harmonyos-references/js-apis-resource-manager.md#getoverrideresourcemanager12)(configuration?: [Configuration](../harmonyos-references/js-apis-resource-manager.md#configuration)) : [ResourceManager](../harmonyos-references/js-apis-resource-manager.md#resourcemanager) | 获取可以加载指定配置的资源的资源管理对象，使用同步方式返回。 |
| [getOverrideConfiguration](../harmonyos-references/js-apis-resource-manager.md#getoverrideconfiguration12)() : [Configuration](../harmonyos-references/js-apis-resource-manager.md#configuration) | 获取指定的配置，使用同步方式返回。 |
| [updateOverrideConfiguration](../harmonyos-references/js-apis-resource-manager.md#updateoverrideconfiguration12)(configuration: [Configuration](../harmonyos-references/js-apis-resource-manager.md#configuration)) : void | 更新指定的配置。 |

**示例**

以获取非当前系统语言的资源为例，说明如何获取指定配置的资源。假设工程中定义了中文、英文、日文的同名资源如下：

* entry/src/main/resources/zh\_CN/element/string.json

```
1. {
2. "string": [
3. {
4. "name": "greetings",
5. "value": "你好，世界"
6. }
7. ]
8. }
```

* entry/src/main/resources/en\_US/element/string.json

```
1. {
2. "string": [
3. {
4. "name": "greetings",
5. "value": "Hello, world"
6. }
7. ]
8. }
```

* entry/src/main/resources/ja\_JP/element/string.json

```
1. {
2. "string": [
3. {
4. "name": "greetings",
5. "value": "こんにちは、世界"
6. }
7. ]
8. }
```

在Index.ets中，分别获取三种语言的资源并显示在文本框中，运行设备当前系统语言为中文，entry/src/main/ets/pages/Index.ets的代码如下：

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. @Entry
4. @Component
5. struct Index {
6. @State englishString: string = '';
7. @State japaneseString: string = '';

9. build() {
10. Column() {
11. // ···
12. Text(this.getString())
13. .id('config_resource_one')
14. .fontSize(30)
15. .fontWeight(FontWeight.Bold)
16. Text(this.englishString)
17. .id('config_resource_two')
18. .fontSize(30)
19. .fontWeight(FontWeight.Bold)
20. Text(this.japaneseString)
21. .id('config_resource_three')
22. .fontSize(30)
23. .fontWeight(FontWeight.Bold)
24. // ···
25. }
26. .height('100%')
27. .width('100%')
28. }

30. getString(): string {
31. let resMgr = this.getUIContext().getHostContext()?.resourceManager;
32. if (!resMgr) {
33. return '';
34. }
35. let currentLanguageString: string = '';
36. try {
37. // 资源name仅作示例，请替换为实际使用的资源
38. let resId = $r('app.string.greetings').id;

40. // 获取符合当前系统语言地区、颜色模式、分辨率等配置的资源
41. currentLanguageString = resMgr.getStringSync(resId);

43. // 获取符合当前系统颜色模式、分辨率等配置的英文资源
44. let overrideConfig = resMgr.getOverrideConfiguration();
45. overrideConfig.locale = 'en_US'; // 指定资源的语言为英语，地区为美国
46. let overrideResMgr = resMgr.getOverrideResourceManager(overrideConfig);
47. this.englishString = overrideResMgr.getStringSync(resId);

49. // 获取符合当前系统颜色模式、分辨率等配置的日文资源
50. overrideConfig.locale = 'ja_JP'; // 指定资源的语言为日文，地区为日本
51. // 等效于resMgr.updateOverrideConfiguration(overrideConfig)
52. overrideResMgr.updateOverrideConfiguration(overrideConfig);
53. this.japaneseString = overrideResMgr.getStringSync(resId);
54. } catch (err) {
55. const code = (err as BusinessError).code;
56. const message = (err as BusinessError).message;
57. console.error(`get override resource failed, error code: ${code}, error msg: ${message}`);
58. }
59. return currentLanguageString;
60. }
61. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ResourceManagement/ResourceCategoriesAndAccess/entry/src/main/ets/pages/Index.ets#L16-L144)

## overlay机制

overlay是一种资源替换机制，针对不同品牌、产品的显示风格，开发者可以在不重新打包HAP的情况下，通过配置和使用overlay资源包，实现应用界面风格变换。overlay资源包只包含资源文件、资源索引文件和配置文件。

### 动态overlay使用方式

1. 对应的overlay资源包需要放在对应应用安装路径下。如应用com.example.overlay的安装路径为data/app/el1/bundle/public/com.example.overlay/。
2. 应用通过[addResource(path)](../harmonyos-references/js-apis-resource-manager.md#addresource10)，实现资源覆盖；通过[removeResource(path)](../harmonyos-references/js-apis-resource-manager.md#removeresource10)，实现overlay删除。overlay资源路径需经过元能力的getContext().bundleCodeDir获取此应用对应的沙箱根目录，由应用的沙箱根目录与overlay资源包名称拼接而成。如：let path = getContext().bundleCodeDir + "overlay资源包名称"，其对应沙箱路径为/data/storage/el1/bundle/overlay资源包名称。

### 静态overlay配置方式

该功能默认使能，使能及去使能请参考[@ohos.bundle.overlay (overlay模块)](../harmonyos-references/js-apis-overlay.md)。

包内overlay资源包中的配置文件app.json5中支持的字段：

```
1. {
2. "app":{
3. "bundleName": "com.example.myapplication.overlay",
4. "vendor" : "example",
5. "versionCode": "1000000",
6. "versionName": "1.0.0.1",
7. "icon": "$media:app_icon",
8. "label": "$string:app_name"
9. }
10. }
```

包内overlay资源包中的配置文件module.json5中支持的字段：

```
1. {
2. "module":{
3. "name": "entry_overlay_module_name",
4. "type": "shared",
5. "description": "$string:entry_overlay_desc",
6. "deviceTypes": [
7. "default",
8. "tablet"
9. ],
10. "deliveryWithInstall": true,
11. "targetModuleName": "entry_module_name",
12. "targetPriority": 1
13. }
14. }
```

说明

* targetModuleName: 字符串类型，指定要overlay的应用中的目标module。
* targetPriority： 整数类型，指定overlay优先级。
* 不支持Ability、ExtensionAbility、Permission等其他字段的配置。
* overlay不支持json类型的图片配置。

在DevEco Studio中创建应用工程时，module的配置文件module.json5中包含targetModuleName和targetPriority字段时，该module将会在安装阶段被识别为overlay特征的module。overlay特征的module一般是为设备上存在的非overlay特征的module提供覆盖的资源文件，以便于targetModuleName指向的module在运行阶段可以使用overlay资源文件展示不同的颜色，标签，主题等等。
