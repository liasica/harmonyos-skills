---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/push-kit-faq-0001
title: Push Kit推送服务接入常见错误码和解决方案
breadcrumb: FAQ > 应用服务开发 > 消息推送服务（Push Kit） > 常见问题 > Push Kit推送服务接入常见错误码和解决方案
category: harmonyos-faqs
scraped_at: 2026-10-23T07:14:32+08:00
doc_updated_at: 2026-10-22
content_hash: sha256:587b6ac0d3475d434965bddf8823a2ad84b27bab48e8d3e352619486be3056e0
---

**Q：消息推送时产生10009000xx、80xxxxxx等错误码，如何排查？**

**A**：在消息推送对接过程中，用于定位的错误码（状态码）主要来自以下三种：

1. [REST API](../harmonyos-references/push-rest-api.md)云侧接口[业务响应码](../harmonyos-references/push-scenariozed-api-response.md#section204526160327)。
2. Push Kit端侧[ArkTS API错误码](../harmonyos-references/push-error-code.md)与[通用错误码](../harmonyos-references/errorcode-universal.md)。
3. 消息[回执状态码](../harmonyos-guides/push-msg-receipt.md#section19100519195717)。

进行问题排查时首先排查云侧REST API接口是否正常下发。然后再排查端侧响应是否正常，是否产生ArkTS API错误码。以下按场景列举几个常见错误码及解决方式：

场景一：REST API业务响应码错误。

* [80200001 认证错误](../harmonyos-references/push-scenariozed-api-response.md#section203123193470)，常见于请求头中Authorization参数鉴权失败，建议排查方向：
  1. 确认用于申请JWT Token的[服务账号密钥](../app/hdc-credential-0000002723016406.md#section3554194116341)凭证中project\_id、[推送请求接口URL](../harmonyos-references/push-scenariozed-api-request-struct.md#section495142212220)中projectId与应用所属项目ID三者一致。
  2. 请确认生成JWT Token的正确性后再推送消息，详情参见[基于服务账号生成鉴权令牌](../harmonyos-guides/push-jwt-token.md)。
  3. HarmonyOS 5及以上系统版本使用V3版本的REST API下发消息，鉴权方式只支持JWT Token令牌；不支持Access Token的鉴权方式。
* [80300002 当前应用无权限下发推送消息](../harmonyos-references/push-scenariozed-api-response.md#section3227145145010)。请确保当前应用所属的项目已开通了推送服务，并基于该项目重新生成鉴权令牌，并重新尝试推送消息。建议排查方向：
  1. 是否已开通推送服务。
  2. 推送请求URL中的projectId与当前应用所属的项目是否一致。
* [80300007 所有Token都是无效的](../harmonyos-references/push-scenariozed-api-response.md#section030511015314)，请根据响应消息中的提示，按关键词排查问题。例如，下面日志中的关键词为noPushTypeRight，表示没有发送对应push-type场景的权益，需要申请对应场景的权益。其他问题情况可参考[80300007](../harmonyos-references/push-scenariozed-api-response.md#section030511015314)相关详细解析。

  **须知** 

  code=80300007,

  msg={"failure":1,"illegalTokens":{"noPushTypeRight":["MAM0Ku.........jixTSG"]}},

  requestId=17xxxxxxxxxxxx001,
* 更多参考[ArkTS API错误码](../harmonyos-references/push-error-code.md)与[通用错误码](../harmonyos-references/errorcode-universal.md)说明。

场景二：Push Kit端侧ArkTS API错误码：

* [1000900010 APP身份验证失败](../harmonyos-references/push-error-code.md#section3835124673016)，常见于[pushService.getToken](../harmonyos-references/push-pushservice.md#section163204312464)失败的场景：
  1. 确认当前HarmonyOS应用已经开启推送服务，生成Profile证书打包，且应用签名正确，详情参见[开通推送服务](../harmonyos-guides/push-config-setting.md#section13206419341)步骤5、步骤6。
  2. 如果生成Profile证书后，再开通推送服务。需要重新更新Profile文件，在[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/#/home/)的“开发者管理 > APP ID > API管理”中启用“推送服务”开启后重新申请Profile文件。同时应用需要重新签名，
  3. 保证设备网络环境通畅。
  4. 建议使用真机进行调试，不要使用云真机调试。
* [1000900009 推送服务内部错误](../harmonyos-references/push-error-code.md#section558801012107)：
  1. 保证设备网络环境通畅。
  2. 建议使用真机进行调试。
  3. 重启设备。
* 更多参考[REST API](../harmonyos-references/push-rest-api.md)云侧接口[业务响应码](../harmonyos-references/push-scenariozed-api-response.md#section204526160327)。
