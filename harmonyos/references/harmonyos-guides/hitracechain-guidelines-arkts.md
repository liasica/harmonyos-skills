---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracechain-guidelines-arkts
title: 使用HiTraceChain打点（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 分布式调用链跟踪 > 使用HiTraceChain打点（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:656ecf44f7ed75a0a50cc18a61361fad854ebf0cdf28299bd5136f2bdcf2b227
---

## 接口说明

分布式跟踪接口由HiTraceChain模块提供，详细API请参考[@ohos.hiTraceChain (分布式跟踪)](../harmonyos-references/js-apis-hitracechain.md)。

| 接口名 | 描述 |
| --- | --- |
| hiTraceChain.begin(name: string, flags?: number = HiTraceFlag.DEFAULT): HiTraceId | 开始跟踪，并返回创建的HiTraceId。 |
| hiTraceChain.end(id: HiTraceId): void | 结束跟踪。 |
| hiTraceChain.getId(): HiTraceId | 获取跟踪标识。 |
| hiTraceChain.setId(id: HiTraceId): void | 设置跟踪标识。 |
| hiTraceChain.clearId(): void | 清除跟踪标识。 |
| hiTraceChain.createSpan(): HiTraceId | 创建跟踪分支。创建一个HiTraceId，使用当前线程TLS中的chainId、spanId初始化HiTraceId的chainId、parentSpanId，并为HiTraceId生成一个新的spanId，返回该HiTraceId。 |
| hiTraceChain.isValid(id: HiTraceId): boolean | 判断HiTraceId是否有效。  true：HiTraceId有效；false：HiTraceId无效。 |
| hiTraceChain.isFlagEnabled(id: HiTraceId, flag: HiTraceFlag): boolean | 判断HiTraceId中指定的跟踪标志是否已启用。  true：指定的跟踪标志已启用；false：指定的跟踪标志未启用。 |
| hiTraceChain.enableFlag(id: HiTraceId, flag: HiTraceFlag): void | 启用HiTraceId中指定的跟踪标志。 |
| hiTraceChain.tracepoint(mode: HiTraceCommunicationMode, type: HiTraceTracepointType, id: HiTraceId, msg?: string): void | HiTraceMeter跟踪信息埋点。 |

## 开发步骤

HiTraceChain在ArkTS中的使用方法参考以下示例，开发者可参考[约束与限制](hitracechain-intro.md#约束与限制)，了解常见的支持与不支持HiTraceChain自动传递的机制。

### async/await和promise/then异步任务中使用HiTraceChain

async/await和promise/then异步任务支持HiTraceChain自动传递，示例结合[事件订阅（ArkTS）](hiappevent-watcher-app-events-arkts.md)和[使用HiTraceMeter跟踪性能（ArkTS）](hitracemeter-guidelines-arkts.md)，说明分布式跟踪在ArkTS中的使用方法。

1. 在DevEco Studio中新建工程，选择“Empty Ability”，SDK版本选择19及以上（示例工程使用的HiTraceMeter接口从API version 19开始支持），工程的目录结构如下：

   ```
   1. ├── entry
   2. │   ├── src
   3. │       ├── main
   4. │       │   ├── ets
   5. │       │   │   ├── entryability
   6. │       │   │   │   └── EntryAbility.ets
   7. │       │   │   ├── entrybackupability
   8. │       │   │   │   └── EntryBackupAbility.ets
   9. │       │   │   └── pages
   10. │       │   │       └── Index.ets
   ```
2. 编辑“entry > src > main > ets > pages > Index.ets”文件，使用HiTraceChain跟踪异步任务，完整的示例代码如下：

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { hiAppEvent, hilog, hiTraceChain, hiTraceMeter } from '@kit.PerformanceAnalysisKit';

   4. async function test3() {
   5. hilog.info(0x0000, 'testTag', 'test3');
   6. }

   8. async function test2() {
   9. hilog.info(0x0000, 'testTag', 'test2');
   10. }

   12. async function test1() {
   13. hilog.info(0x0000, 'testTag', 'test1_1');
   14. await test2();
   15. hilog.info(0x0000, 'testTag', 'test1_2');
   16. await test3();
   17. hilog.info(0x0000, 'testTag', 'test1_3');
   18. }

   20. @Entry
   21. @Component
   22. struct Index {
   23. @State message: string = 'clickTime=0';
   24. @State clickTime: number = 0;

   26. build() {
   27. Row() {
   28. Column() {
   29. Button(this.message)
   30. .fontSize(20)
   31. .margin(5)
   32. .width(350)
   33. .height(60)
   34. .fontWeight(FontWeight.Bold)
   35. .onClick(() => {
   36. this.clickTime++;
   37. this.message = 'clickTime=' + this.clickTime;
   38. // 业务开始前，开启分布式跟踪
   39. // INCLUDE_ASYNC表示会在系统支持的异步机制里自动传递HiTraceId
   40. let traceId = hiTraceChain.begin('testTag: hiTraceChain begin', hiTraceChain.HiTraceFlag.INCLUDE_ASYNC);
   41. // 开始HiTraceMeter同步打点，该接口API version 19开始支持
   42. hiTraceMeter.startSyncTrace(hiTraceMeter.HiTraceOutputLevel.COMMERCIAL, 'onClick', this.message);

   44. // 在按钮点击函数中进行事件打点，以记录按钮点击事件
   45. let eventParams: Record<string, number> = { 'click_time': 100 };
   46. let eventInfo: hiAppEvent.AppEventInfo = {
   47. // 事件领域定义
   48. domain: 'button',
   49. // 事件名称定义
   50. name: 'click',
   51. // 事件类型定义
   52. eventType: hiAppEvent.EventType.BEHAVIOR,
   53. // 事件参数定义
   54. params: eventParams
   55. };
   56. hiAppEvent.write(eventInfo).then(() => {
   57. hilog.info(0x0000, 'testTag', 'Succeeded in writing an app event');
   58. // 按钮点击事件处理结束，关闭异步处理分支的分布式跟踪
   59. hiTraceChain.end(traceId);
   60. hilog.info(0x0000, 'testTag', 'hiTraceChain end in hiAppEvent');
   61. }).catch((err: BusinessError) => {
   62. hilog.error(0x0000, 'testTag', `HiAppEvent err.code: ${err.code}, err.message: ${err.message}`);
   63. // 异常处理结束，关闭异步处理分支的分布式跟踪
   64. hiTraceChain.end(traceId);
   65. hilog.info(0x0000, 'testTag', 'hiTraceChain end in hiAppEvent');
   66. });

   68. // 创建Promise对象执行随机数生成任务，若随机数大于0.5，则正常返回结果，反之则返回异常信息
   69. const promise: Promise<number> = new Promise((resolve: Function, reject: Function) => {
   70. hilog.info(0x0000, 'testTag', 'promise task');
   71. const randomNumber: number = Math.random();
   72. if (randomNumber > 0.5) {
   73. resolve(randomNumber);
   74. } else {
   75. reject(new Error('Random number is too small'));
   76. }
   77. });

   79. // then方法的回调函数处理Promise对象的执行结果
   80. promise.then((result: number) => {
   81. // 成功时执行
   82. hilog.info(0x0000, 'testTag', 'Random number is %{public}d', result);
   83. // 回调函数处理结束，关闭异步处理分支的分布式跟踪
   84. hiTraceChain.end(traceId);
   85. hilog.info(0x0000, 'testTag', 'hiTraceChain end in promise/then');
   86. }).catch((error: BusinessError) => {
   87. // 失败时执行
   88. hilog.error(0x0000, 'testTag', error.message);
   89. // 异常处理结束，关闭异步处理分支的分布式跟踪
   90. hiTraceChain.end(traceId);
   91. hilog.info(0x0000, 'testTag', 'hiTraceChain end in promise/then');
   92. });

   94. // 执行async/await异步任务
   95. let res = test1();
   96. // then方法的回调函数处理异步任务的执行结果
   97. res.then(() => {
   98. hilog.info(0x0000, 'testTag', 'then task');
   99. // 功能同hiTraceChain.end，关闭异步处理分支的分布式跟踪
   100. hiTraceChain.clearId();
   101. hilog.info(0x0000, 'testTag', 'hiTraceChain end in async/await');
   102. });

   104. // 结束HiTraceMeter同步打点，该接口API version 19开始支持
   105. hiTraceMeter.finishSyncTrace(hiTraceMeter.HiTraceOutputLevel.COMMERCIAL);
   106. // 业务结束后，关闭分布式跟踪
   107. hiTraceChain.end(traceId);
   108. hilog.info(0x0000, 'testTag', 'hiTraceChain end in main thread');
   109. })
   110. }
   111. .width('100%')
   112. }
   113. .height('100%')
   114. }
   115. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiTrace/HitraceChain_ArkTS_Sample_A/entry/src/main/ets/pages/Index.ets#L16-L132)
3. 点击DevEco Studio界面中的运行按钮，运行应用工程。在DevEco Studio Terminal窗口中执行以下命令，捕获10秒内的应用trace，并使用关键字“onClick”过滤示例代码中hiTraceMeter.startSyncTrace和hiTraceMeter.finishSyncTrace生成的trace日志。

   ```
   1. PS D:\xxx\xxx> hdc shell
   2. $ hitrace -t 10 app | grep onClick
   ```
4. 点击设备上的“clickTime=0”按钮（需在10秒内完成，否则步骤3捕获不到trace数据），触发业务逻辑。
5. 查看运行结果。

   * 设备屏幕上按钮显示“clickTime=1”，表示点击了按钮一次，已触发业务逻辑。
   * 在DevEco Studio Log窗口查看分布式跟踪的相关信息。

     + 示例所有hilog打印均使用了“testTag”，因此可以使用关键字“testTag”过滤日志，查看该业务代码打印的hilog日志。

       ```
       1. 06-04 17:46:45.156   55451-55451   C02D33/com.exa...tion/HiTraceC  com.examp...lication  I     [a92ab116052648e 0 0]HiTraceBegin name:testTag: hiTraceChain begin flags:0x01.
       2. 06-04 17:46:45.157   55451-55451   A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab116052648e 0 0]promise task
       3. 06-04 17:46:45.158   55451-55451   A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab116052648e 0 0]test1_1
       4. 06-04 17:46:45.158   55451-55451   A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab116052648e 0 0]test2
       5. 06-04 17:46:45.158   55451-55451   A00000/com.exa...ation/testTag  com.examp...lication  I     hiTraceChain end in main thread
       6. 06-04 17:46:45.158   55451-55451   A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab116052648e 3457eff 0]test1_2
       7. 06-04 17:46:45.158   55451-55451   A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab116052648e 3457eff 0]test3
       8. 06-04 17:46:45.158   55451-55451   A00000/com.exa...ation/testTag  com.examp...lication  E     [a92ab116052648e 1bb5a1b 35d9c46]Random number is too small
       9. 06-04 17:46:45.158   55451-55451   A00000/com.exa...ation/testTag  com.examp...lication  I     hiTraceChain end in promise/then
       10. 06-04 17:46:45.158   55451-55451   A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab116052648e 2ddfb70 3457eff]test1_3
       11. 06-04 17:46:45.158   55451-55451   A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab116052648e 225a1d9 2ddfb70]then task
       12. 06-04 17:46:45.158   55451-55451   A00000/com.exa...ation/testTag  com.examp...lication  I     hiTraceChain end in async/await
       13. 06-04 17:46:45.163   55451-55451   A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab116052648e 3a75cb2 520a92]Succeeded in writing an app event
       14. 06-04 17:46:45.163   55451-55451   A00000/com.exa...ation/testTag  com.examp...lication  I     hiTraceChain end in hiAppEvent
       ```
     + hilog日志前附加的[chainId spanId parentSpanId]格式的信息即为HiTraceId信息，例如[a92ab116052648e 2ddfb70 3457eff]表示跟踪链标识chainId值为a92ab116052648e，分支标识spanId值为2ddfb70，父分支标识parentSpanId值为3457eff。
     + 示例得到的跟踪链标识chainId值为a92ab116052648e，可使用chainId值过滤日志，查看业务完整的调用链hilog日志。
     + promise/then和async/await异步机制都会自动传递HiTraceId，并生成分支标识，例如示例hilog日志中的3457eff、2ddfb70、225a1d9等，均为异步任务自动生成的分支标识。
     + hiTraceChain.end()和hiTraceChain.clear()都可以结束跟踪，跟踪结束后，hilog日志不再携带HiTraceId信息。
   * 在DevEco Studio Terminal窗口查看trace数据，HiTraceChain跟踪开启期间，HiTraceMeter打点得到的trace日志会自动携带HiTraceId信息。

     ```
     1. e.myapplication-55451   (  55451) [010] .... 27164.174417: tracing_mark_write: B|55451|H:[a92ab116052648e,0,0]#onClick|M62|clickTime=1
     ```

### 异步宏任务setInterval和setTimeout中使用HiTraceChain

异步宏任务setInterval和setTimeout不支持HiTraceChain自动传递，以下示例说明如何使用hiTraceChain.getId()、hiTraceChain.setId()接口传递HiTraceId，如何使用hiTraceChain.createSpan()接口创建分支标识，进行分布式跟踪。

1. 在DevEco Studio中新建工程，选择“Empty Ability”，工程的目录结构如下：

   ```
   1. ├── entry
   2. │   ├── src
   3. │       ├── main
   4. │       │   ├── ets
   5. │       │   │   ├── entryability
   6. │       │   │   │   └── EntryAbility.ets
   7. │       │   │   ├── entrybackupability
   8. │       │   │   │   └── EntryBackupAbility.ets
   9. │       │   │   └── pages
   10. │       │   │       └── Index.ets
   ```
2. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，使用HiTraceChain跟踪异步任务，完整的示例代码如下：

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { hilog, hiTraceChain } from '@kit.PerformanceAnalysisKit';

   4. @Entry
   5. @Component
   6. struct Index {
   7. @State message: string = 'clickTime=0';
   8. @State clickTime: number = 0;

   10. build() {
   11. Row() {
   12. Column() {
   13. Button(this.message)
   14. .fontSize(20)
   15. .margin(5)
   16. .width(350)
   17. .height(60)
   18. .fontWeight(FontWeight.Bold)
   19. .onClick(() => {
   20. this.clickTime++;
   21. this.message = 'clickTime=' + this.clickTime;
   22. // 获取当前线程的HiTraceId
   23. let traceId = hiTraceChain.getId();
   24. // 如果traceId无效，为当前线程开启分布式跟踪
   25. if (!hiTraceChain.isValid(traceId)) {
   26. hilog.info(0x0000, 'testTag', 'HiTraceId is invalid, begin hiTraceChain');
   27. traceId = hiTraceChain.begin('testTag: hiTraceChain begin');
   28. // 使能traceId的INCLUDE_ASYNC，INCLUDE_ASYNC表示会在系统支持的异步机制里自动传递HiTraceId
   29. hiTraceChain.enableFlag(traceId, hiTraceChain.HiTraceFlag.INCLUDE_ASYNC);
   30. // 将使能INCLUDE_ASYNC的HiTraceId设置到当前线程
   31. hiTraceChain.setId(traceId);
   32. // 查询INCLUDE_ASYNC是否设置成功
   33. if (hiTraceChain.isFlagEnabled(hiTraceChain.getId(), hiTraceChain.HiTraceFlag.INCLUDE_ASYNC)) {
   34. hilog.info(0x0000, 'testTag', 'HiTraceFlag INCLUDE_ASYNC is enabled');
   35. }
   36. }

   38. const promise: Promise<number> = new Promise((resolve: Function, reject: Function) => {
   39. // 创建异步重复定时任务，每1s执行一次
   40. let intervalID = setInterval(() => {
   41. // 为当前异步重复定时任务设置HiTraceId
   42. hiTraceChain.setId(traceId);
   43. const randomNumber: number = Math.random();
   44. hilog.info(0x0000, 'testTag', 'Interval 1s: randomNumber is %{public}d', randomNumber);
   45. // 关闭当前异步重复定时任务的分布式跟踪
   46. hiTraceChain.end(traceId);
   47. }, 1000)

   49. // 创建异步定时任务，2.5s后执行，结束异步重复定时任务
   50. setTimeout(() => {
   51. // 为异步定时任务设置HiTraceId
   52. hiTraceChain.setId(traceId);
   53. // 为异步定时任务生成分支标识spanId
   54. let traceIdTimeout = hiTraceChain.createSpan();
   55. // 为异步定时任务设置带spanId的HiTraceId
   56. hiTraceChain.setId(traceIdTimeout);
   57. hilog.info(0x0000, 'testTag', 'setTimeout 2.5s');
   58. // 结束异步重复定时任务
   59. clearInterval(intervalID);
   60. const randomNumber: number = Math.random();
   61. if (randomNumber > 0.5) {
   62. resolve(randomNumber);
   63. } else {
   64. reject(new Error('Random number is too small'));
   65. }
   66. // 关闭异步定时任务的分布式跟踪
   67. hiTraceChain.end(traceId);
   68. }, 2500)
   69. })

   71. promise.then((result: number) => {
   72. // 成功时执行
   73. hilog.info(0x0000, 'testTag', 'Random number is %{public}d', result);
   74. // 回调函数处理结束，关闭异步处理分支的分布式跟踪
   75. hiTraceChain.end(traceId);
   76. }).catch((error: BusinessError) => {
   77. // 失败时执行
   78. hilog.error(0x0000, 'testTag', error.message);
   79. // 异常处理结束，关闭异步处理分支的分布式跟踪
   80. hiTraceChain.end(traceId);
   81. });

   83. // 业务结束后，关闭分布式跟踪
   84. hiTraceChain.end(traceId);
   85. hilog.info(0x0000, 'testTag', 'hiTraceChain end in main thread');
   86. })
   87. }
   88. .width('100%')
   89. }
   90. .height('100%')
   91. }
   92. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiTrace/HitraceChain_ArkTS_Sample_B/entry/src/main/ets/pages/Index.ets#L16-L109)
3. 点击DevEco Studio界面中的运行按钮，运行应用工程，点击设备上“clickTime=0”按钮，触发业务逻辑。
4. 查看运行结果。

   * 设备屏幕上按钮显示“clickTime=1”，表示点击了按钮一次，已触发业务逻辑。
   * 在DevEco Studio Log窗口查看分布式跟踪的相关信息。
     + 示例所有hilog打印均使用了“testTag”，因此可以使用关键字“testTag”过滤日志，查看该业务代码打印的hilog日志。

       ```
       1. 06-05 15:46:04.544   49568-49568   A00000/com.exa...ation/testTag  com.examp...lication  I     HiTraceId is invalid, begin hiTraceChain
       2. 06-05 15:46:04.544   49568-49568   C02D33/com.exa...tion/HiTraceC  com.examp...lication  I     [a92ab34b3c84ea7 0 0]HiTraceBegin name:testTag: hiTraceChain begin flags:0x00.
       3. 06-05 15:46:04.544   49568-49568   A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab34b3c84ea7 0 0]HiTraceFlag INCLUDE_ASYNC is enabled
       4. 06-05 15:46:04.544   49568-49568   A00000/com.exa...ation/testTag  com.examp...lication  I     hiTraceChain end in main thread
       5. 06-05 15:46:05.547   49568-49568   A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab34b3c84ea7 0 0]Interval 1s: randomNumber is 0.863610
       6. 06-05 15:46:06.548   49568-49568   A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab34b3c84ea7 0 0]Interval 1s: randomNumber is 0.365460
       7. 06-05 15:46:07.047   49568-49568   A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab34b3c84ea7 3cafdfd 0]setTimeout 2.5s
       8. 06-05 15:46:07.048   49568-49568   A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab34b3c84ea7 dc842f 3cafdfd]Random number is 0.524236
       ```
     + hilog日志前附加的[chainId spanId parentSpanId]格式的信息即为HiTraceId信息，例如[a92ab34b3c84ea7 dc842f 3cafdfd]表示跟踪链标识chainId值为a92ab34b3c84ea7，分支标识spanId值为dc842f，父分支标识parentSpanId值为3cafdfd。
     + 示例得到的chainId值为a92ab34b3c84ea7，可使用chainId值过滤日志，查看业务完整的调用链hilog日志。
