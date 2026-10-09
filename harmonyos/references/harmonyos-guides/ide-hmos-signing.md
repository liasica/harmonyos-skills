---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-signing
title: 配置调试签名
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 配置调试签名
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:33+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:7a6bfd1338c7d6baa9c66d88af1fc31edf284df5085c358c76451e4a5b17a258
---

针对开发调试场景，鸿蒙电脑DevEco Studio提供[自动签名](ide-hmos-signing.md#section18815157237)和[手动签名](ide-hmos-signing.md#section297715173233)两种调试签名方式，帮助开发者高效进行应用调试。

自动签名适用于大部分调试场景，但部分调试场景须使用手动签名，具体为跨设备调试、跨应用交互调试、断网情况下调试、多用户共同开发且需要共享密钥、kit需要配置指纹。

**说明** 

使用自动签名前，请确保本地系统时间与北京时间（UTC/GMT +8.00）保持一致。如果不一致，将导致签名失败。

## 自动签名

1. 连接[本地真机设备](ide-run-device.md)后，开始签名。

   **说明** 

   如果同时连接多个设备，使用自动签名时，会同时将这多个设备的信息写到证书文件中。
2. （可选）在配置文件中添加ACL权限信息，ACL权限清单请参考[自动签名支持的ACL权限](restricted-permissions.md)。

   在需要使用权限的模块的module.json5文件中添加“requestPermissions”字段，并在字段下添加对应的权限名等信息，以增加"ohos.permission.ACCESS\_DDK\_USB"权限为例。

   ```screen
   {
     "module": {
       "requestPermissions": [{
         "name": "ohos.permission.ACCESS_DDK_USB",
       }],
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/8Hfh6MokRMCIyOwWVLxfvA/zh-cn_image_0000002778923009.png)

   **说明** 

   * 在调试签名时，不会强制校验配置文件中添加的ACL权限。
   * 涉及受限权限的应用，上架时，应用市场（AGC）将根据应用的使用场景审核是否可以使用对应的受限权限，如不符合，应用的上架申请将被驳回。在配置ACL权限前，请审视是否符合[受限权限的使用场景](restricted-permissions.md)。当前仅少量符合特殊场景的应用可在通过审批后，使用受限权限，申请方式请见[申请使用受限权限](declare-permissions-in-acl.md)。
3. 在菜单栏单击**文件 > 项目结构 > ${default} > 签名配置**，点击**Team**下拉框可以切换团队账号，点击**生成签名文件**按钮，即可完成签名。其中，default为产品的名称，与build-profile.json5文件中的[Products](ide-hvigor-build-profile-app.md#section45865492619)中"name"一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/KUI7EA88QaSeyNTv3yXwrQ/zh-cn_image_0000002749483790.png "点击放大")
4. 签名完成后如下图所示。

   进入工程级build-profile.json5文件，在“signingConfigs”下查看配置成功的签名信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/4vftQdTrTByl9Zk2nNuFKQ/zh-cn_image_0000002749323914.png "点击放大")

## 手动签名

HarmonyOS应用/元服务通过数字证书（.cer文件）和Profile文件（.p7b文件）来保证应用/元服务的完整性。在申请调试证书和调试Profile文件前，需要通过DevEco Studio生成密钥（存储在格式为.p12的密钥库文件中）和证书请求文件（.csr文件）。

**基本概念**

* **密钥**：格式为.p12，包含非对称加密中使用的公钥和私钥，存储在密钥库文件中，公钥和私钥用于数字签名和验证。
* **证书请求文件**：格式为.csr，全称为Certificate Signing Request，包含密钥对中的公钥和通用名称、组织名称、组织单位等信息，用于向AppGallery Connect申请数字证书。
* **数字证书**：格式为.cer，由华为AppGallery Connect颁发。
* **Profile文件**：格式为.p7b，包含HarmonyOS应用/元服务的包名、数字证书信息、描述应用/元服务允许申请的证书权限列表，以及允许应用/元服务调试的设备列表（如果应用/元服务类型为Release类型，则设备列表为空）等内容，每个应用/元服务包中均必须包含一个Profile文件。

### 生成密钥和证书请求文件

1. 在菜单栏单击**构建 > 生成密钥和证书请求文件**。
2. 在生成密钥和证书请求文件界面，可以单击Keystore File后的文件图标选择已有的密钥库文件（存储有密钥的.p12文件）。若本地没有密钥库文件，单击**新建**进行创建。下面以新建密钥库文件为例进行说明。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/Uusw5_4IQk2JtbW10W5ntw/zh-cn_image_0000002779082853.png "点击放大")
3. 在**创建密钥存储文件**窗口中，填写密钥库信息后，单击**确认**。
   * **Keystore file(\*.p12)**：填写p12文件名，仅允许包含字母、数字、下划线（\_）、中划线（-）、句号（.）。
   * **Keystore File**: 设置密钥库文件存储路径。
   * **Keystore** **Password**：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。
   * **Confirm Password**：再次输入密钥库密码。
   * **Key Alias**：密钥的别名信息。请记住该别名，后续签名配置需要使用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/6ZkN20SBTDyR3ypGTZXPUg/zh-cn_image_0000002749323920.png "点击放大")
4. 在**生成密钥和证书请求文件**界面，确认信息后点击**生成**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/PWlrGprSRjy72gtw2IU3bg/zh-cn_image_0000002749483794.png "点击放大")
5. 创建CSR文件成功后，可以在存储路径下获取生成的密钥库文件（.p12）、证书请求文件（.csr）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/bthzzV9NTciWRuzVQvL38g/zh-cn_image_0000002779082855.png)

### 申请调试证书

使用[生成密钥和证书请求文件](ide-hmos-signing.md#section462703710326)，在AGC中申请和下载调试证书，将生成的证书保存至本地，供申请调试Profile文件使用，具体请参考[申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)。

**说明** 

如您未在AGC中注册该应用，申请前需要在AGC中注册，具体请参考[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)。

### 申请调试Profile文件和添加权限信息

1. （可选）如需使用ACL权限，在AGC中[申请ACL权限](../app/agc-help-apply-acl-0000002394212138.md)。同时，在DevEco Studio配置文件中添加权限信息。

   **说明** 

   * 若应用因特殊场景要求使用受限开放权限，请务必在此步骤进行申请，否则应用将在审核时被驳回。受限开放权限可申请的特殊场景请参考[受限开放权限](restricted-permissions.md)。
   * 确保应用申请受限开放权限时提供的场景和功能信息准确。如果应用内使用的受限开放权限超出您申请的范围，或申请权限后使用的功能和场景超出可使用的范围，将影响应用上架。

   在需要使用权限的模块的module.json5文件中添加“requestPermissions”字段，并在字段下添加对应的权限名等信息，以增加"ohos.permission.ACCESS\_DDK\_USB"权限为例。

   ```screen
   {
     "module": {
       "requestPermissions": [{
         "name": "ohos.permission.ACCESS_DDK_USB",
       }],
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/-YUl2-uGQcSlp6GOmvpNpA/zh-cn_image_0000002778923003.png)
2. 使用[申请调试证书](ide-hmos-signing.md#section1723711253433)，在AGC中申请和下载Profile，将生成的Profile保存至本地，供配置签名使用，具体请参考[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。

### 配置签名信息

1. 在菜单栏单击**文件 > 项目结构 > ${default} > 签名配置**，分别配置密钥(.p12文件)、Profile(.p7b文件)和数字证书(.cer文件)的路径等信息，配置完毕后点击**生成签名文件**。
   * **Keystore File**：选择密钥库文件，文件后缀为.p12，该文件为[生成密钥和证书请求文件](ide-hmos-signing.md#section462703710326)中生成的.p12文件。
   * **Keystore Password**：输入密钥库密码，该密码与[生成密钥和证书请求文件](ide-hmos-signing.md#section462703710326)中填写的密钥库密码保持一致。
   * **Key Alias**：输入密钥的别名信息，与[生成密钥和证书请求文件](ide-hmos-signing.md#section462703710326)中填写的别名保持一致。
   * **Key Password**：输入密钥的密码，与[生成密钥和证书请求文件](ide-hmos-signing.md#section462703710326)中填写的**Keystore Password**保持一致。
   * **Profile File**：选择[申请调试Profile文件和添加权限信息](ide-hmos-signing.md#section15151840123413)中生成的Profile文件，文件后缀为.p7b。
   * **Certpath File**：选择[申请调试证书和调试Profile文件](ide-hmos-signing.md#section1723711253433)中生成的数字证书文件，文件后缀为.cer。

   **说明** 

   * Store file、Profile file、Certpath file三个字段支持配置相对路径，以项目根目录为起点，配置文件所在位置的路径名称。
   * 密钥库文件、密钥库密码、密钥别名、密钥密码、Profile文件、数字证书文件必须配套使用，否则会导致签名失败。若失败请根据报错信息进行修改，再进行签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/_GF1l799Rjq5WwXQBN2OUA/zh-cn_image_0000002779082849.png "点击放大")
2. 签名完成后，进入工程级build-profile.json5文件，在“signingConfigs”下查看配置成功的签名信息。
