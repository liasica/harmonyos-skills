---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing-manual
title: 手动签名
breadcrumb: 指南 > 编写与调试应用 > 配置调试签名 > 手动签名
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c05530179d303fd4631811ba45373b19c5e94a721c142210c23382d17bd0a765
---

## 功能介绍

HarmonyOS应用/元服务通过数字证书（.cer文件）和Profile文件（.p7b文件）来保证应用/元服务的完整性。在申请调试证书和调试Profile文件前，需要通过DevEco Studio生成密钥（存储在格式为.p12的密钥库文件中）和证书请求文件（.csr文件）。

**基本概念**

* **密钥**：格式为.p12，包含非对称加密中使用的公钥和私钥，存储在密钥库文件中，公钥和私钥用于数字签名和验证。
* **证书请求文件**：格式为.csr，全称为Certificate Signing Request，包含密钥对中的公钥和通用名称、组织名称、组织单位等信息，用于向AppGallery Connect申请数字证书。
* **数字证书**：格式为.cer，由华为AppGallery Connect颁发。
* **Profile文件**：格式为.p7b，包含HarmonyOS应用/元服务的包名、数字证书信息、描述应用/元服务允许申请的证书权限列表，以及允许应用/元服务调试的设备列表（如果应用/元服务类型为Release类型，则设备列表为空）等内容，每个应用/元服务包中均必须包含一个Profile文件。

## 生成密钥和证书请求文件

**DevEco Studio 6.1.0 Beta2及以上版本**

1. 在主菜单栏单击**Build > Generate Key** **and CSR**。
2. 在**Generate Key** **and CSR**界面，可以单击**Select an existing key**选择已有的密钥库文件（存储有密钥的.p12文件），若没有密钥库文件则进行填写。下面以新创建密钥库文件为例进行说明。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/sKeXXQAlSca5VQuxZeVdBw/zh-cn_image_0000002731381991.png)
3. 在**Generate Key**窗口，填写密钥库信息后，点击**Next**。
   * **Keystore Name**：填写p12文件名称，仅允许包含字母、数字、下划线（\_）、中划线（-）、句号（.）。
   * **Select file save path**：设置密钥库文件存储路径。
   * **Key store password**：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。
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

     **说明** 

     First and last name、Organizational unit、Organization、City or locality、State or province填写要求小于64个字符，不可使用双引号（"）、斜杠（\）、反引号（`）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/VBFu_EWqQh6pJhEpjSQW0A/zh-cn_image_0000002701822684.png)
4. 在**Generate** **Certificate Request File (CSR)**窗口，设置CSR文件名和CSR文件存储路径后，点击**Finish**。
   * **CSR File Name**：填写CSR文件名称，仅允许包含字母、数字、下划线（\_）、中划线（-）、句号（.）。
   * **Select file save path**：设置CSR文件存储路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/-LLEm0mMSwyw-AUUHcl7OQ/zh-cn_image_0000002701662776.png)
5. 创建CSR文件成功，可以在存储路径下获取生成的密钥库文件（.p12）、证书请求文件（.csr）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/msWfk_LERZ-hLYdVJAMppA/zh-cn_image_0000002701822670.png "点击放大")

**DevEco Studio 6.1.0 Beta2以下版本**

1. 在主菜单栏单击**Build > Generate Key** **and CSR**。

   **说明** 

   如果本地已有对应的密钥，无需新生成密钥，可以在**Generate Key**界面中单击下方的Skip跳过密钥生成过程，直接使用已有密钥生成证书请求文件。
2. 在**Key store file**中，可以单击**Choose Existing**选择已有的密钥库文件（存储有密钥的.p12文件）；如果没有密钥库文件，单击**New**进行创建。下面以新创建密钥库文件为例进行说明。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/i0czqkT1QPi8BcEwb9i5sw/zh-cn_image_0000002701662766.png)
3. 在**Create Key Store**窗口，填写密钥库信息后，单击**OK**。
   * **Key store file**：设置密钥库文件存储路径，并填写p12文件名。
   * **Password**：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。
   * **Confirm password**：再次输入密钥库密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/Wop63M1nRFGpG0ismAitRw/zh-cn_image_0000002701662762.png)
4. 在**Generate Key** **and CSR**界面，继续填写密钥信息后，单击**Next**。
   * **Alias**：必填，别名，用于标识密钥名称。请记住该别名，后续签名配置需要使用。
   * **Password**：必填，密码，与密钥库密码保持一致，无需手动输入。
   * **Validity(years)：**选填，证书有效期，建议设置为25年及以上，覆盖应用/元服务的完整生命周期。
   * **First and last name：**选填，通用名称，可填写应用名称或开发者姓名等。
   * **Organizational unit**：选填，组织单位，可填写部门名称或个人开发等。
   * **Organization：**选填，组织名称，可填写公司全称或开发者姓名等。
   * **City or locality：**选填，城市或地区。
   * **State or province：**选填，州或省。
   * **Country code(XX)：**选填，[国家码](../app/agc-help-connect-api-appendix-countrycode-0000002236201362.md)。

   **说明** 

   First and last name、Organizational unit、Organization、City or locality、State or province要求：字符长度为（0，64），且不可使用双引号（"）、斜杠（\）、反引号（`）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/MVWbuh0iScW0Gc4UnwVSOA/zh-cn_image_0000002731541967.png)
5. 在**Generate Key** **and CSR**界面，设置CSR文件存储路径和CSR文件名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/QfCQAX7IRoiz44Tx1nLWiA/zh-cn_image_0000002701662770.png)
6. 单击**Finish**，创建CSR文件成功，可以在存储路径下获取生成的密钥库文件（.p12）、证书请求文件（.csr）和material文件夹（存放密码加密材料等）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/6obbTxFmQVGEnAw3Q18DXg/zh-cn_image_0000002701822698.png)

## 申请调试证书

使用上述生成的证书请求文件（.csr），在AGC中申请和下载调试证书，将生成的证书保存至本地，供申请调试Profile文件使用，具体请参考[申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)。

**说明** 

如您未在AGC中注册该应用，申请前需要在AGC中注册，具体请参考[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)。

## 申请调试Profile文件和添加权限信息

1. （可选）如需使用ACL权限，在AGC中[申请ACL权限](../app/agc-help-apply-acl-0000002394212138.md)。同时，在DevEco Studio配置文件中添加权限信息。

   **说明** 

   * 若应用因特殊场景要求使用受限开放权限，请务必在此步骤进行申请，否则应用将在审核时被驳回。受限开放权限可申请的特殊场景请参考[受限开放权限](restricted-permissions.md)。
   * 确保应用申请受限开放权限时提供的场景和功能信息准确。如果应用内使用的受限开放权限超出您申请的范围，或申请权限后使用的功能和场景超出可使用的范围，将影响应用上架。

   在需要使用权限的模块的module.json5（Stage模型）/config.json（FA模型）文件中添加“requestPermissions”/“reqPermissions”字段，并在字段下添加对应的权限名等信息，以在Stage模型工程中增加"ohos.permission.ACCESS\_DDK\_USB"权限为例。

   ```screen
   {
     "module": {
       ...
       "requestPermissions": [{
         "name": "ohos.permission.ACCESS_DDK_USB",
       }],
       ...
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Q3Pl0qxaTJqmDiGEHHPw9A/zh-cn_image_0000002701662754.png)
2. 使用上述生成的调试证书，在AGC中申请和下载Profile，将生成的Profile保存至本地，供配置签名使用，具体请参考[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。

## 配置签名信息

1. 在**File >** **Project Structure >** **Project > Signing Configs**窗口中，取消勾选“Automatically generate signature”和“Associate with registered application”，分别配置密钥(.p12文件)、Profile(.p7b文件)和数字证书(.cer文件)的路径等信息，配置完毕后点击**Apply**。
   * **Store file**：选择密钥库文件，文件后缀为.p12，该文件为[生成密钥和证书请求文件](ide-signing-manual.md#section1245916381106)中生成的.p12文件。
   * **Store password**：输入密钥库密码，该密码与[生成密钥和证书请求文件](ide-signing-manual.md#section1245916381106)中填写的密钥库密码保持一致。
   * **Key alias**：输入密钥的别名信息，与[生成密钥和证书请求文件](ide-signing-manual.md#section1245916381106)中填写的别名保持一致。
   * **Key password**：输入密钥的密码，与[生成密钥和证书请求文件](ide-signing-manual.md#section1245916381106)中填写的**Store Password**保持一致。
   * **Sign alg**：签名算法，固定为SHA256withECDSA。
   * **Profile file**：选择[申请调试Profile和添加权限信息](ide-signing-manual.md#section201901445352)中生成的Profile文件，文件后缀为.p7b。
   * **Certpath file**：选择[申请调试证书](ide-signing-manual.md#section294112511046)中生成的数字证书文件，文件后缀为.cer。

   **说明** 

   * Store file、Profile file、Certpath file三个字段支持配置相对路径，以项目根目录为起点，配置文件所在位置的路径名称。
   * 密钥库文件、密钥库密码、密钥别名、密钥密码、Profile文件、数字证书文件必须配套使用，否则会导致签名失败。若失败请根据报错信息进行修改，再进行签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/CMmWMdZXRaKcjDD3JNuh6Q/zh-cn_image_0000002701822686.png "点击放大")

   配置完成后，将鼠标悬停在**Provisioning Profile: DevEco Manage Profile**后![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/ksXs_lumTgutkq4nuqoh9w/zh-cn_image_0000002701662760.png)，可查看证书有效期、包名（bundle name）、企业名称（common name）、ACL权限（acl）、开放能力（capability）相关信息；或者进入工程级build-profile.json5文件，在“signingConfigs”下查看到配置成功的签名信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/O8Tfzwu5QhemQimqwPNb4Q/zh-cn_image_0000002701662758.png "点击放大")
2. 配置完成后，将鼠标悬停在**Provisioning Profile: DevEco Manage Profile**后![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/hopgga9vRS6qaIhTG7_p-w/zh-cn_image_0000002701822688.png)，可查看证书有效期、包名（bundle name）、企业名称（common name）、ACL权限（acl）、开放能力（capability）相关信息；或者进入工程级build-profile.json5文件，在“signingConfigs”下查看到配置成功的签名信息。

   点击右上角的“Run”按钮运行应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/CS5alsAlRaOfvmLzWcnOYQ/zh-cn_image_0000002731541939.png "点击放大")
