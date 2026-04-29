---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising
title: @ohos.advertising (广告服务框架)
breadcrumb: API参考 > 应用服务 > Ads Kit（广告服务） > ArkTS API > @ohos.advertising (广告服务框架)
category: harmonyos-references
scraped_at: 2026-04-29T14:06:56+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:fa94579c99c14f28f8f37745eccd545d580c424b3919141a2475f6445f33f612
---

本模块提供广告操作能力，包括请求广告、展示广告。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1Tablet

```
1. import { advertising } from '@kit.AdsKit';
```

## advertising.showAd

PhonePC/2in1Tablet

showAd(ad: Advertisement, options: AdDisplayOptions, context?: common.UIAbilityContext): void

展示全屏广告。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| ad | [Advertisement](js-apis-advertisement.md#advertisement) | 是 | 广告对象。 |
| options | [AdDisplayOptions](js-apis-advertising.md#addisplayoptions) | 是 | 广告展示参数。 |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 否 | UIAbility的上下文环境，不设置从api: [@ohos.app.ability.common](js-apis-app-ability-common.md)中获取。 |

**错误码：**

以下错误码的详细介绍请参见[广告服务框架错误码参考](errorcode-ads.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. Possible causes:  1. Mandatory parameters are left unspecified. |
| 21800001 | System internal error. |
| 21800004 | Failed to display the ad. |

说明

1. 为了保证广告能正确展示，该接口必须和请求广告接口配套使用。
2. 该接口仅支持展示激励广告和插屏广告。

**示例：**

其中context的获取方式参见[各类context的获取方式](../harmonyos-guides/application-context-stage.md#context的获取方式)。

```
1. import { common } from '@kit.AbilityKit';
2. import { advertising } from '@kit.AdsKit';

4. function showAd(ad: advertising.Advertisement, context?: common.UIAbilityContext): void {
5. // 广告展示参数，开发者可根据项目实际情况设置
6. const adDisplayOptions: advertising.AdDisplayOptions = {};
7. // 调用全屏广告展示接口
8. advertising.showAd(ad, adDisplayOptions, context);
9. }
```

## advertising.getAdRequestBody12+

PhonePC/2in1Tablet

getAdRequestBody(adParams: AdRequestParams[], adOptions: AdOptions): Promise<string>

获取广告请求体，使用Promise异步回调（该接口仅对部分系统预置应用开放）。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| adParams | [AdRequestParams](js-apis-advertising.md#adrequestparams)[] | 是 | 广告请求参数。  **说明：** 该接口体的adId参数可以为空。 |
| adOptions | [AdOptions](js-apis-advertising.md#adoptions) | 是 | 广告配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回字符类型的广告数据。 |

**错误码：**

以下错误码的详细介绍请参见[广告服务框架错误码参考](errorcode-ads.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 801 | Device not supported. |
| 21800001 | System internal error. |

**示例：**

```
1. import { advertising } from '@kit.AdsKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. async function getAdRequestBody(adRequestParamsArray: advertising.AdRequestParams[]): Promise<void> {
6. // 广告配置参数，开发者可根据项目实际情况设置
7. const adOptions: advertising.AdOptions = {};
8. await advertising.getAdRequestBody(adRequestParamsArray, adOptions).then((data: string) => {
9. hilog.info(0x0000, 'testTag', `Succeeded in getting ad request body. Data is ${data}`);
10. }).catch((error: BusinessError) => {
11. hilog.info(0x0000, 'testTag', `Failed to get ad request body. Code is ${error.code}, message is ${error.message}`);
12. });
13. }
```

## advertising.parseAdResponse12+

PhonePC/2in1Tablet

parseAdResponse(adResponse: string, listener: MultiSlotsAdLoadListener, context: common.UIAbilityContext): void

解析并处理广告响应体（该接口仅对部分系统预置应用开放）。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| adResponse | string | 是 | 广告响应体。 |
| listener | [MultiSlotsAdLoadListener](js-apis-advertising.md#multislotsadloadlistener) | 是 | 请求广告回调监听。 |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | UIAbility的上下文环境。 |

**错误码：**

以下错误码的详细介绍请参见[广告服务框架错误码参考](errorcode-ads.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 801 | Device not supported. |
| 21800001 | System internal error. |
| 21800005 | Failed to parse the ad response. |

**示例：**

其中context的获取方式参见[各类context的获取方式](../harmonyos-guides/application-context-stage.md#context的获取方式)。

```
1. import { common } from '@kit.AbilityKit';
2. import { advertising } from '@kit.AdsKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. function parseAdResponse(adResponse: string, context: common.UIAbilityContext): void {
6. // 广告解析处理回调监听
7. const multiSlotsAdLoaderListener: advertising.MultiSlotsAdLoadListener = {
8. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
9. hilog.error(0x0000, 'testTag', `Failed to load multiSlots ad. Code is ${errorCode}, message is ${errorMsg}`);
10. },
11. onAdLoadSuccess: (ads: Map<string, Array<advertising.Advertisement>>) => {
12. hilog.info(0x0000, 'testTag', 'Succeeded in loading multiSlots ad');
13. // 保存解析处理完成的广告内容用于展示
14. const returnAds: advertising.Advertisement[] = [];
15. ads.forEach((adsArray) => returnAds.push(...adsArray));
16. }
17. };
18. // 调用响应体解析接口
19. advertising.parseAdResponse(adResponse, multiSlotsAdLoaderListener, context);
20. }
```

## advertising.registerWebAdInterface12+

PhonePC/2in1Tablet

registerWebAdInterface(controller: web\_webview.WebviewController, context: common.UIAbilityContext): void

注入广告JavaScript对象到Web组件中（该接口仅对部分系统预置应用开放）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | web\_webview.[WebviewController](arkts-apis-webview-webviewcontroller.md) | 是 | Web组件控制器。 |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | UIAbility的上下文环境。 |

**错误码：**

以下错误码的详细介绍请参见[广告服务框架错误码参考](errorcode-ads.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. Possible causes:  1. Mandatory parameters are left unspecified. |
| 21800001 | System internal error. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { advertising } from '@kit.AdsKit';
3. import { webview } from '@kit.ArkWeb';

5. @Entry
6. @Component
7. struct Index {
8. private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. private webViewController: webview.WebviewController = new webview.WebviewController();

11. build() {
12. Column() {
13. Button('registerWebAdInterface')
14. .onClick(() => {
15. advertising.registerWebAdInterface(this.webViewController, this.context);
16. })
17. // ...

19. Web({ src: 'https://www.example.com', controller: this.webViewController })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

## advertising.registerWebAdInterface16+

PhonePC/2in1Tablet

registerWebAdInterface(controller: web\_webview.WebviewController, context: common.UIAbilityContext, needRefresh: boolean): void

注入广告JavaScript对象到Web组件中（该接口仅对部分系统预置应用开放）。

**元服务API：** 从API version 16开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | web\_webview.[WebviewController](arkts-apis-webview-webviewcontroller.md) | 是 | Web组件控制器。 |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | UIAbility的上下文环境。 |
| needRefresh | boolean | 是 | 是否需要刷新页面（true: 需要；false: 不需要）。 |

**错误码：**

以下错误码的详细介绍请参见[广告服务框架错误码参考](errorcode-ads.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. Possible causes: Mandatory parameters are left unspecified. |
| 21800001 | System internal error. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { advertising } from '@kit.AdsKit';
3. import { webview } from '@kit.ArkWeb';

5. @Entry
6. @Component
7. struct Index {
8. private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. private webViewController: webview.WebviewController = new webview.WebviewController();

11. build() {
12. Column() {
13. // ...
14. Button('registerWebAdInterface')
15. .onClick(() => {
16. advertising.registerWebAdInterface(this.webViewController, this.context, true);
17. })

19. Web({ src: 'https://www.example.com', controller: this.webViewController })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

## advertising.deleteWebAdInterface16+

PhonePC/2in1Tablet

deleteWebAdInterface(controller: web\_webview.WebviewController, needRefresh: boolean): void

删除通过registerWebAdInterface注入的广告JavaScript对象（该接口仅对部分系统预置应用开放）。

**元服务API：** 从API version 16开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | web\_webview.[WebviewController](arkts-apis-webview-webviewcontroller.md) | 是 | Web组件控制器。 |
| needRefresh | boolean | 是 | 是否需要刷新页面（true: 需要；false: 不需要）。 |

**错误码：**

以下错误码的详细介绍请参见[广告服务框架错误码参考](errorcode-ads.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. Possible causes: Mandatory parameters are left unspecified. |
| 21800001 | System internal error. |

**示例：**

```
1. import { advertising } from '@kit.AdsKit';
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct Index {
7. private webViewController: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('deleteWebAdInterface')
12. .onClick(() => {
13. advertising.deleteWebAdInterface(this.webViewController, true);
14. })

16. Web({ src: 'https://www.example.com', controller: this.webViewController })
17. }
18. .width('100%')
19. .height('100%')
20. }
21. }
```

## AdLoader

PhonePC/2in1Tablet

提供加载广告的功能

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

### constructor

PhonePC/2in1Tablet

constructor(context: common.Context)

构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[Context](js-apis-inner-application-context.md) | 是 | ability或application的上下文环境。 |

**示例：**

其中context的获取方式参见[各类context的获取方式](../harmonyos-guides/application-context-stage.md#context的获取方式)。

```
1. import { common } from '@kit.AbilityKit';
2. import { advertising } from '@kit.AdsKit';
3. // ...

5. function createAdLoader(context: common.Context): void {
6. const adLoader: advertising.AdLoader = new advertising.AdLoader(context);
7. }
```

### loadAd

PhonePC/2in1Tablet

loadAd(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener): void

请求单广告位广告。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| adParam | [AdRequestParams](js-apis-advertising.md#adrequestparams) | 是 | 广告请求参数。 |
| adOptions | [AdOptions](js-apis-advertising.md#adoptions) | 是 | 广告配置参数。 |
| listener | [AdLoadListener](js-apis-advertising.md#adloadlistener) | 是 | 请求广告回调监听。 |

**错误码：**

以下错误码的详细介绍请参见[广告服务框架错误码参考](errorcode-ads.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 801 | Device not supported. |
| 21800001 | System internal error. |
| 21800003 | Failed to load the ad request. |

**示例：**

其中context的获取方式参见[各类context的获取方式](../harmonyos-guides/application-context-stage.md#context的获取方式)。

```
1. import { common } from '@kit.AbilityKit';
2. import { advertising } from '@kit.AdsKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // ...
6. function loadAd(context: common.Context, adRequestParams: advertising.AdRequestParams): void {
7. // 广告配置参数，开发者可根据项目实际情况设置
8. const adOptions: advertising.AdOptions = {};
9. // 广告请求回调监听
10. const adLoaderListener: advertising.AdLoadListener = {
11. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
12. hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
13. },
14. onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
15. hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
16. // 保存请求到的广告内容用于展示
17. const returnAds: advertising.Advertisement[] = ads;
18. }
19. };
20. // 创建AdLoader广告对象
21. const adLoader: advertising.AdLoader = new advertising.AdLoader(context);
22. // 调用广告请求接口
23. adLoader.loadAd(adRequestParams, adOptions, adLoaderListener);
24. }
```

### loadAdWithMultiSlots

PhonePC/2in1Tablet

loadAdWithMultiSlots(adParams: AdRequestParams[], adOptions: AdOptions, listener: MultiSlotsAdLoadListener): void

请求多广告位广告。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| adParams | [AdRequestParams](js-apis-advertising.md#adrequestparams)[] | 是 | 广告请求参数。 |
| adOptions | [AdOptions](js-apis-advertising.md#adoptions) | 是 | 广告配置参数。 |
| listener | [MultiSlotsAdLoadListener](js-apis-advertising.md#multislotsadloadlistener) | 是 | 请求广告回调监听。 |

**错误码：**

以下错误码的详细介绍请参见[广告服务框架错误码参考](errorcode-ads.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 801 | Device not supported. |
| 21800001 | System internal error. |
| 21800003 | Failed to load the ad request. |

**示例：**

其中context的获取方式参见[各类context的获取方式](../harmonyos-guides/application-context-stage.md#context的获取方式)。

```
1. import { common } from '@kit.AbilityKit';
2. import { advertising } from '@kit.AdsKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // ...
6. function loadAdWithMultiSlots(context: common.Context, adRequestParamsArray: advertising.AdRequestParams[]): void {
7. // 广告配置参数，开发者可根据项目实际情况设置
8. const adOptions: advertising.AdOptions = {};
9. // 广告请求回调监听
10. const multiSlotsAdLoaderListener: advertising.MultiSlotsAdLoadListener = {
11. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
12. hilog.error(0x0000, 'testTag', `Failed to load multiSlots ad. Code is ${errorCode}, message is ${errorMsg}`);
13. },
14. onAdLoadSuccess: (ads: Map<string, Array<advertising.Advertisement>>) => {
15. hilog.info(0x0000, 'testTag', 'Succeeded in loading multiSlots ad');
16. // 保存请求到的广告内容用于展示
17. const returnAds: advertising.Advertisement[] = [];
18. ads.forEach((adsArray) => returnAds.push(...adsArray));
19. }
20. };
21. // 创建AdLoader广告对象
22. const adLoader: advertising.AdLoader = new advertising.AdLoader(context);
23. // 调用广告请求接口
24. adLoader.loadAdWithMultiSlots(adRequestParamsArray, adOptions, multiSlotsAdLoaderListener);
25. }
```

## AdLoadListener

PhonePC/2in1Tablet

单广告位广告请求回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

### onAdLoadFailure

PhonePC/2in1Tablet

onAdLoadFailure(errorCode: number, errorMsg: string): void

广告请求失败回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

| 名称 | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| errorCode | number | 是 | 广告请求失败的错误码。 |
| errorMsg | string | 是 | 广告请求失败的错误信息。 |

**示例：**

```
1. import { advertising } from '@kit.AdsKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const adLoaderListener: advertising.AdLoadListener = {
5. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
6. hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
7. },
8. onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
9. hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
10. }
11. }
```

### onAdLoadSuccess

PhonePC/2in1Tablet

onAdLoadSuccess(ads: Array<Advertisement>): void

广告请求成功后回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

| 名称 | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| ads | Array<[Advertisement](js-apis-advertisement.md#advertisement)> | 是 | 广告数据。 |

**示例：**

```
1. import { advertising } from '@kit.AdsKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const adLoaderListener: advertising.AdLoadListener = {
5. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
6. hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
7. },
8. onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
9. hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
10. }
11. }
```

## MultiSlotsAdLoadListener

PhonePC/2in1Tablet

多广告位广告请求回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

### onAdLoadFailure

PhonePC/2in1Tablet

onAdLoadFailure(errorCode: number, errorMsg: string): void

多广告位广告请求失败回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

| 名称 | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| errorCode | number | 是 | 广告请求失败的错误码。 |
| errorMsg | string | 是 | 广告请求失败的错误信息。 |

**示例：**

```
1. import { advertising } from '@kit.AdsKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const multiSlotsAdLoadListener: advertising.MultiSlotsAdLoadListener = {
5. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
6. hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
7. },
8. onAdLoadSuccess: (adsMap: Map<string, Array<advertising.Advertisement>>) => {
9. hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
10. }
11. }
```

### onAdLoadSuccess

PhonePC/2in1Tablet

onAdLoadSuccess(adsMap: Map<string, Array<Advertisement>>): void

多广告位广告请求成功后回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

| **参数名** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| adsMap | Map<string, Array<[Advertisement](js-apis-advertisement.md#advertisement)>> | 是 | 广告数据。 |

**示例：**

```
1. import { advertising } from '@kit.AdsKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const multiSlotsAdLoadListener: advertising.MultiSlotsAdLoadListener = {
5. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
6. hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
7. },
8. onAdLoadSuccess: (adsMap: Map<string, Array<advertising.Advertisement>>) => {
9. hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
10. }
11. }
```

## AdInteractionListener

PhonePC/2in1Tablet

广告状态变化回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

### onStatusChanged

PhonePC/2in1Tablet

onStatusChanged(status: string, ad: Advertisement, data: string)

广告状态回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| status | string | 是 | 广告展示状态。  - onAdLoad：广告加载成功。  - onAdFail：广告加载失败。  - onAdOpen：打开广告。  - onAdClick：点击广告。  - onAdClose：关闭广告。  - onMediaProgress：广告播放进度。  - onMediaStart：广告开始播放。  - onMediaPause：广告暂停播放。  - onMediaStop：广告停止播放。  - onMediaComplete：广告播放完成。  - onMediaCountDown：广告倒计时。  - onMediaError：广告播放失败。  - onLandscape：竖屏状态下点击全屏按钮。  - onPortrait：全屏状态下点击返回按钮。  - onBackClicked：点击返回按钮。 |
| ad | [Advertisement](js-apis-advertisement.md#advertisement) | 是 | 发生状态变化的广告内容。 |
| data | string | 是 | 扩展信息。  当status参数为onAdClose时，data值为关闭原因，关闭原因描述如下：  - adShowEnded：广告展示结束。  - adCloseBtnClicked：点击关闭按钮。  - adSkipBtnClicked：点击跳过。  - adFeedbackClosed：负反馈关闭。  - adBackgroundClosed：开屏切后台关闭。 |

**示例：**

```
1. import { advertising } from '@kit.AdsKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const adInteractionListener: advertising.AdInteractionListener = {
5. onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
6. switch (status) {
7. case 'onAdLoad':
8. hilog.info(0x0000, 'testTag', 'Status is onAdLoad');
9. break;
10. case 'onAdFail':
11. hilog.error(0x0000, 'testTag', 'Status is onAdFail');
12. break;
13. case 'onAdOpen':
14. hilog.info(0x0000, 'testTag', 'Status is onAdOpen');
15. break;
16. case 'onAdClick':
17. hilog.info(0x0000, 'testTag', 'Status is onAdClick');
18. break;
19. case 'onAdClose':
20. // data值为关闭原因
21. hilog.info(0x0000, 'testTag', `Status is onAdClose, Close Reason is ${data}`);
22. if (data === 'adShowEnded') {
23. // 关闭原因为广告展示结束，可根据实际场景添加处理逻辑
24. }
25. break;
26. case 'onMediaProgress':
27. hilog.info(0x0000, 'testTag', 'Status is onMediaProgress');
28. break;
29. case 'onMediaStart':
30. hilog.info(0x0000, 'testTag', 'Status is onMediaStart');
31. break;
32. case 'onMediaPause':
33. hilog.info(0x0000, 'testTag', 'Status is onMediaPause');
34. break;
35. case 'onMediaStop':
36. hilog.info(0x0000, 'testTag', 'Status is onMediaStop');
37. break;
38. case 'onMediaComplete':
39. hilog.info(0x0000, 'testTag', 'Status is onMediaComplete');
40. break;
41. case 'onMediaCountDown':
42. hilog.info(0x0000, 'testTag', 'Status is onMediaCountDown');
43. break;
44. case 'onMediaError':
45. hilog.info(0x0000, 'testTag', 'Status is onMediaError');
46. break;
47. case 'onLandscape':
48. hilog.info(0x0000, 'testTag', 'Status is onLandscape');
49. break;
50. case 'onPortrait':
51. hilog.info(0x0000, 'testTag', 'Status is onPortrait');
52. break;
53. case 'onBackClicked':
54. hilog.info(0x0000, 'testTag', 'Status is onBackClicked');
55. break;
56. default:
57. break;
58. }
59. }
60. }
```

## AdOptions

PhonePC/2in1Tablet

广告配置参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagForChildProtection | number | 否 | 是否希望根据 COPPA 的规定将您的内容视为面向儿童的内容。  -1：默认值，不确定。  0：不希望。  1：希望。  默认为-1。 |
| adContentClassification | string | 否 | 设置广告内容分级上限。  W：3+，所有受众。  PI：7+，家长指导。  J：12+，青少年。  A：16+/18+，成人受众。  不填以业务逻辑为准。 |
| nonPersonalizedAd | number | 否 | 设置是否只请求非个性化广告。  0：请求个性化广告与非个性化广告。  1：只请求非个性化广告。  不填以业务逻辑为准。 |
| [key: string] | number | boolean | string | undefined | 否 | 自定义参数。  - totalDuration：类型number，单位：s。贴片广告必填自定义参数，用于设置贴片广告展示时长。  - allowMobileTraffic：类型number。可选自定义参数，设置是否允许使用流量下载广告素材。0：不允许，1：允许，不设置以广告主设置为准。  - tagForUnderAgeOfPromise：类型number。可选自定义参数，设置未成年保护标签。是否希望按适合未达到法定承诺年龄的欧洲经济区 (EEA) 用户的方式处理该广告请求。-1：默认值，不确定， 0：不希望 ， 1：希望。 |

## AdRequestParams

PhonePC/2in1Tablet

广告请求参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| adId | string | 是 | 广告位ID。  说明：[getAdRequestBody](js-apis-advertising.md#advertisinggetadrequestbody12)接口可以不传该参数。 |
| adType | number | 否 | 请求的广告类型。  - 1：开屏广告。  - 3：原生广告。  - 7：激励广告。  - 8：横幅广告。  - 12：插屏广告。  - 60：贴片广告。  不填默认为原生广告类型。 |
| adCount | number | 否 | 请求的广告数量。不填以业务逻辑为准。 |
| adWidth | number | 否 | 请求广告时期望的创意宽度，单位vp（横幅广告必填）。不填以业务逻辑为准。 |
| adHeight | number | 否 | 请求广告时期望的创意高度，单位vp（横幅广告必填）。不填以业务逻辑为准。 |
| adSearchKeyword | string | 否 | 广告关键字。不填默认""。  说明：暂不支持使用。 |
| [key: string] | number | boolean | string | undefined | 否 | 自定义参数。  - isPreload：类型boolean，请求贴片广告时，用于区分普通在线请求和素材预加载请求。true：素材预加载请求，false：普通在线请求。默认值false。仅对贴片广告生效，其他广告请求不解析该参数。  - enableDirectReturnVideoAd：类型boolean，原生广告自定义扩展参数，是否直接返回广告，不用等待所有广告素材下载完成。true：不等待广告素材下载完成，展示广告时在线加载素材；false：等待广告素材下载完成，展示广告时从本地缓存中加载素材。如果不填以云侧配置为准。仅对原生广告生效，其他广告请求不解析该参数。  - oaid: 类型string，开放匿名设备标识符，用于精准推送广告。不填无法获取到个性化广告。默认值为""。  - tMax：类型number，交易的最大超时时间（包含网络延迟）单位ms。  - cur：类型string，竞价请求支持的币种，支持传多个，用英文逗号分隔。当前支持五种货币：CNY（单位：元）、USD（单位：美元）、EUR（单位：欧元）、GBP（单位：英镑）、JPY（单位：日元），不填则默认是CNY。  - bidFloor：类型number，实时竞价广告位的底价。  - bidFloorCur：类型string，广告位底价使用的币种。如果bidFloor非空，则bidFloorCur也非空。当前只支持五种货币中的一种：CNY（单位：元）、USD（单位：美元）、EUR（单位：欧元）、GBP（单位：英镑）、JPY（单位：日元），不填则默认是CNY。  - bpkgName：类型string，广告位禁投的APP包名，支持传多个，用英文逗号分隔。  - orientation ：类型number，媒体请求广告的屏幕方向。1表示竖屏，0表示横屏，不设置则默认为1。当前未上架横屏开屏素材，若设置请求屏幕方向为横屏则不展示开屏广告。如果媒体设置应用固定横屏展示，但该参数未设置或者设置为1，则展示效果会受影响。 |

## AdDisplayOptions

PhonePC/2in1Tablet

广告展示参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| customData | string | 否 | 媒体自定义数据。用于服务端通知媒体服务器某位用户因为与激励视频广告互动而应予以奖励，从而规避欺骗的行为（不填则不会通知）。 |
| userId | string | 否 | 媒体自定义用户id。用于服务端通知媒体服务器某位用户因为与激励视频广告互动而应予以奖励，从而规避欺骗的行为（不填则不会通知）。 |
| useMobileDataReminder | boolean | 否 | 使用移动数据播放视频或下载应用时是否弹框通知用户。  - true：弹框通知。  - false：不弹框通知。  - 该参数依赖流量弹窗功能，当前不支持完整功能的使用，暂不确定默认值。 |
| mute | boolean | 否 | 广告视频播放是否静音。  - true：静音播放。  - false：非静音播放。  不填以业务逻辑为准。 |
| audioFocusType | number | 否 | 视频播放过程中获得音频焦点的场景类型。  - 0：视频播放静音、非静音时都获取焦点。  - 1：视频静音播放时不获取焦点。  - 2：视频播放静音、非静音时都不获取焦点。  - 该接口依赖的相关功能当前不支持使用，暂不确定默认值。 |
| [key: string] | number | boolean | string | undefined | 否 | 自定义参数。  - refreshTime：类型number，单位：ms，取值范围[30000, 120000]。AutoAdComponent组件可选自定义参数，用于控制广告的轮播时间间隔。填写了该参数，则广告按照参数配置的时间间隔轮播，否则广告不会轮播，只会展示广告响应中的第一个广告内容。 |
