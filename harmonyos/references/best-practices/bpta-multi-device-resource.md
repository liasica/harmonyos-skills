---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-resource
title: 多设备资源文件
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备资源文件
category: best-practices
scraped_at: 2026-04-29T14:12:20+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:78a303fd088fdbe94191745bb0353a577a3a8f1969dd382915dd031e5f88b7d7
---

在页面开发过程中，经常需要用到颜色、字体、间距、图片等资源，在不同的设备或配置中，这些资源的值可能不同。有两种方式处理：

* [应用资源](bpta-multi-device-resource.md#应用资源)：借助资源文件能力，开发者在应用中自定义资源，自行管理这些资源在不同的设备或配置中的表现。
* [系统资源](bpta-multi-device-resource.md#系统资源)：开发者直接使用系统预置的资源定义（即分层参数）。

## 应用资源

### 资源文件介绍

应用开发中使用的各类自定义资源文件，分别存放于不同模块的resources目录下，便于使用和维护。resources目录包括两大类目录，一类为base目录与限定词目录，另一类为rawfile目录。以entry模块为例，其基础目录结构如下所示。

```
1. └──entry/src/main/resources                                  // 资源区
2. ├──base                                                   // 默认存在的目录
3. │  ├──element
4. │  │  ├──color.json                                       // 颜色资源
5. │  │  ├──float.json                                       // 数字资源
6. │  │  └──string.json                                      // 字符串资源
7. │  ├──media                                               // 媒体资源
8. │  └──profile                                             // 路由资源
9. ├──en_US                                                  // 限定词目录示例，需要开发者自行创建
10. ├──zh_CN                                                  // 限定词目录示例，需要开发者自行创建
11. └──rawfile                                                // 原始文件目录
```

base目录默认存在，而限定词目录需要开发者自行创建，其名称可以由一个或多个表征应用场景或设备特征的限定词组合而成。应用使用某资源时，系统会根据当前设备状态优先从相匹配的限定词目录中寻找该资源。只有当resources目录中没有与设备状态匹配的限定词目录，或者在限定词目录中找不到该资源时，才会去base目录中查找。rawfile是原始文件目录，它不会根据设备状态去匹配不同的资源，故不在本文的讨论范围内。

说明

* 请访问[限定词目录](../harmonyos-guides/resource-categories-and-access.md#限定词目录)，了解限定词目录的命名规则、创建流程、匹配规则等，本文不展开介绍。
* 没有设备状态匹配的限定词目录，或者在限定词目录中找不到目标资源时，会继续在base目录中查找。**强烈建议对于所有应用自定义资源都在base目录中定义默认值**，防止出现找不到资源值的异常场景。
* 类Web开发范式的资源文件路径及资源限定词的使用与声明式范式不同，详情请参考类Web开发范式的[资源限定与访问](../harmonyos-guides/js-framework-resource-restriction.md)及[文件组织](../harmonyos-guides/js-framework-file.md)。

base目录与限定词目录下面可以创建资源组目录，用于存放特定类型的资源文件（包括element、media等）。

| 资源组目录 | 目录说明 | 资源文件 |
| --- | --- | --- |
| element | 表示元素资源，以下每一类数据都采用相应的JSON文件来表征。  - boolean，布尔型  - color，颜色  - float，浮点型  - intarray，整型数组  - integer，整型  - pattern，样式  - plural，复数形式  - strarray，字符串数组  - string，字符串 | element目录中的文件名称建议与下面的文件名保持一致。每个文件中只能包含同一类型的数据。  - boolean.json  - color.json  - float.json  - intarray.json  - integer.json  - pattern.json  - plural.json  - strarray.json  - string.json |
| media | 表示媒体资源，包括图片、音频、视频等非文本格式的文件。 | 文件名可自定义，例如：icon.png。 |

在element目录的各个资源文件中，以“name-value”的形式定义资源，如下所示。而在media目录中，直接以文件名作为name，故开发者将文件放入media目录即可，无需再额外定义name。

```
1. // color.json
2. {
3. "color": [
4. {
5. "name": "color_red",
6. "value": "#FFFF0000"
7. },
8. {
9. "name": "color_blue",
10. "value": "#FF0000FF"
11. }
12. ]
13. }
```

### 访问应用资源

在工程中，通过 "$r('app.type.name')" 的形式引用应用资源。app代表是应用模块内resources目录中定义的资源；type 代表资源类型（或资源的存放位置），可以取 color、float、string、plural和media，name代表资源命名，由开发者添加资源时确定。

说明

可以查看声明式范式的[资源访问](../harmonyos-guides/resource-categories-and-access.md#资源访问)，了解资源访问的更多细节。

### 示例

在应用模块的resources目录下，创建名为tablet的限定词子目录，并按照下表所示，在base目录和tablet限定词目录中添加相应的资源。

| 资源名称 | 资源类型 | base目录中资源值 | 限定词目录（tablet）中资源值 |
| --- | --- | --- | --- |
| my\_string | string | default | tablet |
| my\_color | color | #ff0000 | #0000ff |
| my\_float | float | 60vp | 80vp |
| my\_image | media | my\_image.png（太阳图标） | my\_image.png（月亮图标） |

在代码中通过 "$r('app.type.name')" 的形式使用应用资源，并分别在默认设备和平板上查看代码的运行效果，可以发现同一资源在不同设备上的取值不同。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/Bd74pDC4SzSzIBPArFD0qw/zh-cn_image_0000002321308262.png?HW-CC-KV=V1&HW-CC-Date=20260429T061208Z&HW-CC-Expire=86400&HW-CC-Sign=92327A809E3D30F6433B0B214C78545D23A968DEAD484B929AACAEB810E80989 "点击放大")

```
1. @Entry
2. @Component
3. struct ResourceQualifier {
4. build() {
5. Column() {
6. Text($r('app.string.my_string'))
7. .fontSize(60)
8. .fontColor($r('app.color.my_color'))
9. Image($r('app.media.my_image'))
10. .width(100)
11. .height(100)
12. }
13. .height('100%')
14. .width('100%')
15. .alignItems(HorizontalAlign.Center)
16. .justifyContent(FlexAlign.Center)
17. }
18. }
```

[ResourceQualifier.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/resourceQualifier/ResourceQualifier.ets#L17-L34)

## 系统资源

除了自定义资源，开发者也可以使用系统中预定义的资源（即分层参数，同一资源ID在设备类型、深浅色等不同配置下有不同的取值）。

在开发过程中，分层参数的用法与资源限定词基本一致。开发者可以通过"$r('sys.type.resource\_id')"的形式引用系统资源。sys代表是系统资源；type代表资源类型，值可以取color、float、string和media；resource\_id代表资源id。

说明

* 仅声明式开发范式支持使用分层参数，类Web开发范式不支持。
* 系统资源可以保证不同团队开发出的应用有较为一致的视觉风格。对于系统预置应用，强烈建议使用系统资源；对于三方应用，可以根据需要选择使用系统资源或自定义应用资源。
