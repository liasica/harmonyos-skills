---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/call-faq-1
title: 来电横幅无法拉起
breadcrumb: 指南 > 应用服务 > Call Service Kit（通话服务） > Call Service Kit常见问题 > 来电横幅无法拉起
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:07d211b5bc92cb7385674c75566e7f3a26043b1c761fd61f1a4d4b214ec4244a
---

**问题现象**

调用[voipCall.reportIncomingCall](../harmonyos-references/call-voipcall.md#voipcallreportincomingcall)上报来电信息，但来电横幅无法显示。

**解决措施**

1. 检查应用是否已开启[通知权限](notification-enable.md)。
2. 检查是否继承UIAbility，调用[pushService.receiveMessage](../harmonyos-references/push-pushservice.md#pushservicereceivemessage)并在接收后调用上报接口。
3. 来电信息中获取的callId，上报给通话服务接口的callId，二者应该保持一致。
4. 检查构造的callInfo信息是否有参数错误，如voipCallState需要是VOIP\_CALL\_STATE\_RINGING。
5. 如还未解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。
