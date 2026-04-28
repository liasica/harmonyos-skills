---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-kit-introduction
title: Push Kit简介
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > Push Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:098cd1e26239c4b5bda667ebf339dfa571559ce6f8539d1f477010c9cf795e03
---

Push Kit（推送服务）是华为提供的消息推送平台，建立了从云端到终端的消息推送通道。所有HarmonyOS应用可通过集成Push Kit，实现向应用实时推送消息，使消息易见，构筑良好的用户关系，提升用户的感知度和活跃度。

## 快速入门

请参考[使用入门](push-gettingstart.md)章节快速了解接入Push Kit（推送服务）的必要步骤。

## 产品优势

* **稳定的消息发送通道**

  Push Kit通过提供系统级长连接，实现即使应用进程不存在，也能实时推送消息。
* **丰富的消息呈现样式**

  支持文本样式、通知大图标样式、多行文本样式、角标样式等多种消息展示方式，满足您多样化、个性化的消息发送需求。
* **灵活的场景化消息**

  开发者可以根据实际场景灵活接入场景化消息。如通过应用内通话消息实现音视频通话，通过语音播报消息实现语音播报业务处理，通过后台消息实现配置更新等。

## 推送消息提示场景

推送消息指的是应用**通过Push Kit发送的**，在华为终端设备上显示的通知消息。显示场景主要包括通知中心、锁屏、横幅、桌面图标角标与通知图标。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/Obcq9K0HSES_6qCtflq06w/zh-cn_image_0000002552959106.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T235026Z&HW-CC-Expire=86400&HW-CC-Sign=3B20C230392329939DC613AA92DB3A2A7A8DF2B9DB1BDE3D3071A0C5798DF715)

有关各场景的详细说明请参见[通知提示场景](../design-guides/system-features-notification-0000001793074217.md#section162699204401)。

## 推送消息类型

Push Kit支持以下消息类型：

| 消息类型 | 说明 |
| --- | --- |
| [通知消息](push-send-alert.md) | 通知消息由Push Kit直接下发，在终端设备的通知中心、锁屏、横幅等展示，用户点击后拉起应用。  您可以[设置通知消息样式](push-send-alert.md#设置通知消息样式)来吸引用户。  常见场景：行程提醒、账号动态等。 |
| [语音播报消息](push-send-extend-noti.md#开发步骤) | 当用户终端收到您发送的语音播报消息后，Push Kit会拉起应用的子进程，您可以在子进程中自行处理业务。  常见场景：语音播报。 |
| [卡片刷新消息](push-form-update.md) | 通过卡片刷新服务，在合适场景向用户即时推送卡片内容，提升用户的感知度和活跃度。  常见场景：打车出行、快递动态等。 |
| [后台消息](push-background.md) | 终端设备接收到后台消息后，如果应用进程在前台则将消息内容传给应用；如果应用进程不在前台则缓存消息，等待应用启动后再传给应用。  常见场景：用于告知应用更新配置参数。 |
| [实况窗消息](push-update-liveview.md) | 应用服务端向Push Kit服务端发送创建或更新实况窗的请求，创建实况窗，或更新实况窗内容。  常见场景：赛事比分更新，出行打车状态更新等。 |
| [应用内通话消息](push-voip.md) | 支持应用实现网络音视频通话的能力。  常见场景：网络音视频通话。 |

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/fvxYtZmvQwaXQQygynhwhA/zh-cn_image_0000002583479107.png?HW-CC-KV=V1&HW-CC-Date=20260427T235026Z&HW-CC-Expire=86400&HW-CC-Sign=C217AE8223BC22289FC4E69D183933A64C0EF13518AA029756EB4DBD7C155C1D)

使用Push Kit的主要业务流程如下：

1. 应用调用Push Kit，获取Push Token。
2. 应用成功获取Token后，建议及时上报Token等信息至应用服务端。
3. 应用服务端向华为Push Kit服务端（Push Cloud）发送推送消息请求。应用的通知开关默认关闭，发送请求前，请先请求通知授权，详情请参见[请求通知授权](notification-enable.md)。
4. Push Kit服务端下发消息到Push Kit。
5. Push Kit进行消息处理。

## 约束和限制

### 影响送达率的因素说明

Push Kit致力于提供安全可靠的系统级消息发送通道，保障消息成功送达。影响消息送达率的因素如下：

* 终端设备是否在线。如果设备离线，Push Kit会缓存消息，待设备上线后，再将消息推送给设备。
* 终端设备上应用是否被卸载。
* 终端设备的网络状况是否稳定。
* 终端设备的安全控制策略。

### 推送消息的及时性

在终端设备网络条件良好且不拥堵情况下，Push Kit将使用智能推送策略以减少推送消息的时延。

说明

为降低对用户的打扰，系统会学习用户的行为习惯，预测用户的睡眠时间，在用户睡眠期间实施消息管控。在此期间推送服务将暂时缓存该时间段内收到的消息（应用内通话或category=VoIP的消息除外）。用户结束睡眠后，推送服务会将消息重新投递到对应设备。

### 推送消息长度与数量限制

* 消息体最大不能超过4096Bytes（不包括Token），若超过请求会返回错误码[80300008](../harmonyos-references/push-scenariozed-api-response.md#section80300008-消息体大小超过4096bytes不包括push-token)。
* 每个项目每日全网最多可推送1000条测试消息，正式消息区分场景有不同的配额，参考[消息频控](../harmonyos-references/push-msg-freq-control.md)说明。

### 网络受限说明

如果终端设备连接的网络配置了防火墙或处于受限的网络下，将会影响消息的送达率，请检查以下端口号是否被禁用。

端口号：

* 5223
* 443

说明

终端设备连接的推送服务器的IP是动态分配的，无法通过配置IP白名单方式放行。建议连接不受限的网络或放通以上端口。

### 支持的国家/地区

Push Kit当前[支持的设备](push-kit-introduction.md#支持的设备)中Wearable设备支持的国家请参见[支持的国家/地区](push-country.md)，其他设备仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

### 支持的设备

推送服务能力支持Phone、Tablet、PC/2in1、Wearable、TV设备。

### 云真机说明

Push Kit不支持云真机调试。

## 模拟器支持情况

Push Kit支持模拟器，但与真机存在部分能力差异，具体差异如下。

* 通用差异：请参见“[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)”。
* 模拟器不支持推送语音播报消息、推送实况窗消息、推送应用内通话消息。

## 与相关Kit的关系

* Push Kit建立了从云端到终端的消息推送通道，支持开发者从云侧实时推送消息。如果开发者希望从本地推送通知，可通过[Notification Kit（用户通知服务）](notification-overview.md)创建本地通知。
* 开发者[推送卡片刷新消息](push-form-update.md)时，需要通过[Form Kit（卡片开发服务）](formkit-overview.md)提前创建应用的服务卡片。
* 开发者[推送实况窗更新消息](push-update-liveview.md)时，需要通过[Live View Kit（实况窗服务）](liveview-introduction.md)提前创建本地实况窗。
* 开发者[推送应用内通话消息](push-voip.md)时，通过[Call Service Kit（通话服务）](call-introduction.md)管理应用通话能力。

## 示例代码

Push Kit（推送服务）示例代码，请参考[示例代码](https://gitcode.com/harmonyos_samples/push-kit-sample-code-clientdemo-arkts)。
