---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-sensor-service-4
title: 旋转锁定失效
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 旋转锁定失效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:8161b85add198e9baa5c174c2d9bf42b5b48d889f33365c5d4956bc365594b59
---

## 问题现象

设备开启旋转锁定，但应用内页面仍跟随传感器自动旋转。

## 背景知识

* [横竖屏切换](../best-practices/bpta-landscape-and-portrait-development.md)：为实现应用内既支持竖屏又支持横屏，并在不同页面呈现不同方向，需要在应用逻辑中动态切换窗口方向。目前在HarmonyOS系统中，窗口的旋转形态包括以下四种，窗口的状态对应真机实际状态如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/naxQqlEmSQihwBLmPyV7LA/zh-cn_image_0000002686049237.png "点击放大")
* [module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)的orientation标签：标识当前UIAbility组件启动时的方向。
* [setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)：设置主窗口的显示方向属性，使用Promise异步回调。
* [orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)：窗口显示方向类型枚举。

## 问题定位

1. 检查[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)的orientation字段设置是否正确。
2. 在日志中搜索关键字setWindowOrientation或SetPreferredOrientation，如果发现有setWindowOrientation: 7 Succeeded.或OnSetPreferredOrientation end, window [xxxx, xxxx] orientation=7信息，则说明应用将主窗口的显示方向属性设置为AUTO\_ROTATION\_LANDSCAPE。

   **AUTO\_ROTATION\_LANDSCAPE为Orientation枚举值之一，若日志结果为其他枚举值，可参考背景知识。**

   ```txt
   com.examp....ittoggle I  setWindowOrientation: 7 Succeeded., %{public}s
   ```

   ```txt
   SetRequestedOrientation(1869): id: 1167 lastReqOrientation: 1 target: 7 state: 2
   [invalidDomain][]: OnSetPreferredOrientation end, window [1167, rrsp0] orientati
   ```

## 分析结论

* 在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)的orientation字段设置不合理，导致旋转锁定失效。
* 应用设置主窗口的显示方向属性为AUTO\_ROTATION\_LANDSCAPE，不受控制中心的旋转开关控制。

## 修改建议

* 根据实际需求设置合理的字段，例如设置为auto\_rotation\_unspecified受开关控制且由系统判定的自动旋转。
* 使用[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)将主窗口的显示方向属性设置为AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED。

## 常见FAQ

Q：当Ability设置了auto\_rotation\_landscape\_restricted，如何将窗口动态设置为竖屏模式？

A：使用window.setPreferredOrientation接口，在运行时设置orientation为PORTRAIT，从而将屏幕变成竖屏模式。
