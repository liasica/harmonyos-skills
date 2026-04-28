---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navrouter
title: NavRouter
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 已停止维护的组件与接口 > NavRouter
category: harmonyos-references
scraped_at: 2026-04-28T08:02:49+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ba13b2ea49a79538e32121f3af34fa1286d69a96197eafcbb21756e86e5a4aaf
---

导航组件，默认提供点击响应处理，不需要开发者自定义点击事件逻辑。

说明

从API version 13开始，该组件不再维护，推荐使用[NavPathStack](ts-basic-components-navigation.md#navpathstack10)配合navDestination属性进行页面路由。

该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

必须包含两个子组件，其中第二个子组件必须为[NavDestination](ts-basic-components-navdestination.md)。

说明

子组件个数异常时：

1. 有且仅有1个时，触发路由到NavDestination的能力失效。
2. 有且仅有1个时，且使用NavDestination场景下，不进行路由。
3. 大于2个时，后续的子组件不显示。
4. 第二个子组件不为NavDestination时，触发路由功能失效。

## 接口

PhonePC/2in1TabletTVWearable

### NavRouter(deprecated)

PhonePC/2in1TabletTVWearable

NavRouter()

说明

从API version 9开始支持，从API version 13开始废弃，建议使用[NavPathStack](ts-basic-components-navigation.md#navpathstack10)和[navDestination](ts-basic-components-navigation.md#navdestination10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### NavRouter(deprecated)

PhonePC/2in1TabletTVWearable

NavRouter(value: RouteInfo)

提供路由信息，指定点击NavRouter时，要跳转的NavDestination页面。

说明

从API version 10开始支持，从API version 13开始废弃，建议使用[NavPathStack](ts-basic-components-navigation.md#navpathstack10)和[navDestination](ts-basic-components-navigation.md#navdestination10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [RouteInfo](ts-basic-components-navrouter.md#routeinfodeprecated对象说明) | 是 | 路由信息。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### mode(deprecated)

PhonePC/2in1TabletTVWearable

mode(mode: NavRouteMode)

设置指定点击NavRouter跳转到NavDestination页面时，使用的路由模式。

说明

从API version 10开始支持，从API version 13开始废弃，建议使用[LaunchMode](ts-basic-components-navigation.md#launchmode12枚举说明)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [NavRouteMode](ts-basic-components-navrouter.md#navroutemodedeprecated枚举说明) | 是 | 指定点击NavRouter跳转到NavDestination页面时，使用的路由模式。  默认值：NavRouteMode.PUSH\_WITH\_RECREATE |

## RouteInfo(deprecated)对象说明

PhonePC/2in1TabletTVWearable

路由信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 点击NavRouter跳转到的NavDestination页面的名称。  **说明：**  从API version 10开始支持，从API version 13开始废弃，建议使用[name](ts-basic-components-navigation.md#属性-1)替代。 |
| param | unknown | 否 | 是 | 点击NavRouter跳转到NavDestination页面时，传递的参数。  **说明：**  从API version 10开始支持，从API version 13开始废弃，建议使用[param](ts-basic-components-navigation.md#属性-1)替代。 |

## NavRouteMode(deprecated)枚举说明

PhonePC/2in1TabletTVWearable

路由模式。

说明

从API version 10开始支持，从API version 13开始废弃，建议使用[NavPathStack](ts-basic-components-navigation.md#navpathstack10)和[navDestination](ts-basic-components-navigation.md#navdestination10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| --- | --- |
| PUSH\_WITH\_RECREATE | 跳转到新的NavDestination页面时，替换当前显示的NavDestination页面，页面销毁，但该页面信息仍保留在路由栈中。 |
| PUSH | 跳转到新的NavDestination页面时，覆盖当前显示的NavDestination页面，该页面不销毁，且页面信息保留在路由栈中。 |
| REPLACE | 跳转到新的NavDestination页面时，替换当前显示的NavDestination页面，页面销毁，且该页面信息从路由栈中清除。 |

## 事件

PhonePC/2in1TabletTVWearable

### onStateChange(deprecated)

PhonePC/2in1TabletTVWearable

onStateChange(callback: (isActivated: boolean) => void)

组件激活状态切换时触发该回调。开发者点击激活NavRouter，加载对应的NavDestination子组件时，回调onStateChange(true)。NavRouter对应的NavDestination子组件不再显示时，回调onStateChange(false)。

说明

从API version 9开始支持，从API version 13开始废弃，建议使用[onShown](ts-basic-components-navdestination.md#onshown10)和[onHidden](ts-basic-components-navdestination.md#onhidden10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isActivated | boolean | 是 | isActivated为true时表示激活，为false时表示未激活。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct NavRouterExample {
5. @State isActiveWLAN: boolean = false
6. @State isActiveBluetooth: boolean = false

8. build() {
9. Navigation() {
10. NavRouter() {
11. Row() {
12. Row()
13. .width(30)
14. .height(30)
15. .borderRadius(30)
16. .margin({ left: 3, right: 10 })
17. .backgroundColor(Color.Pink)
18. Text(`WLAN`)
19. .fontSize(22)
20. .fontWeight(500)
21. .textAlign(TextAlign.Center)
22. }
23. .width('90%')
24. .height(60)

26. NavDestination() {
27. Flex({ direction: FlexDirection.Row }) {
28. Text('未找到可用WLAN').fontSize(30).padding({ left: 15 })
29. }
30. }.title("WLAN")
31. }
32. .margin({ top: 10, bottom: 10 })
33. .backgroundColor(this.isActiveWLAN ? '#ccc' : '#fff')
34. .borderRadius(20)
35. .mode(NavRouteMode.PUSH_WITH_RECREATE)
36. .onStateChange((isActivated: boolean) => {
37. this.isActiveWLAN = isActivated
38. })

40. NavRouter() {
41. Row() {
42. Row()
43. .width(30)
44. .height(30)
45. .borderRadius(30)
46. .margin({ left: 3, right: 10 })
47. .backgroundColor(Color.Pink)
48. Text(`蓝牙`)
49. .fontSize(22)
50. .fontWeight(500)
51. .textAlign(TextAlign.Center)
52. }
53. .width('90%')
54. .height(60)

56. NavDestination() {
57. Flex({ direction: FlexDirection.Row }) {
58. Text('未找到可用蓝牙').fontSize(30).padding({ left: 15 })
59. }
60. }.title("蓝牙")
61. }
62. .margin({ top: 10, bottom: 10 })
63. .backgroundColor(this.isActiveBluetooth ? '#ccc' : '#fff')
64. .borderRadius(20)
65. .mode(NavRouteMode.REPLACE)
66. .onStateChange((isActivated: boolean) => {
67. this.isActiveBluetooth = isActivated
68. })
69. }
70. .height('100%')
71. .width('100%')
72. .title('设置')
73. .backgroundColor("#F2F3F5")
74. .titleMode(NavigationTitleMode.Free)
75. .mode(NavigationMode.Auto)
76. }
77. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/_s8G3E07T52WQEtLU29T4Q/zh-cn_image_0000002552800516.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000248Z&HW-CC-Expire=86400&HW-CC-Sign=33D1784908C4F2161AE20AFA92AC993769D971519882944382268351E23818BF)
