---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-7
title: 如何开展MDM应用测试
breadcrumb: FAQ > 系统开发 > 基础功能 > 企业设备管理（MDM） > 如何开展MDM应用测试
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bbb9e204262628e1b0c1492381e80d7ed150fca548a056af8d7babe4f4a01f0c
---

## 问题现象

MDM应用开发进入测试阶段后，开发者在申请企业MDM应用发布证书及profile、运行、以及设备重置后自动部署场景中。

1. 申请企业MDM应用发布证书及profile。

   已申请了企业MDM应用发布证书及profile，在signingConfigs里面配置了企业MDM的证书和profile，但是应用编译后无法安装到手机中。报错如下：

   ```txt
   Install Failed: error: failed to install bundle.
   code:9568266
   error: install permission denied.
   ```
2. MDM应用激活。

   使用EMM控制台，添加了测试设备的SN，上传了测试应用的hap，设备重置后也成功下载了应用，但是应用无法获得设备管理权限。

## 背景知识

1. MDM应用开发需要[申请企业MDM应用发布证书和企业MDM应用发布profile](../app/agc-help-enterprise-mdm-profile-0000002248341094.md)。
2. MDM接口需要在激活企业设备管理扩展能力后使用，调试时仍需手动通过hdc命令来激活/解除激活扩展能力，参见[调试说明](../harmonyos-guides/mdm-kit-guide.md#调试说明)。

## 解决方案

1. MDM应用调试、测试阶段，可以正常[申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)，MDM应用的调试证书申请流程和普通APP一致，但是一定要先完成以下操作再申请调试证书：
   * [申请企业MDM应用发布证书](../app/agc-help-enterprise-mdm-cert-0000002283256801.md)，确认开发者账号已经有了MDM应用开发权限。
   * 申请企业MDM应用发布profile，在申请profile的时候勾选上“受限ACL权限”，然后在权限选择时选择MDM的相关权限。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/SG8khCOpRMmzldFzCswxjQ/zh-cn_image_0000002628774292.png "点击放大")
2. 使用调试证书打包出APP。由于MDM接口需要在激活企业设备管理扩展能力后使用，调试时仍需手动通过hdc命令来激活/解除激活扩展能力，因此APP安装后，需要通过命令行“hdc shell edm enable-admin”开启测试设备的MDM权限。
3. 若设备重置后未自动安装部署，需要检查EMM控制台的配置是否正确，最常见的错误是“设备型号”填错。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/wIie_8dxTVqGOBbMqBWGVA/zh-cn_image_0000002658973603.png "点击放大")

   “设备型号”请填写“型号代码”，比如ALN-AL00：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/BXd_Rq-SRPiJ4fyS1iEh-w/zh-cn_image_0000002628614394.png "点击放大")
4. 完成测试后，可使用“hdc shell edm disable-admin -n 包名”去激活。

## 常见FAQ

Q：为什么申请调试证书前，需要先申请发布证书？

A：因为申请发布证书时，会申请MDM权限，有了权限，调试证书才能正常工作。
