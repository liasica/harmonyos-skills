---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing
title: 配置调试签名
breadcrumb: 指南 > 编写与调试应用 > 配置调试签名
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:38+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0ff16e0d2c59936a950a89f92ae62969731d2da35252992278886c477d5bfd73
---

针对开发调试场景，DevEco Studio为开发者提供了[自动签名](ide-signing.md#section18815157237)方案，帮助开发者高效进行调试。此外，也可以选择[手动签名](ide-signing.md#section297715173233)方式生成调试签名。

## 使用场景说明

* 自动签名仅用于调试场景，方便开发者进行应用调试。部分调试场景下必须使用手动签名：
  1. 当需要进行跨设备调试、跨应用交互调试、断网情况下调试或者多用户共同开发且需要共享密钥时，必须使用[手动签名](ide-signing.md#section297715173233)。
  2. 如果开发过程中使用到需要审批的权限时，例如：
     1. 使用部分不支持自动签名的[受限开放权限](restricted-permissions.md)时，必须使用[手动签名](ide-signing.md#section297715173233)。支持自动签名的ACL权限清单请参见[自动签名支持的ACL权限](ide-signing.md#section5301916183411)。
     2. 需要华为业务方审核的权限时（例如华为账号一键登录等），必须使用手动签名。
  3. 若kit需要配置指纹，建议使用手动签名。
* 发布场景必须使用手动签名。

## 自动签名

DevEco Studio 6.0.0 Beta3及之前版本，自动签名未关联注册的应用。从DevEco Studio 6.0.0 Beta5版本开始，自动签名新增关联注册应用的方式，签名操作界面新增“**Associate with registered application**”选项。

* 关联注册应用的自动签名：与应用市场（AppGallery Connect，简称AGC）的应用绑定，可在DevEco Studio开通[开放能力](../app/agc-help-create-app-0000002247955506.md#section1817619495251)。
* 未关联注册应用的自动签名：未与应用市场的应用绑定，不支持在DevEco Studio开通开放能力。

### 约束与限制

* 关联注册应用进行签名仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
* 元服务的自动签名属于关联注册应用进行签名，元服务自动签名仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
* 使用自动签名前，请确保本地系统时间与北京时间（UTC/GMT+08:00）保持一致。如果不一致，将导致签名失败。

### 关联注册应用

**操作步骤**

1. 连接真机设备或模拟器，具体请参考[使用本地真机运行应用/元服务](ide-run-device.md)或[使用模拟器运行应用/元服务](ide-run-emulator.md)，真机连接成功后如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/YoibSeiaQdCzEDjloQZRIQ/zh-cn_image_0000002530912982.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=D9E831F4AB2FE7F1EDCDE1B8DB836C569710CCC4CFF36DB255A8A0E02B4DC9D3)

   说明

   如果同时连接多个设备，则使用自动化签名时，会同时将这多个设备的信息写到证书文件中。
2. 进入**File > Project Structure... > Project > Signing Configs**界面，勾选“**Associate with registered application**”。如果未登录，请先点击**Sign In**进行登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/aAakaatdRl6Usb9w7CNiAA/zh-cn_image_0000002530752994.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=40022AC2FB6FCE4B1C01E04D67994FB2011C0961F004FD14765C6A97D10901C7 "点击放大")

   说明

   * 点击**Team**下拉框，可以切换团队账号。
   * 开始签名后，DevEco Studio根据Bundle name查询该团队在AGC上同包名的应用。若在AGC查询到应用，则进行自动签名；若在AGC未查询到应用或应用冲突，请根据提示信息修改后重新自动签名，具体修改请参考[常见问题](../harmonyos-faqs/faqs-signature-service-18.md)。
3. 点击**Enable open capabilities**，在DevEco Studio上开通[开放能力](../app/agc-help-create-app-0000002247955506.md#section1817619495251)。当前支持开通如下四种开放能力：Push Kit（[推送服务](push-kit-introduction.md)）、Device status detection（[应用设备状态检测](devicesecurity-deviceverify-develop.md)）、Map Kit（[地图服务](map-introduction.md)）、Safety Detect（[安全检测服务](devicesecurity-safetydetect-develop.md)），应用根据需要进行勾选。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/16h-UOPhSxugEdxNvKslJg/zh-cn_image_0000002530913000.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=BBDD42D189E4965A9A361BB1ADD4B6833FC041D8DEBAFA6A14917DE7527D166A)
4. （可选）在配置文件中添加ACL权限信息，ACL权限清单请参考[自动签名支持的ACL权限](ide-signing.md#section5301916183411)。

   在需要使用权限的模块的module.json5（Stage模型）/config.json（FA模型）文件中添加“requestPermissions”/“reqPermissions”字段，并在字段下添加对应的权限名等信息。以下示例为在Stage模型工程中增加"ohos.permission.ACCESS\_DDK\_USB"权限。

   ```
   1. {
   2. "module": {
   3. ...
   4. "requestPermissions": [{
   5. "name": "ohos.permission.ACCESS_DDK_USB",
   6. }],
   7. ...
   8. }
   9. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/Gje44sRLQ2WR5NlbLAaR0w/zh-cn_image_0000002530752988.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=67E7BB08150F40812DAD1837B4159F1752139D57AE41AFC0355FDEC52BEA73E9)

   修改配置文件后点击**OK**，若应用已在AGC申请该权限则签名成功；若应用未申请该权限，会导致签名失败，点击Notice弹窗中"**submit a permission request in AppGallery Connect**"或"**Submit**"，跳转至AGC申请权限，然后再返回DevEco Studio界面重新签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/0scEegpvT9CYwkRp2rvCAA/zh-cn_image_0000002561752937.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=C4DCDCCAE47A2A0BF4D251D44C2F578F6117CB6461EC07178F0B70B01E9D8D87 "点击放大")

   说明

   * 申请ACL前注意事项：
     + 在申请ACL权限前，请审视是否符合[受限权限的使用场景](restricted-permissions.md)。当前仅少量符合特殊场景的应用可在通过审批后，使用受限权限。申请方式请见[申请使用受限权限](declare-permissions-in-acl.md)。
     + 涉及受限权限的应用，在上架时，应用市场（AGC）将根据应用的使用场景审核是否可以使用对应的受限权限。如不符合，应用的上架申请将被驳回，审核方式请见[发布HarmonyOS应用](../app/agc-help-release-app-0000002271695230.md)。
   * 申请ACL后Profile证书说明：
     + 在ACL权限申请审批完成前，可获得一个有效期较短的临时Profile证书，使应用完成签名。临时证书到期后，若申请仍未审批通过，签名时需再次申请和再次获取临时证书。
     + 在ACL权限申请审批完成后，可获取一个有效期较长的正式Profile证书。
5. 签名完成后，在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b）。将鼠标悬停在Provisioning Profile: DevEco Managed Profile后![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/3xo1dB_ARAmSOjJGRZV71g/zh-cn_image_0000002561832929.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=EA3E15925C6AC5CD0BC4452CFCFDF4FD6F6E812EA44FCF56AB65BCCFD1E7CD79)，可查看证书有效期、包名（bundle name）、ACL权限（acl）、开放能力（capability）等信息；或进入工程级build-profile.json5文件，在“signingConfigs”下可查看到配置成功的签名信息。

### 未关联注册应用

**HarmonyOS工程****按以下步骤操作：**

1. 连接真机设备或模拟器，具体请参考[使用本地真机运行应用/元服务](ide-run-device.md)或[使用模拟器运行应用/元服务](ide-run-emulator.md)，真机连接成功后如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/uHy6IAZ_R36N7f5zZQU-Vg/zh-cn_image_0000002561832921.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=209917D2ABC38B7FE969FCAF112A708067090FA0C017E87308CFD1FA635F747B)

   说明

   如果同时连接多个设备，则使用自动化签名时，会同时将这多个设备的信息写到证书文件中。
2. 进入**File > Project Structure... > Project > Signing Configs**界面，勾选“**Automatically generate signature**”即可完成签名。如果未登录，请先单击**Sign In**进行登录，然后自动完成签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/E2IS48RxSeWALsvFbcbO8w/zh-cn_image_0000002530913004.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=F0BA072B558E1D8E4B307F9147364F9C638675AF30B2EF54B449113A45052851 "点击放大")
3. （可选）在配置文件中添加ACL权限信息，ACL权限清单请参考[自动签名支持的ACL权限](ide-signing.md#section5301916183411)。修改配置文件后，点击**Ok。**

   在需要使用权限的模块的module.json5（Stage模型）/config.json（FA模型）文件中添加“requestPermissions”/“reqPermissions”字段，并在字段下添加对应的权限名等信息，以在Stage模型工程中增加"ohos.permission.ACCESS\_DDK\_USB"权限为例。

   ```
   1. {
   2. "module": {
   3. ...
   4. "requestPermissions": [{
   5. "name": "ohos.permission.ACCESS_DDK_USB",
   6. }],
   7. ...
   8. }
   9. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/Tcqpv3Z3TpOa3qGdRWaHXw/zh-cn_image_0000002561752925.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=5029DBCFCB0A23D4927F3AEF421D7D82EA7FFDA82910AD3B6CC3B7F809048301)

   说明

   * 在调试签名时，不会强校验配置文件中添加的ACL权限。
   * 涉及受限权限的应用，上架时，应用市场（AGC）将根据应用的使用场景审核是否可以使用对应的受限权限，如不符合，应用的上架申请将被驳回。在配置ACL权限前，请审视是否符合[受限权限的使用场景](restricted-permissions.md)。当前仅少量符合特殊场景的应用可在通过审批后，使用受限权限，申请方式请见[申请使用受限权限](declare-permissions-in-acl.md)。
4. 签名完成后，在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b）。将鼠标悬停在Provisioning Profile: DevEco Managed Profile后![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/IGKMmBr-TtmaSloL_q6kFA/zh-cn_image_0000002530912988.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=1ADF3759A44637F1E35F86DC1B01EEE0498828B9B41E2B2FBB29D587B5860177)，可查看证书有效期、包名（bundle name）、ACL权限（acl）、开放能力（capability）等信息；或进入工程级build-profile.json5文件，在“signingConfigs”下可查看到配置成功的签名信息。

**OpenHarmony工程****按以下步骤操作：**

1. 连接真机设备或模拟器，具体请参考[使用本地真机运行应用/元服务](ide-run-device.md)或[使用模拟器运行应用/元服务](ide-run-emulator.md)，真机连接成功后如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/vnt60lCARoGkG714jQNDow/zh-cn_image_0000002561752941.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=9333B0B71FEE36D20AE5C5038C7686F692FE8A28EE46B6B1D27839E8EEBC668F)
2. 进入**File > Project Structure... > Project > Signing Configs**界面。仅勾选“**Automatically generate signature**”时，生成OpenHarmony签名；勾选“**Support HarmonyOS**”和“**Automatically generate signature**”时，生成HarmonyOS签名。如果未登录，请先单击**Sign In**进行登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Qz1rlrKsT6CrpPsAyRLszg/zh-cn_image_0000002530752992.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=F0B0EFBF3DC6428FBF81FE81FF652EEAD77F74987551601337CBAC2BF6E0A53C)

   签名完成后，如下图所示。在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b），数字证书在AGCt网站的“证书、APP ID和Profile”页签中可以查看。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/7kYxGSTkRAe86LVug3jxpw/zh-cn_image_0000002561752949.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=9941C6EEB0151F7A8304B026964A1CCF7F1923B54AE454FECB73BFEC81B9EE22)

   说明

   * OpenHarmony工程签名时，推荐使用HarmonyOS签名。因为OpenHarmony签名是Release签名，Release签名的应用不支持调试和打印debug日志等。此外，OpenHarmony签名可能会影响应用运行。
   * 如果同时连接多个设备，则使用自动化签名时，会同时将这多个设备的信息写到证书文件中。

## 手动签名

HarmonyOS应用/元服务通过数字证书（.cer文件）和Profile文件（.p7b文件）来保证应用/元服务的完整性。在申请数字证书和Profile文件前，需要通过DevEco Studio生成密钥（存储在格式为.p12的密钥库文件中）和证书请求文件（.csr文件）。

**基本概念**

* **密钥**：格式为.p12，包含非对称加密中使用的公钥和私钥，存储在密钥库文件中，公钥和私钥用于数字签名和验证。
* **证书请求文件**：格式为.csr，全称为Certificate Signing Request，包含密钥对中的公钥和通用名称、组织名称、组织单位等信息，用于向AppGallery Connect申请数字证书。
* **数字证书**：格式为.cer，由华为AppGallery Connect颁发。
* **Profile文件**：格式为.p7b，包含HarmonyOS应用/元服务的包名、数字证书信息、描述应用/元服务允许申请的证书权限列表，以及允许应用/元服务调试的设备列表（如果应用/元服务类型为Release类型，则设备列表为空）等内容，每个应用/元服务包中均必须包含一个Profile文件。

### 生成密钥和证书请求文件

**DevEco Studio 6.1.0 Beta2及之后版本**

1. 在主菜单栏单击**Build > Generate Key** **and CSR**。
2. 在**Generate Key** **and CSR**界面，可以单击**Select an existing key**选择已有的密钥库文件（存储有密钥的.p12文件），若没有密钥库文件则进行填写。下面以新创建密钥库文件为例进行说明。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/7pIDmURMRn6IdbqFX0Y81w/zh-cn_image_0000002561752935.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=2C1732A7B1C8D71ED330A82E1120DA47D7A957461ED4149C5280523FC72EECC7)
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

     说明

     First and last name、Organizational unit、Organization、City or locality、State or province填写要求小于64个字符，不可使用双引号（"）、斜杠（\）、反引号（`）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/RfJjr-YCTbavMHtBME7Nkw/zh-cn_image_0000002561832933.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=BFD342828E5529566ECFB45221BA8CEAD460108D9E9A5E56387635A182006DC9)
4. 在**Generate** **Certificate Request File (CSR)**窗口，设置CSR文件名和CSR文件存储路径后，点击**Finish**。
   * **CSR File Name**：填写CSR文件名称，仅允许包含字母、数字、下划线（\_）、中划线（-）、句号（.）。
   * **Select file save path**：设置CSR文件存储路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/UNyRMBZbQJ6sOohVpzFcJQ/zh-cn_image_0000002530912990.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=4FE6D86C6BEA385CC35CF514CCAB044B314771F43E4BD6EFFB2E3355B0719F66)
5. 创建CSR文件成功，可以在存储路径下获取生成的密钥库文件（.p12）、证书请求文件（.csr）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/dtZEj1JVQRuJOUdqvGZRzA/zh-cn_image_0000002530752998.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=141988A194D82B3726BB7C073D56C4E989E1F3A6F1EFC3FE6838572F48658B25)

**DevEco Studio 6.1.0 Beta2之前版本**

1. 在主菜单栏单击**Build > Generate Key** **and CSR**。

   说明

   如果本地已有对应的密钥，无需新生成密钥，可以在**Generate Key**界面中单击下方的Skip跳过密钥生成过程，直接使用已有密钥生成证书请求文件。
2. 在**Key store file**中，可以单击**Choose Existing**选择已有的密钥库文件（存储有密钥的.p12文件）；如果没有密钥库文件，单击**New**进行创建。下面以新创建密钥库文件为例进行说明。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/xEAh0BH-R0eKOcMPd6Vn_A/zh-cn_image_0000002561832925.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=97BA563EC1AC9567527DC6C43D908D38A754AE25063C3F02D2A597A4B0011AA7)
3. 在**Create Key Store**窗口，填写密钥库信息后，单击**OK**。
   * **Key store file**：设置密钥库文件存储路径，并填写p12文件名。
   * **Password**：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。
   * **Confirm password**：再次输入密钥库密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/me1CD-f-RcWamacj3y1lQw/zh-cn_image_0000002530753006.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=A73ACE35BD803C4594EC861C97AE44AAC0814FCB9117AD5A5FB2B64498A4FC3D)
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

   说明

   First and last name、Organizational unit、Organization、City or locality、State or province要求：字符长度为（0，64），且不可使用双引号（"）、斜杠（\）、反引号（`）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/ACfQxjvoTV2akqA2oFXfnw/zh-cn_image_0000002561752939.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=0EA204A9E324BE72DB7DA50CD49E3187CE3C2CB4C43C49F55DD9300CED58E699)
5. 在**Generate Key** **and CSR**界面，设置CSR文件存储路径和CSR文件名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/lyDsEbzySWyk8WBsL1XCXg/zh-cn_image_0000002530912996.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=E9D501B2DC27DE775BD5F8E1A6226378E1C761C210610CA0966D96D09A7C89E6)
6. 单击**Finish**，创建CSR文件成功，可以在存储路径下获取生成的密钥库文件（.p12）、证书请求文件（.csr）和material文件夹（存放密码加密材料等）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Zh6oQVTYRN--rfEBbP7Ypw/zh-cn_image_0000002530753004.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=CBEB86996DCCF45B63A6A965F2F616276C5677F4AC61FD66CC564B4510217F21)

### 申请调试证书

在AGC中申请和下载调试证书，具体请参考[申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)。

说明

如您未在AGC中注册该应用，申请前需要在AGC中注册，具体请参考[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)。

### 申请调试Profile文件和添加权限信息

1. （可选）如需使用ACL权限，在AGC中[申请ACL权限](../app/agc-help-apply-acl-0000002394212138.md)。同时，在DevEco Studio配置文件中添加权限信息。

   说明

   * ACL权限申请仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
   * 若应用因特殊场景要求使用受限开放权限，请务必在此步骤进行申请，否则应用将在审核时被驳回。受限开放权限可申请的特殊场景请参考[受限开放权限](restricted-permissions.md)。
   * 确保应用申请受限开放权限时提供的场景和功能信息准确。如果应用内使用的受限开放权限超出您申请的范围，或申请权限后使用的功能和场景超出可使用的范围，将影响应用上架。

   在需要使用权限的模块的module.json5（Stage模型）/config.json（FA模型）文件中添加“requestPermissions”/“reqPermissions”字段，并在字段下添加对应的权限名等信息，以在Stage模型工程中增加"ohos.permission.ACCESS\_DDK\_USB"权限为例。

   ```
   1. {
   2. "module": {
   3. ...
   4. "requestPermissions": [{
   5. "name": "ohos.permission.ACCESS_DDK_USB",
   6. }],
   7. ...
   8. }
   9. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/2_5GIOpFT8eK9E1LMbWSCQ/zh-cn_image_0000002561832915.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=0D3C6F9A1334B8CC06038234C9B66965621A0044400818A335C184E3652CE85C)
2. 在AGC中申请和下载Profile文件，具体请参考[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。

### 配置签名信息

1. 连接真机设备，确保[DevEco Studio与真机设备已连接](ide-run-device.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/Rwn-C9cSSQ-5hxYEeEmvbw/zh-cn_image_0000002561832911.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=84C06CB5C1CCCF576BA6660D3C7572DB9958A206C090BE633F2131DB44AB8863)
2. 在**File >** **Project Structure >** **Project > Signing Configs**窗口中，取消勾选“Automatically generate signature”和“Associate with registered application”，分别配置密钥（.p12文件）、Profile（.p7b文件）和数字证书（.cer文件）的路径等信息，配置完毕后点击**Apply**。
   * **Store file**：选择密钥库文件，文件后缀为.p12，该文件为[生成密钥和证书请求文件](ide-signing.md#section462703710326)中生成的.p12文件。
   * **Store password**：输入密钥库密码，该密码与[生成密钥和证书请求文件](ide-signing.md#section462703710326)中填写的密钥库密码保持一致。
   * **Key alias**：输入密钥的别名信息，与[生成密钥和证书请求文件](ide-signing.md#section462703710326)中填写的别名保持一致。
   * **Key password**：输入密钥的密码，与[生成密钥和证书请求文件](ide-signing.md#section462703710326)中填写的**Store Password**保持一致。
   * **Sign alg**：签名算法，固定为SHA256withECDSA。
   * **Profile file**：选择[申请调试Profile文件和添加权限信息](ide-signing.md#section89479413571)中生成的Profile文件，文件后缀为.p7b。
   * **Certpath file**：选择[申请调试证书](ide-signing.md#section081822416419)中生成的数字证书文件，文件后缀为.cer。

   说明

   * Store file，Profile file，Certpath file三个字段支持配置相对路径，以项目根目录为起点，配置文件所在位置的路径名称。
   * 密钥库文件、密钥库密码、密钥别名、密钥密码、Profile文件、数字证书文件必须配套使用，否则会导致签名失败。若失败请根据报错信息进行修改，再进行签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/hsUPmHfmQACT0RACyhzmaA/zh-cn_image_0000002530753014.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=CCEEBAB6F8DAFC8CBC42C2AA168597D782C902386EF2F2814F640C97122A77A2 "点击放大")

   配置完成后，将鼠标悬停在**Provisioning Profile: DevEco Manage Profile**后![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/Hf4WjAWwQkKof06H4boHXA/zh-cn_image_0000002561752945.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=392A9881725E07D9D7CB3E94E4E908B7D6C13EFE4E9D8B27D0E1DE33328ACB34)，可查看证书有效期、包名（bundle name）、企业名称（common name）、ACL权限（acl）、开放能力（capability）相关信息；或者进入工程级build-profile.json5文件，在“signingConfigs”下可查看到配置成功的签名信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/57YY0XPDTfqzg_RLEL1vbw/zh-cn_image_0000002530912984.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=923F515D5EB8111265C58209C354B53273B86C1231C7FD2147D1FC4DD92EA45A "点击放大")
3. 进入工程级build-profile.json5文件，在“signingConfigs”下可查看到配置成功的签名信息，点击右上角的“Run”按钮运行应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/CgqIM__tS-qGzHpQ5G0QmA/zh-cn_image_0000002530912992.png?HW-CC-KV=V1&HW-CC-Date=20260427T235637Z&HW-CC-Expire=86400&HW-CC-Sign=43BEA4379EF8B864EBDB765761D068CBC87780C64C56403AF09EA7805E4C60AE)

## 附录

### 自动签名支持的ACL权限

自动签名当前支持申请的ACL权限的清单如下所示。执行[操作步骤](ide-signing.md#section18815157237)后，DevEco Studio将校验当前配置的ACL权限是否在以下列表中，然后通过应用市场（AGC）申请对应的Profile文件，用于签名打包，从而避免繁琐的手动签名步骤。

从DevEco Studio 6.1.0 Beta2版本开始，自动签名支持配置的ACL权限具体参考[受限开放权限](restricted-permissions.md)。

**6.0.2 Beta****1**

新增权限

* ohos.permission.SUBSCRIBE\_NOTIFICATION
* ohos.permission.ACCESS\_USER\_FULL\_DISK
* ohos.permission.CUSTOM\_SCREEN\_RECORDING
* ohos.permission.GET\_IP\_MAC\_INFO

**6.0.1 Release****（6.0.1.260）**

新增权限

* ohos.permission.SET\_SYSTEMSHARE\_APPLAUNCHTRUSTLIST
* ohos.permission.HOOK\_KEY\_EVENT
* ohos.permission.WEB\_NATIVE\_MESSAGING

**6.0.0 Beta3**

新增权限

* ohos.permission.CUSTOMIZE\_SAVE\_BUTTON
* ohos.permission.GET\_ABILITY\_INFO
* ohos.permission.LINKTURBO
* ohos.permission.GET\_WIFI\_LOCAL\_MAC
* ohos.permission.GET\_ETHERNET\_LOCAL\_MAC
* ohos.permission.USE\_FLOAT\_BALL
* ohos.permission.READ\_LOCAL\_DEVICE\_NAME
* ohos.permission.ACCESS\_NET\_TRACE\_INFO
* ohos.permission.KEEP\_BACKGROUND\_RUNNING\_SYSTEM
* ohos.permission.atomicService.MANAGE\_STORAGE
* ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**5.1.0 Release**

新增权限

* ohos.permission.ACCESS\_DDK\_USB\_SERIAL
* ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL
* ohos.permission.USE\_FRAUD\_APP\_PICKER

**5.0.5 Release**

新增权限

* ohos.permission.kernel.DISABLE\_GOTPLT\_RO\_PROTECTION
* ohos.permission.MANAGE\_APN\_SETTING

**5.0.3 Release**

新增权限

* ohos.permission.READ\_WRITE\_USB\_DEV
* ohos.permission.USE\_FRAUD\_CALL\_LOG\_PICKER
* ohos.permission.USE\_FRAUD\_MESSAGES\_PICKER
* ohos.permission.ACCESS\_DISK\_PHY\_INFO
* ohos.permission.SET\_PAC\_URL
* ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS
* ohos.permission.START\_PROVISIONING\_MESSAGE
* ohos.permission.PRELOAD\_FILE
* ohos.permission.kernel.ALLOW\_WRITABLE\_CODE\_MEMORY
* ohos.permission.kernel.DISABLE\_CODE\_MEMORY\_PROTECTION
* ohos.permission.kernel.ALLOW\_EXECUTABLE\_FORT\_MEMORY
* ohos.permission.GET\_WIFI\_PEERS\_MAC
* ohos.permission.READ\_WRITE\_DESKTOP\_DIRECTORY
* ohos.permission.MANAGE\_PASTEBOARD\_APP\_SHARE\_OPTION
* ohos.permission.MANAGE\_UDMF\_APP\_SHARE\_OPTION
* ohos.permission.READ\_WRITE\_USER\_FILE

**5.0.0 Release**

支持权限

* ohos.permission.READ\_CONTACTS
* ohos.permission.WRITE\_CONTACTS
* ohos.permission.READ\_AUDIO
* ohos.permission.WRITE\_AUDIO
* ohos.permission.READ\_IMAGEVIDEO
* ohos.permission.READ\_PASTEBOARD
* ohos.permission.WRITE\_IMAGEVIDEO
* ohos.permission.ACCESS\_DDK\_USB
* ohos.permission.ACCESS\_DDK\_HID
* ohos.permission.SYSTEM\_FLOAT\_WINDOW
* ohos.permission.FILE\_ACCESS\_PERSIST
* ohos.permission.INPUT\_MONITORING
* ohos.permission.INTERCEPT\_INPUT\_EVENT
* ohos.permission.SHORT\_TERM\_WRITE\_IMAGEVIDEO
