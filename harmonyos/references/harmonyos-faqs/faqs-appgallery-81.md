---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-81
title: 证书和Profile类型及使用场景
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 证书和Profile类型及使用场景
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1d674af1ed70c0d6321988b985bc54ea5028b4bfd4be8c94430705a7e3329dcf
---

## 问题现象

编译HarmonyOS应用需要使用证书和Profile文件。证书和Profile有哪些类型？如何根据不同场景选择相应的证书和Profile类型？

## 背景知识

1. HarmonyOS软件包签名必须使用到证书和Profile文件，同时根据不同的安装方式，使用的证书和Profile类型也不同。
2. 根据不同的发布方式和设备类型，相应的证书和Profile类型也不同。通常Profile类型是根据证书类型不同做相应适配，证书类型和Profile类型是需要保持一致的。
3. 申请证书的通用步骤：
   * 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“证书、APP ID和Profile”。
   * 在左侧导航栏选择“证书、APP ID和Profile > 证书”，进入“证书”页面，点击“新增证书”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/FK4Scq5HRAyfsk1OxvDReg/zh-cn_image_0000002628554532.png "点击放大")
   * 在弹出的“新增证书”窗口选择证书类型，填写要申请的证书信息，点击“提交”。
4. 申请Profile的通用步骤：
   * 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“证书、APP ID和Profile”。
   * 在左侧导航栏选择“证书、APP ID和Profile > Profile”，进入“Profile”页面，点击右上角“添加”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/pPmbWfEYS-6W4gwCYkdXhA/zh-cn_image_0000002658913851.png "点击放大")
   * 在“添加Profile”页面，选择证书，根据证书类型选择Profile类型，填写应用名称、Profile名称等必填信息。

## 解决方案

按照安装方式，设备类型，账号类型，应用类型，上架类型等多个维度来阐述证书和Profile的类型和使用场景：

1. 调试证书和调试Profile。

   **适用场景**：本地调试应用。

   * 本地通过HDC命令即可安装的应用需要申请调试证书和调试Profile，登录AppGallery Connect申请证书时，弹窗界面证书类型选择“调试证书”，如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/anqMXRFPTS-BcU_NWwWKaQ/zh-cn_image_0000002658793911.png)
   * 调试证书除了登录AppGallery Connect手动申请，也可以通过DevEco Studio自动签名方式从AppGallery Connect申请。详细操作可参考[自动签名。](../harmonyos-guides/ide-signing.md#section18815157237)申请成功也可登录AppGallery Connect查看，证书名称以“auto\_debug”开头：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/IRGbY8yYSFaH0JwAEG6fAQ/zh-cn_image_0000002628394642.png "点击放大")
   * [申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)时，对应的证书类型选择“调试”。

   **注意** 

   每个账号最多可申请3个调试证书。

   一个应用最多可申请100个Profile文件。
2. 发布证书和发布Profile。

   **适用场景**：上架应用市场。包括正式上架，非公开发布，公开测试，邀请测试等。
   * HarmonyOS应用上架应用市场必须申请发布证书和发布Profile，登录AppGallery Connect申请证书时，弹窗界面证书类型选择“发布证书”，如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/1dL878vgRvidYvegS8n8dQ/zh-cn_image_0000002628554534.png)
   * [申请发布Profile](../app/agc-help-release-profile-0000002248341090.md)时，对应的证书类型选择“发布”；[申请指定设备发布Profile](../app/agc-help-internaltest-profile-0000002283260129.md)时，对应的证书类型也选择“发布”。

   **注意** 

   每个账号最多可申请3个发布证书。

   一个应用最多可申请100个Profile文件。
3. In-house发布证书和In-house发布Profile。

   **适用场景**：[发布In-house应用](../app/agc-help-inhouse-0000002281532696.md)。适用于在企业内部网络环境中分发专属应用给内部员工的场景，In-house应用不适合在任何公开渠道发布。
   * In-house应用打包需要申请In-house发布证书，登录AppGallery Connect申请证书时，弹窗界面证书类型选择“In-house发布证书”，如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/W3l_Eqa_RYWujCL82gIJQg/zh-cn_image_0000002658913853.png)
   * [申请In-house发布Profile](../app/agc-help-inhouse-profile-0000002283340021.md)时，对应的证书类型选择“In-house发布”；[申请指定设备发布Profile](../app/agc-help-internaltest-profile-0000002283260129.md)时，对应的证书类型也选择“In-house发布”。

   **注意** 

   In-house受限开放。使用In-house发布前，需要分别完成账号和应用权限申请，详情参考发布In-house应用[准备工作。](../app/agc-help-inhouse-0000002281532696.md#section6267104872410)

   每个账号仅可申请1个In-house发布证书。
4. 二进制证书。

   **适用场景**：涉及二进制程序，需使用华为颁发的二进制证书签名，才能在PC上正常运行。
   * 二进制程序需使用华为颁发的二进制证书签名，登录AppGallery Connect申请证书时，弹窗界面证书类型选择“二进制证书”，如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/gFQ5w0QVSmOhdGHfhipC2g/zh-cn_image_0000002658793913.png)

   **注意** 

   二进制证书目前为受限开放，如需体验可[申请开通权限](../app/agc-help-binary-cert-0000002408063605.md#section149371737114211)。

   二进制证书仅支持企业开发者使用，且每个账号最多可申请3个二进制证书。
5. 企业MDM应用发布证书和企业MDM应用发布Profile。

   **适用场景**：发布企业MDM应用。
   * 发布企业MDM应用时，需要使用企业MDM应用发布证书和企业MDM应用发布Profile手动签名后，才能编译构建正式发布包。登录AppGallery Connect申请证书时，弹窗界面证书类型选择“企业MDM应用发布证书”，如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/IQU0dDmoTwiQ4qg5Wiv87A/zh-cn_image_0000002628394644.png)
   * [申请企业MDM应用发布Profile](../app/agc-help-enterprise-mdm-profile-0000002248341094.md)时，对应的证书类型选择“企业MDM应用发布”。

   **注意** 

   企业MDM应用发布证书受限开放，需要满足[申请开通条件。](../app/agc-help-enterprise-mdm-cert-0000002283256801.md#section55531120183018)

   每个账号最多申请1个企业MDM应用发布证书。

   申请Profile类型选择“企业MDM应用发布”时，证书类型只能选择“企业MDM应用发布”。

## 常见FAQ

Q：In-house账号能否申请调试证书，进行本地HDC命令安装测试？

A：In-house账号可以申请“调试证书”和“调试Profile”构建软件包本地HDC命令安装，也可以申请“In-house发布证书”和“指定设备发布Profile”，构建的软件包也可以本地HDC命令安装。
