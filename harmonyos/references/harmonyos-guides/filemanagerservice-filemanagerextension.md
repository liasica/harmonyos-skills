---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/filemanagerservice-filemanagerextension
title: 自定义文件角标和右键菜单项
breadcrumb: 指南 > 应用服务 > File Manager Service Kit（文件管理服务） > 自定义文件角标和右键菜单项
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:23+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:678d2040f5e98c4615654ed3721da7d4eeb5c0ed354aa8de3e4614884c836a94
---

从API版本26.0.1开始，新增支持自定义文件角标和右键菜单项。

## 场景介绍

用户在打开系统文件管理应用后，支持在文件目录展示应用接入的自定义动态文件角标，并支持显示自定义菜单配置，点击菜单后可实现个性化功能。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/8_jv125cSiCVpazSU7S6HA/zh-cn_image_0000002815399781.png)

## 约束限制

* FileManagerExtensionAbility为独立的进程，由系统的文件管理服务拉起，不允许应用主动拉起。
* 文件角标显示按应用安装顺序决策，仅问询当前设备上先安装的前15个注册文件扩展能力的应用；若同一文件目录被多个文件扩展监听，则按此顺序查询，仅展示最先安装且返回文件角标的第一个FileManagerExtensionAbility的角标。
* 右键菜单最多支持3级子菜单。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [onCreate](../harmonyos-references/filemanagerservice-arkts-extensionability.md#oncreate)(want: Want): void | FileManagerExtensionAbility创建时回调。 |
| [onDestroy](../harmonyos-references/filemanagerservice-arkts-extensionability.md#ondestroy)(): void | FileManagerExtensionAbility销毁前回调。 |
| [onObserveDir](../harmonyos-references/filemanagerservice-arkts-extensionability.md#onobservedir)(params: ObserveDirectoryParams): void | 文件管理应用进入指定目录时回调。 |
| [onStopObservingDir](../harmonyos-references/filemanagerservice-arkts-extensionability.md#onstopobservingdir)(params: ObserveDirectoryParams): void | 文件管理应用离开指定目录时回调。 |
| [onQueryBadges](../harmonyos-references/filemanagerservice-arkts-extensionability.md#onquerybadges)(params: QueryBadgesParams): Promise<QueryBadgesResult> | 文件管理应用查询指定目录下文件的角标。 |
| [onQueryMenu](../harmonyos-references/filemanagerservice-arkts-extensionability.md#onquerymenu)(params: QueryMenuParams): Promise<MenuConfig[]> | 右键菜单时查询扩展菜单配置。 |
| [onMenuAction](../harmonyos-references/filemanagerservice-arkts-extensionability.md#onmenuaction)(params: MenuActionParams): Promise<void> | 菜单项点击处理。 |
| [notifyBadgeChange](../harmonyos-references/filemanagerservice-arkts-extensionability.md#notifybadgechange)(params: BadgeChangeNotify): void | 推送角标变更至文件管理器。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { FileManagerExtensionAbility } from '@kit.FileManagerServiceKit';
   ```
2. 创建一个类继承FileManagerExtensionAbility，并使用export default导出该类。开发者需实现相关回调以提供自定义文件角标和右键菜单能力。

   ```typescript
   import { fileManagerService } from '@kit.FileManagerServiceKit';
   import Want from '@ohos.app.ability.Want';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { FileManagerExtensionAbility } from '@kit.FileManagerServiceKit';

   const DOMAIN = 0x0000;
   const TAG = 'MyExtensionAbility';

   /**
    * onCreate/onDestroy/onObserveDir/onStopObservingDir/onQueryBadges/onQueryMenu/onMenuAction接口，用于被文件管理应用按需回调。
    * notifyBadgeChange接口用于开发者主动调用。当文件变化后，开发者需要主动调用notifyBadgeChange接口，自主监听文件变化，通知文件管理应用刷新角标。
    */
   export default class MyExtensionAbility extends FileManagerExtensionAbility {

     onCreate(want: Want): void {
       hilog.info(DOMAIN, TAG,"MyExtensionAbility onCreate, want = " + JSON.stringify(want));
     }

     onDestroy(): void {
       hilog.info(DOMAIN, TAG,"MyExtensionAbility onDestroy");
     }

     onObserveDir(params: fileManagerService.ObserveDirectoryParams): void {
       // 开发者感知到文件管理应用进入到一个目录
       hilog.info(DOMAIN, TAG,"MyExtensionAbility onObserveDir, param = " + JSON.stringify(params));
     }

     onStopObservingDir(params: fileManagerService.ObserveDirectoryParams): void {
       hilog.info(DOMAIN, TAG,"MyExtensionAbility onStopObservingDir, param = " + JSON.stringify(params));
     }

     onQueryBadges(params: fileManagerService.QueryBadgesParams): Promise<fileManagerService.QueryBadgesResult> {
       hilog.info(DOMAIN, TAG,"MyExtensionAbility onQueryBadges, param = " + JSON.stringify(params));
       const badges: fileManagerService.FileBadge[] = [];
       badges.push({ uri: "file://docs/storage/Users/currentUser/Documents/example.txt", icon: String($r('app.media.add').id) });
       badges.push({ uri: "file://docs/storage/Users/currentUser/Documents/readme.txt", icon: String($r('app.media.add').id) });
       const result: fileManagerService.QueryBadgesResult = { isMemberOf: true, badges };
       return Promise.resolve(result);
     }

     onQueryMenu(params: fileManagerService.QueryMenuParams): Promise<fileManagerService.MenuConfig[]> {
       hilog.info(DOMAIN, TAG,"MyExtensionAbility onQueryMenu, param = " + JSON.stringify(params));
       let menu :fileManagerService.MenuConfig = {
         icon: String($r('app.media.add').id),
         description: "新建",
         menuId: 1,
         submenu: [],
       }
       return Promise.resolve([menu]);
     }

     onMenuAction(params: fileManagerService.MenuActionParams): Promise<void> {
       hilog.info(DOMAIN, TAG,"MyExtensionAbility onMenuAction, param = " + JSON.stringify(params));
       return Promise.resolve();
     }

     // 开发者实现自定义方法决定通知文件管理需要更新文件角标
     sendFileStateChangeMsg() {
       this.notifyBadgeChange({
         badges: [
           { uri: 'file://docs/storage/Users/currentUser/Documents/example.txt', icon: String($r('app.media.add').id) }
         ]
       });
     }
   }
   ```
3. 在模块的module.json5中注册该扩展类，声明类型为fileManager。

   ```json
   "extensionAbilities": [
     {
       "name": "FileServiceExtAbility",
       "srcEntry": "./ets/MyExtensionAbility/MyExtensionAbility.ets",
       "type": "fileManager",
       "exported": true,
       "metadata": []
     }
   ]
   ```
