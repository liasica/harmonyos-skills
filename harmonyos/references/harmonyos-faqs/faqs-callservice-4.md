---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-callservice-4
title: 企业联系人来去电信息手机号国家码匹配
breadcrumb: FAQ > 应用服务开发 > VoIP通话服务（Call Service Kit） > 企业联系人来去电信息手机号国家码匹配
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:78c2856d1079079b8c4e78b63642f9cb3c9348ed7d5b007393b6b849a5702423
---

## 问题现象

企业联系人来去电信息[onQueryCallerInfo](../harmonyos-references/callservicekit-callerinfoquery-extension-ability.md#onquerycallerinfo)回调的参数phoneNumber国家码规则无序混乱怎么解决？

## 背景知识

[onQueryCallerInfo](../harmonyos-references/callservicekit-callerinfoquery-extension-ability.md#onquerycallerinfo)回调的参数phoneNumber包含了国家码、区号、手机号、座机等内容。

* 大陆手机号返回11位数字手机号，无86或者00086，如188xxxxxxx。
* 香港手机号返回5位国家码00852，加上8位手机号，示例：0085212345678。
* 大陆座机号，返回区号加8位座机号，示例：北京01012345678。

E.164是一种国际化、无歧义的电话号码格式标准，核心是通过+号和国家代码，将号码统一为15位以内的纯数字字符串，确保全球通信系统的兼容性和正确性。在需要处理跨国电话号码的场景中，格式化至E.164是关键步骤。

## 解决方案

传给企业应用的号码是来电网络侧下发的原始号码，HarmonyOS没有做过处理，一般国际电话网络侧会自动加上国家码。应用侧在重写[onQueryCallerInfo](../harmonyos-references/callservicekit-callerinfoquery-extension-ability.md#onquerycallerinfo)方法时，可以使用[@ohos.i18n](../harmonyos-references/js-apis-i18n.md)对手机号进行格式化处理，其中国家地区使用[getSystemRegion](../harmonyos-references/js-apis-i18n.md#getsystemregion9)获取。
