---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-faq-2
title: 打开应用功能跳转第三方应用失败
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > Scenario Fusion Kit常见问题 > 打开应用功能跳转第三方应用失败
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:49+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e61a8bee868aae6dc47af0c953198b813fdaf477774c508c2793df78b8704b63
---

**现象描述**

日志报错示例：

```
1. startAbility failed, code is 16000018, message is The application is not allow jumping to other applications when api version is above 11.
```

**解决措施**

需要执行命令手动开启限制开关。

```
1. hdc shell param set persist.sys.abilityms.support.start_other_app true
```
