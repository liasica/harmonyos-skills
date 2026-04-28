---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-scroll
title: 滚动类组件错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:04:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5a2e33ec7f5467434157756158c8a8aa87cc49f432df2b0a3ea88468170e30e9
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 100004 控制器未绑定组件

PhonePC/2in1TabletTVWearable

**错误信息**

Controller not bound to component.

**错误描述**

控制器未绑定组件，通过控制器调用接口时，系统会产生此错误码。该错误码为string类型。

**可能原因**

控制器未绑定组件，通过控制器调用接口。

**处理步骤**

请检查控制器是否绑定了组件，或者控制器绑定的组件是否已经被释放。
