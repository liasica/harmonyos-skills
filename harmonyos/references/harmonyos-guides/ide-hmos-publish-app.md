---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-publish-app
title: 发布应用
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 发布应用
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:37+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:099ffcb3da9087baf01d30391b2b14e2949850d89541bc66c573347c8f4b4547
---

HarmonyOS通过数字证书与Profile文件等签名信息来保证应用/元服务的完整性，应用/元服务上架到AppGallery Connect必须通过签名校验。因此，您需要使用发布证书和Profile文件对应用/元服务进行签名后才能发布。

## 发布流程

开发者完成HarmonyOS应用/元服务开发后，需要将应用/元服务打包成App Pack（.app文件），用于上架到AppGallery Connect。发布应用/元服务的流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/L5EHfv4YQvmXCE6jgI2GMA/zh-cn_image_0000002749483566.png)

关于以上流程的详细介绍，请继续查阅本章节内容。

## 准备签名文件

HarmonyOS应用/元服务通过数字证书（.cer文件）和Profile文件（.p7b文件）来保证应用/元服务的完整性。在申请数字证书和Profile文件前，需要通过鸿蒙电脑DevEco Studio提前生成密钥（存储在格式为.p12的密钥库文件中）和证书请求文件（.csr文件）。

**基本概念**

* **密钥**：包含非对称加密中使用的公钥和私钥，存储在密钥库文件中，格式为.p12，公钥和私钥对用于数字签名和验证。
* **证书请求文件**：格式为.csr，全称为Certificate Signing Request，包含密钥对中的公钥和公共名称、组织名称、组织单位等信息，用于向AppGallery Connect申请数字证书。
* **数字证书**：格式为.cer，由华为AppGallery Connect颁发。
* **Profile文件**：格式为.p7b，包含HarmonyOS应用/元服务的包名、数字证书信息、描述应用/元服务允许申请的证书权限列表，以及允许应用/元服务调试的设备列表（如果应用/元服务类型为Release类型，则设备列表为空）等内容，每个应用/元服务包中均必须包含一个Profile文件。

### 生成密钥和证书请求文件

1. 在主菜单栏单击**构建** **> 生成密钥和证书请求文件**。
2. 在生成密钥和证书请求文件界面，可以单击Keystore File后的文件图标选择已有的密钥库文件（存储有密钥的.p12文件）。若没有密钥库文件，单击**新建**进行创建。下面以新建密钥库文件为例进行说明。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/NYp5vH9ZSBaMiyp8CxlwsQ/zh-cn_image_0000002779082629.png)
3. 在**创建密钥存储文件**窗口中，填写密钥库信息后，单击**确认**。
   * **Keystore file(\*.p12)**：填写p12文件名，仅允许包含字母、数字、下划线（\_）、中划线（-）、句号（.）。
   * **Key store path**：设置密钥库文件存储路径。
   * **Key store Password**：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。
   * **Confirm Password**：再次输入密钥库密码。
   * **Key alias**：密钥的别名信息，用于标识密钥名称。请记住该别名，后续签名配置需要使用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/nZlgL_dXQlSibp248OVMdQ/zh-cn_image_0000002779082633.png)
4. 在**生成密钥和证书请求文件**界面中，确认信息后点击**生成**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/bluWYSmJTLWJEeJk49rLzA/zh-cn_image_0000002749323692.png)
5. 创建CSR文件成功后，可以在存储路径下获取生成的密钥库文件（.p12）和证书请求文件（.csr）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/ea1CjmhLTv6l9ZYGt_ykkA/zh-cn_image_0000002749323696.png "点击放大")

### 申请发布证书和Profile文件

1. 创建HarmonyOS应用/元服务。在AGC中创建一个HarmonyOS应用/元服务，用于申请发布证书和Profile文件，具体请参考[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)和[创建元服务](../app/agc-help-create-atomic-service-0000002247795706.md)。
2. 申请发布证书和发布Profile文件。在AGC中申请、下载发布证书和Profile文件，具体请参考[申请发布证书](../app/agc-help-release-cert-0000002283336729.md)和[申请发布Profile](../app/agc-help-release-profile-0000002248341090.md)。
3. 申请完发布证书和发布Profile文件后，请在DevEco Studio中进行签名。

   **说明** 

   * 如果申请元服务的签名证书，在“创建应用”操作时，“是否元服务”选项请选择“**是**”。
   * 使用发布证书和发布Profile文件进行手动签名，只能用来打包应用上架，不能用来运行调试工程。

## 配置签名信息

使用制作的私钥（.p12）文件、在AppGallery Connect中申请的证书（.cer）文件和Profile（.p7b）文件，在DevEco Studio配置工程的签名信息，构建携带发布签名信息的APP。

在菜单栏单击**文件 > 项目结构 > ${default} > 签名配置**，分别配置密钥(.p12文件)、Profile(.p7b文件)和数字证书(.cer文件)的路径等信息，配置完毕后点击**生成签名文件**。

* **Keystore File**：选择密钥库文件，文件后缀为.p12。
* **Keystore Password**：输入密钥库密码。
* **Key Alias**：输入密钥的别名信息。
* **Key Password**：输入密钥的密码。
* **Profile File**：选择申请的发布Profile文件，文件后缀为.p7b。
* **Certpath File**：选择申请的发布数字证书文件，文件后缀为.cer。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/1Kd74YNvStSzrBus6fpB2Q/zh-cn_image_0000002779082631.png)

然后使用DevEco Studio生成APP，请参考[编译构建.app文件](ide-hmos-publish-app.md#section1992513343374)。

## 编译构建.app文件

**须知** 

应用上架时，要求应用包类型为Release类型。

打包APP时，DevEco Studio会将工程目录下的所有HAP/HSP模块打包到APP中，因此，如果工程目录中存在不需要打包到APP的HAP/HSP模块，请手动删除后再进行编译构建生成APP。

1. 单击**Build > Build APP(s)**，等待编译构建完成已签名的应用包。

   **说明** 

   当未指定[构建模式](ide-hmos-hvigor-compilation-options-customizing-guide.md#section192461528194916)时，构建APP包，默认Release模式；构建HAP/HSP/HAR包，默认Debug模式。即Build APP(s)，默认构建的APP包为Release类型，符合上架要求，开发者无需进行另外设置。
2. 编译构建完成后，可以在工程目录**build > outputs > default**下，获取带签名的应用包。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/ZGffCVo0Sce9cgxUzDvYqA/zh-cn_image_0000002749323694.png)

## 发布.app文件到应用市场

将HarmonyOS应用/元服务打包成.app文件后上架到应用市场，上架详细操作指导请参考[发布HarmonyOS应用](../app/agc-help-release-app-guide-0000002287176372.md)或[发布元服务](../app/agc-help-release-atomic-guide-0000002293651514.md)。
