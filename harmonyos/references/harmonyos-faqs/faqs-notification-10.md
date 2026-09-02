---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-10
title: 应用通知点击跳转异常
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 应用通知点击跳转异常
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:30+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:8aed07e3f96673acfb26933e2533943279d2df032c852ed62d4467252e8ebe35
---

## 问题现象

当用户点击应用推送的通知时，目标页面未能成功跳转，具体表现为：

* 无响应：点击通知后屏幕无任何反馈。
* 跳转异常：虽然页面跳转，但跳转到非预期的位置（如跳转首页而非目标详情页）。

## 背景知识

* [requestEnableNotification()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10-1)：为确保应用可正常收到消息，应用发送通知前调用该方法弹出提醒，告知用户需要允许接收通知消息。详情请参见Notification Kit-[请求通知授权](../harmonyos-guides/notification-enable.md)。
* [信息传递载体Want](../harmonyos-guides/want.md)：[Want](../harmonyos-references/js-apis-app-ability-want.md)是一种对象，用于在应用组件之间传递信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/xAviCcfBQgCCY2yGYQXpZA/zh-cn_image_0000002628554614.png "点击放大")
* [Notification Kit（用户通知服务）](../harmonyos-guides/notification-kit.md)：提供本地通知发布通道，开发者可借助Notification Kit将应用产生的通知直接在客户端本地推送给用户（[相关API参考](../harmonyos-references/notification-api.md)）。
  + [为通知添加行为意图](../harmonyos-guides/notification-with-wantagent.md)：当发布通知时，如果期望用户可以通过点击通知栏拉起目标应用组件或发布公共事件，可以通过[Ability Kit（程序框架服务）](../harmonyos-guides/abilitykit-overview.md)申请[WantAgent](../harmonyos-references/js-apis-app-ability-wantagent.md)封装至通知消息中。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/DQ_QGdBdQHa8HpImFwQuxg/zh-cn_image_0000002658913941.png "点击放大")
* [Push Kit（推送服务）](../harmonyos-guides/push-kit-guide.md)：华为提供的消息推送平台，建立了从云端到终端的消息推送通道。您通过集成推送服务，可以向客户端应用实时推送消息（[HarmonyOS应用推送服务开发](../HMSCore-Guides/harmony-java-quickstart-0000001153706156.md)）。
  + [点击消息动作](../harmonyos-guides/push-send-alert.md#点击消息动作)：云侧发送消息时，[clickAction](../harmonyos-references/push-scenariozed-api-request-param.md#clickaction)中携带data字段并设置**actionType**字段。

    **actionType**：点击消息动作，0表示点击消息后进入首页，1表示点击消息后进入应用内页。当本字段设置为1时，uri和action至少填写一个，若都填写优先寻找与action匹配的应用页面。

    **action**：表示能够接收Want的action值的集合，取值可以自定义。

    **uri**：表示与Want中uris相匹配的集合，uris规则请参见[skills标签](../harmonyos-guides/module-configuration-file.md#skills标签)。

    **data**：点击消息时携带的JSON格式的数据。
  + [点击消息进入应用首页](../harmonyos-guides/push-send-alert.md#点击消息进入应用首页)：项目模块级别下的src/main/module.json5中的[skills标签](../harmonyos-guides/module-configuration-file.md#skills标签)配置，其中用于标识应用首页的skill（即配置了"entity.system.home"和"action.system.home"的skill）中不配置uris。
  + [点击消息进入应用内页](../harmonyos-guides/push-send-alert.md#点击消息进入应用内页)：项目模块级别下的src/main/module.json5中设置目标Ability中skills标签的actions或uris值，两种方式如下：

    **须知** 

    方式一：在skills标签中新增一个独立的skill对象，配置actions参数用于点击消息进入应用内页。

    方式二：在skills标签中新增一个独立的skill对象，配置uris参数用于点击消息进入应用内页（必须同时配置actions参数和uris参数，actions参数为空）。

## 问题定位

1. 查看对应通知的实现原理，可结合消息内容和通知触发方式初步判断是本地通知（Notification）还是云侧推送通知（Push）。
2. 由Notification实现的通知，可根据有无[notificationManager.publish](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerpublish)（发布通知）来确定。再检查构造的[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md)对象是否有[Ability Kit（程序框架服务）](../harmonyos-guides/abilitykit-overview.md)申请的[WantAgent](../harmonyos-references/js-apis-app-ability-wantagent.md)封装至通知消息中，为通知添加行为意图。同时检查WantAgent创建的[WantAgentInfo](../harmonyos-references/js-apis-inner-wantagent-wantagentinfo.md)信息是否正确。
3. 由云侧Push实现的通知，可根据有无[获取Push Token](../harmonyos-guides/push-get-token.md)的行为（[pushService.getToken](../harmonyos-references/push-pushservice.md#pushservicegettoken)）来确定。再检查项目模块级别下的src/main/module.json5中的[skills标签](../harmonyos-guides/module-configuration-file.md#skills标签)配置是否正确，也可以查看是否有应用服务端调用Push Kit服务端的REST API推送的Request Body日志打印（关键词"payload"），并检查其中clickAction信息。

## 分析结论

### 场景一

应用通知是通过[Notification Kit（用户通知服务）](../harmonyos-guides/notification-kit.md)实现的，由于未配置WantAgent或创建WantAgentInfo信息不正确导致跳转异常。

### 场景二

应用通知是通过[Push Kit（推送服务）](../harmonyos-guides/push-kit-guide.md)实现的，由于云侧推送的消息中[clickAction](../harmonyos-references/push-scenariozed-api-request-param.md#clickaction)中携带data字段和actionType字段设置不正确或在module.json5中的[skills标签](../harmonyos-guides/module-configuration-file.md#skills标签)配置不正确导致跳转异常。

## 修改建议

### 场景一

Notification本地消息实现点击跳转，详情请参考[开发步骤](../harmonyos-guides/notification-with-wantagent.md#开发步骤)。

1. 创建[WantAgentInfo](../harmonyos-references/js-apis-inner-wantagent-wantagentinfo.md)信息。
   * 创建拉起[UIAbility](../harmonyos-guides/uiability.md)的WantAgent的WantAgentInfo信息。
   * 创建发布[公共事件](../harmonyos-guides/common-event-overview.md)的WantAgent的WantAgentInfo信息。
2. 调用[getWantAgent()](../harmonyos-references/js-apis-app-ability-wantagent.md#wantagentgetwantagent)方法进行创建WantAgent。
3. 构造[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md)对象，并发布WantAgent通知。

### 场景二

Push推送消息实现点击跳转，以进入应用内页并传递数据为例，详情请参考[点击消息进入应用内页](../harmonyos-guides/push-send-alert.md#点击消息进入应用内页)。

1. 在项目模块级别下的**src/main/module.json5**中设置待跳转Ability的[skills标签](../harmonyos-guides/module-configuration-file.md#skills标签)中的actions或uris值，两种方式如下：
   * 在skills标签中新增一个独立的skill对象，配置actions参数用于点击消息进入应用内页。
   * 在skills标签中新增一个独立的skill对象，配置uris参数用于点击消息进入应用内页（必须同时配置actions参数和uris参数，actions参数为空）。
2. 应用服务端调用Push Kit服务端的REST API推送通知消息时，clickAction中携带data字段并设置actionType字段为1，详情请参考[请求体参数说明](../harmonyos-references/push-scenariozed-api-request-param.md#clickaction)。
3. 在待跳转页面（以TestAbility为例）中接收消息中传递的data数据：
   * [冷启动](../harmonyos-guides/uiability-intra-device-interaction.md#目标uiability冷启动)时进入[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)生命周期回调。
   * [热启动](../harmonyos-guides/uiability-intra-device-interaction.md#目标uiability热启动)时进入[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)生命周期回调。注意：onNewWant()方法仅在单例（singleton）模式下可用。
