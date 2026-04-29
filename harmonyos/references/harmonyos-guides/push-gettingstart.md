---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-gettingstart
title: 使用入门
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 使用入门
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:51+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:519eee1a486c2040e839db9b5c17197ac3cc2a2af27ecb0063744ca4525ea721
---

## 示例代码

开发者可以参考**服务端**[示例代码](https://gitcode.com/harmonyos_samples/push-kit_-sample-code_-server-demo_-java)，了解推送Push场景化消息的过程。参考**客户端**[示例代码](https://gitcode.com/harmonyos_samples/push-kit-sample-code-clientdemo-arkts)，了解生成Push Token和接收Push场景化消息的功能和流程。

## 开发流程

开发者需要按照流程来完成应用的开发工作，**以[推送通知消息](push-send-alert.md)为例**，完整的开发流程如下：

| 序号 | 步骤 | 说明 |
| --- | --- | --- |
| 1 | [开通推送服务](push-config-setting.md) | 在开发应用前，请先参考[操作步骤](push-config-setting.md#操作步骤)开通推送服务。其中**配置签名信息**时，请使用**手动签名**方式。  DevEco Studio 6.0.0 Beta5版本开始，新增[自动签名](ide-signing.md#section18815157237)方式。 |
| 2 | [申请通知消息自分类权益](push-apply-right.md#申请通知消息自分类权益) | · 请根据[通知消息分类标准](push-apply-right.md#通知消息分类标准与提醒方式)，申请对应场景化消息权益。不同类型的消息有对应的通知消息分类标准与提醒方式和[通知消息推送数量管理规则](push-apply-right.md#通知消息推送数量管理规则)。  · 若未开通权益，或开通的权益类型与[调用REST API推送场景化消息](push-scenes-send.md)时，请求体中携带的[category](../harmonyos-references/push-scenariozed-api-request-param.md#notification)字段值不一致，消息将会默认归为**资讯营销类消息**，则会受到“单个应用每日每设备推送数量为2条或5条”的[频控](push-apply-right.md#通知消息推送数量管理规则)限制。若超出限制，设备将会收不到该条消息。  · 调测阶段建议设置[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)为true，以防发送成功的消息被[频控](../harmonyos-references/push-msg-freq-control.md)，设备将会收不到该条消息。  · 若消息被频控，请参考[频控FAQ](push-faq-5.md)进行问题排查。 |
| 3 | **客户端**获取Push Token | [调用Push Kit REST API](push-jwt-token.md#调用push-kit-rest-api)时，需要设置token参数，对应的参数值参考[获取Push Token](push-get-token.md)进行获取。注意[Push Token变化的场景](push-get-token.md#场景介绍)，若设备的Push Token发生变化但服务端调用Push Kit REST API时未更新token的值，将会导致设备收不到该条消息。 |
| 4 | **客户端**请求通知授权 | 为确保应用可正常收到消息，应用发送通知前需调用[requestEnableNotification](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10-1)()方法弹出提醒，告知用户需要允许接收通知消息。示例代码参见[开发步骤](push-send-alert.md#开发步骤)中第2步。 |
| 5 | **客户端**配置skills标签 | 为确保点击消息可以正常跳转应用页面，在应用项目中完成skills标签配置，详情请参见[点击消息动作](push-send-alert.md#点击消息动作)。 |
| 6 | **服务端**基于服务账号生成鉴权令牌 | [调用Push Kit REST API](push-jwt-token.md#调用push-kit-rest-api)推送场景化消息时，请求头需设置Authorization参数，请参考[基于服务账号生成鉴权令牌](push-jwt-token.md)章节进行获取。 |
| 7 | **服务端**[调用REST API推送场景化消息](push-scenes-send.md) | 应用服务端参考HarmonyOS NEXT版本[请求体结构说明](../harmonyos-references/push-scenariozed-api-request-struct.md)、[请求体参数说明](../harmonyos-references/push-scenariozed-api-request-param.md)发送REST API请求。若请求失败请参考[响应参数](../harmonyos-references/push-scenariozed-api-response.md)进行问题排查，若请求成功但设备未收到消息请参考[FAQ](push-faq-2.md)进行问题排查。 |
| 8 | （可选）开发消息回执 | Push服务端会将消息送达状态以回执消息形式发送给您的应用回执服务端，方便您获取消息下达端侧后的状态，定位问题。详情请参考[开发消息回执](push-msg-receipt.md)。 |
| 9 | （可选）**客户端**收到并处理消息 | 通过服务端请求传参和客户端的数据获取，可以进行服务端和客户端的[数据传递](push-send-alert.md#数据传递)。 |

## （可选）其他消息类型

Push Kit支持的所有消息类型及使用场景可以参考[推送消息类型](push-kit-introduction.md#推送消息类型)。

如通过应用内通话消息实现音视频通话，通过语音播报消息实现语音播报业务处理，通过后台消息实现配置更新等。

* 部分场景化消息类型需要您申请特殊权益才能正常发送，详情请参考[场景化消息权益简介](push-apply-right.md#场景化消息权益简介)。
* 权益申请通过后，请参考对应消息类型的开发指南章节进行开发。

  说明

  如果您的项目之前已经基于HarmonyOS 3.x/4.x的系统接入过推送服务，现在需要给HarmonyOS Next/5.x及之后的系统版本推送通知，客户端和服务端仍然需要按照上述开发流程重新进行开发。
