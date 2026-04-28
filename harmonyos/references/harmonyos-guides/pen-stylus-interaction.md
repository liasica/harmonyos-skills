---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-stylus-interaction
title: 接入手写交互
breadcrumb: 指南 > 系统 > 硬件 > Pen Kit（手写笔服务） > 手写功能开发 > 接入手写交互
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ced2c1558b16437900ec154c89c27f89ba37e40d08143ab134b0ae5c3eae5b92
---

接入手写交互功能，对于需要接入支持双击/轻捏功能的手写笔的第三方应用，可以通过调用下面相应接口来监听手写笔双击/轻捏事件，从而触发自身应用内部回调，来执行指定操作。

## 接口说明

| 类名 | 接口名 | 说明 |
| --- | --- | --- |
| stylusInteraction | [on](../harmonyos-references/pen-stylusinteraction.md#stylusinteractiononsqueeze)(type: 'squeeze', receiver: Callback<[SqueezeEvent](../harmonyos-references/pen-stylusinteraction.md#squeezeevent)>): void | 监听手写笔轻捏事件。 |
| stylusInteraction | [off](../harmonyos-references/pen-stylusinteraction.md#stylusinteractionoffsqueeze)(type: 'squeeze', receiver?: Callback<[SqueezeEvent](../harmonyos-references/pen-stylusinteraction.md#squeezeevent)>): void | 取消监听手写笔轻捏事件。 |
| stylusInteraction | [on](../harmonyos-references/pen-stylusinteraction.md#stylusinteractionondoubletap)(type: 'doubleTap', receiver: Callback<[DoubleTapEvent](../harmonyos-references/pen-stylusinteraction.md#doubletapevent)>): void | 监听手写笔双击事件。 |
| stylusInteraction | [off](../harmonyos-references/pen-stylusinteraction.md#stylusinteractionoffdoubletap)(type: 'doubleTap', receiver?: Callback<[DoubleTapEvent](../harmonyos-references/pen-stylusinteraction.md#doubletapevent)>): void | 取消监听手写笔双击事件。 |

## 手写笔轻捏事件

1. 导入相关模块。

   ```
   1. import { stylusInteraction } from '@kit.Penkit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 监听手写笔轻捏事件。

   ```
   1. try {
   2. stylusInteraction.on('squeeze', (event: stylusInteraction.SqueezeEvent) => {
   3. console.info(`got squeeze event, time: ${event.timestamp}`);
   4. });
   5. } catch (err) {
   6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   7. }
   ```
3. 取消监听手写笔轻捏事件。

   ```
   1. try {
   2. stylusInteraction.off('squeeze', (event: stylusInteraction.SqueezeEvent) => {
   3. console.info(`off squeeze event, time: ${event.timestamp}`);
   4. });
   5. } catch (err) {
   6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   7. }
   ```

## 手写笔双击事件

1.导入相关模块。

```
1. import { stylusInteraction } from '@kit.Penkit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

2.监听手写笔双击事件。

```
1. try {
2. stylusInteraction.on('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
3. console.info(`got doubleTap event, time: ${event.timestamp}`);
4. });
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

3.取消监听手写笔双击事件。

```
1. try {
2. stylusInteraction.off('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
3. console.info(`off doubleTap event, time: ${event.timestamp}`);
4. });
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```
