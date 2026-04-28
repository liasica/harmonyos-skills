---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-get-access-token
title: 获取企业应用访问令牌
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 获取企业应用访问令牌
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:350e798d23a5ef197a5e521936a80cf0ad75ae6dfbdbc35a354137e82a88732a
---

## 场景介绍

从6.1.0(23)开始，支持企业应用获取访问令牌的能力。

Enterprise Space Kit为企业应用提供获取企业应用访问令牌的能力，可实现企业应用免密登录。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#getaccesstoken)。

| 接口名 | 描述 |
| --- | --- |
| [getAccessToken](../harmonyos-references/enterprisespace-spacemanager.md#getaccesstoken)(businessParams: Record<string, string>): Promise<Uint8Array> | 获取企业应用令牌并返回结果。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用[getAccessToken](../harmonyos-references/enterprisespace-spacemanager.md#getaccesstoken)接口，进行企业账号认证。

   ```
   1. try {
   2. const params: Record<string, string> = {
   3. 'clientId': 'test1' // 业务参数，由业务方根据请求协议自定义。
   4. };
   5. const result: Uint8Array = await spaceManager.getAccessToken(params);
   6. console.info(`Succeeded in getting access token. Result is: ` + JSON.stringify(result));
   7. } catch (err) {
   8. console.error(`Failed to get access token. Code: ${err.code}, message: ${err.message}`);
   9. }
   ```
