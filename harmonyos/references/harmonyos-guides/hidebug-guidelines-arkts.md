---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidebug-guidelines-arkts
title: HiDebug接口使用示例（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 系统调试信息获取 > HiDebug接口使用示例（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f196134fb7a7e085363e86964037bc45ec6b8875f236f0c6ba0c7f9bdfb5e973
---

HiDebug ArkTS接口功能独立，需要获取调试信息时直接调用。具体调用方式请参考[@ohos.hidebug](../harmonyos-references/js-apis-hidebug.md)中的示例。

## 开发示例

本文以获取系统CPU使用率为例，展示如何调用HiDebug ArkTS接口。

1. 使用DevEco Studio新建工程，选择“Empty Ability”。
2. 在Project窗口单击entry > src > main > ets > pages，打开并编辑Index.ets文件：

   导入所需依赖：

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hidebug, hilog } from '@kit.PerformanceAnalysisKit';
   ```

   定义测试方法：

   ```typescript
   function testHiDebugArk() {  // 按照需要调用的接口实现
     try {
       hilog.info(0x0000, 'testTag', `getSystemCpuUsage: ${hidebug.getSystemCpuUsage()}`);
     } catch (error) {
       hilog.info(0x0000, 'testTag', `error code: ${(error as BusinessError).code},
         error msg: ${(error as BusinessError).message}`);
     }
   }
   ```

   添加按钮以触发接口调用：

   ```typescript
   Button('testHiDebugArk')
     .type(ButtonType.Capsule)
     .margin({
       top: 20
     })
     .backgroundColor('#0D9FFB')
     .width('60%')
     .height('5%')
     // 添加点击事件
     .onClick(testHiDebugArk);
   ```
3. 点击运行，然后在设备上点击“testHiDebugArk”按钮，触发接口调用。
4. 在DevEco Studio底部切换到“Log”窗口，设置日志过滤条件为“testTag”，即可查看相关日志：

   ```text
   10-22 15:46:04.587   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     getSystemCpuUsage: 0.2878989952876323
   ```
