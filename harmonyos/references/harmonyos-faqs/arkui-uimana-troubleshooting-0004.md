---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-troubleshooting-0004
title: ArkUI平板自由多窗挖孔区避让问题定位
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 故障排查 > ArkUI平板自由多窗挖孔区避让问题定位
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:10+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:dfd0049ad58795475a1de42e2cf8f14679293248c4358a8c6bbde37bc6d33152
---

## 问题现象

应用在平板自由多窗模式下启动并最大化后，顶部被挖孔区遮挡。

## 定位过程

建议检查代码中module.json5中配置项是否添加了metadata配置项，将挖孔区添加为默认避让区域。

## 分析结论

代码中module.json5没有添加配置项metadata，导致挖孔区域未被视为避让区，页面默认不进行避让。

## 修改建议

在module.json5文件中增加配置项metadata，将挖孔区域视为非安全区，实现页面默认避让挖孔，具体可参考官方文档安全区域顶部的[说明](../harmonyos-references/ts-universal-attributes-expand-safe-area.md)，或参考官网[挖孔避让案例](../best-practices/bpta-multi-device-window-immersive.md#section35561799107)。
