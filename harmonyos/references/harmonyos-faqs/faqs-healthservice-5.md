---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-healthservice-5
title: 运动健康无法获取数据常见问题和解决方案
breadcrumb: FAQ > 应用服务开发 > 运动健康数据服务（Health Service Kit） > 运动健康无法获取数据常见问题和解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:ce40e9be899e36b74eaafe55dcaa78da504a649748d61639c556910552068d6e
---

## 问题现象

1. 通过下载的代码：[Health\_Service\_Kit\_SampleCode](https://gitcode.com/HarmonyOS_Samples/health_-service_-kit_-sample-code)：本示例基于运动健康服务开放能力，实现运动健康数据的管理和运动联动。已按照要求修改，但是点击授权报错：Failed to request authorization, Code: 1001502014, message: The appdoes not have the reguired scopes or permissions.no scope permission。
2. 报错如下所示：Ext\_AuthManagement: client auth fail,error: {"code":1001502003,"message":"Invalid input parameter value.parameter invalid"}。
3. 调用运动健康服务接口报错如下：Failed to request authorization. Code: undefined, message: Cannot read property connectServiceExtensionAbility of undefined 。
4. 使用healthStore.requestAuthorizations接口报错：Failed to request authorization. Code: 12300001, message: System service works abnormally。
5. Health Service Kit获取健康数据的时候报错201，错误信息是：Permission verification failed, The app is not authorized。

## 背景知识

[Health Service Kit（运动健康服务）](../harmonyos-guides/health-service-kit-guide.md)是为华为生态应用打造的基于华为账号和用户授权的运动健康数据开放平台。在获取用户授权后，开发者可以使用Health Service Kit提供的开放能力获取运动健康数据，基于多种类型数据构建运动健康领域应用与服务，为用户打造丰富、便捷、专业的运动健康场景体验。

| [约束和限制](../harmonyos-guides/health-service-kit-ability.md#约束与限制) | 说明 |
| --- | --- |
| [支持的设备](../harmonyos-guides/health-service-kit-ability.md#支持的设备) | Health Service Kit仅适用于Phone、Tablet、Wearable。 |
| [支持的国家/地区](../harmonyos-guides/health-service-kit-ability.md#支持的国家地区) | Health Service Kit仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| [模拟器支持情况](../harmonyos-guides/health-service-kit-ability.md#模拟器支持情况) | 从6.0.2(22) 版本开始，本kit支持模拟器开发，但与真机存在部分能力差异，具体如下：不支持Wearable应用开发；不支持运动健康联动服务、实时三环数据、手动同步数据，以及运动健康App相关能力；默认开启隐私授权。 |

错误码请参考[ArkTS API错误码](../harmonyos-references/errorcode-healthservice.md)

## 解决方案

* 问题一：确保授权请求参数中的数据类型已经在Health Service Kit卡片中申请相应的权限，申请步骤请参考[申请运动健康服务](../harmonyos-guides/health-apply.md)，数据类型对应的权限参考[权限说明](../harmonyos-guides/health-permission-description.md)。

  登录[开发者联盟网站](https://developer.huawei.com/consumer/cn/)，单击进入“管理中心”。在应用服务中，单击Health Service Kit卡片申请Health Service Kit服务，同意协议后，进入数据权限申请页面，确保使用权限scopes已勾选申请，应用内使用申请权限对照[权限说明](../harmonyos-guides/health-permission-description.md)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/buv-yNnyTpW0yZ22wCMAiQ/zh-cn_image_0000002661377573.png "点击放大")

  更多错误码请参考[ArkTS API错误码](../harmonyos-references/errorcode-healthservice.md)。
* 问题二：说明没有正确配置client\_id，将client\_id(xxxxxxx)配置到‘\entry\src\main\module.json5’文件中再次尝试，参考[配置Client ID](../harmonyos-guides/health-configuration-client-id.md)。
* 问题三：如果调用运动健康服务接口没有回调，或者出现该报错，说明健康服务未进行初始化，调用其他接口前，需要先调用init方法初始化：healthStore.init(this.context)，参考[healthStore(运动健康数据服务)](../harmonyos-references/health-api-healthstore.md)。
* 问题四：[12300001](../harmonyos-references/errorcode-account.md#section12300001-系统服务异常)表示账号管理系统服务异常，具体参考[账号管理错误码](../harmonyos-references/errorcode-account.md)。
* 问题五：[201鉴权失败](../harmonyos-references/errorcode-healthservice.md#section201-鉴权失败)。

  可能原因：

  1. 应用指纹配置不正确。
  2. 缺少权限。
  3. 部分接口仅白名单用户可调用。
  4. 测试用户数已达上限。

  处理步骤：

  1. 检查AGC上应用的指纹证书，详情请见[添加公钥指纹](../harmonyos-guides/application-dev-overview.md#条件必选添加公钥指纹)。
  2. 参考[管理用户授权](../harmonyos-guides/health-add-permissions.md)，确认用户已授权相关权限。
  3. 用户申请成为测试用户失败，请尽快参考[申请验证获取正式权限](../harmonyos-guides/health-verification.md)，完成管理台应用验收。
  4. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/ticketCard)提交问题，华为支持人员会及时处理。
