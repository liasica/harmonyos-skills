---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-43
title: 如何判断应用运行在隐私空间
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何判断应用运行在隐私空间
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:af5981cdf4cb88dd4491a747864162c437397892bd34fcaa2c00b96886b38d67
---

## 问题现象

需要判断出当前的运行环境是否在隐私空间中，在官网文档中没有找到对应API可以判断。

隐私空间：设置->隐私和安全->隐私空间。

## 解决方案

可以通过[getOsAccountType](../harmonyos-references/js-apis-osaccount.md#getosaccounttype9)来判断。回调中的OsAccountType表示当前进程所属的系统账号的账号类型。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ADMIN | 0 | 管理员账号。 |
| NORMAL | 1 | 普通账号。 |
| GUEST | 2 | 访客账号。 |
| MAINTENANCE | 512 | 维修账号。 |
| PRIVATE | 1024 | 隐私账号。 |
| END | 1025 | OsAccountType的上限值。 |

当返回1024时表示在隐私空间中运行。
