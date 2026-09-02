---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-27
title: 设备关闭定位情况下，应用获取位置时闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 设备关闭定位情况下，应用获取位置时闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:07e291ec3696b5f10d59875a3bcafd0996c383c077b3635e808b163bcc17b38c
---

## 问题现象

在设备关闭定位的情况下，应用获取位置信息会出现闪退。

## 背景知识

* 关于位置定位服务开发文档可见[位置定位](../best-practices/bpta-positioning.md)。
* [位置服务错误码](../harmonyos-references/errorcode-geolocationmanager.md)：3301100-位置功能的开关未开启导致功能失败。
* JsCrash异常根据不同的异常场景，在Reason字段进行了分类，分为Error、TypeError、SyntaxError、ReferenceError、RangeError等错误类型。参考文档[JS Crash（进程崩溃）检测](../harmonyos-guides/jscrash-guidelines.md)。
* JsCrash日志可参考[日志规格](../harmonyos-guides/jscrash-guidelines.md#日志规格)。

## 问题定位

1. 从faultlogger目录下获取故障日志。
2. 打开对应日志查看内容，确定故障原因是Error。

   异常信息是“BusinessError 3301100: The location switch is off.”，该错误码表示位置功能的开关未开启导致功能失败。

   ```screen
   Error name:Error
   Error message:BusinessError 3301100: The location switch is off.
   Error code:3301100
   Stacktrace:
   Cannot get SourceMap info, dump raw stack:
   at locationinfo (entry|entry|1.0.0|src/main/ets/model/coordinates.ts:22:1)
   at aboutToAppear (entry|entry|1.0.0|src/main/ets/pages/mapPage/mapPage.ts:95:1)
   ```
3. 排查堆栈中的代码在使用定位服务时，是否先判断位置开关已打开，是否捕获了异常并处理。

## 分析结论

应用在获取当前位置信息前，未判断位置开关状态，且未捕获异常，导致应用闪退。

## 修改建议

建议参考文档[获取设备的位置信息开发指导](../harmonyos-guides/location-guidelines.md)，应用调用位置服务接口前，应当先判断位置开关状态是否开启，如果位置开关未开启，可以使用[requestGlobalSwitch](../harmonyos-references/js-apis-abilityaccessctrl.md#requestglobalswitch12)接口拉起全局开关设置弹框提醒用户开启，代码示例参考[开发步骤](../harmonyos-guides/location-guidelines.md#开发步骤)。
