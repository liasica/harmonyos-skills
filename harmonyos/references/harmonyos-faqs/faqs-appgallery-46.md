---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-46
title: 多系统共用隐私政策协议时，需要注意哪些点
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 多系统共用隐私政策协议时，需要注意哪些点
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:86cf57653d2d6b846456714ece9cc70c64a3cac92213a334f669018c9b97b417
---

## 问题现象

应用需要在多系统上共同发布，隐私政策协议应该怎么写？有哪些注意点？

## 背景知识

隐私政策协议的制作有两种方式，一种为使用隐私管理服务进行托管制作，另一种为开发者自行制作。详细内容如下：

* [隐私管理服务](../harmonyos-guides/store-privacy.md)：隐私管理服务为使用标准化隐私声明托管服务的应用/元服务提供隐私链接查询、隐私签署状态查询、停止隐私协议和拉起标准化隐私弹框功能。
* 自行制作隐私政策：可以使用接口[提交隐私政策协议](../app/agc-help-publish-api-put-privacy-agreement-0000002271000633.md)、[查询隐私政策协议列表](../app/agc-help-publish-api-query-privacy-agreement-0000002328924925.md)、[更新隐私政策协议](../app/agc-help-publish-api-update-privacy-agreement-0000002328805169.md)完成。

## 解决方案

应用需要在多系统上共同发布，注意点有如下两点：

1. **合规性要求：**
   * **必要性原则：**

     隐私政策协议内容应围绕应用实际功能展开。若应用存在跨平台数据共享或需说明多平台兼容性，可在协议中提及相关系统，但需明确说明数据交互的具体场景（例如：用户通过其他平台及HarmonyOS设备使用同一账号时的数据同步逻辑）。
   * **避免误导性描述：**

     若应用仅适用于HarmonyOS，则无需提及其他操作系统，避免用户误解应用支持其他平台。
2. **开发实践建议：**
   * **采用标准化模板：**

     建议使用[AGC（AppGallery Connect）](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)提供的隐私管理服务，通过标准模板生成协议内容，减少合规风险。
   * **声明数据交互场景：**

     若涉及多平台数据交互，需在隐私政策协议中清晰描述：
     + 数据来源。
     + 数据处理范围。
     + 数据保护措施。

## 常见FAQ

Q：应用隐私政策协议中仅有其他平台相关的描述，需要重新制作一份适用于HarmonyOS的隐私政策协议吗？

A：不需要重新单独制作一份，若是多系统共用隐私政策协议，在内容正确的前提下，仅需在原先协议的基础上添加上HarmonyOS相关的声明即可。
