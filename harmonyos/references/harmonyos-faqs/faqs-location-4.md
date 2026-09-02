---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-4
title: 开启定位后没有定位授权的弹窗
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 开启定位后没有定位授权的弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cd40e10f7c8ba7b610c809979e839f3bdcee86c337ba6d2db6c301b4b55cc7e8
---

## 问题现象

应用在启用定位功能时，未弹出请求授权的提示，导致定位未能成功。

## 背景知识

应用在使用[Location Kit](../harmonyos-guides/location-kit.md)系统能力前，需要检查是否已经获取用户授权访问设备位置信息。如未获得授权，可以向用户申请需要的位置权限。系统提供的定位权限有：

* ohos.permission.LOCATION：用于获取精准位置，精准度在米级别。
* ohos.permission.APPROXIMATELY\_LOCATION：用于获取模糊位置，精确度为5公里。
* ohos.permission.LOCATION\_IN\_BACKGROUND：用于应用切换到后台仍然需要获取定位信息的场景。

## 问题定位

1. 查看[module.json5](../harmonyos-guides/module-configuration-file.md)配置文件中是否已经申请了ohos.permission.LOCATION定位权限。也可以通过查看对应时间点的hilog日志，在用户提供的日志中搜索权限ohos.permission.LOCATION，返回结果flag=0表示权限请求的结果为未授权或权限不存在。

   ```txt
   [GetPermissionFlag:386]GetPermissionFlag called, tokenID: xxxxxxxxx, permissionName: ohos.permission.LOCATION
   [GetPermissionFlag:312]Result from server()error=0, flag=0)
   ```
2. 申请了权限之后需要查看[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)方法中是否向用户申请授权。

## 分析结论

1. 未配置定位权限。
2. 未向用户申请授权，如果没有授权用户收不到定位授权的弹窗无法获取定位信息。

## 修改建议

1. 在module.json5中配置ohos.permission.LOCATION定位权限，可参考：[申请位置权限开发指导](../harmonyos-guides/location-permission-guidelines.md)。
2. 使用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)方法向用户申请授权。
