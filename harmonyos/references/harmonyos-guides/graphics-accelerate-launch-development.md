---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-development
title: 实现游戏启动加速
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏启动加速服务 > 秒级启动 > 实现游戏启动加速
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1462c00b87ddca60ab82c63d4bd8b378be35f979e0cab4836cc4549dfd65ae51
---

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/60OZ566jRKSvwXRX_r9JWQ/zh-cn_image_0000002589245035.png?HW-CC-KV=V1&HW-CC-Date=20260429T053632Z&HW-CC-Expire=86400&HW-CC-Sign=BC8CA1670FCE1E979F99BD46EAD6001CB371A17EF5E25A20C5FBEA3DB76A9B99)

1. 用户启动游戏。
2. 游戏在onCreate生命周期中调用[setSupportedProcessCache](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextsetsupportedprocesscache12)接口，设置游戏支持缓存后快速启动。

   说明

   部分机型不支持设置进程资源的缓存，因此在调用[setSupportedProcessCache](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextsetsupportedprocesscache12)接口时需加try catch捕获异常。
3. 用户上划退出游戏。
4. 在onWindowStageWillDestroy生命周期中，游戏调用[isLaunchMirrorEnabled](../harmonyos-references/graphics-accelerate-launchacceleration.md#islaunchmirrorenabled)接口向游戏启动加速服务查询游戏内存镜像功能是否开启。若已开启，ArkTS侧通知游戏引擎将当前场景切换至登录页，引擎完成场景切换后将结果回传ArkTS侧。若场景切换失败或超时，则调用[setSupportedProcessCache](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextsetsupportedprocesscache12)接口，取消游戏对缓存后快速启动的支持。

   说明

   建议开发者切换场景时，将场景切换至游戏登录界面并设置最大超时时间5s。
5. 在onDestroy生命周期中，游戏再次调用[isLaunchMirrorEnabled](../harmonyos-references/graphics-accelerate-launchacceleration.md#islaunchmirrorenabled)接口确认内存镜像功能状态。若未开启，则执行引擎析构流程，游戏进程随即退出。
6. 用户重新启动游戏。
7. 游戏根据是否存在内存镜像决定启动方式：若存在内存镜像，系统将此前换出至磁盘的游戏对象重新换入到内存，实现秒级启动；若不存在内存镜像，则按正常流程启动游戏。

   说明

   根据上架审核规则，建议游戏秒级启动时增加游戏健康公告闪屏，然后再进入内存镜像界面，详细操作可参考[Codelab](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_LaunchAcceleration-ArkTS)示例工程。

## 生命周期

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/5oGfEVfSSXOB1ONL52FBfA/zh-cn_image_0000002558765230.png?HW-CC-KV=V1&HW-CC-Date=20260429T053632Z&HW-CC-Expire=86400&HW-CC-Sign=BC9378ABFE4D7B8D0E2EAAC7C2A3765A8CCB5434EB97BC1CC23C1C0BBCF24891)

* 游戏冷启动场景

  游戏进程会依次创建AbilityStage、UIAbility以及WindowStage，完成应用与界面的初始化。
* 游戏秒级启动场景

  当秒级启动能力开启后，用户上划移除游戏时，系统会依次销毁WindowStage和UIAbility对象，随后对游戏进程进行深度冻结。在此过程中，系统会将游戏进程中的大部分对象换出至磁盘，仅保留少量关键对象驻留在内存中，以降低内存占用。

  在触发游戏秒级启动时，系统会将此前换出到磁盘的游戏对象重新换入内存，同时游戏进程会重新创建UIAbility和WindowStage对象，从而实现快速恢复与启动。

## 接口说明

具体API说明请详见[接口文档](../harmonyos-references/graphics-accelerate-launchacceleration.md)。

| 接口名 | 描述 |
| --- | --- |
| [isLaunchMirrorEnabled](../harmonyos-references/graphics-accelerate-launchacceleration.md#islaunchmirrorenabled)(): boolean | 查询游戏的内存镜像功能是否开启。 |

## 开发步骤

说明

本节主要介绍秒级启动的核心流程，完整的开发步骤和注意事项请参见[Codelab开发指导](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_LaunchAcceleration-ArkTS)。

1. 导入Graphics Accelerate Kit模块。

   ```
   1. import { launchAcceleration } from '@kit.GraphicsAccelerateKit';
   ```
2. 游戏启动时，在onCreate生命周期中调用[setSupportedProcessCache](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextsetsupportedprocesscache12)接口，设置游戏支持缓存后快速启动。

   ```
   1. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   2. if (canIUse("SystemCapability.GraphicsGame.LaunchAcceleration")) {  // 兼容性：通过canIUse()校验设备是否支持启动加速服务
   3. try {
   4. this.context.getApplicationContext().setSupportedProcessCache(true);
   5. } catch (error) {
   6. let code = (error as BusinessError).code;
   7. let message = (error as BusinessError).message;
   8. console.error(`setSupportedProcessCache fail, code: ${code}, msg: ${message}`);
   9. }
   10. }
   11. }
   ```
3. 游戏退出时，调用[isLaunchMirrorEnabled](../harmonyos-references/graphics-accelerate-launchacceleration.md#islaunchmirrorenabled)接口，查询游戏内存镜像功能是否开启。若已开启，游戏先切换场景，游戏需在onWindowStageWillDestroy生命周期中进行场景切换，建议开发者将场景切换至游戏登录界面，并在onDestroy生命周期中取消游戏引擎的销毁步骤，系统在退出游戏前自动制作内存镜像，制作内存镜像大概需要4s。

   说明

   * 游戏启动加速服务制作游戏内存镜像需要4s，若在4s内再次进入游戏，则秒级启动不生效，启动方式为正常冷启动。
   * 游戏本次基于内存镜像启动加速，若在10s内上划退出，下一次启动不会加速，因为系统DFR（Design for Reliability，可靠性设计）保护机制，防止游戏快启后无法使用。
   * 系统将结合当前设备的游戏热度、内存镜像数、当日磁盘换出量综合判定是否开启内存镜像功能。

   ```
   1. onWindowStageWillDestroy(): void {
   2. if (canIUse("SystemCapability.GraphicsGame.LaunchAcceleration")) {  // 兼容性：通过canIUse()校验设备是否支持启动加速服务
   3. let enable = launchAcceleration.isLaunchMirrorEnabled()
   4. if (enable) {
   5. // 切换场景的代码逻辑
   6. }
   7. }
   8. }
   9. onDestroy(): void {
   10. if (canIUse("SystemCapability.GraphicsGame.LaunchAcceleration")) {  // 兼容性：通过canIUse()校验设备是否支持启动加速服务
   11. let enable = launchAcceleration.isLaunchMirrorEnabled()
   12. if (!enable) {
   13. // 若未使能，才进行游戏引擎的销毁
   14. }
   15. }
   16. }
   ```
