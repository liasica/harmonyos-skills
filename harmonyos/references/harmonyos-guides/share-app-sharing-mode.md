---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-app-sharing-mode
title: 配置目标应用名单（仅对企业应用开放）
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 宿主应用发起分享 > 配置目标应用名单（仅对企业应用开放）
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:214f14dcaa1dae77d65955640a79ae36cb430cfc704f57bc9f1469b4d3040737
---

## 场景介绍

该功能仅对企业应用开放。6.0.1(21)版本开始，支持宿主应用配置目标应用名单列表（最多支持50个应用）。配置成功后，仅名单内的目标可出现在系统分享面板的分享推荐区和分享方式区。

## 申请权限

当前能力受限开放，需要申请受限开放权限ohos.permission.SET\_SYSTEMSHARE\_APPLAUNCHTRUSTLIST。

**说明** 

该权限用于限制应用分享范围，仅支持企业应用限制内部数据分享到企业集团信任的应用。

申请权限时，需要在reasonPrompt里面填写企业应用的信息和管控场景。如：用于XXX集团应用管控内部资料仅限于企业内部分享。

申请方式请参考：[申请使用受限权限](declare-permissions-in-acl.md)。

## 示例代码

1. 应用必须在module.json5配置文件的requestPermissions标签中声明权限。参考：[声明权限](declare-permissions.md)。

   ```json
   {
     "module": {
       // ...
       "requestPermissions": [
         {
           "name": "ohos.permission.SET_SYSTEMSHARE_APPLAUNCHTRUSTLIST",
           "reason": '$string:permission_reason_set_system_share_app_launch_trust_list'
         },
       ]
     }
   }
   ```
2. 启动分享面板时，通过配置appLaunchTrustInfo参数，指定目标应用的范围。

   ```typescript
   import { common } from '@kit.AbilityKit';
   import { systemShare } from '@kit.ShareKit';
   import { uniformTypeDescriptor as utd } from '@kit.ArkData';

   @Component
   export struct ShareAppTrustInfo {
     build() {
       Button('share').onClick(() => {
         this.share();
       })
     }

     private share() {
       // 构造ShareData，需配置一条有效数据信息
       let data: systemShare.SharedData = new systemShare.SharedData({
         utd: utd.UniformDataType.PLAIN_TEXT,
         content: 'Hello HarmonyOS'
       });
       let uiContext: UIContext = this.getUIContext();
       // 构建ShareController
       let controller: systemShare.ShareController = new systemShare.ShareController(data);
       let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
       // 进行分享面板显示
       controller.show(context, {
         previewMode: systemShare.SharePreviewMode.DEFAULT,
         selectionMode: systemShare.SelectionMode.SINGLE,
         appLaunchTrustInfo: ['5765880207853060000', '1171817433862770000'], // 此值仅为示例. 目标应用 appidentifier
       })
     }
   }
   ```
