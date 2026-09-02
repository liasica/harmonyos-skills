---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-push-11
title: HarmonyOS 3.x/4.x已接入过华为推送，HarmonyOS Next/5.x及以上版本应用如何升级适配
breadcrumb: FAQ > 应用服务开发 > 消息推送服务（Push Kit） > HarmonyOS 3.x/4.x已接入过华为推送，HarmonyOS Next/5.x及以上版本应用如何升级适配
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:805c98f7bc119b959fc387a9954b338b833aff4456e745c83fb1ae4b66ebcf0e
---

## 问题现象

HarmonyOS 3.x/4.x已接入过[推送服务（Push Kit）](../HMSCore-Guides/service-introduction-0000001050040060.md)，现在需要给HarmonyOS Next/5.x及之后的系统版本推送通知，应用需要如何升级适配。

## 背景知识

HarmonyOS 3.x/4.x应用适配HarmonyOS Next/5.x需要在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)上创建不同APP ID的应用，创建流程可参考官网[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)。

HarmonyOS Next/5.x接入[Push Kit](../harmonyos-guides/push-kit-introduction.md)，开发流程按客户端和服务端可分为以下几个步骤。

* 客户端：
  1. [开通推送服务](../harmonyos-guides/push-config-setting.md)。
  2. [申请通知消息自分类权益](../harmonyos-guides/push-apply-right.md#申请通知消息自分类权益)。
  3. [Push Token获取](../harmonyos-guides/push-get-token.md)与[场景化消息推送](../harmonyos-guides/push-scenes.md)。
* 服务端：
  1. [基于服务账号生成鉴权令牌](../harmonyos-guides/push-jwt-token.md)。
  2. [调用REST API推送场景化消息](../harmonyos-guides/push-scenes-send.md)。
  3. [开发消息回执](../harmonyos-guides/push-msg-receipt.md)。

## 解决方案

HarmonyOS Next/5.x应用升级适配Push Kit流程按客户端和服务端差异点主要在以下几个方面。

**客户端：**

* 开通推送服务：HarmonyOS 3.x/4.x与HarmonyOS Next/5.x应用在同一个项目中时，HarmonyOS 3.x/4.x应用接入Push Kit时已开通过推送服务，HarmonyOS Next/5.x应用无须再开通推送服务权益。但需要注意HarmonyOS Next/5.x应用除Wearable设备外，数据处理地固定为中国。
* 自分类权益：自分类权益以应用为维度，适配HarmonyOS Next/5.x仍需要开通对应权益。HarmonyOS Next/5.x及以上系统版本的自分类权益请[了解详情](../harmonyos-guides/push-apply-right.md#申请通知消息自分类权益)，HarmonyOS 3.x/4.x及以下系统版本的自分类权益请[了解详情](../HMSCore-Guides/message-classification-0000001149358835.md#section1076611477914)。

**服务端：**

* 基于服务账号生成的鉴权令牌：HarmonyOS Next/5.x只支持[基于服务账号生成鉴权令牌（JSON Web Token）](../harmonyos-guides/push-jwt-token.md)方式，如果之前HarmonyOS 3.x/4.x使用的是[OAuth 2.0开放鉴权（客户端模式）](../HMSCore-Guides/oauth2-0000001212610981.md#section128682386159)，需要修改鉴权生成方式。
* 调用REST API推送场景化消息：场景化消息[请求体结构](../harmonyos-references/push-scenariozed-api-request-struct.md)中，请求URL版本为V3（https://push-api.cloud.huawei.com/v3/[projectId]/messages:send）时，仅支持给HarmonyOS Next/5.x及之后的系统版本推送通知；版本为V2（https://push-api.cloud.huawei.com/v2/[projectId]/messages:send）时，仅支持给HarmonyOS 3.x/4.x的系统版本推送通知。HarmonyOS Next/5.x应用接入Push Kit时服务端开发可以参考[Push Kit服务端样例](https://gitee.com/harmonyos_samples/push-kit_-sample-code_-server-demo_-java)。
* 开发消息回执：HarmonyOS Next/5.x需要使用V2回执接口，V1接口不支持/v3/{projectId}/messages:send接口发消息回执。HarmonyOS 5及以上系统版本请查看[回执说明](../harmonyos-guides/push-msg-receipt.md)，HarmonyOS 3.x/4.x及以下系统版本请查看[回执说明](../development/HMSCore-Guides/msg-receipt-guide-0000001050040176.md)。
* AppGallery Connect在线推送通知消息：在线测试推送消息时，HarmonyOS Next/5.x应用需要选择“推送通知（V3 Beta）”页签，HarmonyOS 3.x/4.x版本应用需要选择“推送通知（V2）”页签。

## 总结

HarmonyOS 3.x/4.x与HarmonyOS Next/5.x客户端和服务端Push Kit接入均存在差异，如果您的项目之前已经基于HarmonyOS 3.x/4.x的系统接入过Push Kit，仍然需要按照HarmonyOS Next/5.x[开发流程](../harmonyos-guides/push-gettingstart.md#开发流程)重新进行开发客户端和服务端。

## 常见FAQ

Q：HarmonyOS 3.x/4.x和HarmonyOS Next/5.x使用的AppGallery Connect账号是同一个吗，Push kit接入时使用的基于服务账号生成的鉴权令牌是账号级别的还是项目级别？

A：HarmonyOS 3.x/4.x和HarmonyOS Next/5.x使用的AppGallery Connect账号可以是同一个账号，[基于服务账号生成的鉴权令牌](../harmonyos-guides/push-jwt-token.md)是项目级别的，可以在华为开发者联盟的[API Console](https://developer.huawei.com/consumer/cn/console/api/myApi)上生成。

Q：HarmonyOS 5基于服务账号生成鉴权令牌需要创建服务账号密钥，选择的项目中同时包含了HarmonyOS 3.x/4.x和HarmonyOS Next/5.x的应用是否会影响线上HarmonyOS 3.x/4.x应用正常推送？

A：创建[服务账号密钥](../start/api-0000001062522591.md#section3554194116341)不影响项目中HarmonyOS 3.x/4.x应用线上推送。

Q：在AppGallery Connect测试推送消息时提示Push Token不合法是什么原因？

A：请检查是否选择了正确的推送通知页签。HarmonyOS Next/5.x应用需要选择“推送通知（V3 Beta）”页签，HarmonyOS 3.x/4.x应用需要选择“推送通知（V2）”页签。如果应用类型与页签不匹配，会导致Push Token不合法。
