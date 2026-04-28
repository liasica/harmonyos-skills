---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidebug-guidelines-arkts
title: HiDebug接口使用示例(ArkTS)
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 系统调试信息获取 > HiDebug接口使用示例(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c3eaf4e1b10433b6719b5f9ad300334c49424b355fa757ac598c571977b27ec3
---

HiDebug ArkTS接口功能独立，需要获取调试信息时直接调用。具体调用方式请参考[@ohos.hidebug](../harmonyos-references/js-apis-hidebug.md)中的示例。

## 开发示例

本文以获取系统CPU使用率为例，展示如何调用HiDebug ArkTS接口。

1. 使用DevEco Studio新建工程，选择“Empty Ability”。
2. 在Project窗口单击entry > src > main > ets > pages，打开并编辑Index.ets文件：

   导入所需依赖：

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { hidebug, hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiDebugTool/entry/src/main/ets/pages/Index.ets#L16-L19)

   定义测试方法：

   ```
   1. function testHiDebugArk() {  // 按照需要调用的接口实现
   2. try {
   3. hilog.info(0x0000, 'testTag', `getSystemCpuUsage: ${hidebug.getSystemCpuUsage()}`);
   4. } catch (error) {
   5. hilog.info(0x0000, 'testTag', `error code: ${(error as BusinessError).code},
   6. error msg: ${(error as BusinessError).message}`);
   7. }
   8. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiDebugTool/entry/src/main/ets/pages/Index.ets#L25-L34)

   添加按钮以触发接口调用：

   ```
   1. Button('testHiDebugArk')
   2. .type(ButtonType.Capsule)
   3. .margin({
   4. top: 20
   5. })
   6. .backgroundColor('#0D9FFB')
   7. .width('60%')
   8. .height('5%')
   9. // 添加点击事件
   10. .onClick(testHiDebugArk);
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiDebugTool/entry/src/main/ets/pages/Index.ets#L71-L82)
3. 点击运行，然后在设备上点击“testHiDebugArk”按钮，触发接口调用。
4. 在DevEco Studio底部切换到“Log”窗口，设置日志过滤条件为“testTag”，即可查看相关日志：

   ```
   1. 10-22 15:46:04.587   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     getSystemCpuUsage: 0.2878989952876323
   ```
