---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-45
title: 组件支持的参数类型及参数单位类型：PX、 VP、 FP 、LPX、Percentage、Resource 详细区别是什么
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 组件支持的参数类型及参数单位类型：PX、 VP、 FP 、LPX、Percentage、Resource 详细区别是什么
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:08+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:72158d8b10f7c1595fc70a4474a28e753ace4af8f3171bd8d17aa8e026f3cd66
---

[屏幕像素单位](../harmonyos-references/ts-types.md#px10)：px。屏幕上的实际像素，1px代表手机屏幕上的一个像素点。

[视窗逻辑像素单位](../harmonyos-references/ts-types.md#lpx10)：lpx。视窗逻辑像素单位，lpx单位为实际屏幕宽度与逻辑宽度（通过[designWidth](../harmonyos-guides/module-configuration-file.md#pages标签)配置）的比值，designWidth默认值为720。当designWidth为720时，在实际宽度为1440物理像素的屏幕上，1lpx为2px大小。

[虚拟像素单位](../harmonyos-references/ts-types.md#vp10)：vp。屏幕密度相关像素，根据屏幕像素密度转换为屏幕物理像素，当数值不带单位时，默认单位vp。vp与px的比例与屏幕像素密度有关。

以屏幕相对像素为单位，表示设备针对应用的虚拟尺寸（与屏幕硬件本身的像素单位不同）。该单位提供了一种灵活的方法来适应不同屏幕密度的显示效果，通过使用虚拟像素，确保元素在不同密度的设备上具有一致的视觉效果。

[字体像素单位](../harmonyos-references/ts-types.md#fp10)：fp。字体像素大小默认情况下与 vp 相同，即默认情况下 1 fp = 1 vp。如果用户在设置中选择了更大的字体，字体的实际显示大小就会在vp的基础上乘以scale系数，即 1 fp = 1 vp \* scale。

[Percentage](../harmonyos-references/ts-types.md#percentage10) - 用于描述以%像素单位为单位的长度，如'10%'。

[Resource](../harmonyos-references/ts-types.md#resource) - 资源引用类型，用于设置组件属性的值。

可以通过$r或者$rawfile创建Resource类型对象，不可以修改Resource中的各属性的值。
