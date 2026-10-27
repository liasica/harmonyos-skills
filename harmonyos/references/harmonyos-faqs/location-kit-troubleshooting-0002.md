---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/location-kit-troubleshooting-0002
title: 应用获取设备定位信息问题定位
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 故障排查 > 应用获取设备定位信息问题定位
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:41+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:3f6951f2f85f332c41d0c227e0b39093baeb4c7f26d287f5767c4ba027016a51
---

## 问题现象

在设备关闭定位的情况下，应用获取位置信息会出现闪退。

## 定位过程

1. 从faultlogger目录下获取故障日志。
2. 打开对应日志查看内容，确定故障原因是Error。异常信息是“BusinessError 3301100: The location switch is off.”，该错误码表示位置功能的开关未开启导致功能失败。

   ```txt
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
