---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-formlink
title: FormLink
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 卡片 > FormLink
category: harmonyos-references
scraped_at: 2026-04-29T13:52:48+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:fafcf2280f6fc98ce2f61c50e9f5ed5d429e90ceb52af9c9fa8b59d3a4407e73
---

提供静态卡片交互组件，用于静态卡片内部和卡片提供方应用间的交互，当前支持router、message和call三种类型的事件。

说明

* 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可以在静态卡片中使用。
* 本文仅提供静态卡片开发指导，其他卡片相关内容请参考[卡片开发指南](../harmonyos-guides/formkit-overview.md)。

## 权限

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

支持单个子组件。

## 接口

PhonePC/2in1TabletTVWearable

FormLink(options: FormLinkOptions)

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [FormLinkOptions](ts-container-formlink.md#formlinkoptions对象说明) | 是 | 定义卡片信息 |

## FormLinkOptions对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| action | string | 否 | 否 | action的类型，支持三种预定义的类型：  - router：跳转到提供方应用的指定UIAbility。  - message：自定义消息，触发后会调用提供方FormExtensionAbility的[onFormEvent()](js-apis-app-form-formextensionability.md#formextensionabilityonformevent)生命周期回调。  - call：后台启动提供方应用。触发后会拉起提供方应用的指定UIAbility（仅支持launchType为[singleton](../harmonyos-guides/uiability-launch-type.md#singleton启动模式)的UIAbility，即启动模式为单实例的UIAbility），但不会调度到前台。提供方应用需要具备后台运行权限([ohos.permission.KEEP\_BACKGROUND\_RUNNING](../harmonyos-guides/permissions-for-all.md#ohospermissionkeep_background_running))。  **说明：**  不推荐使用router事件刷新卡片UI。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |
| moduleName | string | 否 | 是 | action为router / call 类型时跳转的模块名。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |
| bundleName | string | 否 | 是 | action为router / call 类型时跳转的包名。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |
| abilityName | string | 否 | 是 | action为router / call 类型时跳转的UIAbility名。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |
| uri11+ | string | 否 | 是 | action为router 类型时跳转的UIAbility的统一资源标识符。uri和abilityName同时存在时，abilityName优先。  **卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。 |
| params | Object | 否 | 是 | 当前action携带的额外参数，内容使用JSON格式的键值对形式。call 类型时需填入参数'method'，且类型需要为string类型，用于触发UIAbility中对应的方法。  **说明：**  不建议通过params传递卡片内部的状态变量。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](ts-component-general-attributes.md)。

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

```
1. @Entry
2. @Component
3. struct FormLinkDemo {
4. build() {
5. Column() {
6. Text("这是一个静态卡片").fontSize(20).margin(10)

8. // router事件用于静态卡片跳转到对应的UIAbility
9. FormLink({
10. action: "router",
11. abilityName: "EntryAbility",
12. params: {
13. 'message': 'testForRouter' // 自定义要发送的message
14. }
15. }) {
16. Button("router event").width(120)
17. }.margin(10)

20. // message事件触发FormExtensionAbility的onFormEvent生命周期
21. FormLink({
22. action: "message",
23. abilityName: "EntryAbility",
24. params: {
25. 'message': 'messageEvent' // 自定义要发送的message
26. }
27. }) {
28. Button("message event").width(120)
29. }.margin(10)

32. // call事件用于触发UIAbility中对应的方法
33. FormLink({
34. action: "call",
35. abilityName: "EntryAbility",
36. params: {
37. 'method': 'funA', // 在EntryAbility中调用的方法名
38. 'num': 1 // 需要传递的其他参数
39. }
40. }) {
41. Button("call event").width(120)
42. }.margin(10)

44. // router事件用于静态卡片deeplink跳转到对应的UIAbility
45. FormLink({
46. action: "router",
47. uri: 'example://uri.ohos.com/link_page',
48. params: {
49. message: 'router msg for static uri deeplink' // 自定义要发送的message
50. }
51. }) {
52. Button("deeplink event").width(120)
53. }.margin(10)
54. }
55. .justifyContent(FlexAlign.Center)
56. .width('100%').height('100%')
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/kKamFc7RTIGN1rs2Hs0otA/zh-cn_image_0000002589326465.png?HW-CC-KV=V1&HW-CC-Date=20260429T055247Z&HW-CC-Expire=86400&HW-CC-Sign=DC29585EB32281D53EADD36D9F7C0C89DD901FF59A8759AA460F1B125B60ED69)

**待跳转应用 [module.json5](../harmonyos-guides/module-configuration-file.md#skills标签) uris 配置示例：**

```
1. "abilities": [
2. {
3. "skills": [
4. {
5. "uris": [
6. {
7. "scheme": "example",
8. "host": "uri.ohos.com",
9. "path": "link_page"
10. },
11. ]
12. }
13. ],
14. }
15. ]
```
