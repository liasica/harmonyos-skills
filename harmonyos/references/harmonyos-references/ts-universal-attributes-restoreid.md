---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-restoreid
title: 分布式迁移标识
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 基础属性 > 分布式迁移标识
category: harmonyos-references
scraped_at: 2026-04-28T08:01:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:71e2f761b7d64d25e001626a2c4e087107c81d6b576ba1d0551e094f1d52fc71
---

组件的分布式迁移标识，指明了该组件在分布式迁移场景下可以将特定状态恢复到对端设备。

说明

从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## restoreId

PhonePC/2in1TabletTVWearable

restoreId(value: number): T

标记支持分布式迁移的组件Id，用于两端设备组件的配对。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 标记支持分布式迁移的组件Id，用于两端设备组件的配对。同一个应用中各个支持分布式迁移组件的Id必须不同。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 支持的组件

PhonePC/2in1TabletTVWearable

| 组件名称 | 起始版本 | 迁移状态 |
| --- | --- | --- |
| [List](ts-container-list.md) | 8 | 迁移当前设备显示在顶部ListItem的索引值，迁移后在对端设备上，将迁移索引值对应的ListItem在List中完整地置顶显示。 |
| [Grid](ts-container-grid.md) | 9 | 迁移当前设备显示在顶部GridItem的索引值，迁移后在对端设备上，将迁移索引值对应的GridItem在Grid中完整地置顶显示。ScrollBar位置无法迁移。 |
| [Scroll](ts-container-scroll.md) | 9 | 迁移距顶部滚动的绝对距离。两端设备显示规格不同等原因导致布局不一致，会影响迁移效果。 |
| [WaterFlow](ts-container-waterflow.md) | 11 | 迁移当前设备显示在顶部FlowItem的索引值，迁移后在对端设备上，将迁移索引值对应的FlowItem在WaterFlow顶部显示。同时迁移顶部FlowItem相对WaterFlow的主轴偏移值（vp单位）。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例通过restoreId设置了List组件的分布式迁移标识。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RestoreIdExample {
5. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
6. build() {
7. Column() {
8. List({ space: 20 }) {
9. ForEach(this.arr, (item:number) => {
10. ListItem() {
11. Text('' + item)
12. .width('100%')
13. .height(100)
14. .fontSize(16)
15. .textAlign(TextAlign.Center)
16. .borderRadius(10)
17. .backgroundColor(Color.Pink)
18. }
19. }, (item:number) => (item.toString()))
20. }
21. .restoreId(1)
22. }
23. }
24. }
```
