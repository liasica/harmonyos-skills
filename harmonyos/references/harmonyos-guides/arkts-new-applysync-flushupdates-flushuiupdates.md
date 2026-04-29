---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-applysync-flushupdates-flushuiupdates
title: applySync/flushUpdates/flushUIUpdates接口：同步刷新
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 辅助接口 > applySync/flushUpdates/flushUIUpdates接口：同步刷新
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9bfc894ae30110b937fb7d5be7fcf761122eab37b28112f4bac16bdbf5c5494a
---

为了实现状态管理V2与[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)等动效的同步刷新，开发者可以使用[applySync](../harmonyos-references/js-apis-statemanagement.md#applysync22)、[flushUpdates](../harmonyos-references/js-apis-statemanagement.md#flushupdates22)或[flushUIUpdates](../harmonyos-references/js-apis-statemanagement.md#flushuiupdates22)接口。

说明

从API version 22开始，开发者可以使用UIUtils中的applySync、flushUpdates和flushUIUpdates接口实现状态管理V2的同步标脏。

## 概述

与状态管理V1不同的是，状态管理V2修改完状态变量后不会立即[标脏](arkts-state-management-glossary.md#标脏mark-dirty)，而是抛出一个Promise微任务（优先级低于宏任务），该微任务在当前宏任务执行完成后才会处理自定义组件标脏，具体差异可参考[V1状态变量更新和V2状态变量更新差异](arkts-v1-v2-update-difference.md#v1状态变量更新和v2状态变量更新差异)。而animateTo动效会立刻刷新已标脏节点来决定动效首帧。如果动效中使用了V2状态变量，并且在动效前修改了该状态变量，由于调用animateTo时状态变量的变化尚未标脏，这会导致animateTo的动效首帧不符合预期。为此，引入applySync、flushUpdates和flushUIUpdates接口，实现状态管理V2的同步标脏，确保动效达到预期效果。

使用applySync/flushUpdates/flushUIUpdates接口需要导入UIUtils工具。

```
1. import { UIUtils } from '@kit.ArkUI';
```

## 使用规则

* applySync接口用于同步刷新指定的状态变量，该接口接收一个闭包函数，仅刷新闭包函数内的修改，包括更新[@Computed](arkts-new-computed.md)计算、[@Monitor](arkts-new-monitor.md)回调以及重新渲染UI节点。

  ```
  1. import { UIUtils } from '@kit.ArkUI';

  3. @Entry
  4. @ComponentV2
  5. struct Index {
  6. @Local w: number = 50; // 宽度
  7. @Local h: number = 50; // 高度
  8. @Local message: string = 'Hello';

  10. @Monitor('message')
  11. onMessageChange(monitor: IMonitor) {
  12. monitor.dirty.forEach((path: string) => {
  13. console.info(`${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  14. });
  15. }

  17. build() {
  18. Column() {
  19. Button('change size')
  20. .margin(20)
  21. .onClick(() => {
  22. // 在执行动画前，存在额外的修改
  23. UIUtils.applySync(() => {
  24. this.w = 100;
  25. this.h = 100;
  26. this.message = 'Hello World';
  27. });

  29. this.getUIContext().animateTo({
  30. duration: 1000
  31. }, () => {
  32. this.w = 200;
  33. this.h = 200;
  34. this.message = 'Hello ArkUI';
  35. });
  36. })
  37. // ...
  38. Column() {
  39. Text(`${this.message}`)
  40. }
  41. .backgroundColor('#ff17a98d')
  42. .width(this.w)
  43. .height(this.h)
  44. }
  45. }
  46. }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/lgIXogfyQkCAW7wXUQYh5w/zh-cn_image_0000002589243919.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052723Z&HW-CC-Expire=86400&HW-CC-Sign=3B0F798554CA5D4651EBE0CF853EF7E2FEC7942AD5E1C43FB035F186831CF41C)
* flushUpdates接口用于同步刷新在调用该函数之前所有的状态变量修改，包括更新@Computed计算、@Monitor回调以及重新渲染UI节点。

  ```
  1. import { UIUtils } from '@kit.ArkUI';

  3. @Entry
  4. @ComponentV2
  5. struct Index {
  6. @Local w: number = 50; // 宽度
  7. @Local h: number = 50; // 高度
  8. @Local message: string = 'Hello';

  10. @Monitor('message')
  11. onMessageChange(monitor: IMonitor) {
  12. monitor.dirty.forEach((path: string) => {
  13. console.info(`${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  14. });
  15. }

  17. build() {
  18. Column() {
  19. Button('change size')
  20. .margin(20)
  21. .onClick(() => {
  22. // 在执行动画前，存在额外的修改
  23. this.w = 100;
  24. this.h = 100;
  25. this.message = 'Hello World';
  26. UIUtils.flushUpdates();

  28. this.getUIContext().animateTo({
  29. duration: 1000
  30. }, () => {
  31. this.w = 200;
  32. this.h = 200;
  33. this.message = 'Hello ArkUI';
  34. });
  35. })
  36. // ...
  37. Column() {
  38. Text(`${this.message}`)
  39. }
  40. .backgroundColor('#ff17a98d')
  41. .width(this.w)
  42. .height(this.h)
  43. }
  44. }
  45. }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/KsxMwlNmQVqwkA16ufcfKw/zh-cn_image_0000002589243919.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052723Z&HW-CC-Expire=86400&HW-CC-Sign=818F9FB870EA3CE242A119EDF8208F5D05BA40739E5BDDFFF235E7ADD15098A0)
* 上述的applySync、flushUpdates接口都会同步执行@Computed计算和@Monitor回调，这会使得在上述示例代码中，一次点击事件里触发了两次@Monitor回调，这可能会与开发者的预期不符，因此引入了flushUIUpdates接口，该接口仅用于同步刷新在调用该函数之前所有的UI节点，不会执行@Computed计算和@Monitor回调。

  ```
  1. import { UIUtils } from '@kit.ArkUI';

  3. @Entry
  4. @ComponentV2
  5. struct Index {
  6. @Local message: string = 'Hello';

  8. @Monitor('message')
  9. onMessageChange(monitor: IMonitor) {
  10. monitor.dirty.forEach((path: string) => {
  11. console.info(`${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  12. });
  13. }

  15. build() {
  16. Column() {
  17. Text(`message: ${this.message}`)
  18. Button('change size')
  19. .margin(20)
  20. .onClick(() => {
  21. // test1：调用applySync接口，日志打印两次
  22. // UIUtils.applySync(() => { this.message = 'Hello World'; });

  24. // test2：调用flushUpdates接口，日志打印两次
  25. // this.message = 'Hello World';
  26. // UIUtils.flushUpdates();

  28. // test3：调用flushUIUpdates接口，日志打印一次
  29. this.message = 'Hello World';
  30. UIUtils.flushUIUpdates();
  31. this.message = 'Hello ArkUI';
  32. })
  33. // ...
  34. }
  35. }
  36. }
  ```

## 限制条件

* 在applySync闭包函数中嵌套调用applySync，内层的applySync将会被跳过并返回undefined，同时打印出警告信息UIUtils.applySync will be skipped when called within another UIUtils.applySync. The inner UIUtils.applySync will return undefined。

  ```
  1. import { UIUtils } from '@kit.ArkUI';

  3. @Entry
  4. @ComponentV2
  5. struct Index {
  6. @Local w: number = 50; // 宽度
  7. @Local h: number = 50; // 高度

  9. build() {
  10. Column() {
  11. Button('change size')
  12. .margin(20)
  13. .onClick(() => {
  14. // 在执行动画前，存在额外的修改
  15. UIUtils.applySync(() => {
  16. this.w = 100;
  17. // 内层applySync会被跳过
  18. UIUtils.applySync(() => {
  19. this.h = 100;
  20. });
  21. });

  23. this.getUIContext().animateTo({
  24. duration: 1000
  25. }, () => {
  26. this.w = 200;
  27. this.h = 200;
  28. });
  29. })
  30. // ...
  31. Column() {
  32. Text('BOX')
  33. }
  34. .backgroundColor('#ff17a98d')
  35. .width(this.w)
  36. .height(this.h)
  37. }
  38. }
  39. }
  ```
* 在applySync闭包函数中调用flushUpdates或flushUIUpdates接口将不起作用。同时打印出对应警告信息UIUtils.flushUpdates will be skipped when called within UIUtils.applySync/UIUtils.flushUIUpdates will be skipped when called within UIUtils.applySync。

  ```
  1. import { UIUtils } from '@kit.ArkUI';

  3. @Entry
  4. @ComponentV2
  5. struct Index {
  6. @Local w: number = 50; // 宽度
  7. @Local h: number = 50; // 高度

  9. build() {
  10. Column() {
  11. Button('change size')
  12. .margin(20)
  13. .onClick(() => {
  14. // 在执行动画前，存在额外的修改
  15. UIUtils.applySync(() => {
  16. this.w = 100;
  17. UIUtils.flushUpdates(); // 在applySync中，flushUpdates被忽略
  18. UIUtils.flushUIUpdates(); // 在applySync中，flushUIUpdates被忽略
  19. });
  20. this.h = 100;
  21. UIUtils.flushUpdates(); // 会生效

  23. this.getUIContext().animateTo({
  24. duration: 1000
  25. }, () => {
  26. this.w = 200;
  27. this.h = 200;
  28. });
  29. })
  30. // ...
  31. Column() {
  32. Text('BOX')
  33. }
  34. .backgroundColor('#ff17a98d')
  35. .width(this.w)
  36. .height(this.h)
  37. }
  38. }
  39. }
  ```
* 不支持在@Computed装饰的getter方法中调用applySync、flushUpdates和flushUIUpdates接口，否则运行时会报错。错误信息为The function is not allowed to be called in @Computed，错误码为[140001](../harmonyos-references/errorcode-statemanagement.md#section140001-applysyncflushupdatesflushuiupdates非法调用)。

  ```
  1. import { UIUtils } from '@kit.ArkUI';

  3. @Entry
  4. @ComponentV2
  5. struct Page {
  6. @Local firstName: string = 'Hua';
  7. @Local lastName: string = 'Li';
  8. @Local count: number = 0;

  10. @Computed
  11. get fullName() {
  12. // 在computed中调用applySync、flushUpdates、flushUIUpdates运行时报错
  13. UIUtils.flushUIUpdates();
  14. UIUtils.flushUpdates();
  15. UIUtils.applySync(() => {
  16. this.count++;
  17. });
  18. return this.firstName + ' ' + this.lastName;
  19. }

  21. build() {
  22. Column() {
  23. Text(`${this.fullName}`)
  24. Text(`${this.count}`)
  25. Button('change fullName').onClick(() => {
  26. this.firstName = 'Zhang';
  27. this.lastName = 'San';
  28. })
  29. }
  30. }
  31. }
  ```
* 不支持在@Monitor回调函数中调用flushUpdates和flushUIUpdates接口，否则运行时会报错。错误信息为The function is not allowed to be called in @Monitor，错误码为[140002](../harmonyos-references/errorcode-statemanagement.md#section140002-flushupdatesflushuiupdates非法调用)。

  ```
  1. import { UIUtils } from '@kit.ArkUI';

  3. @Entry
  4. @ComponentV2
  5. struct Page {
  6. @Local count: number = 0;

  8. @Monitor('count')
  9. onCountChange(monitor: IMonitor) {
  10. monitor.dirty.forEach((path: string) => {
  11. console.info(`${path} changed from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  12. });
  13. UIUtils.flushUpdates(); // 在monitor中调用flushUpdates会运行时报错
  14. UIUtils.flushUIUpdates(); // 在monitor中调用flushUIUpdates会运行时报错
  15. }

  17. build() {
  18. Column() {
  19. Text(`${this.count}`)
  20. Button('change count')
  21. .onClick(() => {
  22. this.count++;
  23. })
  24. // ...
  25. }
  26. }
  27. }
  ```

## 使用场景

### 动效场景

状态管理V2的异步标脏逻辑与animateTo立即刷新脏节点的逻辑存在冲突，导致在@Monitor中触发animateTo时不显示动画。使用applySync接口同步刷新状态变量的改变能够实现预期效果，示例如下。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct Index {
6. @Local message: string = 'Hello World';
7. @Local x: number = 0;
8. @Local y: number = 0;
9. @Local w: number = 200;
10. @Local h: number = 50;

12. @Monitor('message')
13. onMsgChange() {
14. console.info('message change to', this.message);
15. this.animateAction();
16. }

18. animateAction() {
19. this.getUIContext().animateTo({
20. duration: 1000
21. }, () => {
22. // 调用applySync接口同步刷新动画尾帧，若不调用该接口则不显示动画
23. UIUtils.applySync(() => {
24. this.x = 100;
25. this.y = 100;
26. });
27. });
28. }

30. build() {
31. Column() {
32. Text(this.message)
33. .fontSize(20)
34. .width(this.w)
35. .height(this.h)
36. .backgroundColor(Color.Pink)
37. .onClick(() => {
38. this.message = 'New Message';
39. })
40. .position({
41. x: this.x,
42. y: this.y
43. })
44. // ...
45. }
46. .height('100%')
47. .width('100%')
48. }
49. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/fwDHRdTRSXml4r6OqAClLw/zh-cn_image_0000002558764112.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052723Z&HW-CC-Expire=86400&HW-CC-Sign=CFFE20DCEDF2CB10D3E477AAE39955FF0F669A2B1319BF92EA7DFFF71BF61167)

### 路由场景

在路由场景下设置[共享元素转场动效](../harmonyos-references/ts-transition-animation-shared-elements.md#sharedtransition)，使用applySync接口可以使得转场时同步刷新name值，实现转场动效效果。在如下示例代码中，从Index页面向PageTransitionTwo页面跳转时，两个页面的id值不匹配，没有转场动效。从PageTransitionTwo页面返回Index页面时，两个页面的id值匹配，有转场动效。

```
1. // PageUse.ets

3. import { UIUtils, AppStorageV2 } from '@kit.ArkUI';

5. @ObservedV2
6. export class Info {
7. @Trace public name: string = '';
8. }

10. @Entry
11. @ComponentV2
12. struct SharedTransitionExample {
13. @Local info: Info = AppStorageV2.connect(Info, () => new Info())!;

15. build() {
16. Column() {
17. // 此处'app.media.startIcon'仅做示例，请开发者自行替换
18. Image($r('app.media.startIcon'))
19. .width(50)
20. .height(50)
21. .margin({ left: 20, top: 20 })
22. .sharedTransition(this.info.name, { duration: 800, curve: Curve.Linear, delay: 100 })
23. }
24. .width('100%')
25. .height('100%')
26. .alignItems(HorizontalAlign.Start)
27. .onClick(() => {
28. UIUtils.applySync(() => {
29. this.info.name = 'id1'; // 不匹配
30. });
31. this.getUIContext().getRouter().pushUrl({ url: 'pages/PageTransitionTwo' })
32. })
33. // ...
34. }
35. }
```

```
1. // PageTransitionTwo.ets

3. import { UIUtils, AppStorageV2 } from '@kit.ArkUI';
4. import { Info } from './PageUse';

6. @Entry
7. @ComponentV2
8. struct PageBExample {
9. build() {
10. Stack() {
11. // 此处'app.media.startIcon'仅做示例，请开发者自行替换
12. Image($r('app.media.startIcon'))
13. .width(150)
14. .height(150)
15. .sharedTransition('sharedImage', { duration: 800, curve: Curve.Linear, delay: 100 })
16. .onClick(() => {
17. UIUtils.applySync(() => {
18. AppStorageV2.connect(Info, () => new Info())!.name = 'sharedImage'; // 匹配
19. });
20. this.getUIContext().getRouter().back();
21. })
22. // ...
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/vg9_GckITJC6lP5QDNaDIw/zh-cn_image_0000002558604456.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052723Z&HW-CC-Expire=86400&HW-CC-Sign=0D1FD590EFBA944B3D68ABF3D2E03899E15AAF13EFD30B2278CD1C52BD90EAC3)
