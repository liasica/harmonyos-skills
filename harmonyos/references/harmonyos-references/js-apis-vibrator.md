---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vibrator
title: @ohos.vibrator (振动)
breadcrumb: API参考 > 系统 > 硬件 > Sensor Service Kit（传感器服务） > ArkTS API > @ohos.vibrator (振动)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:90b74885197b1c0a8754a8f5aab07cc0ec1f0c20be26b7a089aaf90645afa948
---

vibrator模块提供控制设备马达振动的能力。包括启动指定时长、预置效果、自定义文件等模式的振动；停止指定时长、预置效果或所有模式的振动。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { vibrator } from '@kit.SensorServiceKit';
```

## vibrator.startVibration9+

PhonePC/2in1TabletTVWearable

startVibration(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback<void>): void

根据指定的振动效果和振动属性触发马达振动。使用callback异步回调。

**需要权限**：ohos.permission.VIBRATE

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effect | [VibrateEffect](js-apis-vibrator.md#vibrateeffect9) | 是 | 马达振动效果，支持四种：  1、[VibratePreset](js-apis-vibrator.md#vibratepreset9)：按照预置振动效果触发马达振动，适用于交互反馈类的短振场景（如点击长按，滑动，拖拽等），为确保与系统整体振感反馈体验风格一致，推荐使用此接口；  2、[VibrateFromFile](js-apis-vibrator.md#vibratefromfile10)：按照文件形式定制自定义振动效果触发马达振动，适用于匹配复杂场景效果的交互反馈（如表情包触发的拟真效果、游戏场景/操作反馈）；  3、[VibrateTime](js-apis-vibrator.md#vibratetime9)：按照指定时长触发马达振动，仅对振动时长进行启动或停止控制，满足基础功能，无法对振动强度、频率等维度进行个性化设置，此种振动调节不够细腻，无法满足精致体验；  4、[VibrateFromPattern18+](js-apis-vibrator.md#vibratefrompattern18)：按照自定义振动效果触发马达振动。使用场景和VibrateFromFile一致。VibrateFromFile是面向文件中提前定制好的效果，将具体的振动事件以文件描述符形式传递到接口中；VibrateFromPattern提供更加灵活的振动事件排列组合，将振动事件以振动事件数组的形式传递到接口中。 |
| attribute | [VibrateAttribute](js-apis-vibrator.md#vibrateattribute9) | 是 | 马达振动属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当马达振动成功，err为undefined；否则为错误对象，包含错误码和错误信息。 |

**错误码**：

以下错误码的详细介绍请参见[振动错误码](errorcode-vibrator.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14600101 | Device operation failed. |

**示例**：

1. 按照预置振动效果触发马达振动：

   ```
   1. import { vibrator } from '@kit.SensorServiceKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. // 使用try catch对可能出现的异常进行捕获
   5. try {
   6. // 查询是否支持'haptic.notice.success'
   7. vibrator.isSupportEffect('haptic.notice.success', (err: BusinessError, state: boolean) => {
   8. if (err) {
   9. console.error(`Failed to query effect. Code: ${err.code}, message: ${err.message}`);
   10. return;
   11. }
   12. console.info('Succeed in querying effect');
   13. if (state) {
   14. try {
   15. vibrator.startVibration({
   16. type: 'preset',
   17. effectId: 'haptic.notice.success',
   18. count: 1,
   19. }, {
   20. usage: 'notification' // 根据实际选择类型归属不同的开关管控
   21. }, (error: BusinessError) => {
   22. if (error) {
   23. console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
   24. return;
   25. }
   26. console.info('Succeed in starting vibration');

   28. });
   29. } catch (err) {
   30. let e: BusinessError = err as BusinessError;
   31. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   32. }
   33. }
   34. })
   35. } catch (error) {
   36. let e: BusinessError = error as BusinessError;
   37. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   38. }
   ```
2. 按照自定义振动配置文件触发马达振动：

   ```
   1. import { vibrator } from '@kit.SensorServiceKit';
   2. import { resourceManager } from '@kit.LocalizationKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. const fileName: string = 'xxx.json';

   7. @Entry
   8. @Component
   9. struct Index {
   10. uiContext = this.getUIContext();

   12. build() {
   13. Row() {
   14. Column() {
   15. Button('alarm-file')
   16. .onClick(() => {
   17. let rawFd: resourceManager.RawFileDescriptor | undefined = this.uiContext.getHostContext()?.resourceManager.getRawFdSync(fileName);
   18. if (rawFd != undefined) {
   19. try {
   20. vibrator.startVibration({
   21. type: "file",
   22. hapticFd: { fd: rawFd.fd, offset: rawFd.offset, length: rawFd.length }
   23. }, {
   24. id: 0,
   25. usage: 'alarm' // 根据实际选择类型归属不同的开关管控
   26. }, (error: BusinessError) => {
   27. if (error) {
   28. console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
   29. return;
   30. }
   31. console.info('Succeed in starting vibration');
   32. });
   33. } catch (err) {
   34. let e: BusinessError = err as BusinessError;
   35. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   36. } finally {
   37. vibrator.stopVibration();
   38. this.uiContext.getHostContext()?.resourceManager.closeRawFdSync(fileName);
   39. }
   40. }
   41. })
   42. }
   43. .width('100%')
   44. }
   45. .height('100%')
   46. }
   47. }
   ```
3. 按照指定时长触发马达振动：

   ```
   1. import { vibrator } from '@kit.SensorServiceKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. try {
   5. vibrator.startVibration({
   6. type: 'time',
   7. duration: 1000,
   8. }, {
   9. id: 0,
   10. usage: 'alarm' // 根据实际选择类型归属不同的开关管控
   11. }, (error: BusinessError) => {
   12. if (error) {
   13. console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
   14. return;
   15. }
   16. console.info('Succeed in starting vibration');
   17. });
   18. } catch (err) {
   19. let e: BusinessError = err as BusinessError;
   20. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   21. }
   ```

## vibrator.startVibration9+

PhonePC/2in1TabletTVWearable

startVibration(effect: VibrateEffect, attribute: VibrateAttribute): Promise<void>

根据指定的振动效果和振动属性触发马达振动。使用promise异步回调。

**需要权限**：ohos.permission.VIBRATE

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effect | [VibrateEffect](js-apis-vibrator.md#vibrateeffect9) | 是 | 马达振动效果，支持四种：  1、[VibrateTime](js-apis-vibrator.md#vibratetime9)：按照预置振动效果触发马达振动，适用于交互反馈类的短振场景（如点击长按，滑动，拖拽等），为确保与系统整体振感反馈体验风格一致，推荐使用此接口；  2、[VibratePreset](js-apis-vibrator.md#vibratepreset9)：按照文件形式定制自定义振动效果触发马达振动，适用于匹配复杂场景效果的交互反馈（如表情包触发的拟真效果、游戏场景/操作反馈）；  3、[VibrateFromFile](js-apis-vibrator.md#vibratefromfile10)：按照指定时长触发马达振动，仅对振动时长进行启动或停止控制，满足基础功能，无法对振动强度、频率等维度进行个性化设置，此种振动调节不够细腻，无法满足精致体验；  4、[VibrateFromPattern18+](js-apis-vibrator.md#vibratefrompattern18)：按照自定义振动效果触发马达振动。使用场景和VibrateFromFile一致。VibrateFromFile是面向文件中提前定制好的效果，将具体的振动事件以文件描述符形式传递到接口中；VibrateFromPattern提供更加灵活的振动事件排列组合，将振动事件以振动事件数组的形式传递到接口中。 |
| attribute | [VibrateAttribute](js-apis-vibrator.md#vibrateattribute9) | 是 | 马达振动属性。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[振动错误码](errorcode-vibrator.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14600101 | Device operation failed. |

**示例**：

1. 按照预置振动效果触发马达振动：

   ```
   1. import { vibrator } from '@kit.SensorServiceKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. // 使用try catch对可能出现的异常进行捕获
   5. try {
   6. // 查询是否支持'haptic.notice.success'
   7. vibrator.isSupportEffect('haptic.notice.success', (err: BusinessError, state: boolean) => {
   8. if (err) {
   9. console.error(`Failed to query effect. Code: ${err.code}, message: ${err.message}`);
   10. return;
   11. }
   12. console.info('Succeed in querying effect');
   13. if (state) {
   14. try {
   15. vibrator.startVibration({
   16. type: 'preset',
   17. effectId: 'haptic.notice.success',
   18. count: 1,
   19. }, {
   20. usage: 'notification' // 根据实际选择类型归属不同的开关管控
   21. }, (error: BusinessError) => {
   22. if (error) {
   23. console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
   24. return;
   25. }
   26. console.info('Succeed in starting vibration');

   28. });
   29. } catch (err) {
   30. let e: BusinessError = err as BusinessError;
   31. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   32. }
   33. }
   34. })
   35. } catch (error) {
   36. let e: BusinessError = error as BusinessError;
   37. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   38. }
   ```
2. 按照自定义振动配置文件触发马达振动：

   ```
   1. import { vibrator } from '@kit.SensorServiceKit';
   2. import { resourceManager } from '@kit.LocalizationKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. const fileName: string = 'xxx.json';

   7. @Entry
   8. @Component
   9. struct Index {
   10. uiContext = this.getUIContext();

   12. build() {
   13. Row() {
   14. Column() {
   15. Button('alarm-file')
   16. .onClick(() => {
   17. let rawFd: resourceManager.RawFileDescriptor | undefined = this.uiContext.getHostContext()?.resourceManager.getRawFdSync(fileName);
   18. if (rawFd != undefined) {
   19. try {
   20. vibrator.startVibration({
   21. type: "file",
   22. hapticFd: { fd: rawFd.fd, offset: rawFd.offset, length: rawFd.length }
   23. }, {
   24. id: 0,
   25. usage: 'alarm' // 根据实际选择类型归属不同的开关管控
   26. }, (error: BusinessError) => {
   27. if (error) {
   28. console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
   29. return;
   30. }
   31. console.info('Succeed in starting vibration');
   32. });
   33. } catch (err) {
   34. let e: BusinessError = err as BusinessError;
   35. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   36. } finally {
   37. vibrator.stopVibration();
   38. this.uiContext.getHostContext()?.resourceManager.closeRawFdSync(fileName);
   39. }
   40. }
   41. })
   42. }
   43. .width('100%')
   44. }
   45. .height('100%')
   46. }
   47. }
   ```
3. 按照指定时长触发马达振动：

   ```
   1. import { vibrator } from '@kit.SensorServiceKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. try {
   5. vibrator.startVibration({
   6. type: 'time',
   7. duration: 1000
   8. }, {
   9. id: 0,
   10. usage: 'alarm' // 根据实际选择类型归属不同的开关管控
   11. }).then(() => {
   12. console.info('Succeed in starting vibration');
   13. }, (error: BusinessError) => {
   14. console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
   15. });
   16. } catch (err) {
   17. let e: BusinessError = err as BusinessError;
   18. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   19. }
   ```

## vibrator.stopVibration9+

PhonePC/2in1TabletTVWearable

stopVibration(stopMode: VibratorStopMode, callback: AsyncCallback<void>): void

按照指定模式停止马达振动。使用callback异步回调。

**需要权限**：ohos.permission.VIBRATE

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stopMode | [VibratorStopMode](js-apis-vibrator.md#vibratorstopmode) | 是 | 指定的停止振动模式，支持两种：  VIBRATOR\_STOP\_MODE\_TIME：停止固定时长振动；  VIBRATOR\_STOP\_MODE\_PRESET：停止预置振动。  此接口无法停止自定义振动，请使用[vibrator.stopVibration10+](js-apis-vibrator.md#vibratorstopvibration10)。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当马达停止振动成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

1. 停止指定时长振动：

   ```
   1. import { vibrator } from '@kit.SensorServiceKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. // 使用try catch对可能出现的异常进行捕获
   5. try {
   6. // 按照指定时长振动
   7. vibrator.startVibration({
   8. type: 'time',
   9. duration: 1000,
   10. }, {
   11. id: 0,
   12. usage: 'alarm' // 根据实际选择类型归属不同的开关管控
   13. }, (error: BusinessError) => {
   14. if (error) {
   15. console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
   16. return;
   17. }
   18. console.info('Succeed in starting vibration');
   19. });
   20. } catch (err) {
   21. let e: BusinessError = err as BusinessError;
   22. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   23. }

   25. try {
   26. // 按照VIBRATOR_STOP_MODE_TIME模式停止振动
   27. vibrator.stopVibration(vibrator.VibratorStopMode.VIBRATOR_STOP_MODE_TIME, (error: BusinessError) => {
   28. if (error) {
   29. console.error(`Failed to stop vibration. Code: ${error.code}, message: ${error.message}`);
   30. return;
   31. }
   32. console.info('Succeed in stopping vibration');
   33. })
   34. } catch (err) {
   35. let e: BusinessError = err as BusinessError;
   36. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   37. }
   ```
2. 停止预置振动：

   ```
   1. import { vibrator } from '@kit.SensorServiceKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. try {
   5. // 按照预置效果振动
   6. vibrator.startVibration({
   7. type: 'preset',
   8. effectId: 'haptic.notice.success',
   9. count: 1,
   10. }, {
   11. id: 0,
   12. usage: 'notification' // 根据实际选择类型归属不同的开关管控
   13. }, (error: BusinessError) => {
   14. if (error) {
   15. console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
   16. return;
   17. }
   18. console.info('Succeed in starting vibration');
   19. });
   20. } catch (err) {
   21. let e: BusinessError = err as BusinessError;
   22. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   23. }

   25. try {
   26. // 按照VIBRATOR_STOP_MODE_PRESET模式停止振动
   27. vibrator.stopVibration(vibrator.VibratorStopMode.VIBRATOR_STOP_MODE_PRESET, (error: BusinessError) => {
   28. if (error) {
   29. console.error(`Failed to stop vibration. Code: ${error.code}, message: ${error.message}`);
   30. return;
   31. }
   32. console.info('Succeed in stopping vibration');
   33. })
   34. } catch (err) {
   35. let e: BusinessError = err as BusinessError;
   36. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   37. }
   ```

## vibrator.stopVibration9+

PhonePC/2in1TabletTVWearable

stopVibration(stopMode: VibratorStopMode): Promise<void>

按照指定模式停止马达的振动。使用promise异步回调。

**需要权限**：ohos.permission.VIBRATE

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stopMode | [VibratorStopMode](js-apis-vibrator.md#vibratorstopmode) | 是 | 支持停止两种指定的振动模式：  VIBRATOR\_STOP\_MODE\_TIME：停止指定时长振动；  VIBRATOR\_STOP\_MODE\_PRESET：停止预置振动。  此接口无法停止自定义振动，请使用[vibrator.stopVibration10+](js-apis-vibrator.md#vibratorstopvibration10-1)。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

1. 停止指定时长振动：

   ```
   1. import { vibrator } from '@kit.SensorServiceKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. // 使用try catch对可能出现的异常进行捕获
   5. try {
   6. // 按照指定时长振动
   7. vibrator.startVibration({
   8. type: 'time',
   9. duration: 1000,
   10. }, {
   11. id: 0,
   12. usage: 'alarm' // 根据实际选择类型归属不同的开关管控
   13. }).then(() => {
   14. console.info('Succeed in starting vibration');
   15. }, (error: BusinessError) => {
   16. console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
   17. });
   18. } catch (err) {
   19. let e: BusinessError = err as BusinessError;
   20. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   21. }

   23. try {
   24. // 按照VIBRATOR_STOP_MODE_TIME模式停止振动
   25. vibrator.stopVibration(vibrator.VibratorStopMode.VIBRATOR_STOP_MODE_TIME).then(() => {
   26. console.info('Succeed in stopping vibration');
   27. }, (error: BusinessError) => {
   28. console.error(`Failed to stop vibration. Code: ${error.code}, message: ${error.message}`);
   29. });
   30. } catch (err) {
   31. let e: BusinessError = err as BusinessError;
   32. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   33. }
   ```
2. 停止预置振动：

   ```
   1. import { vibrator } from '@kit.SensorServiceKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. try {
   5. // 按照预置效果振动
   6. vibrator.startVibration({
   7. type: 'preset',
   8. effectId: 'haptic.notice.success',
   9. count: 1,
   10. }, {
   11. id: 0,
   12. usage: 'notification' // 根据实际选择类型归属不同的开关管控
   13. }).then(() => {
   14. console.info('Succeed in starting vibration');
   15. }, (error: BusinessError) => {
   16. console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
   17. });
   18. } catch (err) {
   19. let e: BusinessError = err as BusinessError;
   20. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   21. }

   23. try {
   24. // 按照VIBRATOR_STOP_MODE_PRESET模式停止振动
   25. vibrator.stopVibration(vibrator.VibratorStopMode.VIBRATOR_STOP_MODE_PRESET).then(() => {
   26. console.info('Succeed in stopping vibration');
   27. }, (error: BusinessError) => {
   28. console.error(`Failed to stop vibration. Code: ${error.code}, message: ${error.message}`);
   29. });
   30. } catch (err) {
   31. let e: BusinessError = err as BusinessError;
   32. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   33. }
   ```

## vibrator.stopVibration10+

PhonePC/2in1TabletTVWearable

stopVibration(callback: AsyncCallback<void>): void

停止所有模式的马达振动。使用callback异步回调。

**需要权限**：ohos.permission.VIBRATE

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数，当马达停止振动成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. // 停止所有模式的马达振动
7. vibrator.stopVibration((error: BusinessError) => {
8. if (error) {
9. console.error(`Failed to stop vibration. Code: ${error.code}, message: ${error.message}`);
10. return;
11. }
12. console.info('Succeed in stopping vibration');
13. })
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
17. }
```

## vibrator.stopVibration10+

PhonePC/2in1TabletTVWearable

stopVibration(): Promise<void>

停止所有模式的马达振动。使用promise异步回调。

**需要权限**：ohos.permission.VIBRATE

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.MiscDevice

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. // 停止所有模式的马达振动
7. vibrator.stopVibration().then(() => {
8. console.info('Succeed in stopping vibration');
9. }, (error: BusinessError) => {
10. console.error(`Failed to stop vibration. Code: ${error.code}, message: ${error.message}`);
11. });
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
15. }
```

## vibrator.stopVibration19+

PhonePC/2in1TabletTVWearable

stopVibration(param?: VibratorInfoParam): Promise<void>

不传参默认停止本地设备所有马达的振动，也可传递参数停止指定设备马达振动。使用promise异步回调。

**需要权限**：ohos.permission.VIBRATE

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [VibratorInfoParam](js-apis-vibrator.md#vibratorinfoparam19) | 否 | 指出需要控制的设备和马达信息，不传参默认控制的为本地设备的全部马达 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14600101 | Device operation failed. |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function vibratorDemo() {
5. // 查询所有马达设备信息。
6. const vibratorInfoList: vibrator.VibratorInfo[] = vibrator.getVibratorInfoSync();
7. // 根据实际业务逻辑获取目标马达, 例如查找本地马达，此处示例仅做展示，开发者需要自行调整筛选逻辑。
8. const targetVibrator = vibratorInfoList.find((vibrator: vibrator.VibratorInfo) => {
9. return vibrator.isLocalVibrator;
10. });
11. if (!targetVibrator) {
12. return;
13. }
14. // 调用 vibrator.startVibration 开始振动。
15. // ...

17. // 使用try catch对可能出现的异常进行捕获。
18. try {
19. // 根据实际业务场景停止马达振动。
20. vibrator.stopVibration({ deviceId: targetVibrator.deviceId, vibratorId: targetVibrator.vibratorId }).then(() => {
21. console.info('Succeed in stopping vibration');
22. }, (error: BusinessError) => {
23. console.error(`Failed to stop vibration. Code: ${error.code}, message: ${error.message}`);
24. });
25. } catch (error) {
26. let e: BusinessError = error as BusinessError;
27. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
28. }
29. }
```

## vibrator.stopVibrationSync12+

PhonePC/2in1TabletTVWearable

stopVibrationSync(): void

停止任何形式的马达振动。

**需要权限**：ohos.permission.VIBRATE

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.MiscDevice

**错误码**：

以下错误码的详细介绍请参见[振动错误码](errorcode-vibrator.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14600101 | Device operation failed. |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. // 停止任何形式的马达振动
7. vibrator.stopVibrationSync()
8. console.info('Succeed in stopping vibration');
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
12. }
```

## vibrator.isSupportEffect10+

PhonePC/2in1TabletTVWearable

isSupportEffect(effectId: string, callback: AsyncCallback<boolean>): void

查询是否支持传入参数effectId。使用callback异步回调。

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effectId | string | 是 | 待确认的预置振动效果，字符串最大长度64，超出截取64。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数，当返回true则表示支持该effectId，返回false不支持。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. // 查询是否支持'haptic.notice.success'
7. vibrator.isSupportEffect('haptic.notice.success', (err: BusinessError, state: boolean) => {
8. if (err) {
9. console.error(`Failed to query effect. Code: ${err.code}, message: ${err.message}`);
10. return;
11. }
12. console.info('Succeed in querying effect');
13. if (state) {
14. try {
15. // 使用startVibration需要添加ohos.permission.VIBRATE权限
16. vibrator.startVibration({
17. type: 'preset',
18. effectId: 'haptic.notice.success',
19. count: 1,
20. }, {
21. usage: 'unknown' // 根据实际选择类型归属不同的开关管控
22. }, (error: BusinessError) => {
23. if (error) {
24. console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
25. } else {
26. console.info('Succeed in starting vibration');
27. }
28. });
29. } catch (error) {
30. let e: BusinessError = error as BusinessError;
31. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
32. }
33. }
34. })
35. } catch (error) {
36. let e: BusinessError = error as BusinessError;
37. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
38. }
```

## vibrator.isSupportEffect10+

PhonePC/2in1TabletTVWearable

isSupportEffect(effectId: string): Promise<boolean>

查询是否支持传入参数effectId。使用promise异步回调。

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effectId | string | 是 | 待确认的预置振动效果，字符串最大长度64，超出截取64。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。当返回true则表示支持该effectId，返回false不支持。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. // 查询是否支持'haptic.notice.success'
7. vibrator.isSupportEffect('haptic.notice.success').then((state: boolean) => {
8. console.info(`The query result is ${state}`);
9. if (state) {
10. try {
11. vibrator.startVibration({
12. type: 'preset',
13. effectId: 'haptic.notice.success',
14. count: 1,
15. }, {
16. usage: 'unknown' // 根据实际选择类型归属不同的开关管控
17. }).then(() => {
18. console.info('Succeed in starting vibration');
19. }).catch((error: BusinessError) => {
20. console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
21. });
22. } catch (error) {
23. let e: BusinessError = error as BusinessError;
24. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
25. }
26. }
27. }, (error: BusinessError) => {
28. console.error(`Failed to query effect. Code: ${error.code}, message: ${error.message}`);
29. })
30. } catch (error) {
31. let e: BusinessError = error as BusinessError;
32. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
33. }
```

## vibrator.isSupportEffectSync12+

PhonePC/2in1TabletTVWearable

isSupportEffectSync(effectId: string): boolean

查询是否支持预设的振动效果。

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effectId | string | 是 | 待确认的预置振动效果，字符串最大长度64，超出截取64。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 返回对象。当返回true则表示支持该effectId，返回false不支持。 |

**错误码**：

以下错误码的详细介绍请参见[振动错误码](errorcode-vibrator.md)和[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14600101 | Device operation failed. |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. // 查询是否支持预设'haptic.notice.success'
7. let ret = vibrator.isSupportEffectSync('haptic.notice.success');
8. console.info(`The query result is ${ret}`);
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
12. }
```

## vibrator.getEffectInfoSync19+

PhonePC/2in1TabletTVWearable

getEffectInfoSync(effectId: string, param?: VibratorInfoParam): EffectInfo

通过设备ID和可控马达ID获取预置振动效果信息，用于判断该预置振动效果是否受支持。

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effectId | string | 是 | 待确认的预置振动效果，字符串最大长度64，超出截取64。 |
| param | [VibratorInfoParam](js-apis-vibrator.md#vibratorinfoparam19) | 否 | 指出需要查询的设备和马达信息，默认查询的是本地设备。 |

**错误码**：

以下错误码的详细介绍请参见[振动错误码](errorcode-vibrator.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14600101 | Device operation failed. |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [EffectInfo](js-apis-vibrator.md#effectinfo19) | 该信息包括指示是否支持该效果。 |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. const effectInfo: vibrator.EffectInfo = vibrator.getEffectInfoSync('haptic.clock.timer', { deviceId: 1, vibratorId: 3});
7. console.info(`isEffectSupported: ${effectInfo.isEffectSupported}`);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
11. }
```

## vibrator.getVibratorInfoSync19+

PhonePC/2in1TabletTVWearable

getVibratorInfoSync(param?: VibratorInfoParam): Array<VibratorInfo>;

查询一个或所有设备的马达信息列表。

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [VibratorInfoParam](js-apis-vibrator.md#vibratorinfoparam19) | 否 | 指出需要控制的设备和马达信息,不传参默认查询所有设备所有马达的信息 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Array<[VibratorInfo](js-apis-vibrator.md#vibratorinfo19)> | 马达设备的信息。 |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. const vibratorInfoList: vibrator.VibratorInfo[] = vibrator.getVibratorInfoSync({ deviceId: 1, vibratorId: 3 });
6. console.info(`vibratorInfoList: ${JSON.stringify(vibratorInfoList)}`);
7. } catch (error) {
8. let e: BusinessError = error as BusinessError;
9. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
10. }
```

## vibrator.on19+

PhonePC/2in1TabletTVWearable

on(type: 'vibratorStateChange', callback: Callback<VibratorStatusEvent>): void

注册一个回调函数，在马达上线或下线时触发回调。

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'vibratorStateChange' | 是 | 监听类型，该值固定为vibratorStateChange。 |
| callback | Callback<[VibratorStatusEvent](js-apis-vibrator.md#vibratorstatusevent19)> | 是 | 回调函数，回调参数数据为VibratorStatusEvent。 |

**错误码**：

以下错误码的详细介绍请参见[振动错误码](errorcode-vibrator.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14600101 | Device operation failed. |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 回调函数
5. const vibratorStateChangeCallback = (data: vibrator.VibratorStatusEvent) => {
6. console.info('vibrator state callback info:', JSON.stringify(data));
7. }

9. // 使用try catch对可能出现的异常进行捕获
10. try {
11. // 订阅 vibratorStateChange事件
12. vibrator.on('vibratorStateChange', vibratorStateChangeCallback);
13. } catch (error) {
14. let e: BusinessError = error as BusinessError;
15. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
16. }
```

## vibrator.off19+

PhonePC/2in1TabletTVWearable

off(type: 'vibratorStateChange', callback?: Callback<VibratorStatusEvent>): void

注销马达上线或下线事件的回调函数。

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'vibratorStateChange' | 是 | 监听类型，该值固定为vibratorStateChange。 |
| callback | Callback<[VibratorStatusEvent](js-apis-vibrator.md#vibratorstatusevent19)> | 否 | 回调函数，回调参数数据为VibratorStatusEvent，不填此参数则为注销所有callback |

**错误码**：

以下错误码的详细介绍请参见[振动错误码](errorcode-vibrator.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14600101 | Device operation failed. |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 回调函数
5. const vibratorStateChangeCallback = (data: vibrator.VibratorStatusEvent) => {
6. console.info('vibrator state callback info:', JSON.stringify(data));
7. }
8. // 使用try catch对可能出现的异常进行捕获
9. try {
10. // 取消订阅 vibratorStateChange事件
11. vibrator.off('vibratorStateChange', vibratorStateChangeCallback);
12. // 取消订阅所有 vibratorStateChange事件
13. // vibrator.off('vibratorStateChange');
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
17. }
```

## VibratorStatusEvent19+

PhonePC/2in1TabletTVWearable

振动设备上线、下线状态事件信息。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 否 | 否 | 报告事件的时间戳，单位ms。 |
| deviceId | number | 否 | 否 | 设备的ID。 |
| vibratorCount | number | 否 | 否 | 设备上的马达的数量。 |
| isVibratorOnline | boolean | 否 | 否 | 指示设备的上线和下线状态，true表示上线，false表示下线。 |

## VibratorInfoParam19+

PhonePC/2in1TabletTVWearable

设备上马达的参数。默认情况下，VibratorInfoParam默认为查询或控制本地全部马达。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | number | 否 | 是 | 设备的ID：默认值为-1，表示本地设备，API19以后设备ID可以使用[getVibratorInfoSync](js-apis-vibrator.md#vibratorgetvibratorinfosync19)或设备上下线接口[on](js-apis-vibrator.md#vibratoron19)查询。 |
| vibratorId | number | 否 | 是 | 马达ID：默认值为0，控制的是该设备的全部马达，API19以后马达ID可以使用[getVibratorInfoSync](js-apis-vibrator.md#vibratorgetvibratorinfosync19)设备上下线接口[on](js-apis-vibrator.md#vibratoron19)查询。 |

## EffectInfo19+

PhonePC/2in1TabletTVWearable

查询的预制效果信息。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isEffectSupported | boolean | 否 | 否 | 预制效果是否支持，true表示支持，false表示不支持。 |

## VibratorInfo19+

PhonePC/2in1TabletTVWearable

表示查询的马达信息。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | number | 否 | 否 | 设备ID。 |
| vibratorId | number | 否 | 否 | 马达ID。 |
| deviceName | string | 否 | 否 | 设备名称。 |
| isHdHapticSupported | boolean | 否 | 否 | 是否支持高清振动，true为支持，false为不支持。 |
| isLocalVibrator | boolean | 否 | 否 | 是否为本地设备，true为本地设备，false为非本地设备。 |

## vibrator.isHdHapticSupported12+

PhonePC/2in1TabletTVWearable

isHdHapticSupported(): boolean

查询是否支持高清振动。

**系统能力**：SystemCapability.Sensors.MiscDevice

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 返回对象，当返回true表示支持高清振动，返回false不支持。 |

**错误码**：

以下错误码的详细介绍请参见[振动错误码](errorcode-vibrator.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 14600101 | Device operation failed. |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 使用try catch对可能出现的异常进行捕获
5. try {
6. // 查询是否支持高清振动
7. let ret = vibrator.isHdHapticSupported();
8. console.info(`The query result is ${ret}`);
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
12. }
```

## VibratorPatternBuilder18+

PhonePC/2in1TabletTVWearable

### vibrator('addContinuousEvent')18+

PhonePC/2in1TabletTVWearable

addContinuousEvent(time: number, duration: number, options?: ContinuousParam): VibratorPatternBuilder;

添加长振事件的方法成VibratorPattern对象。

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| time | number | 是 | 长振事件的起始时间。单位ms，取值范围[0,1800000]区间内所有整数。 |
| duration | number | 是 | 长振事件的持续时间。单位ms，取值范围(0,5000]区间内所有整数。 |
| options | [ContinuousParam](js-apis-vibrator.md#continuousparam18) | 否 | 可选参数，可选参数对象。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| VibratorPatternBuilder | 返回已添加连续振动事件的VibratorPatternBuilder对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let builder = new vibrator.VibratorPatternBuilder();
5. // 使用try catch对可能出现的异常进行捕获
6. try {
7. let pointsMe: vibrator.VibratorCurvePoint[] = [
8. { time: 0, intensity: 0, frequency: -7 },
9. { time: 42, intensity: 1, frequency: -6 },
10. { time: 128, intensity: 0.94, frequency: -4 },
11. { time: 217, intensity: 0.63, frequency: -14 },
12. { time: 763, intensity: 0.48, frequency: -14 },
13. { time: 1125, intensity: 0.53, frequency: -10 },
14. { time: 1503, intensity: 0.42, frequency: -14 },
15. { time: 1858, intensity: 0.39, frequency: -14 },
16. { time: 2295, intensity: 0.34, frequency: -17 },
17. { time: 2448, intensity: 0.21, frequency: -14 },
18. { time: 2468, intensity: 0, frequency: -21 }
19. ] // VibratorCurvePoint参数最少设置4个，最大设置16个
20. let param: vibrator.ContinuousParam = {
21. intensity: 97,
22. frequency: 34,
23. points:pointsMe,
24. index: 0
25. }
26. builder.addContinuousEvent(0, 2468, param);
27. console.info(`addContinuousEvent builder is ${builder.build()}`);
28. } catch(error) {
29. let e: BusinessError = error as BusinessError;
30. console.error(`Exception. Code ${e.code}`);
31. }
```

### vibrator('addTransientEvent')18+

PhonePC/2in1TabletTVWearable

addTransientEvent(time: number, options?: TransientParam): VibratorPatternBuilder;

添加短振事件的方法成VibratorPattern对象。

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| time | number | 是 | 短振事件的起始时间。单位ms，取值范围[0,1800000]区间内所有整数。 |
| options | [TransientParam](js-apis-vibrator.md#transientparam18) | 否 | 可选参数，可选参数对象。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| VibratorPatternBuilder | 返回已添加短振事件的VibratorPatternBuilder对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let builder = new vibrator.VibratorPatternBuilder();
5. // 使用try catch对可能出现的异常进行捕获
6. try {
7. let param: vibrator.TransientParam = {
8. intensity: 80,
9. frequency: 70,
10. index: 0
11. }
12. builder.addTransientEvent(0, param);
13. console.info(`addTransientEvent builder is ${builder.build()}`);
14. } catch(error) {
15. let e: BusinessError = error as BusinessError;
16. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
17. }
```

### vibrator('build')18+

PhonePC/2in1TabletTVWearable

build(): VibratorPattern;

构造组合短事件或长事件的振动序列的方法。

**系统能力**：SystemCapability.Sensors.MiscDevice

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [VibratorPattern](js-apis-vibrator.md#vibratorpattern18) | 构造组合短振或长振的振动序列方法。 |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let builder = new vibrator.VibratorPatternBuilder();
5. try {
6. let param: vibrator.TransientParam = {
7. intensity: 80,
8. frequency: 70,
9. index: 0
10. }
11. builder.addTransientEvent(0, param);
12. console.info(`addTransientEvent builder is ${builder.build()}`);
13. } catch(error) {
14. let e: BusinessError = error as BusinessError;
15. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
16. }
17. try {
18. vibrator.startVibration({
19. type: "pattern",
20. pattern: builder.build()
21. }, {
22. usage: "alarm", // 根据实际选择类型归属不同的开关管控
23. }, (error) => {
24. if (error) {
25. let e: BusinessError = error as BusinessError;
26. console.error(`Vibrate fail. Code: ${e.code}, message: ${e.message}`);
27. } else {
28. console.info(`vibrate success`);
29. }
30. });
31. } catch(error) {
32. let e: BusinessError = error as BusinessError;
33. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
34. }
```

## EffectId

PhonePC/2in1TabletTVWearable

预置的振动效果。在调用[vibrator.startVibration9+](js-apis-vibrator.md#vibratorstartvibration9)或[vibrator.stopVibration9+](js-apis-vibrator.md#vibratorstopvibration9-1)接口下发[VibratePreset](js-apis-vibrator.md#vibratepreset9)形式振动的时候需要使用此参数类型。此参数值种类多样，'haptic.clock.timer'为其中一种。[HapticFeedback12+](js-apis-vibrator.md#hapticfeedback12)展示了几种常用的EffectId值。

说明

由于设备存在多样性，不同的设备可能预置不同的效果，建议使用预置效果前先使用[vibrator.isSupportEffect](js-apis-vibrator.md#vibratorissupporteffect10-1)10+接口查询当前设备是否支持该预置效果。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EFFECT\_CLOCK\_TIMER | 'haptic.clock.timer' | 描述用户调整计时器时的振动效果。 |

## HapticFeedback12+

PhonePC/2in1TabletTVWearable

简单而通用的振动效果。根据各设备的马达器件不同，同一振动效果的频率会有差异，但效果的频率趋向是统一的。这几种振动效果是EffectId参数的具体值，使用方法参考[vibrator.startVibration9+](js-apis-vibrator.md#vibratorstartvibration9)或[vibrator.stopVibration9+](js-apis-vibrator.md#vibratorstopvibration9-1)接口下发[VibratePreset](js-apis-vibrator.md#vibratepreset9)形式振动的示例代码。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EFFECT\_SOFT | 'haptic.effect.soft' | 较松散的振动效果，频率偏低。 |
| EFFECT\_HARD | 'haptic.effect.hard' | 较沉重的振动效果，频率居中。 |
| EFFECT\_SHARP | 'haptic.effect.sharp' | 较尖锐的振动效果，频率偏高。 |
| EFFECT\_NOTICE\_SUCCESS18+ | 'haptic.notice.success' | 表达成功通知的振动效果。 |
| EFFECT\_NOTICE\_FAILURE18+ | 'haptic.notice.fail' | 表达失败通知的振动效果。 |
| EFFECT\_NOTICE\_WARNING18+ | 'haptic.notice.warning' | 表达警告通知的振动效果。 |

## VibratorStopMode

PhonePC/2in1TabletTVWearable

停止振动的模式。在调用[vibrator.stopVibration9+](js-apis-vibrator.md#vibratorstopvibration9)或[vibrator.stopVibration9+](js-apis-vibrator.md#vibratorstopvibration9-1)接口时，需要使用此参数类型指定停止的振动模式。停止模式和[VibrateEffect9+](js-apis-vibrator.md#vibrateeffect9)中下发的模式为对应关系。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VIBRATOR\_STOP\_MODE\_TIME | 'time' | 停止duration模式的振动。 |
| VIBRATOR\_STOP\_MODE\_PRESET | 'preset' | 停止预置EffectId的振动。 |

## VibrateEffect9+

PhonePC/2in1TabletTVWearable

type VibrateEffect = VibrateTime | VibratePreset | VibrateFromFile | VibrateFromPattern

马达振动效果，支持以下四种：在调用[vibrator.startVibration9+](js-apis-vibrator.md#vibratorstartvibration9)或[vibrator.startVibration9+](js-apis-vibrator.md#vibratorstartvibration9-1)接口时，此参数的四种类型表示以四种不同的形式触发振动。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 类型 | 说明 |
| --- | --- |
| [VibrateTime](js-apis-vibrator.md#vibratetime9) | 按照指定时长触发马达振动。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| [VibratePreset](js-apis-vibrator.md#vibratepreset9) | 按照预置振动类型触发马达振动。 |
| [VibrateFromFile](js-apis-vibrator.md#vibratefromfile10) | 按照自定义振动配置文件触发马达振动。 |
| [VibrateFromPattern18+](js-apis-vibrator.md#vibratefrompattern18) | 按照自定义振动效果触发马达振动。 |

## VibrateTime9+

PhonePC/2in1TabletTVWearable

指定时长振动类型。

**元服务API**：从API version 11开始，该接口在支持元服务中使用。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | 'time' | 否 | 否 | 值为'time'，按照指定时长触发马达振动。 |
| duration | number | 否 | 否 | 马达持续振动时长, 单位ms。取值范围(0,1800000]区间内所有整数。由于实际产品厂商驱动对器件保护设计规格不同，不同设备实际最大振动时长会有差异。单次触发长振动一般建议不超过10秒，以最大化用户体验。 |

## VibratePreset9+

PhonePC/2in1TabletTVWearable

预置振动类型。当调用[vibrator.startVibration9+](js-apis-vibrator.md#vibratorstartvibration9)或[vibrator.startVibration9+](js-apis-vibrator.md#vibratorstartvibration9-1)时，[VibrateEffect9+](js-apis-vibrator.md#vibrateeffect9)参数的值可以为VibratePreset，表示触发预置振动类型。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | 'preset' | 否 | 否 | 值为'preset'，按照预置振动效果触发马达振动。 |
| effectId | string | 否 | 否 | 预置的振动效果ID，字符串最大长度64，超出截取64。 |
| count | number | 否 | 是 | 可选参数，振动的重复次数，默认值为1。 |
| intensity12+ | number | 否 | 是 | 可选参数，振动调节强度，取值范围(0,100]内所有整数，默认值为100。若振动效果不支持强度调节或设备不支持时，则按默认强度振动。 |

## VibrateFromFile10+

PhonePC/2in1TabletTVWearable

自定义振动类型。仅部分设备支持。当设备不支持此振动类型时，返回设备不支持错误码。当调用[vibrator.startVibration9+](js-apis-vibrator.md#vibratorstartvibration9)或[vibrator.startVibration9+](js-apis-vibrator.md#vibratorstartvibration9-1)时，[VibrateEffect9+](js-apis-vibrator.md#vibrateeffect9)参数的值可以为VibrateFromFile，表示触发自定义振动类型。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | 'file' | 否 | 否 | 值为'file'，按照振动配置文件触发马达振动。 |
| hapticFd | [HapticFileDescriptor](js-apis-vibrator.md#hapticfiledescriptor10)10+ | 否 | 否 | 振动配置文件的描述符。 |

## HapticFileDescriptor10+

PhonePC/2in1TabletTVWearable

自定义振动配置文件的描述符，必须确认资源文件可用，其参数可通过[fileIo.open](js-apis-file-fs.md#fileioopen)从沙箱路径获取或者通过[getRawFd](js-apis-resource-manager.md#getrawfd9)从HAP资源获取。使用场景：振动序列被存储在一个文件中，需要根据偏移量和长度进行振动，振动序列存储格式，请参考[振动效果说明](../harmonyos-guides/vibrator-guidelines.md#振动效果说明)。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fd | number | 否 | 否 | 资源文件描述符。 |
| offset | number | 否 | 是 | 距文件起始位置的偏移量，单位为字节，默认为文件起始位置，不可超出文件有效范围。 |
| length | number | 否 | 是 | 资源长度，单位为字节，默认值为从偏移位置至文件结尾的长度，不可超出文件有效范围。 |

## VibratorEventType18+

PhonePC/2in1TabletTVWearable

振动事件类型。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONTINUOUS | 0 | 表示长振。 |
| TRANSIENT | 1 | 表示短振。 |

## VibratorCurvePoint18+

PhonePC/2in1TabletTVWearable

相对事件振动强度的增益。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| time | number | 否 | 否 | 起始时间偏移，单位ms。 |
| intensity | number | 否 | 是 | 可选参数，相对事件振动强度增益，取值范围[0,100%]，省略时默认值为1。 |
| frequency | number | 否 | 是 | 可选参数，相对事件振动频率变化，取值范围[-100,100]内所有整数，省略时默认值为0。 |

## VibratorEvent18+

PhonePC/2in1TabletTVWearable

振动事件。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eventType | VibratorEventType | 否 | 否 | 振动事件类型。 |
| time | number | 否 | 否 | 振动起始时间，单位ms。取值范围[0,1800000]区间内所有整数。 |
| duration | number | 否 | 是 | 可选参数，表示振动持续时间，单位ms，取值范围（0,5000]区间所有整数，短振默认值为48，长振默认值为1000 |
| intensity | number | 否 | 是 | 可选参数，表示振动强度，取值范围[0,100]区间所有整数，省略时默认值为100。 |
| frequency | number | 否 | 是 | 可选参数，表示振动频率，取值范围[0,100]区间内所有整数，省略时默认值为50。 |
| index | number | 否 | 是 | 可选参数，表示通道编号，取值范围[0,2]区间内所有整数，省略时默认值为0。 |
| points | Array<[VibratorCurvePoint](js-apis-vibrator.md#vibratorcurvepoint18)> | 否 | 是 | 可选参数，表示振动调节曲线数组。 |

## VibratorPattern18+

PhonePC/2in1TabletTVWearable

马达振动序列，每个events代表一个振动事件。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| time | number | 否 | 否 | 振动绝对起始时间，单位ms。 |
| events | Array<[VibratorEvent](js-apis-vibrator.md#vibratorevent18)> | 否 | 否 | 振动事件数组，build()方法返回的VibratorPattern对象。 |

## ContinuousParam18+

PhonePC/2in1TabletTVWearable

连续振动参数。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| intensity | number | 否 | 是 | 可选参数，表示振动强度，取值范围[0,100]内所有整数，省略时默认值为100。 |
| frequency | number | 否 | 是 | 可选参数，表示振动频率，取值范围[0,100]内所有整数，省略时默认值为50。 |
| points | [VibratorCurvePoint](js-apis-vibrator.md#vibratorcurvepoint18)[] | 否 | 是 | 可选参数，表示振动调节曲线数组。 |
| index | number | 否 | 是 | 可选参数，表示通道编号，取值范围[0,2]区间内所有整数，省略时默认值为0。 |

## TransientParam18+

PhonePC/2in1TabletTVWearable

瞬态振动参数。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| intensity | number | 否 | 是 | 可选参数，表示振动强度，取值范围[0,100]内所有整数，省略时默认值为100。 |
| frequency | number | 否 | 是 | 可选参数，表示振动频率，取值范围[0,100]内所有整数，省略时默认值为50。 |
| index | number | 否 | 是 | 可选参数，表示通道编号，取值范围[0,2]区间内所有整数，省略时默认值为0。 |

## VibrateFromPattern18+

PhonePC/2in1TabletTVWearable

自定义振动效果触发马达振动。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | 'pattern' | 否 | 否 | 值为“pattern”，根据组合模式触发电机振动。 |
| pattern | VibratorPattern | 否 | 否 | 振动事件数组，build()方法返回的VibratorPattern对象。 |

## VibrateAttribute9+

PhonePC/2in1TabletTVWearable

马达振动属性。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 否 | 是 | 马达ID， 默认值为0。 |
| deviceId19+ | number | 否 | 是 | 设备ID，默认值为-1，表示本地设备，API19以后设备ID可以使用[getVibratorInfoSync](js-apis-vibrator.md#vibratorgetvibratorinfosync19)或设备上下线接口[on](js-apis-vibrator.md#vibratoron19)查询。  **元服务API**：从API version 19开始，该接口支持在元服务中使用。 |
| usage | [Usage](js-apis-vibrator.md#usage9) | 否 | 否 | 马达振动的使用场景。默认值为'unknown'，取值范围只允许在[Usage](js-apis-vibrator.md#usage9)提供的类型中选取。 |

## Usage9+

PhonePC/2in1TabletTVWearable

type Usage = 'unknown' | 'alarm' | 'ring' | 'notification' | 'communication' | 'touch' | 'media' | 'physicalFeedback' | 'simulateReality'

振动使用场景。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.MiscDevice

| 类型 | 说明 |
| --- | --- |
| 'unknown' | 没有明确使用场景，最低优先级，值固定为'unknown'字符串。受触感开关管控，关闭时不振动。 |
| 'alarm' | 用于警报场景，值固定为'alarm'字符串。受三态开关管控，静音时不振动。 |
| 'ring' | 用于铃声场景，值固定为'ring'字符串。受三态开关管控，静音时不振动。 |
| 'notification' | 用于通知场景，值固定为'notification'字符串。受三态开关管控，静音时不振动。 |
| 'communication' | 用于通信场景，值固定为'communication'字符串。受三态开关管控，静音时不振动。 |
| 'touch' | 用于触摸场景，值固定为'touch'字符串。 受触感开关管控，关闭时不振动。 |
| 'media' | 用于多媒体场景，值固定为'media'字符串。受触感开关管控，关闭时不振动。 |
| 'physicalFeedback' | 用于物理反馈场景，值固定为'physicalFeedback'字符串。受触感开关管控，关闭时不振动。 |
| 'simulateReality' | 用于模拟现实场景，值固定为'simulateReality'字符串。受触感开关管控，关闭时不振动。 |

## vibrator.vibrate(deprecated)

PhonePC/2in1TabletTVWearable

vibrate(duration: number): Promise<void>

按照指定持续时间触发马达振动。

从API version 8 开始支持，从API version 9 开始废弃，建议使用 [vibrator.startVibration](js-apis-vibrator.md#vibratorstartvibration9-1)9+代替。

**需要权限**：ohos.permission.VIBRATE

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| duration | number | 是 | 马达振动时长, 单位ms；取值范围是（0,1800000]区间的所有整数。由于实际产品厂商驱动对器件保护设计规格不同，不同设备实际最大振动时长会有差异。单次触发长振动一般建议不超过10秒，以最大化用户体验。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。 |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. vibrator.vibrate(1000).then(() => {
5. console.info('Succeed in vibrating');
6. }, (error: BusinessError) => {
7. console.error(`Failed to vibrate. Code: ${error.code}, message: ${error.message}`);
8. });
```

## vibrator.vibrate(deprecated)

PhonePC/2in1TabletTVWearable

vibrate(duration: number, callback?: AsyncCallback<void>): void

按照指定持续时间触发马达振动。

从API version 8 开始支持，从API version 9 开始废弃，建议使用 [vibrator.startVibration](js-apis-vibrator.md#vibratorstartvibration9)9+代替。

**需要权限**：ohos.permission.VIBRATE

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| duration | number | 是 | 马达振动时长, 单位ms。取值范围是（0,1800000]区间的所有整数。由于实际产品厂商驱动对器件保护设计规格不同，不同设备实际最大振动时长会有差异。单次触发长振动一般建议不超过10秒，以最大化用户体验。 |
| callback | AsyncCallback<void> | 否 | 回调函数，当马达振动成功，err为undefined，否则为错误对象。 |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. vibrator.vibrate(1000, (error: BusinessError) => {
5. if (error) {
6. console.error(`Failed to vibrate. Code: ${error.code}, message: ${error.message}`);
7. } else {
8. console.info('Succeed in vibrating');
9. }
10. })
```

## vibrator.vibrate(deprecated)

PhonePC/2in1TabletTVWearable

vibrate(effectId: EffectId): Promise<void>

按照预置振动效果触发马达振动。

从API version 8 开始支持，从API version 9 开始废弃，建议使用 [vibrator.startVibration](js-apis-vibrator.md#vibratorstartvibration9-1)9+代替。

**需要权限**：ohos.permission.VIBRATE

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effectId | [EffectId](js-apis-vibrator.md#effectid) | 是 | 预置的振动效果ID，字符串最大长度64，超出截取64，建议先查询是否支持。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。 |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. vibrator.vibrate(vibrator.EffectId.EFFECT_CLOCK_TIMER).then(() => {
5. console.info('Succeed in vibrating');
6. }, (error: BusinessError) => {
7. console.error(`Failed to vibrate. Code: ${error.code}, message: ${error.message}`);
8. });
```

## vibrator.vibrate(deprecated)

PhonePC/2in1TabletTVWearable

vibrate(effectId: EffectId, callback?: AsyncCallback<void>): void

按照指定振动效果触发马达振动。

从API version 8 开始支持，从API version 9 开始废弃，建议使用 [vibrator.startVibration](js-apis-vibrator.md#vibratorstartvibration9)9+代替。

**需要权限**：ohos.permission.VIBRATE

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effectId | [EffectId](js-apis-vibrator.md#effectid) | 是 | 预置的振动效果ID，字符串最大长度64，超出截取64，建议先查询是否支持。 |
| callback | AsyncCallback<void> | 否 | 回调函数，当马达振动成功，err为undefined，否则为错误对象。 |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. vibrator.vibrate(vibrator.EffectId.EFFECT_CLOCK_TIMER, (error: BusinessError) => {
5. if (error) {
6. console.error(`Failed to vibrate. Code: ${error.code}, message: ${error.message}`);
7. } else {
8. console.info('Succeed in vibrating');
9. }
10. })
```

## vibrator.stop(deprecated)

PhonePC/2in1TabletTVWearable

stop(stopMode: VibratorStopMode): Promise<void>

按照指定模式停止马达的振动。

从API version 8 开始支持，从API version 9 开始废弃，建议使用 [vibrator.stopVibration](js-apis-vibrator.md#vibratorstopvibration9-1)9+代替。

**需要权限**：ohos.permission.VIBRATE

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stopMode | [VibratorStopMode](js-apis-vibrator.md#vibratorstopmode) | 是 | 马达停止指定的振动模式。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。 |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 按照effectId类型启动振动
5. vibrator.vibrate(vibrator.EffectId.EFFECT_CLOCK_TIMER, (error: BusinessError) => {
6. if (error) {
7. console.error(`Failed to vibrate. Code: ${error.code}, message: ${error.message}`);
8. } else {
9. console.info('Succeed in vibrating');
10. }
11. })
12. // 使用VIBRATOR_STOP_MODE_PRESET模式停止振动
13. vibrator.stop(vibrator.VibratorStopMode.VIBRATOR_STOP_MODE_PRESET).then(() => {
14. console.info('Succeed in stopping');
15. }, (error: BusinessError) => {
16. console.error(`Failed to stop. Code: ${error.code}, message: ${error.message}`);
17. });
```

## vibrator.stop(deprecated)

PhonePC/2in1TabletTVWearable

stop(stopMode: VibratorStopMode, callback?: AsyncCallback<void>): void

按照指定模式停止马达的振动。

从API version 8 开始支持，从API version 9 开始废弃，建议使用 [vibrator.stopVibration](js-apis-vibrator.md#vibratorstopvibration9)9+代替。

**需要权限**：ohos.permission.VIBRATE

**系统能力**：SystemCapability.Sensors.MiscDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stopMode | [VibratorStopMode](js-apis-vibrator.md#vibratorstopmode) | 是 | 马达停止指定的振动模式。 |
| callback | AsyncCallback<void> | 否 | 回调函数，当马达停止振动成功，err为undefined，否则为错误对象。 |

**示例**：

```
1. import { vibrator } from '@kit.SensorServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 按照effectId类型启动振动
5. vibrator.vibrate(vibrator.EffectId.EFFECT_CLOCK_TIMER, (error: BusinessError) => {
6. if (error) {
7. console.error(`Failed to vibrate. Code: ${error.code}, message: ${error.message}`);
8. } else {
9. console.info('Succeed in vibrating');
10. }
11. })
12. // 使用VIBRATOR_STOP_MODE_PRESET模式停止振动
13. vibrator.stop(vibrator.VibratorStopMode.VIBRATOR_STOP_MODE_PRESET, (error: BusinessError) => {
14. if (error) {
15. console.error(`Failed to stop. Code: ${error.code}, message: ${error.message}`);
16. } else {
17. console.info('Succeed in stopping');
18. }
19. })
```
