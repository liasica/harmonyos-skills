---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1208
title: 点击跳转按钮无反应
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 点击跳转按钮无反应
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fe331c7c05ef3f2d4f30910dcbd51dfeb911193d5be851a1d4dd3363b1da1944
---

## 问题现象

点击应用中的直达链接按钮，无任何反应，不进行跳转。

## 背景知识

跳转的类型通常分为三种：

* [拉起指定应用](../harmonyos-guides/app-startup-overview.md)：拉起方应用明确指定跳转的目标应用，来实现应用跳转。指向性跳转可以分为指定应用链接、指定Ability两种方式。
  + 指定应用链接（推荐）：通过[openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)或[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)接口来指定应用链接，拉起目标应用页面。
  + 指定Ability（不推荐）：通过[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)接口指定具体的Ability（即显式Want方式），拉起目标应用页面。
* [拉起指定类型的应用](../harmonyos-guides/start-intent-panel.md)：拉起方应用通过指定应用类型，拉起垂类应用面板。该面板将展示目标方接入的垂域应用，由用户选择打开指定应用。
* [Router](../harmonyos-guides/arkts-routing.md)/[Navigation](../harmonyos-guides/arkts-navigation-navigation.md)实现页面间跳转：通过配置需跳转的指定页面url，拉起指定页面。

## 问题定位

1. 查看日志中报错部分，其中zolxb://navigateTo?json=中包含需要打开应用的应用名、跳转的应用内的url地址等。

   ```screen
   protocol info zolxb://navigateTo?json={"page":"tbMall.open","data":{"shopAppUrl":"https:\/\/s.click.***.com\/t?e=m%3D2%26s%3DWD07Zg8T%2B6tw4vFB6t2Z2ueEDrYVVa64yK8Cckff7TVRAdhuF14FMZ8t5svtDNV28sviUM61dt33dPcEDU9PrAyKP3Li%2BRxZGXIO%2BajC16cCRHo%2BLSv4uw7AYKSmXaOVCGsxm48e9hkfF%2Bxu0N%2BwWuNuzGFfLfLZJacGw0cdRDH9Umq014SDk%2F3G4s1I7HnfLOMElksE2%2BmlBFARV%2ByS0ozyQOSle91Rla4yZNVxZ3jmrzYD%2B1beXJEuifbDPrCh6FTIuJSduFeQOnvGTHGHmdOG7fwodBwmz5z6ZDUnxVm4BOrOxKLpwOw0cHTcw5Bti%2FARjdUyGUghhQs2DjqgEA%3D%3D&union_lens=lensId:TAPI@1750228402@2127cbfb_183d_19781be01bc_8826@01","webUrl":"https:\/\/s.click.***.com\/t?e=m%3D2%26s%3DWD07Zg8T%2B6tw4vFB6t2Z2ueEDrYVVa64yK8Cckff7TVRAdhuF14FMZ8t5svtDNV28sviUM61dt33dPcEDU9PrAyKP3Li%2BRxZGXIO%2BajC16cCRHo%2BLSv4uw7AYKSmXaOVCGsxm48e9hkfF%2Bxu0N%2BwWuNuzGFfLfLZJacGw0cdRDH9Umq014SDk%2F3G4s1I7HnfLOMElksE2%2BmlBFARV%2ByS0ozyQOSle91Rla4yZNVxZ3jmrzYD%2B1beXJEuifbDPrCh6FTIuJSduFeQOnvGTHGHmdOG7fwodBwmz5z6ZDUnxVm4BOrOxKLpwOw0cHTcw5Bti%2FARjdUyGUghhQs2DjqgEA%3D%3D&union_lens=lensId:TAPI@1750228402@2127cbfb_183d_19781be01bc_8826@01","sourcePage":"\u666e\u901a\u6587\u7ae0\u8be6\u60c5","contentId":0,"pageName":"","location":"\u666e\u901a\u6587\u7ae0\u8be6\u60c5\u9875\u6587\u4e2d\u63d2\u5165\u7684\u5546\u54c1","dataFrom":"tb","businessName":"\u6dd8\u5b9d"}}, %{public}s
   page: [object Object], %{public}s
   protocolConfig.get undefined, %{public}s
   ```
2. 全局搜索zolxb://navigateTo?json=查看其实现逻辑，可以发现需要跳转的应用或页面均通过protocolConfig.get()方法来获取，而protocolConfig.get()方法在ProtocolMap页面中。
3. 日志中存在"page":"tbMall.open"，在initProtocolMap中set的应用名中查找该名字。
4. 检查main\_pages.json中是否正确配置了页面src，Router中url，或Navigation中target跳转路径是否与main\_pages.json中配置的一致。

## 分析结论

* 结论一：没有set此点击事件需要跳转的应用，导致get方法返回的值为undefined，无法进行跳转。
* 结论二：跳转页面没有在main\_pages.json中配置，Router中url和Navigation中target跳转路径填写错误。

## 修改建议

在方法中正确配置需要跳转的应用名称或通过openLink或startAbility接口来指定应用链接，拉起目标应用页面的方式来进行应用间的跳转。
