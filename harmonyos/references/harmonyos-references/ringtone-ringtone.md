---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ringtone-ringtone
title: ringtone（铃声服务）
breadcrumb: API参考 > 媒体 > Ringtone Kit（铃声服务） > ArkTS API > ringtone（铃声服务）
category: harmonyos-references
scraped_at: 2026-04-28T08:14:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:32ca1c1f45773057b97f858211696ef8abc9caaf24b54358ecfb02f6ef6dffd7
---

ringtone提供铃声设置的功能。

**起始版本：** 5.0.0(12)

## 导入模块

PhoneTablet

```
1. import { ringtone } from '@kit.RingtoneKit'
```

## RingtoneType

PhoneTablet

描述铃声的类型枚举。

系统能力：SystemCapability.Ringtone.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CALL | 0 | 来电铃声。 |
| MESSAGE | 1 | 信息铃声。 |
| NOTIFICATION | 2 | 通知铃声。 |
| ALARM | 3 | 闹钟铃声。 |

## RingtoneErrors

PhoneTablet

该枚举为设置铃声，获取铃声支持类型和获取铃声支持文件类型等接口的错误码。

**系统能力：** SystemCapability.Ringtone.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ERROR\_INVALID\_PARAM | 401 | 参数非法。 |
| ERROR\_USER\_CANCELED | 1011600001 | 用户取消。 |
| ERROR\_FILE\_NOT\_FOUND | 1011600002 | 文件不存在。 |
| ERROR\_SHOW\_FAILED | 1011600003 | 铃声弹框失败。 |
| ERROR\_CALL\_SYSTEM\_API\_FAILED | 1011600004 | 调用系统接口失败。 |
| ERROR\_SYSTEM | 1011699999 | 系统内部错误。 |

## ringtone.getSupportedRingtoneTypes

PhoneTablet

getSupportedRingtoneTypes(): Array<RingtoneType>

查询当前系统支持自定义的铃声类型。

**系统能力：** SystemCapability.Ringtone.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[RingtoneType](ringtone-ringtone.md#ringtonetype)> | 当前系统支持自定义的铃声类型。 |

**示例：**

```
1. import { ringtone } from '@kit.RingtoneKit'
2. import { JSON } from '@kit.ArkTS';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const APP_TAG = "Msc_Demo"
6. const DOMAIN = 0x0001

8. @Entry
9. @Component
10. struct Index {
11. build() {
12. Stack() {
13. Column() {
14. Button("查询当前系统支持自定义的铃声类型")
15. .width(200)
16. .height(50)
17. .onClick(() => {
18. let typeList: Array<ringtone.RingtoneType> = ringtone.getSupportedRingtoneTypes()
19. hilog.info(DOMAIN, APP_TAG, 'getSupportedRingtoneTypes : ' + JSON.stringify(typeList));
20. })
21. }
22. .width('100%')
23. .height('100%')
24. .backgroundColor(Color.Pink)
25. }
26. .height('100%')
27. .width('100%')
28. }
29. }
```

## ringtone.getSupportedDataTypes

PhoneTablet

getSupportedDataTypes(ringtoneType: RingtoneType): Array<uniformTypeDescriptor.UniformDataType>

查询对应铃声类型支持的文件类型。

**系统能力**：SystemCapability.Ringtone.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ringtoneType | [RingtoneType](ringtone-ringtone.md#ringtonetype) | 是 | 待查询的铃声类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[uniformTypeDescriptor.UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)> | 返回对应铃声类型支持的文件类型。 |

**错误码：**

以下错误码的详细介绍请参见铃声服务[ArkTS API错误码](ringtone-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter invalid. |

**示例：**

```
1. import { ringtone } from '@kit.RingtoneKit'
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { uniformTypeDescriptor } from '@kit.ArkData';
4. import { JSON } from '@kit.ArkTS';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. const APP_TAG = "Msc_Demo"
8. const DOMAIN = 0x0001

10. @Entry
11. @Component
12. struct Index {
13. build() {
14. Stack() {
15. Column() {
16. Button("查询支持的文件类型")
17. .width(200)
18. .height(50)
19. .onClick(() => {
20. try {
21. let typeList: Array<uniformTypeDescriptor.UniformDataType> =
22. ringtone.getSupportedDataTypes(ringtone.RingtoneType.NOTIFICATION)
23. hilog.info(DOMAIN, APP_TAG, 'getSupportedDataTypes3----- : ' + JSON.stringify(typeList));
24. } catch (error) {
25. let err: BusinessError = error as BusinessError;
26. hilog.error(DOMAIN, APP_TAG,
27. 'getSupportedDataType error message: ' + err.message + ', error code: ' + err.code);
28. }
29. })
30. }
31. .width('100%')
32. .height('100%')
33. .backgroundColor(Color.Pink)
34. }
35. .height('100%')
36. .width('100%')
37. }
38. }
```

## ringtone.getSupportedMaxDuration

PhoneTablet

getSupportedMaxDuration(ringtoneType: RingtoneType, dataType: uniformTypeDescriptor.UniformDataType): number

查询对应铃声类型以及文件类型支持的时长。

**系统能力**：SystemCapability.Ringtone.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ringtoneType | [RingtoneType](ringtone-ringtone.md#ringtonetype) | 是 | 待查询的铃声类型。 |
| dataType | [uniformTypeDescriptor.UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype) | 是 | 待查询的文件类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回对应类型的铃声和文件支持的最大时长（单位：秒），其中闹钟铃声时长为300s，短信铃声和通知铃声时长为7s，来电铃声时长为60s。 |

**错误码：**

以下错误码的详细介绍请参见铃声服务[ArkTS API错误码](ringtone-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter invalid. |

**示例：**

```
1. import { ringtone } from '@kit.RingtoneKit'
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { uniformTypeDescriptor } from '@kit.ArkData';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. const APP_TAG = "Msc_Demo"
7. const DOMAIN = 0x0001

9. @Entry
10. @Component
11. struct Index {
12. build() {
13. Stack() {
14. Column() {
15. Button("查询最大时长")
16. .width(200)
17. .height(50)
18. .onClick(() => {
19. try {
20. let maxDuration: number =
21. ringtone.getSupportedMaxDuration(ringtone.RingtoneType.MESSAGE,
22. uniformTypeDescriptor.UniformDataType.MP3)
23. hilog.info(DOMAIN, APP_TAG, 'getSupportedMaxDuration: ' + maxDuration);
24. } catch (error) {
25. let err: BusinessError = error as BusinessError;
26. hilog.error(DOMAIN, APP_TAG,
27. 'getSupportedMaxDuration error message: ' + err.message + ', error code: ' + err.code);
28. }
29. })
30. }
31. .width('100%')
32. .height('100%')
33. .backgroundColor(Color.Pink)
34. }
35. .height('100%')
36. .width('100%')
37. }
38. }
```

## ringtone.startRingtoneSetting

PhoneTablet

startRingtoneSetting(context: common.UIAbilityContext, path: string, name: string, callback: AsyncCallback<RingtoneType>): void

拉起设置铃声弹窗，并返回点击的铃声类型，使用Callback异步回调。

**系统能力**：SystemCapability.Ringtone.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | UIAbility上下文。 |
| path | string | 是 | 具有访问权限的文件路径。 |
| name | string | 是 | 文件名，限制长度1000。 |
| callback | AsyncCallback<[RingtoneType](ringtone-ringtone.md#ringtonetype)> | 是 | Callback对象。返回用户选择设置的铃声类型。 |

**错误码：**

以下错误码的详细介绍请参见铃声服务[ArkTS API错误码](ringtone-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter invalid. |
| 1011600001 | User canceled. |
| 1011600002 | The media file is not found. |
| 1011600003 | Failed to show the dialog box. |
| 1011600004 | Failed to call the system API. |
| 1011699999 | System exception. |

```
1. import { common } from '@kit.AbilityKit';
2. import { ringtone } from '@kit.RingtoneKit'
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { JSON } from '@kit.ArkTS';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. const APP_TAG = "Msc_Demo"
8. const DOMAIN = 0x0001

10. @Entry
11. @Component
12. struct Index {
13. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

15. build() {
16. Stack() {
17. Column() {
18. Button("设为铃声OGG格式")
19. .width(200)
20. .height(50)
21. .onClick(async () => {
22. let audioPath: string = this.context.filesDir + '/test.ogg'
23. let splitList = audioPath.split('/')
24. let fileName = splitList[splitList.length - 1]
25. hilog.info(DOMAIN, APP_TAG, 'audioPath:' + audioPath)
26. hilog.info(DOMAIN, APP_TAG, 'fileName:' + fileName)

28. try {
29. ringtone.startRingtoneSetting(this.context, audioPath, fileName, (err, res) => {
30. hilog.info(DOMAIN, APP_TAG, '返回值：' + JSON.stringify(res))
31. })
32. } catch (error) {
33. let err: BusinessError = error as BusinessError;
34. hilog.error(DOMAIN, APP_TAG,
35. 'accessSync failed with error message: ' + err.message + ', error code: ' + err.code);
36. }
37. })
38. }
39. .width('100%')
40. .height('100%')
41. .backgroundColor(Color.Pink)
42. }
43. .height('100%')
44. .width('100%')
45. }
46. }
```

## ringtone.startRingtoneSetting

PhoneTablet

startRingtoneSetting(context: common.UIAbilityContext, path: string, name: string): Promise<RingtoneType>

拉起设置铃声弹窗，并返回点击的铃声类型，使用Promise异步回调。

**系统能力**：SystemCapability.Ringtone.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | UIAbility上下文。 |
| path | string | 是 | 具有访问权限的文件路径。 |
| name | string | 是 | 文件名，限制长度1000。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RingtoneType](ringtone-ringtone.md#ringtonetype)> | Promise对象。返回用户选择设置的铃声类型。 |

**错误码：**

以下错误码的详细介绍请参见铃声服务[ArkTS API错误码](ringtone-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter invalid. |
| 1011600001 | User canceled. |
| 1011600002 | The media file is not found. |
| 1011600003 | Failed to show the dialog box. |
| 1011600004 | Failed to call the system API. |
| 1011699999 | System exception. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { ringtone } from '@kit.RingtoneKit'
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { JSON } from '@kit.ArkTS';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. const APP_TAG = "Msc_Demo"
8. const DOMAIN = 0x0001

10. @Entry
11. @Component
12. struct Index {
13. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

15. build() {
16. Stack() {
17. Column() {
18. Button("设为铃声OGG格式")
19. .width(200)
20. .height(50)
21. .onClick(async () => {
22. let audioPath: string = this.context.filesDir + '/test.ogg'
23. let splitList = audioPath.split('/')
24. let fileName = splitList[splitList.length - 1]
25. hilog.info(DOMAIN, APP_TAG, 'audioPath:' + audioPath)
26. hilog.info(DOMAIN, APP_TAG, 'fileName:' + fileName)
27. try {
28. await ringtone.startRingtoneSetting(this.context, audioPath, fileName).then(res => {
29. hilog.info(DOMAIN, APP_TAG, '返回值：' + JSON.stringify(res))
30. })
31. } catch (error) {
32. let err: BusinessError = error as BusinessError;
33. hilog.error(DOMAIN, APP_TAG,
34. 'accessSync failed with error message: ' + err.message + ', error code: ' + err.code);
35. }
36. })
37. }
38. .width('100%')
39. .height('100%')
40. .backgroundColor(Color.Pink)
41. }
42. .height('100%')
43. .width('100%')
44. }
45. }
```
