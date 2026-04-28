---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-productviewmanager
title: productViewManager (应用市场推荐)
breadcrumb: API参考 > 应用服务 > AppGallery Kit（应用市场服务） > ArkTS API > productViewManager (应用市场推荐)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1a4ba1f8225e219ad5fde6e9a36e1c186331f5e1fe5adc2bce0b5fa439da42f5
---

提供展示应用/元服务详情页、应用内快捷方式加桌的能力。

说明

调用接口需捕获异常。

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { productViewManager } from '@kit.AppGalleryKit';
```

## ProductViewCallback

PhonePC/2in1TabletTV

在加载应用详情页面时作为入参用于接收加载过程中的状态变化。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onError | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 是 | 回调函数，接收应用详情页加载失败的错误码。  1011表示拉起/切前台失败。  1012表示切后台失败。  1013表示销毁失败。 |
| onAppear | Callback<void> | 否 | 是 | 回调函数，当应用详情页成功打开时回调该方法。  **起始版本：** 5.0.2(14) |
| onDisappear | Callback<void> | 否 | 是 | 回调函数，当应用详情页关闭时回调该方法。  **起始版本：** 5.0.2(14) |

## ServiceViewCallback

PhonePC/2in1TabletTV

在加载元服务卡片加桌页面时作为入参用于接收加载过程中的状态变化。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onReceive | Callback<[ServiceViewReceiveData](store-productviewmanager.md#serviceviewreceivedata)> | 否 | 是 | 当打开元服务卡片加桌页成功，点击加桌，收到加桌结果。 |
| onError | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 是 | 回调函数，接收元服务卡片加桌页加载失败的错误码。  1011表示拉起/切前台失败。  1012表示切后台失败。  1013表示销毁失败。 |
| onAppear | Callback<void> | 否 | 是 | 回调函数，当元服务卡片加桌页成功打开时回调该方法。  **起始版本：** 5.0.2(14) |
| onDisappear | Callback<void> | 否 | 是 | 回调函数，当元服务卡片加桌页关闭时回调该方法。  **起始版本：** 5.0.2(14) |

## ServiceViewReceiveData

PhonePC/2in1TabletTV

元服务加桌回调数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | [ReceiveDataResult](store-productviewmanager.md#receivedataresult) | 是 | 否 | 加桌结果。 |
| msg | string | 是 | 否 | 加桌结果描述信息。 |
| formInfo | {[key: string]: Object;} | 是 | 否 | 加桌卡片数据。有以下必填属性：  - bundleName表示元服务包名。  - name表示卡片名称。  - abilityName表示ability名称。  - moduleName表示元服务模块名。  - defaultDimension表示卡片尺寸。 |

## ReceiveDataResult

PhonePC/2in1TabletTV

元服务加桌结果码类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 1000 | 成功。 |
| FAILURE | 1001 | 失败。 |
| EXCEPTION | 1002 | 异常。 |

## CheckShortcutResult

PhonePC/2in1TabletTV

快捷方式校验结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tid | string | 否 | 是 | 基于应用的快捷方式信息生成的Transaction ID。若快捷方式信息发生变化，则每次覆盖生成新的tid，否则返回历史tid以及剩余过期时间expired。 |
| expired | number | 否 | 是 | Transaction ID的过期时间，单位是ms。 |
| code | number | 否 | 否 | 校验的结果码，0表示校验成功，否则具体的失败原因，可以参考[ArkTS API错误码](store-error-code.md)。 |
| limit | number | 否 | 是 | 允许应用添加快捷方式的数量。 |

## SKExposure

PhonePC/2in1TabletTV

登记归因来源的广告曝光数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| adTechId | string | 否 | 否 | 分发平台对应的归因角色ID，本次登记归因来源对应营销任务所归属的分发平台的标识符。  分发平台向应用归因云侧[注册归因角色](../harmonyos-guides/store-attribution-register.md#注册归因角色)时，由应用归因服务分配，长度固定为8个字符。 |
| campaignId | string | 否 | 否 | 营销任务ID，登记归因来源对应的营销任务的ID，长度不超过6个字符。  **说明：** 从6.0.2(22)开始，该接口支持长度由不超过6个字符变为不超过9个字符。 |
| destinationId | string | 否 | 否 | 应用上架华为应用市场的AppId，长度不超过64个字符。  **说明：** 您的应用ID参考[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)获取。 |
| mmpIds | string[] | 否 | 是 | 本次广告投放，使用的归因监测平台对应的归因角色ID。最大数量2个，每个ID字符串长度固定为8个字符。  如果调用方传递了归因监测平台ID，应用归因服务会向归因监测平台回传归因结果；如果调用方没有传递监测平台ID，则归因监测平台收不到回传的归因结果。 |
| serviceTag | string | 否 | 是 | 分发平台关注的业务信息，如创意、素材等，长度不超过32个字符。  如果调用方传递了serviceTag，在[申请开通权限](../harmonyos-guides/store-attribution-register.md#开通权限)后应用归因服务会将serviceTag回传分发平台。 |
| nonce | string | 否 | 否 | 用于计算签名的随机数，不带'-'，每次广告请求，nonce唯一。长度固定为32个字符。  同一个adTechId，同一个nonce最多可以登记5次曝光，5次点击类型的归因来源信息。 |
| timestamp | number | 否 | 否 | unix时间戳，单位：毫秒，请求广告的时间戳。（即广告投放时间，登记归因来源时，要求广告时间与当前时间偏差不超过10分钟） |
| signature | string | 否 | 否 | 签名值，分发平台/媒体根据广告相应信息按照[归因来源签名计算规则](../harmonyos-guides/appgallery-attribution-appendix-triger.md#归因来源签名计算规则)计算生成签名并提供，长度不超过800个字符。 |

**示例：**

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { productViewManager } from '@kit.AppGalleryKit';

6. const TAG: string = 'LoadProduct';

8. @Entry
9. @Component
10. struct LoadProduct {
11. build() {
12. Column() {
13. Button("load_product")
14. .onClick(() => {
15. try {
16. // 登记归因来源的广告曝光数据
17. const exposureData: productViewManager.SKExposure = {
18. // 在应用归因云侧注册广告生态伙伴角色时，由应用归因服务分配
19. adTechId: '20****e8',
20. // 分发平台创建的营销任务id
21. campaignId: '123456',
22. // 开发者应用上架华为应用市场的appId，不带C
23. destinationId: '10******',
24. // 归因监测平台id
25. mmpIds: ['2f****5', '2f7***5'],
26. // 分发平台关注的业务信息
27. serviceTag: '123***2',
28. // 用于计算签名的随机数，不带'-'
29. nonce: '123***2',
30. // 时间戳
31. timestamp: 1705536488,
32. // 签名值
33. signature: 'MEQCIEQlmZ****zKBSE8QnhLTIHZZZ****ZpRqRxHss65Ko****JgJKjdrWdkL****juEx2RmFS7da****ZRVZ8RyMyUXg=='
34. };

36. const request: Want = {
37. parameters: {
38. bundleName: 'com.huawei.hmsapp.books',
39. skExposure: exposureData
40. }
41. };
42. // 展示应用详情页，下载安装目标应用
43. productViewManager.loadProduct(this.getUIContext().getHostContext() as common.UIAbilityContext, request, {
44. onError: (error: BusinessError) => {
45. hilog.error(0, TAG, `loadProduct onError.code is ${error.code}, message is ${error.message}`);
46. }
47. });
48. } catch (err) {
49. hilog.error(0, TAG, `loadProduct failed.code is ${err.code}, message is ${err.message}`);
50. }
51. })
52. .width('100%')
53. }
54. .margin(16)
55. .height('100%')
56. .justifyContent(FlexAlign.Center)
57. }
58. }
```

## productViewManager.loadProduct

PhonePC/2in1TabletTV

loadProduct(context: common.UIAbilityContext, want: Want, callback?: ProductViewCallback): void

展示应用详情页，下载安装目标应用。使用Callback回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**设备行为差异：** 对于6.0.1(21)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中返回401错误码。对于6.0.2(22)及之后版本，该接口在Phone、Tablet、PC/2in1、TV中均可正常使用，在其他设备类型中返回401错误码。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 调用方应用的上下文。 |
| want | [Want](js-apis-app-ability-want.md) | 是 | 展示应用详情页的请求参数。parameters 是该参数中的必填属性，为一个结构体。  该结构体包含两个属性：  - bundleName，必填，表示需要展示详情页的应用包名。  - skExposure，可选，表示需要传递登记归因来源的广告曝光数据。具体参考示例代码。 |
| callback | [ProductViewCallback](store-productviewmanager.md#productviewcallback) | 否 | 在加载应用详情页面时作为入参用于接收加载过程中的状态变化。若不填此参数，当加载应用详情页失败时，无法获取失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { productViewManager } from '@kit.AppGalleryKit';

6. const TAG: string = 'LoadProduct';

8. @Entry
9. @Component
10. struct LoadProduct {
11. build() {
12. Column() {
13. Button("load_product")
14. .onClick(() => {
15. try {
16. const request: Want = {
17. parameters: {
18. // 此处填入要加载的应用包名，例如： bundleName: "com.huawei.hmsapp.appgallery"
19. bundleName: 'com.xxx'
20. }
21. };
22. productViewManager.loadProduct(this.getUIContext().getHostContext() as common.UIAbilityContext, request, {
23. onError: (error: BusinessError) => {
24. hilog.error(0, TAG, `loadProduct onError.code is ${error.code}, message is ${error.message}`);
25. },
26. onAppear: () => {
27. hilog.info(0, TAG, `loadProduct onAppear.`);
28. },
29. onDisappear: () => {
30. hilog.info(0, TAG, `loadProduct onDisappear.`);
31. }
32. });
33. } catch (err) {
34. hilog.error(0, TAG, `loadProduct failed.code is ${err.code}, message is ${err.message}`);
35. }
36. })
37. .width('100%')
38. }
39. .margin(16)
40. .height('100%')
41. .justifyContent(FlexAlign.Center)
42. }
43. }
```

## productViewManager.loadService

PhonePC/2in1TabletTV

loadService(context: common.UIAbilityContext, want: Want, callback?: ServiceViewCallback): void

展示元服务详情页，添加至桌面。使用Callback回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**设备行为差异：** 对于6.0.1(21)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中返回401错误码。对于6.0.2(22)及之后版本，该接口在Phone、Tablet、PC/2in1中可正常使用，TV中无响应，在其他设备类型中返回401错误码。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 调用方应用的上下文。 |
| want | [Want](js-apis-app-ability-want.md) | 是 | 加载元服务详情页面接口的请求参数。uri为必填参数，其值为元服务加桌链接。具体可参考下文中的示例代码。 |
| callback | [ServiceViewCallback](store-productviewmanager.md#serviceviewcallback) | 否 | 在加载元服务详情页面时作为入参用于接收加载过程中的状态变化。若不填此参数，当加载元服务详情页失败时，无法返回失败的错误码；当加载元服务详情页成功时，点击加桌，无法获取加桌结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { productViewManager } from '@kit.AppGalleryKit';

6. const TAG: string = 'LoadService';

8. @Entry
9. @Component
10. struct LoadService {

12. build() {
13. Column() {
14. Button("load_service")
15. .onClick(() => {
16. try {
17. const request: Want = {
18. // 请输入元服务的加桌链接
19. uri: 'store://appgallery.huawei.com/oper/addhome?referrer=xxxx&id=xxxx&installType=xxxx&s=xxxx'
20. };
21. productViewManager.loadService(this.getUIContext().getHostContext() as common.UIAbilityContext, request, {
22. onReceive: (data: productViewManager.ServiceViewReceiveData) => {
23. hilog.info(0, TAG, `Succeeded in loading Service onReceive.result is ${data.result}, msg is ${data.msg}`);
24. },
25. onError: (error: BusinessError) => {
26. hilog.error(0, TAG, `loadService onError.code is ${error.code}, message is ${error.message}`)
27. },
28. onAppear: () => {
29. hilog.info(0, TAG, `loadService onAppear.`);
30. },
31. onDisappear: () => {
32. hilog.info(0, TAG, `loadService onDisappear.`);
33. }
34. });
35. } catch (err) {
36. hilog.error(0, TAG, `loadService failed.code is ${err.code}, message is ${err.message}`);
37. }
38. })
39. .width('100%')
40. }
41. .margin(16)
42. .height('100%')
43. .justifyContent(FlexAlign.Center)
44. }
45. }
```

## productViewManager.checkPinShortcutPermitted

PhonePC/2in1TabletTV

checkPinShortcutPermitted(context: common.UIAbilityContext, shortcutId: string, want: Want, labelResName: string, iconResName: string): Promise<CheckShortcutResult>

以静态资源方式校验快捷方式是否允许加桌，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**设备行为差异：** 对于6.0.1(21)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中返回401错误码。对于6.0.2(22)及之后版本，该接口在Phone、Tablet、PC/2in1中可正常使用，TV中返回1006620001错误码，在其他设备类型中返回401错误码。

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 调用方应用的上下文。 |
| shortcutId | string | 是 | 快捷方式ID，取值为长度不超过63字节的字符串。 |
| want | [Want](js-apis-app-ability-want.md) | 是 | 点击快捷方式后被拉起方的want信息。 |
| labelResName | string | 是 | 快捷方式显示在桌面名称的label资源索引名称。 |
| iconResName | string | 是 | 快捷方式显示在桌面图标的icon资源索引名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CheckShortcutResult](store-productviewmanager.md#checkshortcutresult)> | Promise对象，返回快捷方式校验结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006620001 | System internal error. |
| 1006620002 | Request to service error. |
| 1006620003 | Shortcut id already exists. |
| 1006620004 | The number of shortcuts has reached the maximum. |
| 1006620005 | Shortcut verification failed. |

**示例：**

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { productViewManager } from '@kit.AppGalleryKit';

6. const TAG: string = 'CheckPinShortcutPermitted';

8. @Entry
9. @Component
10. struct CheckPinShortcutPermitted {

12. build() {
13. Column() {
14. Button("checkPinShortcutPermitted")
15. .onClick(() => {
16. try {
17. const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
18. const shortcutId = "id_test1"; // 对应shortcuts标签中配置的shortcutId, 例如: "shortcutId": "id_test1"
19. const labelResName = "shortcut"; // 对应shortcuts标签中配置的label资源索引名称, 例如: "label": "$string:shortcut"
20. const iconResName = "aa_icon"; // 对应shortcuts标签中配置的icon资源索引名称, 例如: "icon": "$media:aa_icon"
21. const want: Want = {
22. bundleName: "com.example.appgallery.kit.demo",
23. moduleName: "entry",
24. abilityName: "EntryAbility",
25. parameters: {
26. testKey: "testValue"
27. }
28. };
29. // 以静态资源方式校验快捷方式是否允许加桌,并返回快捷方式校验结果
30. productViewManager.checkPinShortcutPermitted(uiContext, shortcutId, want, labelResName, iconResName)
31. .then((result: productViewManager.CheckShortcutResult) => {
32. hilog.info(0x0001, TAG, `checkPinShortcutPermitted success result is ${JSON.stringify(result)}`);
33. }).catch((error: BusinessError) => {
34. hilog.error(0x0001, TAG, `checkPinShortcutPermitted error. code is ${error.code}, message is ${error.message}`);
35. })
36. } catch (err) {
37. hilog.error(0x0001, TAG, `checkPinShortcutPermitted failed, code is ${err.code}, message is ${err.message}`);
38. }
39. })
40. .width('100%')
41. }
42. .margin(16)
43. .height('100%')
44. .justifyContent(FlexAlign.Center)
45. }
46. }
```

## productViewManager.checkPinShortcutPermitted

PhonePC/2in1TabletTV

checkPinShortcutPermitted(context: common.UIAbilityContext, shortcutId: string, want: Want, label: string, foregroundIcon: string, backgroundIcon: string): Promise<CheckShortcutResult>

以自定义资源方式校验快捷方式是否允许加桌，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**设备行为差异：** 对于6.0.1(21)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中返回401错误码。对于6.0.2(22)及之后版本，该接口在Phone、Tablet、PC/2in1中可正常使用，TV中返回1006620001错误码，在其他设备类型中返回401错误码。

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 上下文。 |
| shortcutId | string | 是 | 快捷方式ID，取值为长度不超过63字节的字符串。 |
| want | [Want](js-apis-app-ability-want.md) | 是 | 点击快捷方式后被拉起方的want信息。 |
| label | string | 是 | 快捷方式显示在桌面名称的文本，长度不超过255个字符。 |
| foregroundIcon | string | 是 | 快捷方式显示在桌面图标的沙箱地址，图标最大不超过100KB，格式为png和webp。 |
| backgroundIcon | string | 是 | 预留字段，目前只支持传入空字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CheckShortcutResult](store-productviewmanager.md#checkshortcutresult)> | Promise对象，返回快捷方式校验结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006620001 | System internal error. |
| 1006620002 | Request to service error. |
| 1006620003 | Shortcut id already exists. |
| 1006620004 | The number of shortcuts has reached the maximum. |
| 1006620005 | Shortcut verification failed. |

**示例：**

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { productViewManager } from '@kit.AppGalleryKit';

6. const TAG: string = 'CheckPinShortcutPermitted';

8. @Entry
9. @Component
10. struct CheckPinShortcutPermitted {

12. build() {
13. Column() {
14. Button("checkPinShortcutPermitted")
15. .onClick(() => {
16. try {
17. const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
18. const shortcutId = `shortcutId_1`;
19. const want: Want = {
20. bundleName: "com.example.appgallery.kit.demo",
21. moduleName: "entry",
22. abilityName: "EntryAbility",
23. parameters: {
24. testKey: "testValue"
25. }
26. }
27. const label = "shortcut";
28. const foregroundIcon = uiContext.filesDir + "/icon.png";
29. const backgroundIcon = "";
30. // 以自定义资源方式校验快捷方式是否允许加桌,返回快捷方式校验结果
31. productViewManager.checkPinShortcutPermitted(uiContext, shortcutId, want, label, foregroundIcon, backgroundIcon)
32. .then((result: productViewManager.CheckShortcutResult) => {
33. hilog.info(0x0001, TAG, `checkPinShortcutPermitted success result is ${JSON.stringify(result)}`);
34. }).catch((error: BusinessError) => {
35. hilog.error(0x0001, TAG, `checkPinShortcutPermitted error. code is ${error.code}, message is ${error.message}`);
36. })
37. } catch (err) {
38. hilog.error(0x0001, TAG, `checkPinShortcutPermitted failed, code is ${err.code}, message is ${err.message}`);
39. }
40. })
41. .width('100%')
42. }
43. .margin(16)
44. .height('100%')
45. .justifyContent(FlexAlign.Center)
46. }
47. }
```

## productViewManager.requestNewPinShortcut

PhonePC/2in1TabletTV

requestNewPinShortcut(context: common.UIAbilityContext, tid: string): Promise<void>

创建快捷方式加桌，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**设备行为差异：** 对于6.0.1(21)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中返回401错误码。对于6.0.2(22)及之后版本，该接口在Phone、Tablet、PC/2in1中可正常使用，TV中无响应，在其他设备类型中返回401错误码。

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 上下文。 |
| tid | string | 是 | 快捷方式校验结果[CheckShortcutResult](store-productviewmanager.md#checkshortcutresult)返回的tid。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006620001 | System internal error. |
| 1006620003 | Shortcut id already exists. |
| 1006620004 | The number of shortcuts has reached the maximum. |
| 1006620005 | Shortcut verification failed. |
| 1006620006 | The shortcut is not verified or has expired. |
| 1006620007 | User refused to add shortcut. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { productViewManager } from '@kit.AppGalleryKit';

6. const TAG: string = 'RequestNewPinShortcut';

8. @Entry
9. @Component
10. struct RequestNewPinShortcut {

12. build() {
13. Column() {
14. Button("RequestNewPinShortcut")
15. .onClick(() => {
16. try {
17. const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
18. const tid = 'xxx'; // 通过checkPinShortcutPermitted接口获取
19. productViewManager.requestNewPinShortcut(uiContext, tid)
20. .then(() => {
21. hilog.info(0x0001, TAG, `requestNewPinShortcut success.`);
22. }).catch((error: BusinessError) => {
23. hilog.error(0x0001, TAG, `requestNewPinShortcut error. code is ${error.code}, message is ${error.message}`);
24. })
25. } catch (err) {
26. hilog.error(0x0001, TAG, `requestNewPinShortcut failed, code is ${err.code}, message is ${err.message}`);
27. }
28. })
29. .width('100%')
30. }
31. .margin(16)
32. .height('100%')
33. .justifyContent(FlexAlign.Center)
34. }
35. }
```
