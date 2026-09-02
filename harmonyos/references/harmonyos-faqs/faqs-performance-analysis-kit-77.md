---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-77
title: 开启VPN后访问https资源报错，如何导出日志信息定界问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 开启VPN后访问https资源报错，如何导出日志信息定界问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5119f011027b8871a4d3fe3a0f43c8cd8468b8e00d9bf26d9b90437cbfdc3b0c
---

## 问题现象

打开VPN后，在内置浏览器打开https资源，服务器下发的证书校验失败，请问如何导出日志信息定位问题？

## 解决方案

1. 分析是否访问的地址服务器证书配置异常，建议检查服务器证书。
   * 其他平台上同样的VPN是否可以正常访问。
   * 导出证书，看下手机设置是否有预置相应的根证书。
   * HarmonyOS手机上其他网站浏览器是否可以正常访问，HarmonyOS手机上其他三方应用是否可以正常访问，如果三方应用可以访问，但浏览器不能访问，则需要导出netlog分析日志信息。
2. netlog导出方法：
   * 在设备上打开浏览器输入：hwbrowser://net-export。
   * 点击Start Logging to Disk，此时会开始记录用户当前在浏览器里的行为。然后在新标签页访问网站并做相关操作，操作完成后再返回此页面点击Stop Logging。
   * 结束后show file把arkweb-net-export-log.json导出。
