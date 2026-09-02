---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-productviewmanager
title: productViewManager (应用市场推荐)
breadcrumb: API参考 > 应用服务 > AppGallery Kit（应用市场服务） > ArkTS API > productViewManager (应用市场推荐)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e4c1a772288a126002b9edb39fa5e5df55942c246bf339ab0870ca01c9fce121
---

提供展示应用详情页、添加元服务卡片至桌面，以及添加、查询和删除桌面快捷方式的能力。

**说明** 

调用接口需捕获异常。

**起始版本：** 4.1.0(11)

## 导入模块

```typescript
import { productViewManager } from '@kit.AppGalleryKit';
```

## ProductViewCallback

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

在加载元服务卡片添加至桌面页时作为入参用于接收加载过程中的状态变化。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onReceive | Callback<[ServiceViewReceiveData](store-productviewmanager.md#serviceviewreceivedata)> | 否 | 是 | 回调函数，当元服务卡片加载成功并添加至桌面时调用，获取元服务卡片加载成功并添加至桌面后的相关信息和结果。 |
| onError | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 是 | 回调函数，接收元服务卡片添加至桌面页加载失败的错误码。  1011表示拉起/切前台失败。  1012表示切后台失败。  1013表示销毁失败。 |
| onAppear | Callback<void> | 否 | 是 | 回调函数，当元服务卡片添加至桌面页成功打开时回调该方法。  **起始版本：** 5.0.2(14) |
| onDisappear | Callback<void> | 否 | 是 | 回调函数，当元服务卡片添加至桌面页关闭时回调该方法。  **起始版本：** 5.0.2(14) |

## ServiceViewReceiveData

元服务卡片添加至桌面的回调数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | [ReceiveDataResult](store-productviewmanager.md#receivedataresult) | 是 | 否 | 元服务卡片添加至桌面结果。 |
| msg | string | 是 | 否 | 元服务卡片添加至桌面结果描述信息。 |
| formInfo | {[key: string]: Object;} | 是 | 否 | 添加至桌面的元服务卡片数据。有以下必填属性：  - bundleName表示元服务包名。  - name表示卡片名称。  - abilityName表示ability名称。  - moduleName表示元服务模块名。  - defaultDimension表示卡片尺寸。 |

## ReceiveDataResult

元服务卡片添加至桌面结果码类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 1000 | 成功。 |
| FAILURE | 1001 | 失败。 |
| EXCEPTION | 1002 | 异常。 |

## CheckShortcutResult

快捷方式校验结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tid | string | 否 | 是 | 基于应用的快捷方式信息生成的Transaction ID。若快捷方式信息发生变化，则每次覆盖生成新的tid，否则返回历史tid以及剩余过期时间expired。 |
| expired | number | 否 | 是 | Transaction ID的过期时间，单位是ms。 |
| code | number | 否 | 否 | 校验的结果码，0表示校验成功，否则具体的失败原因，可以参考[ArkTS API错误码](errorcode-appgallery.md)。 |
| limit | number | 否 | 是 | 允许应用添加快捷方式的数量。 |

## SKExposure

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

```typescript
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { productViewManager } from '@kit.AppGalleryKit';

const TAG: string = 'LoadProduct';

@Entry
@Component
struct LoadProduct {
  build() {
    Column() {
      Button("load_product")
        .onClick(() => {
          try {
            // 登记归因来源的广告曝光数据
            const exposureData: productViewManager.SKExposure = {
              // 在应用归因云侧注册广告生态伙伴角色时，由应用归因服务分配
              adTechId: '20****e8',
              // 分发平台创建的营销任务id
              campaignId: '123456',
              // 开发者应用上架华为应用市场的appId，不带C
              destinationId: '10******',
              // 归因监测平台id
              mmpIds: ['2f****5', '2f7***5'],
              // 分发平台关注的业务信息
              serviceTag: '123***2',
              // 用于计算签名的随机数，不带'-'
              nonce: '123***2',
              // 时间戳
              timestamp: 1705536488,
              // 签名值
              signature: 'MEQCIEQlmZ****zKBSE8QnhLTIHZZZ****ZpRqRxHss65Ko****JgJKjdrWdkL****juEx2RmFS7da****ZRVZ8RyMyUXg=='
            };

            const want: Want = {
              parameters: {
                bundleName: 'com.huawei.hmsapp.books',
                skExposure: exposureData
              }
            };
            // 展示应用详情页，下载安装目标应用
            productViewManager.loadProduct(this.getUIContext().getHostContext() as common.UIAbilityContext, want, {
              onError: (error: BusinessError) => {
                hilog.error(0, TAG, `loadProduct onError.code is ${error.code}, message is ${error.message}`);
              }
            });
          } catch (err) {
            hilog.error(0, TAG, `loadProduct failed.code is ${err.code}, message is ${err.message}`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## PinShortcutInfo

桌面快捷方式信息列表。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**起始版本：** 6.1.1(24)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| shortcutId | string | 否 | 否 | 桌面快捷方式的ID。 |
| icon | string | 否 | 是 | 桌面快捷方式的图标。 |
| iconId | number | 否 | 是 | 桌面快捷方式图标的资源ID。 |
| label | string | 否 | 是 | 桌面快捷方式的标签信息。 |
| labelId | number | 否 | 是 | 桌面快捷方式标签信息为资源索引时的资源ID。 |
| want | [Want](js-apis-app-ability-want.md) | 否 | 是 | 桌面快捷方式内定义的目标want信息。 |

## productViewManager.loadProduct

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

```typescript
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { productViewManager } from '@kit.AppGalleryKit';

const TAG: string = 'LoadProduct';

@Entry
@Component
struct LoadProduct {
  build() {
    Column() {
      Button("load_product")
        .onClick(() => {
          try {
            const want: Want = {
              parameters: {
                // 此处填入要加载的应用包名，例如： bundleName: "com.huawei.hmsapp.appgallery"
                bundleName: 'com.xxx'
              }
            };
            productViewManager.loadProduct(this.getUIContext().getHostContext() as common.UIAbilityContext, want, {
              onError: (error: BusinessError) => {
                hilog.error(0, TAG, `loadProduct onError.code is ${error.code}, message is ${error.message}`);
              },
              onAppear: () => {
                hilog.info(0, TAG, `loadProduct onAppear.`);
              },
              onDisappear: () => {
                hilog.info(0, TAG, `loadProduct onDisappear.`);
              }
            });
          } catch (err) {
            hilog.error(0, TAG, `loadProduct failed.code is ${err.code}, message is ${err.message}`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## productViewManager.loadService

loadService(context: common.UIAbilityContext, want: Want, callback?: ServiceViewCallback): void

添加元服务卡片至桌面。使用Callback回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**设备行为差异：** 对于6.0.1(21)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中返回401错误码。对于6.0.2(22)及之后版本，该接口在Phone、Tablet、PC/2in1中可正常使用，TV中无响应，在其他设备类型中返回401错误码。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 调用方应用的上下文。 |
| want | [Want](js-apis-app-ability-want.md) | 是 | 加载元服务卡片添加至桌面页面接口的请求参数。uri为必填参数，其值为元服务卡片添加至桌面页链接。具体可参考下文中的示例代码。 |
| callback | [ServiceViewCallback](store-productviewmanager.md#serviceviewcallback) | 否 | 在加载元服务卡片添加至桌面页面时作为入参用于接收加载过程中的状态变化。若不填此参数，当加载元服务卡片添加至桌面页失败时，无法返回失败的错误码；当加载元服务卡片添加至桌面页成功时，点击添加至桌面，无法获取元服务卡片添加至桌面结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```typescript
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { productViewManager } from '@kit.AppGalleryKit';

const TAG: string = 'LoadService';

@Entry
@Component
struct LoadService {

  build() {
    Column() {
      Button("load_service")
        .onClick(() => {
          try {
            const want: Want = {
              // 请输入元服务卡片添加至桌面的链接
              uri: 'store://appgallery.huawei.com/oper/addhome?referrer=xxxx&id=xxxx&installType=xxxx&s=xxxx'
            };
            productViewManager.loadService(this.getUIContext().getHostContext() as common.UIAbilityContext, want, {
              onReceive: (data: productViewManager.ServiceViewReceiveData) => {
                hilog.info(0, TAG, `Succeeded in loading Service onReceive.result is ${data.result}, msg is ${data.msg}`);
              },
              onError: (error: BusinessError) => {
                hilog.error(0, TAG, `loadService onError.code is ${error.code}, message is ${error.message}`)
              },
              onAppear: () => {
                hilog.info(0, TAG, `loadService onAppear.`);
              },
              onDisappear: () => {
                hilog.info(0, TAG, `loadService onDisappear.`);
              }
            });
          } catch (err) {
            hilog.error(0, TAG, `loadService failed.code is ${err.code}, message is ${err.message}`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## productViewManager.checkPinShortcutPermitted

checkPinShortcutPermitted(context: common.UIAbilityContext, shortcutId: string, want: Want, labelResName: string, iconResName: string): Promise<CheckShortcutResult>

校验是否允许以静态资源方式在桌面创建快捷方式。使用Promise异步回调。

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

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-appgallery.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006620001 | System internal error. |
| 1006620002 | Request to service error. |
| 1006620003 | Shortcut id already exists. |
| 1006620004 | The number of shortcuts has reached the maximum. |
| 1006620005 | Shortcut verification failed. |

**示例：**

```typescript
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { productViewManager } from '@kit.AppGalleryKit';

const TAG: string = 'CheckPinShortcutPermitted';

@Entry
@Component
struct CheckPinShortcutPermitted {

  build() {
    Column() {
      Button("checkPinShortcutPermitted")
        .onClick(() => {
          try {
            const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
            const shortcutId = "id_test1"; // 对应shortcuts标签中配置的shortcutId, 例如: "shortcutId": "id_test1"
            const labelResName = "shortcut"; // 对应shortcuts标签中配置的label资源索引名称, 例如: "label": "$string:shortcut"
            const iconResName = "aa_icon"; // 对应shortcuts标签中配置的icon资源索引名称, 例如: "icon": "$media:aa_icon"
            const want: Want = {
              bundleName: "com.example.appgallery.kit.demo",
              moduleName: "entry",
              abilityName: "EntryAbility",
              parameters: {
                testKey: "testValue"
              }
            };
            // 校验是否允许以静态资源方式在桌面创建快捷方式，并返回快捷方式校验结果
            productViewManager.checkPinShortcutPermitted(uiContext, shortcutId, want, labelResName, iconResName)
              .then((result: productViewManager.CheckShortcutResult) => {
                hilog.info(0x0001, TAG, `checkPinShortcutPermitted success result is ${JSON.stringify(result)}`);
              }).catch((error: BusinessError) => {
              hilog.error(0x0001, TAG, `checkPinShortcutPermitted error. code is ${error.code}, message is ${error.message}`);
            })
          } catch (err) {
            hilog.error(0x0001, TAG, `checkPinShortcutPermitted failed, code is ${err.code}, message is ${err.message}`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## productViewManager.checkPinShortcutPermitted

checkPinShortcutPermitted(context: common.UIAbilityContext, shortcutId: string, want: Want, label: string, foregroundIcon: string, backgroundIcon: string): Promise<CheckShortcutResult>

校验是否允许以自定义资源方式在桌面创建快捷方式。使用Promise异步回调。

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

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-appgallery.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006620001 | System internal error. |
| 1006620002 | Request to service error. |
| 1006620003 | Shortcut id already exists. |
| 1006620004 | The number of shortcuts has reached the maximum. |
| 1006620005 | Shortcut verification failed. |

**示例：**

```typescript
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { productViewManager } from '@kit.AppGalleryKit';

const TAG: string = 'CheckPinShortcutPermitted';

@Entry
@Component
struct CheckPinShortcutPermitted {

  build() {
    Column() {
      Button("checkPinShortcutPermitted")
        .onClick(() => {
          try {
            const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
            const shortcutId = `shortcutId_1`;
            const want: Want = {
              bundleName: "com.example.appgallery.kit.demo",
              moduleName: "entry",
              abilityName: "EntryAbility",
              parameters: {
                testKey: "testValue"
              }
            }
            const label = "shortcut";
            const foregroundIcon = uiContext.filesDir + "/icon.png";
            const backgroundIcon = "";
            // 校验是否允许以自定义资源方式在桌面创建快捷方式，返回快捷方式校验结果
            productViewManager.checkPinShortcutPermitted(uiContext, shortcutId, want, label, foregroundIcon, backgroundIcon)
              .then((result: productViewManager.CheckShortcutResult) => {
                hilog.info(0x0001, TAG, `checkPinShortcutPermitted success result is ${JSON.stringify(result)}`);
              }).catch((error: BusinessError) => {
              hilog.error(0x0001, TAG, `checkPinShortcutPermitted error. code is ${error.code}, message is ${error.message}`);
            })
          } catch (err) {
            hilog.error(0x0001, TAG, `checkPinShortcutPermitted failed, code is ${err.code}, message is ${err.message}`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## productViewManager.requestNewPinShortcut

requestNewPinShortcut(context: common.UIAbilityContext, tid: string): Promise<void>

请求在桌面创建快捷方式。使用Promise异步回调。

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

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-appgallery.md)。

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

```typescript
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { productViewManager } from '@kit.AppGalleryKit';

const TAG: string = 'RequestNewPinShortcut';

@Entry
@Component
struct RequestNewPinShortcut {

  build() {
    Column() {
      Button("RequestNewPinShortcut")
        .onClick(() => {
          try {
            const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
            const tid = 'xxx'; // 通过checkPinShortcutPermitted接口获取
            productViewManager.requestNewPinShortcut(uiContext, tid)
              .then(() => {
                hilog.info(0x0001, TAG, `requestNewPinShortcut success.`);
              }).catch((error: BusinessError) => {
              hilog.error(0x0001, TAG, `requestNewPinShortcut error. code is ${error.code}, message is ${error.message}`);
            })
          } catch (err) {
            hilog.error(0x0001, TAG, `requestNewPinShortcut failed, code is ${err.code}, message is ${err.message}`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## productViewManager.getPinShortcutInfos

getPinShortcutInfos(): Promise<PinShortcutInfo[]>

查询桌面快捷方式信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**起始版本：** 6.1.1(24)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PinShortcutInfo](store-productviewmanager.md#pinshortcutinfo)[]> | Promise对象。返回查询桌面快捷方式信息列表的结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-appgallery.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1006620001 | System internal error. |
| 1006620002 | Request to service error. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { productViewManager } from '@kit.AppGalleryKit';

const TAG: string = 'GetPinShortcutInfos';

@Entry
@Component
struct GetPinShortcutInfos {

  build() {
    Column() {
      Button("GetPinShortcutInfos")
        .onClick(() => {
          try {
            // 通过getPinShortcutInfos接口获取桌面快捷方式列表信息
            productViewManager.getPinShortcutInfos()
              .then(() => {
                hilog.info(0x0001, TAG, `getPinShortcutInfos success.`);
              }).catch((error: BusinessError) => {
              hilog.error(0x0001, TAG, `getPinShortcutInfos error. code is ${error.code}, message is ${error.message}`);
            })
          } catch (err) {
            hilog.error(0x0001, TAG, `getPinShortcutInfos failed, code is ${err.code}, message is ${err.message}`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## productViewManager.removePinShortcut

removePinShortcut(context: common.UIAbilityContext, shortcutId: string): Promise<void>

删除桌面快捷方式。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Recommendations

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 上下文。 |
| shortcutId | string | 是 | 快捷方式ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-appgallery.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1006620001 | System internal error. |
| 1006620010 | The shortcut ID does not exist. |
| 1006620011 | Invalid context. |
| 1006620012 | Invalid shortcutId. |
| 1006620013 | The user refused to delete the shortcut. |
| 1006620014 | Invalid number of parameters. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { productViewManager } from '@kit.AppGalleryKit';

const TAG: string = 'RemovePinShortcut';

@Entry
@Component
struct RemovePinShortcut {

  build() {
    Column() {
      Button("RemovePinShortcut")
        .onClick(() => {
          try {
            const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
            const shortcutId = 'xxx'; // 通过checkPinShortcutPermitted接口获取
            productViewManager.removePinShortcut(uiContext, shortcutId)
              .then(() => {
                hilog.info(0x0001, TAG, `removePinShortcut success.`);
              }).catch((error: BusinessError) => {
              hilog.error(0x0001, TAG, `removePinShortcut error. code is ${error.code}, message is ${error.message}`);
            })
          } catch (err) {
            hilog.error(0x0001, TAG, `removePinShortcut failed, code is ${err.code}, message is ${err.message}`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
