---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-xcomponent
title: XComponent组件错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > XComponent组件错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fc42b28ec46085ceedb8326b307dc8559a63cfc4642223e02c704a9ba978ccc0
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)。

## 103501 XComponent无效状态

**错误信息**

当前XComponent处于无效状态，方法调用失败。

**错误描述**

当前XComponent处于无效状态，方法调用失败。

**可能原因**

调用XComponent相关方法时，XComponent尚未完成初始化或持有的Surface已被销毁或释放，导致当前处于无效状态。

**处理步骤**

1. 确认XComponent已完成加载并初始化完成后再调用相关方法。
2. 检查XComponent持有的Surface是否已被销毁或释放，若已失效请重新创建XComponent实例后再调用。
