---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-autoadcomponent
title: @ohos.advertising.AutoAdComponent (轮播广告展示组件)
breadcrumb: API参考 > 应用服务 > Ads Kit（广告服务） > ArkTS组件 > @ohos.advertising.AutoAdComponent (轮播广告展示组件)
category: harmonyos-references
scraped_at: 2026-04-29T14:06:57+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:86c46bd435e732c50b59cd3c8a62de649e20011e7b304c8aafa33dd4ae63decf
---

本模块提供展示轮播广告的能力。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1Tablet

```
1. import { AutoAdComponent } from '@kit.AdsKit';
```

## AutoAdComponent

PhonePC/2in1Tablet

```
1. AutoAdComponent({
2. adParam: advertising.AdRequestParams,
3. adOptions: advertising.AdOptions,
4. displayOptions: advertising.AdDisplayOptions,
5. interactionListener: advertising.AdInteractionListener
6. })
```

用于展示轮播广告的组件。

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **参数名** | **类型** | 必填 | **装饰器类型** | 说明 |
| --- | --- | --- | --- | --- |
| adParam | advertising.[AdRequestParams](js-apis-advertising.md#adrequestparams) | 是 | - | 广告请求参数。 |
| adOptions | advertising.[AdOptions](js-apis-advertising.md#adoptions) | 是 | - | 广告配置参数。 |
| displayOptions | advertising.[AdDisplayOptions](js-apis-advertising.md#addisplayoptions) | 是 | - | 广告展示参数。 |
| interactionListener | advertising.[AdInteractionListener](js-apis-advertising.md#adinteractionlistener) | 是 | - | 广告状态变化回调。 |

**示例：**

```
1. import { advertising, AutoAdComponent } from '@kit.AdsKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. // 广告请求参数
8. private adRequestParams: advertising.AdRequestParams = {
9. // 广告位ID
10. adId: 'h5xkz3mbr2',
11. // 广告类型
12. adType: 8,
13. // 广告位宽，单位vp
14. adWidth: 360,
15. // 广告位高，单位vp
16. adHeight: 57
17. };
18. // 广告配置参数
19. private adOptions: advertising.AdOptions = {};
20. // 广告展示参数
21. private adDisplayOptions: advertising.AdDisplayOptions = {
22. // 广告轮播的时间间隔，单位ms，取值范围[30000, 120000]
23. refreshTime: 30000
24. };
25. private ratio: number = -1;

27. aboutToAppear() {
28. if (this.adRequestParams.adWidth && this.adRequestParams.adHeight) {
29. this.ratio = this.adRequestParams.adWidth / this.adRequestParams.adHeight;
30. }
31. }

33. build() {
34. Column() {
35. AutoAdComponent({
36. adParam: this.adRequestParams,
37. adOptions: this.adOptions,
38. displayOptions: this.adDisplayOptions,
39. interactionListener: {
40. onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
41. switch (status) {
42. case 'onAdOpen':
43. hilog.info(0x0000, 'testTag', 'onAdOpen');
44. break;
45. case 'onAdClick':
46. hilog.info(0x0000, 'testTag', 'onAdClick');
47. break;
48. case 'onAdClose':
49. hilog.info(0x0000, 'testTag', 'onAdClose');
50. break;
51. }
52. }
53. }
54. })
55. .width('100%')
56. .aspectRatio(this.ratio)
57. }
58. .width('100%')
59. .height('100%')
60. }
61. }
```

**效果图：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/mQgIpDsYSjqDBYP2N4ASTw/zh-cn_image_0000002558605608.png?HW-CC-KV=V1&HW-CC-Date=20260429T060656Z&HW-CC-Expire=86400&HW-CC-Sign=806793C52B56DD90F7A9E6580E28079D6D651D001AD055B5F77F078A5730816C)

### build

PhonePC/2in1Tablet

build(): void

用于创建AutoAdComponent对象的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads
