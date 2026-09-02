---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-lifecycle
title: 生命周期
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 框架说明 > 生命周期
category: harmonyos-references
scraped_at: 2026-09-02T15:01:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b00be93260a8e574f40f28528cfa2903aaa8d23fad8a94639692eaa858155e2c
---

生命周期用于描述应用和页面从创建、显示、隐藏到销毁的状态变化过程。开发者可以通过应用生命周期和页面生命周期函数，在对应阶段处理初始化、页面显示隐藏响应、销毁清理等逻辑，适用于管理应用启动退出、页面切换和前后台状态变化的场景，有助于按阶段组织业务逻辑和资源管理。

## 应用生命周期

在app.js中可以定义如下应用生命周期函数：

| 属性 | 类型 | 描述 | 触发时机 |
| --- | --- | --- | --- |
| onCreate | () => void | 应用创建 | 当应用创建时触发。 |
| onDestroy | () => void | 应用销毁 | 当应用退出时触发。 |

## 页面生命周期

在页面JS文件中可以定义如下页面生命周期函数：

**说明** 

请注意不要在生命周期函数中执行复杂耗时操作，以避免影响页面切换性能。

| 属性 | 类型 | 描述 | 触发时机 |
| --- | --- | --- | --- |
| onInit | () => void | 页面初始化 | 页面数据初始化完成时触发，只触发一次。 |
| onReady | () => void | 页面创建完成 | 页面创建完成时触发，只触发一次。 |
| onShow | () => void | 页面显示 | 页面显示时触发。 |
| onHide | () => void | 页面消失 | 页面消失时触发。 |
| onDestroy | () => void | 页面销毁 | 页面销毁时触发。 |

页面A的生命周期函数的调用顺序：

* 打开页面A：onInit() -> onReady() -> onShow()
* 在页面A打开页面B：onHide() -> onDestroy()
* 从页面B返回页面A：onInit() -> onReady() -> onShow()
* 退出页面A：onHide() -> onDestroy()
* 页面隐藏到后台运行：onHide()
* 页面从后台运行恢复到前台：onShow()

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/htAv9DEsR52k2b4MP5RLLw/zh-cn_image_0000002706676586.png)
