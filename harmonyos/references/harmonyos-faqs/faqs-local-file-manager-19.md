---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-19
title: 如何保存faultLogger
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何保存faultLogger
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3703a8a87d0816f6a623af4d666ec83e2e3f7c13b233bd0cd5b930a4b38cf022
---

**参考代码**

```ts
import { fileIo } from '@kit.CoreFileKit';
import { FaultLogger, hilog } from '@kit.PerformanceAnalysisKit';
import { AbilityConstant, common } from '@kit.AbilityKit';
import { preferences } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = 'FaultLoggerUtils';

export class LogUtils {
  static async queryAndUploadFaultLog(context: common.UIAbilityContext, launchParam: AbilityConstant.LaunchParam) {
    if (launchParam.lastExitReason == AbilityConstant.LastExitReason.NORMAL) {
      hilog.info(0x00000, TAG, 'No exceptions occurred when the application was last exited');
      return;
    }
    let value: Array<FaultLogger.FaultLogInfo> = await FaultLogger.query(FaultLogger.FaultType.NO_SPECIFIC)
    hilog.info(0x00000, TAG, 'error log:' + value.toString());
    if (value) {
      let len = value.length;
      hilog.info(0x00000, TAG, 'Number of error logs:' + len);
      if (len === 0) {
        return;
      }
      // Get instance
      let preference: preferences.Preferences = await preferences.getPreferences(context, 'STLiveness');
      // Query the timestamp of the last processing time
      let lastFaultHandleTime = preference.getSync('faultHandleTime', 0);
      hilog.info(0x0000, TAG, 'lastFaultHandleTime:' + lastFaultHandleTime);
      for (let i = 0; i < len; i++) {
        let timestamp = value[i].timestamp;
        hilog.info(0x00000, TAG, 'Log File Name#' + timestamp);
        if (lastFaultHandleTime >= timestamp) {
          hilog.error(0x00000, TAG, 'Maple No New Logs.');
          return;
        }
        // Save the log to the application sandbox directory with the file name "timestamp.log"
        await LogUtils.save(value[i].fullLog, context.filesDir + '/crash', timestamp + '.log');
        await preference.put('faultHandleTime', timestamp);
        await preference.flush();
      }
    }
  }
  static async save(buffer: ArrayBuffer | string, destFilePath: string, name: string): Promise<string> {
    await LogUtils.mkdir(destFilePath);
    hilog.info(0x00000, TAG, 'Write content:' + buffer);
    hilog.info(0x00000, TAG, 'Log file path:' + destFilePath);
    if (buffer) {
      try {
        let file = fileIo.openSync(destFilePath + '/' + name, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
        fileIo.writeSync(file.fd, buffer);
        fileIo.closeSync(file);
      } catch (error) {
        let e: BusinessError = error as BusinessError;
        hilog.info(0x0000, TAG, 'FileUtils:save:::' + e.message);
      }
    }
    return destFilePath;
  }

  static async mkdir(destFilePath: string) {
    hilog.info(0x00000, TAG, 'Start creating the directory:' + destFilePath);
    if (fileIo.accessSync(destFilePath)) {
      hilog.info(0x00000, TAG, 'The directory already exists, no need to create it.');
      return;
    }
    await fileIo.mkdir(destFilePath);
    hilog.info(0x00000, TAG, 'Create completed');
  }
}
```
