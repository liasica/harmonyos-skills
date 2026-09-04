---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/aodnavigation-development-guidance
title: 接入熄屏导航
breadcrumb: 指南 > 系统 > 硬件 > AOD Navigation Kit（熄屏导航服务） > 接入熄屏导航
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fadfa23cc6822298fe647bda23676c906940f169372a98a091e665a708aeaf54
---

## 概述

AOD Navigation Kit提供应用接入熄屏导航的能力，支持低功耗导航业务代理能力。该服务专为户外徒步、骑行、跑步等场景打造，用户无需频繁解锁亮屏即可掌握导航关键信息，在确保导航实时性的同时有效降低设备功耗，助力户外探索类应用快速集成熄屏导航能力。

### 场景介绍

接入熄屏导航能力的应用可在设备熄屏后，在设备熄屏界面实时展示行进路线、运动轨迹、里程及耗时等核心信息。应用可自定义显示的数据项，当前支持12种数据选项供灵活配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/tZSUynbeSxy6FF9DW0rk3w/zh-cn_image_0000002742003619.png)

### 开发流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/eXwF5-TsRSC_b3qnQNj8SA/zh-cn_image_0000002712404632.png)

流程说明：

1. 用户使用应用导航功能：

   1.1. 设备能力差异化判断，调用[isAodNaviSupported](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanagerisaodnavisupported)接口判断当前设备是否支持熄屏导航功能及[getAodNaviExtendCapabilities](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanagergetaodnaviextendcapabilities)接口获取当前设备上支持的扩展能力集，在不支持的设备上进行业务隔离

   1.2. 熄屏导航初始化配置：调用[setupAodNaviConfig](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanagersetupaodnaviconfig)接口进行熄屏导航功能初始化配置。

   1.3. 设置规划轨迹路线，调用[setPlanRouteToAod](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanagersetplanroutetoaod)将规划轨迹路线下发给AOD Navigation Kit。
2. 设备熄屏进入熄屏导航：

   2.1. 应用接收到对应熄屏导航事件[AodNaviEventInfo](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavieventinfo)回调后，下发设备亮屏期间应用产生的轨迹和导航数据给AOD Navigation Kit。

   2.2. 应用根据自身初始化配置进行响应，若应用休眠策略为休眠时，则释放长时任务，否则调用[updateAodViewData](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanagerupdateaodviewdata)定时刷新熄屏导航界面数据。

   2.3. 若应用休眠策略为休眠时，熄屏导航期间满足条件时会回调对应导航事件[AodNaviEventInfo](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavieventinfo)（熄屏导航数据缓存或语音播报事件）给应用，应用接收后需进行数据合并或者语音播报。
3. 设备亮屏退出熄屏导航：应用接收到对应熄屏导航事件[AodNaviEventInfo](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavieventinfo)回调后，根据初始化配置进行事件响应，若应用休眠策略为休眠时，则进行数据合并并恢复长时任务，否则停止调用[updateAodViewData](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanagerupdateaodviewdata)数据刷新接口。
4. 暂停或者恢复应用导航时，应用需要调用[updateAppRecordStatus](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanagerupdateapprecordstatus)接口将状态更新至AOD Navigation Kit，若应用导航处于暂停状态时，设备熄屏将不会进入熄屏导航状态。
5. 退出应用导航时，应用需要调用[offAodNaviEvent](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanageroffaodnavievent)解注册熄屏导航事件监听。

## 开发步骤

1. 导入aodNaviManager模块。

   ```typescript
   import { abilityAccessCtrl, common } from '@kit.AbilityKit';
   import { aodNaviManager } from '@kit.AODNavigationKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 设备能力差异化判断。

   1. 熄屏循迹导航能力强依赖设备能力，非所有设备支持，应用可以通过[isAodNaviSupported](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanagerisaodnavisupported)接口获取当前设备是否支持AOD熄屏循迹导航。

      ```typescript
      // 首次进入申请定位权限
      let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      await atManager.requestPermissionsFromUser(this.getUIContext().getHostContext() as common.UIAbilityContext,
        ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'])
      // 检查设备是否支持熄屏导航
      const isSupported: boolean = aodNaviManager.isAodNaviSupported();
      hilog.info(0x0000, 'aodNavigationSample', 'Succeeded in checking whether AOD navigation is supported, supported: %{public}s', isSupported);
      ```
   2. 部分能力子项依赖产品特定器件，非所有设备支持，应用可以通过[getAodNaviExtendCapabilities](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanagergetaodnaviextendcapabilities)获取当前设备支持能力子项列表。

      ```typescript
      // 获取设备扩展能力列表
      const capabilities: Array<aodNaviManager.AodNaviExtendDataType> =
        aodNaviManager.getAodNaviExtendCapabilities();
      hilog.info(0x0000, 'aodNavigationSample', 'Succeeded in getting AOD navigation extend capabilities, capabilities: %{public}s', JSON.stringify(capabilities));
      ```
3. 调用[isAodNaviSwitchEnabled](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanagerisaodnaviswitchenabled)接口判断熄屏导航功能开关（操作路径：“设置 > 桌面和个性化 > 熄屏显示设置 > 熄屏导航”）是否开启。

   ```typescript
   // 检查熄屏导航开关是否已启用
   try {
     const enabled: boolean = await aodNaviManager.isAodNaviSwitchEnabled();
     hilog.info(0x0000, 'aodNavigationSample', 'Succeeded in checking whether AOD navigation switch is enabled, enabled: %{public}s', enabled);
   } catch (error) {
     hilog.error(0x0000, 'aodNavigationSample', 'Failed to check whether AOD navigation switch is enabled: %{public}d %{public}s', error.code, error.message);
   }
   ```
4. 调用[setupAodNaviConfig](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanagersetupaodnaviconfig)接口进行熄屏导航功能初始化配置。

   ```typescript
   try {
     const config: aodNaviManager.AodNaviConfig = {
       // 设备熄屏应用休眠策略：配置设备熄屏后应用休眠策略为休眠
       aliveStrategy: aodNaviManager.AodNaviAliveStrategy.HIBERNATE,
       // 设备熄屏界面显示参数项
       aodViewDataConfig: {
         aodViewDataCount: 4,
         aodViewDataTypes: [
           aodNaviManager.AodNaviBasicDataType.DISTANCE,
           aodNaviManager.AodNaviBasicDataType.STEPS,
           aodNaviManager.AodNaviBasicDataType.CURRENT_SPEED,
           aodNaviManager.AodNaviBasicDataType.OVERALL_ELAPSED_TIME
         ]
       },
       // 语音播报参数项
       aodVoiceBroadcastConfig: {
         distance: 1000,
         timeInterval: 60,
         enableGpsBroadcast: true
       },
       // 业务代理数据项
       aodProxyDataTypes: [
         aodNaviManager.AodNaviBasicDataType.DISTANCE,
         aodNaviManager.AodNaviBasicDataType.STEPS,
         aodNaviManager.AodNaviBasicDataType.CURRENT_SPEED,
         aodNaviManager.AodNaviBasicDataType.OVERALL_ELAPSED_TIME
       ]
     };
     // 初始化接入配置
     await aodNaviManager.setupAodNaviConfig(config);
     hilog.info(0x0000, 'aodNavigationSample', 'Succeeded in setting up AOD navigation config.');
   } catch (error) {
     hilog.error(0x0000, 'aodNavigationSample', 'Failed to set up AOD navigation config: %{public}d %{public}s', error.code, error.message);
   }
   ```
5. 调用[onAodNaviEvent](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanageronaodnavievent)接口注册熄屏导航事件监听，系统会将具体事件信息[AodNaviEventInfo](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavieventinfo)回调给应用，应用根据系统回调事件信息进行对应任务处理。回调事件类型详见[AodNaviEventType](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavieventtype)。

   ```typescript
   try {
     aodNaviManager.onAodNaviEvent((eventInfo: aodNaviManager.AodNaviEventInfo) => {
       hilog.info(0x0000, 'aodNavigationSample', 'Received AOD navigation event: eventType: %{public}d, eventId: %{public}s', eventInfo.eventType, eventInfo.eventId);
       switch (eventInfo.eventType) {
         // 进入熄屏导航事件回调
         case aodNaviManager.AodNaviEventType.AOD_NAVI_ENTER:
           this.handleNaviEnter(eventInfo);
           break;
         // 退出熄屏导航事件回调
         case aodNaviManager.AodNaviEventType.AOD_NAVI_EXIT:
           this.handleNaviExit(eventInfo);
           break;
         // 语音播报事件回调
         case aodNaviManager.AodNaviEventType.AOD_NAVI_VOICE_BROADCAST:
           this.handleVoiceBroadcast(eventInfo);
           break;
         // 数据缓存事件回调
         case aodNaviManager.AodNaviEventType.AOD_NAVI_DATA_CACHE:
           this.handleDataCache(eventInfo);
           break;
       }
     });
     hilog.info(0x0000, 'aodNavigationSample', 'onAodNaviEvent success.');
   } catch (error) {
     hilog.error(0x0000, 'aodNavigationSample', 'onAodNaviEvent error: %{public}d %{public}s', error.code, error.message);
   }

   // 处理进入熄屏导航事件
   async handleNaviEnter(eventInfo: aodNaviManager.AodNaviEventInfo) {
     let historyRoutes: aodNaviManager.HistoryRoute[] = [
       { timestamp: 1234567890, longitude: 116.404, latitude: 39.915 },
       { timestamp: 1234567891, longitude: 116.405, latitude: 39.916 }
     ];

     let aodNaviData: aodNaviManager.AodNaviData = {
       timestamp: Date.now() / 1000,
       distance: 1000,
       steps: 1500,
       currentSpeed: 5.5
     };

     let aodNaviInteractData: aodNaviManager.AodNaviInteractData = {
       historyRoutes: historyRoutes,
       aodNaviData: aodNaviData
     };

     try {
       await aodNaviManager.setNaviDataToAod(eventInfo.eventId, aodNaviInteractData);
       hilog.info(0x0000, 'aodnavigationSample', 'Succeeded in setting navigation data to AOD.');
     } catch (error) {
       hilog.error(0x0000, 'aodnavigationSample', 'Failed to set navigation data to AOD: %{public}d %{public}s', error.code, error.message);
     }
     // 如果应用休眠策略选择保活，则需要定时刷新熄屏导航视图数据，否则不需要以下代码
     const aodViewData: aodNaviManager.AodViewData = {
       "distance": 5.5,
       "steps": 5500,
       "currentSpeed": 11.0,
       "overallAvgSpeed": 12
     };

     try {
       await aodNaviManager.updateAodViewData(aodViewData);
       hilog.info(0x0000, 'aodNavigationSample', 'Succeeded in updating AOD view data.');
     } catch (error) {
       hilog.error(0x0000, 'aodNavigationSample', 'Failed to update AOD view data: %{public}d %{public}s', error.code, error.message);
     }
   }

   // 处理熄屏导航退出事件
   async handleNaviExit(eventInfo: aodNaviManager.AodNaviEventInfo) {
     hilog.info(0x0000, 'aodNavigationSample', 'handleNaviExit');
   }

   // 处理语音播报事件
   async handleVoiceBroadcast(eventInfo: aodNaviManager.AodNaviEventInfo) {
     hilog.info(0x0000, 'aodNavigationSample', 'handleVoiceBroadcast');
   }

   // 处理数据缓存事件
   async handleDataCache(eventInfo: aodNaviManager.AodNaviEventInfo) {
     hilog.info(0x0000, 'aodNavigationSample', 'handleDataCache');
   }
   ```
6. 调用[setPlanRouteToAod](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanagersetplanroutetoaod)接口下发规划轨迹路线至AOD Navigation Kit用于熄屏界面显示。

   ```typescript
   try {
     // 规划轨迹路线点
     const planRoutes: Array<aodNaviManager.PlanRoute> = [
       { longitude: 116.404, latitude: 39.915 },
       { longitude: 116.414, latitude: 39.925 },
       { longitude: 116.424, latitude: 39.935 }
     ];
     // 标记点
     const markPoints: Array<aodNaviManager.MarkPoint> = [
       { name: '起点', longitude: 116.404, latitude: 39.915 },
       { name: '终点', longitude: 116.424, latitude: 39.935 }
     ];

     await aodNaviManager.setPlanRouteToAod(planRoutes, markPoints);
     hilog.info(0x0000, 'aodNavigationSample', 'Succeeded in setting plan route to AOD.');
   } catch (error) {
     hilog.error(0x0000, 'aodNavigationSample', 'Failed to set plan route to AOD: %{public}d %{public}s', error.code, error.message);
   }
   ```
7. 当设备从亮屏切换至熄屏时，应用会收到AOD\_NAVI\_ENTER回调事件，此时应调用[setNaviDataToAod](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanagersetnavidatatoaod)接口，将设备亮屏阶段应用产生的轨迹及导航数据同步至AOD Navigation Kit，以支持熄屏时循迹导航功能的正常显示。

   ```typescript
   try {
     await aodNaviManager.setNaviDataToAod(eventInfo.eventId, aodNaviInteractData);
     hilog.info(0x0000, 'aodnavigationSample', 'Succeeded in setting navigation data to AOD.');
   } catch (error) {
     hilog.error(0x0000, 'aodnavigationSample', 'Failed to set navigation data to AOD: %{public}d %{public}s', error.code, error.message);
   }
   ```
8. 调用[updateAodViewData](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanagerupdateaodviewdata)更新熄屏导航界面视图数据。

   当应用休眠策略为保活时，在设备从亮屏切换至熄屏且应用收到AOD\_NAVI\_ENTER回调后，应用需定时调用此方法以更新熄屏导航视图数据。请注意，定时刷新的频率不得高于1秒/次。

   ```typescript
   const aodViewData: aodNaviManager.AodViewData = {
     "distance": 5000,
     "steps": 2000,
     "currentSpeed": 5.5
   };

   try {
     await aodNaviManager.updateAodViewData(aodViewData);
     hilog.info(0x0000, 'aodNavigationSample', 'Succeeded in updating AOD view data.');
   } catch (error) {
     hilog.error(0x0000, 'aodNavigationSample', 'Failed to update AOD view data: %{public}d %{public}s', error.code, error.message);
   }
   ```
9. 调用[updateAppRecordStatus](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanagerupdateapprecordstatus)更新应用导航记录状态。

   在应用暂停状态下，AOD Navigation Kit需同步暂停业务代理的计算，且熄屏界面不展示内容。因此，应用处于暂停或恢复状态时，必须将当前状态同步至AOD Navigation Kit，以确保显示与计算状态的一致性。

   ```typescript
   try {
     const recordStatus: aodNaviManager.AppRecordStatus = aodNaviManager.AppRecordStatus.RECORDING;
     await aodNaviManager.updateAppRecordStatus(recordStatus);
     hilog.info(0x0000, 'aodNavigationSample', 'Succeeded in updating app record status');
   } catch (error) {
     hilog.error(0x0000, 'aodNavigationSample', 'Failed to update app record status: %{public}d %{public}s', error.code, error.message);
   }
   ```
10. 应用退出或结束导航时，需调用[offAodNaviEvent](../harmonyos-references/aodnavigation-aodnavimanager.md#aodnavimanageroffaodnavievent)解注册熄屏导航事件监听，以避免无效的资源占用。

    ```typescript
    try {
      aodNaviManager.offAodNaviEvent();
      hilog.info(0x0000, 'aodnavigationSample', 'Succeeded in stopping AOD navigation event listener.');
    } catch (error) {
      hilog.error(0x0000, 'aodNavigationSample', 'Failed to stop AOD navigation event listener:  %{public}d %{public}s', error.code, error.message);
    }
    ```
