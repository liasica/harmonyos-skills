---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-comment
title: 应用评论服务
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用评论服务
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:377e9bae0989ec7551694a03f5b931ec289c7520255ebc0546390fefef65dfb8
---

通过应用评论服务，用户无需进入应用市场应用详情页，可以直接在应用内进行评论。

说明

从版本6.0.0(20)开始，支持拉起应用评论弹框。

## 场景介绍

* 拉起应用评论弹框

  开发者可以通过该接口拉起应用评论弹窗对应用进行评分及评论，无需进入应用市场应用详情页进行评论。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/X7B3UB8dQk-08OBEnfNRuQ/zh-cn_image_0000002558765294.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053716Z&HW-CC-Expire=86400&HW-CC-Sign=37AB25FEB93C8DEEBB19E875DBBC49BE34AA98DC43DC29836F6E14D238603CA2)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/4D9HPjOITkyuCtE0gbbKBA/zh-cn_image_0000002558605638.png?HW-CC-KV=V1&HW-CC-Date=20260429T053716Z&HW-CC-Expire=86400&HW-CC-Sign=4FDBC36D933CA8741983D805A9760CD7381013FFDC2A971EB0D3B1183C946C7C)

1. 用户需要在应用内评论应用。
2. 应用调用showCommentDialog接口拉起应用评论弹窗。
3. AppGalleryKit返回接口调用结果给应用。
4. 应用返回评论窗口给用户。

## 约束与限制

应用评论服务不支持模拟器，请使用真机调试。

## 接口说明

应用评论服务提供以下接口，具体API说明详见[接口文档](../harmonyos-references/appgallery-commentmanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [showCommentDialog](../harmonyos-references/appgallery-commentmanager.md#commentmanagershowcommentdialog)(context: common.UIExtensionContext | common.UIAbilityContext): Promise<void> | 拉起应用评论弹窗，用户可以在应用内评论应用。 |

## 开发步骤

1. 导入commentManager模块及相关公共模块。

   ```
   1. import { commentManager} from '@kit.AppGalleryKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import type { common } from '@kit.AbilityKit';
   ```
2. 调用[showCommentDialog](../harmonyos-references/appgallery-commentmanager.md#commentmanagershowcommentdialog)方法拉起评论弹窗。

   ```
   1. try {
   2. const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   3. commentManager.showCommentDialog(uiContext).then(()=>{
   4. hilog.info(0, 'TAG', "succeeded in showing commentDialog.");
   5. }).catch((error: BusinessError<Object>) => {
   6. hilog.error(0, 'TAG', `showCommentDialog failed, Code: ${error.code}, message: ${error.message}`);
   7. });
   8. } catch (error) {
   9. hilog.error(0, 'TAG', `showCommentDialog failed, Code: ${error.code}, message: ${error.message}`);
   10. }
   ```
