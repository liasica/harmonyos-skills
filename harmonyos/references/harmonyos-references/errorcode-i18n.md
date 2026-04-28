---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-i18n
title: I18n错误码
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > 错误码 > I18n错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:06:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:11f3aaea0e0eef34108ce7540df0dc1efbd0c626c490718c23ac20b9da4714d5
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 890001 参数校验错误

PhonePC/2in1TabletTVWearable

**错误信息**

Invalid parameter. Possible causes: Parameter verification failed.

**错误描述**

当接口传入非法的参数值时，系统会产生此错误码。

**可能原因**

该错误码表示参数内容校验失败，可能原因是传入参数的值无效。

**处理步骤**

检查参数的值是否合法。
