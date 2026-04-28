---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-set-workspace-status_bar_icon
title: 设置工作空间状态栏图标
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 设置工作空间状态栏图标
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a7d6d8dd88addf7e2c767de4f17029dc3a860ce1b1c4dd7d249a989243b83292
---

## 场景介绍

从6.1.0(23)开始，支持设置工作空间图标的能力。

Enterprise Space Kit为应用提供设置工作空间图标。所有工作空间都可以设置图标，可以展示在状态栏中。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#setworkspacestatusbaricon)。

| 接口名 | 描述 |
| --- | --- |
| [setWorkspaceStatusBarIcon](../harmonyos-references/enterprisespace-spacemanager.md#setworkspacestatusbaricon)(statusBarIcon: [StatusBarIcon](../harmonyos-references/enterprisespace-spacemanager.md#statusbaricon), workspaceId?: number): Promise<void> | 设置工作空间状态栏图标。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用[setWorkspaceStatusBarIcon](../harmonyos-references/enterprisespace-spacemanager.md#setworkspacestatusbaricon)接口，设置工作空间状态栏图标，并且查看打印信息。

   ```
   1. const context: Context = getContext();
   2. if (!context) {
   3. console.error('getHostContext failed');
   4. return;
   5. }
   6. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

   8. // 创建white pixelMap，需在资源rawfile文件夹中预置HuaweiWhite.jpg图片
   9. let whiteFileData = await resourceMgr.getRawFd('HuaweiWhite.jpg');
   10. const whiteImageSource: image.ImageSource = image.createImageSource(whiteFileData);
   11. const whitePixelMap: image.PixelMap = await whiteImageSource.createPixelMap();

   13. // 创建black pixelMap，需在资源rawfile文件夹中预置HuaweiBlack.jpg图片
   14. let blackFileData = await resourceMgr.getRawFd('HuaweiBlack.jpg');
   15. const blackImageSource: image.ImageSource = image.createImageSource(blackFileData);
   16. const blackPixelMap: image.PixelMap = await blackImageSource.createPixelMap();

   18. // 构建图标信息
   19. const icons: spaceManager.StatusBarIcon = { // 设置的工作空间的状态栏图标。
   20. white: whitePixelMap,
   21. black: blackPixelMap
   22. };
   23. const workspaceId: number = 100; // 工作空间ID。
   24. try {
   25. await spaceManager.setWorkspaceStatusBarIcon(icons, workspaceId);
   26. console.info(TAG, `Succeeded in setting workspace status bar icon`);
   27. } catch (err) {
   28. console.error(`Failed to set workspace status bar icon. Code: ${err.code}, message: ${err.message}`);
   29. }
   ```
