---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-calendarmanager
title: @ohos.calendarManager (日程管理能力)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:92256c8c5aa2a522ae7452ce95a034460ad0266753977a2777433f714f289a1a
---

本模块提供日历与日程管理能力，包括日历和日程的创建、删除、修改、查询等。

* 日历管理器[CalendarManager](js-apis-calendarmanager.md#calendarmanager)用于管理日历[Calendar](js-apis-calendarmanager.md#calendar)。
* 日历[Calendar](js-apis-calendarmanager.md#calendar)主要包含账户信息[CalendarAccount](js-apis-calendarmanager.md#calendaraccount)和配置信息[CalendarConfig](js-apis-calendarmanager.md#calendarconfig)。日历Calendar与日程[Event](js-apis-calendarmanager.md#event)属于从属关系，需要先创建日历Calendar对象，然后再通过日历Calendar创建日程Event对象，一个Calendar可以有多个Event，一个Event只属于一个Calendar。日历管理器是对日历的管理，日程过滤器是对日程的管理。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 进行日历或日程的读取时，需要申请ohos.permission.READ\_CALENDAR或ohos.permission.READ\_WHOLE\_CALENDAR权限。
* 进行日历或日程的添加、删除或修改时，需要申请ohos.permission.WRITE\_CALENDAR或ohos.permission.WRITE\_WHOLE\_CALENDAR权限。

申请对应权限之后，支持的相关操作可见下表。

| 申请的权限 | 支持的日历账户操作范围 | 支持的日程操作范围 |
| --- | --- | --- |
| ohos.permission.READ\_CALENDAR | - 读取系统默认日历账户  - 读取当前应用创建的日历账户 | - 读取系统默认日历账户下当前应用创建的日程  - 读取当前应用创建的日历账户下当前应用创建的日程 |
| ohos.permission.WRITE\_CALENDAR | - 添加、删除或修改当前应用创建的日历账户 | - 添加、删除或修改系统默认日历账户下当前应用创建的日程  - 添加、删除或修改当前应用创建的日历账户下当前应用创建的日程 |
| ohos.permission.READ\_WHOLE\_CALENDAR | - 读取所有日历账户 | - 读取所有应用创建的日程 |
| ohos.permission.WRITE\_WHOLE\_CALENDAR | - 添加、删除或修改所有日历账户 | - 添加、删除或修改所有应用创建的日程 |

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { calendarManager } from '@kit.CalendarKit';
```

## calendarManager.getCalendarManager

PhonePC/2in1TabletTVWearable

getCalendarManager(context: Context): CalendarManager

根据上下文获取CalendarManager对象，用于管理日历。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Applications.CalendarData

**模型约束**：此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-uiabilitycontext.md)。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| CalendarManager | 返回创建的CalendarManager对象。 |

**示例**：

说明

示例中的mContext的获取方式请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // 获取上下文mContext
2. // 获取日历管理器calendarMgr
3. // 该文件为系统生成，目录：entry/src/main/ets/entryability/EntryAbility.ets
4. // 文档后续示例代码都需要配置此文件才能正常运行
5. import {
6. abilityAccessCtrl,
7. AbilityConstant,
8. common,
9. PermissionRequestResult,
10. Permissions,
11. UIAbility,
12. Want
13. } from '@kit.AbilityKit';
14. import { BusinessError } from '@kit.BasicServicesKit';
15. import { calendarManager } from '@kit.CalendarKit';
16. import { window } from '@kit.ArkUI';

18. export let calendarMgr: calendarManager.CalendarManager | null = null;
19. export let mContext: common.UIAbilityContext | null = null;
20. export default class EntryAbility extends UIAbility {
21. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
22. console.info("Ability onCreate");
23. }

25. onDestroy(): void {
26. console.info("Ability onDestroy");
27. }

29. onWindowStageCreate(windowStage: window.WindowStage): void {
30. // Main window is created, set main page for this ability
31. console.info("Ability onWindowStageCreate");

33. windowStage.loadContent('pages/Index', (err, data) => {
34. if (err.code) {
35. console.error(`Failed to load the content. Code: ${err.code}, message: ${err.message}`);
36. return;
37. }
38. console.info(`Succeeded in loading the content. Data: ${JSON.stringify(data)}`);
39. });
40. mContext = this.context;
41. const permissions: Permissions[] = ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR'];
42. let atManager = abilityAccessCtrl.createAtManager();
43. atManager.requestPermissionsFromUser(mContext, permissions).then((result: PermissionRequestResult) => {
44. console.info(`get Permission success, result: ${JSON.stringify(result)}`);
45. calendarMgr = calendarManager.getCalendarManager(mContext);
46. }).catch((error: BusinessError) => {
47. console.error(`get Permission error, error. Code: ${error.code}, message: ${error.message}`);
48. })
49. }

51. onWindowStageDestroy(): void {
52. // 主窗口已销毁，释放 UI 相关资源
53. console.info("Ability onWindowStageDestroy");
54. }

56. onForeground(): void {
57. // Ability 进入前台
58. console.info("Ability onForeground");
59. }

61. onBackground(): void {
62. // Ability 进入后台
63. console.info("Ability onBackground");
64. }
65. }
```

## CalendarManager

PhonePC/2in1TabletTVWearable

下列API示例中需先通过[getCalendarManager()](js-apis-calendarmanager.md#calendarmanagergetcalendarmanager)方法获取CalendarManager对象，再通过此对象调用对应方法，进行Calendar的创建、删除、修改、查询等操作。

**系统能力**： SystemCapability.Applications.CalendarData

### createCalendar

PhonePC/2in1TabletTVWearable

createCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void

根据日历账户信息，创建一个Calendar对象，使用callback异步回调。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.WRITE\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.WRITE\_CALENDAR或ohos.permission.WRITE\_WHOLE\_CALENDAR。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| calendarAccount | [CalendarAccount](js-apis-calendarmanager.md#calendaraccount) | 是 | 日历账户信息。 |
| callback | AsyncCallback<[Calendar](js-apis-calendarmanager.md#calendar)> | 是 | 回调函数，当创建账户成功时，err为undefined，data为创建成功的Calendar；否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. const calendarAccount: calendarManager.CalendarAccount = {
7. name: 'CreateMyCalendarByCallBack',
8. type: calendarManager.CalendarType.LOCAL
9. };
10. try {
11. calendarMgr?.createCalendar(calendarAccount, (err: BusinessError, data: calendarManager.Calendar) => {
12. if (err) {
13. console.error(`Failed to create calendar. Code: ${err.code}, message: ${err.message}`);
14. } else {
15. console.info(`Succeeded in creating calendar, data -> ${JSON.stringify(data)}`);
16. }
17. });
18. } catch (error) {
19. // 检查权限是否已成功申请或者参数是否正确。
20. console.error(`Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
21. }
```

### createCalendar

PhonePC/2in1TabletTVWearable

createCalendar(calendarAccount: CalendarAccount): Promise<Calendar>

根据日历账户信息，创建一个Calendar对象，使用Promise异步回调。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.WRITE\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.WRITE\_CALENDAR或ohos.permission.WRITE\_WHOLE\_CALENDAR。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| calendarAccount | [CalendarAccount](js-apis-calendarmanager.md#calendaraccount) | 是 | 日历账户信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[Calendar](js-apis-calendarmanager.md#calendar)> | Promise对象，返回创建的Calendar对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. const calendarAccount: calendarManager.CalendarAccount = {
7. name: 'CreateMyCalendarByPromise',
8. type: calendarManager.CalendarType.LOCAL,
9. displayName : 'MyApplication'
10. };
11. calendarMgr?.createCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
12. console.info(`Succeeded in creating calendar data->${JSON.stringify(data)}`);
13. }).catch((error : BusinessError) => {
14. // 检查权限是否已成功申请或者参数是否正确。
15. console.error(`Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
16. });
```

### deleteCalendar

PhonePC/2in1TabletTVWearable

deleteCalendar(calendar: Calendar, callback: AsyncCallback<void>): void

删除指定Calendar对象，使用callback异步回调。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.WRITE\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.WRITE\_CALENDAR或ohos.permission.WRITE\_WHOLE\_CALENDAR。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| calendar | [Calendar](js-apis-calendarmanager.md#calendar) | 是 | 即将删除的Calendar对象。无法删除默认账户。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当删除账户成功时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. const calendarAccount: calendarManager.CalendarAccount = {
7. name: 'DeleteMyCalendarByCallBack',
8. type: calendarManager.CalendarType.LOCAL
9. };
10. calendarMgr?.createCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
11. console.info(`Succeeded in creating calendar, data -> ${JSON.stringify(data)}`);
12. calendarMgr?.getCalendar(calendarAccount, (err: BusinessError, data: calendarManager.Calendar) => {
13. if (err) {
14. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
15. } else {
16. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
17. calendarMgr?.deleteCalendar(data, (err1: BusinessError) => {
18. if (err1) {
19. // 检查参数是否正确。
20. console.error(`Failed to delete calendar. Code: ${err1.code}, message: ${err1.message}`);
21. } else {
22. console.info("Succeeded in deleting calendar");
23. }
24. });
25. }
26. });
27. }).catch((error: BusinessError) => {
28. // 检查权限是否已成功申请或者参数是否正确。
29. console.error(`Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
30. })
```

### deleteCalendar

PhonePC/2in1TabletTVWearable

deleteCalendar(calendar: Calendar): Promise<void>

删除指定Calendar对象，使用Promise异步回调。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.WRITE\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.WRITE\_CALENDAR或ohos.permission.WRITE\_WHOLE\_CALENDAR。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| calendar | [Calendar](js-apis-calendarmanager.md#calendar) | 是 | 即将删除的Calendar对象。无法删除默认账户。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. const calendarAccount: calendarManager.CalendarAccount = {
7. name: 'DeleteMyCalendarByPromise',
8. type: calendarManager.CalendarType.LOCAL
9. };
10. calendarMgr?.createCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
11. console.info(`Succeeded in creating calendar, data -> ${JSON.stringify(data)}`);
12. calendarMgr?.getCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
13. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
14. calendarMgr?.deleteCalendar(data).then(() => {
15. console.info("Succeeded in deleting calendar");
16. }).catch((err: BusinessError) => {
17. // 检查参数是否正确。
18. console.error(`Failed to delete calendar. Code: ${err.code}, message: ${err.message}`);
19. });
20. }).catch((err: BusinessError) => {
21. // 检查权限是否已成功申请或者参数是否正确。
22. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
23. });
24. }).catch((error: BusinessError) => {
25. // 检查权限是否已成功申请或者参数是否正确。
26. console.error(`Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
27. })
```

### getCalendar

PhonePC/2in1TabletTVWearable

getCalendar(callback: AsyncCallback<Calendar>): void

获取默认Calendar对象，默认Calendar是日历存储首次运行时创建的，若创建Event时不关注其Calendar归属，则无须通过[createCalendar()](js-apis-calendarmanager.md#createcalendar)创建Calendar，直接使用默认Calendar，使用callback异步回调。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.READ\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.READ\_CALENDAR或ohos.permission.READ\_WHOLE\_CALENDAR。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[Calendar](js-apis-calendarmanager.md#calendar)> | 是 | 回调函数，当查询账户成功时，err为undefined，data为查询到的Calendar；否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
7. if (err) {
8. // 检查权限是否已成功申请或者参数是否正确。
9. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
10. } else {
11. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
12. }
13. });
```

### getCalendar

PhonePC/2in1TabletTVWearable

getCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void

获取指定Calendar对象，使用callback异步回调。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.READ\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.READ\_CALENDAR或ohos.permission.READ\_WHOLE\_CALENDAR。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| calendarAccount | [CalendarAccount](js-apis-calendarmanager.md#calendaraccount) | 是 | 指定日历账户信息。 |
| callback | AsyncCallback<[Calendar](js-apis-calendarmanager.md#calendar)> | 是 | 回调函数，当查询账户成功时，err为undefined，data为查询到的Calendar；否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 23900003 | The specified account was not found. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. const calendarAccount: calendarManager.CalendarAccount = {
7. name: 'MyCalendar',
8. type: calendarManager.CalendarType.LOCAL
9. };
10. calendarMgr?.createCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
11. console.info(`Succeeded in creating calendar, data -> ${JSON.stringify(data)}`);
12. calendarMgr?.getCalendar(calendarAccount, (err: BusinessError, data: calendarManager.Calendar) => {
13. if (err) {
14. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
15. // 检查权限是否已成功申请或者参数是否正确。
16. } else {
17. console.info(`Succeeded in getting calendar data -> ${JSON.stringify(data)}`);
18. }
19. });
20. }).catch((error: BusinessError) => {
21. console.error(`Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
22. // 检查权限是否已成功申请或者参数是否正确。
23. })
```

### getCalendar

PhonePC/2in1TabletTVWearable

getCalendar(calendarAccount?: CalendarAccount): Promise<Calendar>

获取默认Calendar对象或者指定Calendar对象，使用Promise异步回调。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.READ\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.READ\_CALENDAR或ohos.permission.READ\_WHOLE\_CALENDAR。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| calendarAccount | [CalendarAccount](js-apis-calendarmanager.md#calendaraccount) | 否 | 指定日历账户信息，用来获取指定Calendar对象，不填时，表示获取默认Calendar对象。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[Calendar](js-apis-calendarmanager.md#calendar)> | Promise对象，返回查询到的Calendar对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Incorrect parameter types. |
| 801 | Capability not supported. |
| 23900003 | The specified account was not found. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. calendarMgr?.getCalendar().then((data: calendarManager.Calendar) => {
7. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
8. }).catch((err: BusinessError) => {
9. // 检查权限是否已成功申请。
10. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
11. });
```

### getAllCalendars

PhonePC/2in1TabletTVWearable

getAllCalendars(callback: AsyncCallback<Calendar[]>): void

获取当前应用所有创建的Calendar对象以及默认Calendar对象，使用callback异步回调。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.READ\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.READ\_CALENDAR或ohos.permission.READ\_WHOLE\_CALENDAR。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[Calendar](js-apis-calendarmanager.md#calendar)[]> | 是 | 回调函数，当查询账户成功时，err为undefined，data为查询到的Calendar数组；否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. calendarMgr?.getAllCalendars((err: BusinessError, data: calendarManager.Calendar[]) => {
7. if (err) {
8. console.error(`Failed to get all calendars. Code: ${err.code}, message: ${err.message}`);
9. } else {
10. console.info(`Succeeded in getting all calendars, data -> ${JSON.stringify(data)}`);
11. data.forEach((calendar) => {
12. const account = calendar.getAccount();
13. console.info(`account -> ${JSON.stringify(account)}`);
14. })
15. }
16. });
```

### getAllCalendars

PhonePC/2in1TabletTVWearable

getAllCalendars(): Promise<Calendar[]>

获取当前应用所有创建的Calendar对象以及默认Calendar对象，使用Promise异步回调。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.READ\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.READ\_CALENDAR或ohos.permission.READ\_WHOLE\_CALENDAR。

**系统能力**： SystemCapability.Applications.CalendarData

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[Calendar](js-apis-calendarmanager.md#calendar)[]> | Promise对象，返回查询到的Calendar对象数组。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Incorrect parameter types. |
| 801 | Capability not supported. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. calendarMgr?.getAllCalendars().then((data: calendarManager.Calendar[]) => {
7. console.info(`Succeeded in getting all calendars, data -> ${JSON.stringify(data)}`);
8. data.forEach((calendar) => {
9. const account = calendar.getAccount();
10. console.info(`account -> ${JSON.stringify(account)}`);
11. })
12. }).catch((err: BusinessError) => {
13. // 检查权限是否已成功申请。
14. console.error(`Failed to get all calendars. Code: ${err.code}, message: ${err.message}`);

16. });
```

### editEvent12+

PhonePC/2in1TabletTVWearable

editEvent(event: Event): Promise<number>

通过跳转到日程创建页面创建单个日程，入参Event不填日程id，使用Promise异步回调。使用该接口创建的日程，系统日历可以进行查询和修改，申请到READ\_WHOLE\_CALENDAR权限的三方应用可以查询，申请到WRITE\_WHOLE\_CALENDAR权限的三方应用可以修改。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Event](js-apis-calendarmanager.md#event) | 是 | Event对象。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回日程的id，日程id是日程的唯一标识符，是数据库的自增主键。创建失败时没有返回值；当返回值小于0时代表用户取消创建；当返回值大于0时代表日程创建成功；没有等于0的情况。 |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. const date = new Date();
7. const event: calendarManager.Event = {
8. title: 'title',
9. type: calendarManager.EventType.NORMAL,
10. startTime: date.getTime(),
11. endTime: date.getTime() + 60 * 60 * 1000
12. };
13. calendarMgr?.editEvent(event).then((eventId: number): void => {
14. console.info(`create Event id = ${eventId}`);
15. });
```

## Calendar

PhonePC/2in1TabletTVWearable

下列API示例中需先通过[createCalendar()](js-apis-calendarmanager.md#createcalendar)、[getCalendar()](js-apis-calendarmanager.md#getcalendar)中任一方法获取Calendar对象，再通过此对象调用对应方法，对该Calendar下的日程进行创建、删除、修改、查询等操作。

**系统能力**： SystemCapability.Applications.CalendarData

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.CalendarData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 是 | 否 | 日历账户id，日历账户id是日历账户的唯一标识符，是数据库的自增主键，小于0代表日历账户创建失败，大于0代表日历账户创建成功，没有等于0的情况。 |

### addEvent

PhonePC/2in1TabletTVWearable

addEvent(event: Event, callback: AsyncCallback<number>): void

创建日程，入参[Event](js-apis-calendarmanager.md#event)不填日程id、instanceStartTime和instanceEndTime，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.WRITE\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.WRITE\_CALENDAR或ohos.permission.WRITE\_WHOLE\_CALENDAR。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Event](js-apis-calendarmanager.md#event) | 是 | Event对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数，当添加日程成功时，err为undefined，data为日程id；否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. const date = new Date();
8. const event: calendarManager.Event = {
9. type: calendarManager.EventType.NORMAL,
10. startTime: date.getTime(),
11. endTime: date.getTime() + 60 * 60 * 1000
12. };
13. calendarMgr?.getCalendar().then((data: calendarManager.Calendar) => {
14. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
15. calendar = data;
16. calendar.addEvent(event, (err: BusinessError, data: number): void => {
17. if (err) {
18. // 检查权限是否已成功申请或者参数是否正确。
19. console.error(`Failed to addEvent. Code: ${err.code}, message: ${err.message}`);
20. } else {
21. console.info(`Succeeded in adding event, id -> ${data}`);
22. }
23. });
24. }).catch((err: BusinessError) => {
25. // 检查权限是否已成功申请。
26. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
27. });
```

### addEvent

PhonePC/2in1TabletTVWearable

addEvent(event: Event): Promise<number>

创建日程，入参[Event](js-apis-calendarmanager.md#event)不填日程id、instanceStartTime和instanceEndTime，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.WRITE\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.WRITE\_CALENDAR或ohos.permission.WRITE\_WHOLE\_CALENDAR。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Event](js-apis-calendarmanager.md#event) | 是 | Event对象。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回日程的id，id大于0。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. const date = new Date();
8. const event: calendarManager.Event = {
9. type: calendarManager.EventType.NORMAL,
10. startTime: date.getTime(),
11. endTime: date.getTime() + 60 * 60 * 1000
12. };
13. calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
14. if (err) {
15. // 检查权限是否已成功申请。
16. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
17. } else {
18. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
19. calendar = data;
20. calendar.addEvent(event).then((data: number) => {
21. console.info(`Succeeded in adding event, id -> ${data}`);
22. }).catch((err: BusinessError) => {
23. // 检查权限是否已成功申请或者参数是否正确。
24. console.error(`Failed to addEvent. Code: ${err.code}, message: ${err.message}`);
25. });
26. }
27. });
```

### addEvents

PhonePC/2in1TabletTVWearable

addEvents(events: Event[], callback: AsyncCallback<void>): void

批量创建日程，入参[Event](js-apis-calendarmanager.md#event)不填日程id、instanceStartTime和instanceEndTime，使用callback异步回调。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.WRITE\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.WRITE\_CALENDAR或ohos.permission.WRITE\_WHOLE\_CALENDAR。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| events | [Event](js-apis-calendarmanager.md#event)[] | 是 | Event对象数组。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当添加日程成功时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. const date = new Date();
8. const events: calendarManager.Event[] = [
9. {
10. type: calendarManager.EventType.NORMAL,
11. startTime: date.getTime(),
12. endTime: date.getTime() + 60 * 60 * 1000
13. },
14. {
15. type: calendarManager.EventType.NORMAL,
16. startTime: date.getTime(),
17. endTime: date.getTime() + 60 * 60 * 1000
18. }
19. ];
20. calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
21. if (err) {
22. // 检查权限是否已成功申请。
23. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
24. } else {
25. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
26. calendar = data;
27. calendar.addEvents(events, (err: BusinessError) => {
28. if (err) {
29. // 检查权限是否已成功申请或者参数是否正确。
30. console.error(`Failed to add events. Code: ${err.code}, message: ${err.message}`);
31. } else {
32. console.info("Succeeded in adding events");
33. }
34. });
35. }
36. });
```

### addEvents

PhonePC/2in1TabletTVWearable

addEvents(events: Event[]): Promise<void>

批量创建日程，入参[Event](js-apis-calendarmanager.md#event)不填日程id、instanceStartTime和instanceEndTime，使用Promise异步回调。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.WRITE\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.WRITE\_CALENDAR或ohos.permission.WRITE\_WHOLE\_CALENDAR。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| events | [Event](js-apis-calendarmanager.md#event)[] | 是 | Event对象数组。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. const date = new Date();
8. const events: calendarManager.Event[] = [
9. {
10. type: calendarManager.EventType.NORMAL,
11. startTime: date.getTime(),
12. endTime: date.getTime() + 60 * 60 * 1000
13. },
14. {
15. type: calendarManager.EventType.NORMAL,
16. startTime: date.getTime(),
17. endTime: date.getTime() + 60 * 60 * 1000
18. }
19. ];
20. calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
21. if (err) {
22. // 检查权限是否已成功申请。
23. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
24. } else {
25. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
26. calendar = data;
27. calendar.addEvents(events).then(() => {
28. console.info("Succeeded in adding events");
29. }).catch((err: BusinessError) => {
30. // 检查权限是否已成功申请或者参数是否正确。
31. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
32. });
33. }
34. });
```

### deleteEvent

PhonePC/2in1TabletTVWearable

deleteEvent(id: number, callback: AsyncCallback<void>): void

删除指定id的日程，使用callback异步回调。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 日程id，传入的日程id为整数，表示已创建日程的id，是日程的唯一标识符。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当删除日程成功时，err为undefined；否则为错误对象。 |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. let id: number = 0;
8. const date = new Date();
9. const event: calendarManager.Event = {
10. type: calendarManager.EventType.NORMAL,
11. startTime: date.getTime(),
12. endTime: date.getTime() + 60 * 60 * 1000
13. };
14. calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
15. if (err) {
16. // 检查权限是否已成功申请。
17. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
18. } else {
19. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
20. calendar = data;
21. calendar.addEvent(event).then((data: number) => {
22. console.info(`Succeeded in adding event, id -> ${data}`);
23. id = data;
24. calendar?.deleteEvent(id, (err: BusinessError) => {
25. if (err) {
26. // 检查参数是否正确。
27. console.error(`Failed to delete event. Code: ${err.code}, message: ${err.message}`);
28. } else {
29. console.info(`Succeeded in deleting event`);
30. }
31. });
32. }).catch((err: BusinessError) => {
33. // 检查权限是否已成功申请或者参数是否正确。
34. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
35. });
36. }
37. });
```

### deleteEvent

PhonePC/2in1TabletTVWearable

deleteEvent(id: number): Promise<void>

删除指定id的日程，使用Promise异步回调。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 日程id。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. let id: number = 0;
8. const date = new Date();
9. const event: calendarManager.Event = {
10. type: calendarManager.EventType.NORMAL,
11. startTime: date.getTime(),
12. endTime: date.getTime() + 60 * 60 * 1000
13. };
14. calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
15. if (err) {
16. // 检查权限是否已成功申请。
17. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
18. } else {
19. console.info(`Succeeded in getting calendar data->${JSON.stringify(data)}`);
20. calendar = data;
21. await calendar.addEvent(event).then((data: number) => {
22. console.info(`Succeeded in adding event, id -> ${data}`);
23. id = data;
24. }).catch((err: BusinessError) => {
25. // 检查权限是否已成功申请或者参数是否正确。
26. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
27. });
28. calendar.deleteEvent(id).then(() => {
29. console.info("Succeeded in deleting event");
30. }).catch((err: BusinessError) => {
31. // 检查权限是否已成功申请或者参数是否正确。
32. console.error(`Failed to delete event. Code: ${err.code}, message: ${err.message}`);
33. });
34. }
35. });
```

### deleteEvents

PhonePC/2in1TabletTVWearable

deleteEvents(ids: number[], callback: AsyncCallback<void>): void

根据日程id，批量删除日程，使用callback异步回调。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | number[] | 是 | 日程id数组。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当删除多个日程成功时，err为undefined；否则为错误对象。 |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. let id1: number = 0;
8. let id2: number = 0;
9. const date = new Date();
10. const event1: calendarManager.Event = {
11. type: calendarManager.EventType.NORMAL,
12. startTime: date.getTime(),
13. endTime: date.getTime() + 60 * 60 * 1000
14. };
15. const event2: calendarManager.Event = {
16. type: calendarManager.EventType.IMPORTANT,
17. startTime: date.getTime(),
18. endTime: date.getTime() + 60 * 60 * 1000
19. };
20. calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
21. if (err) {
22. // 检查权限是否已成功申请。
23. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
24. } else {
25. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
26. calendar = data;
27. await calendar.addEvent(event1).then((data: number) => {
28. console.info(`Succeeded in adding event, id -> ${data}`);
29. id1 = data;
30. }).catch((err: BusinessError) => {
31. // 检查权限是否已成功申请或者参数是否正确。
32. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
33. });
34. await calendar.addEvent(event2).then((data: number) => {
35. console.info(`Succeeded in adding event, id -> ${data}`);
36. id2 = data;
37. }).catch((err: BusinessError) => {
38. // 检查参数是否正确。
39. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
40. });
41. calendar.deleteEvents([id1, id2], (err: BusinessError) => {
42. if (err) {
43. // 检查参数是否正确。
44. console.error(`Failed to delete events. Code: ${err.code}, message: ${err.message}`);
45. } else {
46. console.info("Succeeded in deleting events");
47. }
48. });
49. }
50. });
```

### deleteEvents

PhonePC/2in1TabletTVWearable

deleteEvents(ids: number[]): Promise<void>

根据日程id，批量删除日程，使用Promise异步回调。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | number[] | 是 | 日程id数组。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. let id1: number = 0;
8. let id2: number = 0;
9. const date = new Date();
10. const event1: calendarManager.Event = {
11. type: calendarManager.EventType.NORMAL,
12. startTime: date.getTime(),
13. endTime: date.getTime() + 60 * 60 * 1000
14. };
15. const event2: calendarManager.Event = {
16. type: calendarManager.EventType.IMPORTANT,
17. startTime: date.getTime(),
18. endTime: date.getTime() + 60 * 60 * 1000
19. };
20. calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
21. if (err) {
22. // 检查权限是否已成功申请。
23. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
24. } else {
25. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
26. calendar = data;
27. await calendar.addEvent(event1).then((data: number) => {
28. console.info(`Succeeded in adding event, id -> ${data}`);
29. id1 = data;
30. }).catch((err: BusinessError) => {
31. // 检查权限是否已成功申请或者参数是否正确。
32. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
33. });
34. await calendar.addEvent(event2).then((data: number) => {
35. console.info(`Succeeded in adding event, id -> ${data}`);
36. id2 = data;
37. }).catch((err: BusinessError) => {
38. // 检查参数是否正确。
39. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
40. });
41. calendar.deleteEvents([id1, id2]).then(() => {
42. console.info("Succeeded in deleting events");
43. }).catch((err: BusinessError) => {
44. // 检查参数是否正确。
45. console.error(`Failed to delete events. Code: ${err.code}, message: ${err.message}`);
46. });
47. }
48. });
```

### updateEvent

PhonePC/2in1TabletTVWearable

updateEvent(event: Event, callback: AsyncCallback<void>): void

更新日程，入参[Event](js-apis-calendarmanager.md#event)需要填写被修改日程的id，使用callback异步回调。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Event](js-apis-calendarmanager.md#event) | 是 | Event对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当更新日程成功时，err为undefined；否则为错误对象。 |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. const date = new Date();
8. const oriEvent: calendarManager.Event = {
9. title: 'update',
10. type: calendarManager.EventType.NORMAL,
11. description: 'updateEventTest',
12. startTime: date.getTime(),
13. endTime: date.getTime() + 60 * 60 * 1000
14. };
15. calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
16. if (err) {
17. // 检查权限是否已成功申请。
18. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
19. } else {
20. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
21. calendar = data;
22. await calendar.addEvent(oriEvent).then((data: number) => {
23. console.info(`Succeeded in adding event, id -> ${data}`);
24. oriEvent.id = data;
25. oriEvent.title = 'newUpdate';
26. }).catch((err: BusinessError) => {
27. // 检查权限是否已成功申请或者参数是否正确。
28. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
29. });
30. calendar.updateEvent(oriEvent, (err: BusinessError) => {
31. if (err) {
32. // 检查参数是否正确。
33. console.error(`Failed to update event. Code: ${err.code}, message: ${err.message}`);
34. } else {
35. console.info("Succeeded in updating event");
36. }
37. });
38. }
39. });
```

### updateEvent

PhonePC/2in1TabletTVWearable

updateEvent(event: Event): Promise<void>

更新日程，入参[Event](js-apis-calendarmanager.md#event)需要填写被修改日程的id，使用Promise异步回调。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Event](js-apis-calendarmanager.md#event) | 是 | Event对象。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. const date = new Date();
8. const oriEvent: calendarManager.Event = {
9. title: 'update',
10. type: calendarManager.EventType.NORMAL,
11. description: 'updateEventTest',
12. startTime: date.getTime(),
13. endTime: date.getTime() + 60 * 60 * 1000
14. };
15. calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
16. if (err) {
17. // 检查权限是否已成功申请。
18. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
19. } else {
20. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
21. calendar = data;
22. await calendar.addEvent(oriEvent).then((data: number) => {
23. console.info(`Succeeded in adding event, id -> ${data}`);
24. oriEvent.id = data;
25. oriEvent.title = 'newUpdate';
26. }).catch((err: BusinessError) => {
27. // 检查权限是否已成功申请或者参数是否正确。
28. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
29. });
30. calendar.updateEvent(oriEvent).then(() => {
31. console.info(`Succeeded in updating event`);
32. }).catch((err: BusinessError) => {
33. // 参数是否正确。
34. console.error(`Failed to update event. Code: ${err.code}, message: ${err.message}`);
35. });
36. }
37. });
```

### getEvents

PhonePC/2in1TabletTVWearable

getEvents(callback: AsyncCallback<Event[]>): void

查询当前日历下所有日程，使用callback异步回调。

API version 20之前，默认查询字段包括id、type、title、startTime、endTime、isAllDay、description、timeZone、location、service、attendee、reminderTime。从API version 20开始，默认查询字段包括id、type、title、startTime、endTime、isAllDay、description、timeZone、location、service、attendee、reminderTime、identifier。若查询字段为空，则不返回该字段。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.READ\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.READ\_CALENDAR或ohos.permission.READ\_WHOLE\_CALENDAR。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[Event](js-apis-calendarmanager.md#event)[]> | 是 | 回调函数，当查询日程成功时，err为undefined，data为查询到的Event数组；否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
8. if (err) {
9. // 检查权限是否已成功申请。
10. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
11. } else {
12. console.info(`Succeeded in getting calendar data -> ${JSON.stringify(data)}`);
13. calendar = data;
14. calendar.getEvents((err: BusinessError, data: calendarManager.Event[]) => {
15. if (err) {
16. console.error(`Failed to get events. Code: ${err.code}, message: ${err.message}`);
17. } else {
18. console.info(`Succeeded in getting events, data -> ${JSON.stringify(data)}`);
19. }
20. });
21. }
22. });
```

### getEvents

PhonePC/2in1TabletTVWearable

getEvents(eventFilter: EventFilter, eventKey: (keyof Event)[], callback: AsyncCallback<Event[]>):void

获取Calendar下符合查询条件的Event，使用callback异步回调。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.READ\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.READ\_CALENDAR或ohos.permission.READ\_WHOLE\_CALENDAR。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventFilter | [EventFilter](js-apis-calendarmanager.md#eventfilter) | 是 | 查询条件。 |
| eventKey | (keyof [Event](js-apis-calendarmanager.md#event))[] | 是 | 查询字段。 |
| callback | AsyncCallback<[Event](js-apis-calendarmanager.md#event)[]> | 是 | 回调函数，当查询日程成功时，err为undefined，data为查询到的Event数组；否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. let id1: number = 0;
8. let id2: number = 0;
9. const date = new Date();
10. const event1: calendarManager.Event = {
11. type: calendarManager.EventType.NORMAL,
12. startTime: date.getTime(),
13. endTime: date.getTime() + 60 * 60 * 1000
14. };
15. const event2: calendarManager.Event = {
16. type: calendarManager.EventType.IMPORTANT,
17. startTime: date.getTime(),
18. endTime: date.getTime() + 60 * 60 * 1000
19. };
20. calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
21. if (err) {
22. // 检查权限是否已成功申请。
23. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
24. } else {
25. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
26. calendar = data;
27. await calendar.addEvent(event1).then((data: number) => {
28. console.info(`Succeeded in adding event, id -> ${data}`);
29. }).catch((err: BusinessError) => {
30. // 检查权限是否已成功申请或者参数是否正确。
31. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
32. });
33. await calendar.addEvent(event2).then((data: number) => {
34. console.info(`Succeeded in adding event, id -> ${data}`);
35. }).catch((err: BusinessError) => {
36. // 检查参数是否正确。
37. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
38. });
39. const filter = calendarManager.EventFilter.filterById([id1, id2]);
40. calendar.getEvents(filter, ['title', 'type', 'startTime', 'endTime'], (err: BusinessError, data: calendarManager.Event[]) => {
41. if (err) {
42. // 检查参数是否正确。
43. console.error(`Failed to get events. Code: ${err.code}, message: ${err.message}`);
44. } else {
45. console.info(`Succeeded in getting events, data -> ${JSON.stringify(data)}`);
46. }
47. });
48. }
49. });
```

### getEvents

PhonePC/2in1TabletTVWearable

getEvents(eventFilter?: EventFilter, eventKey?: (keyof Event)[]): Promise<Event[]>

获取Calendar下符合查询条件的Event，使用Promise异步回调。

只有一个入参时，参数必须为查询条件，对应参数类型为EventFilter。

当没有入参时，可查询指定日历账户下的所有日程。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.READ\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.READ\_CALENDAR或ohos.permission.READ\_WHOLE\_CALENDAR。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventFilter | [EventFilter](js-apis-calendarmanager.md#eventfilter) | 否 | 查询条件。 |
| eventKey | (keyof [Event](js-apis-calendarmanager.md#event))[] | 否 | 查询字段。API version 20之前，不填时默认查询字段包括id、type、title、startTime、endTime、isAllDay、description、timeZone、location、service、attendee、reminderTime；从API version 20开始，不填时默认查询字段包括id、type、title、startTime、endTime、isAllDay、description、timeZone、location、service、attendee、reminderTime、identifier。若查询字段为空，则不返回该字段。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[Event](js-apis-calendarmanager.md#event)[]> | Promise对象，返回的是Event对象数组。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. const date = new Date();
8. const event: calendarManager.Event = {
9. title: 'MyEvent',
10. type: calendarManager.EventType.IMPORTANT,
11. startTime: date.getTime(),
12. endTime: date.getTime() + 60 * 60 * 1000
13. };
14. calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
15. if (err) {
16. // 检查权限是否已成功申请。
17. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
18. } else {
19. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
20. calendar = data;
21. await calendar.addEvent(event).then((data: number) => {
22. console.info(`Succeeded in adding event, id -> ${data}`);
23. }).catch((err: BusinessError) => {
24. // 检查权限是否已成功申请或者参数是否正确。
25. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
26. });
27. // 根据MyEvent进行模糊查询，如果存在类似标题为MyEvent1类型的日程，也可查询出来
28. const filter = calendarManager.EventFilter.filterByTitle('MyEvent');
29. calendar.getEvents(filter).then((data: calendarManager.Event[]) => {
30. console.info(`Succeeded in getting events, data -> ${JSON.stringify(data)}`);
31. }).catch((err: BusinessError) => {
32. // 检查参数是否正确。
33. console.error(`Failed to get events. Code: ${err.code}, message: ${err.message}`);
34. });
35. }
36. });
```

### getConfig

PhonePC/2in1TabletTVWearable

getConfig(): CalendarConfig

获取日历配置信息。

**系统能力**： SystemCapability.Applications.CalendarData

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [CalendarConfig](js-apis-calendarmanager.md#calendarconfig) | 日历配置信息。 |

**示例**：

```
1. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
2. import { calendarMgr } from '../entryability/EntryAbility';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
8. if (err) {
9. // 检查权限是否已成功申请。
10. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
11. } else {
12. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
13. calendar = data;
14. const config = calendar.getConfig();
15. console.info(`Succeeded in getting config, config -> ${JSON.stringify(config)}`);
16. }
17. });
```

### setConfig

PhonePC/2in1TabletTVWearable

setConfig(config: CalendarConfig, callback: AsyncCallback<void>): void

设置日历配置信息，使用callback异步回调。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [CalendarConfig](js-apis-calendarmanager.md#calendarconfig) | 是 | 日历配置信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当设置Config成功时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 23900001 | Parameter value error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. const config: calendarManager.CalendarConfig = {
8. enableReminder: true,
9. color: '#aabbcc'
10. };
11. calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
12. if (err) {
13. // 检查权限是否已成功申请。
14. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
15. } else {
16. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
17. calendar = data;
18. calendar.setConfig(config, (err: BusinessError) => {
19. if (err) {
20. // 检查权限是否已成功申请或者参数是否正确。
21. console.error(`Failed to set config. Code: ${err.code}, message: ${err.message}`);
22. } else {
23. console.info(`Succeeded in setting config, config -> ${JSON.stringify(config)}`);
24. }
25. });
26. }
27. });
```

### setConfig

PhonePC/2in1TabletTVWearable

setConfig(config: CalendarConfig): Promise<void>

设置日历配置信息，使用Promise异步回调。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [CalendarConfig](js-apis-calendarmanager.md#calendarconfig) | 是 | 日历配置信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 23900001 | Parameter value error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. const config: calendarManager.CalendarConfig = {
8. enableReminder: true,
9. color: '#aabbcc'
10. };
11. calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
12. if (err) {
13. // 检查权限是否已成功申请。
14. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
15. } else {
16. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
17. calendar = data;
18. calendar.setConfig(config).then(() => {
19. console.info(`Succeeded in setting config, data->${JSON.stringify(config)}`);
20. }).catch((err: BusinessError) => {
21. // 检查权限是否已成功申请或者参数是否正确。
22. console.error(`Failed to set config. Code: ${err.code}, message: ${err.message}`);
23. });
24. }
25. });
```

### getAccount

PhonePC/2in1TabletTVWearable

getAccount(): CalendarAccount

获取日历账户信息。

**系统能力**： SystemCapability.Applications.CalendarData

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [CalendarAccount](js-apis-calendarmanager.md#calendaraccount) | 日历账户信息。 |

**示例**：

```
1. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
2. import { calendarMgr } from '../entryability/EntryAbility';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
8. if (err) {
9. // 检查权限是否已成功申请。
10. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
11. } else {
12. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
13. calendar = data;
14. const account = calendar.getAccount();
15. console.info(`succeeded in getting account, account -> ${JSON.stringify(account)}`);
16. }
17. });
```

### queryEventInstances18+

PhonePC/2in1TabletTVWearable

queryEventInstances(start: number, end: number, ids?: number[], eventKey?: (keyof Event)[]): Promise<Event[]>

获取Calendar下符合查询条件的日程实例，使用Promise异步回调。

**需要权限**： API version 21之前，使用此接口需申请ohos.permission.READ\_CALENDAR权限；

从API version 21开始，使用此接口需申请ohos.permission.READ\_CALENDAR或ohos.permission.READ\_WHOLE\_CALENDAR。

**系统能力**： SystemCapability.Applications.CalendarData

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 日程开始时间，类型为13位时间戳。 |
| end | number | 是 | 日程结束时间，类型为13位时间戳。 |
| ids | number[] | 否 | 需要查询的日程id数组，可为空数组或undefined。 |
| eventKey | (keyof [Event](js-apis-calendarmanager.md#event))[] | 否 | 所有查询日程的字段。不填时，默认查询字段为：id、title、startTime、endTime、instanceStartTime、instanceEndTime、isAllDay、description、timeZone、location、service。若查询字段为空，则不返回该字段。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[Event](js-apis-calendarmanager.md#event)[]> | Promise对象，返回的是Event对象数组。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[日历服务错误码](errorcode-calendarmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23900004 | Internal program errors. Possible causes: 1. dataShare database execution error; 2. null pointer error; 3. Data parsing error. |

**示例**：

```
1. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. const date = new Date();
8. const event: calendarManager.Event = {
9. title: 'MyEvent',
10. type: calendarManager.EventType.IMPORTANT,
11. startTime: date.getTime(),
12. endTime: date.getTime() + 60 * 60 * 1000
13. };
14. calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
15. if (err) {
16. // 检查权限是否已成功申请。
17. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
18. } else {
19. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
20. calendar = data;
21. await calendar.addEvent(event).then((data: number) => {
22. console.info(`Succeeded in adding event, id -> ${data}`);
23. }).catch((err: BusinessError) => {
24. // 检查权限是否已成功申请或者参数是否正确。
25. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
26. });
27. calendar?.queryEventInstances(date.getTime(), date.getTime() + 60 * 60 * 1000, undefined,
28. ["title", "startTime", "endTime", "instanceStartTime", "instanceEndTime",]).then((data: calendarManager.Event[]) => {
29. console.info(`Succeeded in getting event instances, data -> ${JSON.stringify(data)}`);
30. }).catch((err: BusinessError) => {
31. // 检查参数是否正确。
32. console.error(`Failed to get event instances. Code: ${err.code}, message: ${err.message}`);
33. });
34. }
35. });
```

## CalendarAccount

PhonePC/2in1TabletTVWearable

日历账户信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.CalendarData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 否 | 账户名称（面向开发者），长度限制为[0,5000]字符，长度超限制可能会导致创建账户失败。 |
| type | [CalendarType](js-apis-calendarmanager.md#calendartype) | 否 | 否 | 账户类型。 |
| displayName | string | 否 | 是 | 账户显示在日历应用上的名称（面向用户）。不填时，默认为空字符串，长度限制为[0,64]字符，长度超限制会导致日历应用上账户名显示不全，被截断。 |

## CalendarConfig

PhonePC/2in1TabletTVWearable

日历配置信息。

**系统能力**：SystemCapability.Applications.CalendarData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enableReminder | boolean | 否 | 是 | 是否打开Calendar下所有Event提醒能力。当取值为true时，该Calendar下所有Event具备提醒能力；当取值为false时，不具备提醒能力，默认具备提醒能力。 |
| color | number | string | 否 | 是 | 设置Calendar颜色。值为number时取值范围为0x000000至0xFFFFFF或0x00000000至0xFFFFFFFF，值为string时长度为7或9，如'#FFFFFF'，'#FFFFFFFFF'。不设置时默认值为0xFF0A59F7，输入undefined或错误值时抛异常。 |

## Event

PhonePC/2in1TabletTVWearable

日程对象，包含日程标题、开始时间、结束时间等信息。

**系统能力**：SystemCapability.Applications.CalendarData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 否 | 是 | 日程id。当调用[addEvent()](js-apis-calendarmanager.md#addevent)、[addEvents()](js-apis-calendarmanager.md#addevents)创建日程时，不填写此参数；当调用[deleteEvent()](js-apis-calendarmanager.md#deleteevent)、[deleteEvents()](js-apis-calendarmanager.md#deleteevents)删除日程时，日程id数组，日程id需为整数，传入其他非法入参会报错。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| type | [EventType](js-apis-calendarmanager.md#eventtype) | 否 | 否 | 日程类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| title | string | 否 | 是 | 日程标题。长度限制为[0,5000]字符，长度超限制可能会导致日程创建失败，不填时，默认为空字符串。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| location | [Location](js-apis-calendarmanager.md#location) | 否 | 是 | 日程地点。不填时，默认为undefined。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| startTime | number | 否 | 否 | 日程开始时间，需要13位时间戳。全天日程时，该字段转换为传入日期00:00对应的时间戳。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| endTime | number | 否 | 否 | 日程结束时间，需要13位时间戳。全天日程时，该字段转换为传入日期24:00对应的时间戳。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isAllDay | boolean | 否 | 是 | 是否为全天日程。当取值为true时，说明为全天日程；当取值为false时，说明不是全天日程，默认为非全天日程。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| attendee | [Attendee](js-apis-calendarmanager.md#attendee)[] | 否 | 是 | 会议日程参与者。不填时，默认为null。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| timeZone | string | 否 | 是 | 日程时区。长度限制为[0,5000]字符，长度超限制可能会导致日程创建失败，不填或异常值时，默认为当前所在时区，当需要创建与当前不一样的时区时，可填入对应的时区。可通过[systemDateTime.getTimezone()](js-apis-date-time.md#systemdatetimegettimezone)获取当前系统时区。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| reminderTime | number[] | 否 | 是 | 日程提醒时间，单位为分钟。填写x分钟，即距开始时间提前x分钟提醒，不填时，默认为不提醒。为负值时表示延期多长时间提醒。全天日程时此字段表示上午9:00前x分钟提醒，可取负值，负值表示上午9:00后多长时间提醒。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| recurrenceRule | [RecurrenceRule](js-apis-calendarmanager.md#recurrencerule) | 否 | 是 | 日程重复规则，设置了此字段的日程为重复日程。不填时，默认为非重复日程。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| description | string | 否 | 是 | 日程描述。长度限制为[0,5000]字符，长度超限制可能会导致日程创建失败，不填时，默认为空字符串。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| service | [EventService](js-apis-calendarmanager.md#eventservice) | 否 | 是 | 日程服务。不填时，默认没有一键服务。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| identifier12+ | string | 否 | 是 | 写入方可指定日程唯一标识。长度限制为[0,5000]字符，长度超限制可能会导致日程创建失败，不填时，默认为null。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isLunar12+ | boolean | 否 | 是 | 是否为农历日程。当取值为true时，说明为农历日程；当取值为false时，说明不是农历日程，默认为非农历日程。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| instanceStartTime18+ | number | 否 | 是 | 日程实例开始时间，需要13位时间戳。当调用[addEvent()](js-apis-calendarmanager.md#addevent)、[addEvents()](js-apis-calendarmanager.md#addevents)创建日程时，不填写此参数。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| instanceEndTime18+ | number | 否 | 是 | 日程实例结束时间，需要13位时间戳。当调用[addEvent()](js-apis-calendarmanager.md#addevent)、[addEvents()](js-apis-calendarmanager.md#addevents)创建日程时，不填写此参数。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## CalendarType

PhonePC/2in1TabletTVWearable

账户类型枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.CalendarData

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOCAL | 'local' | 本地账户。 |
| EMAIL | 'email' | 邮箱账户。 |
| BIRTHDAY | 'birthday' | 生日账户。 |
| CALDAV | 'caldav' | 支持CalDAV协议账户。CalDAV是一种基于WebDAV的互联网开放协议，用于在多设备间同步、共享和管理日历、事件和任务数据。 |
| SUBSCRIBED | 'subscribed' | 订阅账户。 |

## Location

PhonePC/2in1TabletTVWearable

日程地点。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.CalendarData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| location | string | 否 | 是 | 地点位置。长度限制为[0,5000]字符，长度超限制可能会导致日程创建失败，不填时，默认为空字符串。 |
| longitude | number | 否 | 是 | 地点经度。取值范围[-180, 180]，默认为undefined。超过取值范围地图将无法正常显示。 |
| latitude | number | 否 | 是 | 地点纬度。取值范围[-90, 90]，默认为undefined。超过取值范围地图将无法正常显示。 |

## EventFilter

PhonePC/2in1TabletTVWearable

日程过滤器，查询日程时进行筛选过滤，获取符合条件的日程。

通过[filterById()](js-apis-calendarmanager.md#filterbyid)、[filterByTime()](js-apis-calendarmanager.md#filterbytime)、[filterByTitle()](js-apis-calendarmanager.md#filterbytitle)任一方法获取日程过滤器，传入[getEvents()](js-apis-calendarmanager.md#getevents)过滤。

**系统能力**： SystemCapability.Applications.CalendarData

### filterById

PhonePC/2in1TabletTVWearable

static filterById(ids: number[]): EventFilter

根据日程id过滤日程。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | number[] | 是 | 日程id数组，日程id需为整数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [EventFilter](js-apis-calendarmanager.md#eventfilter) | 返回日程过滤器对象。 |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. let id1: number = 0;
8. let id2: number = 0;
9. const date = new Date();
10. const event1: calendarManager.Event = {
11. type: calendarManager.EventType.NORMAL,
12. startTime: date.getTime(),
13. endTime: date.getTime() + 60 * 60 * 1000
14. };
15. const event2: calendarManager.Event = {
16. type: calendarManager.EventType.IMPORTANT,
17. startTime: date.getTime(),
18. endTime: date.getTime() + 60 * 60 * 1000
19. };
20. calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
21. if (err) {
22. // 检查权限是否已成功申请。
23. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
24. } else {
25. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
26. calendar = data;
27. await calendar.addEvent(event1).then((data: number) => {
28. console.info(`Succeeded in adding event, id -> ${data}`);
29. id1 = data;
30. }).catch((err: BusinessError) => {
31. // 检查权限是否已成功申请或者参数是否正确。
32. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
33. });
34. await calendar.addEvent(event2).then((data: number) => {
35. console.info(`Succeeded in adding event, id -> ${data}`);
36. id2 = data;
37. }).catch((err: BusinessError) => {
38. // 检查参数是否正确。
39. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
40. });
41. const filter = calendarManager.EventFilter.filterById([id1, id2]);
42. calendar.getEvents(filter).then((data: calendarManager.Event[]) => {
43. console.info(`Succeeded in getting events filter by id, data -> ${JSON.stringify(data)}`);
44. }).catch((err: BusinessError) => {
45. // 检查参数是否正确。
46. console.error(`Failed to filter by id. Code: ${err.code}, message: ${err.message}`);
47. });
48. }
49. });
```

### filterByTime

PhonePC/2in1TabletTVWearable

static filterByTime(start: number, end: number): EventFilter

根据日程时间过滤日程。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 开始时间。格式为13位时间戳。 |
| end | number | 是 | 结束时间。格式为13位时间戳。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [EventFilter](js-apis-calendarmanager.md#eventfilter) | 返回日程过滤器对象。 |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. const event1: calendarManager.Event = {
8. type: calendarManager.EventType.NORMAL,
9. startTime: 1686931200000,
10. endTime: 1687017600000
11. };
12. const event2: calendarManager.Event = {
13. type: calendarManager.EventType.IMPORTANT,
14. startTime: 1686931200000,
15. endTime: 1687017600000
16. };
17. calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
18. if (err) {
19. // 检查权限是否已成功申请。
20. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
21. } else {
22. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
23. calendar = data;
24. await calendar.addEvent(event1).then((data: number) => {
25. console.info(`Succeeded in adding event, id -> ${data}`);
26. }).catch((err: BusinessError) => {
27. // 检查权限是否已成功申请或者参数是否正确。
28. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
29. });
30. await calendar.addEvent(event2).then((data: number) => {
31. console.info(`Succeeded in adding event, id -> ${data}`);
32. }).catch((err: BusinessError) => {
33. // 检查参数是否正确。
34. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
35. });
36. const filter = calendarManager.EventFilter.filterByTime(1686931200000, 1687017600000);
37. calendar.getEvents(filter).then((data: calendarManager.Event[]) => {
38. console.info(`Succeeded in getting events filter by time, data -> ${JSON.stringify(data)}`);
39. }).catch((err: BusinessError) => {
40. // 检查参数是否正确。
41. console.error(`Failed to filter by time. Code: ${err.code}, message: ${err.message}`);
42. });
43. }
44. });
```

### filterByTitle

PhonePC/2in1TabletTVWearable

static filterByTitle(title: string): EventFilter

根据日程标题过滤日程，该条件为模糊匹配。

**系统能力**： SystemCapability.Applications.CalendarData

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 日程标题。长度限制为[0,5000]字符，长度超限制可能会导致日程创建失败。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [EventFilter](js-apis-calendarmanager.md#eventfilter) | 返回日程过滤器对象。 |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
3. import { calendarMgr } from '../entryability/EntryAbility';
4. import { calendarManager } from '@kit.CalendarKit';

6. let calendar : calendarManager.Calendar | undefined = undefined;
7. const event: calendarManager.Event = {
8. title: 'MyEvent',
9. type: calendarManager.EventType.NORMAL,
10. startTime: 1686931200000,
11. endTime: 1687017600000
12. };
13. calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
14. if (err) {
15. // 检查权限是否已成功申请。
16. console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
17. } else {
18. console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
19. calendar = data;
20. await calendar.addEvent(event).then((data: number) => {
21. console.info(`Succeeded in adding event, id -> ${data}`);
22. }).catch((err: BusinessError) => {
23. // 检查权限是否已成功申请或者参数是否正确。
24. console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
25. });
26. const filter = calendarManager.EventFilter.filterByTitle('MyEvent');
27. calendar.getEvents(filter).then((data: calendarManager.Event[]) => {
28. console.info(`Succeeded in getting events filter by title, data -> ${JSON.stringify(data)}`);
29. }).catch((err: BusinessError) => {
30. // 检查参数是否正确。
31. console.error(`Failed to filter by title. Code: ${err.code}, message: ${err.message}`);
32. });
33. }
34. });
```

## EventType

PhonePC/2in1TabletTVWearable

日程类型枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.CalendarData

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 普通日程，例如会议，闹钟等日常提醒的日程。 |
| IMPORTANT | 1 | 重要日程，例如结婚纪念日等具有重要意义的日期，不推荐三方开发者使用，重要日程类型不支持一键服务跳转功能及无法自定义提醒时间。 |

## RecurrenceRule

PhonePC/2in1TabletTVWearable

重复日程重复规则。

**系统能力**：SystemCapability.Applications.CalendarData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| recurrenceFrequency | [RecurrenceFrequency](js-apis-calendarmanager.md#recurrencefrequency) | 否 | 否 | 日程重复规则类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| expire | number | 否 | 是 | 重复周期截止日。格式为13位时间戳，不填时则日程无截止日期。  当expire与count和interval同时设置时，以先到达的限制条件及效果为准。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| count12+ | number | 否 | 是 | 重复日程的重复次数，取值为非负整数，浮点数输入将向下取整，不填时默认为0，表示不会限定重复次数，会一直重复。取值为负时，效果等同于取值为0。  当count与interval和expire同时设置时，以先到达的限制条件及效果为准。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| interval12+ | number | 否 | 是 | 重复日程的重复周期，取值为非负整数，浮点数输入将向下取整。  不填时默认为0，当取值为0、1或负值时，表示日程每天/周/月/年重复一次。  当interval与count和expire同时设置时，以先到达的限制条件及效果为准。  此属性与recurrenceFrequency重复规则相关，不同的重复规则下，表示的重复周期不同，以interval取2为例，分为以下几种情况：  每天重复时：表示日程每两天重复一次。  每周重复时：表示日程每两周重复一次。  每月重复时：表示日程每两月重复一次。  每年重复时：表示日程每两年重复一次。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| excludedDates12+ | number[] | 否 | 是 | 重复日程的排除日期，参数取值为时间戳格式，不填时，默认为空，表示没有排除的日期，0或负数为无效值，与空值效果相同。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| daysOfWeek12+ | number[] | 否 | 是 | 按照一周第几天重复。不填时，默认为空，表示没有一周第几天重复的规则。范围为[1, 7]，对应周一到周日，其他值为无效值，与空值效果相同。该字段数组与其相关字段数组为一一对应关系，如weeksOfMonth为[1, 2, 3]，daysOfWeek为[1, 2, 3]，则表示按照每月的第一周的周一，第二周的周二，第三周的周三进行重复。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| daysOfMonth12+ | number[] | 否 | 是 | 按照一个月第几天重复。不填时，默认为空，表示没有一个月第几天重复的规则。范围为[1, 31]，[1, 31]对应1到31号，其他值为无效值，与空值效果相同。若当月没有29号、30号或31号，则29、30、31也为无效值。该字段数组与其相关字段数组为一一对应关系，如monthsOfYear为[1, 2, 3]，daysOfMonth为[1, 2, 3]，则表示按照一月一号，二月二号，三月三号进行重复。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| daysOfYear12+ | number[] | 否 | 是 | 按照一年第几天重复。不填时，默认为空，表示没有一年第几天重复的规则。范围为[1, 366]，[1, 366]表示一年的1到366天，其他值为无效值，与空值效果相同。若当年没有366天，366也为无效值。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| weeksOfMonth12+ | number[] | 否 | 是 | 按照一个月第几周重复。不填时，默认为空，表示没有一个月第几周重复的规则。范围为[1, 5]，[1, 5]为每月的第1到第5周，其他值为无效值，与空值效果相同。若当月没有第五周，5也为无效值。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| weeksOfYear12+ | number[] | 否 | 是 | 按照一年中第几周重复。不填时，默认为空，表示没有一年第几周重复的规则。范围为[1, 53]，[1, 53]为每年的第1到第53周，其他值为无效值，与空值效果相同。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| monthsOfYear12+ | number[] | 否 | 是 | 按照一年中第几个月重复。不填时，默认为空，表示没有一年第几个月重复的规则。范围为[1, 12]，[1, 12]为每年的1到12月，其他值为无效值，与空值效果相同。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## RecurrenceFrequency

PhonePC/2in1TabletTVWearable

日程重复规则类型枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.CalendarData

| 名称 | 值 | 说明 |
| --- | --- | --- |
| YEARLY | 0 | 每年重复。 |
| MONTHLY | 1 | 每月重复。 |
| WEEKLY | 2 | 每周重复。 |
| DAILY | 3 | 每天重复。 |

## Attendee

PhonePC/2in1TabletTVWearable

会议日程参与者。

**系统能力**：SystemCapability.Applications.CalendarData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 会议日程参与者的姓名。长度限制为[0,5000]字符，长度超限制可能会导致日程创建失败。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| email | string | 否 | 否 | 会议日程参与者的邮箱，邮箱格式为“用户名@域名.后缀”，用户名部分只能包含字母、数字、下划线“\_”、点 “.”、连字符 “-”。不能以点 “.” 开头或结尾。 不能连续出现两个点（即“..”）。长度限制为[0,5000]字符，长度超限制可能会导致日程创建失败。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| role12+ | [AttendeeRole](js-apis-calendarmanager.md#attendeerole12) | 否 | 是 | 会议日程参与者的角色，不填时默认为空。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| status18+ | [AttendeeStatus](js-apis-calendarmanager.md#attendeestatus18) | 否 | 是 | 会议日程参与者的状态，不填时默认为空。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| type18+ | [AttendeeType](js-apis-calendarmanager.md#attendeetype18) | 否 | 是 | 会议日程参与者的类型，不填时默认为空。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## EventService

PhonePC/2in1TabletTVWearable

日程服务。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.CalendarData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ServiceType](js-apis-calendarmanager.md#servicetype) | 否 | 否 | 服务类型。 |
| uri | string | 否 | 否 | 服务的uri，格式为DeepLink类型。可以跳转到三方应用相应界面。长度限制为[0,5000]字符，长度超限制可能会导致日程创建失败。 |
| description | string | 否 | 是 | 服务辅助描述。长度限制为[0,5000]字符，长度超限制可能会导致日程创建失败，不填时，默认为空字符串。 |

## ServiceType

PhonePC/2in1TabletTVWearable

日程服务类型枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.CalendarData

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MEETING | 'Meeting' | 一键入会。 |
| WATCHING | 'Watching' | 一键追剧。 |
| REPAYMENT | 'Repayment' | 一键还款。 |
| LIVE | 'Live' | 一键直播。 |
| SHOPPING | 'Shopping' | 一键购物。 |
| TRIP | 'Trip' | 一键查看。 |
| CLASS | 'Class' | 一键上课。 |
| SPORTS\_EVENTS | 'SportsEvents' | 一键看赛事。 |
| SPORTS\_EXERCISE | 'SportsExercise' | 一键运动。 |

## AttendeeRole12+

PhonePC/2in1TabletTVWearable

会议日程参与者角色类型枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.CalendarData

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ORGANIZER | 'organizer' | 会议组织者。 |
| PARTICIPANT | 'participant' | 会议参与者。 |

## AttendeeStatus18+

PhonePC/2in1TabletTVWearable

会议日程参与者状态类型枚举。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.CalendarData

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 参与者状态未知。 |
| TENTATIVE | 1 | 参与者状态暂定。 |
| ACCEPTED | 2 | 参与者已接受。 |
| DECLINED | 3 | 参与者已拒绝。 |
| UNRESPONSIVE | 4 | 参与者未响应。 |

## AttendeeType18+

PhonePC/2in1TabletTVWearable

会议日程参与者受邀类型枚举。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.CalendarData

| 名称 | 值 | 说明 |
| --- | --- | --- |
| REQUIRED | 1 | 会议日程主送者。 |
| OPTIONAL | 2 | 会议日程抄送者。 |
| RESOURCE | 3 | 会议中使用的资源（电视或投影仪等）。 |
