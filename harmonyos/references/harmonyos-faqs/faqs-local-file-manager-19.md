---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-19
title: 如何保存faultLogger
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何保存faultLogger
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3094fd831787f9757bdf4ffcd4cb9a9fa57a24943c81b28c23440a1c32e4b9dd
---

**参考代码**

```
1. import { fileIo } from '@kit.CoreFileKit';
2. import { FaultLogger, hilog } from '@kit.PerformanceAnalysisKit';
3. import { AbilityConstant, common } from '@kit.AbilityKit';
4. import { preferences } from '@kit.ArkData';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. const TAG: string = 'FaultLoggerUtils';

9. export class LogUtils {
10. static async queryAndUploadFaultLog(context: common.UIAbilityContext, launchParam: AbilityConstant.LaunchParam) {
11. if (launchParam.lastExitReason == AbilityConstant.LastExitReason.NORMAL) {
12. hilog.info(0x00000, TAG, 'No exceptions occurred when the application was last exited');
13. return;
14. }
15. let value: Array<FaultLogger.FaultLogInfo> = await FaultLogger.query(FaultLogger.FaultType.NO_SPECIFIC)
16. hilog.info(0x00000, TAG, 'error log:' + value.toString());
17. if (value) {
18. let len = value.length;
19. hilog.info(0x00000, TAG, 'Number of error logs:' + len);
20. if (len === 0) {
21. return;
22. }
23. // Get instance
24. let preference: preferences.Preferences = await preferences.getPreferences(context, 'STLiveness');
25. // Query the timestamp of the last processing time
26. let lastFaultHandleTime = preference.getSync('faultHandleTime', 0);
27. hilog.info(0x0000, TAG, 'lastFaultHandleTime:' + lastFaultHandleTime);
28. for (let i = 0; i < len; i++) {
29. let timestamp = value[i].timestamp;
30. hilog.info(0x00000, TAG, 'Log File Name#' + timestamp);
31. if (lastFaultHandleTime >= timestamp) {
32. hilog.error(0x00000, TAG, 'Maple No New Logs.');
33. return;
34. }
35. // Save the log to the application sandbox directory with the file name "timestamp.log"
36. await LogUtils.save(value[i].fullLog, context.filesDir + '/crash', timestamp + '.log');
37. await preference.put('faultHandleTime', timestamp);
38. await preference.flush();
39. }
40. }
41. }
42. static async save(buffer: ArrayBuffer | string, destFilePath: string, name: string): Promise<string> {
43. await LogUtils.mkdir(destFilePath);
44. hilog.info(0x00000, TAG, 'Write content:' + buffer);
45. hilog.info(0x00000, TAG, 'Log file path:' + destFilePath);
46. if (buffer) {
47. try {
48. let file = fileIo.openSync(destFilePath + '/' + name, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
49. fileIo.writeSync(file.fd, buffer);
50. fileIo.closeSync(file);
51. } catch (error) {
52. let e: BusinessError = error as BusinessError;
53. hilog.info(0x0000, TAG, 'FileUtils:save:::' + e.message);
54. }
55. }
56. return destFilePath;
57. }

59. static async mkdir(destFilePath: string) {
60. hilog.info(0x00000, TAG, 'Start creating the directory:' + destFilePath);
61. if (fileIo.accessSync(destFilePath)) {
62. hilog.info(0x00000, TAG, 'The directory already exists, no need to create it.');
63. return;
64. }
65. await fileIo.mkdir(destFilePath);
66. hilog.info(0x00000, TAG, 'Create completed');
67. }
68. }
```

[FaultLog.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/LocationKit/entry/src/main/ets/pages/FaultLog.ets#L21-L88)
