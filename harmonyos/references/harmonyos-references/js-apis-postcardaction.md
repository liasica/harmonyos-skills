---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-postcardaction
title: postCardAction
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > postCardAction
category: harmonyos-references
scraped_at: 2026-04-28T08:00:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:221e165efdf023ac29a021b0a298433e5a086e850e266532c2f8672385f63a52
---

用于卡片内部和提供方应用间的交互，当前支持router、message和call三种类型的事件，仅在卡片中可以调用。

说明

本接口从API version 9开始支持。

## postCardAction

PhonePC/2in1TabletTVWearable

postCardAction(component: Object, action: Object): void

执行函数内部的交互，处理component和action对象的相关操作，不返回任何内容。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| component | Object | 是 | 当前自定义组件的实例，通常传入this。 |
| action | Object | 是 | action的具体描述，详情见下表。 |

action参数说明：

| **参数名** | **类型** | **必填** | **取值说明** |
| --- | --- | --- | --- |
| action | string | 是 | action的类型，支持三种预定义的类型：  - router：跳转到提供方应用的指定UIAbility，只允许在点击事件中触发。  - message：自定义消息，触发后会调用提供方FormExtensionAbility的[onFormEvent()](js-apis-app-form-formextensionability.md#formextensionabilityonformevent)生命周期回调。  - call：后台启动提供方应用。触发后会拉起提供方应用的指定UIAbility（仅支持launchType为singleton的[UIAbility](../harmonyos-guides/uiability-launch-type.md)，即启动模式为单实例的UIAbility），但不会调度到前台。提供方应用需要具备后台运行权限([ohos.permission.KEEP\_BACKGROUND\_RUNNING](../harmonyos-guides/permissions-for-all.md#ohospermissionkeep_background_running))。 |
| bundleName | string | 否 | action为router / call 类型时跳转的包名。 |
| moduleName | string | 否 | action为router / call 类型时跳转的模块名。 |
| abilityName | string | 否 | action为router / call 类型时跳转的UIAbility名。 |
| uri11+ | string | 否 | action为router 类型时跳转的UIAbility的统一资源标识符。uri和abilityName同时存在时，abilityName优先。 |
| params | Object | 否 | 当前action携带的额外参数，内容使用JSON格式的键值对形式。 |

说明

"action"为"call" 类型时，"params"需填入参数'method'，且类型需为string类型，用于触发UIAbility中对应的方法。

**示例：**

```
1. Button('跳转')
2. .width('40%')
3. .height('20%')
4. .onClick(() => {
5. postCardAction(this, {
6. action: 'router',
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EntryAbility',
9. params: {
10. message: 'testForRouter' // 自定义要发送的message
11. }
12. });
13. })

15. Button('拉至后台')
16. .width('40%')
17. .height('20%')
18. .onClick(() => {
19. postCardAction(this, {
20. action: 'call',
21. bundleName: 'com.example.myapplication',
22. abilityName: 'EntryAbility',
23. params: {
24. method: 'fun', // 自定义调用的方法名，必填
25. message: 'testForCall' // 自定义要发送的message
26. }
27. });
28. })

30. Button('URI跳转')
31. .width('40%')
32. .height('20%')
33. .onClick(() => {
34. postCardAction(this, {
35. action: 'router',
36. uri: 'example://uri.ohos.com/link_page',
37. params: {
38. message: 'router msg for dynamic uri deeplink' // 自定义要发送的message
39. }
40. });
41. })
```

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
10. }
11. ]
12. }
13. ]
14. }
15. ]
```
