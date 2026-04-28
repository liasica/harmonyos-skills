---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-faq-1
title: 如何处理推送消息时遇到的问题
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > Push Kit常见问题 > 如何处理推送消息时遇到的问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a4f23215f991214969c6fbf91c139c56fe9f7cc3cc9bf0145fa8f736fcfd661f
---

当使用REST API接口进行消息推送时，您可能遇到一些问题，请按照如下思路进行处理：

1. 优先检查[消息推送接口](../harmonyos-references/push-scenariozed-api-request-struct.md)URL（https://push-api.cloud.huawei.com/**v3**/**[projectId]**/messages:send）是否正确。

   * 请使用v3版本的推送接口URL，不要使用v1或v2版本的推送接口URL，详情请参见[场景化消息中的请求URL版本问题](push-faq-8.md)。
   * 请检查推送接口地址中的projectId，确保与您当前应用所属的项目保持一致，若不一致请更新推送接口URL中的projectId，并重新[生成鉴权令牌](push-jwt-token.md)，应用重新[获取Push Token](push-get-token.md)，再进行消息推送。
2. 若调用消息推送接口返回了错误码，请参见[业务响应码](../harmonyos-references/push-scenariozed-api-response.md#业务响应码)进行排查。
3. 若调用消息推送接口返回成功，但设备未展示消息，请参见[“如何处理云侧推送消息成功端侧消息未展示的问题”](push-faq-2.md)进行排查。
