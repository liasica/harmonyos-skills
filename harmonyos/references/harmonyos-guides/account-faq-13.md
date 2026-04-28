---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-13
title: 未成年人模式开启后USB断连如何解决
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 未成年人模式开启后USB断连如何解决
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9f139da62450c35464a1c61551e25d2b68f1c8b213d05d8207dca20117e8e889
---

开发者可以进入设置-系统-开发者选项，点击USB调试开关，会校验健康使用设备密码，校验成功后可解除开发者调试模式限制。

如开发者重新开启USB调试开关后，发现DevEco Studio工具上hilog日志未恢复到断连之前，请执行“hdc shell hilog -G 16M”来扩大hilog日志缓存区，若hilog日志仍无法完全展示，可取出hilog日志本地查看。更多命令请参见[hilog](hilog.md)。
