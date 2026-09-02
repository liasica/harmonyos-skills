---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-frequently-asked-questions-three
title: 使用意图框架调试助手Agent进行联调时，小艺拉起应用后，出现闪退情况，应该如何处理？
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 常见问题 > 使用意图框架调试助手Agent进行联调时，小艺拉起应用后，出现闪退情况，应该如何处理？
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:102c1d9cc40d71db79a677754b7d4739e4b4afc34ebe4f0c0c10af9b0aaa025d
---

出现此现象时，优先排查接入意图框架的代码是否被混淆。接入意图框架的代码文件不可被混淆。关于混淆的详细内容请参考[ArkGuard混淆实践指导](source-obfuscation-apply-code.md)。若排查后问题依然存在，请检查应用的业务代码是否有其他异常引发应用闪退。
