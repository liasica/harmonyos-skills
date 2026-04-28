---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-authenticate
title: 企业账号认证
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 企业账号认证
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5570f39f4c8125444ab8aa7747673b5c6411dc115f564f50b3dfb4460a87e329
---

## 场景介绍

从6.1.0(23)开始，支持企业认证的能力。

Enterprise Space Kit为企业应用提供企业账号认证的能力。在企业空间初始化阶段，实现企业用户的账号认证。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#authenticate)。

| 接口名 | 描述 |
| --- | --- |
| [authenticate](../harmonyos-references/enterprisespace-spacemanager.md#authenticate)(enterpriseAuthInfo: [WorkspaceDomainInfo](../harmonyos-references/enterprisespace-spacemanager.md#workspacedomaininfo), credential: Uint8Array): Promise<[AuthResult](../harmonyos-references/enterprisespace-spacemanager.md#authresult)> | 企业账号认证并返回结果。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用[authenticate](../harmonyos-references/enterprisespace-spacemanager.md#authenticate)接口，进行企业账号认证。

   ```
   1. try {
   2. const enterpriseAuthInfo: spaceManager.WorkspaceDomainInfo = {
   3. domain: 'testDomain', // 域名。
   4. workspaceName: 'testAccountName', // 工作空间域账号名称。
   5. serverConfigId: 'testServerConfigId' // 工作空间所属域的服务器配置标识符。
   6. };
   7. const credential = new Uint8Array([0, 0, 0, 0, 0, 0, 0, 0])
   8. const authResult: spaceManager.AuthResult = await spaceManager.authenticate(enterpriseAuthInfo, credential);
   9. console.info(`Succeeded in authenticating. Auth result is: ` + JSON.stringify(authResult));
   10. } catch (err) {
   11. console.error(`Failed to authenticate. Code: ${err.code}, message: ${err.message}`);
   12. }
   ```
