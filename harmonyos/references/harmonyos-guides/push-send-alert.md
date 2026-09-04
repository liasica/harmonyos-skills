---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-send-alert
title: 发送通知消息
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 推送场景化消息 > 推送通知消息 > 发送通知消息
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:18+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:c42128ec53d7931128a093a4fe3313a3087919c657a0f0d0260d8a597539fd18
---

## 场景介绍

通知消息通过Push Kit通道直接下发，可在终端设备的通知中心、锁屏、横幅等展示，用户点击后拉起应用。您可以通过[设置通知消息样式](push-send-alert.md#设置通知消息样式)来吸引用户。

## 约束与限制

发送通知消息能力支持Phone、Tablet、PC/2in1设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备。

## 开通权益

Push Kit根据消息内容，将通知消息分类为**服务与通讯**、**资讯营销**两大类别，开放通知消息自分类权益。

两种类型的通知消息在**提醒方式、消息展示位置、推送数量**上皆存在差异。更多说明与权益申请详情参见[申请通知消息自分类权益](push-apply-right.md#申请通知消息自分类权益)。

**说明** 

* **若您未申请通知消息自分类权益，则推送的通知消息默认为资讯营销类（[category](../harmonyos-references/push-scenariozed-api-request-param.md#notification)取值为MARKETING）消息**；若您仅需发送资讯营销类消息，则无需申请通知消息自分类权益。
* 资讯营销类消息每天可发送消息数量根据应用类型分为**2条**或**5条**，详情请参见[通知消息推送数量管理规则](push-apply-right.md#通知消息推送数量管理规则)。若您发送通知消息被频控，请尝试发送测试消息或申请自分类权益，详情请参见[消息频控](../harmonyos-references/push-msg-freq-control.md)。

## 频控规则

**调测阶段**，每个项目每日全网最多可推送1000条测试消息。发送测试消息需设置[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)为true。

**正式发布阶段**，单设备单应用下每日推送消息总条数受[设备消息频控](../harmonyos-references/push-msg-freq-control.md#设备消息频控)限制，系统会根据使用场景和流量进行管控，不合理的使用场景系统会进行频控。

服务通讯类消息与资讯营销类消息存在不同的频控策略，详情请参见[通知消息推送数量管理规则](push-apply-right.md#通知消息推送数量管理规则)。

## 开发步骤

1. 参见指导[获取Push Token](push-get-token.md)。
2. 为确保应用可正常收到消息，应用发送通知前需调用[requestEnableNotification](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10-1)()方法弹出提醒，告知用户需要允许接收通知消息。示例代码如下：

   导入notificationManager模块及相关公共模块：

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { UIAbility } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';
   import { notificationManager } from '@kit.NotificationKit';
   ```

   向用户请求通知授权:

   ```typescript
   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     // ...
     onWindowStageCreate(windowStage: window.WindowStage) {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
       windowStage.loadContent('pages/Index', (err, data) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
           return;
         }
         hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
         notificationManager.requestEnableNotification(this.context).then(() => {
           hilog.info(DOMAIN, 'testTag', 'RequestEnableNotification success');
         }).catch((err: BusinessError) => {
           hilog.error(DOMAIN, 'testTag',
             `RequestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
         });
       });
     }
     // ...
   }
   ```
3. 为确保点击消息可以正常跳转应用页面，在应用项目中完成skills标签配置，详情请参见[点击消息动作](push-send-alert.md#点击消息动作)。
4. 应用服务端调用Push Kit服务端的REST API推送通知消息。若未[开通权益](push-send-alert.md#开通权益)，或开通的权益类型与[调用REST API推送场景化消息](push-scenes-send.md)时，请求体中携带的[category](../harmonyos-references/push-scenariozed-api-request-param.md#notification)字段值不一致，消息将会默认归为**资讯营销类消息**，则会受到“单个应用每日每设备推送数量为2条或5条”的[频控](push-apply-right.md#通知消息推送数量管理规则)限制。

   **说明** 

   * 本示例仅包含REST API中部分消息字段，关于服务端开发的更多详情请参见[端云调试](push-server-intro.md)。
   * 请使用V3版本的请求URL（https://push-api.cloud.huawei.com/v3/[projectId]/messages:send）进行消息推送。

     请求URL版本为V3（https://push-api.cloud.huawei.com/v3/[projectId]/messages:send）时，仅支持给HarmonyOS Next/5.x及之后的系统版本推送通知；版本为V2（https://push-api.cloud.huawei.com/v2/[projectId]/messages:send）时，仅支持给HarmonyOS 3.x/4.x的系统版本推送通知。

   请求示例如下（注意category参数设置为实际消息类型）：

   ```json5
   // Request URL
   POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

   // Request Header
   Content-Type: application/json
   Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   push-type: 0

   // Request Body
   {
     "payload": {
       "notification": {
         "category": "xxxxxx", // 替换为实际消息类型
         "title": "普通通知标题",
         "body": "普通通知内容",
         "clickAction": {
           "actionType": 0
         },
         // 通知是否在应用在前台情况下展示，仅对push-type为0的通知消息生效
         "foregroundShow": true,
         "notifyId": 12345
       }
     },
     "target": {
       "token": ["MAMzLg**********lPW"]
     },
     "pushOptions": {
      "testMessage": true,
       "ttl": 86400
     }
   }
   ```

   * [projectId]：项目ID，登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
   * Authorization：JWT格式字符串，可参见[Authorization](../harmonyos-references/push-scenariozed-api-request-struct.md#request-header)获取。
   * push-type：0表示Alert消息，此处为通知消息场景。
   * category：表示通知消息自分类的类别，MARKETING为资讯营销类消息，更多类别可参见[category](../harmonyos-references/push-scenariozed-api-request-param.md#notification)获取。
   * actionType：0表示[点击消息进入应用首页](push-send-alert.md#点击消息进入应用首页)，1表示[点击消息后进入应用内页](push-send-alert.md#点击消息进入应用内页)。
   * token：Push Token，可参见[获取Push Token](push-get-token.md)获取。
   * testMessage：（选填）测试消息标识，true表示测试消息。每个项目每天限制发送1000条测试消息，单次推送可发送Token数不超过10个。详情请参见[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)。
   * ttl：（选填）消息缓存时间，详见[ttl](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)。
   * notifyId：（选填）自定义消息标识字段。不携带或者设置-1时，Push Kit自动为每条消息生成一个唯一标识；不同的通知消息可以拥有相同的notifyId，实现新消息覆盖旧消息功能。仅支持数字，范围 [0, 2147483647]，若要**用于消息撤回则必填**。详情请参见[notifyId](../harmonyos-references/push-scenariozed-api-request-param.md#notification)。
   * foregroundShow：（选填）通知消息是否在应用在前台时候展示。true表示应用在前后台都展示。false表示应用只在后台展示，应用在前台时，通知栏消息将不会展示。默认为true。foregroundShow为true时，[receiveMessage](../harmonyos-references/push-pushservice.md#pushservicereceivemessage)不会被触发，无法获取消息数据。
5. 发送消息推送请求，请求响应请参见[响应参数](../harmonyos-references/push-scenariozed-api-response.md)。请求发送成功后，可检查设备是否收到通知消息，如果设备未收到通知消息，请参见[常见问题](push-faq-2.md)进行排查。

## 点击消息动作

### 点击消息进入应用首页

1. 检查项目模块级别下的**src/main/module.json5**中的[skills标签](module-configuration-file.md#skills标签)配置，其中用于标识**应用首页**的skill（即配置了"entity.system.home"和"ohos.want.action.home"的skill）中**不要配置uris，否则消息会接收不到**。

   **说明** 

   module.json5文件中的skills标签下可以同时存在多个skill对象，每个对象对应一种能力。

   若您需要同时设置推送消息跳转能力和其他跳转能力（如NFC跳转、浏览器跳转等），需要在skills数组中创建不同的skill对象，分别映射对应的能力。

   点击消息进入应用首页skills标签配置示例：

   ```json5
   {
     "module": {
       // ...
       "abilities": [
         {
           "name": "EntryAbility",
           "srcEntry": "./ets/entryability/EntryAbility.ets",
           "description": "$string:EntryAbility_desc",
           "icon": "$media:layered_image",
           "label": "$string:EntryAbility_label",
           "startWindowIcon": "$media:startIcon",
           "startWindowBackground": "$color:start_window_background",
           "exported": true,
           "skills": [
             // 该skill标识应用首页，不要配置uris
             {
               "entities": [
                 "entity.system.home"
               ],
               "actions": [
                 // "action.system.home"为API19以下版本配置，已废弃
                 "ohos.want.action.home"
               ]
             },
             // 其他skill配置
             {}
           ]
         },
         // ...
       ]
     }
   }
   ```
2. 发送消息时设置**actionType**字段为0。

   ```json5
   // Request URL
   POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

   // Request Header
   Content-Type: application/json
   Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   push-type: 0

   // Request Body
   {
     "payload": {
       "notification": {
         "category": "MARKETING",
         "title": "普通通知标题",
         "body": "普通通知内容",
         "clickAction": {
           "actionType": 0,
           "data": {"testKey": "testValue"}
         }
       }
     },
     "target": {
       "token": ["MAMzLg**********lPW"]
     },
     "pushOptions": {
       "testMessage": true
     }
   }
   ```

   * actionType：点击消息的动作，0表示点击消息后进入首页（即入口Ability当前所在页面，入口Ability通常为EntryAbility）。

     **说明** 

     场景化消息[请求体](../harmonyos-references/push-scenariozed-api-request-struct.md)中，接口URL版本为V3（https://push-api.cloud.huawei.com/v3/[projectId]/messages:send）时，仅支持给HarmonyOS Next/5.x及之后的系统版本推送通知；接口URL版本为V2（https://push-api.cloud.huawei.com/v2/[projectId]/messages:send）时，仅支持给HarmonyOS 3.x/4.x的系统版本推送通知。

### 点击消息进入应用内页

1. 在您的项目模块级别下的**src/main/module.json5** 中设置目标Ability中[skills标签](module-configuration-file.md#skills标签)的actions或uris值，两种方式如下：

   方式一：在[skills标签](module-configuration-file.md#skills标签)中新增一个**独立的skill对象**，配置**actions参数**用于点击消息进入应用内页，示例如下：

   ```json5
   {
     "name": "TestAbility",
     "srcEntry": "./ets/abilities/TestAbility.ets",
     "exported": false,
     "startWindowIcon": "$media:startIcon",
     "startWindowBackground": "$color:start_window_background",
     "skills": [
       // 保持现有skill对象不变
       {
         "actions": [
           "com.app.action"
         ]
       },
       // 新增一个独立的skill对象，配置actions参数
       {
         "actions": [
           "com.test.action"
         ]
       }
     ]
     // ...
   }
   ```

   方式二：在[skills标签](module-configuration-file.md#skills标签)中新增一个**独立的skill对象**，配置**uris参数**用于点击消息进入应用内页（**必须同时配置actions参数和uris参数，actions参数为空**），示例如下：

   ```json5
   {
     "name": "InnerUrisAbility",
     "srcEntry": "./ets/abilities/InnerUrisAbility.ets",
     "exported": false,
     "startWindowIcon": "$media:startIcon",
     "startWindowBackground": "$color:start_window_background",
     "skills": [
       // 保持现有skill对象不变
       {
         "actions": [
           "com.app.action"
         ]
       },
       // 新增一个独立的skill对象，配置uris参数，且必须同时配置actions参数，actions参数为空字符串
       {
         "actions": [
           ""
         ],
         "uris": [
           {
             "scheme": "https",
             "host": "www.xxx.com",
             "port": "8080",
             "path": "push/test"
           }
         ]
       }
     ]
     // ...
   }
   ```

   **说明** 

   module.json5文件中的skills标签下可以同时存在多个skill对象，每个对象对应一种能力。

   若您需要同时设置推送消息跳转能力和其他跳转能力（如NFC跳转、浏览器跳转等），需要在skills数组中创建不同的skill对象，分别映射对应的能力。
2. 发送消息时[clickAction](../harmonyos-references/push-scenariozed-api-request-param.md#clickaction)中设置**actionType**字段为1。

   ```json5
   // Request URL
   POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

   // Request Header
   Content-Type: application/json
   Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   push-type: 0

   // Request Body
   {
     "payload": {
       "notification": {
         "category": "MARKETING",
         "title": "普通通知标题",
         "body": "普通通知内容",
         "clickAction": {
           "actionType": 1,
           "action": "com.test.action",
           "uri": "https://www.xxx.com:8080/push/test",
           "data": {"testKey": "testValue"}
         }
       }
     },
     "target": {
       "token": ["MAMzLg**********lPW"]
     },
     "pushOptions": {
       "testMessage": true
     }
   }
   ```

   * actionType：点击消息动作，1表示点击消息后进入应用内页。当本字段设置为1时，uri和action至少填写一个，若都填写优先寻找与action匹配的应用页面。若action和uri都未匹配到应用页面，则点击消息后会进入应用首页。
   * action：表示能够接收[Want](../harmonyos-references/js-apis-inner-ability-want.md)的action值的集合，取值可以自定义。
   * uri：表示与[Want](../harmonyos-references/js-apis-inner-ability-want.md)中uris相匹配的集合，uris规则请参见[skills标签](module-configuration-file.md#skills标签)。

   **说明** 

   * 场景化消息[请求体](../harmonyos-references/push-scenariozed-api-request-struct.md)中，接口URL版本为V3（https://push-api.cloud.huawei.com/v3/[projectId]/messages:send）时，仅支持给HarmonyOS Next/5.x及之后的系统版本推送通知；接口URL版本为V2（https://push-api.cloud.huawei.com/v2/[projectId]/messages:send）时，仅支持给HarmonyOS 3.x/4.x的系统版本推送通知。
   * 若action和uri都未匹配成功，则点击消息后会进入应用首页。

### 数据传递

应用服务端调用Push Kit服务端的REST API推送通知消息时，可携带**data**字段，当用户点击消息时将传递数据至客户端应用。

1. 调用REST API推送通知消息，消息体中[clickAction](../harmonyos-references/push-scenariozed-api-request-param.md#clickaction)携带**data**字段。

   ```json5
   {
     "payload": {
       "notification": {
         "category": "MARKETING",
         "title": "普通通知标题",
         "body": "普通通知内容",
         "clickAction": {
           "actionType": 0,
           "data": {"testKey": "testValue"} // 携带data字段
         }
       }
     },
     "target": {
       "token": ["MAMzLg**********lPW"]
     },
     "pushOptions": {
       "testMessage": true
     }
   }
   ```

   data：点击消息时携带的JSON格式的数据。
2. 在待跳转页面（以TestAbility为例）中的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)()方法中覆盖重写如下代码（[冷启动](uiability-intra-device-interaction.md#目标uiability冷启动)时进入该生命周期回调）：

   ```typescript
   import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   // ...
   const DOMAIN = 0x0000;

   export default class InnerUrisAbility extends UIAbility {
     // ...
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'InnerUrisAbility onCreate');
       // 获取消息中传递的data数据
       const value = want.parameters?.['testKey']; // value: "testValue"
       hilog.info(DOMAIN, 'testTag', 'Succeeded in getting message data, value is %{public}s', value ?? 'default value');
       // 根据实际业务场景对data进行处理
       // ...
     }
     // ...
   }
   ```

   [onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)()方法中覆盖重写如下代码（[热启动](uiability-intra-device-interaction.md#目标uiability热启动)时进入该生命周期回调）：

   ```typescript
   import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   // ...
   const DOMAIN = 0x0000;

   export default class InnerUrisAbility extends UIAbility {
     // ...
     onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'InnerUrisAbility onNewWant');
       // 获取消息中传递的data数据
       const value = want.parameters?.['testKey']; // value: "testValue"
       hilog.info(DOMAIN, 'testTag', 'Succeeded in getting message data, value is %{public}s', value ?? 'default value');
       // 根据实际业务场景对data进行处理
       // ...
     }
     // ...
   }
   ```

**说明** 

onNewWant()方法仅在单例（singleton）模式下可用。

## 设置通知消息样式

Push Kit提供了多种通知消息样式，您可以自定义其中内容来吸引用户，从而提高应用的日活跃用户数量。

### 普通通知

您在发送通知消息时[notification](../harmonyos-references/push-scenariozed-api-request-param.md#notification)参数中必须携带**title**与**body**字段，来设置应用收到通知消息后展示在通知中心的标题与内容。文本内容最多显示3行，超出3行以“...”截断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/Jj9kwxvYS_mun46lzcroWA/zh-cn_image_0000002712245388.png)

消息体示例：

```json
{
  "payload": {
    "notification": {
      "category": "MARKETING",
      "title": "推送服务",
      "body": "推送服务（Push Kit）是华为提供的消息推送平台，建立了从云端到终端的消息推送通道。您通过集成推送服务，可以向客户端应用实时推送消息，构筑良好的用户关系，提升用户的感知度和活跃度。",
      "clickAction": {
        "actionType": 0
      }
    }
  },
  "target": {
    "token": ["MAMzLg**********lPW"]
  },
  "pushOptions": {
    "testMessage": true
  }
}
```

### 通知角标

**说明** 

Wearable、TV不支持此通知样式。

您可以发送通知消息时携带[badge](../harmonyos-references/push-scenariozed-api-request-param.md#badge)字段来设置应用收到通知消息后以数字的形式展示角标，提醒用户查看消息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/izoqkQGXQF6gytKfTLwbNA/zh-cn_image_0000002742004337.png)

消息体示例：

```json
{
  "payload": {
    "notification": {
      "category": "MARKETING",
      "title": "通知标题",
      "body": "通知内容",
      "badge":{
        "addNum": 1,
        "setNum": 99
      },
      "clickAction": {
        "actionType": 0
      }
    }
  },
  "target": {
    "token": ["MAMzLg**********lPW"]
  },
  "pushOptions": {
    "testMessage": true
  }
}
```

**说明** 

* addNum设置后为应用角标累加数字，非应用角标实际显示数字。
* setNum设置后为应用角标实际显示数字。setNum优先级高于addNum。
* 打开应用或者点击、清理通知消息并不会清理角标数字，开发者可通过[setBadgeNumber](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagersetbadgenumber10)()方法清理角标，使用前需先[导入模块](../harmonyos-references/js-apis-notificationmanager.md#导入模块)。
* 当setBadgeNumber()方法中的badgeNumber设置为0时，可以实现清理效果。

### 通知大图标

**说明** 

Wearable不支持此通知样式。

**Push Kit禁止推送包含敏感信息的图片。**

您可以发送通知消息时携带[image](../harmonyos-references/push-scenariozed-api-request-param.md#notification)字段设置消息大图标内容，提醒用户查看消息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/koN43DE1QCabyGmkzAxxhQ/zh-cn_image_0000002712405348.png)

消息体示例：

```json5
{
  "payload": {
    "notification": {
      "category": "MARKETING",
      "title": "推送服务",
      "body": "推送服务是华为提供的消息推送平台",
      "image": "https://***.png", // 支持图片的格式为PNG、JPG、JPEG、BMP、WEBP，图片像素的总字节数不超过192KB，若超过则图片不展示。
      "clickAction": {
        "actionType": 0
      }
    }
  },
  "target": {
    "token": ["MAMzLg**********lPW"]
  },
  "pushOptions": {
    "testMessage": true
  }
}
```

### 多行文本样式

**说明** 

Wearable不支持此通知样式。

您可以发送通知消息时在[notification](../harmonyos-references/push-scenariozed-api-request-param.md#notification)中携带**inboxContent**和**style**字段设置通知消息为多行文本样式。最多可展示3行内容，每行内容无法完全展示时以“...”截断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/2r210T5oTeiBDnWomwJaHA/zh-cn_image_0000002742124297.png)

消息体示例：

```json
{
  "payload": {
    "notification": {
      "category": "MARKETING",
      "title": "推送个性化显示",
      "body": "通知内容",
      "style": 3,
      "inboxContent": [
          "1. 通知栏消息样式",
          "2. 通知栏消息提醒方式和展示方式",
          "3. 通知栏消息语言本地化"
          ],
      "clickAction": {
        "actionType": 0
      }
    }
  },
  "target": {
    "token": ["MAMzLg**********lPW"]
  },
  "pushOptions": {
    "testMessage": true
  }
}
```

**说明** 

* 多行文本样式需要设置style字段为3。
* 当您发送多条通知消息导致用户通知消息折叠时，多行文本样式在展开前显示的标题与内容取自title与body字段。
* 当用户展开多行文本消息，或仅存在一条多行文本消息时，通知中显示的标题与内容取自title与inboxContent字段。

## 开发通知消息账号校验

Push Kit提供了账号校验功能，该功能支持您根据终端设备上不同账户属性来推送消息，将通知发送给对应设备上的对应账号。

举例：华为手机上某个应用存在账号A和账号B，若当前登录的账号A切换至账号B后，发送给账号A的通知消息在到达设备后不会进行展示，以避免账号B看到账号A的消息。

**说明** 

* 当Push Token变更后，账号与应用的绑定关系自动解除。
* 绑定的应用内账号数量最大为10。

Push Kit支持华为账号和应用账号两种账号类型：

* **华为账号**

  该profileId为应用通过华为账号映射的唯一匿名标识。

  调用[bindAppProfileId](../harmonyos-references/push-pushservice.md#pushservicebindappprofileid-1)()绑定接口时机：

  + 在应用内通过华为账号授权登录后。
  + 在应用内从其他账号切换到当前华为账号后。

  调用[unbindAppProfileId](../harmonyos-references/push-pushservice.md#pushserviceunbindappprofileid-1)()解绑接口时机：

  + 在应用内登出华为账号后。

  举例： 用户选择华为账号作为应用登录账号并登录账号A成功后，调用Push Kit绑定接口[bindAppProfileId](../harmonyos-references/push-pushservice.md#pushservicebindappprofileid-1)()将账号A的profileId绑定到当前设备的应用token上。应用服务器发送通知消息时若携带该账号A的profileId，则只有当前登录的华为账号为账号A时，才会展示通知消息；若不携带profileId，则无论当前登录的华为账号是否为账号A，都正常展示通知消息。
* **应用账号**

  该profileId为应用通过自己的账号映射的唯一匿名标识。

  调用[bindAppProfileId](../harmonyos-references/push-pushservice.md#pushservicebindappprofileid-1)()绑定接口时机：

  + 在应用内登录应用账号后。
  + 在应用内从其他应用账号切换到当前应用账号后。

  调用[unbindAppProfileId](../harmonyos-references/push-pushservice.md#pushserviceunbindappprofileid-1)()解绑接口时机：

  + 在应用内登出应用账号后。

  举例： 用户成功登录应用的账号A后，调用Push Kit绑定接口[bindAppProfileId](../harmonyos-references/push-pushservice.md#pushservicebindappprofileid-1)()将账号A的profileId绑定到当前设备的应用token上。应用服务器发送通知消息时若携带账号A的profileId，则只有当前登录的应用账号为账号A时，才会展示通知消息；若不携带profileId，则无论当前登录的应用账号是否为账号A，都正常展示通知消息。

**说明** 

若在账号登出时未做[unbindAppProfileId](../harmonyos-references/push-pushservice.md#pushserviceunbindappprofileid-1)()解绑，或者在账号切换时未做[bindAppProfileId](../harmonyos-references/push-pushservice.md#pushservicebindappprofileid-1)()重新绑定，则会导致应用依然能接收到原账号的通知消息。

1. 参见指导[获取Push Token](push-get-token.md)。
2. 为确保应用可正常收到通知消息，建议应用发送通知前调用[requestEnableNotification](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10-1)()方法弹出提醒，告知用户需要允许接收通知消息。详情请参见Notification Kit-[请求通知授权](notification-enable.md)。
3. 为待绑定的账号生成一个非空唯一的profileId（不建议使用真实的账号id，推荐使用账号id自行生成对应的匿名标识，能与该账号id建立唯一映射关系即可，生成算法无限制），调用[bindAppProfileId](../harmonyos-references/push-pushservice.md#pushservicebindappprofileid-1)()方法，添加当前设备上该用户与应用的关系，代码示例：

   导入pushService模块及相关公共模块：

   ```typescript
   import { pushCommon, pushService } from '@kit.PushKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   调用bindAppProfileId方法：

   ```typescript
   const profileId: string = '111***222';
   const DOMAIN = 0x0000;

   // ...
   function bindAppProfileId(): void {
     pushService.bindAppProfileId(pushCommon.AppProfileType.PROFILE_TYPE_APPLICATION_ACCOUNT, profileId).then(() => {
       hilog.info(DOMAIN, 'testTag', 'Succeeded in binding app profile id');
     }).catch((err: BusinessError) => {
       hilog.error(DOMAIN, 'testTag', 'Failed to bind app profile id: %{public}d %{public}s', err.code, err.message);
     });
   }
   ```
4. 建议您将Push Token和生成的profileId上报到应用服务端，便于应用服务端向终端推送消息。
5. 应用服务端调用REST API推送通知消息，通知消息示例如下：

   ```json5
   // Request URL
   POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

   // Request Header
   Content-Type: application/json
   Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   push-type: 0

   // Request Body
   {
     "payload": {
       "notification": {
         "category": "MARKETING",
         "title": "普通通知标题",
         "body": "普通通知内容",
         "profileId": "111***222",
         "clickAction": {
           "actionType": 0
         }
       }
     },
     "target": {
       "token": ["MAMzLg**********lPW"]
     },
     "pushOptions": {
       "testMessage": true
     }
   }
   ```

   * [projectId]：项目ID，登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
   * Authorization：JWT格式字符串，可参见[Authorization](../harmonyos-references/push-scenariozed-api-request-struct.md#request-header)获取。
   * push-type：0表示通知消息场景。
   * actionType：0表示点击消息打开应用首页。
   * token：Push Token，可参见[获取Push Token](push-get-token.md)获取。
   * profileId：应用内账号id匿名标识。详情请参见[profileId](../harmonyos-references/push-scenariozed-api-request-param.md#notification)。

   消息发送成功后，Push Kit会先校验绑定账号时的[AppProfileType](../harmonyos-references/push-pushcommon.md#appprofiletype)（华为账号或应用账号）：

   * 若绑定华为账号则先校验下发消息中携带的profileId和之前应用绑定的profileId是否一致，再校验当前登录的华为账号和绑定时登录的分布式账号是否一致，若全部满足则展示消息，否则不展示消息。
   * 若绑定应用账号则校验下发消息中携带的profileId和之前应用绑定的profileId是否一致，若满足则展示消息，否则不展示消息。

     **说明** 

     场景化消息[请求体](../harmonyos-references/push-scenariozed-api-request-struct.md)中，接口URL版本为V3（https://push-api.cloud.huawei.com/v3/[projectId]/messages:send）时，仅支持给HarmonyOS Next/5.x及之后的系统版本推送通知；接口URL版本为V2（https://push-api.cloud.huawei.com/v2/[projectId]/messages:send）时，仅支持给HarmonyOS 3.x/4.x的系统版本推送通知。

## 应用在前台时处理通知消息

为实现应用在后台时展示通知消息，在前台时只接收通知消息并自行完成业务处理，需要服务端和客户端协同配置，具体步骤可以参考以下：

1. 服务端调用REST API推送通知消息，消息体中携带[foregroundShow](../harmonyos-references/push-scenariozed-api-request-param.md#notification)字段，并且**设置为false（默认为true，表示前后台都展示）** ，则应用在前台时不会展示通知消息。

   ```json5
   {
     "payload": {
       "notification": {
         "category": "MARKETING",
         "title": "普通通知标题",
         "body": "普通通知内容",
         "clickAction": {
           "actionType": 0
         },
         "foregroundShow": false // 设置为false则应用在前台时不会展示通知消息
       }
     },
     "target": {
       "token": ["MAMzLg**********lPW"]
     },
     "pushOptions": {
       "testMessage": true
     }
   }
   ```
2. 在客户端项目模块的**src/main/module.json5**文件的对应Ability配置中（以PushMessageAbility为例），skills标签的actions属性内容配置为**action.ohos.push.listener**（**项目中有且只能有一个ability定义该action**）。

   ```json5
   {
     "name": "PushMessageAbility",
     "srcEntry": "./ets/abilities/PushMessageAbility.ets",
     "description": "$string:PushMessageAbility_desc",
     "icon": "$media:layered_image",
     "label": "$string:PushMessageAbility_label",
     "startWindowIcon": "$media:startIcon",
     "startWindowBackground": "$color:start_window_background",
     "launchType": "singleton",
     "exported": false,
     "skills": [
       // 保持现有skill对象不变
       {
         "actions": [
           "com.app.action"
         ]
       },
       // 新增一个独立的skill对象，配置actions参数
       {
         "actions": [
           "action.ohos.push.listener"
         ]
       }
     ]
   // ...
   }
   ```
3. 在客户端项目中，已经通过步骤2配置了actions属性内容的UIAbility类的onCreate()中（以PushMessageAbility为例），通过[receiveMessage](../harmonyos-references/push-pushservice.md#pushservicereceivemessage)()方法传入[PushType](../harmonyos-references/push-pushservice.md#pushservicepushtype)为"DEFAULT"获取通知消息，用于应用在前台时接收通知消息，示例代码如下：

   导入pushService模块及相关公共模块：

   ```typescript
   import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { pushService } from '@kit.PushKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```

   调用receiveMessage接口接收Push场景化消息：

   ```typescript
   const DOMAIN = 0x0000;

   export default class PushMessageAbility extends UIAbility {
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       // ...
       try {
         // receiveMessage中的参数固定为DEFAULT
         pushService.receiveMessage('DEFAULT', this, (payload) => {
           hilog.info(DOMAIN, 'testTag', '%{public}s', 'Receive message for DEFAULT type.');

           try {
             // 获取服务端传递的数据
             const data: string = payload?.data;
             // TODO：业务自行处理
             hilog.info(DOMAIN, 'testTag', 'Succeeded in getting notification,data=%{public}s',
               JSON.stringify(JSON.parse(data)?.notification));
           } catch (err) {
             const e: BusinessError = err as BusinessError;
             hilog.error(DOMAIN, 'testTag', 'Failed to process data: %{public}d %{public}s.', e.code, e.message);
           }
         });
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Succeeded in registering default message.');
       } catch (err) {
         const e: BusinessError = err as BusinessError;
         hilog.error(DOMAIN, 'testTag', 'Failed to register default message: %{public}d %{public}s', e.code, e.message);
       }
       // ...
     }
   }
   ```

## 通知消息自定义铃声实现

当用户终端收到通知消息时，通知提示会播放系统默认通知铃声。如需实现自定义铃声功能（category取值为MARKETING不支持该功能），消息需要携带[sound](../harmonyos-references/push-scenariozed-api-request-param.md#notification)字段。此功能需要服务端和客户端协同配置，具体步骤可以参考以下：

1. 将自定义铃声文件放在**客户端**工程中/resources/rawfile路径下（例如设置为**alert.mp3**，对应本地的 **/resources/rawfile/alert.mp3**文件），重新编译安装应用程序包。
2. **服务端**调用REST API推送通知消息，消息体中携带**sound**字段。

   ```json5
   // Request URL
   POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

   // Request Header
   Content-Type: application/json
   Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   push-type: 0

   // Request Body
   {
     "payload": {
       "notification": {
         "category": "TRAVEL", // 替换为实际消息类型
         "title": "普通通知标题",
         "body": "普通通知内容",
         "clickAction": {
           "actionType": 0
         },
         "notifyId": 12345,
         "sound": "alert.mp3", // category取值为MARKETING时，不支持该功能
         "soundDuration": 10 // 请求同时携带sound字段时才会生效
       }
     },
     "target": {
       "token": ["MAMzLg**********lPW"]
     },
     "pushOptions": {
      "testMessage": true,
       "ttl": 86400
     }
   }
   ```

   * sound：（选填）自定义消息通知铃声。此处设置的铃声文件必须放在应用的/resources/rawfile路径下。例如设置为**alert.mp3**，对应应用本地的 **/resources/rawfile/alert.mp3**文件。详情请见[sound](../harmonyos-references/push-scenariozed-api-request-param.md#notification)。category取值为MARKETING时，不支持该功能。
   * soundDuration：（选填）自定义消息通知铃声时长，仅支持数字，单位：s，取值范围 [1, 60]，在请求同时携带**sound字段**时才会生效。sound字段传入的自定义消息通知铃声会播放至soundDuration字段值后停止，若自定义消息通知铃声对应的时长不足soundDuration字段值则会循环播放，在达到soundDuration字段值后停止。详情请参见[soundDuration](../harmonyos-references/push-scenariozed-api-request-param.md#notification)。
