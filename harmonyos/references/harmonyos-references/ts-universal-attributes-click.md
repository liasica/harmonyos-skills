---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-click
title: 点击控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 已停止维护的组件与接口 > 点击控制
category: harmonyos-references
scraped_at: 2026-04-29T13:53:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c6be77671531a062fb27d4cec7f1699a548f9dbe928df604f14a17830074a694
---

设置组件是否可以响应点击事件、触摸事件等手指交互事件。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## touchable(deprecated)

PhonePC/2in1TabletTVWearable

touchable(value: boolean): T

设置当前组件是否可以响应点击事件、触摸事件等手指交互事件。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[hitTestBehavior](ts-universal-attributes-hit-test-behavior.md#hittestbehavior)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置当前组件是否可以响应点击事件、触摸事件等手指交互事件。  默认值：true，可以响应交互事件。设置为false时，不可以响应交互事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TouchAbleExample {
5. @State text1: string = ''
6. @State text2: string = ''

8. build() {
9. Stack() {
10. Rect()
11. .fill(Color.Gray).width(150).height(150)
12. .onClick(() => {
13. console.info(this.text1 = 'Rect Clicked')
14. })
15. .overlay(this.text1, { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
16. Ellipse()
17. .fill(Color.Pink).width(150).height(80)
18. .touchable(false) // 点击Ellipse区域，不会打印 “Ellipse Clicked”
19. .onClick(() => {
20. console.info(this.text2 = 'Ellipse Clicked')
21. })
22. .overlay(this.text2, { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
23. }.margin(100)
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/cL-VbhY6SbeA_Lyz8p6SZQ/zh-cn_image_0000002558607032.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055312Z&HW-CC-Expire=86400&HW-CC-Sign=B0E38C84BC9C6A7B27AA4D48C6FC210E760A9946CAFBAA561F3C7FFCE4E4F019)
