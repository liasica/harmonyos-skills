---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-plugincomponent
title: "@ohos.pluginComponent (PluginComponentManager)"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.pluginComponent (PluginComponentManager)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e8afb3a71920539dbcabdfe6d72eff9543e3d7fc43c6471c70d488f41a3b031f
---

本模块供插件组件的使用方请求组件与数据，供提供方发送组件模板和数据。

插件组件的通信流程如下图所示。

```mermaid
sequenceDiagram
    participant 使用方 as 组件使用方
    participant 提供方 as 组件提供方

    rect rgb(235, 245, 255)
        Note over 使用方, 提供方: push通信流程（提供方主动推送）
        提供方->>使用方: push(PushParameters)
        Note right of 提供方: 携带 name、data、extraData
        使用方->>使用方: on('push') 回调触发
        Note left of 使用方: 接收 template、data、extraData
    end

    rect rgb(255, 245, 235)
        Note over 使用方, 提供方: request通信流程（使用方主动请求）
        使用方->>提供方: request(RequestParameters)
        Note left of 使用方: 携带 name、data
        提供方->>提供方: on('request') 回调触发
        Note right of 提供方: 返回 RequestEventResult（template、data、extraData）
        提供方-->>使用方: 返回请求结果
        使用方->>使用方: request 回调触发
        Note left of 使用方: 接收 componentTemplate、data、extraData
    end
```

**说明** 

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { pluginComponentManager } from '@kit.ArkUI';
```

## PluginComponentTemplate

插件组件模板参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| source | string | 否 | 否 | 组件模板名。 |
| ability | string | 否 | 否 | 提供方Ability的bundleName。 |

## pluginComponentManager

插件组件管理器，提供插件组件的请求、推送和事件监听等管理能力。

### KVObject

type KVObject = { [key: string]: number | string | boolean | [] | KVObject }

以键值对形式存储信息，符合JSON格式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [key: string] | number | string | boolean | [] | [KVObject](js-apis-plugincomponent.md#kvobject) | 否 | 键值对形式存储。  number：键值，表示值类型为数字。  string：键值，表示值类型为字符串，可取空字符串。  boolean：键值，表示值类型为布尔值。  []：键值，表示值类型为空数组。  [KVObject](js-apis-plugincomponent.md#kvobject)：键值，表示值类型为KVObject。 |

### PushParameters

使用pluginComponentManager.push方法时需要传递的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| want | [Want](js-apis-application-want.md) | 否 | 否 | 组件使用方Ability信息。 |
| name | string | 否 | 否 | 组件名称。 |
| data | [KVObject](js-apis-plugincomponent.md#kvobject) | 否 | 否 | 组件数据，以键值对形式存储，用于传递给组件使用方的业务数据，键和值类型由业务定义。 |
| extraData | [KVObject](js-apis-plugincomponent.md#kvobject) | 否 | 否 | 附加数据，以键值对形式存储，用于传递额外的业务信息，键和值类型由业务定义。 |
| jsonPath | string | 否 | 是 | 存放模板路径的[external.json](js-apis-plugincomponent.md#externaljson文件说明)文件的路径。当需要通过外部配置文件直接加载模板而非通过push通信发送时传入此参数；当jsonPath字段不为空时不触发push通信，直接从external.json中读取模板路径进行加载。不传入或为空时，触发push通信向组件使用方推送组件和数据。 |

### RequestParameters

使用pluginComponentManager.request方法时需要传递的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| want | [Want](js-apis-application-want.md) | 否 | 否 | 组件提供方Ability信息。 |
| name | string | 否 | 否 | 请求组件名称。 |
| data | [KVObject](js-apis-plugincomponent.md#kvobject) | 否 | 否 | 组件数据，以键值对形式存储，用于传递给组件提供方的业务数据，键和值类型由业务定义。 |
| jsonPath | string | 否 | 是 | 存放模板路径的[external.json](js-apis-plugincomponent.md#externaljson文件说明)文件的路径。当需要通过外部配置文件直接加载模板而非通过request通信获取时传入此参数；当jsonPath字段不为空时不触发request通信，直接从external.json中读取模板路径。不传入或为空时，触发request通信向组件提供方请求模板。 |

### RequestCallbackParameters

pluginComponentManager.request方法接收到的回调结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| componentTemplate | [PluginComponentTemplate](js-apis-plugincomponent.md#plugincomponenttemplate) | 否 | 否 | 组件模板。 |
| data | [KVObject](js-apis-plugincomponent.md#kvobject) | 否 | 否 | 组件数据，以键值对形式存储，键和值类型由业务定义。 |
| extraData | [KVObject](js-apis-plugincomponent.md#kvobject) | 否 | 否 | 附加数据。该字段为可选字段，不提供时默认不包含在返回结果中。 |

### RequestEventResult

注册request监听方法后，接收到请求事件时回应请求的数据类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| template | string | 否 | 是 | 组件模板。该字段为可选字段，不提供时默认不包含在返回结果中。当需要返回组件模板信息时设置此字段；不需要返回模板时可省略。 |
| data | [KVObject](js-apis-plugincomponent.md#kvobject) | 否 | 是 | 组件数据，以键值对形式存储，用于回应请求时传递的业务数据，键和值类型由业务定义。该字段为可选字段，不提供时默认不包含在返回结果中。 |
| extraData | [KVObject](js-apis-plugincomponent.md#kvobject) | 否 | 是 | request事件中传递的附加数据。该字段为可选字段，不提供时默认不包含在返回结果中。 |

### OnPushEventCallback

type OnPushEventCallback = (source: Want, template: PluginComponentTemplate, data: KVObject, extraData: KVObject) => void

对应push事件的监听回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [Want](js-apis-application-want.md) | 是 | push事件发送方相关信息。 |
| template | [PluginComponentTemplate](js-apis-plugincomponent.md#plugincomponenttemplate) | 是 | 组件模板。 |
| data | [KVObject](js-apis-plugincomponent.md#kvobject) | 是 | push事件中传递的数据内容，以键值对形式存储，键和值类型由业务定义。 |
| extraData | [KVObject](js-apis-plugincomponent.md#kvobject) | 是 | push事件中传递的附加数据，以键值对形式存储，键和值类型由业务定义。 |

**示例：**

```ts
import { pluginComponentManager, PluginComponentTemplate } from '@kit.ArkUI';
import { Want } from '@kit.AbilityKit';

const onPushListener = (source: Want, template: PluginComponentTemplate, data: pluginComponentManager.KVObject, extraData: pluginComponentManager.KVObject) => {
  console.info("onPushListener template.source=" + template.source);
  console.info("onPushListener source=" + JSON.stringify(source));
  console.info("onPushListener template=" + JSON.stringify(template));
  console.info("onPushListener data=" + JSON.stringify(data));
  console.info("onPushListener extraData=" + JSON.stringify(extraData));
};
```

### OnRequestEventCallback

type OnRequestEventCallback = (source: Want, name: string, data: KVObject) => RequestEventResult

对应request事件的监听回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [Want](js-apis-application-want.md) | 是 | request请求发送方相关信息。 |
| name | string | 是 | 请求的组件名称。 |
| data | [KVObject](js-apis-plugincomponent.md#kvobject) | 是 | request事件中传递的数据内容，以键值对形式存储，键和值类型由业务定义。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RequestEventResult](js-apis-plugincomponent.md#requesteventresult) | 注册request监听方法后，接收到请求事件时回应请求的数据类型。 |

**示例：**

```ts
import { pluginComponentManager } from '@kit.ArkUI';
import { Want } from '@kit.AbilityKit';

const onRequestListener = (source: Want, name: string, data: pluginComponentManager.KVObject) => {
  console.info("onRequestListener");
  console.info("onRequestListener source=" + JSON.stringify(source));
  console.info("onRequestListener name=" + name);
  console.info("onRequestListener data=" + JSON.stringify(data));
  // 构建Request事件回调的返回数据，指定组件模板路径并携带请求数据返回给请求方
  let returnData: Record<string, string | pluginComponentManager.KVObject> = {
    "template": "ets/pages/plugin.js",
    "data": data,
  }
  return returnData;
}
```

### pluginComponentManager.push

push(param: PushParameters , callback: AsyncCallback<void>): void

组件提供方向组件使用方主动发送组件和数据。适用于提供方数据更新后需主动通知使用方刷新显示的场景。

配合方法：使用方需先调用 [on('push', callback)](js-apis-plugincomponent.md#plugincomponentmanageron) 注册push事件监听，才能接收到通过本接口推送的组件和数据。若使用方未注册监听，推送的数据将无法被接收。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [PushParameters](js-apis-plugincomponent.md#pushparameters) | 是 | 推送组件的详细参数。 |
| callback | AsyncCallback<void> | 是 | 此次接口调用的异步回调。 |

**示例：**

```ts
import { pluginComponentManager } from '@kit.ArkUI';

pluginComponentManager.push(
  {
    want: {
      bundleName: "com.example.provider",
      abilityName: "com.example.provider.MainAbility",
    },
    name: "plugintemplate",
    data: {
      "key_1": "plugin component test",
      "key_2": 34234,
    },
    extraData: {
      "extra_str": "this is push event",
    },
    jsonPath: "",
  },
  (err) => {
    if (err) {
      console.error(`push_callback: err.code = ${err.code}, err.message = ${err.message}`);
      return;
    }
    console.info("push_callback: push ok!");
  }
)
```

### pluginComponentManager.request

request(param: RequestParameters, callback: AsyncCallback<RequestCallbackParameters>): void

组件使用方向组件提供方主动请求组件。适用于使用方需按需获取提供方组件及数据的场景。

配合方法：提供方需先调用 [on('request', callback)](js-apis-plugincomponent.md#plugincomponentmanageron) 注册request事件监听，才能接收到使用方通过本接口发起的请求并返回数据。若提供方未注册监听，请求将无法得到响应。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [RequestParameters](js-apis-plugincomponent.md#requestparameters) | 是 | 组件模板的详细请求信息。 |
| callback | AsyncCallback<[RequestCallbackParameters](js-apis-plugincomponent.md#requestcallbackparameters)> | 是 | 此次请求的异步回调，通过回调接口的参数返回请求所获取的数据。 |

**示例：**

```ts
import { pluginComponentManager } from '@kit.ArkUI';

pluginComponentManager.request(
  {
    want: {
      bundleName: "com.example.provider",
      abilityName: "com.example.provider.MainAbility",
    },
    name: "plugintemplate",
    data: {
      "key_1": "plugin component test",
      "key_2": 1111111,
    },
    jsonPath: "",
  },
  (err, data) => {
    if (err) {
      console.error(`request_callback: err.code = ${err.code}, err.message = ${err.message}`);
      return;
    }
    console.info("request_callback: componentTemplate.ability=" + data.componentTemplate.ability);
    console.info("request_callback: componentTemplate.source=" + data.componentTemplate.source);
    console.info("request_callback: data=" + JSON.stringify(data.data));
    console.info("request_callback: extraData=" + JSON.stringify(data.extraData));
  }
)
```

### pluginComponentManager.on

on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback): void

提供方监听"request"类型的事件，给使用方返回通过request接口主动请求的数据；使用方监听"push"类型的事件，接收提供方通过push接口主动推送的数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | string | 是 | 监听的事件类型， 可选值为："push" 、"request"。  “push”：指组件提供方向使用方主动推送数据。  “request”：指组件使用方向提供方主动请求数据。 |
| callback | [OnPushEventCallback](js-apis-plugincomponent.md#onpusheventcallback) | [OnRequestEventCallback](js-apis-plugincomponent.md#onrequesteventcallback) | 是 | 对应监听回调，push事件对应回调类型为[OnPushEventCallback](js-apis-plugincomponent.md#onpusheventcallback)，request事件对应回调类型为[OnRequestEventCallback](js-apis-plugincomponent.md#onrequesteventcallback) 。 |

**示例：**

```ts
import { pluginComponentManager, PluginComponentTemplate } from '@kit.ArkUI';
import { Want } from '@kit.AbilityKit';

const onPushListener = (source:Want, template:PluginComponentTemplate, data:pluginComponentManager.KVObject, extraData:pluginComponentManager.KVObject) => {
  console.info("onPushListener template.source=" + template.source);
  console.info("onPushListener source=" + JSON.stringify(source));
  console.info("onPushListener template=" + JSON.stringify(template));
  console.info("onPushListener data=" + JSON.stringify(data));
  console.info("onPushListener extraData=" + JSON.stringify(extraData));
}
const onRequestListener = (source:Want, name:string, data:pluginComponentManager.KVObject) => {
  console.info("onRequestListener");
  console.info("onRequestListener source=" + JSON.stringify(source));
  console.info("onRequestListener name=" + name);
  console.info("onRequestListener data=" + JSON.stringify(data));
  let returnData: Record<string, string | pluginComponentManager.KVObject> = { "template": "ets/pages/plugin.js", "data": data };
  return returnData;
}
pluginComponentManager.on("push", onPushListener);
pluginComponentManager.on("request", onRequestListener);
```

## external.json文件说明

external.json文件由开发者创建。external.json中以键值对形式存放组件名称以及对应的模板路径。以组件名称name作为关键字，对应的模板路径作为值。

**示例：**

```json
{
  "PluginProviderExample": "ets/pages/PluginProviderExample.js",
  "plugintemplate2": "ets/pages/plugintemplate2.js"
}
```
