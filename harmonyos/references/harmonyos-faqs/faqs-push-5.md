---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-push-5
title: 设备收不到服务端手动推送的离线消息
breadcrumb: FAQ > 应用服务开发 > 消息推送服务（Push Kit） > 设备收不到服务端手动推送的离线消息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:d1ff9c112ab35c78dc8313086abec5e5a0aaafa46d9f4516e4de3e29a74ec935
---

## 问题现象

服务端推送离线消息，手机端应用进程不存在时，消息收不到，启动应用，进程存在，依旧收不到消息，该问题如何定位处理？

场景：

* 推送时选择的category选择是MARKETING。
* Token已获取。

## 背景知识

* 离线推送：离线推送是指如果设备离线，Push Kit会缓存消息，待设备上线后，再将消息推送给设备，具体可参考：[Push Kit简介](../harmonyos-guides/push-kit-introduction.md)。
* 离线是指设备处于离线状态，即关机或者无网络状态，和APP是否处于进程中没有关联。如果设备有网络连接，无论APP是否处于进程中，都可以收到推送消息。如果设备已经处于离线状态，开发者可以通过[请求体](../harmonyos-references/push-scenariozed-api-request-param.md)中ttl参数控制消息在Push服务器缓存的时间，在消息缓存时间内用户设备上线，消息会下发，超过缓存时间后消息会丢弃。

## 问题定位

按以下步骤进行排查：

* [通知授权](../harmonyos-guides/notification-enable.md)：

  可通过requestEnableNotification的错误码判断用户是否授权。若返回的错误码为1600004，即为拒绝授权。示例代码参考：[开发步骤](../harmonyos-guides/notification-enable.md#开发步骤)。
* [消息类型和配置](../harmonyos-guides/push-send-alert.md)：

  确认发送的消息类型和配置是否正确。例如，需要设置合适的category和push-type来确保消息被正确处理。同时，检查[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)是否被设置为true，这是因为测试消息有特定的发送限制：

  当testMessage为true时，单个项目最多可推送1000条测试消息，每次推送携带Token数不超过10个。推送授权订阅消息与卡片刷新消息时，每次仅能携带一个Token。

  若未申请通知消息自分类权益，则推送的通知消息默认为资讯营销类（category取值为MARKETING）消息；若仅需发送资讯营销类消息，则无需申请通知消息自分类权益。
* [Push Token](../harmonyos-guides/push-get-token.md)：

  确认应用已经成功获取并上传了Push Token。

  Push Token标识了每台设备上每个应用，开发者调用[getToken()](../harmonyos-references/push-pushservice.md#pushservicegettoken)接口向Push Kit服务端请求Push Token，获取到之后使用Push Token来推送消息。

  Push Token一般情况不会变化，仅下列场景Push Token会发生变化：

  + 卸载应用后重新安装。
  + 设备恢复出厂设置。
  + 应用显式调用[deleteToken()](../harmonyos-references/push-pushservice.md#pushservicedeletetoken)接口后重新调用getToken()接口。
  + 应用显式调用[deleteAAID()](../harmonyos-references/push-aaid-api.md#aaiddeleteaaid)接口后重新调用getToken()接口。
  + 将设备（仅涉及Wearable设备）拿到海外其他国家或者地区后，系统会更新设备的Token。更新后的Token通过pushService.on('tokenUpdate')接口的回调返回。

  因此，建议在应用启动时调用getToken()接口，若设备的Push Token发生变化，及时上报到应用服务器更新Push Token。

  示例代码参考：[Push Token更新回调](../harmonyos-guides/push-get-token.md#push-token更新回调)。
* [点击消息动作](../harmonyos-guides/push-send-alert.md#点击消息动作)module.json5文件的配置问题：

  module.json5文件中的skills标签下可以同时存在多个skill对象，每个对象对应一种能力。如果需要同时设置推送消息跳转能力和其他跳转能力（如NFC跳转、浏览器跳转等），需要在skills数组中创建不同的skill对象，分别映射对应的能力。一个skill中不建议配置多个action，否则会导致无法匹配预期场景。

## 分析结论

module.json5文件的配置问题，需要在skills数组中创建不同的skill对象。

## 修改建议

* 如果要同时设置推送消息跳转能力和其他跳转能力（如NFC跳转、浏览器跳转等），需要在skills数组中创建不同的skill对象，分别映射对应的能力。
* 一个skill中不建议配置多个action，否则会导致无法匹配预期场景。

## 常见FAQ

Q：通过pushService.getToken()获取Push Token，为什么打印获取到的Push Token内容为[object Promise]？

A：getToken()为Promise异步接口，需要使用异步回调方法获取返回值，示例代码参考：[获取Push Token](../harmonyos-guides/push-get-token.md#获取push-token-1)。
