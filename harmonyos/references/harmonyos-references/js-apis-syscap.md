---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-syscap
title: SysCap (系统能力)
breadcrumb: API参考 > 公共基础能力 > ArkTS API > SysCap (系统能力)
category: harmonyos-references
scraped_at: 2026-04-28T08:19:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f67b03c836c0382153b55749374c09dc00d706f5f77ae532e4a2396bca674ecc
---

系统能力（SystemCapability，简称SysCap），指操作系统中每一个相对独立的特性。不同的设备对应不同的系统能力集，每个系统能力对应一个或多个API。开发者可根据系统能力来判断是否可以使用某接口。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## canIUse

PhonePC/2in1TabletTVWearable

canIUse(syscap: string): boolean

查询系统是否具备某个系统能力。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| syscap | string | 是 | 待查询的系统能力名称。不支持输入null、undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 系统能力查询结果，true表示系统具备该能力，false表示系统不具备。 |

**示例：**

```
1. import { geoLocationManager } from '@kit.LocationKit'
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const isLocationAvailable = canIUse('SystemCapability.Location.Location.Core');
5. if (isLocationAvailable) {
6. geoLocationManager.getCurrentLocation((err: BusinessError, location: geoLocationManager.Location) => {
7. if (err) {
8. console.error('err=' + JSON.stringify(err));
9. }
10. if (location) {
11. console.info('location=' + JSON.stringify(location));
12. }
13. });
14. } else {
15. console.info('Location not by this device.');
16. }
```
