---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-publish-app
title: 发布应用
breadcrumb: 指南 > 发布应用 > 发布应用
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:939bf4b33964076589954abfa8abacf86234ff9be2aa6050de65e318f2686fbc
---

HarmonyOS通过数字证书与Profile文件等签名信息来保证应用/元服务的完整性，应用/元服务上架到AppGallery Connect（AGC）必须通过签名校验。因此，您需要使用发布证书和Profile文件对应用/元服务进行签名后才能发布。

从DevEco Studio 6.1.0 Beta2版本开始，准备签名文件时生成密钥和证书请求文件界面发生变更，以及上传软件包页面新增Build Version字段。

## 发布流程

开发者完成HarmonyOS应用/元服务开发后，需要将应用/元服务打包成App Pack（.app文件），用于上架到AppGallery Connect。发布应用/元服务的流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/jT-Ne7SgTSCtDp15TdPXSw/zh-cn_image_0000002561833593.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=698F690374242B2B872220429991451818C7CFC188D764BB1A53F4740D2D914A)

关于以上流程的详细介绍，请继续查阅本章节内容。

## 准备签名文件

HarmonyOS应用/元服务通过数字证书（.cer文件）和Profile文件（.p7b文件）来保证应用/元服务的完整性。在申请数字证书和Profile文件前，需要提前生成密钥（存储在格式为.p12的密钥库文件中）和证书请求文件（.csr文件）。

**基本概念**

* **密钥**：包含非对称加密中使用的公钥和私钥，存储在密钥库文件中，格式为.p12，公钥和私钥对用于数字签名和验证。
* **证书请求文件**：格式为.csr，全称为Certificate Signing Request，包含密钥对中的公钥和公共名称、组织名称、组织单位等信息，用于向AppGallery Connect申请数字证书。
* **数字证书**：格式为.cer，由AppGallery Connect颁发。
* **Profile文件**：格式为.p7b，包含HarmonyOS应用/元服务的包名、数字证书信息、描述应用/元服务允许申请的证书权限列表，以及允许应用/元服务调试的设备列表（如果应用/元服务类型为Release类型，则设备列表为空）等内容，每个应用/元服务包中均必须包含一个Profile文件。

### 生成密钥和证书请求文件

当前支持通过DevEco Studio和[CertificateTool](ide-publish-app.md#section72897415171)两种方式生成密钥和证书请求文件。

说明

CertificateTool生成密钥和证书请求文件的操作界面与DevEco Studio 6.1.0 Beta2及之后版本一致，文档以DevEco Studio进行说明。

使用CertificateTool生成时，操作界面中各选项的含义和填写要求请参考DevEco Studio 6.1.0 Beta2及之后版本。

**DevEco Studio 6.1.0 Beta2及之后版本**

1. 在主菜单栏单击**Build > Generate Key** **and CSR**。

   说明

   如果本地已有对应的密钥，无需新生成密钥，可以在**Generate Key**界面中单击下方的Skip跳过密钥生成过程，直接使用已有密钥生成证书请求文件。
2. 填写密钥库文件，若已有的密钥库文件（存储有密钥的.p12文件），单击**Select an existing key**进行选择。下面以新创建密钥库文件为例进行说明。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/4NFZywL1Qv65c1U0ps0xsw/zh-cn_image_0000002565405209.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=475F07163EB925242B42339D6212F2955B22C0CCFD286A132B4F3C339B2BDC5B)
3. 在**Generate Key**窗口，填写密钥库信息后，点击**Next**。
   * **Keystore Name**：填写p12文件名称，仅允许包含字母、数字、下划线（\_）、中划线（-）、句点（．）。
   * **Select file save path**：设置密钥库文件存储路径。
   * **Key store Password**：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。
   * **Confirm password**：再次输入密钥库密码。
   * **Alias**：密钥别名。请记住该别名，后续签名配置需要使用。
   * **Advance Setting**：密钥库文件的高级设置，选填。
     + **Validity(years)：**选填，证书有效期，建议设置为25年及以上，覆盖应用/元服务的完整生命周期。
     + **First and last name：**选填，通用名称，可填写应用名称或开发者姓名等。
     + **Organizational unit**：选填，组织单位，可填写部门名称或个人开发等。
     + **Organization：**选填，组织名称，可填写公司全称或开发者姓名等。
     + **City or locality：**选填，城市或地区。
     + **State or province：**选填，州或省。
     + **Country code(XX)：**选填，[国家码](../app/agc-help-connect-api-appendix-countrycode-0000002236201362.md)。

     说明

     First and last name、Organizational unit、Organization、City or locality、State or province填写要求小于64个字符，不可使用双引号（"）、单引号（`）、斜杠（\）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/K0ti5YoFT8-cmW62Rien6Q/zh-cn_image_0000002534325388.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=878C519FF8F93CFFA63CFFA48CDC98E25241992DF6685AAFF624B53759D4F168)
4. 在**Generate** **Certificate Request File (CSR)**窗口，设置CSR文件名和CSR文件存储路径后，点击**Finish**。
   * **CSR File Name**：填写CSR文件名称，仅允许包含字母、数字、下划线（\_）、中划线（-）、句点（．）。
   * **Select file save path**：设置CSR文件存储路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/03zP7xyLSBGWiYCyALtczw/zh-cn_image_0000002534485342.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=7E280F8F7B3682F1A34915793657039F36C9E928A6FFA6DCD24693B7F2B9EEFF)
5. 创建CSR文件成功，可以在存储路径下获取生成的密钥库文件（.p12）、证书请求文件（.csr）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/jaf4mXG3TnSsX31kE4xFfA/zh-cn_image_0000002565365229.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=53FA69EDF9DBC0D1848049DE63C2544D7659844A53DAD20D9548F6C3AC12CC90)

**DevEco Studio 6.1.0 Beta2之前版本**

1. 在主菜单栏单击**Build > Generate Key** **and CSR**。

   说明

   如果本地已有对应的密钥，无需新生成密钥，可以在**Generate Key**界面中单击下方的Skip跳过密钥生成过程，直接使用已有密钥生成证书请求文件。
2. 在**Key Store File**中，可以单击**Choose Existing**选择已有的密钥库文件（存储有密钥的.p12文件）；如果没有密钥库文件，单击**New**进行创建。下面以新创建密钥库文件为例进行说明。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/ZUzIzXtdQFutlJ1XpOXiMQ/zh-cn_image_0000002561753607.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=B47C07EB5C8A0C177287D7BC9988D8A15B791A7AA57BE1C15D436330713F52E2 "点击放大")
3. 在**Create Key Store**窗口中，填写密钥库信息后，单击**OK**。
   * **Key Store File**：设置密钥库文件存储路径，并填写p12文件名。
   * **Password**：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。
   * **Confirm Password**：再次输入密钥库密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/8hcm_4sLRfixHgmKquPj-g/zh-cn_image_0000002530753650.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=1831DF7BC9E034F566AF97F849F30E8A056FC27A5229752A681BCF2D74966BF9 "点击放大")
4. 在**Generate Key** **and CSR**界面中，继续填写密钥信息后，单击**Next**。
   * **Alias**：必填，别名，用于标识密钥名称。请记住该别名，后续签名配置需要使用。
   * **Password**：必填，密码，与密钥库密码保持一致，无需手动输入。
   * **Validity(years)：**选填，证书有效期，建议设置为25年及以上，覆盖应用/元服务的完整生命周期。
   * **First and last name：**选填，通用名称，可填写应用名称或开发者姓名等。字符长度为（0，64），且不可使用（双引号）"、（斜杠）\、（反引号）`。
   * **Organizational unit**：选填，组织单位，可填写部门名称或个人开发等。字符长度为（0，64），且不可使用（双引号）"、（斜杠）\、（反引号）`。
   * **Organization：**选填，组织名称，可填写公司全称或开发者姓名等。字符长度为（0，64），且不可使用（双引号）"、（斜杠）\、（反引号）`。
   * **City or locality：**选填，城市或地区。字符长度为（0，64），且不可使用（双引号）"、（斜杠）\、（反引号）`。
   * **State or province：**选填，州或省。字符长度为（0，64），且不可使用（双引号）"、（斜杠）\、（反引号）`。
   * **Country code(XX)：**选填，[国家码](../app/agc-help-connect-api-appendix-countrycode-0000002236201362.md)。

   说明

   First and last name、Organizational unit、Organization、City or locality、State or province要求：字符长度为（0，64），且不可使用（双引号）"、（斜杠）\、（反引号）`。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/ICz3KG_ASDeTt2w3zsH6AQ/zh-cn_image_0000002561833571.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=6CF65EE47F0F693C3862D56EEAB2A2BC531D9766AC98021618F2A615F8907252)
5. 在**Generate Key** **and CSR**界面，设置CSR文件存储路径和CSR文件名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/ZoU7-lCaR6aCjbCstM2ZjQ/zh-cn_image_0000002530753672.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=3AA05D2CE8BEA58125296FCEBFB0248068F39FC18F805E198B37C3BD617FBAED "点击放大")
6. 单击**OK**按钮，创建CSR文件成功，可以在存储路径下获取生成的密钥库文件（.p12）和证书请求文件（.csr）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/DFVvxnf4TC--qUv71kzOpg/zh-cn_image_0000002530913658.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=27B7F21FA868EC42D15DE45CFB528E49F8A60BB7A8CBC7C57EABFAEF37DE393D)

### 申请发布证书和发布Profile文件

1. 创建HarmonyOS应用/元服务。在AGC中创建一个HarmonyOS应用/元服务，用于申请发布证书和Profile文件，具体请参考[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)和[创建元服务](../app/agc-help-create-atomic-service-0000002247795706.md)。
2. 申请发布证书和发布Profile文件。在AGC中申请、下载发布证书和Profile文件，具体请参考[申请发布证书](../app/agc-help-release-cert-0000002283336729.md)和[申请发布Profile](../app/agc-help-release-profile-0000002248341090.md)。
3. 申请完发布证书和发布Profile文件后，请在DevEco Studio中进行签名，具体请参考[配置签名信息](ide-publish-app.md#section280162182818)。

   说明

   * 如果申请元服务的签名证书，在“创建应用”操作时，“是否元服务”选项请选择“**是**”。
   * 使用发布证书和发布Profile文件进行手动签名，只能用来打包应用上架，不能用来运行调试工程。

## 配置签名信息

使用制作的私钥（.p12）文件、在AppGallery Connect中申请的证书（.cer）文件和Profile（.p7b）文件，在DevEco Studio配置工程的签名信息，构建携带发布签名信息的APP。

在**File >** **Project Structure >** **Project > Signing Configs** **> default**界面中，取消勾选“Automatically generate signature”和“Associate with registered application”，分别配置密钥(.p12文件)、Profile(.p7b文件)和数字证书(.cer文件)的路径等信息。

* **Store File**：选择密钥库文件，文件后缀为.p12。
* **Store Password**：输入密钥库密码。
* **Key Alias**：输入密钥的别名信息。
* **Key Password**：输入密钥的密码。
* **Sign Alg**：签名算法，固定为SHA256withECDSA。
* **Profile File**：选择申请的发布Profile文件，文件后缀为.p7b。
* **Certpath File**：选择申请的发布数字证书文件，文件后缀为.cer。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/Skm4qG02QBOSHO9ZCbvXjA/zh-cn_image_0000002561833579.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=F34A469F807CDE5DB22D8B193749D18017372791F7EA9548433456E7CE88A48F "点击放大")

设置完签名信息后，单击**OK**进行保存，然后使用DevEco Studio生成APP，请参考[编译构建.app文件](ide-publish-app.md#section1992513343374)。

## （条件必选）更新公钥指纹

当应用需要使用以下开放能力的一种或多种时，发布应用前，需在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中将调试应用的指纹更新为发布证书指纹。具体操作请参见[配置公钥指纹](../app/agc-help-cert-fingerprint-0000002278002933.md)。

* Account Kit（华为账号服务）
* Game Service Kit（游戏服务）
* Health Service Kit（运动健康服务）
* IAP Kit（应用内支付服务）
* Map Kit（地图服务）
* Payment Kit（华为支付服务）
* Wallet Kit（钱包服务）

## 编译构建.app文件

注意

应用上架时，要求应用包类型为Release类型。

打包APP时，DevEco Studio会将工程目录下的所有HAP/HSP模块打包到APP中，因此，如果工程目录中存在不需要打包到APP的HAP/HSP模块，请手动删除后再进行编译构建生成APP。

1. 单击**Build > Build Hap(s)/APP(s) > Build APP(s)**，等待编译构建完成已签名的应用包。

   说明

   当未指定[构建模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)时，构建APP包，默认Release模式；构建HAP/HSP/HAR包，默认Debug模式。

   即**Build APP(s)**时，默认构建的APP包为Release类型，符合上架要求，开发者无需进行另外设置。
2. 编译构建完成后，可以在工程目录**build > outputs > default**下，获取带签名的应用包。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/e1_hj7udSZ-zX6Q0U6S8cA/zh-cn_image_0000002530913642.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=A241F2ED0045BF4308979B99552FD26A09D4DD954BF3ADA6292460252DE48FFA)

## 上传软件包

DevEco Studio 5.0.5.200版本开始，支持在DevEco Studio内上传应用软件包。上传软件包前，请先[创建应用](../app/agc-help-create-app-0000002247955506.md)。

### 约束与限制

* 该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
* 该功能将会把您的应用包传至App Gallery Connect用于测试或上架。为了您的信息安全，请勿上传带有个人敏感信息的数据（如密码、源代码、私钥、调试安装包、业务日志等信息）。
* 仅Build Mode为Release的应用支持上传软件包，且确保软件包已配置Release签名。
* 同时支持通过[App Gallery Connect上传软件包](../app/agc-help-release-app-upload-pkg-0000002277983368.md)。

### 操作步骤

1. 在DevEco Studio菜单栏，点击**Build > Upload Product。**若未登录，请点击**Sign in**登录华为开发者账号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/pE8RZ3tVTOGpNuqz5BEdKg/zh-cn_image_0000002530753658.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=8F4DD7693D69416CF49014A6DF8BFAE5EFD512BD0643841A28F56B3B4E86754D "点击放大")
2. 登录成功后，返回DevEco Studio进入软件包上传界面。确认当前工程的product信息，选择需要上传的软件包类型，点击**OK**开始上传。
   * 若当前上传的软件包仅做测试发布，请选择**Generate app package and upload it to AppGallery Connect for test**。
   * 若软件包需要在全网正式发布，请选择**Generate app package and upload it to AppGallery Connect for test and publish**。

   说明

   * 如需上传符号表信息，请勾选**Upload your app's symbols**选项。
   * 上传的product可以通过点击DevEco Studio编辑区域右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/ODpi2xo-T_CkUJ3GvuZvXw/zh-cn_image_0000002530913668.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=66C6709792DD246A430673664EA91C32458D712F26AFC9F31C62C3B364C1331C)图标进行查看及切换。
   * 可通过app.json5中bundleName/versionName字段修改当前product对应的包名/版本号信息。必须使用当前开发者账号下已在AppGallery注册且真实存在的包名。
   * Build Version值由AGC计算后回传填入。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/luzA4jvVQuGyx_V99T2wmQ/zh-cn_image_0000002561833585.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=803B561AAC738E1C6398FAE1C6DC4FD8ED3C78B51E42E77097AC3E9A9222FB02)
3. 上传完成后，出现云测试的结果，点击**View Full result in AppGallery Connect**可进入AGC查看软件包上传记录和检测结果，具体请参考[上传软件包](../app/agc-help-release-app-upload-pkg-0000002277983368.md)。点击**Close**关闭上传页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/23ELd0s6RYiOQElbi7xcUQ/zh-cn_image_0000002530913650.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=12B48265D3DB1DD151FD0153F2C7D06BF7DD7D3E69B5AEF6FED448C732674D29)

## 发布.app文件到应用市场

将HarmonyOS应用/元服务打包成.app文件后上架到应用市场，发布详细操作指导请参考[发布HarmonyOS应用](../app/agc-help-release-app-0000002271695230.md)或[发布元服务](../app/agc-help-release-atomic-0000002327731065.md)。

## 附录

### CertificateTool下载

| 平台 | 包名 | 版本号 | SHA256校验码 | 更新时间 |
| --- | --- | --- | --- | --- |
| Windows(64-bit) | [certificate-tool-windows-x64-1.0.0.1.zip](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/92/v3/aqVWHUspRTO9BJKZ-5NULQ/certificate-tool-windows-x64-1.0.0.1.zip?HW-CC-KV=V1&HW-CC-Date=20260420T021601Z&HW-CC-Expire=315360000&HW-CC-Sign=71B0174C33B7E64463BA3D3E0530998CF4FDEB56D80C6F177BAED3E8E7488750) | 1.0.0.1 | dee6c2ae3b300fd7450bbeb2aadd96f1099ee5235ae627afcfad9b3ed3ded7da | 2026/04/20 |
| Mac(64-bit) | [certificate-tool-mac-x64-1.0.0.1.zip](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/bc/v3/l9egptIHRIyxS4tM_SPzuQ/certificate-tool-mac-x64-1.0.0.1.zip?HW-CC-KV=V1&HW-CC-Date=20260420T021701Z&HW-CC-Expire=315360000&HW-CC-Sign=A3B7F4BA42F7790DDA25A916B3EEFDDA52C905DCCE85D362AF4A576F152FFC67) | 1.0.0.1 | 8afc53e6714cb7e8840114065012b5f706c265c056491c240e5433be311bf084 | 2026/04/20 |
| Mac(ARM64) | [certificate-tool-mac-arm64-1.0.0.1.zip](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/90/v3/TeaUV0NbSvSx15zqhZRY0Q/certificate-tool-mac-arm64-1.0.0.1.zip?HW-CC-KV=V1&HW-CC-Date=20260420T021801Z&HW-CC-Expire=315360000&HW-CC-Sign=604E5AA8AFCCE2FF2127308E0F94B0830DB8E52C24DFF0AA5E0118E55EAAA878) | 1.0.0.1 | 07283684624b11c2db0c2ce2654729b5114b3085df68736a43967eda247a7b4e | 2026/04/20 |
