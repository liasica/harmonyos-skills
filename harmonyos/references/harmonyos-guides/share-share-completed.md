---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-share-completed
title: 获取分享结果
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 宿主应用发起分享 > 获取分享结果
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6ecb6190acfb989a08574dbaa6e4f98c89ab8767232dcb149ba20066dccc1e68
---

## 场景介绍

从5.1.0(18)版本开始，支持宿主应用获取用户分享结果。

基于业务实现需要，开发者可统计用户使用分享功能时，将内容分享到了哪些渠道。渠道信息规则如下：

* 系统操作有固定名称。请参见：[ShareAbilityName](../harmonyos-references/share-system-share.md#shareabilityname)。
* 非系统操作采用'[bundleName]#[moduleName]#[abilityName]'格式拼接。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { common } from '@kit.AbilityKit';
   import { systemShare } from '@kit.ShareKit';
   import { uniformTypeDescriptor as utd } from '@kit.ArkData';
   ```
2. 构造分享数据。

   ```typescript
   // 构造ShareData，需配置一条有效数据信息
   let data: systemShare.SharedData = new systemShare.SharedData({
     utd: utd.UniformDataType.PLAIN_TEXT,
     content: 'Hello HarmonyOS'
   });
   ```
3. 注册分享结果监听事件，并启动分享面板。

   ```typescript
   // 构建ShareController
   let controller: systemShare.ShareController = new systemShare.ShareController(data);
   // 获取UIAbility上下文对象
   let uiContext: UIContext = this.getUIContext();
   let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
   // 注册分享结果事件监听
   controller.on('shareCompleted', (result: systemShare.ShareOperationResult) => {
     console.info('shareCompleted name:', result.targetAbilityInfo.name);
     // 可根据分享渠道进行数据统计等操作
   });

   // 进行分享面板显示
   controller.show(context, {
     previewMode: systemShare.SharePreviewMode.DEFAULT,
     selectionMode: systemShare.SelectionMode.SINGLE
   });
   ```
