---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-54
title: 如何使用手动生成证书打包
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何使用手动生成证书打包
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:578c386738110c0e96248ca98f70b0d6a2482684033f2e98f32f5b3c645819d7
---

操作步骤：

1. 生成密钥和证书请求文件。

   在申请数字证书和Profile文件前，需使用DevEco Studio生成密钥和证书请求文件。

   * 密钥包含非对称加密中使用的公钥和私钥，存储在格式为.p12的密钥库文件中，用于数字签名和验证。
   * 证书请求文件格式为.csr，包含密钥对中的公钥和公共名称、组织名称、组织单位等信息，用于向AGC申请数字证书。
   1. 选择“Build > Generate Key and CSR”。
   2. 点击“Choose Existing”，选择已有的密钥库文件（.p12文件），然后跳转至步骤d继续配置。如果没有密钥库文件，点击“New”，跳转至步骤c进行创建。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/tev1ij5JSTW9gSsQ5Ufbxg/zh-cn_image_0000002229604337.png?HW-CC-KV=V1&HW-CC-Date=20260429T062031Z&HW-CC-Expire=86400&HW-CC-Sign=34D3343627D32D9E64B21B162FB7F9BB54EC92AF7C0896C24FBED6A0D73CEFB3 "点击放大")
   3. 在“Create Key Store”界面，填写密钥库信息后，点击“OK”。
      * Key store file：设置密钥库文件存储路径，填写p12文件名。
      * Password：设置密钥库密码。密码必须由大写字母、小写字母、数字和特殊符号中的两种以上字符组合，长度至少为8位。请记住该密码，后续签名配置时需要使用。
      * Confirm password：输入密钥库密码。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/bg_7l-CATISPQ8Mwpoy3GQ/zh-cn_image_0000002194158960.png?HW-CC-KV=V1&HW-CC-Date=20260429T062031Z&HW-CC-Expire=86400&HW-CC-Sign=9EC7A9CAD40384776FC4CF2EE43F378377201DE5517A95035D2AD6BEECBBBD71)
   4. 在“Generate Key and CSR”界面继续填写密钥信息后，点击“Next”。
      * Alias：密钥的别名，用于标识密钥。记住该别名，后续签名配置时需要使用。
      * Password：密钥对应的密码。
      * Validity：证书有效期，建议设置为25年。
      * Certificate：输入证书基本信息。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/sjfN0J_DR16rdBm6r7MqwA/zh-cn_image_0000002194318588.png?HW-CC-KV=V1&HW-CC-Date=20260429T062031Z&HW-CC-Expire=86400&HW-CC-Sign=9225DB5307E1991F3BA2BF8F220C0DF6C238AE39BCC7B35E50DFD10B2C59F21B)
   5. 在“Generate Key and CSR”界面设置CSR文件存储路径和文件名，然后点击“Finish”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/rBacRdLdTaqKQHnR1BCL6g/zh-cn_image_0000002194318568.png?HW-CC-KV=V1&HW-CC-Date=20260429T062031Z&HW-CC-Expire=86400&HW-CC-Sign=5936ECEA561CB2C0FCA8344B24F6003360675812EB98E43F282D12B75A494207)

      CSR文件创建成功后，将在存储路径下生成密钥库文件（.p12）和证书请求文件（.csr）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/IHhhALAqTh615QJKapNnIQ/zh-cn_image_0000002229604369.png?HW-CC-KV=V1&HW-CC-Date=20260429T062031Z&HW-CC-Expire=86400&HW-CC-Sign=D7E067354E35CEEE94EE5C9DB124C21885E33676945C4C7E34AC77F68CE8E770)
2. 申请调试证书，用于配置HarmonyOS应用/元服务的签名信息，保障软件代码完整性和发布者身份真实性。证书格式为.cer，包含公钥和证书指纹。
   1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)。选择“用户与访问”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/fUDrXEkoSEK2hNw0HnFF7Q/zh-cn_image_0000002229604361.png?HW-CC-KV=V1&HW-CC-Date=20260429T062031Z&HW-CC-Expire=86400&HW-CC-Sign=027BF3FBE48B670A148AEEA68D43BFAED1DCAF725E30DC104138684BB93BD6A7 "点击放大")
   2. 选择“证书管理”，点击“新增证书”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/z2hEqCluRhy8WuPLvDy-IA/zh-cn_image_0000002229758837.png?HW-CC-KV=V1&HW-CC-Date=20260429T062031Z&HW-CC-Expire=86400&HW-CC-Sign=1262088907A7DBF0A7E5F10E2385D93BAB30A7900133536DC48693BE8A66E8C2 "点击放大")
   3. 填写要申请的证书信息，点击“提交”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/qF4ZGmuvSxiNyWaYRVx12w/zh-cn_image_0000002194318560.png?HW-CC-KV=V1&HW-CC-Date=20260429T062031Z&HW-CC-Expire=86400&HW-CC-Sign=58C4E2330CDA5EF1B3CA90E6C88A2017D0E988EB660F29C52F0C3AF19EDE097D "点击放大")
   4. 证书申请成功后，展示证书名称、证书类型和失效日期。点击“下载”，保存证书至本地。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/AIAovwlVSZmYP-0bQXCnvg/zh-cn_image_0000002229604345.png?HW-CC-KV=V1&HW-CC-Date=20260429T062031Z&HW-CC-Expire=86400&HW-CC-Sign=A2692EDCCF863D6B2679DBDFE6AA8AE97523D1855F03492C8BB7F2E6EDE9E2AC "点击放大")
3. 注册调试设备。
   1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，选择“用户与访问”。
   2. 选择“设备管理”，点击右上角的“添加设备”，填写设备信息，点击“提交”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/Ha1DbUZwQLSSg3h_oUiTyg/zh-cn_image_0000002194318576.png?HW-CC-KV=V1&HW-CC-Date=20260429T062031Z&HW-CC-Expire=86400&HW-CC-Sign=21201F5F618CFDF6698D5D61C4AD6C59122AB6F2EAA2F3E0DD2F207EA63F2935 "点击放大")
   3. 设备添加成功后，您可以在“设备管理”页面查看设备的名称、类型和UDID。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/PZrIaeC_SgqLR9N45GUw-Q/zh-cn_image_0000002229758833.png?HW-CC-KV=V1&HW-CC-Date=20260429T062031Z&HW-CC-Expire=86400&HW-CC-Sign=23C48CC5CCE4F565168FEBF2019C0B4413B18F667AD1C430CBC2FA44B7A6CF22 "点击放大")
   4. 如需删除调试设备，勾选一个或多个设备，点击“批量删除设备”，在弹出窗口中点击“确认”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/RboTQ666T9-jsJn0eaHznQ/zh-cn_image_0000002229758845.png?HW-CC-KV=V1&HW-CC-Date=20260429T062031Z&HW-CC-Expire=86400&HW-CC-Sign=BCF59FA8B128A3792EE30BC3B6845561E7371998D5298339523B4503CA616D9C "点击放大")
4. 申请调试Profile。
   1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，选择“我的项目”。
   2. 找到项目，点击创建的HarmonyOS应用或元服务。
   3. 选择“HarmonyOS应用 > HAP Provision Profile管理”，点击右上角“添加”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/KBGGgSiMRf6jUJGjTaZTig/zh-cn_image_0000002194158952.png?HW-CC-KV=V1&HW-CC-Date=20260429T062031Z&HW-CC-Expire=86400&HW-CC-Sign=0AD5D02A9B4D0900AE79D8EA0BA0C733D3406AAB3A6BB62472E7C5B2B09FA4CF "点击放大")
   4. 在弹出的“HarmonyAppProvision信息”窗口中添加调试Profile，完成后点击“提交”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/OWkpuzNPSd6U_J_94GmkSw/zh-cn_image_0000002229604365.png?HW-CC-KV=V1&HW-CC-Date=20260429T062031Z&HW-CC-Expire=86400&HW-CC-Sign=DF778F8B6ECCD3DB1ED755B0395B15957097AADE9520E8B7C099BC849ABDE500 "点击放大")
   5. 调试Profile申请成功后，展示Profile信息。点击“下载”，保存Profile至本地。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/wbnv4JhPSje9WHkAb7GyKA/zh-cn_image_0000002194318580.png?HW-CC-KV=V1&HW-CC-Date=20260429T062031Z&HW-CC-Expire=86400&HW-CC-Sign=B839D5DA2FED23E0EFC502BBF4697BFAAABA836219C572301A04C0EA2D691258 "点击放大")
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

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Ur1Ka76eRpW-vM2PMyfcNg/zh-cn_image_0000002194318556.png?HW-CC-KV=V1&HW-CC-Date=20260429T062031Z&HW-CC-Expire=86400&HW-CC-Sign=5FD3BE9FB0DDA488AA8DA3A0B136FAD5F0A76970243B2629FAD3F81970677436 "点击放大")

**参考链接**

[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)
