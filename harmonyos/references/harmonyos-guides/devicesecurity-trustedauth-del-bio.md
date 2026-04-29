---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-del-bio
title: 关闭指定生物类型认证能力
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 数字盾服务 > 生物特征绑定、认证与解绑 > 关闭指定生物类型认证能力
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:41b34dfc8de707bc86e9c50153959c415d16c6bf36c5be4a5a2daa3447291318
---

## 场景介绍

当用户期望关闭指定生物特征认证能力时，可以通过指定已开通的生物特征信息，关闭指定的生物类型认证能力。

## 约束与限制

本功能目前仅在手机设备支持，且需应用服务器端同步接入配合端云协同认证。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/sefRlOCtQMWBRni9tQOYHg/zh-cn_image_0000002558764896.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053134Z&HW-CC-Expire=86400&HW-CC-Sign=0585EC217FFF4F5EB4F1410323B1C6F16C26FDE1DCE89C930C4FC7C1611972DE)

## 接口说明

接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-arktsapi-errcode-trusted-auth.md)。

| 接口名 | 描述 |
| --- | --- |
| [disableTrustedBioAuthentication](../harmonyos-references/devicesecurity-trusted-auth-api.md#disabletrustedbioauthentication)(authID: bigint, authType: [AuthType](../harmonyos-references/devicesecurity-trusted-auth-api.md#authtype)): Promise<void> | 解绑指定生物类型认证能力 |

## 开发步骤

1. 导入trustedAuthentication 和相关依赖模块。

   ```
   1. import { trustedAuthentication} from '@kit.DeviceSecurityKit';
   2. import { BusinessError} from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 首先开发者需要在服务器查询对应账户是否已开通对应生物特征认证能力，在确认开通后方可发起解绑指定生物类型认证能力请求。
3. 发起关闭指定生物类型认证能力请求前，需从服务器获取当前账号在[设置数字盾密码](devicesecurity-trustedauth-setpwd.md)时获取的authID。
4. 调用数字盾解绑指定生物类型认证能力接口发起关闭对应生物类型认证能力申请。

   ```
   1. const TAG = "TrustedAuthenticationJsTest";
   2. try {
   3. const authID: bigint = 1687413472599354502n;//实际填充为从服务器获取到的账号对应的authID值
   4. const authType = trustedAuthentication.AuthType.AUTH_TYPE_FACE; //实际填充为计划解绑的生物特征类型
   5. const remainTimes = await trustedAuthentication.disableTrustedBioAuthentication(authID, authType);
   6. } catch (err) {
   7. let e: BusinessError = err as BusinessError;
   8. hilog.error(0x0000, TAG, 'disableTrustedBioAuthentication: %{public}d %{public}s', e.code, e.message);
   9. }
   ```
5. 在接收到端侧解绑成功结果后，开发者需要同步将服务器绑定的生物特征信息解绑。
