---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-11
title: 应用申请位置信息权限为什么没有弹窗
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 应用申请位置信息权限为什么没有弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8dfd690c84f2188de3350cb9d73090d7d9948b9bc785e4fd30ce5f83eb1a2b61
---

## 可能原因

未在module.json5文件中配置相关位置权限。

## 解决措施

主要涉及三种权限：

* ohos.permission.LOCATION用于获取精准位置。
* ohos.permission.APPROXIMATELY\_LOCATION用于获取模糊位置。
* ohos.permission.LOCATION\_IN\_BACKGROUND用于后台定位的场景。

开发者根据需要在module.json5文件中配置进行声明，并获取用户明确授权方可使用，获取授权有两种方式：（1）通过[requestPermissionsFromUser接口](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)向用户弹窗以获得授权。（2）跳转到应用权限设置页面，打开开关进行授权。

## 参考链接

[申请位置权限开发指导](../harmonyos-guides/location-permission-guidelines.md)
