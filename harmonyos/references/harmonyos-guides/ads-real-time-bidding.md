---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-real-time-bidding
title: 实时竞价
breadcrumb: 指南 > 应用服务 > Ads Kit（广告服务） > 流量变现服务开发 > 实时竞价
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:05+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:30d5b40dea845812e36a68a4243823da3e0c2ec334e52f9f361e33f7d26f5dd7
---

## 场景介绍

实时竞价是指用户在访问媒体产生曝光机会时，众多家DSP（Demand Side Platform，需求方平台）根据曝光的上下文以及用户属性实时地评估曝光价值并给出报价，出价最高的DSP胜出，赢得此次曝光机会。

## 约束与限制

支持Phone、Tablet、PC/2in1设备。

使用PC/2in1设备时，需要确保设备上智慧营销服务或广告服务的版本在8.4.80.300及以上，版本号可通过选择“设置> 应用和元服务 > 更多应用”查看。

## 支持场景

* 原生广告
* 激励广告
* 插屏广告
* 开屏广告
* 贴片广告

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [loadAd](../harmonyos-references/js-apis-advertising.md#loadad)(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener): void | 请求单广告位广告，通过AdRequestParams、AdOptions进行广告请求参数设置，通过AdLoadListener监听广告请求回调。 |
| [loadAdWithMultiSlots](../harmonyos-references/js-apis-advertising.md#loadadwithmultislots)(adParams: AdRequestParams[], adOptions: AdOptions, listener: MultiSlotsAdLoadListener): void | 请求多广告位广告，通过AdRequestParams[]、AdOptions进行广告请求参数设置，通过MultiSlotsAdLoadListener监听广告请求回调。 |

## 开发步骤

### 添加竞价参数

开发者需要在广告请求参数[AdRequestParams](../harmonyos-references/js-apis-advertising.md#adrequestparams)中添加实时竞价相关参数。

实时竞价关键参数如下所示：

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tMax | number | 否 | 交易的最大超时时间（包含网络延迟），单位ms。 |
| cur | string | 否 | 竞价请求支持的币种，支持传多个，用英文逗号分隔。当前支持五种货币：  1. CNY（单位：元）。  2. USD（单位：美元）。  3. EUR（单位：欧元）。  4. GBP（单位：英镑）。  5. JPY（单位：日元）。  不填默认是CNY。 |
| bidFloor | number | 否 | 竞价广告位的底价。当前支持五种货币：  1. CNY（单位：元）。  2. USD（单位：美元）。  3. EUR（单位：欧元）。  4. GBP（单位：英镑）。  5. JPY（单位：日元）。  不填默认是CNY。 |
| bidFloorCur | string | 否 | 竞价广告位底价使用的币种。如果bidFloor非空，则bidFloorCur也非空。当前只支持五种货币中的一种：  1. CNY（单位：元）。  2. USD（单位：美元）。  3. EUR（单位：欧元）。  4. GBP（单位：英镑）。  5. JPY（单位：日元）。  不填默认是CNY。 |
| bpkgName | string | 否 | 广告位竞投的APP包名，支持传多个，用英文逗号分隔。 |

示例代码如下所示：

```
1. import { advertising } from '@kit.AdsKit';

3. const adRequestParams: advertising.AdRequestParams = {
4. // 'h8asowxwhq'为测试专用的广告位ID，暂无竞价信息，App正式发布时需要改为正式的广告位ID
5. adId: 'h8asowxwhq',
6. // 广告类型
7. adType: 3,
8. // 交易的最大超时时间
9. tMax: 100,
10. // 竞价请求支持的币种，多个用英文逗号分隔
11. cur: 'CNY',
12. // 竞价广告位的底价
13. bidFloor: 6.66,
14. // 竞价广告位底价使用的币种
15. bidFloorCur: 'CNY',
16. // 广告位竞投的APP包名，多个用英文逗号分隔
17. bpkgName: 'com.huawei.baidu,com.huawei.music'
18. };
```

### 处理竞价结果

开发者需要在广告请求成功后的回调AdLoadListener.[onAdLoadSuccess](../harmonyos-references/js-apis-advertising.md#onadloadsuccess)或MultiSlotsAdLoadListener.[onAdLoadSuccess](../harmonyos-references/js-apis-advertising.md#onadloadsuccess)中，处理广告返回的实时竞价结果[Advertisement](../harmonyos-references/js-apis-advertisement.md#advertisement).biddingInfo。

实时竞价结果信息如下所示：

说明

回传竞价结果，需要申请使用Internet网络权限[ohos.permission.INTERNET](permissions-for-all.md#ohospermissioninternet)。详细申请权限流程请参考[开发准备](development-preparation.md)。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| price | number | 是 | 本条广告的eCPM（Effective Cost Per Mille，每一千次展示可以获得的广告收入）。 |
| cur | string | 是 | 本条广告的价格币种。支持币种：CNY（单位：元）、USD（单位：美元）、EUR（单位：欧元）、GBP（单位：英镑）、JPY（单位：日元）。 |
| nurl | string | 是 | 媒体回传竞价成功结果的URL。 |
| lurl | string | 是 | 媒体回传竞价失败结果的URL。 |

* 若广告竞胜，开发者需要替换nurl中的宏，并回传竞胜结果。

  宏说明如下：

  | 宏 | 说明 |
  | --- | --- |
  | SECOND\_PRICE | 竞胜时，其他DSP最高出价。样例：3.6。 |
  | AUCTION\_CURRENCY | 价格币种。支持币种：CNY（单位：元）、USD（单位：美元）、EUR（单位：欧元）、GBP（单位：英镑）、JPY（单位：日元）。 |
* 若广告竞败，开发者需要替换lurl中的宏，并回传竞败结果。

  宏说明如下：

  | 宏 | 说明 |
  | --- | --- |
  | AUCTION\_PRICE | 竞败时，其他DSP最高出价。样例：3.6。 |
  | AUCTION\_LOSS | 竞价结果，如果没有走到参竞环节也需要回调，并替换具体过滤结果码。  枚举：  102：竞价失败。  103：底价过滤。  104：包名过滤。  105：其他原因过滤。  4005：超时未返回。 |
  | AUCTION\_CURRENCY | 价格币种。支持币种：CNY（单位：元）、USD（单位：美元）、EUR（单位：欧元）、GBP（单位：英镑）、JPY（单位：日元）。 |
  | AUCTION\_APP\_PKG | 竞败时，竞胜DSP推广的App包名。 |
  | AUCTION\_APP\_NAME | 竞败时，竞胜DSP推广的App名称。 |
  | AUCTION\_CP\_ID | 竞败时，竞胜DSP的编号：  1：广点通  2：穿山甲  3：百青藤  4：快手联盟  5：爱奇艺  6：阿里  7：VIVO  8：OPPO  9：小米  10：京东  11：拼多多  100：其他 |

示例代码如下所示：

```
1. import { advertising } from '@kit.AdsKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { rcp } from '@kit.RemoteCommunicationKit';

5. interface BiddingInfo {
6. // 本条广告的eCPM（每一千次展示可以获得的广告收入）
7. price: number;

9. // 本条广告的价格币种
10. cur: string;

12. // 媒体回传竞价成功结果的URL
13. nurl: string;

15. // 媒体回传竞价失败结果的URL
16. lurl: string;
17. }

19. const adLoaderListener: advertising.AdLoadListener = {
20. // 广告请求失败回调
21. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
22. hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
23. },
24. // 广告请求成功回调
25. onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
26. hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
27. // 期望的底价
28. const bidFloor: number = 6;
29. const biddingSuccessAds: Array<advertising.Advertisement> = [];
30. for (const ad of ads) {
31. const biddingInfo: BiddingInfo = ad.biddingInfo as BiddingInfo;
32. if (!biddingInfo) {
33. continue;
34. }
35. if (biddingInfo.cur === 'CNY' && biddingInfo.price >= bidFloor) {
36. hilog.info(0x0000, 'testTag', 'Petal Ads wins.');
37. if (biddingInfo.nurl) {
38. const url: string = biddingInfo.nurl
39. // 竞胜时，其他DSP最高出价
40. .replace('SECOND_PRICE', '3.6')
41. // 价格币种
42. .replace('AUCTION_CURRENCY', 'CNY');
43. void sendBiddingResult(url).catch((error: BusinessError) => {
44. hilog.error(0x0000, 'testTag',
45. `Failed to sendBiddingResult. Code is ${error.code}, message is ${error.message}`);
46. });
47. }
48. biddingSuccessAds.push(ad);
49. } else {
50. hilog.info(0x0000, 'testTag', 'Petal Ads loses.');
51. if (biddingInfo.lurl) {
52. const url: string = biddingInfo.lurl
53. // 竞败时，其他DSP最高出价
54. .replace('AUCTION_PRICE', '3.6')
55. // 竞价结果
56. .replace('AUCTION_LOSS', '102')
57. // 价格币种
58. .replace('AUCTION_CURRENCY', 'CNY')
59. // 竞败时，竞胜DSP推广的App包名
60. .replace('AUCTION_APP_PKG', 'com.huawei.music')
61. // 竞败时，竞胜DSP推广的App名称
62. .replace('AUCTION_APP_NAME', 'music')
63. // 竞败时，竞胜DSP的编号
64. .replace('AUCTION_CP_ID', '100')
65. void sendBiddingResult(url).catch((error: BusinessError) => {
66. hilog.error(0x0000, 'testTag',
67. `Failed to sendBiddingResult. Code is ${error.code}, message is ${error.message}`);
68. });
69. }
70. }
71. }
72. // ...此处省略展示广告的逻辑
73. }
74. };

76. async function sendBiddingResult(url: string): Promise<void> {
77. let session: rcp.Session | undefined = undefined;
78. try {
79. session = rcp.createSession();
80. await session.get(url);
81. } catch (e) {
82. hilog.error(0x0000, 'testTag', `Failed to send bidding result. Code is ${e.code}, message is ${e.message}`);
83. } finally {
84. session?.close();
85. }
86. }
```
