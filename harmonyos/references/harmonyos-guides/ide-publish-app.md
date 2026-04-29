---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-publish-app
title: 发布应用
breadcrumb: 指南 > 发布应用 > 发布应用
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c1cfc937ab2d8df94a20bf2a368c9d26bf0c0fcba16c4e0ad183d63f0415a9eb
---

HarmonyOS通过数字证书与Profile文件等签名信息来保证应用/元服务的完整性，应用/元服务上架到AppGallery Connect（AGC）必须通过签名校验。因此，您需要使用发布证书和Profile文件对应用/元服务进行签名后才能发布。

从DevEco Studio 6.1.0 Beta2版本开始，准备签名文件时生成密钥和证书请求文件界面发生变更，以及上传软件包页面新增Build Version字段。

## 发布流程

开发者完成HarmonyOS应用/元服务开发后，需要将应用/元服务打包成App Pack（.app文件），用于上架到AppGallery Connect。发布应用/元服务的流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/7q6e601gRl2f3-7HjQSxjQ/zh-cn_image_0000002561833593.png?HW-CC-KV=V1&HW-CC-Date=20260429T054746Z&HW-CC-Expire=86400&HW-CC-Sign=E1791386E9295C1040C039951EF1502F524F58D4FEA5A3E89F4593D2A1CBA745)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/cYAoMQ1pSVyeNKg3Gd7xAA/zh-cn_image_0000002565405209.png?HW-CC-KV=V1&HW-CC-Date=20260429T054746Z&HW-CC-Expire=86400&HW-CC-Sign=99B8764E20D143B7EA577F7DDC5B9FA9162A97F8B6108E875FF7F1637F54618B)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/TQhO4wjlQ_WCKOCl8DPlJw/zh-cn_image_0000002534325388.png?HW-CC-KV=V1&HW-CC-Date=20260429T054746Z&HW-CC-Expire=86400&HW-CC-Sign=9AAC3FB4EEB7E72CFC6B56ABA38F1714E3652E206D5E874B8EFEF9BAC0622401)
4. 在**Generate** **Certificate Request File (CSR)**窗口，设置CSR文件名和CSR文件存储路径后，点击**Finish**。
   * **CSR File Name**：填写CSR文件名称，仅允许包含字母、数字、下划线（\_）、中划线（-）、句点（．）。
   * **Select file save path**：设置CSR文件存储路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/hNpMB05EQtimFR36QoefCA/zh-cn_image_0000002534485342.png?HW-CC-KV=V1&HW-CC-Date=20260429T054746Z&HW-CC-Expire=86400&HW-CC-Sign=763D056108998F25C6A8D43E6A3E2B0BB4573C0FD28A902E78F7A1F7F47729B0)
5. 创建CSR文件成功，可以在存储路径下获取生成的密钥库文件（.p12）、证书请求文件（.csr）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/7F1nfhMsSoSlYSXN5Qs_Cw/zh-cn_image_0000002565365229.png?HW-CC-KV=V1&HW-CC-Date=20260429T054746Z&HW-CC-Expire=86400&HW-CC-Sign=AA80445151DA16EA1BDFD9D99C6D495AFB739118E353926DE320D2AB81BC5FC6)

**DevEco Studio 6.1.0 Beta2之前版本**

1. 在主菜单栏单击**Build > Generate Key** **and CSR**。

   说明

   如果本地已有对应的密钥，无需新生成密钥，可以在**Generate Key**界面中单击下方的Skip跳过密钥生成过程，直接使用已有密钥生成证书请求文件。
2. 在**Key Store File**中，可以单击**Choose Existing**选择已有的密钥库文件（存储有密钥的.p12文件）；如果没有密钥库文件，单击**New**进行创建。下面以新创建密钥库文件为例进行说明。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/ZZU17K_aTFK6xPgCbwY-Uw/zh-cn_image_0000002561753607.png?HW-CC-KV=V1&HW-CC-Date=20260429T054746Z&HW-CC-Expire=86400&HW-CC-Sign=52942514BF3EF7789AB9DA7A138996C843E296C590C8AC33EAA22EA1EBD86D5A "点击放大")
3. 在**Create Key Store**窗口中，填写密钥库信息后，单击**OK**。
   * **Key Store File**：设置密钥库文件存储路径，并填写p12文件名。
   * **Password**：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。
   * **Confirm Password**：再次输入密钥库密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/5jeNZ5CHQ6q1XLFmsiTzHw/zh-cn_image_0000002530753650.png?HW-CC-KV=V1&HW-CC-Date=20260429T054746Z&HW-CC-Expire=86400&HW-CC-Sign=9CC70043A1DDD1F6B86B34CCB4797E35CE91190BDA331D78C4C6B857B260AFCF "点击放大")
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/ZlvdWR0mS-K9GBgp_pOifg/zh-cn_image_0000002561833571.png?HW-CC-KV=V1&HW-CC-Date=20260429T054746Z&HW-CC-Expire=86400&HW-CC-Sign=F4089B36FFC7E2B94339ADB46ABC6A6FA6417580040D504A7623862F6CF14DA8)
5. 在**Generate Key** **and CSR**界面，设置CSR文件存储路径和CSR文件名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/cDFcW4t9S76kCNPJocnJXg/zh-cn_image_0000002530753672.png?HW-CC-KV=V1&HW-CC-Date=20260429T054746Z&HW-CC-Expire=86400&HW-CC-Sign=D35A68FA034DF1DD3F992C6889BE01E50371B9A2C54EC2B5DC18611A1794471C "点击放大")
6. 单击**OK**按钮，创建CSR文件成功，可以在存储路径下获取生成的密钥库文件（.p12）和证书请求文件（.csr）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/gHQXCx1JTfaEUCpOAgatRA/zh-cn_image_0000002530913658.png?HW-CC-KV=V1&HW-CC-Date=20260429T054746Z&HW-CC-Expire=86400&HW-CC-Sign=675CD7EEDDF91CFD40E9797030AEB2F862B1813E0404C16BC8400C0AA0ED371B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/po9wdtX8SsaJvGbIE1fKyA/zh-cn_image_0000002561833579.png?HW-CC-KV=V1&HW-CC-Date=20260429T054746Z&HW-CC-Expire=86400&HW-CC-Sign=D6FE452232AA7123FA5E4FCC07969B4078B5D6202ACBF9A3192C6BD0EE6F8130 "点击放大")

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/VUSlRHhkSbuIinRNyLZnNg/zh-cn_image_0000002530913642.png?HW-CC-KV=V1&HW-CC-Date=20260429T054746Z&HW-CC-Expire=86400&HW-CC-Sign=10251E6B623E9C9D568EECB9EC4E06D49B23F6B40D76376226093FCF57343DB4)

## 上传软件包

DevEco Studio 5.0.5.200版本开始，支持在DevEco Studio内上传应用软件包。上传软件包前，请先[创建应用](../app/agc-help-create-app-0000002247955506.md)。

### 约束与限制

* 该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
* 该功能将会把您的应用包传至App Gallery Connect用于测试或上架。为了您的信息安全，请勿上传带有个人敏感信息的数据（如密码、源代码、私钥、调试安装包、业务日志等信息）。
* 仅Build Mode为Release的应用支持上传软件包，且确保软件包已配置Release签名。
* 同时支持通过[App Gallery Connect上传软件包](../app/agc-help-release-app-upload-pkg-0000002277983368.md)。

### 操作步骤

1. 在DevEco Studio菜单栏，点击**Build > Upload Product。**若未登录，请点击**Sign in**登录华为开发者账号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/8XJqfXntRUS218ygmyQQcA/zh-cn_image_0000002530753658.png?HW-CC-KV=V1&HW-CC-Date=20260429T054746Z&HW-CC-Expire=86400&HW-CC-Sign=8802BA37A0382051A7A84EC3759460ABF262AAFDB0DA6F199D5EDA899BB2D4FF "点击放大")
2. 登录成功后，返回DevEco Studio进入软件包上传界面。确认当前工程的product信息，选择需要上传的软件包类型，点击**OK**开始上传。
   * 若当前上传的软件包仅做测试发布，请选择**Generate app package and upload it to AppGallery Connect for test**。
   * 若软件包需要在全网正式发布，请选择**Generate app package and upload it to AppGallery Connect for test and publish**。

   说明

   * 如需上传符号表信息，请勾选**Upload your app's symbols**选项。
   * 上传的product可以通过点击DevEco Studio编辑区域右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/MqColTapSnKcHdal-QyEaQ/zh-cn_image_0000002530913668.png?HW-CC-KV=V1&HW-CC-Date=20260429T054746Z&HW-CC-Expire=86400&HW-CC-Sign=A8E39F5D92FF8C26B5FB0971739EF207925932D1F7DC6DE18FFD3142ABDA288E)图标进行查看及切换。
   * 可通过app.json5中bundleName/versionName字段修改当前product对应的包名/版本号信息。必须使用当前开发者账号下已在AppGallery注册且真实存在的包名。
   * Build Version值由AGC计算后回传填入。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/27Otuv2tRqaIl0QyNW8pgA/zh-cn_image_0000002561833585.png?HW-CC-KV=V1&HW-CC-Date=20260429T054746Z&HW-CC-Expire=86400&HW-CC-Sign=A6644FF2C596F6B3BAC09651E74255E2A5294E902EDD5CB2A097C287787EA5A5)
3. 上传完成后，出现云测试的结果，点击**View Full result in AppGallery Connect**可进入AGC查看软件包上传记录和检测结果，具体请参考[上传软件包](../app/agc-help-release-app-upload-pkg-0000002277983368.md)。点击**Close**关闭上传页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/V7eKk0Y5RLyqc-ejpqJtxw/zh-cn_image_0000002530913650.png?HW-CC-KV=V1&HW-CC-Date=20260429T054746Z&HW-CC-Expire=86400&HW-CC-Sign=5FDD52ED77D4BCA5CC2A2BC394F7AD1ECB5B8A2E3788FDAA5E42B7E3A8DB2645)

## 发布.app文件到应用市场

将HarmonyOS应用/元服务打包成.app文件后上架到应用市场，发布详细操作指导请参考[发布HarmonyOS应用](../app/agc-help-release-app-0000002271695230.md)或[发布元服务](../app/agc-help-release-atomic-0000002327731065.md)。

## 附录

### CertificateTool下载

| 平台 | 包名 | 版本号 | SHA256校验码 | 更新时间 |
| --- | --- | --- | --- | --- |
| Windows(64-bit) | [certificate-tool-windows-x64-1.0.0.1.zip](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/92/v3/aqVWHUspRTO9BJKZ-5NULQ/certificate-tool-windows-x64-1.0.0.1.zip?HW-CC-KV=V1&HW-CC-Date=20260420T021601Z&HW-CC-Expire=315360000&HW-CC-Sign=71B0174C33B7E64463BA3D3E0530998CF4FDEB56D80C6F177BAED3E8E7488750) | 1.0.0.1 | dee6c2ae3b300fd7450bbeb2aadd96f1099ee5235ae627afcfad9b3ed3ded7da | 2026/04/20 |
| Mac(64-bit) | [certificate-tool-mac-x64-1.0.0.1.zip](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/bc/v3/l9egptIHRIyxS4tM_SPzuQ/certificate-tool-mac-x64-1.0.0.1.zip?HW-CC-KV=V1&HW-CC-Date=20260420T021701Z&HW-CC-Expire=315360000&HW-CC-Sign=A3B7F4BA42F7790DDA25A916B3EEFDDA52C905DCCE85D362AF4A576F152FFC67) | 1.0.0.1 | 8afc53e6714cb7e8840114065012b5f706c265c056491c240e5433be311bf084 | 2026/04/20 |
| Mac(ARM64) | [certificate-tool-mac-arm64-1.0.0.1.zip](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/90/v3/TeaUV0NbSvSx15zqhZRY0Q/certificate-tool-mac-arm64-1.0.0.1.zip?HW-CC-KV=V1&HW-CC-Date=20260420T021801Z&HW-CC-Expire=315360000&HW-CC-Sign=604E5AA8AFCCE2FF2127308E0F94B0830DB8E52C24DFF0AA5E0118E55EAAA878) | 1.0.0.1 | 07283684624b11c2db0c2ce2654729b5114b3085df68736a43967eda247a7b4e | 2026/04/20 |
