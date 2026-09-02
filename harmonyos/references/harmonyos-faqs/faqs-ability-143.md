---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-143
title: 如何判断权限状态是首次申请还是用户已拒绝
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何判断权限状态是首次申请还是用户已拒绝
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:432896f3ed6de096808f2dfc244ac08a46f5b7805cba4426b5e973650261e8f1
---

## 问题现象

通过atManager.checkAccessTokenSync获取权限的授权状态时，只有PERMISSION\_DENIED（未授权）和PERMISSION\_GRANTED（已授权）两种状态，怎么判断当前权限是否为首次申请？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/gw4ZspjZQEqL_bPklL8eGQ/zh-cn_image_0000002658868617.png "点击放大")

## 背景知识

* [abilityAccessCtrl.createAtManager](../harmonyos-references/js-apis-abilityaccessctrl.md#abilityaccessctrlcreateatmanager)：获取访问控制模块对象，访问控制管理。
* [atManager.requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)：用于UIAbility/UIExtensionAbility拉起弹框请求用户授权。

## 解决方案

可用atManager.requestPermissionsFromUser拉起弹框请求用户授权，返回类型为：[PermissionRequestResult](../harmonyos-references/js-apis-permissionrequestresult.md)，如果dialogShownResults为true，则代表为首次弹窗请求授权。

以申请ohos.permission.CAMERA为例：

```ts
export function checkPermission(context: Context) {
  const PERMISSION_ARRAY: Permissions[] = ['ohos.permission.CAMERA'];
  const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  atManager.requestPermissionsFromUser(context, PERMISSION_ARRAY).then((data) => {
    if (data.authResults[0] === 0) {
      // 已授权
      console.info('request permission success.')
      return;
    }
    if (data.dialogShownResults && data.dialogShownResults.length > 0 && data.dialogShownResults[0]) {
      // 首次权限申请
      console.info('request permission first.')
    } else {
      // 如果是未授权状态，可通过requestPermissionOnSetting拉起系统设置半模态二次授权
      atManager.requestPermissionOnSetting(context, PERMISSION_ARRAY)
        .then((data: Array<abilityAccessCtrl.GrantStatus>) => {
          console.info('data:' + JSON.stringify(data));
        })
        .catch((err: BusinessError) => {
          console.error('data:' + JSON.stringify(err));
        });
    }
  })
}
```
