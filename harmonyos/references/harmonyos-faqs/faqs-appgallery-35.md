---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-35
title: 应用内点击检查更新跳转到应用市场后提示“此应用暂不支持在当前设备安装”
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 应用内点击检查更新跳转到应用市场后提示“此应用暂不支持在当前设备安装”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e8b0e4e3f51ff6c2701eaa775e1fe3f3e3af4ba79a7e444c9ebe1432b3d1b49a
---

## 问题现象

在应用内提供了检查更新按钮，点击后跳转到应用市场，显示“此应用暂不支持在当前设备安装”。

## 解决方案

* 问题原因1：目标应用未在HarmonyOS NEXT应用市场上架。此场景一般出现在上架调试、邀请测试场景。

  解决方案：需通过华为应用市场查看目标应用是否已上架；若应用未适配，需按HarmonyOS NEXT规范升级并重新发布。
* 问题原因2：若应用已经正式上架，仍然出现这个问题，需排查是否跳转链接使用错误。

  解决方案：在应用内使用链接形式跳转到应用市场，id建议使用bundleName。

  ```screen
  store://appgallery.huawei.com/app/detail?id= + bundleName。
  ```

  如果使用了appId,为兼容旧链接，可以在appId前拼接大写的C。如下所示：

  ```screen
  store://appgallery.huawei.com/app/detail?id=C123456。
  ```

## 总结

推荐使用官方文档提供的方式实现[应用市场更新功能](../harmonyos-guides/store-update.md)。
