---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-permissionrequestresult
title: PermissionRequestResult
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > security > PermissionRequestResult
category: harmonyos-references
scraped_at: 2026-04-28T07:58:48+08:00
doc_updated_at: 2026-04-03
content_hash: sha256:c6a312f4a9166d14b105151db225eadfd958af451b57283c5b28d7e8ae9dc8d7
---

权限请求结果对象，在调用[requestPermissionsFromUser](js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)申请权限时返回此对象表明此次权限申请的结果。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { PermissionRequestResult } from '@kit.AbilityKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力**：以下各项对应的系统能力均为SystemCapability.Security.AccessToken

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| permissions | Array<string> | 否 | 否 | 用户传入的权限。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| authResults | Array<number> | 否 | 否 | 相应请求权限的结果：  - -1：未授权。①dialogShownResults返回为true，表示用户首次申请；②dialogShownResults返回为false，表示权限已设置，无需弹窗，需要用户在"设置"中修改。  - 0：已授权。  - 2：未授权，表示请求无效。可能原因有：①未在设置文件中声明目标权限；②权限名非法；③部分权限存在特殊申请条件，在申请对应权限时未满足其指定的条件，见[ohos.permission.LOCATION](../harmonyos-guides/permissions-for-all-user.md#ohospermissionlocation)与[ohos.permission.APPROXIMATELY\_LOCATION](../harmonyos-guides/permissions-for-all-user.md#ohospermissionapproximately_location)。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| dialogShownResults12+ | Array<boolean> | 否 | 是 | 此权限申请是否有弹窗：  - true：有弹窗。  - false：无弹窗。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| errorReasons18+ | Array<number> | 否 | 是 | 申请相应权限的返回值说明：  0：本次申请合法。  1：权限名非法。  2：权限未声明。  3：不满足对应权限的申请条件，请参考[权限列表](../harmonyos-guides/permissions-for-all-user.md)中具体权限的说明。当前仅位置权限涉及。  4：用户未同意隐私声明。  5：该权限不支持通过权限弹窗进行申请，可能原因为该权限不支持申请或被系统策略强制管控。  6：该权限授权方式为manual\_settings，无法通过权限弹窗申请。  12：服务异常。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |

## 使用说明

PhonePC/2in1TabletTVWearable

通过atManager实例来获取。

**示例：**

示例中context的获取方式请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { abilityAccessCtrl, Context, common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let atManager = abilityAccessCtrl.createAtManager();
5. try {
6. // 请在组件内获取context
7. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
8. atManager.requestPermissionsFromUser(context, ["ohos.permission.CAMERA"]).then((data) => {
9. console.info("data permissions:" + data.permissions);
10. console.info("data authResults:" + data.authResults);
11. console.info("data dialogShownResults:" + data.dialogShownResults);
12. console.info("data errorReasons:" + data.errorReasons);
13. }).catch((err: BusinessError) => {
14. console.error(`code: ${err.code}, message: ${err.message}`);
15. })
16. } catch(err) {
17. console.error(`catch errcode: ${err.code}, message: ${err.message}`);
18. }
```
