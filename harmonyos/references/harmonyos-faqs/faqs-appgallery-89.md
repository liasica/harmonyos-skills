---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-89
title: p12和csr文件丢失后如何找回并更新应用
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > p12和csr文件丢失后如何找回并更新应用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b62fdf3421bac5ab7e2b0d58de84bd622cab1fc515fa6a29e2dea4bd6e287d8b
---

## 背景知识

HarmonyOS应用签名需要使用p12文件、cer文件和p7b文件。p7b文件是通过cer文件生成，cer文件是通过csr文件生成，csr文件是通过p12文件生成。可见最源头的文件是p12文件。

## 问题现象

项目原始的csr文件或p12文件丢失后是否可以找回？如何找回？后续如何更新应用？

## 解决方案

按照p12文件，csr文件，Alias，Password全部丢失或部分丢失有不同场景。

* **场景1：p12文件存在，Alias和Password存在，csr文件丢失；**

  如果仅仅丢失csr文件，可以通过IDE工具使用p12文件重新生成csr文件：

  1. 在主菜单栏单击Build > Generate Key and CSR，单击Choose Existing选择已有的p12文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/nRd-X3HJQ6iJExd2K_iMDA/zh-cn_image_0000002628554588.png)
  2. 输入Key store Password和Alias后，即可重新生成csr文件。
* **场景2：p12文件和csr文件存在，但Password或Alias丢失；**

  这种情况只能重新生成p12文件和csr文件，详细步骤可参考[生成密钥和证书请求文件](../harmonyos-guides/ide-signing.md#section462703710326)。
* **场景3：p12文件丢失，csr文件或Password或Alias存在；**

  由于签名必须使用p12文件，这种情况csr存在也失去作用，只能重新生成p12文件和csr文件，详细步骤可参考[生成密钥和证书请求文件](../harmonyos-guides/ide-signing.md#section462703710326)。

## 总结

1. 只要p12文件和对应的Alias，Password文件存在，都是可以重新生成csr文件，cer文件，p7b文件的，因此需要妥善保管p12文件和对应的Alias，Password文件。
2. 如果不慎丢失p12文件，只要应用的appid不发生变化，即AGC上未进行应用删除操作，也可以使用新的p12文件签名打包，更新应用时不会因为p12文件不一致导致更新失败。

## 常见FAQ

Q：更换p12文件后是否会影响用户更新版本，需要卸载老版本重新安装新版本？

A：只要应用在AGC的appid没发生变化，即没有进行过删除应用的操作，即使更换p12也不影响应用版本更新。
