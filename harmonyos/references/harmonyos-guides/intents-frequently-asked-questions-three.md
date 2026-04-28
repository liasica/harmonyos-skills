---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-frequently-asked-questions-three
title: 使用意图框架调试助手Agent进行联调时，小艺拉起应用后，出现闪退情况，应该如何处理？
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 常见问题 > 使用意图框架调试助手Agent进行联调时，小艺拉起应用后，出现闪退情况，应该如何处理？
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e9ddc329bfa31e9cb6561d7e2c066c6206b48e711c61221b7063fbe8b33e88e5
---

出现此现象时，优先排查接入意图框架的代码是否被混淆。接入意图框架的代码文件不可被混淆。关于混淆的详细内容请参考[应用代码混淆](../best-practices/bpta-app-code-ob.md#section13780943192313)。若排查后问题依然存在，请检查应用的业务代码是否有其他异常引发应用闪退。
