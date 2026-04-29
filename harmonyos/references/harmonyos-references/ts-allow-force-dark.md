---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-allow-force-dark
title: 禁用反色能力
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 基础属性 > 禁用反色能力
category: harmonyos-references
scraped_at: 2026-04-29T13:51:15+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:fef9a1b6b8ae10b0d363ca042ec89dabc7ed390c42abdb7931a955f002771701
---

设置组件是否使用反色能力，反色能力是在深浅色切换时自动对颜色值进行反色或变换，开发者可以通过主动设置不启用反色算法，以保持在深浅色切换时的原有逻辑。

说明

本模块首批接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记该接口的起始版本。

## allowForceDark

PhonePC/2in1TabletTVWearable

allowForceDark(value: boolean): T

设置组件是否使用反色能力。

说明

* 当组件主动设置不使用反色能力时，组件及其所有子组件均不使用反色能力，不受父组件或祖先组件主动设置使用反色能力的影响。
* 该接口仅在开启了反色能力的情况下生效，开启反色能力可参考[利用反色能力快速适配深色模式](../harmonyos-guides/ui-dark-light-color-adaptation.md#利用反色能力快速适配深色模式)。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 组件是否使用反色能力。true：组件使用反色能力；false：组件不使用反色能力。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. // 组件添加allowForceDark(false)属性后，说明对当前组件不使用反色相关能力。
2. @Entry
3. @Component
4. struct ComponentPage {
5. build() {
6. Column() {
7. Column() {
8. Text("Hello World")
9. .fontSize(20)
10. .fontColor(Color.Blue)
11. .onClick(() => {
12. console.info(`Text is clicked`);
13. })
14. }
15. .allowForceDark(false) // Column及其子组件Text不生效反色能力，不受父组件Column使用反色能力的影响。

17. Row() {
18. Button('BUTTON')
19. .backgroundColor(Color.Grey)
20. .allowForceDark(true)
21. .onClick(() => {
22. console.info(`Button is clicked`);
23. })
24. }
25. .allowForceDark(false) // Row及其子组件Button不生效反色能力，不受父组件Column使用反色能力的影响。
26. }
27. .allowForceDark(true)
28. .width('100%')
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/SPOVnMMETiujT_AA1HgNwg/zh-cn_image_0000002589325877.png?HW-CC-KV=V1&HW-CC-Date=20260429T055114Z&HW-CC-Expire=86400&HW-CC-Sign=86D19A86CF2F8DF76A1F82AF1038A31D02DEFE190929F504D34145FEBFDC1B1D)
