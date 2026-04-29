---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/calendarmanager-practice-developer
title: 日历服务实践案例
breadcrumb: 指南 > 应用服务 > Calendar Kit（日历服务） > 日历服务实践案例
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4b6236a28f6c342585b84e90b2f5537672358885db5600af96c1af5488c0b6be
---

## 场景介绍

通过日历服务，开发者可将带有时间属性的事件作为日程写入，并支持通过“[一键服务](calendar-service.md)”功能快速跳转，帮助用户快速直达对应服务，并完成各类信息的归一化管理。各典型场景选择适用的模板，并按照模板格式填写各个字段信息，确保用户体验完整、一致。

写入日历的日程可通过通知中心、桌面卡片以及日历应用内部等多种入口向用户展示。

不同场景下，一键服务按钮出现时机如下：

* 桌面卡片、月视图日程列表卡片：日程开始时间前15分钟显示，日程结束时自动隐藏。
* 日程详情：始终显示。
* 日程通知：通知弹出时显示，通知中心内点击对应日程卡片后显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/P8mbQcICSoaUpcJFIKnQ3g/zh-cn_image_0000002558765322.png?HW-CC-KV=V1&HW-CC-Date=20260429T053736Z&HW-CC-Expire=86400&HW-CC-Sign=B8FE288C7B9B4C3CEBB6D9F308F57638EB6169663C63C4D25C2491A3E80F8E6F)

## 开发准备

请参考日程管理前三步的[开发步骤](calendarmanager-calendar-developer.md#开发步骤)：

1. 导入相关依赖。
2. 申请权限。使用Calendar Kit时，需要在module.json5中声明申请读写日历日程所需的权限：ohos.permission.READ\_CALENDAR和ohos.permission.WRITE\_CALENDAR。具体指导可见[声明权限](declare-permissions.md)。
3. 根据上下文获取日程管理器对象calendarMgr，用于对日历账户进行相关管理操作。推荐在EntryAbility.ets文件中进行操作。

## 一键服务典型场景

一键服务典型场景及对应显示内容如下表所示：

| 场景类型 | [ServiceType取值](../harmonyos-references/js-apis-calendarmanager.md#servicetype) | 按钮显示内容 |
| --- | --- | --- |
| 会议 | 'Meeting' | 加入会议 |
| 追剧 | 'Watching' | 立即观看 |
| 还款 | 'Repayment' | 马上还款 |
| 直播 | 'Live' | 开启直播 |
| 购物 | 'Shopping' | 开始选购 |
| 查看 | 'Trip' | 立即查看 |
| 上课 | 'Class' | 开始上课 |
| 赛事 | 'SportsEvents' | 立即观看 |
| 运动 | 'SportsExercise' | 开始运动 |

在进行各场景的开发前，请确保已导入相关依赖、申请相关权限等，具体可见[开发准备](calendarmanager-practice-developer.md#开发准备)。

### 出行服务场景

当用户通过购票平台预订火车票、机票或其他交通方式后，系统可以自动将其行程信息添加至日历，并在适当的时间节点进行提醒。

下表列出了该场景中主要字段的推荐配置及其说明：

| 字段名称 | 对应设置项 | 建议取值 |
| --- | --- | --- |
| 日程标题 | title | 航班、车次信息加出发地、目的地信息 |
| 开始时间 | startTime | 行程开始时间 |
| 结束时间 | endTime | 行程结束时间 |
| 提醒时间 | reminderTime | 2小时前、4小时前分别提醒 |
| 日历账户（在日历中对用户体现） | displayName | 生态应用名（建议与应用市场中名称一致） |
| 备注 | description | 可补充检票口信息、座位号信息 |
| 一键服务 | ServiceType | calendarManager.ServiceType.TRIP |

1. 创建日程。

   ```
   1. // Index.ets
   2. import { calendarMgr } from '../entryability/EntryAbility';
   3. import { calendarManager } from '@kit.CalendarKit';

   5. let tripCalendar: calendarManager.Calendar | undefined = undefined;
   6. let oriEvent: calendarManager.Event | null = null;
   7. let id: number = 0;

   9. async createTripCalendarAndEvent(): Promise<void> {
   10. // 指定日历账户信息
   11. const calendarAccount: calendarManager.CalendarAccount = {
   12. name: 'TripCalendar',
   13. type: calendarManager.CalendarType.LOCAL,
   14. // 日历账户显示名称：建议使用应用实际名称。
   15. displayName: '高铁出行'
   16. };
   17. // 日历配置信息
   18. const config: calendarManager.CalendarConfig = {
   19. // 设置日历账户颜色
   20. color: '#aabbcc'
   21. };
   22. const startTime = new Date('2025-10-01T08:17:00').getTime();
   23. const endTime = new Date('2025-10-01T12:51:00').getTime();
   24. // 日程配置信息
   25. const event: calendarManager.Event = {
   26. type: calendarManager.EventType.NORMAL,
   27. // 日程标题
   28. title: '行程信息：G107 上海虹桥-北京南',
   29. // 开始时间
   30. startTime: startTime,
   31. // 结束时间
   32. endTime: endTime,
   33. // 是否全天日程
   34. isAllDay:false,
   35. // 提醒时间
   36. reminderTime:[120, 240],
   37. // 备注
   38. description: '检票口：南二楼1口或北广场B2候车室 \n座位号：02车04二等座',
   39. // 一键服务
   40. service: {
   41. // 服务类型
   42. type: calendarManager.ServiceType.TRIP,
   43. // 服务的uri，格式为DeepLink类型。请根据“一键服务”指导文档配置。
   44. uri: 'demo://mobile/player?params='
   45. }
   46. }
   47. try {
   48. // 创建日历账户
   49. tripCalendar = await calendarMgr?.createCalendar(calendarAccount);
   50. if (!tripCalendar || tripCalendar === null) {
   51. console.error('Failed to create calendar. tripCalendar is null.');
   52. return;
   53. }
   54. // 请确保日历账户创建成功后，再进行相关日程的管理
   55. // 设置日历配置信息，设置日历账户颜色
   56. await tripCalendar.setConfig(config);
   57. // 添加日程
   58. id = await tripCalendar.addEvent(event);
   59. oriEvent = event;
   60. oriEvent.id = id;
   61. console.info(`Succeeded in creating calendar and event, result: ${JSON.stringify(id)}`);
   62. } catch (error) {
   63. console.error(`Failed to create calendar or event. Code: ${error.code}, message: ${error.message}`);
   64. }
   65. }
   ```
2. 查询日程。

   ```
   1. // Index.ets
   2. async getTripEvent(): Promise<void> {
   3. // 校验calendar是否为空
   4. if (!tripCalendar || tripCalendar === null) {
   5. console.error('Failed to get event, calendar is null.');
   6. return;
   7. }
   8. try {
   9. // 查询行程
   10. const filter = calendarManager.EventFilter.filterById([id]);
   11. let data: calendarManager.Event[] = await tripCalendar.getEvents(filter, ['title', 'type', 'startTime', 'endTime']);
   12. if (data && data.length > 0) {
   13. oriEvent = data[0];
   14. }
   15. console.info(`Succeeded in getting events, data -> ${JSON.stringify(data)}`);
   16. } catch (err) {
   17. console.error(`Failed to get events. Code: ${err.code}, message: ${err.message}`);
   18. }
   19. }
   ```
3. 更新日程。

   ```
   1. // Index.ets
   2. async updateTripEvent(): Promise<void> {
   3. // 校验calendar是否为空
   4. if (!tripCalendar || tripCalendar === null) {
   5. console.error('Failed to update event, calendar is null.');
   6. return;
   7. }
   8. if (!oriEvent || oriEvent === null) {
   9. console.error('Failed to update event, oriEvent is null');
   10. return;
   11. }
   12. // 修改行程的开始时间startTime和结束时间endTime
   13. oriEvent.startTime = new Date('2025-10-01T07:03:00').getTime();
   14. oriEvent.endTime = new Date('2025-10-01T11:51:00').getTime();
   15. try {
   16. // 更新行程
   17. await tripCalendar.updateEvent(oriEvent);
   18. console.info("Succeeded in updating event");
   19. } catch (err) {
   20. console.error(`Failed to update event. Code: ${err.code}, message: ${err.message}`);
   21. }
   22. }
   ```
4. 删除日程。

   ```
   1. // Index.ets
   2. async deleteTripEvent(): Promise<void> {
   3. // 校验calendar是否为空
   4. if (!tripCalendar || tripCalendar === null) {
   5. console.error('Failed to delete event, calendar is null.');
   6. return;
   7. }
   8. try {
   9. // 删除行程
   10. await tripCalendar.deleteEvent(id);
   11. oriEvent = null;
   12. console.info(`Succeeded in deleting Event`);
   13. } catch (err) {
   14. console.error(`Failed to delete Event, Code is ${err.code}, message is ${err.message}`);
   15. }
   16. }
   ```

示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/cMAJDv5lQHym8UDdarCWOA/zh-cn_image_0000002558605666.png?HW-CC-KV=V1&HW-CC-Date=20260429T053736Z&HW-CC-Expire=86400&HW-CC-Sign=E4AEF56CDEBEFC52C3E26C8C30FFC6A5203D839CDE9027DD47F7FE29972505A0)

### 酒店住宿场景

下表列出了该场景中主要字段的推荐配置及其说明：

| 字段名称 | 对应设置项 | 建议取值 |
| --- | --- | --- |
| 日程标题 | title | 酒店入住信息（酒店标题地址） |
| 地点 | [location](../harmonyos-references/js-apis-calendarmanager.md#location) | 酒店的地理位置 |
| 开始时间 | startTime | 入住时间 |
| 结束时间 | endTime | 离店时间 |
| 全天日程 | isAllDay | true：表示添加全天日程。 |
| 提醒时间 | reminderTime | 0：全天日程时表示当天上午9点提醒（非全天日程则是日程开始时间）。  1440：表示前一天上午9点提醒。  不填时，默认为不提醒。 |
| 日历账户（在日历中对用户体现） | displayName | 生态应用名（建议与应用市场中名称一致） |
| 备注 | description | 可补充入住时间、离店时间信息 |
| 一键服务 | ServiceType | calendarManager.ServiceType.TRIP |

创建日程示例和示意图如下：

```
1. // Index.ets
2. async createHotelCalendarAndEvent(): Promise<void> {
3. // 指定日历账户信息
4. const calendarAccount: calendarManager.CalendarAccount = {
5. name: 'hotelCalendar',
6. type: calendarManager.CalendarType.LOCAL,
7. // 日历账户显示名称：建议使用应用实际名称。
8. displayName: '酒店住宿'
9. };
10. // 日历配置信息
11. const config: calendarManager.CalendarConfig = {
12. // 设置日历账户颜色
13. color: '#aabbcc'
14. };
15. const startTime = new Date('2025-05-01T15:00:00').getTime();
16. const endTime = new Date('2025-05-02T12:00:00').getTime();
17. // 日程配置信息
18. const event: calendarManager.Event = {
19. type: calendarManager.EventType.NORMAL,
20. title: '入住信息:酒店(上海新天地店)',
21. location: {
22. location: '上海新天地',
23. longitude: 121.47506199999998,
24. latitude: 31.219150000000013
25. },
26. startTime: startTime,
27. endTime: endTime,
28. isAllDay: true,
29. // 提醒时间：全天日程是按9点往前计算分钟数
30. reminderTime: [0, 1440],
31. description: '入住:15:00后\n离店:12:00前',
32. // 一键服务
33. service: {
34. type: calendarManager.ServiceType.TRIP,
35. uri: 'demo://mobile/player?params='
36. }
37. }
38. try {
39. // 创建日历账户
40. let data: calendarManager.Calendar | undefined= await calendarMgr?.createCalendar(calendarAccount);
41. if (!data || data === null) {
42. console.error('Failed to create calendar. data is null.');
43. return;
44. }
45. // 请确保日历账户创建成功后，再进行相关日程的管理
46. // 设置日历配置信息，设置日历账户颜色
47. await data.setConfig(config);
48. // 添加日程
49. id = await data.addEvent(event);
50. console.info(`Succeeded in creating calendar and event, result: ${JSON.stringify(id)}`);
51. } catch (error) {
52. console.error(`Failed to create calendar or event. Code: ${error.code}, message: ${error.message}`);
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/ipfGA9gBSUaEvdzBrdxFmA/zh-cn_image_0000002589325193.png?HW-CC-KV=V1&HW-CC-Date=20260429T053736Z&HW-CC-Expire=86400&HW-CC-Sign=1C0EDEA088F4F948F7C04E7710748E8338CF1F41EA470EDCAACD22F4E0F2E56E)

### 直播预约场景

下表列出了该场景中主要字段的推荐配置及其说明：

| 字段名称 | 对应设置项 | 建议取值 |
| --- | --- | --- |
| 日程标题 | title | 直播名称 |
| 开始时间 | startTime | 直播开始时间 |
| 结束时间 | endTime | 直播结束时间 |
| 提醒时间 | reminderTime | 准时、10分钟前分别提醒 |
| 日历账户（在日历中对用户体现） | displayName | 生态应用名（建议与应用市场中名称一致） |
| 备注 | description | 可补充直播相关详情介绍 |
| 一键服务 | ServiceType | calendarManager.ServiceType.LIVE |

创建日程示例和示意图如下：

```
1. // Index.ets
2. async createLiveCalendarAndEvent(): Promise<void> {
3. // 指定日历账户信息
4. const calendarAccount: calendarManager.CalendarAccount = {
5. name: 'liveCalendar',
6. type: calendarManager.CalendarType.LOCAL,
7. // 日历账户显示名称：建议使用应用实际名称。
8. displayName: '直播抢购'
9. };
10. // 日历配置信息
11. const config: calendarManager.CalendarConfig = {
12. // 设置日历账户颜色
13. color: '#aabbcc'
14. };
15. const startTime = new Date('2025-11-04T21:00:00').getTime();
16. const endTime = new Date('2025-11-04T22:00:00').getTime();
17. // 日程配置信息
18. const event: calendarManager.Event = {
19. type: calendarManager.EventType.NORMAL,
20. title: '直播抢购',
21. startTime: startTime,
22. endTime: endTime,
23. isAllDay: false,
24. reminderTime: [0, 10],
25. description: '限时特惠,秋季最大福利就在直播间',
26. // 一键服务
27. service: {
28. type: calendarManager.ServiceType.LIVE,
29. uri: 'demo://mobile/player?params='
30. }
31. }
32. try {
33. // 创建日历账户
34. let data: calendarManager.Calendar | undefined= await calendarMgr?.createCalendar(calendarAccount);
35. if (!data || data === null) {
36. console.error('Failed to create calendar. data is null.');
37. return;
38. }
39. // 请确保日历账户创建成功后，再进行相关日程的管理
40. // 设置日历配置信息，设置日历账户颜色
41. await data.setConfig(config);
42. // 添加日程
43. id = await data.addEvent(event);
44. console.info(`Succeeded in creating calendar and event, result: ${JSON.stringify(id)}`);
45. } catch (error) {
46. console.error(`Failed to create calendar or event. Code: ${error.code}, message: ${error.message}`);
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/peqIawmwRfiHIlbBzsEz1g/zh-cn_image_0000002589245129.png?HW-CC-KV=V1&HW-CC-Date=20260429T053736Z&HW-CC-Expire=86400&HW-CC-Sign=5A14B12C31AFA00EF7ED2BF91744628034317D92D37AC43950574322C967E19D)

### 抢购预约场景

下表列出了该场景中主要字段的推荐配置及其说明：

| 字段名称 | 对应设置项 | 建议取值 |
| --- | --- | --- |
| 日程标题 | title | 购物节（抢购活动）名称 |
| 开始时间 | startTime | 抢购开始时间 |
| 结束时间 | endTime | 抢购结束时间 |
| 提醒时间 | reminderTime | 准时、10分钟前分别提醒 |
| 日历账户（在日历中对用户体现） | displayName | 生态应用名（建议与应用市场中名称一致） |
| 备注 | description | 可补充购物节相关介绍 |
| 一键服务 | ServiceType | calendarManager.ServiceType.SHOPPING |

创建日程示例和示意图如下：

```
1. // Index.ets
2. async createShoppingCalendarAndEvent(): Promise<void> {
3. // 指定日历账户信息
4. const calendarAccount: calendarManager.CalendarAccount = {
5. name: 'shoppingCalendar',
6. type: calendarManager.CalendarType.LOCAL,
7. // 日历账户显示名称：建议使用应用实际名称。
8. displayName: '购物'
9. };
10. // 日历配置信息
11. const config: calendarManager.CalendarConfig = {
12. // 设置日历账户颜色
13. color: '#aabbcc'
14. };
15. const startTime = new Date('2025-12-19T19:00:00').getTime();
16. const endTime = new Date('2025-12-19T20:00:00').getTime();
17. // 日程配置信息
18. const event: calendarManager.Event = {
19. type: calendarManager.EventType.NORMAL,
20. title: '购物节预热',
21. startTime: startTime,
22. endTime: endTime,
23. isAllDay: false,
24. reminderTime: [0, 10],
25. description: '9.9限时秒杀,还有精彩福利',
26. // 一键服务
27. service: {
28. type: calendarManager.ServiceType.SHOPPING,
29. uri: 'demo://mobile/player?params='
30. }
31. }
32. try {
33. // 创建日历账户
34. let data: calendarManager.Calendar | undefined= await calendarMgr?.createCalendar(calendarAccount);
35. if (!data || data === null) {
36. console.error('Failed to create calendar. data is null.');
37. return;
38. }
39. // 请确保日历账户创建成功后，再进行相关日程的管理
40. // 设置日历配置信息，设置日历账户颜色
41. await data.setConfig(config);
42. // 添加日程
43. id = await data.addEvent(event);
44. console.info(`Succeeded in creating calendar and event, result: ${JSON.stringify(id)}`);
45. } catch (error) {
46. console.error(`Failed to create calendar or event. Code: ${error.code}, message: ${error.message}`);
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/tXNgFTTNQkCiMmWUcN3odQ/zh-cn_image_0000002558765324.png?HW-CC-KV=V1&HW-CC-Date=20260429T053736Z&HW-CC-Expire=86400&HW-CC-Sign=5FAA0E0F2957F3ABB6C6C5CA4AEE7261CE97D214B8F3557848634FF01ABD839D)

### 还款提醒场景

下表列出了该场景中主要字段的推荐配置及其说明：

| 字段名称 | 对应设置项 | 建议取值 |
| --- | --- | --- |
| 日程标题 | title | 还款提醒 |
| 开始时间 | startTime | 还款日日期 |
| 结束时间 | endTime | 还款日日期 |
| 全天日程 | isAllDay | true：表示添加全天日程。 |
| 提醒时间 | reminderTime | 0：全天日程时表示当天上午9点提醒（非全天日程则是日程开始时间）。  不填时，默认为不提醒。 |
| 日历账户（在日历中对用户体现） | displayName | 生态应用名（建议与应用市场中名称一致） |
| 备注 | description | 可补充待还款金额信息 |
| 一键服务 | ServiceType | calendarManager.ServiceType.REPAYMENT |

创建日程示例和示意图如下：

```
1. // Index.ets
2. async createRepaymentCalendarAndEvent(): Promise<void> {
3. // 指定日历账户信息
4. const calendarAccount: calendarManager.CalendarAccount = {
5. name: 'repaymentCalendar',
6. type: calendarManager.CalendarType.LOCAL,
7. // 日历账户显示名称：建议使用应用实际名称。
8. displayName: '金融理财'
9. };
10. // 日历配置信息
11. const config: calendarManager.CalendarConfig = {
12. // 设置日历账户颜色
13. color: '#aabbcc'
14. };
15. const startTime = new Date('2025-10-20T00:00:00').getTime();
16. const endTime = new Date('2025-10-20T23:59:59').getTime();
17. // 日程配置信息
18. const event: calendarManager.Event = {
19. type: calendarManager.EventType.NORMAL,
20. title: '还款提醒',
21. startTime: startTime,
22. endTime: endTime,
23. isAllDay: true,
24. // 全天日程时，提醒时间为0表示当天上午9点提醒
25. reminderTime: [0],
26. description: '本月账单：待还款10989.35元',
27. // 一键服务
28. service: {
29. type: calendarManager.ServiceType.REPAYMENT,
30. uri: 'demo://mobile/player?params='
31. }
32. }
33. try {
34. // 创建日历账户
35. let data: calendarManager.Calendar | undefined= await calendarMgr?.createCalendar(calendarAccount);
36. if (!data || data === null) {
37. console.error('Failed to create calendar. data is null.');
38. return;
39. }
40. // 请确保日历账户创建成功后，再进行相关日程的管理
41. // 设置日历配置信息，设置日历账户颜色
42. await data.setConfig(config);
43. // 添加日程
44. id = await data.addEvent(event);
45. console.info(`Succeeded in creating calendar and event, result: ${JSON.stringify(id)}`);
46. } catch (error) {
47. console.error(`Failed to create calendar or event. Code: ${error.code}, message: ${error.message}`);
48. }
49. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/vdqC0R4JQBysI5nc77piGg/zh-cn_image_0000002558605668.png?HW-CC-KV=V1&HW-CC-Date=20260429T053736Z&HW-CC-Expire=86400&HW-CC-Sign=56CE79FB515F2A97FB20959DD49F7496B38AE3B5C85759CEEE476A73E4A5AF3C)

### 课程提醒场景

下表列出了该场景中主要字段的推荐配置及其说明：

| 字段名称 | 对应设置项 | 建议取值 |
| --- | --- | --- |
| 日程标题 | title | 课程名称 |
| 开始时间 | startTime | 课程开始时间 |
| 结束时间 | endTime | 课程结束时间 |
| 提醒时间 | reminderTime | 准时、10分钟前分别提醒 |
| 日历账户（在日历中对用户体现） | displayName | 生态应用名（建议与应用市场中名称一致） |
| 备注 | description | 可补充课程相关介绍 |
| 一键服务 | ServiceType | calendarManager.ServiceType.CLASS |

创建日程示例和示意图如下：

```
1. // Index.ets
2. async createClassCalendarAndEvent(): Promise<void> {
3. // 指定日历账户信息
4. const calendarAccount: calendarManager.CalendarAccount = {
5. name: 'classCalendar',
6. type: calendarManager.CalendarType.LOCAL,
7. // 日历账户显示名称：建议使用应用实际名称。
8. displayName: '我的课表'
9. };
10. // 日历配置信息
11. const config: calendarManager.CalendarConfig = {
12. // 设置日历账户颜色
13. color: '#aabbcc'
14. };
15. const startTime = new Date('2025-11-03T09:00:00').getTime();
16. const endTime = new Date('2025-11-03T09:45:00').getTime();
17. // 日程配置信息
18. const event: calendarManager.Event = {
19. type: calendarManager.EventType.NORMAL,
20. title: '语文课',
21. startTime: startTime,
22. endTime: endTime,
23. isAllDay: false,
24. reminderTime: [0, 10],
25. description: '语文课上课前准备诗歌朗读',
26. // 一键服务
27. service: {
28. type: calendarManager.ServiceType.CLASS,
29. uri: 'demo://mobile/player?params='
30. }
31. }
32. try {
33. // 创建日历账户
34. let data: calendarManager.Calendar | undefined= await calendarMgr?.createCalendar(calendarAccount);
35. if (!data || data === null) {
36. console.error('Failed to create calendar. data is null.');
37. return;
38. }
39. // 请确保日历账户创建成功后，再进行相关日程的管理
40. // 设置日历配置信息，设置日历账户颜色
41. await data.setConfig(config);
42. // 添加日程
43. id = await data.addEvent(event);
44. console.info(`Succeeded in creating calendar and event, result: ${JSON.stringify(id)}`);
45. } catch (error) {
46. console.error(`Failed to create calendar or event. Code: ${error.code}, message: ${error.message}`);
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/Pxvt-yhmTl6tHORuioTvlA/zh-cn_image_0000002589325195.png?HW-CC-KV=V1&HW-CC-Date=20260429T053736Z&HW-CC-Expire=86400&HW-CC-Sign=2924E02F1AF4FCD1E5716863F435C8A5844BB8E5C10CB0E2C6A86481AAD4A3C4)

### 影音娱乐场景

下表列出了该场景中主要字段的推荐配置及其说明：

| 字段名称 | 对应设置项 | 建议取值 |
| --- | --- | --- |
| 日程标题 | title | 赛事名称 |
| 开始时间 | startTime | 赛事开始时间 |
| 结束时间 | endTime | 赛事结束时间 |
| 提醒时间 | reminderTime | 准时、10分钟前分别提醒 |
| 日历账户（在日历中对用户体现） | displayName | 生态应用名（建议与应用市场中名称一致） |
| 备注 | description | 可补充赛事相关介绍 |
| 一键服务 | ServiceType | calendarManager.ServiceType.SPORTS\_EVENTS |

创建日程示例和示意图如下：

```
1. // Index.ets
2. async createSportsCalendarAndEvent(): Promise<void> {
3. // 指定日历账户信息
4. const calendarAccount: calendarManager.CalendarAccount = {
5. name: 'sportsEventsCalendar',
6. type: calendarManager.CalendarType.LOCAL,
7. // 日历账户显示名称：建议使用应用实际名称。
8. displayName: '足球比赛'
9. };
10. // 日历配置信息
11. const config: calendarManager.CalendarConfig = {
12. // 设置日历账户颜色
13. color: '#aabbcc'
14. };
15. const startTime = new Date('2025-10-19T20:00:00').getTime();
16. const endTime = new Date('2025-10-19T21:30:00').getTime();
17. // 日程配置信息
18. const event: calendarManager.Event = {
19. type: calendarManager.EventType.NORMAL,
20. title: '2026年足球联赛',
21. startTime: startTime,
22. endTime: endTime,
23. isAllDay: false,
24. reminderTime: [0, 10],
25. description: 'A组 xx队首战',
26. // 一键服务
27. service: {
28. type: calendarManager.ServiceType.SPORTS_EVENTS,
29. uri: 'demo://mobile/player?params='
30. }
31. }
32. try {
33. // 创建日历账户
34. let data: calendarManager.Calendar | undefined= await calendarMgr?.createCalendar(calendarAccount);
35. if (!data || data === null) {
36. console.error('Failed to create calendar. data is null.');
37. return;
38. }
39. // 请确保日历账户创建成功后，再进行相关日程的管理
40. // 设置日历配置信息，设置日历账户颜色
41. await data.setConfig(config);
42. // 添加日程
43. id = await data.addEvent(event);
44. console.info(`Succeeded in creating calendar and event, result: ${JSON.stringify(id)}`);
45. } catch (error) {
46. console.error(`Failed to create calendar or event. Code: ${error.code}, message: ${error.message}`);
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/nPnC8oy7RruNQxbrZm1aQg/zh-cn_image_0000002589245131.png?HW-CC-KV=V1&HW-CC-Date=20260429T053736Z&HW-CC-Expire=86400&HW-CC-Sign=6274BF6F070C7754B3ECBB96180B16F473015FC4E948E9B8A0265755EBF328E8)

### 运动训练场景

下表列出了该场景中主要字段的推荐配置及其说明：

| 字段名称 | 对应设置项 | 建议取值 |
| --- | --- | --- |
| 日程标题 | title | 训练课程名称 |
| 开始时间 | startTime | 训练开始时间 |
| 结束时间 | endTime | 训练结束时间 |
| 提醒时间 | reminderTime | 准时、30分钟前分别提醒 |
| 日历账户（在日历中对用户体现） | displayName | 生态应用名（建议与应用市场中名称一致） |
| 备注 | description | 可补充训练计划相关介绍 |
| 一键服务 | ServiceType | calendarManager.ServiceType.SPORTS\_EXERCISE |

创建日程示例及示意图如下：

```
1. // Index.ets
2. async createSportsExerciseEvent(): Promise<void> {
3. // 指定日历账户信息
4. const calendarAccount: calendarManager.CalendarAccount = {
5. name: 'sportsExerciseCalendar',
6. type: calendarManager.CalendarType.LOCAL,
7. // 日历账户显示名称：建议使用应用实际名称。
8. displayName: '运动健康'
9. };
10. // 日历配置信息
11. const config: calendarManager.CalendarConfig = {
12. // 设置日历账户颜色
13. color: '#aabbcc'
14. };
15. const startTime = new Date('2025-10-26T10:30:00').getTime();
16. const endTime = new Date('2025-10-26T10:45:00').getTime();
17. // 日程配置信息
18. const event: calendarManager.Event = {
19. type: calendarManager.EventType.NORMAL,
20. title: '健身操·15分钟无跑跳燃脂',
21. startTime: startTime,
22. endTime: endTime,
23. isAllDay: false,
24. reminderTime: [0, 30],
25. description: '训练日第17天',
26. // 一键服务
27. service: {
28. type: calendarManager.ServiceType.SPORTS_EXERCISE,
29. uri: 'demo://mobile/player?params='
30. }
31. }
32. try {
33. // 创建日历账户
34. let data: calendarManager.Calendar | undefined= await calendarMgr?.createCalendar(calendarAccount);
35. if (!data || data === null) {
36. console.error('Failed to create calendar. data is null.');
37. return;
38. }
39. // 请确保日历账户创建成功后，再进行相关日程的管理
40. // 设置日历配置信息，设置日历账户颜色
41. await data.setConfig(config);
42. // 添加日程
43. id = await data.addEvent(event);
44. console.info(`Succeeded in creating calendar and event, result: ${JSON.stringify(id)}`);
45. } catch (error) {
46. console.error(`Failed to create calendar or event. Code: ${error.code}, message: ${error.message}`);
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/E95ZZp8gRWmiIe1zEJG8qQ/zh-cn_image_0000002558765326.png?HW-CC-KV=V1&HW-CC-Date=20260429T053736Z&HW-CC-Expire=86400&HW-CC-Sign=5B34D66D2E0CFB5E46AE9E6EDEC4A8741F6C2A0A1758915374B0AFECE6F6A6EE)

### 会议场景

下表列出了该场景中主要字段的推荐配置及其说明：

| 字段名称 | 对应设置项 | 建议取值 |
| --- | --- | --- |
| 日程标题 | title | 会议主题 |
| 开始时间 | startTime | 会议开始时间 |
| 结束时间 | endTime | 会议结束时间 |
| 与会人 | attendee | 与会人信息 |
| 提醒时间 | reminderTime | 准时、15分钟前分别提醒 |
| 日历账户（在日历中对用户体现） | displayName | 生态应用名（建议与应用市场中名称一致） |
| 备注 | description | 可补充会议相关介绍 |
| 一键服务 | ServiceType | calendarManager.ServiceType.MEETING |

创建日程示例和示意图如下：

```
1. // Index.ets
2. async createMeetingEvent(): Promise<void> {
3. // 指定日历账户信息
4. const calendarAccount: calendarManager.CalendarAccount = {
5. name: 'meetingCalendar',
6. type: calendarManager.CalendarType.LOCAL,
7. // 日历账户显示名称：建议使用应用实际名称。
8. displayName: '会议'
9. };
10. // 日历配置信息
11. const config: calendarManager.CalendarConfig = {
12. // 设置日历账户颜色
13. color: '#aabbcc'
14. };
15. // 与会人信息
16. let attendee: calendarManager.Attendee[] = [
17. {
18. name: 'Chris',
19. email: 'test1@example.com',
20. role: calendarManager.AttendeeRole.ORGANIZER
21. },
22. {
23. name: 'Jack',
24. email: 'test2@example.com',
25. role: calendarManager.AttendeeRole.PARTICIPANT,
26. type: calendarManager.AttendeeType.REQUIRED
27. },
28. {
29. name: 'Jerry',
30. email: 'test3@example.com',
31. role: calendarManager.AttendeeRole.PARTICIPANT,
32. type: calendarManager.AttendeeType.REQUIRED
33. }
34. ];
35. const startTime = new Date('2025-10-20T09:00:00').getTime();
36. const endTime = new Date('2025-10-20T10:00:00').getTime();
37. // 日程配置信息
38. const event: calendarManager.Event = {
39. type: calendarManager.EventType.NORMAL,
40. title: 'xxx会议',
41. startTime: startTime,
42. endTime: endTime,
43. isAllDay: false,
44. reminderTime: [0, 15],
45. attendee: attendee,
46. description: 'xx事务评审',
47. // 一键服务
48. service: {
49. type: calendarManager.ServiceType.MEETING,
50. uri: 'demo://mobile/player?params='
51. }
52. }
53. try {
54. // 创建日历账户
55. let data: calendarManager.Calendar | undefined= await calendarMgr?.createCalendar(calendarAccount);
56. if (!data || data === null) {
57. console.error('Failed to create calendar. data is null.');
58. return;
59. }
60. // 请确保日历账户创建成功后，再进行相关日程的管理
61. // 设置日历配置信息，设置日历账户颜色
62. await data.setConfig(config);
63. // 添加日程
64. id = await data.addEvent(event);
65. console.info(`Succeeded in creating calendar and event, result: ${JSON.stringify(id)}`);
66. } catch (error) {
67. console.error(`Failed to create calendar or event. Code: ${error.code}, message: ${error.message}`);
68. }
69. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/hWR50ee9RH21kx1Y76MknA/zh-cn_image_0000002558605670.png?HW-CC-KV=V1&HW-CC-Date=20260429T053736Z&HW-CC-Expire=86400&HW-CC-Sign=EA6C0B09A2C722AEA29C59438B6B9E1A241BD9674FB2CD634211429C9A2E8EEF)
