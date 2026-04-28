---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-plugincomponent
title: @ohos.pluginComponent (PluginComponentManager)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.pluginComponent (PluginComponentManager)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:32+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:cbbca65ad40b12bdab933d4e013c7f57b6e6a10e94e775ec62d06584e08a066c
---

用于给插件组件的使用方请求组件与数据，使用方发送组件模板和数据。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { pluginComponentManager } from '@kit.ArkUI';
```

## PluginComponentTemplate

PhonePC/2in1TabletTVWearable

Plugin组件模板参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| source | string | 否 | 否 | 组件模板名。 |
| ability | string | 否 | 否 | 提供方Ability的bundleName。 |

## pluginComponentManager

PhonePC/2in1TabletTVWearable

插件组件管理器。

### KVObject

PhonePC/2in1TabletTVWearable

type KVObject = { [key: string]: number | string | boolean | [] | KVObject }

以键值对形式存储信息，符合json格式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [key: string] | number | string | boolean | [] | [KVObject](js-apis-plugincomponent.md#kvobject) | 否 | 键值对形式存储。  number：键值，表示值类型为数字。  string：键值，表示值类型为字符串，可取空字符串。  boolean：键值，表示值类型为布尔值。  []：键值，可取值为[]。  [KVObject](js-apis-plugincomponent.md#kvobject)：键值，表示值类型为KVObject。 |

### PushParameters

PhonePC/2in1TabletTVWearable

使用PluginManager.Push方法时需要传递的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| want | [Want](js-apis-application-want.md) | 否 | 否 | 组件使用方Ability信息。 |
| name | string | 否 | 否 | 组件名称。 |
| data | [KVObject](js-apis-plugincomponent.md#kvobject) | 否 | 否 | 组件数据。 |
| extraData | [KVObject](js-apis-plugincomponent.md#kvobject) | 否 | 否 | 附加数据。 |
| jsonPath | string | 否 | 是 | 存放模板路径的[external.json](js-apis-plugincomponent.md#externaljson文件说明)文件的路径。 |

### RequestParameters

PhonePC/2in1TabletTVWearable

使用PluginManager.Request方法时需要传递的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| want | [Want](js-apis-application-want.md) | 否 | 否 | 组件提供方Ability信息。 |
| name | string | 否 | 否 | 请求组件名称。 |
| data | [KVObject](js-apis-plugincomponent.md#kvobject) | 否 | 否 | 组件数据。 |
| jsonPath | string | 否 | 是 | 存放模板路径的[external.json](js-apis-plugincomponent.md#externaljson文件说明)文件的路径。当jsonPath字段不为空时不触发Request通信。 |

### RequestCallbackParameters

PhonePC/2in1TabletTVWearable

PluginManager.Request方法接收到的回调结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| componentTemplate | [PluginComponentTemplate](js-apis-plugincomponent.md#plugincomponenttemplate) | 否 | 否 | 组件模板。 |
| data | [KVObject](js-apis-plugincomponent.md#kvobject) | 否 | 否 | 组件数据。 |
| extraData | [KVObject](js-apis-plugincomponent.md#kvobject) | 否 | 否 | 附加数据。 |

### RequestEventResult

PhonePC/2in1TabletTVWearable

注册Request监听方法后，接收到请求事件时回应请求的数据类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| template | string | 否 | 是 | 组件模板。 |
| data | [KVObject](js-apis-plugincomponent.md#kvobject) | 否 | 是 | 组件数据。 |
| extraData | [KVObject](js-apis-plugincomponent.md#kvobject) | 否 | 是 | 附加数据。 |

### OnPushEventCallback

PhonePC/2in1TabletTVWearable

type OnPushEventCallback = (source: Want, template: PluginComponentTemplate, data: KVObject, extraData: KVObject) => void

对应Push事件的监听回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [Want](js-apis-application-want.md) | 是 | Push请求发送方相关信息。 |
| template | [PluginComponentTemplate](js-apis-plugincomponent.md#plugincomponenttemplate) | 是 | 请求组件模板名称。 |
| data | [KVObject](js-apis-plugincomponent.md#kvobject) | 是 | 数据。 |
| extraData | [KVObject](js-apis-plugincomponent.md#kvobject) | 是 | 附加数据。 |

**示例：**

```
1. import { pluginComponentManager, PluginComponentTemplate } from '@kit.ArkUI';
2. import { Want } from '@kit.AbilityKit';

4. function onPushListener(source: Want, template: PluginComponentTemplate, data: pluginComponentManager.KVObject, extraData: pluginComponentManager.KVObject) {
5. console.info("onPushListener template.source=" + template.source);
6. console.info("onPushListener source=" + JSON.stringify(source));
7. console.info("onPushListener template=" + JSON.stringify(template));
8. console.info("onPushListener data=" + JSON.stringify(data));
9. console.info("onPushListener extraData=" + JSON.stringify(extraData));
10. }
```

### OnRequestEventCallback

PhonePC/2in1TabletTVWearable

type OnRequestEventCallback = (source: Want, name: string, data: KVObject) => RequestEventResult

对应request事件的监听回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [Want](js-apis-application-want.md) | 是 | request请求发送方相关信息。 |
| name | string | 是 | 模板名称。 |
| data | [KVObject](js-apis-plugincomponent.md#kvobject) | 是 | 数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RequestEventResult](js-apis-plugincomponent.md#requesteventresult) | 注册Request监听方法后，接收到请求事件时回应请求的数据类型。 |

**示例：**

```
1. import { pluginComponentManager } from '@kit.ArkUI';
2. import { Want } from '@kit.AbilityKit';

4. function onRequestListener(source: Want, name: string, data: pluginComponentManager.KVObject) {
5. console.info("onRequestListener");
6. console.info("onRequestListener source=" + JSON.stringify(source));
7. console.info("onRequestListener name=" + name);
8. console.info("onRequestListener data=" + JSON.stringify(data));
9. let RtnData: Record<string, string | pluginComponentManager.KVObject> = {
10. 'template': "ets/pages/plugin.js",
11. 'data': data,
12. }
13. return RtnData;
14. }
```

### pluginComponentManager.push

PhonePC/2in1TabletTVWearable

push(param: PushParameters , callback: AsyncCallback<void>): void

组件提供方向组件使用方主动发送组件和数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [PushParameters](js-apis-plugincomponent.md#pushparameters) | 是 | 组件使用方的详细信息。 |
| callback | AsyncCallback<void> | 是 | 此次接口调用的异步回调。 |

**示例：**

```
1. import { pluginComponentManager } from '@kit.ArkUI';

3. pluginComponentManager.push(
4. {
5. want: {
6. bundleName: "com.example.provider",
7. abilityName: "com.example.provider.MainAbility",
8. },
9. name: "plugintemplate",
10. data: {
11. "key_1": "plugin component test",
12. "key_2": 34234,
13. },
14. extraData: {
15. "extra_str": "this is push event",
16. },
17. jsonPath: "",
18. },
19. (err) => {
20. console.info("push_callback: push ok!");
21. }
22. )
```

### pluginComponentManager.request

PhonePC/2in1TabletTVWearable

request(param: RequestParameters, callback: AsyncCallback<RequestCallbackParameters>): void

组件使用方向组件提供方主动请求组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [RequestParameters](js-apis-plugincomponent.md#requestparameters) | 是 | 组件模板的详细请求信息。 |
| callback | AsyncCallback<[RequestCallbackParameters](js-apis-plugincomponent.md#requestcallbackparameters)> | 是 | 此次请求的异步回调，通过回调接口的参数返回接收请求的数据。 |

**示例：**

```
1. import { pluginComponentManager } from '@kit.ArkUI';

3. pluginComponentManager.request(
4. {
5. want: {
6. bundleName: "com.example.provider",
7. abilityName: "com.example.provider.MainAbility",
8. },
9. name: "plugintemplate",
10. data: {
11. "key_1": "plugin component test",
12. "key_2": 1111111,
13. },
14. jsonPath: "",
15. },
16. (err, data) => {
17. console.info("request_callback: componentTemplate.ability=" + data.componentTemplate.ability);
18. console.info("request_callback: componentTemplate.source=" + data.componentTemplate.source);
19. console.info("request_callback: data=" + JSON.stringify(data.data));
20. console.info("request_callback: extraData=" + JSON.stringify(data.extraData));
21. }
22. )
```

### pluginComponentManager.on

PhonePC/2in1TabletTVWearable

on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback): void

提供方监听"request"类型的事件，给使用方返回通过request接口主动请求的数据；使用方监听"push"类型的事件，接收提供方通过push接口主动推送的数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | string | 是 | 监听的事件类型， 可选值为："push" 、"request"。  "push”：指组件提供方向使用方主动推送数据。  "request”：指组件使用方向提供方主动请求数据。 |
| callback | [OnPushEventCallback](js-apis-plugincomponent.md#onpusheventcallback) | [OnRequestEventCallback](js-apis-plugincomponent.md#onrequesteventcallback) | 是 | 对应监听回调，push事件对应回调类型为[OnPushEventCallback](js-apis-plugincomponent.md#onpusheventcallback)，request事件对应回调类型为[OnRequestEventCallback](js-apis-plugincomponent.md#onrequesteventcallback) 。 |

**示例：**

```
1. import { pluginComponentManager, PluginComponentTemplate } from '@kit.ArkUI';
2. import { Want } from '@kit.AbilityKit';

4. function onPushListener(source:Want, template:PluginComponentTemplate, data:pluginComponentManager.KVObject, extraData:pluginComponentManager.KVObject) {
5. console.info("onPushListener template.source=" + template.source);
6. console.info("onPushListener source=" + JSON.stringify(source));
7. console.info("onPushListener template=" + JSON.stringify(template));
8. console.info("onPushListener data=" + JSON.stringify(data));
9. console.info("onPushListener extraData=" + JSON.stringify(extraData));
10. }
11. function onRequestListener(source:Want, name:string, data:pluginComponentManager.KVObject) {
12. console.info("onRequestListener");
13. console.info("onRequestListener source=" + JSON.stringify(source));
14. console.info("onRequestListener name=" + name);
15. console.info("onRequestListener data=" + JSON.stringify(data));
16. let RtnData:Record<string,string|pluginComponentManager.KVObject> = { 'template': "ets/pages/plugin.js", 'data': data };
17. return RtnData;
18. }
19. pluginComponentManager.on("push", onPushListener);
20. pluginComponentManager.on("request", onRequestListener);
```

## external.json文件说明

PhonePC/2in1TabletTVWearable

external.json文件由开发者创建。external.json中以键值对形式存放组件名称以及对应模板路径。以组件名称name作为关键字，对应模板路径作为值。

**示例**

```
1. {
2. "PluginProviderExample": "ets/pages/PluginProviderExample.js",
3. "plugintemplate2": "ets/pages/plugintemplate2.js"
4. }
```
