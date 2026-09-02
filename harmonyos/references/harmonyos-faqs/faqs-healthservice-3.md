---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-healthservice-3
title: 运动健康服务授权及取消授权失败问题
breadcrumb: FAQ > 应用服务开发 > 运动健康数据服务（Health Service Kit） > 运动健康服务授权及取消授权失败问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:30+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:b67341a4c3f35680b2888b26b8269bfca98bd62d95fe1c50858bf29f32a5086b
---

## 问题现象

1. 运动健康Kit无法授权，或者请求授权无回调。
2. 运动健康服务日常活动数据取消授权未生效，调用getAuthorizations返回的是已授权，并且还可以从健康读到有效步数。

## 背景知识

使用运动健康服务时，需要拉起华为账号登录和授权界面，由用户授权相应的数据访问权限。用户可以自主选择授权的数据类型，可以只授权部分数据权限。应用所能操作的用户数据，是用户授权和运动健康服务审批通过的数据权限的交集。

开发前检查：

1. 完成[申请运动健康服务](../harmonyos-guides/health-apply.md)与[配置Client ID](../harmonyos-guides/health-configuration-client-id.md)。
2. 确保授权参数中的数据类型权限已在申请运动健康服务时勾选，权限说明参考[权限说明](../harmonyos-guides/health-permission-description.md)。
3. 接口需在页面或自定义组件生命周期内调用。接口首次调用前，需先使用[healthStore.init](../harmonyos-references/health-api-healthstore.md#healthstoreinit)方法进行初始化。

## 问题定位

* 针对运动健康Kit无法授权，或者请求授权无回调的问题：
  1. 检查HiLog日志，查看错误码。
  2. 检查是否申请相关运动健康服务权限。
  3. 检查client\_id配置的位置及client\_id值配置的是否正确，应配置在‘\entry\src\main\module.json5’文件的module下，值为“xxxxxxxx”，即登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置>常规>应用”的Client ID：

     ```json
     {
       "module": {
         "metadata": [
           {
             "name": "client_id",
             "value": "xxxxxxxx"
           }
         ]
       }
     }
     ```
  4. 在请求授权的参数‘authorizationParameter’的readDataTypes中增加日常活动权限（healthStore.samplePointHelper.dailyActivities.DATA\_TYPE）重新拉起授权试试，此权限是当前申请的权限。
  5. 调用运动健康数据服务接口是否报错。
  6. 如果问题依旧存在，建议升级到新版本进行尝试。
  7. 检查接口调用前是否healthStore.init初始化。
* 针对运动健康服务授权后再取消授权不生效：
  1. 检查授权之后再设置中取消授权，系统是否有杀进程的操作。
  2. 检查缓存是否清除。

虽然运动健康数据管理里面取消授权，但授权信息是有缓存(当前缓存的时效是2小时)不会立刻被清除，如果要清除权限立刻生效，需要调用Health Service Kit的取消授权[healthStore.cancelAuthorizations](../harmonyos-references/health-api-healthstore.md#healthstorecancelauthorizations)接口。

不过，有缓存也不会影响应用的功能使用，应用使用时通过Health Service Kit接口检查是否有权限，无权限时正常提示用户授权就行。

## 分析结论

1. 无法授权问题需要针对具体错误码分析，也和client\_id的配置有关；
2. 如果需要取消授权立即生效的话，需要主动调用healthStore.cancelAuthorizations接口。

## 修改意见

* 针对运动健康Kit无法授权，或者请求授权无回调的问题：
  1. 在文档中查找错误码，对应进行处理，参考：[ArkTS API错误码](../harmonyos-references/errorcode-healthservice.md)。

     **说明** 

     在AGC上面，添加公钥指纹（HarmonyOS API 9及以上）后，指纹有一定时间的缓存，不会立刻生效，建议配置完成后等半小时再尝试。
  2. 如果错误码是1001502014，说明缺少运动健康服务的Scope权限。参考：[申请运动健康服务](../harmonyos-guides/health-apply.md)。
  3. 如果报错如下所示：那么说明没有正确[配置Client ID](../harmonyos-guides/health-configuration-client-id.md)，将client\_id(xxxxxxx)配置到‘\entry\src\main\module.json5’文件中再次尝试。

     ```shell
     Ext_AuthManagement: client auth fail,error: {"code":1001502003,"message":"Invalid input parameter value.parameter invalid"}
     ```
  4. 如果调用运动健康服务接口没有回调，或者出现报错如下，说明健康服务未进行初始化，调用其他接口前，需要先调用init方法初始化：healthStore.init(this.context)；具体可参考：[运动健康数据服务](../harmonyos-references/health-api-healthstore.md)。

     ```shell
     Failed to request authorization. Code: undefined, message: Cannot read property connectServiceExtensionAbility of undefined
     ```
  5. 确认相关权限已经申请并配置成功，例如：步数通过日常活动数据进行开放，如果需要获取步数数据，需要申请“日常活动数据”权限。
* 针对运动健康服务授权后再取消授权不生效：

  调用healthStore.getAuthorizations判断用户是否授权了该权限。如果开发者想要清除权限立刻生效，需要调用Health Service Kit的[healthStore.cancelAuthorizations](../harmonyos-references/health-api-healthstore.md#healthstorecancelauthorizations)接口取消授权。

## 常见FAQ

Q：Health Service Kit接口是否支持在子线程调用？

A：Health Service Kit接口，仅支持在主线程中调用，不支持在子线程中调用，否则getAuthorizations接口会报错：“Failed to get authorization. Code: 1, message: System internal error. Now pid 62571 is not equal to tid 62682”。

Q：提供了哪些运动健康数据？

A：运动健康服务提供了一系列运动和健康数据类型，主要分三组：[采样数据](../harmonyos-guides/health-samplepoint.md)、[锻炼记录数据](../harmonyos-guides/health-exercisesequence.md)、[健康记录数据](../harmonyos-guides/health-healthsequence.md)。
