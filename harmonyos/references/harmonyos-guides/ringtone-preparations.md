---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ringtone-preparations
title: 设置铃声
breadcrumb: 指南 > 媒体 > Ringtone Kit（铃声服务） > 设置铃声
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9cec4354880af49316af2f9758c55cffd27496ef0b314cf4a6f754bc502add46
---

1. 导入ringtone模块和相关公共模块。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { ringtone } from '@kit.RingtoneKit'
   3. import { uniformTypeDescriptor } from '@kit.ArkData';
   4. import { JSON } from '@kit.ArkTS';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';
   6. const APP_TAG = "Msc_Demo"
   7. const DOMAIN = 0x0001
   ```
2. 调用[ringtone.getSupportedRingtoneTypes](../harmonyos-references/ringtone-ringtone.md#ringtonegetsupportedringtonetypes)接口，查询支持设置的铃声类型。

   ```
   1. let ringtoneTypeList: Array<ringtone.RingtoneType> = ringtone.getSupportedRingtoneTypes();
   2. hilog.info(DOMAIN, APP_TAG,'getSupportedRingtoneTypes : ' + JSON.stringify(ringtoneTypeList));
   ```
3. 调用[ringtone.getSupportedDataTypes](../harmonyos-references/ringtone-ringtone.md#ringtonegetsupporteddatatypes)接口，查询支持的数据类型。当前支持格式：MP3，OGG，FLAC，AAC，MP2，M4A。

   ```
   1. // 其中 ringtone.RingtoneType.NOTIFICATION 为通知铃声
   2. let dataTypeList: Array<uniformTypeDescriptor.UniformDataType> = ringtone.getSupportedDataTypes(ringtone.RingtoneType.NOTIFICATION);
   3. hilog.info(DOMAIN, APP_TAG,'getSupportedDataTypes: ' + JSON.stringify(dataTypeList));
   ```
4. 调用[ringtone.startRingtoneSetting](../harmonyos-references/ringtone-ringtone.md#ringtonestartringtonesetting)接口拉起设置弹窗，用户设置铃声后返回设置的铃声类型。

   通过promise异步方式：

   ```
   1. // 详细代码参考API参考
   2. let prefixUri: string = '';
   3. let audioPath: string = prefixUri + '/' + this.buttonText;
   4. let fileName: string = audioPath.substring(audioPath.lastIndexOf('/') + 1, audioPath.lastIndexOf('.'));
   5. await ringtone.startRingtoneSetting(this.context, audioPath, fileName).then(res => {
   6. hilog.info(DOMAIN, APP_TAG,'setFlag :' + res);
   7. });
   ```

   通过callback异步方式：

   ```
   1. // 详细代码参考API参考
   2. let prefixUri: string = '';
   3. let audioPath: string = prefixUri + '/' + this.buttonText;
   4. let fileName: string = audioPath.substring(audioPath.lastIndexOf('/') + 1, audioPath.lastIndexOf('.'));
   5. ringtone.startRingtoneSetting(this.context, audioPath, fileName, (err, data) => {
   6. hilog.info(DOMAIN, APP_TAG,'setFlag :' + data);
   7. });
   ```
5. 调用[ringtone.getSupportedMaxDuration](../harmonyos-references/ringtone-ringtone.md#ringtonegetsupportedmaxduration)接口，获取当前铃声支持的最大时长。

   ```
   1. // 其中 ringtone.RingtoneType.MESSAGE 为短信铃声
   2. let maxDuration: number =
   3. ringtone.getSupportedMaxDuration(ringtone.RingtoneType.MESSAGE, uniformTypeDescriptor.UniformDataType.MP3)
   4. hilog.info(DOMAIN, APP_TAG,'getSupportedMaxDuration: ' + maxDuration);
   ```
