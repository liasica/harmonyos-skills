---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-faq
title: HiAppEvent常见问题
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > HiAppEvent常见问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:06272e48acace848cf2cd8203b6c7caeb056b257aa61553738c12afeb775c4b8
---

## 查不到已通过HiAppEvent订阅的事件内容

**问题现象**

在开发调试阶段，崩溃、应用冻屏等故障发生后，无法在DevEco Studio的HiLog窗口中获取已通过HiAppEvent订阅的事件内容。

**可能的原因&解决措施**

发生崩溃、应用冻屏等故障后，应用已退出。

解决办法：再次启动应用，查看相应的事件内容。

## 无法获取external\_log日志文件

**问题现象**

Hilog中出现如下日志：

* eventInfo.params.external\_log=[]
* HiAppEvent file does not exist

**可能的原因&解决措施**

**情况一**：

external\_log日志文件所在目录的空间已达到上限。

external\_log所在的目录为[应用沙箱目录](app-sandbox-directory.md)，目录空间受限。log\_over\_limit字段用于判断external\_log日志文件所在目录的空间是否达到上限。如果log\_over\_limit的值为true，表示external\_log日志文件所在目录空间已达到上限，事件包含的日志文件将无法写入。

external\_log是一个字符串数组。例如：

external\_log=["/data/storage/el2/log/hiappevent/APP\_CRASH\_时间戳\_xxxx.log"]。

**可采取的解决措施**：

参考[无法删除external\_log日志文件](hiappevent-faq.md#无法删除external_log日志文件)中的解决措施，清理历史日志文件。

**情况二**：

部分系统事件（如启动耗时事件）本身没有external\_log，因而没有external\_log日志文件。

**可采取的解决措施**：

查看对应的事件介绍章节，确认事件是否包含external\_log：[系统事件](event-subscription-overview.md#系统事件)。

**情况三**：

事件发生在事件订阅之前。

在调用事件订阅接口addWatcher()前，没有开始监听系统事件。因此事件订阅之前的事件没有external\_log日志文件。

**可采取的解决措施**：

确认事件订阅与事件发生的时序关系。先事件订阅，然后事件发生，才能获取到事件的external\_log日志文件。

**情况四**：

系统事件没有触发成功。

如果系统事件没发生，就不会有external\_log日志文件。

**可采取的解决措施**：

查看系统事件的其他日志，确认系统事件是否已经触发成功。

**情况五**：

external\_log日志文件生成后又被删除了。

例如，在一个应用中，A和B两个模块都订阅了系统事件C。A模块处理完系统事件C的回调后，删除了external\_log日志文件。随后B模块在系统事件C的回调中访问external\_log日志文件，会提示日志文件不存在。

**可采取的解决措施**：

检查其他模块是否已删除external\_log日志文件。

## 无法删除external\_log日志文件

**问题现象**

external\_log日志文件所在目录的空间已达到上限，但无法删除external\_log日志文件。

**解决措施**

* 开发者如果有权限访问设备的“/data/app/el2/100/log/应用包名”目录，可以手动删除external\_log日志文件。文件目录为/data/app/el2/100/log/应用包名/hiappevent（或resourcelimit或watchdog）。
* 开发者若没有权限访问设备的“/data/app/el2/100/log/应用包名”目录，可以在应用代码中删除external\_log日志文件。代码示例如下。文件删除接口可以参考[fileIo.unlink](../harmonyos-references/js-apis-file-fs.md#fileiounlink)。

**代码示例**

```
1. import { fileIo } from '@kit.CoreFileKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';

5. hiAppEvent.addWatcher({
6. // 开发者可以自定义观察者名称，系统会使用名称来标识不同的观察者
7. name: "AppCrashWatcher",
8. // 订阅过滤条件，这里是订阅了系统事件中的崩溃事件
9. appEventFilters: [
10. {
11. domain: hiAppEvent.domain.OS,
12. names: [hiAppEvent.event.APP_CRASH]
13. }
14. ],
15. // 实现onReceive回调，监听到事件后实时回调
16. onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
17. hilog.info(0x0000, 'testTag', `domain=${domain}`);
18. for (const eventGroup of appEventGroups) {
19. hilog.info(0x0000, 'testTag', `HiAppEvent eventName=${eventGroup.name}`);
20. for (const eventInfo of eventGroup.appEventInfos) {
21. // 开发者可以获取到崩溃事件发生的时间戳
22. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.time=${JSON.stringify(eventInfo.params['time'])}`);
23. // 开发者可以获取到崩溃应用的包名
24. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.bundle_name=${JSON.stringify(eventInfo.params['bundle_name'])}`);
25. // 开发者可以获取到崩溃事件发生时的故障日志文件
26. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.external_log=${JSON.stringify(eventInfo.params['external_log'])}`);

28. if (eventInfo.params['external_log'] != undefined) {
29. for (let index = 0; index < eventInfo.params['external_log'].length; ++index) {
30. let externalLog: string = eventInfo.params['external_log'][index];
31. hilog.info(0x0000, 'testTag', `externalLog=${externalLog}`);
32. // 验证访问权限：
33. let res = fileIo.accessSync(externalLog);
34. if (res) {
35. hilog.info(0x0000, 'testTag', `HiAppEvent file exists`);
36. } else {
37. hilog.error(0x0000, 'testTag', `HiAppEvent file does not exist`);
38. }
39. // 验证读写权限：
40. fileIo.open(externalLog, fileIo.OpenMode.READ_WRITE).then((file: fileIo.File) => {
41. hilog.info(0x0000, 'testTag', `HiAppEvent file=${externalLog} fd=${file.fd}`);
42. fileIo.closeSync(file);
43. }).catch((err: BusinessError) => {
44. hilog.info(0x0000, 'testTag',
45. `HiAppEvent open file=${externalLog} failed with error message=${err.message}, error code=${err.code}`);
46. });
47. // 删除external_log日志文件：
48. fileIo.unlink(externalLog).then(() => {
49. console.info("HiAppEvent remove file:" + externalLog + " succeed");
50. }).catch((err: BusinessError) => {
51. console.error("HiAppEvent remove file:" + externalLog + " failed with error message: " + err.message +
52. ", error code: " + err.code);
53. });
54. }
55. }
56. }
57. }
58. }
59. });
```

访问及删除external\_log日志文件的日志：

```
1. externalLog=/data/storage/el2/log/hiappevent/APP_CRASH_1751081104816_35595.log
2. HiAppEvent file exists
3. HiAppEvent file=/data/storage/el2/log/hiappevent/APP_CRASH_1751081104816_35595.log fd=61
4. HiAppEvent remove file:/data/storage/el2/log/hiappevent/APP_CRASH_1751081104816_35595.log succeed
```

说明

external\_log返回的路径是应用沙箱目录，非真实物理路径。应用有权限访问自己的沙箱目录。external\_log日志空间受限，应用处理完日志文件后应及时删除。

## 同一应用内，事件的回调不区分线程、进程

例如，在同一个应用内，有A、B两个进程，进程A已调用addWatcher()接口订阅崩溃事件。如果进程B发生崩溃，进程A能收到进程B的崩溃回调。只要进程A和B的应用名一致即可。

**接口参考链接**

[hiAppEvent.addWatcher](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventaddwatcher)。
