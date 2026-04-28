---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-set-workspace-info
title: 设置工作空间信息
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 设置工作空间信息
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c2d068f20064b53272d67b1fda9beba4e8dfeed140e631bb7fff722ffeac71bf
---

## 场景介绍

Enterprise Space Kit为应用提供设置工作空间信息的能力。在企业初始化阶段，设置工作空间信息，方便企业绑定域账号。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#setworkspaceinfo)。

| 接口名 | 描述 |
| --- | --- |
| [setWorkspaceInfo](../harmonyos-references/enterprisespace-spacemanager.md#setworkspaceinfo)(workspaceId: number, domainInfo: [WorkspaceDomainInfo](../harmonyos-references/enterprisespace-spacemanager.md#workspacedomaininfo)): Promise<void> | 设置工作空间信息。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用[setWorkspaceInfo](../harmonyos-references/enterprisespace-spacemanager.md#setworkspaceinfo)接口，设置工作空间信息，并且查看打印信息。

   ```
   1. const workspaceId: number = 100;
   2. const domainInfo: spaceManager.WorkspaceDomainInfo = {
   3. domain: 'test1',
   4. workspaceName: 'test2',
   5. accountId: 'test3',
   6. isAuthenticated: false,
   7. serverConfigId: 'test4',
   8. enterpriseWorkspaceName: 'default'
   9. };

   11. try {
   12. await spaceManager.setWorkspaceInfo(workspaceId, domainInfo);
   13. console.info('Succeeded in setting workspace info');
   14. } catch (err) {
   15. console.error(`Failed to set workspace info. Code: ${err.code}, message: ${err.message}`);
   16. }
   ```
