---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-mobilephone-app-share
title: 通过分享面板发起分享
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 宿主应用发起分享 > 通过分享面板发起分享
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5f3eef6774d802c9dad870b0c12e047fa47689e5f66b68102d5627e3e3db37b2
---

## 接口说明

**表1** 宿主应用发起分享接口功能介绍

| 类名 | 接口名 | 描述 |
| --- | --- | --- |
| SharedData | [constructor](../harmonyos-references/share-system-share.md#constructor)(record: [SharedRecord](../harmonyos-references/share-system-share.md#sharedrecord)) | SharedData构造函数 |
| SharedData | [addRecord](../harmonyos-references/share-system-share.md#addrecord)(record: [SharedRecord](../harmonyos-references/share-system-share.md#sharedrecord)): void | 添加分享记录 |
| SharedData | [getRecords](../harmonyos-references/share-system-share.md#getrecords)(): Array<[SharedRecord](../harmonyos-references/share-system-share.md#sharedrecord)> | 获取分享记录 |
| ShareController | [constructor](../harmonyos-references/share-system-share.md#constructor-1)(data: [SharedData](../harmonyos-references/share-system-share.md#shareddata)) | ShareController构造函数 |
| ShareController | [show](../harmonyos-references/share-system-share.md#show)(context: [common.UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md), options: [ShareControllerOptions](../harmonyos-references/share-system-share.md#sharecontrolleroptions)): Promise<void> | 显示分享面板 |
| ShareController | [on](../harmonyos-references/share-system-share.md#ondismiss)(event: 'dismiss', callback: () => void): void | 注册分享面板关闭事件监听 |
| ShareController | [off](../harmonyos-references/share-system-share.md#offdismiss)(event: 'dismiss', callback: () => void): void | 取消分享面板关闭事件监听 |

## 开发步骤

根据不同的分享场景，参考下表：

| 分享场景 | 参考链接 |
| --- | --- |
| 分享App Linking直达应用 | [分享App Linking直达应用](share-utd-link.md#分享app-linking直达应用) |
| 分享图片 | [分享图片](share-utd-image.md) |
| 分享视频 | [分享视频](share-utd-video.md) |
| 分享普通链接直达浏览器 | [分享普通链接直达浏览器](share-utd-link.md#分享普通链接直达浏览器) |
| 分享文本 | [分享文本](share-utd-text.md) |

**2in1设备可通过配置的方式决定分享面板的显示位置。** 参考如下：

1. 导入相关模块。

   ```typescript
   import { common } from '@kit.AbilityKit';
   import { systemShare } from '@kit.ShareKit';
   import { uniformTypeDescriptor as utd } from '@kit.ArkData';
   ```
2. 构造分享数据，可添加多条分享记录。

   ```typescript
   // 构造ShareData，需配置一条有效数据信息
   let data: systemShare.SharedData = new systemShare.SharedData({
     utd: utd.UniformDataType.PLAIN_TEXT,
     content: 'Hello HarmonyOS'
   });
   ```
3. 启动分享面板时，配置分享面板显示的位置信息或关联的组件ID，面板将以Popup形式展示。

   ```typescript
   // 构建ShareController
   let controller: systemShare.ShareController = new systemShare.ShareController(data);
   // 获取UIAbility上下文对象
   let uiContext: UIContext = this.getUIContext();
   let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
   // 注册分享面板关闭监听
   controller.on('dismiss', () => {
     console.info('Share panel closed');
     // 分享结束，可处理其他业务。
   });

   // 进行分享面板显示
   // 方法一：配置分享面板关联的控件ID
   controller.show(context, {
     anchor: 'shareButtonId'
   });
   // 方法二：配置分享面板显示的坐标
   controller.show(context, {
     anchor: {
       // 必选 相对锚点的窗体偏移值
       windowOffset: { x: 100, y: 100 },
       // 可选 组件的宽高 配置后会综合计算组件的大小
       size: { width: 0, height: 0 }
     }
   });
   ```
