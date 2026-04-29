---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-stop-guard-strategy
title: 停止策略
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 守护策略管理 > 停止策略
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:50b3df128d2c9f526e78b7ddb042ed8f957314544597f46caeec7c83ef094e54
---

## 场景介绍

当用户希望停止某个管控规则时，可以调用停止管控策略的接口。根据参数中传入的策略名，应用可以停止对应管控策略。一旦策略被停止，系统将不再根据该规则对用户的屏幕使用行为进行监管。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/r8Wf2iSZRMi3juLWjTTppg/zh-cn_image_0000002558765674.png?HW-CC-KV=V1&HW-CC-Date=20260429T054029Z&HW-CC-Expire=86400&HW-CC-Sign=CBE2910596275983897AAB4B041AF090AE0BA963036FDFBD7AAFB7761BF77CBE)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/W58_BSlzTF-jVnNmj7L_PQ/zh-cn_image_0000002558606018.png?HW-CC-KV=V1&HW-CC-Date=20260429T054029Z&HW-CC-Expire=86400&HW-CC-Sign=F6C869D20FBAB5BE04D9ADDF51B5F388068FFDB96F748EDF683C13E99C897D68)

流程说明：

1. 应用继承TimeGuardExtensionAbility，实现onStop方法，此步非必需。
2. 应用调用停止管控策略的接口，会拉起健康使用设备查询本应用是否已申请权限、用户是否已给本应用授权。
3. 若没有权限，则抛出相应错误码。若有权限，则解析参数中传入的策略名称，判断策略是否存在。
4. 若策略不存在，则抛出相应错误码；若存在，则查询该策略是否正在执行。
5. 若停止策略时正在执行策略，则策略会正常停止，健康使用设备会记录策略停止状态；若停止策略时策略并未执行，该接口将抛出策略未在执行中的错误码。
6. 策略生效期间停止策略，会拉起extension进程，执行TimeGuardExtensionAbility的onStop回调。在非策略生效期间停止策略，不会触发onStop回调。
7. 停止该策略后，若该应用不存在任何启动状态的策略，则该应用被设置为可卸载。
8. 停止该策略后，若设备中不存在任何启动状态的策略，则系统时间设置为可修改。

## 接口说明

停止策略的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [stopGuardStrategy](../harmonyos-references/screentimeguard-guardservice.md#stopguardstrategy)(strategyName: string): Promise<void> | 根据策略名称，停止其管控策略。 |
| [onStop](../harmonyos-references/screentimeguard-timeguardextensionability.md#onstop)(strategyName: string): Promise<void> | 在策略结束时执行特定逻辑。 |

## 开发前提

停止管控策略需要申请用户授权，请先参考[请求用户授权](screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { guardService, TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 继承TimeGuardExtensionAbility，重写onStop回调。

   ```
   1. export default class EntryAbility extends TimeGuardExtensionAbility {
   2. async onStop(strategyName: string): Promise<void> {
   3. hilog.info(0x0000, 'test --- onStop', strategyName);
   4. }
   5. }
   ```
3. 调用stopGuardStrategy，停止管控策略。

   ```
   1. async function testStopGuardStrategy() {
   2. try {
   3. const strategyName = "TestStrategy";
   4. await guardService.stopGuardStrategy(strategyName);
   5. } catch (err) {
   6. const message = (err as BusinessError).message;
   7. const code = (err as BusinessError).code;
   8. hilog.error(0x0000, `ScreenTimeGuard:stopGuardStrategy`, `stopGuardStrategy failed with error code: ${code}, message: ${message}`);
   9. }
   10. }
   ```
