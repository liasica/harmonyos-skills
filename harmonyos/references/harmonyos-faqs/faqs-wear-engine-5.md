---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-wear-engine-5
title: Wear Engine请求用户授权requestAuthorization失败
breadcrumb: FAQ > 系统开发 > 硬件 > 穿戴服务（Wear Engine Kit） > Wear Engine请求用户授权requestAuthorization失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6abdc7b45b3d2795d079ca2bb390cb85f63ed8e2564b4fbe90b0d85d9d4c779d
---

## 问题现象

按照官网Wear Engine开发指导，请求用户授权requestAuthorization失败。

调用Wear Engine相关接口前置条件已配置：

1. 申请通过Wear Engine服务（设备基础信息）。
2. 在应用module.json5中配置了client\_id。
3. 应用手动签名，且配置了公钥。

请求授权：

```ts
// 在使用Wear Engine服务前，请导入Wear Engine与相关模块
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

// 步骤1：获取AuthClient对象
let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());

// 步骤2：基于需要用户授权的权限定义权限请求类
let request: wearEngine.AuthorizationRequest = {
  permissions: [wearEngine.Permission.USER_STATUS]
}

// 步骤3：请求用户授权
authClient.requestAuthorization(request).then(result => {
  console.info(`Succeeded in requesting authorize, authorized permissions is ${result.permissions}`);
}).catch((error: BusinessError) => {
  console.error(`Failed to request authorize. Code is ${error.code}, message is ${error.message}`);
})
```

## 背景知识

* 调用Wear Engine服务前，需要在开发者联盟接入Wear Engine服务能力：[申请接入Wear Engine服务](../harmonyos-guides/wearengine_apply.md)。
* [配置Client ID](../harmonyos-guides/configuration_client_id.md)。
* 需要用户授权的权限枚举如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/aMx61y2SSfmiXCwG4LAhAQ/zh-cn_image_0000002628775058.png "点击放大")

## 问题定位

1. 日志显示报错，The app does not have the required scopes or permission.no scope permission。
2. 确认申请的Wear Engine服务权限仅勾选了“设备基础信息”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/1aPGyb1qTGuvn8id01iv1A/zh-cn_image_0000002658974375.png "点击放大")
3. 查看USER\_STATUS对应的服务权限为“获取用户状态权限”。

## 分析结论

1. 用户在开发者联盟平台申请的权限为“设备基础权限”，应用内申请授权的权限为“获取用户状态权限”，不匹配。
2. 没有在开发者联盟平台申请过的权限，不予授权。
3. 在开发者联盟平台申请通过Wear Engine“设备基础权限”后，无需用户授权。

## 修改建议

Wear Engine服务“设备基础信息”包含手机与穿戴设备通信、获取已配对穿戴设备的随机标识符等信息的能力。如果在开发者联盟平台申请通过此权限，无需在应用内申请授权，请删除请求授权代码。

Wear Engine服务权限是否需要用户授权映射关系如下：

| Wear Engine服务权限 | permission | 是否需要用户授权 |
| --- | --- | --- |
| 设备基础信息 | NA | 否 |
| 消息通知 | NA | 否 |
| 穿戴用户状态 | wearEngine.Permission.USER\_STATUS | 是 |
| 人体传感器 | wearEngine.Permission.HEALTH\_SENSOR | 是 |
| 运动传感器 | wearEngine.Permission.MOTION\_SENSOR | 是 |
| 设备标识符 | wearEngine.Permission.DEVICE\_IDENTIFIER | 是 |
