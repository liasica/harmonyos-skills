---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-calendar
title: calendar
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 基础组件 > calendar
category: harmonyos-references
scraped_at: 2026-04-29T13:54:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b57b36a9a56bdfee123a302a6783e3fe61f609dd057fa097d104991e044d0ca2
---

日历组件，用于呈现日历界面。

说明

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](js-service-widget-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| date | string | 当前日期 | 否 | 当前页面选中的日期，默认是当前日期，格式为年-月-日，如"2019-11-22"。 |
| cardcalendar | boolean | false | 否 | 标识当前日历是否为卡片日历。  默认值：false，表示标识当前日历不是卡片日历。 |
| startdayofweek | int | 6 | 否 | 标识卡片显示的起始天，默认是星期天（取值范围：0-6）。 |
| offdays | string | 5，6 | 否 | 标识卡片显示的休息日，默认是星期六、星期天（取值范围：0-6）。 |
| calendardata | string | - | 是 | 卡片需要显示的月视图数据信息，包括5\*7或者6\*7格的日数据信息，格式为JSON字符串。"data"标签属性信息见**表1** calendardata的日属性。 |
| showholiday | boolean | true | 否 | 标识当前是否显示节假日信息。  默认值：true，表示标识当前要显示节假日信息。 |

**表1** calendardata的日属性

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| index | int | 数据的索引，表示第几个日期。 |
| day | int | 表示具体哪一天。 |
| month | int | 表示月份。 |
| year | int | 表示年份。 |
| isFirstOfLunar | boolean | 表示是否是农历的第一天，在农历第一天的数据下绘制横线。取值true，表示是农历的第一天。取值false，表示不是农历的第一天。 |
| hasSchedule | boolean | 表示是否有日程，在有日程的日期数据上绘制圆。取值true，表示当前有日程。取值false，表示当前无日程。 |
| markLunarDay | boolean | 表示节假日时，农历数据部分是否会变成蓝色。取值true，表示当天为节假日时，农历数据部分会变成蓝色。取值false，表示当天为节假日时，农历数据部分不会变成蓝色。 |
| lunarDay | string | 农历日期。 |
| lunarMonth | string | 农历月份。 |
| dayMark | string | 表示工作日。  - “work”：工作日。  - “off”：休息日。 |
| dayMarkValue | string | 表示具体需要显示的“班”、“休”信息。 |

calendardata示例：

```
1. {
2. "year":2021,
3. "month":1,
4. "data": [{
5. "index": 0,
6. "lunarMonth": "十一",
7. "lunarDay": "十三",
8. "year": 2020,
9. "month": 12,
10. "day": 27,
11. "dayMark": "work",
12. "dayMarkValue": "班",
13. "isFirstOfLunar": true,
14. "hasSchedule": true,
15. "markLunarDay": true
16. },  {
17. "index": 1,
18. "lunarMonth": "十一",
19. "lunarDay": "十四",
20. "year": 2020,
21. "month": 12,
22. "day": 28,
23. "dayMark": "work",
24. "dayMarkValue": "班",
25. "isFirstOfLunar": true,
26. "hasSchedule": true,
27. "markLunarDay": true
28. },  {
29. "index": 2,
30. "lunarMonth": "十一",
31. "lunarDay": "十五",
32. "year": 2020,
33. "month": 12,
34. "day": 29,
35. "dayMark": "work",
36. "dayMarkValue": "班",
37. "isFirstOfLunar": true,
38. "hasSchedule": true,
39. "markLunarDay": true
40. },
41. ...
42. ]
43. }
```

## 样式

PhonePC/2in1TabletTVWearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| background-color | <color> | - | 否 | 设置背景颜色。 |

## 事件

PhonePC/2in1TabletTVWearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| selectedchange | changeEvent | 在点击日期和上下月跳转时触发。 |
| requestdata | requestEvent | 请求日期时触发。 |

**表2** changeEvent

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| $event.day | string | 选择的日期。 |
| $event.month | string | 选择的月份。 |
| $event.year | string | 选择的年份。 |

**表3** requestEvent

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| $event.month | string | 请求的月份。 |
| $event.year | string | 请求的年份。 |
| $event.currentYear | string | 当前显示的年份。 |
| $event.currentMonth | string | 当前显示的月份。 |

## 示例

PhonePC/2in1TabletTVWearable

当前数据仅为示例数据，实际使用时请补充完整的日期数据。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <calendar class="container_test"
4. cardcalendar="true"
5. onselectedchange="clickOneDay"
6. onrequestdata="messageEventData"
7. date="{{currentDate}}"
8. offdays="{{offDays}}"
9. showholiday="{{showHoliday}}"
10. startdayofweek="{{startDayOfWeek}}"
11. calendardata="{{calendarData}}">
12. </calendar>
13. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction:column;
4. width: 100%;
5. height: 100%;
6. align-items:center;
7. padding-start: 4px;
8. padding-end: 4px;
9. }
10. .container_test {
11. background-color: white;
12. }
```

```
1. {
2. "data": {
3. "currentDate": "",
4. "offDays": "",
5. "startDayOfWeek": 6,
6. "showHoliday": true,
7. "calendarData": ""
8. },
9. "actions": {
10. "clickOneDay": {
11. "action": "router",
12. "bundleName": "com.example.calendar",
13. "abilityName": "EntryAbility",
14. "params": {
15. "action": "click_month_view_event",
16. "day": "$event.day",
17. "month": "$event.month",
18. "year": "$event.year"
19. }
20. },
21. "messageEventData": {
22. "action": "message",
23. "params": {
24. "month": "$event.month",
25. "year": "$event.year",
26. "currentMonth": "$event.currentMonth",
27. "currentYear": "$event.currentYear"
28. }
29. }
30. }
31. }
```

**4\*4卡片**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/xFPZIcxkT6-KFKYWfZc7ag/zh-cn_image_0000002558766954.png?HW-CC-KV=V1&HW-CC-Date=20260429T055400Z&HW-CC-Expire=86400&HW-CC-Sign=806C113CBDDC6733A2F8C88E9DFA3CABCEEEDF2DEE972BF0C6279D031468F703)
