---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/package-structure-faq-0007
title: 应用安装到设备方式常见问题
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 常见问题 > 应用安装到设备方式常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:45+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:a14a44fb70ff17916fc7482ba970efde9630fa552e5f8f08612bad8a02242145
---

**Q：应用安装到设备的方式有哪些？**

**A**：支持两种方式安装HAP包到设备：

* 通过hdc命令安装：hdc install xxx.hap。
* 将.app文件上架到应用市场后，通过应用市场将HAP分发部署到设备中。

参考链接：[发布应用（APP）](../app/agc-help-releaseharmony-0000001933963166.md)。

**Q：如何实现应用侧载？**

**A**：目前不支持侧载（直接安装包体）的方式，需通过应用市场上架流程进行安装。具体流程参考[发布应用](../guidebook/develop-once-deploy-everwhere-7-1-0000002625192371.md)。
