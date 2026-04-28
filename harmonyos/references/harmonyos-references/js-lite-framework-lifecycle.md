---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-lifecycle
title: 生命周期
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 框架说明 > 生命周期
category: harmonyos-references
scraped_at: 2026-04-28T08:03:23+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ad5c8a12d4e7e72108156d88f0386aecb45ff786d6ef523f208ded2d802f4e35
---

## 应用生命周期

PhonePC/2in1TabletTVWearableLite Wearable

在app.js中可以定义如下应用生命周期函数：

| 属性 | 类型 | 描述 | 触发时机 |
| --- | --- | --- | --- |
| onCreate | () => void | 应用创建 | 当应用创建时调用。 |
| onDestroy | () => void | 应用销毁 | 当应用退出时触发。 |

## 页面生命周期

PhonePC/2in1TabletTVWearableLite Wearable

在页面JS文件中可以定义如下页面生命周期函数：

说明

请注意不要在生命周期函数中执行复杂耗时操作，以避免影响页面切换性能。

| 属性 | 类型 | 描述 | 触发时机 |
| --- | --- | --- | --- |
| onInit | () => void | 页面初始化 | 页面数据初始化完成时触发，只触发一次。 |
| onReady | () => void | 页面创建完成 | 页面创建完成时触发，只触发一次。 |
| onShow | () => void | 页面显示 | 页面显示时触发。 |
| onHide | () => void | 页面消失 | 页面消失时触发。 |
| onDestroy | () => void | 页面销毁 | 页面销毁时触发。 |

页面A的生命周期接口的调用顺序：

* 打开页面A：onInit() -> onReady() -> onShow()
* 在页面A打开页面B：onHide() -> onDestroy()
* 从页面B返回页面A：onInit() -> onReady() -> onShow()
* 退出页面A：onHide() -> onDestroy()
* 页面隐藏到后台运行：onHide()
* 页面从后台运行恢复到前台：onShow()

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/3Tm1II7kTR6Uz9ODRj8Dxw/zh-cn_image_0000002583480331.png?HW-CC-KV=V1&HW-CC-Date=20260428T000322Z&HW-CC-Expire=86400&HW-CC-Sign=08DDEE52E9F3B7221B7E7CAA1FE1E92018BC3B7E83C0E71A4C16307E46F3B53A)
