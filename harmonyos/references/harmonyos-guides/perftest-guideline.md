---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/perftest-guideline
title: 白盒性能测试框架使用指导
breadcrumb: 指南 > 应用测试 > 单元测试和UI测试 > 自动化测试框架使用指导 > 白盒性能测试框架使用指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:52+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:ce3d1d7e5efac07ec4792f15468aa170e6e6ffc91bbc24f2cde8a636663b41b9
---

## 简介

白盒性能测试框架（PerfTest），提供了针对指定代码段运行时的白盒性能测试能力，用于度量指定应用进程的性能表现。框架通过多轮迭代执行机制和环境复位机制实现自动化测试，支持耗时、CPU使用率等基础数据和启动时延、滑动帧率等场景化性能数据的采集和度量。使用PerfTest接口的性能测试脚本需基于单元测试框架进行开发。

## 实现原理

PerfTest功能设计图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/puXgmZl-RXmcjzemLSVzvQ/zh-cn_image_0000002581217683.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=3A6576709ED943924649D51ED8F600AAA8584A39F981E959C0630C388818BCE0)

PerfTest对外提供ArkTS API，包括性能测试策略设置、性能测试执行、测试结果获取等能力。具体请参考[API文档](../harmonyos-references/js-apis-perftest.md)。

跨语言通信层负责上层ArkTS接口与底层C++接口的转换，包括参数校验、JSON序列化对象处理和异常处理等。作为PerfTest的客户端，它提供启动入口和功能调用接口。该层由测试应用加载运行，通过IPC与服务端通信实现功能调用和生命周期管理。此外，该层还负责管理C++层对ArkTS回调函数的调用。

PerfTest服务端负责白盒性能测试框架的主要功能处理，包含以下两部分：

* 框架运行通用能力：管理C++接口和错误码，包括接口调用、参数解析、异常处理等。PerfTest服务端以独立进程运行，通过IPC与客户端通信，监听客户端生命周期，实现进程保活和按需启停。
* 白盒性能测试能力：主要负责测试任务调度和性能数据采集工作。根据用户定义的测试策略，实现测试代码段运行、性能数据采集、数据处理和存储的自动化性能测试流程。当前支持采集的性能指标包括：耗时、CPU、内存、应用启动时延、页面切换时延、列表滑动帧率等。

## 开发步骤

使用PerfTest接口进行白盒性能测试流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/Wjv4gbW8QjeZxuK8-s0tCg/zh-cn_image_0000002550777588.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=07F33EE041E7ACFF7D4069532B682E8A4F402B764C3E772C5D6EB6B0CA5210BD)

1. 定义性能测试策略，明确测试指标列表、被测代码段、环境复位代码段、被测应用包名、测试迭代次数、代码段单次执行超时时间等，后续白盒性能测试中将依照此策略执行测试。
2. 创建测试任务，配置测试策略并准备测试环境。
3. 启动测试，将根据测试迭代次数执行多轮测试。每轮测试采集被测代码段执行期间的性能数据，并执行环境复位代码段恢复环境。完成后进行数据处理和保存。
4. 获取测量数据值，结果存储在对象中，支持获取每轮测试详细数据和最大值、最小值、平均值等统计数据。
5. 销毁创建的对象，释放内存占用。

下面以采集指定代码段执行期间的耗时、CPU使用率为例，介绍详细代码开发步骤。

### 定义测试策略

1. 定义测试性能指标列表

   定义所需测试的性能指标列表metrics，类型为Array<PerfMetric>，其中[PerfMetric](../harmonyos-references/js-apis-perftest.md#perfmetric)为框架支持采集的性能指标枚举。

   ```
   1. let metrics: Array<PerfMetric> = [PerfMetric.DURATION, PerfMetric.CPU_USAGE]; // 定义待测指标
   ```
2. 定义被测代码段和环境复位代码段

   被测代码段actionCode是一个类型为Callback<Callback<boolean>>的回调函数，框架在测试期间会自动调用此回调函数，并采集性能数据。执行结束时需调用入参Callback<boolean>函数通知框架执行完成，否则会导致代码段执行超时。例如测试Utils.CalculateTest方法性能时，通过调用finish(true)通知框架代码段执行完成。

   ```
   1. let actionCode: Callback<Callback<boolean>> = async (finish: Callback<boolean>) => { // 定义被测代码段
   2. Utils.CalculateTest();
   3. finish(true);
   4. };
   ```

   此外，框架支持定义环境复位代码段resetCode，用于在单次测试后进行环境复位，类型和使用方法与actionCode相同。resetCode会在actionCode执行完成后执行，但执行期间不会采集应用性能数据。

   ```
   1. let resetCode: Callback<Callback<boolean>> = async (finish: Callback<boolean>) => { // 定义环境复位代码段
   2. Utils.Reset();
   3. finish(true);
   4. };
   ```
3. 构造测试策略对象

   除以上步骤定义的属性外，框架还支持定义其他测试策略，从而帮助开发者进行更加精确的自动化性能测试。所有测试策略通过[PerfTestStrategy](../harmonyos-references/js-apis-perftest.md#perfteststrategy)对象定义和保存，性能测试期间会依据此策略执行并采集数据。

   ```
   1. let perfTestStrategy: PerfTestStrategy = {
   2. // 定义测试策略
   3. metrics: metrics,
   4. actionCode: actionCode,
   5. resetCode: resetCode,
   6. bundleName: 'com.samples.test.perftest', // 定义被测应用包名，请开发者替换为实际包名
   7. iterations: 10, // 定义测试迭代次数
   8. timeout: 20000  // 定义代码段单次执行超时时间
   9. };
   ```

### 创建测试任务和启动测试

使用[PerfTest.create()](../harmonyos-references/js-apis-perftest.md#create)创建测试任务时，传入上文定义的PerfTestStrategy对象。然后调用[PerfTest.run()](../harmonyos-references/js-apis-perftest.md#run)异步接口启动测试。测试会自动迭代执行被测代码段并采集性能数据。使用await语法糖同步等待执行完成后再进行后续操作。

```
1. let perfTest: PerfTest = PerfTest.create(perfTestStrategy); // 创建测试任务对象PerfTest
2. await perfTest.run(); // 执行测试，异步函数需使用await同步等待完成
```

### 获取测试结果

性能测试运行完成后，调用[PerfTest.getMeasureResult()](../harmonyos-references/js-apis-perftest.md#getmeasureresult)获取各个指标的测试结果。结果存储在[PerfMeasureResult](../harmonyos-references/js-apis-perftest.md#perfmeasureresult)对象中。若测试未完成或指标未定义，则抛出错误码。

```
1. let res1: PerfMeasureResult = perfTest.getMeasureResult(PerfMetric.DURATION); // 获取耗时指标的测试结果
2. let res2: PerfMeasureResult = perfTest.getMeasureResult(PerfMetric.CPU_USAGE); // 获取CPU使用率指标的测试结果
```

### 销毁创建的对象

性能测试完成后，若无需继续使用PerfTest对象，可以调用[PerfTest.destroy()](../harmonyos-references/js-apis-perftest.md#destroy)销毁对象以释放内存。

```
1. perfTest.destroy(); // 销毁PerfTest对象
```

## 完整示例

### 基础性能数据采集示例

下面以测试应用内指定逻辑执行时的基础性能数据为例，应用内定义了一个名为'Utils.CalculateTest()'的方法，性能测试时执行此方法，并采集执行期间的耗时和应用CPU占用率。

1. 在 main > ets > utils 文件夹下新增 Utils.ets 文件，在文件中编写自定义的函数。

   ```
   1. export class Utils {
   2. static num: number = 0;
   3. static maxNum: number = 10000;

   5. public static CalculateTest() {
   6. for (let index = 0; index < Utils.maxNum; index++) {
   7. Utils.num++;
   8. }
   9. }

   11. public static Reset() {
   12. Utils.num = 0;
   13. }
   14. }
   ```
2. 在 ohosTest > ets > test 文件夹下 CPUMetric.test.ets 文件中编写具体测试代码。

   ```
   1. import { describe, expect, it, Level } from '@ohos/hypium';
   2. import { abilityDelegatorRegistry, PerfMeasureResult, PerfMetric, PerfTest, PerfTestStrategy } from '@kit.TestKit';
   3. import { Utils } from '../../../main/ets/utils/Utils';

   5. export default function PerfTestTest() {
   6. describe('PerfTestTest2', () => {
   7. it('testExample1', 0, async (done: Function) => {
   8. let metrics: Array<PerfMetric> = [PerfMetric.DURATION, PerfMetric.CPU_USAGE]; // 定义待测指标
   9. let actionCode: Callback<Callback<boolean>> = async (finish: Callback<boolean>) => { // 定义被测代码段
   10. Utils.CalculateTest();
   11. finish(true);
   12. };
   13. let resetCode: Callback<Callback<boolean>> = async (finish: Callback<boolean>) => { // 定义环境复位代码段
   14. Utils.Reset();
   15. finish(true);
   16. };
   17. let perfTestStrategy: PerfTestStrategy = {
   18. // 定义测试策略
   19. metrics: metrics,
   20. actionCode: actionCode,
   21. resetCode: resetCode,
   22. bundleName: 'com.samples.test.perftest', // 定义被测应用包名，请开发者替换为实际包名
   23. iterations: 10, // 定义测试迭代次数
   24. timeout: 20000  // 定义代码段单次执行超时时间
   25. };
   26. try {
   27. let perfTest: PerfTest = PerfTest.create(perfTestStrategy); // 创建测试任务对象PerfTest
   28. await perfTest.run(); // 执行测试，异步函数需使用await同步等待完成
   29. let res1: PerfMeasureResult = perfTest.getMeasureResult(PerfMetric.DURATION); // 获取耗时指标的测试结果
   30. let res2: PerfMeasureResult = perfTest.getMeasureResult(PerfMetric.CPU_USAGE); // 获取CPU使用率指标的测试结果
   31. perfTest.destroy(); // 销毁PerfTest对象
   32. expect(res1.average).assertLessOrEqual(1000); // 断言性能测试结果
   33. expect(res2.average).assertLessOrEqual(30); // 断言性能测试结果
   34. } catch (error) {
   35. expect(false).assertTrue();
   36. }
   37. done();
   38. })
   39. })
   40. }
   ```

### 场景化性能数据采集示例

下面以测试应用内列表滑动的帧率为例，实现如下功能：打开指定应用，使用UI测试框架接口查找类型为'Scroll'的可滚动组件，并进行滑动操作，采集期间的列表滑动帧率数据。

1. 在 main > ets > pages 文件夹下编写 PageListPage.ets 页面代码，作为被测示例demo。

   ```
   1. @Entry
   2. @Component
   3. struct ListPage {
   4. scroller: Scroller = new Scroller();
   5. private arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

   7. build() {
   8. Row() {
   9. Column() {
   10. Scroll(this.scroller) {
   11. Column() {
   12. ForEach(this.arr, (item: number) => {
   13. Text(item.toString())
   14. .width('90%')
   15. .height('40%')
   16. .fontSize(80)
   17. .textAlign(TextAlign.Center)
   18. .margin({ top: 10 })
   19. }, (item: string) => item)
   20. }
   21. }
   22. .width('100%')
   23. .height('100%')
   24. .scrollable(ScrollDirection.Vertical)
   25. .scrollBar(BarState.On)
   26. .scrollBarColor(Color.Gray)
   27. }
   28. .width('100%')
   29. }
   30. .height('100%')
   31. }
   32. }
   ```
2. 在ohosTest > ets > test文件夹下 slideFps.test.ets 文件中编写具体测试代码。

   ```
   1. import { describe, expect, it, Level } from '@ohos/hypium';
   2. import {
   3. abilityDelegatorRegistry,
   4. Driver,
   5. ON,
   6. PerfMeasureResult,
   7. PerfMetric,
   8. PerfTest,
   9. PerfTestStrategy
   10. } from '@kit.TestKit';
   11. import { Want } from '@kit.AbilityKit';

   13. const delegator: abilityDelegatorRegistry.AbilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();

   15. export default function PerfTestTest() {
   16. describe('PerfTestTest1', () => {
   17. it('testExample2', Level.LEVEL3, async (done: Function) => {
   18. let driver = Driver.create();
   19. await driver.delayMs(1000);
   20. const bundleName = abilityDelegatorRegistry.getArguments().bundleName;
   21. // 被拉起应用的包名和Ability组件名，请开发者替换为实际的bundleName和abilityName
   22. const want: Want = {
   23. bundleName: bundleName,
   24. abilityName: 'EntryAbility'
   25. };
   26. await delegator.startAbility(want); // 拉起测试应用
   27. await driver.delayMs(1000);
   28. let toPageListBtn = await driver.findComponent(ON.id('toPageList'));
   29. await toPageListBtn.click();
   30. await driver.delayMs(1000);
   31. let scroll = await driver.findComponent(ON.type('Scroll'));
   32. await driver.delayMs(1000);
   33. let center = await scroll.getBoundsCenter(); // 获取Scroll可滚动组件坐标
   34. await driver.delayMs(1000);
   35. let metrics: Array<PerfMetric> = [PerfMetric.LIST_SWIPE_FPS]; // 指定被测指标为列表滑动帧率
   36. let actionCode = async (finish: Callback<boolean>) => { // 测试代码段中使用uitest进行列表滑动
   37. await driver.fling({ x: center.x, y: Math.floor(center.y * 3 / 2) },
   38. { x: center.x, y: Math.floor(center.y / 2) }, 50, 20000);
   39. await driver.delayMs(3000);
   40. finish(true);
   41. };
   42. let resetCode = async (finish: Callback<boolean>) => { // 复位环境，将列表划至顶部
   43. await scroll.scrollToTop(40000);
   44. await driver.delayMs(1000);
   45. finish(true);
   46. };
   47. let perfTestStrategy: PerfTestStrategy = {
   48. // 定义测试策略
   49. metrics: metrics,
   50. actionCode: actionCode,
   51. resetCode: resetCode,
   52. iterations: 5, // 指定测试迭代次数
   53. timeout: 50000, // 指定actionCode和resetCode的超时时间
   54. };
   55. try {
   56. let perfTest: PerfTest = PerfTest.create(perfTestStrategy); // 创建测试任务对象PerfTest
   57. await perfTest.run(); // 执行测试，异步函数需使用await同步等待完成
   58. let res: PerfMeasureResult = perfTest.getMeasureResult(PerfMetric.LIST_SWIPE_FPS); // 获取列表滑动帧率指标的测试结果
   59. perfTest.destroy(); // 销毁PerfTest对象
   60. expect(res.average).assertLargerOrEqual(30); // 断言性能测试结果
   61. } catch (error) {
   62. console.error(`Failed to execute perftest. Cause:${JSON.stringify(error)}`);
   63. }
   64. done();
   65. })
   66. })
   67. }
   ```
