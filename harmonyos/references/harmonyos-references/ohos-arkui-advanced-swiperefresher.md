---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-swiperefresher
title: SwipeRefresher
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > SwipeRefresher
category: harmonyos-references
scraped_at: 2026-04-28T08:02:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4dfd0a4c3044f8c8f62012925e60a9d062b8b7221820c3f9405a59253bb077c7
---

内容加载指获取内容并加载出来，常用于衔接展示下拉加载的内容。

说明

* 该组件及其子组件从 API version 10 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果SwipeRefresher设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到SwipeRefresher本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议SwipeRefresher设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { SwipeRefresher } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## SwipeRefresher

PhonePC/2in1TabletTVWearable

SwipeRefresher ({content?: ResourceStr, isLoading: boolean})

主要用于实现下拉刷新功能。当用户下拉页面时，会触发内容加载操作，即从数据源获取新内容并动态展示在界面中。

**装饰器类型：**@Component

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | @Prop | 内容加载时显示的文本。  默认值：空字符串。  **说明**：如果文本大于列宽时，文本被截断。从API version 20开始，支持Resource类型。 |
| isLoading | boolean | 是 | @Prop | 当前是否正在加载。  true：正在加载。  false：未在加载。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

展示设置属性content为空字符串及不为空、isLoading为true和false的不同加载效果。

```
1. import { SwipeRefresher } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Column() {
8. SwipeRefresher({
9. content: '正在加载中',
10. isLoading: true
11. })
12. SwipeRefresher({
13. content: '',
14. isLoading: true
15. })
16. SwipeRefresher({
17. content: '正在加载中',
18. isLoading: false
19. })
20. }
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/UIDF6_RSTqOe2HtVpZcqIw/zh-cn_image_0000002583440181.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000239Z&HW-CC-Expire=86400&HW-CC-Sign=75C1625598836072D1D9909519FAD3C28D2070D19725E3AEF3897FF26B75DF21)
