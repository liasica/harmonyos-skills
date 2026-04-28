---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/runninglock-dev
title: 阻止系统闲时进入睡眠开发指南
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 电源管理 > 运行锁使用指南 > 阻止系统闲时进入睡眠开发指南
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:35c202aabf03d3e85b234af2eea0ff6be1d23a4d953e255e2f65e2be59969e0f
---

## 场景介绍

当计算机在一段时间内没有检测到用户活动（如键盘或鼠标输入）时，系统会自动尝试进入睡眠，使用RunningLockType.BACKGROUND\_USER\_IDLE运行锁，保证在持锁过程中系统不会进入自动睡眠，保证业务正常运行。

## 环境准备

### 环境要求

* 开发工具及配置：

  [DevEco Studio](https://developer.huawei.com/consumer/cn/download/)是HarmonyOS应用开发的推荐IDE工具。开发者可以使用该工具进行开发、调试、打包等操作。请下载安装该工具，并参考[DevEco Studio使用指南](ide-tools-overview.md)中的[创建工程及运行](ide-create-new-project.md)进行基本的操作验证，保证在DevEco Studio可正常运行。
* SDK版本配置：

  RunningLockType.BACKGROUND\_USER\_IDLE类型的运行锁，所需SDK版本为API version 23及以上才可使用。
* HDC配置：

  HDC（HarmonyOS Device Connector）是为开发人员提供的用于调试的命令行工具，通过该工具可以在Windows/Linux/Mac系统上与真实设备或者模拟器进行交互，详细参考[HDC配置](hdc.md)。

### 搭建环境

* 在PC上安装[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)，要求版本在4.1及以上。
* 将public-SDK更新到API version 23或以上，更新SDK的具体操作可参见[更新指南](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/faqs/full-sdk-switch-guide.md)。
* PC安装HDC工具，通过该工具可以在Windows/Linux/Mac系统上与真实设备或者模拟器进行交互。
* 用USB线缆将搭载HarmonyOS的设备连接到PC。

## 开发指导

### 接口说明

1. 介绍自动睡眠与强制睡眠:

   系统睡眠（sleep）指的是计算机系统进入一种低功耗状态，其中大部分硬件组件停止工作，只有最小必要的组件保持运行，以维持系统状态。系统睡眠分为两种主要类型：自动睡眠和强制睡眠。

   （1）自动睡眠：由系统预设的条件或用户配置自动触发的睡眠状态。通常，当计算机在一段时间内没有检测到用户活动（如键盘或鼠标输入）时，系统会自动进入睡眠状态。

   （2）强制睡眠是指用户或应用程序直接命令系统立即进入睡眠状态（如用户合上pc盖子，或主动点击菜单里的睡眠等），而不考虑当前系统状态或用户活动。
2. RunningLockType.BACKGROUND\_USER\_IDLE接口的使用约束和设备差异：

   （1）PC设备创建该类型的运行锁无系统应用权限管控，系统应用和非系统应用均可创建以及使用；非PC设备创建和使用该类型的运行锁要求是系统应用，非PC设备且非系统应用使用该类型锁**功能不生效**，开发时应考虑此约束。

   （2）BACKGROUND\_USER\_IDLE用户闲时任务锁可以阻止系统自动睡眠，但不能阻止系统强制睡眠。因此使用该接口的应用必须监听[进入强制睡眠的公共事件](../harmonyos-references/commoneventmanager-definitions.md#common_event_enter_force_sleep12)，在接收到该公共事件后1s内主动释放掉该锁；是否监听[退出强制睡眠的公共事件](../harmonyos-references/commoneventmanager-definitions.md#common_event_exit_force_sleep12)并重新持有锁，由应用根据具体场景自行决策。

   注意

   进入强制睡眠时系统会做兜底来强制释放该锁，确保系统能正常进入睡眠，公共事件提供给业务测一个感知强制睡眠并处理相应业务的途径。

### 开发步骤

使用RunningLockType.BACKGROUND\_USER\_IDLE运行锁，开发示例如下：

1. 申请使用运行锁所需的权限：ohos.permission.RUNNING\_LOCK。申请流程请参考：[申请应用权限](determine-application-mode.md)。
2. 导入模块。

   ```
   1. // 导入runningLock、commonEventManager模块
   2. import { runningLock } from '@kit.BasicServicesKit';
   3. import { commonEventManager } from '@kit.BasicServicesKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   ```
3. 开发公共事件工具类以及运行锁工具类。

   ```
   1. // CommonEventHelper.ets
   2. import { commonEventManager } from '@kit.BasicServicesKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. type SubscriberInfo = commonEventManager.CommonEventSubscribeInfo;
   6. type Subscriber = commonEventManager.CommonEventSubscriber;
   7. type EventData = commonEventManager.CommonEventData;

   9. // 公共事件工具类，用来创建公共事件监听者以及订阅、取消订阅公共事件
   10. export class CommonEventHelper {
   11. // 创建监听者以及订阅公共事件
   12. public static async subscribeSystemCommonEvent(info: SubscriberInfo,
   13. callback: (data: EventData) => void): Promise<Subscriber | undefined> {
   14. try {
   15. // 创建监听对象
   16. const subscriber: Subscriber = await commonEventManager.createSubscriber(info);
   17. // 订阅指定的公共事件
   18. commonEventManager.subscribe(subscriber, (err: BusinessError, data: EventData): void => {
   19. if (err) {
   20. console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
   21. return;
   22. }
   23. // 监听到公共事件后执行回调
   24. callback(data);
   25. });
   26. // 返回监听者对象
   27. return subscriber;
   28. } catch (error) {
   29. console.error('Failed to subscribe system common event, err: ' + error);
   30. return undefined;
   31. }
   32. }

   34. // 根据传入的监听者取消订阅公共事件
   35. public static async unsubscribeSystemCommonEvent(subscriber: Subscriber | undefined): Promise<boolean> {
   36. try {
   37. // 取消订阅公共事件
   38. commonEventManager.unsubscribe(subscriber, (error: BusinessError): void => {
   39. if (error) {
   40. console.error(`Failed to unsubscribe. Code is ${error.code}, message is ${error.message}`);
   41. } else {
   42. console.info('unsubscribe success');
   43. }
   44. });
   45. return true;
   46. } catch (error) {
   47. console.error('Failed to unsubscribe event, err: ' + error);
   48. return false;
   49. }
   50. }
   51. }
   ```

   ```
   1. // RunningLockUtil.ets
   2. import { runningLock } from '@kit.BasicServicesKit';

   4. // 运行锁工具类，用来创建运行锁、持锁以及释放锁
   5. export class RunningLockUtil {
   6. // 保存运行锁对象
   7. public static recordLock: runningLock.RunningLock | undefined;

   9. public static holdRunningLock(): void {
   10. // 通过isSupport接口查询当前设备是否支持该类型锁
   11. if (!runningLock.isSupported(runningLock.RunningLockType.BACKGROUND_USER_IDLE)) {
   12. console.error('type BACKGROUND_USER_IDLE is not support in the device.');
   13. return;
   14. }
   15. if (RunningLockUtil.recordLock) {
   16. try {
   17. // 持锁时长取决于具体业务场景，锁超时自动释放；这里示例持锁5000ms
   18. RunningLockUtil.recordLock.hold(5000);
   19. console.info('hold running lock success');
   20. } catch (err) {
   21. console.error('hold running lock failed, err: ' + err);
   22. }
   23. } else {
   24. // 创建运行锁，并保存运行锁
   25. RunningLockUtil.createRunningLockAndHold();
   26. }
   27. }

   29. private static async createRunningLockAndHold(): Promise<void> {
   30. try {
   31. const lock = await runningLock.create(
   32. 'running_lock_user_idle',
   33. runningLock.RunningLockType.BACKGROUND_USER_IDLE
   34. );
   35. console.info('create running lock: ' + lock);
   36. RunningLockUtil.recordLock = lock;
   37. // 持锁时长取决于具体业务场景，锁超时自动释放；示例持锁5000ms
   38. lock.hold(5000);
   39. console.info('hold running lock success');
   40. } catch (err) {
   41. console.error('create or hold failed, err: ' + err);
   42. }
   43. }

   45. public static unholdRunningLock(): void {
   46. if (!RunningLockUtil.recordLock) {
   47. console.error('lock is null');
   48. return;
   49. }
   50. try {
   51. // 判断是否持锁，并进行释放操作
   52. if (RunningLockUtil.recordLock.isHolding()) {
   53. RunningLockUtil.recordLock.unhold();
   54. console.info('unhold running lock success');
   55. }
   56. } catch (error) {
   57. console.error('unhold running lock failed, err: ' + error);
   58. }
   59. }
   60. }
   ```
4. 实现业务需要完成的后台系统闲时任务。

   ```
   1. // UserIdleTask.ets
   2. import { CommonEventHelper } from './CommonEventHelper';
   3. import { RunningLockUtil } from './RunningLockUtil';
   4. import { commonEventManager } from '@kit.BasicServicesKit';

   6. // 闲时任务类，可参考下方步骤开发
   7. class UserIdleTask {
   8. private static subscriber: Nullable<commonEventManager.CommonEventSubscriber> = undefined;

   10. // 1、初始化监听公共事件以及其他业务流程，示例只完成监听
   11. public async init(): Promise<void> {
   12. if (UserIdleTask.subscriber === undefined) {
   13. // 监听进入强制睡眠和退出强制睡眠公共事件，并保存监听者对象
   14. UserIdleTask.subscriber = await CommonEventHelper.subscribeSystemCommonEvent(
   15. {
   16. events: [
   17. commonEventManager.Support.COMMON_EVENT_ENTER_FORCE_SLEEP,
   18. commonEventManager.Support.COMMON_EVENT_EXIT_FORCE_SLEEP,
   19. ],
   20. },
   21. this.onReceiveEvent
   22. );
   23. }
   24. }

   26. // 2、持锁后执行任务，任务执行完成后释放锁
   27. public runUserIdleTask(): void {
   28. RunningLockUtil.holdRunningLock();
   29. // 开发者需要自行实现执行系统闲时任务的具体业务逻辑，这里是空实现
   30. console.info('background user idle task run');
   31. RunningLockUtil.unholdRunningLock();
   32. }

   34. // 3、实现收到进入强制睡眠或退出强制睡眠事件的回调函数
   35. private onReceiveEvent(data: commonEventManager.CommonEventData): void {
   36. if (data?.event === commonEventManager.Support.COMMON_EVENT_ENTER_FORCE_SLEEP) {
   37. // 收到进入强制睡眠公共事件后需要在1s内暂停或结束任务（如有），然后释放锁
   38. RunningLockUtil.unholdRunningLock();
   39. }
   40. if (data?.event === commonEventManager.Support.COMMON_EVENT_EXIT_FORCE_SLEEP) {
   41. // 收到退出强制睡眠公共事件后由业务自行决策是否需要继续执行未完成的任务（如有），示例不做处理
   42. }
   43. }
   44. }

   46. // 创建并执行任务
   47. function main() {
   48. let task: UserIdleTask = new UserIdleTask();
   49. task.init();
   50. task.runUserIdleTask();
   51. }
   ```
