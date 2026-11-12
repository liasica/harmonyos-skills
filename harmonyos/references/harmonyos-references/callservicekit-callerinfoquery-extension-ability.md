---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/callservicekit-callerinfoquery-extension-ability
title: CallerInfoQueryExtensionAbility (来去电信息查询扩展Ability)
breadcrumb: API参考 > 应用服务 > Call Service Kit（通话服务） > ArkTS API > CallerInfoQueryExtensionAbility (来去电信息查询扩展Ability)
category: harmonyos-references
scraped_at: 2026-11-12T09:57:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a44f67ae6dce529fad4048d759bb2f08a2bd29b5237b1ce035d80b30cdddece0
---

CallerInfoQueryExtensionAbility是来去电信息查询扩展Ability，提供通话来去电页面显示企业联系人信息的能力。有如下约束：

* CallerInfoQueryExtensionAbility需求场景面向企业，仅供企业应用开发者接入。
* CallerInfoQueryExtensionAbility为轻量级独立子进程，不允许唤醒主进程，进程存在最长时间为2秒，超时后自动销毁。
* CallerInfoQueryExtensionAbility支持在[HAP](../harmonyos-guides/hap-package.md)和[HAR](../harmonyos-guides/har-package.md)中使用。

**起始版本：** 5.0.2(14)

## 导入模块

```typescript
import { CallerInfoQueryExtensionAbility, CallerInfo, numberIdentify } from '@kit.CallServiceKit';
```

## CallerInfoQueryExtensionAbility

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力**：SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 5.0.2(14)

**说明** 

由于调用onQueryCallerInfo方法时，系统先创建应用的AbilityStage实例，请勿在AbilityStage中添加过于复杂耗时的逻辑，避免调用超时。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [CallerInfoQueryExtensionContext](callservicekit-callerinfoquery-extension-context.md) | 否 | 否 | [CallerInfoQueryExtensionContext](callservicekit-callerinfoquery-extension-context.md#callerinfoqueryextensioncontext)的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。 |

### onQueryCallerInfo

onQueryCallerInfo(phoneNumber: string):Promise<CallerInfo>

查询企业联系人接口，利用Promise返回查询结果，供来电和去电页面展示。企业应用需继承CallerInfoQueryExtensionAbility实现该接口，接口查询时间建议小于1s。由于通话应用会对已查询过的联系人进行缓存，若需清除该联系人缓存信息请使用resolve({ contactName: '' })。使用Promise异步回调。

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力**：SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 需要查询的号码 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CallerInfo](callservicekit-callerinfoquery-extension-ability.md#callerinfo)> | Promise对象，返回查询的号码信息。 |

**示例：**

```typescript
import { CallerInfoQueryExtensionAbility, CallerInfo } from '@kit.CallServiceKit';

export default class EntryCallerInfoQueryExtAbility extends CallerInfoQueryExtensionAbility {
  async onQueryCallerInfo(phoneNumber: string): Promise<CallerInfo> {
    return new Promise<CallerInfo>((resolve, reject) => {
      let isSuccess = true;
      // 在此处实现根据号码查询企业联系人的业务逻辑
      if (isSuccess) {
        // 查询成功，返回结果
        resolve({
          contactName: "张三",
          employeeId: "E123456",
          department: "销售部",
          position: "销售经理"
        });
      } else {
        // 查询失败，返回错误原因
        reject("error reason");
      }
    });
  }
}
```

**RDB（Relational Database）场景示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { relationalStore } from '@kit.ArkData';
import { CallerInfo, CallerInfoQueryExtensionAbility } from '@kit.CallServiceKit';

export default class EntryCallerInfoQueryExtAbility extends CallerInfoQueryExtensionAbility {
  async onQueryCallerInfo(phoneNumber: string): Promise<CallerInfo> {
    // 使用rdb场景需转化context类型
    const context = (this.context as common.ExtensionContext).getApplicationContext();
    let store = await relationalStore.getRdbStore(context, null);
    // 查询rdb数据后返回
    return new Promise<CallerInfo>((resolve, reject) => {
      let isSuccess = true;
      // 在此处实现根据号码查询企业联系人的业务逻辑
      if (isSuccess) {
        // 查询成功，返回结果
        resolve({
          contactName: "张三",
          employeeId: "S123456",
          department: "人力资源部",
          position: "招聘主管"
        });
      } else {
        // 查询失败，返回错误原因
        reject("error reason");
      }
    });
  }
}
```

### onQueryBusinessServiceData

onQueryBusinessServiceData(phoneNumber: string): Promise<Array<BusinessServiceData>>

查询企业服务信息，用于来电和去电页面展示。使用Promise异步回调。

企业应用需继承CallerInfoQueryExtensionAbility实现该接口，接口查询时间建议小于1s。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 需要查询的号码 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[BusinessServiceData](callservicekit-numberldentify.md#businessservicedata)>> | Promise对象，返回查询的企业服务信息列表。 |

**快递服务类型示例：**

```typescript
import { CallerInfoQueryExtensionAbility, numberIdentify } from '@kit.CallServiceKit';

export default class EntryCallerInfoQueryExtAbility extends CallerInfoQueryExtensionAbility {
  async onQueryBusinessServiceData(phoneNumber: string): Promise<Array<numberIdentify.BusinessServiceData>> {
    return new Promise<Array<numberIdentify.BusinessServiceData>>((resolve, reject) => {
      let isSuccess = true;
      // 在此处实现根据号码查询快递服务数据的业务逻辑
      if (isSuccess) {
        // 查询成功，返回结果
        resolve([{
          type: numberIdentify.BusinessServiceType.DELIVERY,
          delivery: {
            customerName: "张三",
            deliveryNumber: "ABC123456789",
            deliveryStatus: "派送中",
            deliveryAddress: "深圳市龙岗区坂田华为总部办公楼‌",
            deliveryTimeout: "预计11点之前送达",
            deliveryStatusColor: numberIdentify.DeliveryStatusColor.GREEN
          }
        }]);
      } else {
        // 查询失败，返回错误原因
        reject("error reason");
      }
    });
  }
}
```

**RDB场景示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { relationalStore } from '@kit.ArkData';
import { CallerInfoQueryExtensionAbility, numberIdentify } from '@kit.CallServiceKit';

export default class EntryCallerInfoQueryExtAbility extends CallerInfoQueryExtensionAbility {
  async onQueryBusinessServiceData(phoneNumber: string): Promise<Array<numberIdentify.BusinessServiceData>> {
    // 使用rdb场景需转化context类型
    const context = (this.context as common.ExtensionContext).getApplicationContext();
    let store = await relationalStore.getRdbStore(context, null);
    // 查询rdb数据后返回
    return new Promise<Array<numberIdentify.BusinessServiceData>>((resolve, reject) => {
      let isSuccess = true;
      // 在此处实现根据号码查询快递服务数据的业务逻辑
      if (isSuccess) {
        // 查询成功，返回结果
        resolve([{
          type: numberIdentify.BusinessServiceType.DELIVERY,
          delivery: {
            customerName: "张三",
            deliveryNumber: "ABC123456789",
            deliveryStatus: "派送中",
            deliveryAddress: "深圳市龙岗区坂田华为总部办公楼",
            deliveryTimeout: "预计30分钟内送达",
            deliveryStatusColor: numberIdentify.DeliveryStatusColor.GREEN
          }
        }]);
      } else {
        // 查询失败，返回错误原因
        reject("error reason");
      }
    });
  }
}
```

**外卖服务类型示例：**

```typescript
import { CallerInfoQueryExtensionAbility, numberIdentify } from '@kit.CallServiceKit';

export default class EntryCallerInfoQueryExtAbility extends CallerInfoQueryExtensionAbility {
  async onQueryBusinessServiceData(phoneNumber: string): Promise<Array<numberIdentify.BusinessServiceData>> {
    return new Promise<Array<numberIdentify.BusinessServiceData>>((resolve, reject) => {
      let isSuccess = true;
      // 在此处实现根据号码查询外卖服务数据的业务逻辑
      if (isSuccess) {
        // 查询成功，返回结果
        resolve([{
          type: numberIdentify.BusinessServiceType.CARRYOUT,
          carryout: {
            customerName: "张三",
            carryoutNumber: "123456789",
            carryoutMerchant: "xx炸鸡店",
            carryoutStatus: "配送中",
            carryoutStatusColor: numberIdentify.StatusColor.GREEN,
            carryoutAddress: "深圳市龙岗区坂田华为总部办公楼",
            carryoutTimeoutDescription: "预计30分钟内送达",
            deepLinking: "app://com.huawei.xxxx"
          }
        }]);
      } else {
        // 查询失败，返回错误原因
        reject("error reason");
      }
    });
  }
}
```

**说明** 

在外卖服务类型查询示例代码中利用deepLinking进行跳转，需要在应用module.json5中配置[详见module.json5配置](../harmonyos-guides/deep-linking-startup.md#配置modulejson5文件)，scheme和应用bundleName一致。

### onQueryBusinessServiceDataWithProtocol

onQueryBusinessServiceDataWithProtocol(privacyPhoneNumber: Uint8Array, privacyProtocol: PrivacyProtocol): Promise<PrivacySearchResult>

隐私查询企业服务信息。

企业应用需继承CallerInfoQueryExtensionAbility实现该接口，接口查询时间建议小于1s。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| privacyPhoneNumber | Uint8Array | 是 | 隐私计算后的电话号码数据。 |
| privacyProtocol | [PrivacyProtocol](js-apis-privacycomputation.md#privacyprotocol) | 是 | 隐私计算协议参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PrivacySearchResult](js-apis-privacycomputation.md#privacysearchresult)> | Promise对象，返回隐私查询结果。 |

**示例：**

```typescript
import { CallerInfoQueryExtensionAbility, numberIdentify } from '@kit.CallServiceKit';
import { privacyComputation } from '@kit.DataProtectionKit'

export default class EntryBusinessServiceDataQueryExtAbility extends CallerInfoQueryExtensionAbility {
  async onQueryBusinessServiceDataWithProtocol(privacyPhoneNumber: Uint8Array, privacyProtocol: privacyComputation.PrivacyProtocol): Promise<privacyComputation.PrivacySearchResult> {
    // 定义订单记录类型
    interface OrderRecord {
      phone: string;
      carryoutData: numberIdentify.CarryoutData;
    }
    // 构造CarryoutData对象
    const carryoutData: numberIdentify.CarryoutData = {customerName: "张三", carryoutNumber: "123456789", carryoutMerchant: "xx×餐饮店", carryoutStatus: "配送中", carryoutStatusColor: numberIdentify.StatusColor.BLUE, carryoutAddress: "深圳市龙岗区坂田华为总部办公楼", carryoutTimeoutDescription: "预计30分钟内送达", deepLinking: "app://com.huawei.xxxx" };
    // 查询订单数据
    const orders: Array<OrderRecord> = ([{ phone: "138xxxxxxxx", carryoutData: carryoutData }]);
    // 将订单数据转换为隐私对象，其中elemValue为numberIdentify.BusinessServiceData对象。
    const elements: Array<privacyComputation.Element> = orders.map(o => {
      const businessData: numberIdentify.BusinessServiceData = {
        type: numberIdentify.BusinessServiceType.CARRYOUT,
        carryout: o.carryoutData
      };
      const element: privacyComputation.Element = {
        elemKey: stringToUint8Array(o.phone), // 匹配键
        hashAlg: privacyComputation.HashAlg.SHA256, // 指定哈希算法
        elemValue: stringToUint8Array(JSON.stringify(businessData))
      };
      return element;
    });

    return await privacyComputation.privacySearch(privacyPhoneNumber, elements, privacyProtocol);
  }
}
```

**说明** 

* 示例代码中stringToUint8Array方法实现，详见文档[Uint8Array类型和String以及hex如何互相转换](../harmonyos-faqs/faqs-arkts-91.md)中示例代码stringToUint8Array方法。
* 示例代码中[privacyComputation.Element](js-apis-privacycomputation.md#element)是由Data Protection Kit定义的数据接口。
* 示例代码中HashAlg含义与具体枚举值详见[privacyComputation.HashAlg](js-apis-privacycomputation.md#hashalg)。
* 示例代码中[privacyComputation.privacySearch](js-apis-privacycomputation.md#privacycomputationprivacysearch)是由Data Protection Kit提供的隐私查询方法。

## CallerInfo

联系人信息。

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力**：SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| contactName | string | 否 | 否 | 联系人姓名：为保证页面最佳显示效果，字数建议限制在20字以内。 |
| employeeId | string | 否 | 是 | 工号：为保证页面最佳显示效果，字数建议限制在20字以内。不填该参数则不显示工号。 |
| department | string | 否 | 是 | 部门：为保证页面最佳显示效果，字数建议限制在20字以内。不填该参数则不显示部门。 |
| position | string | 否 | 是 | 职位：为保证页面最佳显示效果，字数建议限制在20字以内。不填该参数则不显示职位。 |
