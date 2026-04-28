---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/stationary-guidelines
title: Stationary开发指导
breadcrumb: 指南 > 系统 > 硬件 > Multimodal Awareness Kit（多模态融合感知服务） > Stationary开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c2a499694dbab934d84dd62667e3718d083cac80b005f601e9c0fe1278c0fead
---

## 场景介绍

当应用需要获取当前设备状态时，可以调用Stationary模块，例如：需要判断当前设备处于绝对静止状态或者相对静止状态。

详细的接口介绍请参考[@ohos.stationary (设备状态感知框架)](../harmonyos-references/js-apis-stationary.md)。

## 设备状态类型参数说明

| 名称 | 描述 |
| --- | --- |
| still | 绝对静止。 |
| relativeStill | 相对静止。 |

## 订阅设备状态事件参数说明

| 变量 | 值 | 说明 |
| --- | --- | --- |
| ENTER | 1 | 订阅进入事件。 |
| EXIT | 2 | 订阅退出事件。 |
| ENTER\_EXIT | 3 | 订阅进入和退出事件。 |

## 返回设备状态参数说明

| 变量 | 值 | 说明 |
| --- | --- | --- |
| ENTER | 1 | 返回进入状态。 |
| EXIT | 2 | 返回退出状态。 |

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| on(activity: ActivityType, event: ActivityEvent, reportLatencyNs: number, callback: Callback<ActivityResponse>): void | 订阅设备状态，结果通过callback返回。 |
| once(activity: ActivityType, callback: Callback<ActivityResponse>): void | 查询设备状态，结果通过callback返回。 |
| off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void | 取消订阅设备状态。 |

## 约束与限制

设备需要支持加速度传感器。

目前只提供了算法框架，api接口测试框架的调用返回结果为:data={"type":3,"value":-1};

如需相对静止和绝对静止能力，则具体算法需要开发者自己在device\_status/libs/src/algorithm实现，可参考案例如下：

```
1. algoPara_.resultantAcc =
2. sqrt((algoPara_.x * algoPara_.x) + (algoPara_.y * algoPara_.y) + (algoPara_.z * algoPara_.z));
3. if ((algoPara_.resultantAcc > RESULTANT_ACC_LOW_THRHD) && (algoPara_.resultantAcc < RESULTANT_ACC_UP_THRHD)) {
4. if (state_ == STILL) {
5. return;
6. }
7. counter_--;
8. if (counter_ == 0) {
9. counter_ = COUNTER_THRESHOLD;
10. UpdateStateAndReport(VALUE_ENTER, STILL, TYPE_ABSOLUTE_STILL);
11. }
12. } else {
13. counter_ = COUNTER_THRESHOLD;
14. if (state_ == UNSTILL) {
15. return;
16. }
17. UpdateStateAndReport(VALUE_EXIT, UNSTILL, TYPE_ABSOLUTE_STILL);
18. }
```

## 开发步骤

1. 订阅绝对静止的进入事件，1秒上报一次。

   ```
   1. import { stationary } from '@kit.MultimodalAwarenessKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. let reportLatencyNs = 1000000000; // 单位：纳秒
   5. try {
   6. stationary.on('still', stationary.ActivityEvent.ENTER, reportLatencyNs, (data) => {
   7. console.info('data=' + JSON.stringify(data));
   8. })
   9. } catch (error) {
   10. let message = (error as BusinessError).message;
   11. console.error('stationary on failed:' + message);
   12. }
   ```
2. 查询绝对静止状态的进入事件。

   ```
   1. import { stationary } from '@kit.MultimodalAwarenessKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. try {
   5. stationary.once('still', (data) => {
   6. console.info('data=' + JSON.stringify(data));
   7. })
   8. } catch (error) {
   9. let message = (error as BusinessError).message;
   10. console.error('stationary once failed:' + message);
   11. }
   ```
3. 取消订阅绝对静止状态的进入事件。

   ```
   1. import { stationary } from '@kit.MultimodalAwarenessKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. try {
   5. stationary.off('still', stationary.ActivityEvent.ENTER, (data) => {
   6. console.info('data=' + JSON.stringify(data));
   7. })
   8. } catch (error) {
   9. let message = (error as BusinessError).message;
   10. console.error('stationary off failed:' + message);
   11. }
   ```
