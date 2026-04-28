---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/appgallery-appinfomanager
title: appInfoManager（应用元数据管理服务）
breadcrumb: API参考 > 应用服务 > AppGallery Kit（应用市场服务） > ArkTS API > appInfoManager（应用元数据管理服务）
category: harmonyos-references
scraped_at: 2026-04-28T08:16:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8d01cf293aa38e3581d0bbd01779b8d3d34d66c783c3aa17714de6447c88f773
---

提供查询动态图标信息、选择动态图标、禁用动态图标功能。

说明

调用接口需捕获异常。

**起始版本：** 5.0.3(15)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { appInfoManager } from '@kit.AppGalleryKit';
```

## DynamicIconInfo

PhonePC/2in1TabletTVWearable

动态图标信息。

**系统能力：** SystemCapability.AppGalleryService.AppInfoManager

**起始版本：** 5.0.3(15)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iconUrl | string | 是 | 否 | 动态图标链接。 |
| iconId | string | 是 | 否 | 动态图标ID。 |
| enabled | boolean | 是 | 否 | 该动态图标是否正在使用中。true表示当前正在使用中，false表示当前未使用。 |

## appInfoManager.queryDynamicIcons

PhonePC/2in1TabletTVWearable

queryDynamicIcons(): Promise<DynamicIconInfo[]>

查询动态图标信息。通过Promise异步回调。

**系统能力：** SystemCapability.AppGalleryService.AppInfoManager

**起始版本：** 5.0.3(15)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DynamicIconInfo](appgallery-appinfomanager.md#dynamiciconinfo)[]> | Promise对象，返回动态图标信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006800001 | The specified service extension connect failed. |
| 1006800009 | System internal error. |
| 1006800010 | No dynamic icon data. |

**示例：**

```
1. import { appInfoManager } from '@kit.AppGalleryKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. const TAG: string = 'dynamicIconManager';

7. @Entry
8. @Component
9. @Preview
10. struct DynamicIconPage {

12. scroller: Scroller = new Scroller();
13. @State dynamicIconInfos: appInfoManager.DynamicIconInfo[] = [];
14. @State message: string = '';

16. private queryDynamicIcon() {
17. try {
18. hilog.info(0, TAG, `queryDynamicIcon start.`);
19. // 查询动态图标信息,返回动态图标信息
20. appInfoManager.queryDynamicIcons().then((iconInfos: appInfoManager.DynamicIconInfo[]) => {
21. hilog.info(0, TAG, `queryDynamicIcons success. iconInfos: ${JSON.stringify(iconInfos)}`);
22. this.dynamicIconInfos = iconInfos;
23. this.message = JSON.stringify(iconInfos);
24. }).catch((error: BusinessError) => {
25. this.message = `queryDynamicIcon failed: ${JSON.stringify(error)}`;
26. hilog.error(0, TAG,
27. `queryDynamicIcons failed, code: ${error.code}, exception message: ${error.message}`);
28. })
29. } catch (error) {
30. this.message = `queryDynamicIcon exception: ${JSON.stringify(error)}`;
31. hilog.error(0, TAG,
32. `queryDynamicIcons exception, code: ${error.code}, exception message: ${error.message}`);
33. }
34. }

36. build() {
37. Scroll(this.scroller) {
38. Column() {
39. Row() {
40. Button("queryDynamicIcons").onClick(() => {
41. this.queryDynamicIcon();
42. }).margin({ top: 4, bottom: 4 })
43. }
44. }
45. }
46. }
47. }
```

## appInfoManager.selectDynamicIcon

PhonePC/2in1TabletTVWearable

selectDynamicIcon(iconId: string): Promise<void>

选择动态图标。通过Promise异步回调。

**系统能力：** SystemCapability.AppGalleryService.AppInfoManager

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| iconId | string | 是 | 动态图标ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006800009 | System internal error. |
| 1006800011 | Select dynamic icon failed. |
| 1006800013 | Failed to switch to the custom icon because a custom theme icon is currently in use. |

说明

从版本6.0.0(20)开始，该接口支持返回1006800013错误码。

**示例：**

```
1. import { appInfoManager } from '@kit.AppGalleryKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let iconId: string = 'iconId';
7. appInfoManager.selectDynamicIcon(iconId).then(() => {
8. hilog.info(0, 'TAG', "Succeeded in selecting dynamic icon");
9. }).catch((error: BusinessError) => {
10. hilog.error(0, 'TAG', "selectDynamicIcon failed, code: " + error.code + ", exception message: " + error.message);
11. });
12. } catch (error) {
13. hilog.error(0, 'TAG', "selectDynamicIcon exception code: " + error.code + ", exception message: " + error.message);
14. }
```

## appInfoManager.disableDynamicIcon

PhonePC/2in1TabletTVWearable

disableDynamicIcon(): Promise<void>

禁用动态图标，恢复默认图标。通过Promise异步回调。

**系统能力：** SystemCapability.AppGalleryService.AppInfoManager

**起始版本：** 5.0.3(15)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006800009 | System internal error. |
| 1006800012 | Disable dynamic icon failed. |

**示例：**

```
1. import { appInfoManager } from '@kit.AppGalleryKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. appInfoManager.disableDynamicIcon().then(() => {
7. hilog.info(0, 'TAG', "Succeeded in disabling dynamic icon");
8. }).catch((error: BusinessError) => {
9. hilog.error(0, 'TAG', "disableDynamicIcon failed, code: " + error.code + ", exception message: " + error.message);
10. });
11. } catch (error) {
12. hilog.error(0, 'TAG', "disableDynamicIcon exception code: " + error.code + ", exception message: " + error.message);
13. }
```
