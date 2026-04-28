---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-create-workspace
title: 创建工作空间
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 创建工作空间
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5e2f1221e07b987fd1e98fe46adb17b4fbfc845f98b90e7fdec389a089789933
---

## 场景介绍

Enterprise Space Kit为应用提供创建工作空间的能力。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#createworkspace)。

| 接口名 | 描述 |
| --- | --- |
| [createWorkspace](../harmonyos-references/enterprisespace-spacemanager.md#createworkspace)(localName: string, workspaceType: [WorkspaceType](../harmonyos-references/enterprisespace-spacemanager.md#workspacetype), params?: [CreateWorkspaceParams](../harmonyos-references/enterprisespace-spacemanager.md#createworkspaceparams)): Promise<[WorkspaceInfo](../harmonyos-references/enterprisespace-spacemanager.md#workspaceinfo)> | 创建工作空间并返回结果。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用[createWorkspace](../harmonyos-references/enterprisespace-spacemanager.md#createworkspace)接口，创建工作空间，并且查看打印信息。

   ```
   1. const localName: string = '111111';
   2. const workspaceType: spaceManager.WorkspaceType = spaceManager.WorkspaceType.ADMIN;
   3. const params: spaceManager.CreateWorkspaceParams = {
   4. shortName: 'test'
   5. };
   6. try {
   7. const workspaceInfo: spaceManager.WorkspaceInfo = await spaceManager.createWorkspace(localName, workspaceType, params);
   8. console.info(`Succeeded in creating workspace, workspaceInfo:` + JSON.stringify(workspaceInfo));
   9. } catch (err) {
   10. console.error(`Failed to create workspace. Code: ${err.code}, message: ${err.message}`);
   11. }
   ```
