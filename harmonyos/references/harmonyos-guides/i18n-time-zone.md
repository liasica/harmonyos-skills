---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-time-zone
title: 时区
breadcrumb: 指南 > 应用框架 > Localization Kit（本地化开发服务） > 应用国际化 > 时区与夏令时国际化 > 时区
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:32d72fc105597cc0cbb4a31a7b80209dcd329eb40d84569691b016e5c24920c3
---

## 使用场景

全球各国家和地区的经度不同，地方时间也有所不同，因此划分了不同的时区。例如，英国采用0时区，中国采用东8时区，中国时间要比英国快8小时，中国北京中午12:00，对应英国伦敦是凌晨4:00。时区模块可用于获取时区列表，应用可基于该列表实现业务逻辑，如双时钟应用。

从API version 20开始，时区模块还可用于获取时区跳变时间点和偏移量等，时区的跳变逻辑参考[夏令时跳变](i18n-dst-transition.md)。

## 接口说明

时区模块关键接口如下表所示，具体API说明详见[国际化-I18n](../harmonyos-references/js-apis-i18n.md)。

| 接口名 | 描述 |
| --- | --- |
| getTimeZone(zoneID?: string): TimeZone | 获取时区ID对应的时区对象。 |
| getID(): string | 获取时区对象的ID。 |
| getDisplayName(locale?: string, isDST?: boolean): string | 获取时区对象名称在指定语言下的翻译。 |
| getRawOffset(): number | 获取时区的固定偏移量。 |
| getOffset(date?: number): number | 获取某一时刻时区对象所表示时区的偏移量。 |
| getAvailableIDs(): Array<string> | 获取系统支持的时区ID列表。 |
| getAvailableZoneCityIDs(): Array<string> | 获取系统支持的时区城市ID列表。 |
| getCityDisplayName(cityID: string, locale: string): string | 获取时区城市名称在指定语言下的翻译。 |
| getTimezoneFromCity(cityID: string): TimeZone | 根据城市ID创建对应的时区对象。 |
| getTimezonesByLocation(longitude: number, latitude: number): Array<TimeZone> | 根据地理坐标获取所在时区对象的数组。 |
| getZoneRules(): ZoneRules | 获取时区跳变规则。 |
| nextTransition(date?: number): ZoneOffsetTransition | 获取指定时间的下一个时区跳变对象。 |
| getMilliseconds(): number | 获取时区跳变点的时间戳。 |
| getOffsetAfter(): number | 获取时区跳变后的偏移量。 |
| getOffsetBefore(): number | 获取时区跳变前的偏移量。 |

## 开发步骤

### 时区接口基本功能

1. 导入模块。

   ```
   1. import { i18n } from '@kit.LocalizationKit';
   ```

   [TimezoneDstSetting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/TimezoneDstSetting.ets#L19-L21)
2. 使用场景。

* 时区接口基本功能：包括获取特定时区、计算固定和实际时区偏移量、遍历时区列表。

  ```
  1. // 获取巴西时区
  2. let timezone: i18n.TimeZone = i18n.getTimeZone('America/Sao_Paulo'); // 传入特定时区，创建时区对象
  3. let timezoneId = timezone.getID(); // timezoneId = 'America/Sao_Paulo'

  5. // 获取城市ID对应的时区对象
  6. let aucklandTimezone: i18n.TimeZone = i18n.TimeZone.getTimezoneFromCity('Auckland');
  7. timezoneId = aucklandTimezone.getID(); // timezoneId = 'Pacific/Auckland'

  9. // 获取时区的本地化名称
  10. let timeZoneName = timezone.getDisplayName('zh-Hans', true); // timeZoneName = '巴西利亚标准时间'

  12. // 本地化城市名称
  13. let cityDisplayName = i18n.TimeZone.getCityDisplayName('Auckland', 'zh-Hans'); // cityDisplayName = '奥克兰 (新西兰)'

  15. // 时区的固定偏移量
  16. let rawOffset = timezone.getRawOffset(); // rawOffset = -10800000

  18. // 时区的实际偏移量（固定偏移量+夏令时）
  19. let offset = timezone.getOffset(1234567890); // offset = -10800000

  21. // 系统支持的时区ID列表
  22. let availableIDs = i18n.TimeZone.getAvailableIDs(); // availableIDs = ['America/Adak', 'Asia/Hovd', ...]

  24. // 系统支持的时区城市ID列表
  25. let cityIDs = i18n.TimeZone.getAvailableZoneCityIDs(); // cityIDs = ['Auckland', 'Magadan', ...]

  27. // 遍历时区城市ID列表
  28. let timezoneList: object[] = []; // 呈现给用户的时区列表

  30. class Item {
  31. public cityDisplayName = '';
  32. public timezoneId = '';
  33. public offset = '';
  34. public cityId = '';
  35. };

  37. for (let i = 0; i < cityIDs.length; i++) {
  38. let cityId = cityIDs[i];
  39. let timezone: i18n.TimeZone = i18n.TimeZone.getTimezoneFromCity(cityId); // 城市ID对应的时区对象
  40. let cityDisplayName = i18n.TimeZone.getCityDisplayName(cityId, 'zh-CN'); // 本地化城市名称
  41. let timestamp = (new Date()).getTime();
  42. let item: Item = {
  43. cityDisplayName: cityDisplayName,
  44. timezoneId: timezone.getID(),
  45. offset: 'GMT' + (timezone.getOffset(timestamp) / 3600 * 1000),
  46. cityId: cityId
  47. };
  48. timezoneList.push(item);
  49. }

  51. // 指定地理坐标所在的时区对象数组
  52. let timezoneArray: i18n.TimeZone[] = i18n.TimeZone.getTimezonesByLocation(-43.1, -22.5);

  54. // 获取指定时间的下一个时区跳变点
  55. let tijuanaTzId = 'America/Tijuana';
  56. let tijuanaTimeZone: i18n.TimeZone = i18n.getTimeZone(tijuanaTzId); // 获取蒂华纳时区对象
  57. let zoneRules: i18n.ZoneRules = tijuanaTimeZone.getZoneRules(); // 获取蒂华纳时区的时区跳变规则
  58. let someTime = new Date(2025, 4, 13);
  59. let zoneOffsetTrans: i18n.ZoneOffsetTransition = zoneRules.nextTransition(someTime.getTime());
  60. zoneOffsetTrans.getMilliseconds(); // 跳变点的时间戳: 1762074000000
  61. zoneOffsetTrans.getOffsetAfter(); // 跳变后的偏移量: -28800000
  62. zoneOffsetTrans.getOffsetBefore(); // 跳变前的偏移量: -25200000
  63. // 将跳变点时间格式化
  64. let dateTimeFormat: Intl.DateTimeFormat = new Intl.DateTimeFormat('en-US', {
  65. timeZone: tijuanaTzId,
  66. dateStyle: 'long',
  67. timeStyle: 'long',
  68. hour12: false
  69. });
  70. let dateFormat =
  71. dateTimeFormat.format(new Date(zoneOffsetTrans.getMilliseconds())); // November 2, 2025, 1:00:00 PST
  ```

  [TimezoneDstSetting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/TimezoneDstSetting.ets#L26-L98)
* 双时钟应用：首先选择时区列表中的时区，添加到应用偏好时区列表。然后遍历应用偏好时区列表，获取各时区的时间。

  ```
  1. let pauloTimezone: i18n.TimeZone = i18n.getTimeZone('America/Sao_Paulo');
  2. let defaultTimezone: i18n.TimeZone = i18n.getTimeZone();
  3. let appPreferredTimeZoneList: i18n.TimeZone[] = []; // 应用偏好时区列表
  4. appPreferredTimeZoneList.push(pauloTimezone);
  5. appPreferredTimeZoneList.push(defaultTimezone);

  7. let locale: Intl.Locale = i18n.System.getSystemLocaleInstance();
  8. for (let i = 0; i < appPreferredTimeZoneList.length; i++) {
  9. let timezone = appPreferredTimeZoneList[i].getID();
  10. let calendar: i18n.Calendar = i18n.getCalendar(locale.toString());
  11. calendar.setTimeZone(timezone); // 设置日历对象的时区
  12. // 获取年月日时分秒
  13. let year = calendar.get('year');
  14. let month = calendar.get('month');
  15. let day = calendar.get('date');
  16. let hour = calendar.get('hour');
  17. let minute = calendar.get('minute');
  18. let second = calendar.get('second');
  19. }
  ```

  [TimezoneDstSetting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/TimezoneDstSetting.ets#L100-L130)
