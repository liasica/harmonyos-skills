---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-check-application-start
title: 主动获取HiCar的连接状态
breadcrumb: 指南 > 系统 > 硬件 > Car Kit（车服务） > 获取HiCar连接状态 > 主动获取HiCar的连接状态
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:68f3f3419b2d5e3025d9299973973e4fd8f6e49548137898b34d7fde0341a492
---

## 场景介绍

生态应用可以通过主动获取智慧出行连接状态接口来获取HiCar的连接状态（如：判断应用是否在HiCar上拉起）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/CBrGGl-fQgenYKWfLi-xyQ/zh-cn_image_0000002558764970.png?HW-CC-KV=V1&HW-CC-Date=20260429T053329Z&HW-CC-Expire=86400&HW-CC-Sign=24A1640280C2EE13BC7EA6027DCA6AB487F0B5C53FDD2576A056315F55E35005)

## 接口说明

获取HiCar连接状态的接口如下：

| 接口名 | 描述 |
| --- | --- |
| [getSmartMobilityStatus](../harmonyos-references/car-smartmobilitycommon.md#getsmartmobilitystatus) | 获取智慧出行连接状态。 |

### SmartMobilityInfo事件名说明

SmartMobilityInfo状态（status）取值如下：

| **编号** | **状态** | **描述** |
| --- | --- | --- |
| 0 | IDLE | 空闲态。 |
| 1 | RUNNING | 运行态。 |

SmartMobilityInfo业务类型（type）取值如下：

| **编号** | 业务类型 | **描述** |
| --- | --- | --- |
| 0 | HICAR | HiCar。 |
| 1 | SUPER\_LAUNCHER | 超级桌面。 |
| 2 | CAR\_HOP | 流转。 |

SmartMobilityInfo业务数据（data）参数如下：

| **编号** | 参数 | **描述** |
| --- | --- | --- |
| 0 | DEVICE\_TYPE | 设备类型。 |
| 1 | DISPLAY\_ID | 业务所在的虚拟屏ID。 |
| 2 | IS\_PHONE\_DESKTOP | 当前是否在HiCar上显示手机桌面（仅在HiCar业务中展示）。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { smartMobilityCommon } from '@kit.CarKit';
   2. import { UIAbility } from '@kit.AbilityKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 查询智慧出行连接状态。

   应用在适配HiCar时，可以实时查询接口来获取智慧出行连接状态（如：判断应用是否在HiCar上）。

   ```
   1. export default class EntryAbility extends UIAbility {
   2. isAppOnHiCar(): boolean {
   3. try {
   4. // 应用所在的屏幕id
   5. const currentDisplayId = this.context.config.displayId;
   6. // 获取SmartMobilityAwareness实例
   7. let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
   8. // 获取当前智慧出行连接状态
   9. let info: smartMobilityCommon.SmartMobilityInfo =
   10. awareness.getSmartMobilityStatus(smartMobilityCommon.SmartMobilityType.HICAR);
   11. const deviceDisplayId = Number(info.data["DISPLAY_ID"]);
   12. if (currentDisplayId === deviceDisplayId) {
   13. // 表示应用在对应的设备屏幕上
   14. hilog.info(0x0000, 'testTag', 'app in on device screen');
   15. return true;
   16. }
   17. } catch (e) {
   18. // 捕获接口调用异常时的错误码并做相应处理
   19. hilog.error(0x0000, 'testTag', `get smart mobility status error, error code: ${e?.code}`);
   20. }
   21. return false;
   22. }
   23. }
   ```
