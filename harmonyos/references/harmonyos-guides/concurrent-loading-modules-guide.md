---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/concurrent-loading-modules-guide
title: 业务模块并发加载场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 应用多线程开发实践案例 > 业务模块并发加载场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:41+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:f233bb23adaabe914f56f37516d33ae78c4d44bac4a2f37a0f6e6baf9a8aeaef
---

在应用启动时，多个业务模块需要加载，例如地图应用中的定位、打车、导航等模块。如果全部在UI主线程初始化，会严重影响应用冷启动时间。此时，应在不同子线程中并行加载这些模块，以降低启动耗时。

通过使用ArkTS提供的TaskPool能力，可以将不同的业务初始化任务移到子线程中。业务模块可通过下沉C++实现为[NativeBinding对象](transferabled-object.md)或在ArkTS层定义为[Sendable对象](arkts-sendable.md)，从而将初始化的模块返回给UI主线程调用，实现如下。

1. 各业务功能（SDK）模块定义（这里以使用Sendable对象为例）。

   计算器业务模块定义如下：

   ```
   1. import { collections } from '@kit.ArkTS';

   3. @Sendable
   4. export class Calculator {
   5. public history?: collections.Array<collections.Array<string>>;
   6. public totalCount: number = 0;

   8. // 初始化
   9. static init(): Calculator {
   10. let calc = new Calculator();
   11. calc.totalCount = 0;
   12. calc.history = collections.Array.create(calc.totalCount, collections.Array.create(2, ''));
   13. return calc;
   14. }

   16. // 加法运算
   17. add(a: number, b: number) {
   18. let result = a + b;
   19. this.newCalc(`${a} + ${b}`, `${result}`);
   20. return result;
   21. }

   23. // 减法运算
   24. sub(a: number, b: number) {
   25. let result = a - b;
   26. this.newCalc(`${a} - ${b}`, `${result}`);
   27. return result;
   28. }

   30. // 乘法运算
   31. mul(a: number, b: number) {
   32. let result = a * b;
   33. this.newCalc(`${a} * ${b}`, `${result}`);
   34. return result;
   35. }

   37. // 除法运算
   38. div(a: number, b: number) {
   39. let result = a / b;
   40. this.newCalc(`${a} / ${b}`, `${result}`);
   41. return result;
   42. }

   44. // 获取历史记录
   45. getHistory(): collections.Array<collections.Array<string>> {
   46. return this.history!;
   47. }

   49. // 打印历史记录
   50. showHistory() {
   51. for (let i = 0; i < this.totalCount; i++) {
   52. console.info(`${i}: ${this.history![i][0]} = ${this.history![i][1]}`);
   53. }
   54. }

   56. // 添加新计算记录
   57. private newCalc(opt: string, ret: string) {
   58. let newRecord = new collections.Array<string>(opt, ret);
   59. this.totalCount = this.history!.unshift(newRecord);
   60. }
   61. }
   ```

   定时器业务模块的定义如下：

   ```
   1. @Sendable
   2. export class TimerSdk {

   4. // 初始化
   5. static init(): TimerSdk {
   6. let timer = new TimerSdk();
   7. return timer;
   8. }

   10. // 倒计时
   11. async Countdown(time: number) {
   12. return new Promise((resolve: (value: boolean) => void) => {
   13. setTimeout(() => {
   14. resolve(true);
   15. }, time);
   16. });
   17. }
   18. }
   ```
2. 在UI主线程触发各业务模块分发到子线程，加载完成后在UI主线程使用，示例如下：

   ```
   1. import { Calculator } from '../sdk/Calculator';
   2. import { TimerSdk } from '../sdk/TimerSdk';
   3. import { taskpool } from '@kit.ArkTS';

   5. // 初始化Calculator
   6. @Concurrent
   7. function initCalculator(): Calculator {
   8. return Calculator.init();
   9. }

   11. // 初始化TimerSdk
   12. @Concurrent
   13. function initTimerSdk(): TimerSdk {
   14. return TimerSdk.init();
   15. }

   17. @Entry
   18. @Component
   19. struct Index {
   20. @State calculateAdd: string = 'calculate add';
   21. @State showHistory: string = 'show history';
   22. @State countdown: string = 'countdown';
   23. calc?: Calculator;
   24. timer?: TimerSdk;

   26. aboutToAppear(): void {
   27. taskpool.execute(initCalculator).then((ret) => {
   28. this.calc = ret as Calculator;
   29. })
   30. taskpool.execute(initTimerSdk).then((ret) => {
   31. this.timer = ret as TimerSdk;
   32. })
   33. }

   35. build() {
   36. Row() {
   37. Column() {
   38. Text(this.calculateAdd)
   39. .id('add')
   40. .fontSize(50)
   41. .fontWeight(FontWeight.Bold)
   42. .alignRules({
   43. center: { anchor: '__container__', align: VerticalAlign.Center },
   44. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   45. })
   46. .onClick(async () => {
   47. let result = this.calc?.add(1, 2)
   48. console.info(`Result is ${result}`)
   49. this.calculateAdd = 'success';
   50. })
   51. Text(this.showHistory)
   52. .id('show')
   53. .fontSize(50)
   54. .fontWeight(FontWeight.Bold)
   55. .alignRules({
   56. center: { anchor: '__container__', align: VerticalAlign.Center },
   57. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   58. })
   59. .onClick(async () => {
   60. this.calc?.showHistory();
   61. this.showHistory = 'success';
   62. })
   63. Text(this.countdown)
   64. .id('get')
   65. .fontSize(50)
   66. .fontWeight(FontWeight.Bold)
   67. .alignRules({
   68. center: { anchor: '__container__', align: VerticalAlign.Center },
   69. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   70. })
   71. .onClick(async () => {
   72. console.info(`Timer start`);
   73. await this.timer?.Countdown(1000);
   74. console.info(`Timer end`);
   75. this.countdown = 'success';
   76. })
   77. }
   78. .width('100%')
   79. }
   80. .height('100%')
   81. }
   82. }
   ```
