---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-set-workspace-profile-photo
title: 设置工作空间资料照片
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 设置工作空间资料照片
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f34d33fe8fb7d57796afca95d9ea485070bf977c74ad05530d7bd7a0cbb4f65c
---

## 场景介绍

Enterprise Space Kit为应用提供设置工作空间资料照片的能力。所有工作空间都可以设置资料照片。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#setworkspaceprofilephoto)。

| 接口名 | 描述 |
| --- | --- |
| [setWorkspaceProfilePhoto](../harmonyos-references/enterprisespace-spacemanager.md#setworkspaceprofilephoto)(workspaceId: number, photo: string): Promise<void> | 设置工作空间资料照片。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用[setWorkspaceProfilePhoto](../harmonyos-references/enterprisespace-spacemanager.md#setworkspaceprofilephoto)接口，设置工作空间资料照片，并且查看打印信息。

   ```
   1. const workspaceId: number = 100;
   2. const photo: string = '{"type":0,"defaultImg":"data:image/png;base64,iVBO******Jggg==}';
   3. try {
   4. await spaceManager.setWorkspaceProfilePhoto(workspaceId, photo);
   5. console.info('Succeeded in setting workspace profile photo');
   6. } catch (err) {
   7. console.error(`Failed to set workspace profile photo. Code: ${err.code}, message: ${err.message}`);
   8. }
   ```
