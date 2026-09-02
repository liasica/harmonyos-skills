---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-5
title: 设置应用水印策略时报401错误及尺寸限制的解决方法
breadcrumb: FAQ > 系统开发 > 基础功能 > 企业设备管理（MDM） > 设置应用水印策略时报401错误及尺寸限制的解决方法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:dcd682b731a14a1c5f544a1ec5056a7e521ea4d41d6fd2221838ee7c3ae3bb38
---

## 问题现象

* 场景一：使用[securityManager.setWatermarkImage](../harmonyos-references/js-apis-enterprise-securitymanager.md#securitymanagersetwatermarkimage14)为指定用户的指定应用设置水印策略时，一直报401错误。
* 场景二：使用[securityManager.setWatermarkImage](../harmonyos-references/js-apis-enterprise-securitymanager.md#securitymanagersetwatermarkimage14)设置水印策略时，水印生成和下发时画布/图片尺寸会被限制在350x350范围内，导致部分配置无法真实生效。

## 背景知识

[securityManager.setWatermarkImage](../harmonyos-references/js-apis-enterprise-securitymanager.md#securitymanagersetwatermarkimage14)：为指定用户的指定应用设置水印策略。本接口适用于企业场景下为三方应用设置水印，降低企业信息泄露风险。不建议为系统应用设置水印（如：桌面应用），可能存在未知异常。

[securityManager.setScreenWatermarkImage](../harmonyos-references/js-apis-enterprise-securitymanager.md#securitymanagersetscreenwatermarkimage)：设置屏幕水印策略，可规避350x350的尺寸限制。该接口在API Version 26及以上版本生效。

[应用沙箱路径和真实物理路径的对应关系](../harmonyos-guides/app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系)：在应用沙箱路径下读写文件，经过映射转换，实际读写的是真实物理路径中的应用文件。

## 问题定位

* 场景一：

  有问题的操作步骤如下：设置水印的方法参考[securityManager.setWatermarkImage](../harmonyos-references/js-apis-enterprise-securitymanager.md#securitymanagersetwatermarkimage14)接口示例，将图片来源换成沙箱图片。

  accountId和source参数填写错误是出现401错误的常见原因，参考以下步骤排查：

  1. accountId参数不能传不存在的用户id，可以通过[getOsAccountLocalId](../harmonyos-references/js-apis-osaccount.md#getosaccountlocalid9-1)获取。
  2. source参数表示图像路径或者image.PixelMap对象。
  + 图像路径为应用沙箱路径(应用沙箱路径和真实路径的对应关系可参见:[应用沙箱路径和真实物理路径的对应关系](../harmonyos-guides/app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系))等应用有权限访问的路径。
  + image.PixelMap表示图像对象，图像像素占用大小不得超过500KB。

  经过上述排查，将图片存放至物理路径：/data/app/el1//base//test.png，并在传参时使用对应的沙箱路径：/data/storage/el1/base/test.png，问题得以解决。
* 场景二：

  屏幕水印链路存在350x350的尺寸限制，水印生成和下发时画布/图片尺寸会被限制在350x350范围内，导致超出该尺寸的水印配置无法真实生效。可通过调用[securityManager.setScreenWatermarkImage](../harmonyos-references/js-apis-enterprise-securitymanager.md#securitymanagersetscreenwatermarkimage)接口设置屏幕水印策略来解决此问题。

## 分析结论

* 场景一：
  1. 正确设置接口的accountId参数，不能传不存在的用户id。
  2. source参数表示图像路径或者image.PixelMap对象，需要将图片存入正确的物理路径，并保证图像像素占用大小不得超过500KB。
* 场景二：

  屏幕水印链路对水印图片尺寸存在350x350的限制，导致超出该尺寸的水印配置无法真实生效。可改用[securityManager.setScreenWatermarkImage](../harmonyos-references/js-apis-enterprise-securitymanager.md#securitymanagersetscreenwatermarkimage)接口设置屏幕水印策略来解决此问题。

## 修改建议

* 场景一：

  将图片存放至物理路径：/data/app/el1//base//test.png，并在传参时使用对应的沙箱路径：/data/storage/el1/base/test.png。
* 场景二：

  改用[securityManager.setScreenWatermarkImage](../harmonyos-references/js-apis-enterprise-securitymanager.md#securitymanagersetscreenwatermarkimage)接口设置屏幕水印策略。该接口在API Version 26及以上版本生效，请在此版本上验证。
