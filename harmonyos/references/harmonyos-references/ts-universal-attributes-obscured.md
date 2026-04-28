---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-obscured
title: 隐私遮罩
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 基础属性 > 隐私遮罩
category: harmonyos-references
scraped_at: 2026-04-28T08:01:01+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2a9e762946eceb778e082adbcf5637b834bbfbc49f107512464b9a546ae8fd39
---

用于对组件内容进行隐私遮罩处理。

说明

从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## obscured

PhonePC/2in1TabletTVWearable

obscured(reasons: Array<ObscuredReasons>): T

设置组件内容的遮罩类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reasons | Array<[ObscuredReasons](ts-appendix-enums.md#obscuredreasons10)> | 是 | 设置组件内容的遮罩类型。  默认值：[]  仅支持[Image](ts-basic-components-image.md)组件、[Text](ts-basic-components-text.md)组件的隐私遮罩处理。  **说明：**  如需在图片加载过程中显示隐私遮罩，需要设置Image组件的宽度和高度。  Text组件设置子组件或设置[属性字符串](ts-universal-styled-string.md)时，不支持隐私遮罩。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例通过obscured对Text、Image组件实现了隐私遮罩效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ObscuredExample {
5. build() {
6. Row() {
7. Column() {
8. Text('Text not set obscured attribute').fontSize(10).fontColor(Color.Black)
9. Text('This is an example for text obscured attribute.')
10. .fontSize(30)
11. .width('600px')
12. .fontColor(Color.Black)
13. .border({ width: 1 })
14. Text('Image not set obscured attribute').fontSize(10).fontColor(Color.Black)
15. // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
16. Image($r('app.media.icon'))
17. .width('200px')
18. .height('200px')
19. Text('Text set obscured attribute').fontSize(10).fontColor(Color.Black)
20. Text('This is an example for text obscured attribute.')
21. .fontSize(30)
22. .width('600px')
23. .fontColor(Color.Black)
24. .border({ width: 1 })
25. .obscured([ObscuredReasons.PLACEHOLDER])
26. Text('Image set obscured attribute').fontSize(10).fontColor(Color.Black)
27. // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
28. Image($r('app.media.icon'))
29. .width('200px')
30. .height('200px')
31. .obscured([ObscuredReasons.PLACEHOLDER])
32. }
33. .width('100%')
34. }
35. .height('100%')
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/ukusNgs4Q1O7bWUQGx1_xA/zh-cn_image_0000002583479487.png?HW-CC-KV=V1&HW-CC-Date=20260428T000100Z&HW-CC-Expire=86400&HW-CC-Sign=489701D44EBC16A0B74FD9B49E3F59DB928D00C8A5F00DFAC13F30F316CD6852)
