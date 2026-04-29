---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-resource
title: Resource
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > arkui > Resource
category: harmonyos-references
scraped_at: 2026-04-29T13:50:54+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:95609eb4ab67f51a9f7e128d66bda283ef67001d70b73e76ea879d5d2c45b4ab
---

提供获取应用资源或系统资源信息的接口。应用资源及系统资源的介绍及使用方法可参考[资源分类与访问](../harmonyos-guides/resource-categories-and-access.md)。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## $r

PhonePC/2in1TabletTVWearable

$r(value: string, ...params: any[]): Resource

获取应用资源或系统资源的信息。$r会在编译期由工具链转换为[Resource](js-apis-resource-manager.md#resource9)对象。通过$r访问应用资源或系统资源，可参考[资源分类与访问](../harmonyos-guides/resource-categories-and-access.md)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 资源标识符，访问格式为belonging.type.name。  belonging：表示该资源为系统资源、应用资源或HSP包资源，可选值为sys、app或[hsp\_name]。  type：资源类型，可选值为boolean，color，float，intarray，integer，pattern，plural，strarray，string或media。  name：资源名称，应用资源名称定义在工程resources目录下，系统资源名称获取可参考[资源分类与访问](../harmonyos-guides/resource-categories-and-access.md)。 |
| ...params | any[] | 否 | 开发者传入的剩余参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Resource](js-apis-resource-manager.md#resource9) | 资源相关信息，包括应用包名、应用模块名、资源id等。 |

**示例：**

```
1. @Entry
2. @Component
3. struct Page {
4. build() {
5. Row() {
6. Column() {
7. Text($r('app.string.app_name'))
8. }
9. .width('100%')
10. }
11. .height('100%')
12. }
13. }
```

访问HSP包的资源示例可参考[访问跨HAP/HSP包资源](../harmonyos-guides/resource-categories-and-access.md#访问跨haphsp包资源)。

## $rawfile

PhonePC/2in1TabletTVWearable

$rawfile(value: string): Resource

获取工程rawfile目录下的资源信息。$rawfile会在编译期由工具链转换为[Resource](js-apis-resource-manager.md#resource9)对象。通过$rawfile访问应用资源或系统资源，可参考[资源分类与访问](../harmonyos-guides/resource-categories-and-access.md)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | rawfile目录下的相对路径。文件名需要包含后缀，路径开头不可以"/"开头。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Resource](js-apis-resource-manager.md#resource9) | 资源相关信息，包括应用包名、应用模块名、资源id等。 |

```
1. // src/main/resources/rawfile目录下添加startIcon.png。

3. @Entry
4. @Component
5. struct Page {
6. build() {
7. Row() {
8. Column() {
9. Image($rawfile("startIcon.png"))
10. }
11. .width('100%')
12. }
13. .height('100%')
14. }
15. }
```

访问HSP包资源示例可参考[跨HAP/HSP包应用资源](../harmonyos-guides/resource-categories-and-access.md#访问跨haphsp包资源)。
