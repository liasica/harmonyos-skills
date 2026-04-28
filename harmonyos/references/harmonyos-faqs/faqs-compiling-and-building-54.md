---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-54
title: 如何使用手动生成证书打包
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何使用手动生成证书打包
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0a5a944598014e6064d97e4b8c77b1012faf36a491731745a41ae1e633144661
---

操作步骤：

1. 生成密钥和证书请求文件。

   在申请数字证书和Profile文件前，需使用DevEco Studio生成密钥和证书请求文件。

   * 密钥包含非对称加密中使用的公钥和私钥，存储在格式为.p12的密钥库文件中，用于数字签名和验证。
   * 证书请求文件格式为.csr，包含密钥对中的公钥和公共名称、组织名称、组织单位等信息，用于向AGC申请数字证书。
   1. 选择“Build > Generate Key and CSR”。
   2. 点击“Choose Existing”，选择已有的密钥库文件（.p12文件），然后跳转至步骤d继续配置。如果没有密钥库文件，点击“New”，跳转至步骤c进行创建。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/tev1ij5JSTW9gSsQ5Ufbxg/zh-cn_image_0000002229604337.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=A0028F1C03E1353C210E1B7D42ED5CB39B636B3F29AC3A0088E32B7F587D2E9D "点击放大")
   3. 在“Create Key Store”界面，填写密钥库信息后，点击“OK”。
      * Key store file：设置密钥库文件存储路径，填写p12文件名。
      * Password：设置密钥库密码。密码必须由大写字母、小写字母、数字和特殊符号中的两种以上字符组合，长度至少为8位。请记住该密码，后续签名配置时需要使用。
      * Confirm password：输入密钥库密码。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/bg_7l-CATISPQ8Mwpoy3GQ/zh-cn_image_0000002194158960.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=8EC6678E4DFEC2125E68BB4461F1F517CFC1D5C7F591957EEBFA5E13535F5ACF)
   4. 在“Generate Key and CSR”界面继续填写密钥信息后，点击“Next”。
      * Alias：密钥的别名，用于标识密钥。记住该别名，后续签名配置时需要使用。
      * Password：密钥对应的密码。
      * Validity：证书有效期，建议设置为25年。
      * Certificate：输入证书基本信息。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/sjfN0J_DR16rdBm6r7MqwA/zh-cn_image_0000002194318588.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=D4D724DEB474670EC93531191724588C72BAA75A77035753EE80F9357D7F5CE2)
   5. 在“Generate Key and CSR”界面设置CSR文件存储路径和文件名，然后点击“Finish”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/rBacRdLdTaqKQHnR1BCL6g/zh-cn_image_0000002194318568.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=CAFB8B0A72E831F36A4AFAA955B3F9100B93DF041008706FF0DA0DE99478AF3A)

      CSR文件创建成功后，将在存储路径下生成密钥库文件（.p12）和证书请求文件（.csr）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/IHhhALAqTh615QJKapNnIQ/zh-cn_image_0000002229604369.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=BB942EDAB043754F7380AE38751F80C55851EC10A53AEC18E61F3951EAB6B1ED)
2. 申请调试证书，用于配置HarmonyOS应用/元服务的签名信息，保障软件代码完整性和发布者身份真实性。证书格式为.cer，包含公钥和证书指纹。
   1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)。选择“用户与访问”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/fUDrXEkoSEK2hNw0HnFF7Q/zh-cn_image_0000002229604361.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=B5B8D14D60701E5A6E41139BC0CC2AD5AE02BB432BC0DE852F2EB6DCB27A6854 "点击放大")
   2. 选择“证书管理”，点击“新增证书”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/z2hEqCluRhy8WuPLvDy-IA/zh-cn_image_0000002229758837.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=717C4A97B91A89A0E2D1D27B7F543CFE3B23D8B93CDCE18241F3E236ED657B44 "点击放大")
   3. 填写要申请的证书信息，点击“提交”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/qF4ZGmuvSxiNyWaYRVx12w/zh-cn_image_0000002194318560.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=5BD04716D5B027F2E744BC40A6B409F9D0F52B29073B244B658BF772794A915F "点击放大")
   4. 证书申请成功后，展示证书名称、证书类型和失效日期。点击“下载”，保存证书至本地。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/AIAovwlVSZmYP-0bQXCnvg/zh-cn_image_0000002229604345.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=8AE25C2D144824C8A4E080CA2C0785758F9C3C6E6AFBC832C56595B192E7A773 "点击放大")
3. 注册调试设备。
   1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，选择“用户与访问”。
   2. 选择“设备管理”，点击右上角的“添加设备”，填写设备信息，点击“提交”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/Ha1DbUZwQLSSg3h_oUiTyg/zh-cn_image_0000002194318576.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=6CAFEB9E2D2753A7E3F55845DC030B2EE039B976D7863CE6145FF5C48A9B7A35 "点击放大")
   3. 设备添加成功后，您可以在“设备管理”页面查看设备的名称、类型和UDID。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/PZrIaeC_SgqLR9N45GUw-Q/zh-cn_image_0000002229758833.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=74124BCB3FA1EA7728DD4F5C6235F33E170F353334C80D162AC9BDDAF4060254 "点击放大")
   4. 如需删除调试设备，勾选一个或多个设备，点击“批量删除设备”，在弹出窗口中点击“确认”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/RboTQ666T9-jsJn0eaHznQ/zh-cn_image_0000002229758845.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=CB2DBD71B0FF81BE832BA8DDAF53ECCE6E9B38F4BC08955A928AAA13D38897FA "点击放大")
4. 申请调试Profile。
   1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，选择“我的项目”。
   2. 找到项目，点击创建的HarmonyOS应用或元服务。
   3. 选择“HarmonyOS应用 > HAP Provision Profile管理”，点击右上角“添加”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/KBGGgSiMRf6jUJGjTaZTig/zh-cn_image_0000002194158952.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=C327454A0975EA064D6790B7825344FF1CAF5CCB4BBEE36AE776864A707B8538 "点击放大")
   4. 在弹出的“HarmonyAppProvision信息”窗口中添加调试Profile，完成后点击“提交”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/OWkpuzNPSd6U_J_94GmkSw/zh-cn_image_0000002229604365.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=53F1E2A49BB920BB84D9D4CCB9A281FAC369FB71F5DF472C6ACA976F908269DD "点击放大")
   5. 调试Profile申请成功后，展示Profile信息。点击“下载”，保存Profile至本地。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/wbnv4JhPSje9WHkAb7GyKA/zh-cn_image_0000002194318580.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=B4B9318E2148D7150D00367E01998AAEB3FBCEA748622027B36E789495AB166C "点击放大")
5. 手动配置签名信息。
   1. 打开DevEco Studio，选择“File > Project Structure”，进入“Project Structure”界面。
   2. 导航到“Project”，点击“Signing Configs”页签。取消勾选“Automatically generate signature”（如果是API 8和9工程，还需勾选“Support HarmonyOS”），填写相关信息，然后点击“OK”。
      * Store File：选择生成的.p12文件。
      * Store Password：密钥库密码，需与生成密钥和证书请求文件时设置的密码一致。
      * Key alias：密钥别名，需与生成密钥和证书请求文件时设置的别名一致。
      * Key password：设置的密钥密码，需与生成密钥和证书请求文件时的密码一致。
      * Sign alg：设置为“SHA256withECDSA”。
      * Profile file：选择.p7b文件。
      * Certpath file：选择.cer文件。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Ur1Ka76eRpW-vM2PMyfcNg/zh-cn_image_0000002194318556.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=B065605BFFF996C9A9939DB7B90D782D989AFC48919A518C43345CFF737184E7 "点击放大")

**参考链接**

[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)
