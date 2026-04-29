---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-adcomponent
title: @ohos.advertising.AdComponent (广告展示组件)
breadcrumb: API参考 > 应用服务 > Ads Kit（广告服务） > ArkTS组件 > @ohos.advertising.AdComponent (广告展示组件)
category: harmonyos-references
scraped_at: 2026-04-29T14:06:57+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:ac85afebb958aaf568c73075a2cd01afb47b461e3842228aed40735447fd0dad
---

本模块提供展示广告的能力，覆盖了原生、贴片、开屏等广告样式。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1Tablet

```
1. import { AdComponent } from '@kit.AdsKit';
```

## AdComponent

PhonePC/2in1Tablet

```
1. AdComponent({
2. ads: advertising.Advertisement[],
3. displayOptions: advertising.AdDisplayOptions,
4. interactionListener: advertising.AdInteractionListener,
5. @BuilderParam adRenderer?: () => void,
6. @Prop rollPlayState?: number
7. })
```

广告展示组件，提供展示原生、贴片、开屏等广告的能力。

**装饰器类型：**@Component

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| ads | advertising.[Advertisement](js-apis-advertisement.md#advertisement)[] | 是 | 广告对象数组。  说明：非贴片广告类型，组件只展示数组第一个数据。  元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| displayOptions | advertising.[AdDisplayOptions](js-apis-advertising.md#addisplayoptions) | 是 | 广告展示参数。  元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| interactionListener | advertising.[AdInteractionListener](js-apis-advertising.md#adinteractionlistener) | 是 | 广告状态变化回调。  元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| adRenderer12+ | () => void | 否 | 应用自渲染广告样式。应用自渲染广告样式为受限使用能力，具体请前往[流量变现官网客服支持](../monetize/kefuzhichi-0000001104461922.md)进行咨询。  元服务API：从API version 20开始，该接口支持在元服务中使用。  装饰器类型：@BuilderParam |
| rollPlayState15+ | number | 否 | 用于对外提供贴片广告播放状态，设置1为播放，2为暂停，默认值为2，其他值为非法值，不改变之前的播放状态。在贴片广告所在页面需要通过@State关联属性，使用方法参考[示例代码](../harmonyos-guides/ads-publisher-service-roll.md#展示广告)。  元服务API：从API version 20开始，该接口支持在元服务中使用。  装饰器类型：@Prop |

说明

为了保证广告能正确展示，该接口必须和请求广告接口配套使用。效果和使用方法可参考[原生广告](../harmonyos-guides/ads-publisher-service-native.md)、[贴片广告](../harmonyos-guides/ads-publisher-service-roll.md)、[开屏广告](../harmonyos-guides/ads-publisher-service-splash.md)接入和展示。

**示例：**

```
1. import { AdComponent, advertising } from '@kit.AdsKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. // 请求到的广告内容
8. private ads: advertising.Advertisement[] = [];
9. // 广告展示参数
10. private adDisplayOptions: advertising.AdDisplayOptions = {};

12. build() {
13. Column() {
14. AdComponent({
15. ads: this.ads,
16. displayOptions: this.adDisplayOptions,
17. interactionListener: {
18. onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
19. switch (status) {
20. case 'onAdOpen':
21. hilog.info(0x0000, 'testTag', 'onAdOpen');
22. break;
23. case 'onAdClick':
24. hilog.info(0x0000, 'testTag', 'onAdClick');
25. break;
26. case 'onAdClose':
27. hilog.info(0x0000, 'testTag', 'onAdClose');
28. break;
29. }
30. }
31. }
32. })
33. .width('100%')
34. .height('100%')
35. }
36. .width('100%')
37. .height('100%')
38. }
39. }
```

### build

PhonePC/2in1Tablet

build(): void

用于创建AdComponent对象的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads
