---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-51
title: 访问剪贴板控件，没有剪贴板访问记录
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 访问剪贴板控件，没有剪贴板访问记录
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:35e13e2a68b35d8766a229c28bb4353e2fb8b2e938086d58aeddefb3f5b3ce3a
---

## 问题现象

在系统设置->隐私和安全->剪贴板->访问记录，没有问题应用的剪贴板访问记录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/aILGMzRhRcOJx9wlBQ8D3g/zh-cn_image_0000002658973157.png "点击放大")

## 背景知识

* [ohos.permission.READ\_PASTEBOARD](../harmonyos-guides/restricted-permissions.md#ohospermissionread_pasteboard)：应用剪贴板权限，可允许应用读取剪贴板。
* [使用粘贴控件](../harmonyos-guides/pastebutton.md)：允许应用在用户的授权下无提示地读取剪贴板数据。

## 问题定位

hilog搜索accesstoken\_service/Permission关键字，得到有如下的日志信息：

```screen
11-10 16:09:04.497  1559  1559 I C05A01/accesstoken_service/PermissionManager: [GetPermissionFlag:386]GetPermissionFlag called, tokenID: 537306917, permissionName: ohos.permission.READ_PASTEBOARD
11-10 16:09:04.497  1559  1559 E C05A01/accesstoken_service/PermissionPolicySet: [QueryPermissionFlag:329]Invalid params!
```

由日志可知，获取ohos.permission.READ\_PASTEBOARD剪贴板权限异常。

## 分析结论

获取剪贴板权限异常导致无法对剪贴板进行访问，从而没有访问记录。

## 修改建议

1. 剪贴板属于受限开放权限，申请场景参考[ohos.permission.READ\_PASTEBOARD](../harmonyos-guides/restricted-permissions.md#ohospermissionread_pasteboard)。在满足条件的基础上，可通过[申请应用权限](../harmonyos-guides/request-app-permissions.md)获取权限，进行剪贴操作。
2. 对于其他应用，读取剪贴板优先使用[粘贴控件](../harmonyos-guides/pastebutton.md)。
