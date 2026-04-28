---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-navigator
title: Navigator
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 已停止维护的组件与接口 > Navigator
category: harmonyos-references
scraped_at: 2026-04-28T08:02:51+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f5441d9faa870474bae071120b6eb81f2c8a9b520896ef52ea46702979d63414
---

路由容器组件，提供路由跳转能力。

说明

从API version 13开始，该组件不再维护，建议使用[Navigation](ts-basic-components-navigation.md)组件进行页面路由。

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含子组件。

## 接口

PhonePC/2in1TabletTVWearable

### Navigator(deprecated)

PhonePC/2in1TabletTVWearable

Navigator(value?: {target: string, type?: NavigationType})

说明

从API version 7开始支持，从API version 13开始废弃，建议使用[NavPathInfo](ts-basic-components-navigation.md#navpathinfo10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | string | 是 | 指定跳转目标页面的路径。 |
| type | [NavigationType](ts-container-navigator.md#navigationtypedeprecated枚举说明) | 否 | 指定路由方式。  默认值：NavigationType.Push |

### Navigator(deprecated)

PhonePC/2in1TabletTVWearable

Navigator()

说明

从API version 7开始支持，从API version 13开始废弃，建议使用[NavigationAttribute](ts-basic-components-navigation.md#属性)替代。NavigationAttribute为Navigation组件的属性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## NavigationType(deprecated)枚举说明

PhonePC/2in1TabletTVWearable

路由的跳转方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Push | 1 | 跳转到应用内的指定页面。  **说明：**  从API version 7开始支持，从API version 13开始废弃，建议使用[pushPath](ts-basic-components-navigation.md#pushpath10)替代。 |
| Replace | 2 | 用应用内的某个页面替换当前页面，并销毁被替换的页面。  **说明：**  从API version 7开始支持，从API version 13开始废弃，建议使用[replacePath](ts-basic-components-navigation.md#replacepath11)替代。 |
| Back | 3 | 返回到指定的页面。指定的页面不存在栈中时不响应。未传入指定的页面时返回上一页。  **说明：**  从API version 7开始支持，从API version 13开始废弃，建议使用[pop](ts-basic-components-navigation.md#pop10)替代。 |

## 属性

PhonePC/2in1TabletTVWearable

### active(deprecated)

PhonePC/2in1TabletTVWearable

active(value: boolean)

设置当前路由组件是否处于激活状态，处于激活状态时，会生效相应的路由操作。

说明

从API version 7开始支持，从API version 13开始废弃，建议使用[Navigation](ts-basic-components-navigation.md)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 路由组件是否处于激活状态。设置为true时，组件处于激活态。设置为false时，组件不处于激活态。 |

### params(deprecated)

PhonePC/2in1TabletTVWearable

params(value: object)

设置跳转时传递到目标页面的数据。

说明

从API version 7开始支持，从API version 13开始废弃，建议使用[param](ts-basic-components-navigation.md#属性-1)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | object | 是 | 跳转时要同时传递到目标页面的数据，可在目标页面使用[router.getParams()](js-apis-router.md#routergetparamsdeprecated)获得。 |

### target(deprecated)

PhonePC/2in1TabletTVWearable

target(value: string)

设置跳转目标页面的路径。目标页面需加入main\_pages.json文件中。

说明

从API version 7开始支持，从API version 13开始废弃，建议使用[Navigation](ts-basic-components-navigation.md)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 跳转目标页面的路径。 |

### type(deprecated)

PhonePC/2in1TabletTVWearable

type(value: NavigationType)

设置路由跳转方式。

说明

从API version 7开始支持，从API version 13开始废弃，建议使用[Navigation](ts-basic-components-navigation.md)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NavigationType](ts-container-navigator.md#navigationtypedeprecated枚举说明) | 是 | 路由跳转方式。  默认值：NavigationType.Push |

## 示例

PhonePC/2in1TabletTVWearable

```
1. // code.ets
2. export interface NameObject {
3. name: string;
4. }

6. export class TextObject {
7. text: NameObject;

9. constructor(text: NameObject) {
10. this.text = text;
11. }
12. }
```

```
1. import { NameObject, TextObject } from '../../code';

3. @Entry
4. @Component
5. struct NavigatorExample {
6. @State active: boolean = false
7. @State name: NameObject = { name: 'news' }

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
11. Navigator({ target: 'pages/container/navigator/Detail', type: NavigationType.Push }) {
12. Text('Go to ' + this.name.name + ' page')
13. .width('100%').textAlign(TextAlign.Center)
14. }.params(new TextObject(this.name)) // 传参数到Detail页面

16. Navigator() {
17. Text('Back to previous page').width('100%').textAlign(TextAlign.Center)
18. }.active(this.active)
19. .onClick(() => {
20. this.active = true
21. })
22. }.height(150).width(350).padding(35)
23. }
24. }
```

```
1. import { NameObject } from '../../code';

3. @Entry
4. @Component
5. struct DetailExample {
6. // 接收Navigator.ets的传参
7. params: Record<string, NameObject> = this.getUIContext().getRouter().getParams() as Record<string, NameObject>
8. @State name: NameObject = this.params.text

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
12. Navigator({ target: 'pages/container/navigator/Back', type: NavigationType.Push }) {
13. Text('Go to back page').width('100%').height(20)
14. }

16. Text('This is ' + this.name.name + ' page')
17. .width('100%').textAlign(TextAlign.Center)
18. }
19. .width('100%').height(200).padding({ left: 35, right: 35, top: 35 })
20. }
21. }
```

```
1. // Back.ets
2. @Entry
3. @Component
4. struct BackExample {
5. build() {
6. Column() {
7. Navigator({ target: 'pages/container/navigator/Navigator', type: NavigationType.Back }) {
8. Text('Return to Navigator Page').width('100%').textAlign(TextAlign.Center)
9. }
10. }.width('100%').height(200).padding({ left: 35, right: 35, top: 35 })
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/erwSL0_qRNaxFGn0imqQtg/zh-cn_image_0000002583440211.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000250Z&HW-CC-Expire=86400&HW-CC-Sign=B5A1E753984AD5709EB63F70B55559BE3757D4C6741CDF2A1A87125C02019EB8)
