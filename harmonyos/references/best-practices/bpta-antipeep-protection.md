---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-antipeep-protection
title: 防窥保护
breadcrumb: 最佳实践 > 技术创新 > 防窥保护
category: best-practices
scraped_at: 2026-09-02T15:03:15+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:f6ed041c256b178158ae9cff4a404a05c42f88344bc3d8c323f7c41bb35c2318
---

## 概述

HarmonyOS自发布以来持续深化安全与隐私能力体系建设：从早期的应用沙箱隔离、权限管控，到数据防泄漏（DLP）框架，再到如今面向物理环境的感知型安全防护能力，安全防护的边界已从系统内部延伸至用户所处的真实空间。

与此同时，移动设备已深度融入日常生活——人们在地铁、咖啡厅、会议室等公共场所查看账户余额、阅读私密消息、浏览个人内容。屏幕上的信息可能暴露在陌生人的视线之下，“肩窥”已成为现实生活中不可忽视的隐私威胁。

正是在这一背景下，HarmonyOS推出了dlpAntiPeep（防窥保护）能力。它依托前置摄像头的实时感知，检测屏幕前是否存在非机主人员，并在检测到窥视时通知应用主动隐藏敏感信息或触发系统防窥蒙层，将安全防护从系统层延伸到用户的物理使用环境。

## 场景介绍

### 防窥保护简介

防窥保护能力采用“感知 + 响应”的分层设计，由应用根据自身业务特点灵活决策——检测到窥视时，可以选择遮盖敏感字段、模糊画面、暂停播放，也可以直接拉起系统级防窥蒙层覆盖整个窗口。这种灵活的响应机制意味着防窥保护并非对所有场景一刀切地拦截，而是让不同类型的应用都能以最贴合自身场景的方式接入防窥保护

### 防窥保护应用场景

以下列举了防窥保护能力的典型应用场景。需要注意的是，这些场景仅为示例，开发者应根据应用的实际业务特点和用户隐私需求，灵活运用防窥保护能力，而不必局限于这些场景。任何涉及敏感信息展示的应用场景都可以考虑接入防窥保护。

1. 金融类应用汇集了大量的财务敏感信息——账户余额、收益曲线、持仓明细，每一项都是不希望被他人知晓的隐私数据。在地铁、咖啡厅等人流密集的公共场所，用户往往无暇顾及身旁是否有人窥视屏幕。接入dlpAntiPeep能力后，应用可在检测到窥视的瞬间自动将敏感数字替换为 \*\*\*\*，并可选触发系统级防窥蒙层，让用户在任何环境下都能放心查看财务信息，效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/b6VMwCKFSoGQEnWVcFDtaA/zh-cn_image_0000002624454639.gif "点击放大")
2. 短视频内容往往折射出用户的个人偏好、生活习惯乃至私密时刻，这些信息在公共场所被他人看到，会带来不同程度的隐私不适感。接入dlpAntiPeep能力后，应用可在检测到窥视时暂停定制化推送内容的展示，或对关注列表进行模糊隐藏，待窥视解除后自动恢复，在不打断用户使用节奏的前提下，为内容浏览筑起一道隐形屏障，效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/U3cfmX8tQ_GaS56dpzcC5w/zh-cn_image_0000002594175038.png "点击放大")
3. 即时通讯是隐私敏感度最高的应用场景之一——消息列表中的联系人姓名、消息预览，聊天详情中的情感交流、商业沟通，任何一条信息被旁观者读取都可能造成难以挽回的隐私损失。接入dlpAntiPeep能力后，应用可在检测到窥视时将消息内容隐藏或替换为自定义不敏感内容，确保私密对话只属于对话双方，效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/iiPoz3xsTXCxOiqSTtuzFA/zh-cn_image_0000002624574493.png "点击放大")

## 案例实现

本节以用户隐私安全的财务场景为例，介绍[DlpAntiPeep（防窥保护](../harmonyos-references/devicesecurity-dlpantipeep-api.md)）能力的完整接入方案。

### 实现原理

dlpAntiPeep能力属于[Device Security Kit（设备安全服务）](../harmonyos-references/device-security-api.md)，通过前置摄像头实时分析屏幕前的人员情况，将结果以[DlpAntiPeepStatus](../harmonyos-references/devicesecurity-dlpantipeep-api.md#dlpantipeepstatus)枚举值的形式通知应用。核心优势在于系统级的实时感知与应用层的灵活响应，开发者无需自行实现人脸检测算法，只需调用少量API即可为应用添加防窥保护功能。

整体实现流程如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/du684xoYQciVdxVC8h0frA/zh-cn_image_0000002594015116.jpg "点击放大")

## 开发前置条件

在正式接入防窥保护能力前，开发者需要引导用户授权打开防窥保护开关。防窥保护功能需要用户在系统设置中主动开启，应用才能获取相关权 限并启用防窥能力。API23版本开始，可调用[requestAntiPeepOptions](../harmonyos-references/devicesecurity-dlpantipeep-api.md#requestantipeepoptions)拉起弹窗，弹窗中开启系统设置中的防窥保护按钮，此接口避免了用户主动转到设置中开启按钮。

```typescript
// Request the system to obtain the configuration options for anti-peeping protection
const result = await dlpAntiPeep.requestAntiPeepOptions(context);
```

### 开发步骤

1. 检测设备能力并查询开关状态：使用[canIUse()](../harmonyos-references/js-apis-syscap.md#caniuse)检测设备是否支持防窥能力，再调用[isDlpAntiPeepSwitchOn()](../harmonyos-references/devicesecurity-dlpantipeep-api.md#isdlpantipeepswitchon)确认用户已开启系统开关，两项条件均满足后才进行后续初始化。

   ```typescript
   export function canUseAntiPeep(): boolean {
     return canIUse('SystemCapability.Security.DlpAntiPeep');
   }
   ```

   ```typescript
   export async function isAntiPeepOn(): Promise<boolean> {
     try {
       if (canUseAntiPeep()) {
         let result: boolean = await dlpAntiPeep.isDlpAntiPeepSwitchOn();
         Logger.info(TAG, `[isAntiPeepOn] isDlpAntiPeepSwitchOn success. ${result}`);
         return result;
       } else {
         return false;
       }
     } catch (err) {
       Logger.error(TAG, `[isAntiPeepOn] isDlpAntiPeepSwitchOn failed.${JSON.stringify(err)}`);
       return false;
     }
   }
   ```
2. 获取当前窥视状态并注册监听：调用[getDlpAntiPeepInfo()](../harmonyos-references/devicesecurity-dlpantipeep-api.md#getdlpantipeepinfo)同步获取页面展示时的初始状态。

   ```typescript
   if (canUseAntiPeep()) {
     isAntiPeepOn().then(async (opened) => {
       if (opened) {
         let info = getAntiPeepInfo();
         // ...
       }
     })
     // ...
   }
   ```

   ```typescript
   export function getAntiPeepInfo(): dlpAntiPeep.DlpAntiPeepStatus {
     try {
       if (canUseAntiPeep()) {
         let dlpAntiPeepStatus = dlpAntiPeep.getDlpAntiPeepInfo();
         Logger.info(TAG, `getDlpHideInfo success. ${JSON.stringify(dlpAntiPeepStatus)}`);
         return dlpAntiPeepStatus;
       } else {
         return -1;
       }
     } catch (err) {
       Logger.info(TAG, `getDlpHideInfo failed. ${JSON.stringify(err)}`);
       return -1;
     }
   }
   ```
3. 根据窥视状态切换敏感信息显示：在状态回调中，当状态为[DlpAntiPeepStatus.HIDE](../harmonyos-references/devicesecurity-dlpantipeep-api.md#dlpantipeepstatus)时将@State修饰的金额变量替换为 \*\*\*\*，状态为[DlpAntiPeepStatus.PASS](../harmonyos-references/devicesecurity-dlpantipeep-api.md#dlpantipeepstatus)时恢复真实数值，ArkUI框架自动触发界面刷新。

   ```typescript
   if (canUseAntiPeep()) {
     isAntiPeepOn().then(async (opened) => {
       if (opened) {
         let info = getAntiPeepInfo();
         this.handleAntiPeepStatus(info);
         // ...
       }
     })
     // ...
   }
   ```

   ```typescript
   private async handleAntiPeepStatus(status: dlpAntiPeep.DlpAntiPeepStatus) {
     if (canUseAntiPeep()) {
       switch (status) {
         case dlpAntiPeep.DlpAntiPeepStatus.PASS:
           this.summaryShow(true);
           this.itemsEnableShow(true);
           break;
         case dlpAntiPeep.DlpAntiPeepStatus.HIDE:
           // ...
           this.summaryShow(false);
           this.itemsEnableShow(false);
           break;
         default:
           this.summaryShow(true);
           this.itemsEnableShow(true);
           break;
       }
     } else {
       return
     }
   }
   ```
4. 实时监听：通过[on("dlpAntiPeep")](../harmonyos-references/devicesecurity-dlpantipeep-api.md#ondlpantipeep)注册监听，确保状态变化时立即响应，更新界面内容。

   ```typescript
   private antiPeepCB: AntiPeepCallback = {
     onStatusChanged: async (status: dlpAntiPeep.DlpAntiPeepStatus): Promise<void> => {
       await this.handleAntiPeepStatus(status);
     }
   };
   ```

   ```typescript
   export function listenOnAntiPeepStatus(antiPeepCB: AntiPeepCallback): boolean {
     try {
       if (canUseAntiPeep()) {
         Logger.info(TAG, `start on('dlpAntiPeep')`);
         dlpAntiPeep.on('dlpAntiPeep', (dlpAntiPeepStatus: dlpAntiPeep.DlpAntiPeepStatus) => {
           Logger.info(TAG, `dlpAntiPeep callback: ${JSON.stringify(dlpAntiPeepStatus)}`);
           if (antiPeepCB) {
             antiPeepCB.onStatusChanged(dlpAntiPeepStatus);
           } else {
             Logger.warn(TAG, `antiPeepCB is empty`);
           }
         });
         Logger.info(TAG, `on('dlpAntiPeep') ok`);
         return true;
       } else {
         return false;
       }
     } catch (err) {
       Logger.error(TAG, `dlpAntiPeep.on failed. ${JSON.stringify(err)}`);
       return false;
     }
   }
   ```
5. 触发系统防窥蒙层（可选）：当用户开启了防窥蒙层开关且检测到窥视时，在切换敏感信息显示函数handleAntiPeepStatus()中调用[setAntiPeepMaskLayer()](../harmonyos-references/devicesecurity-dlpantipeep-api.md#setantipeepmasklayer)拉起系统级蒙层覆盖整个窗口。建议开发者在检测到窥视状态后调用一次即可，频繁调用可能对用户体验造成影响。直到用户重新进入页面前不再重复触发。

   ```typescript
   case dlpAntiPeep.DlpAntiPeepStatus.HIDE:
     if (this.isShowToggle && this.isToggleOpened) {
       try {
         // The anti-peep overlay has not been triggered yet.
         if (!this.isSystemLayerTriggered && !this.isAlertDialogShow) {
           const id = AppStorage.get(ConstValues.WINDOW_ID_NAME) as number;
           this.isSystemLayerTriggered = await showSystemMaskLayer(id);
           // ...
         }
       } catch (err) {
         Logger.error(TAG, `Show mask layer error:${JSON.stringify(err)}`);
       }
     }
     // ...
     break;
   ```

   ```typescript
   export function showSystemMaskLayer(windowId: number): Promise<boolean> {
     return new Promise((resolve) => {
       try {
         if (canUseAntiPeep()) {
           dlpAntiPeep.setAntiPeepMaskLayer(windowId).catch((err: BusinessError) => {
             Logger.error(TAG, `Execute setAntiPeepMaskLayer failed. error code:${err.code}, error message:${err.message}`);
             resolve(false);
           }).then(() => {
             Logger.info(TAG, `setAntiPeepMaskLayer success`);
             resolve(true);
           })
         } else {
           resolve(false);
         }
       } catch (err) {
         Logger.error(TAG, `Call setAntiPeepMaskLayer failed. ${JSON.stringify(err)}`);
         resolve(false);
       }
     });
   }
   ```
6. 页面销毁时取消监听：在aboutToDisappear()生命周期中调用[off("dlpAntiPeep")](../harmonyos-references/devicesecurity-dlpantipeep-api.md#offdlpantipeep)取消监听，防止页面销毁后回调仍然触发导致内存泄漏。

```typescript
aboutToDisappear(): void {
  if (this.isListenOn) {
    listenOffAntiPeepStatus();
    this.isListenOn = false;
  }
  // ...
}
```

```typescript
export function listenOffAntiPeepStatus() {
  try {
    if (canUseAntiPeep()) {
      Logger.info(TAG, `start off('dlpAntiPeep')`);
      dlpAntiPeep.off('dlpAntiPeep');
      Logger.info(TAG, `off('dlpAntiPeep') ok`);
    }
  } catch (err) {
    Logger.error(TAG, `dlpAntiPeep.off failed. ${JSON.stringify(err)}`);
  }
}
```

### 效果预览

防窥保护效果如下所示：

|  |  |  |
| --- | --- | --- |
| **正常显示** | **窥视隐藏** | **系统防窥蒙层** |
|  |  |  |

**注意** 

调用任何dlpAntiPeep API之前，必须先通过canIUse('SystemCapability.Security.DlpAntiPeep')检测设备能力，在不支持该SystemCapability的设备上直接调用会抛出异常导致应用崩溃。

在页面组件的aboutToDisappear()生命周期中必须调用dlpAntiPeep.off('dlpAntiPeep')取消监听，否则页面销毁后回调仍会触发，导致访问已销毁组件状态时出现异常。

setAntiPeepMaskLayer()触发的系统防窥蒙层每次进入页面只触发一次，需通过标志位isSystemLayerTriggered控制，避免重复触发。

如果仅本地调试防窥保护能力，自动签名时同意权限申请即可；如果应用上架需使用防窥保护能力则需要申请ohos.permission.DLP\_GET\_HIDE\_STATUS权限，并在AGC平台[申请ACL权限](../app/agc-help-apply-acl-0000002394212138.md)。

## 约束与限制

1. API版本：dlpAntiPeep相关api接口需保证API版本20及以上。
2. 防窥保护能力当前仅支持Phone设备。
3. 本功能通过低功耗传感器智能判断您的周边环境，仅当机主本人浏览指定应用、并存在有他人注视屏幕的风险时，系统才会自动提示。识别过程均在设备端完成，不会泄露用户的隐私。
4. 当人脸处于暗光、强光、逆光等环境，或手机与人脸位置角度过大时，识别成功率可能会受到影响。
5. 如系统检测到身边有人像类物品（如：人物海报）时，可能会进行提示。

## 总结

本文介绍了基于HarmonyOS dlpAntiPeep能力实现应用防窥保护的完整方案，覆盖用户隐私安全、短视频浏览、即时通讯三类典型场景。核心接入步骤为：通过isDlpAntiPeepSwitchOn()确认用户授权、getDlpAntiPeepInfo()获取初始状态on('dlpAntiPeep', callback)实时监听，并在回调中根据DlpAntiPeepStatus枚举值灵活控制敏感信息的显示与隐藏。

接下来，可进一步探索[Device Security Kit（设备安全服务）](../harmonyos-references/device-security-api.md)中的其他安全能力，结合应用的具体业务场景设计更完善的隐私保护方案。

## 示例代码

* [基于防窥保护能力实现敏感信息防窥功能](https://gitcode.com/HarmonyOS_Samples/AntiPeep)
