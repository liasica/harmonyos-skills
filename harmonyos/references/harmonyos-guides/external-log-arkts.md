---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/external-log-arkts
title: external_log日志清理（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 故障检测 > 通用日志 > external_log日志 > external_log日志清理（ArkTS）
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:45+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:7395bea9481b0d4f80882a1495c19e185c17d08299a82ada6c3c3d045843bf89
---

从API版本26.0.1开始提供了external\_log日志管理者注册接口，确保故障日志沙箱目录容量达到阈值时通知应用清理删除文件。

## 接口说明

API接口使用说明，包括参数使用限制和具体取值范围。请参考[@ohos.hiviewdfx.hiAppEvent](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)。

| 接口名 | 描述 |
| --- | --- |
| registerExternalLogManager(logMngr: ExternalLogManager): void | 注册external\_log日志管理者。 |
| isExternalLogManagerRegistered(): boolean | 查询external\_log日志管理者是否被注册。 |

## 注册external\_log日志管理者开发指导

1. 新建一个ArkTS应用工程，编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，导入所需的依赖模块：

   ```typescript
   import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
   // ...
   import { fileIo } from '@kit.CoreFileKit';
   ```
2. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets” 文件，在onCreate函数中添加注册external\_log日志文件管理者。

   ```typescript
   // 定义删除文件函数
   let deleteFiles: (files: string[]) => void = (files: string[]): void => {
     for (const file of files) {
       try {
         fileIo.unlinkSync(file);
         hilog.info(0x0000, 'testTag', `[MyLogManager] 已删除: ${file}`);
       } catch (e) {
         hilog.info(0x0000, 'testTag', `[MyLogManager] 删除失败: ${file}, error: ${e}`);
       }
     }
   };

   // 定义ExternalLogManager实现
   let myLogManager: hiAppEvent.ExternalLogManager = {
     onCapacityReached(container: hiAppEvent.ExternalLogContainer): void {
       hilog.info(0x0000, 'testTag', `[MyLogManager] 容量达到阈值，日志数量: ${container.getLogNumber()}`);

       // 获取所有日志文件路径
       let allFiles: Set<string> = container.getAllLogFiles();
       hilog.info(0x0000, 'testTag', `[MyLogManager] 所有日志文件: ${JSON.stringify(Array.from(allFiles))}`);

       // 获取所有日志详情
       let allLogs: Set<hiAppEvent.ExternalLogWrapper> = container.getAllLogs();
       for (const log of Array.from(allLogs)) {
         hilog.info(0x0000, 'testTag', `[MyLogManager] 文件: ${log.getFilePath()}, ` +
           `时间: ${log.getGenerationTime()}, ` +
           `大小: ${log.getSizeInKb()}KB, ` +
           `事件: ${log.getSysEvent()}`);
       }

       // 按事件类型过滤的日志
       let crashFiles: Set<string> = container.getLogFilesOfSysEvent('APP_CRASH');
       hilog.info(0x0000, 'testTag', `[MyLogManager] APP_CRASH 日志: ${JSON.stringify(Array.from(crashFiles))}`);

       // 按时间过滤日志，获取5分钟前生成的日志
       let timePoint = Date.now() - 5 * 60 * 1000;
       let files: Set<string> = container.getLogFilesGeneratedBefore(timePoint);
       hilog.info(0x0000, 'testTag', `[MyLogManager] 5分钟前的日志: ${JSON.stringify(Array.from(files))}`);

       // 按时间过滤，获取5分钟内生成的日志
       files = container.getLogFilesGeneratedAfter(timePoint);
       hilog.info(0x0000, 'testTag', `[MyLogManager] 5分钟内的日志: ${JSON.stringify(Array.from(files))}`);

       // 按大小过滤，获取大于100KB的日志
       files = container.getLogFilesLargerThan(100);
       hilog.info(0x0000, 'testTag', `[MyLogManager] 大于100KB的日志: ${JSON.stringify(Array.from(files))}`);

       // 按大小过滤，获取小于100KB的日志
       files = container.getLogFilesSmallerThan(100);
       hilog.info(0x0000, 'testTag', `[MyLogManager] 小于100KB的日志: ${JSON.stringify(Array.from(files))}`);

       // 获取最早生成的3个日志文件，并删除
       files = container.getFirstGeneratedLogFiles(3);
       hilog.info(0x0000, 'testTag', `[MyLogManager] 最早的3个日志: ${JSON.stringify(Array.from(files))}`);
       deleteFiles(Array.from(files));
     }
   };

   // 注册external_log日志文件管理者
   try {
     hiAppEvent.registerExternalLogManager(myLogManager);
     hilog.info(0x0000, 'testTag', '[MyLogManager] ExternalLogManager 注册成功');
   } catch (e) {
     hilog.info(0x0000, 'testTag', `[MyLogManager] 注册失败: ${e.code}, ${e.message}`);
   }

   // 检查是否已注册
   let registered: boolean = hiAppEvent.isExternalLogManagerRegistered();
   hilog.info(0x0000, 'testTag', `[MyLogManager] 已注册: ${registered}`);
   ```

## 调测验证

1. 点击DevEco Studio界面中的运行按钮，运行应用工程。
2. 在HiLog窗口搜索“MyLogManager”关键字，查看应用注册external\_log日志管理者的日志：

   ```text
   [MyLogManager] ExternalLogManager 注册成功
   [MyLogManager] 已注册: true
   ```
3. 这里以[订阅崩溃事件（ArkTS）](hiappevent-watcher-crash-events-arkts.md)为例，每隔一分钟触发一次应用的崩溃事件，直到沙箱目录达到阈值。
4. 在HiLog窗口搜索“MyLogManager”关键字，查看external\_log目录达到阈值收到回调的日志：

   ```text
   [MyLogManager] 容量达到阈值，日志数量: 11
   [MyLogManager] 文件: /data/storage/el2/log/hiappevent/APP_CRASH_1788340658144_14537_0.log, 时间: 1788340658144, 大小: 470KB, 事件: APP_CRASH
   ...
   [MyLogManager] 文件: /data/storage/el2/log/hiappevent/APP_CRASH_1788340823716_15778_0.log, 时间: 1788340823716, 大小: 50KB, 事件: APP_CRASH
   [MyLogManager] APP_CRASH 日志: ["/data/storage/el2/log/hiappevent/APP_CRASH_1788340658144_14537_0.log",..."/data/storage/el2/log/hiappevent/APP_CRASH_1788340418807_12609_0.log"]
   [MyLogManager] 5分钟前的日志: ["/data/storage/el2/log/hiappevent/APP_CRASH_1788340353265_12024_0.log",..."/data/storage/el2/log/hiappevent/APP_CRASH_1788340418807_12609_0.log"]
   [MyLogManager] 5分钟内的日志: ["/data/storage/el2/log/hiappevent/APP_CRASH_1788340658144_14537_0.log",...,"/data/storage/el2/log/hiappevent/APP_CRASH_1788340823716_15778_0.log"]
   [MyLogManager] 大于100KB的日志: ["/data/storage/el2/log/hiappevent/APP_CRASH_1788340658144_14537_0.log",...,"/data/storage/el2/log/hiappevent/APP_CRASH_1788340823714_15778_0.log"]
   [MyLogManager] 小于100KB的日志: ["/data/storage/el2/log/hiappevent/APP_CRASH_1788340708211_14892_0.log","/data/storage/el2/log/hiappevent/APP_CRASH_1788340823716_15778_0.log"]
   [MyLogManager] 最早的3个日志: ["/data/storage/el2/log/hiappevent/APP_CRASH_1788340353265_12024_0.log","/data/storage/el2/log/hiappevent/APP_CRASH_1788340362652_12116_0.log","/data/storage/el2/log/hiappevent/APP_CRASH_1788340374253_12272_0.log"]
   [MyLogManager] 已删除: /data/storage/el2/log/hiappevent/APP_CRASH_1788340353265_12024_0.log
   [MyLogManager] 已删除: /data/storage/el2/log/hiappevent/APP_CRASH_1788340362652_12116_0.log
   [MyLogManager] 已删除: /data/storage/el2/log/hiappevent/APP_CRASH_1788340374253_12272_0.log
   ```
