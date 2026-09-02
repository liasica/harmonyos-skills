---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-wear-engine-2
title: 申请接入Wear Engine服务咨询
breadcrumb: FAQ > 系统开发 > 硬件 > 穿戴服务（Wear Engine Kit） > 申请接入Wear Engine服务咨询
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:0d49be595953478cd6e765c4fb05a9b4426facd7a61a18a9d9f5994fc3445f4b
---

## 问题现象

接入Wear Engine服务，填写申请中对选项疑问咨询。

问题一：针对与旧版本穿戴应用通信的手机移动应用的兼容选项存在疑问。

问题二：对权限中设备能力类的各个权限有疑惑。

问题三：对基本信息选项有疑惑。

问题四：运动表引入[Wear Engine SDK (Lite Wearable Devices)](https://developer.huawei.com/consumer/en/doc/connectivity-Library/litewearable-sdk-cn-0000001705004353)后编译报错，报错内容如下：

```screen
>hvigor ERROR: Failed :entry:default@LegacyBuildJS...
>hvigor ERROR: Tools execution failed.
Module not found:Error: Can't resolve '@system.wearengine' in 'D:\Demo\entry\src\main\js\MainAbility\pages'
  Detail: Please check the message from tools.
>hvigor ERROR BUILD FAILED in 10 s 445 ms
```

问题五：若智能表在申请Wear Engine服务时未申请佩戴状态服务，应当如何获取佩戴状态或传感器服务？

问题六：若开发者不计划接入Wear Engine SDK，应如何通过手机应用获取穿戴设备的传感器数据？

## 解决方案

问题一：这里兼容的目的是让HarmonyOS Next手机应用与旧版本的其他平台手表应用通信（系统内部会将HarmonyOS Next应用包名转为映射其他平台包名）。

问题二：权限可参考[权限说明](../harmonyos-guides/wearengine_apply.md)。

问题三：

* 智能穿戴设备与轻量级穿戴设备的区别：
  + 智能穿戴（Wearable）：如Watch3、Watch4系列智能表。
  + 轻量级智能穿戴（Lite Wearable）：如HUAWEI WATCH GT系列、Watch D系列、Fit系列、Watch Ultimate系列。
* 是否开发在该穿戴设备上的应用？
  + 是，指的是开发手机、手表侧应用。
  + 否，指的是只开发手机侧应用。

问题四：Wear Engine SDK只支持设备类型为：Lite Wearable，将deviceType中Wearable设备类型去掉即可。

问题五：可以参考[传感器服务](../harmonyos-guides/sensor-service-kit.md)文档。

问题六：可以通过华为运动健康授权，调用运动健康相关接口，获取此类信息，参考[华为运动健康服务接入流程](../harmonyos-guides/health-application-access.md)。
