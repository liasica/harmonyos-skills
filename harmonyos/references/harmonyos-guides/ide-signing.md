---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing
title: 配置调试签名
breadcrumb: 指南 > 编写与调试应用 > 配置调试签名
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:34+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:97f0d44f35b3fdd4a5c65fa3e14c2d33cc163bc2fde741b1a02388edffe6ed5b
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/lX5ppebZTBSb3uzqD3f85w/zh-cn_image_0000002530912982.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=688901D459E5AAD10876E97F162E33C55F0824ABB55A991A580DC2689611E161)

   说明

   如果同时连接多个设备，则使用自动化签名时，会同时将这多个设备的信息写到证书文件中。
2. 进入**File > Project Structure... > Project > Signing Configs**界面，勾选“**Associate with registered application**”。如果未登录，请先点击**Sign In**进行登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/65jTD_8jRTCPFPkJtbM8tQ/zh-cn_image_0000002530752994.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=C9A55E502119C4B2BE95DFCF99BBEBBB6D0F0115D48FB0194519DD459576BA7C "点击放大")

   说明

   * 点击**Team**下拉框，可以切换团队账号。
   * 开始签名后，DevEco Studio根据Bundle name查询该团队在AGC上同包名的应用。若在AGC查询到应用，则进行自动签名；若在AGC未查询到应用或应用冲突，请根据提示信息修改后重新自动签名，具体修改请参考[常见问题](../harmonyos-faqs/faqs-signature-service-18.md)。
3. 点击**Enable open capabilities**，在DevEco Studio上开通[开放能力](../app/agc-help-create-app-0000002247955506.md#section1817619495251)。当前支持开通如下四种开放能力：Push Kit（[推送服务](push-kit-introduction.md)）、Device status detection（[应用设备状态检测](devicesecurity-deviceverify-develop.md)）、Map Kit（[地图服务](map-introduction.md)）、Safety Detect（[安全检测服务](devicesecurity-safetydetect-develop.md)），应用根据需要进行勾选。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/-LBBZAybR--tJOW29XaEZQ/zh-cn_image_0000002530913000.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=AC29B1E2EF42BD6D641ABE224C59039A43078F4AFB02536BCC29159AC4371D02)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/zHymkpiaTAS6IICgaj9KmA/zh-cn_image_0000002530752988.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=E05BF256FD66F42A97665E7FCE73348DE5BEEF6C4A6167CF180F822139D77AE7)

   修改配置文件后点击**OK**，若应用已在AGC申请该权限则签名成功；若应用未申请该权限，会导致签名失败，点击Notice弹窗中"**submit a permission request in AppGallery Connect**"或"**Submit**"，跳转至AGC申请权限，然后再返回DevEco Studio界面重新签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/l30rjQm5QsmqPPDT7HrVmw/zh-cn_image_0000002561752937.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=261E5CBB93651A85702E8C12DFB13A82ABA741413001635FE59D5C626E762047 "点击放大")

   说明

   * 申请ACL前注意事项：
     + 在申请ACL权限前，请审视是否符合[受限权限的使用场景](restricted-permissions.md)。当前仅少量符合特殊场景的应用可在通过审批后，使用受限权限。申请方式请见[申请使用受限权限](declare-permissions-in-acl.md)。
     + 涉及受限权限的应用，在上架时，应用市场（AGC）将根据应用的使用场景审核是否可以使用对应的受限权限。如不符合，应用的上架申请将被驳回，审核方式请见[发布HarmonyOS应用](../app/agc-help-release-app-0000002271695230.md)。
   * 申请ACL后Profile证书说明：
     + 在ACL权限申请审批完成前，可获得一个有效期较短的临时Profile证书，使应用完成签名。临时证书到期后，若申请仍未审批通过，签名时需再次申请和再次获取临时证书。
     + 在ACL权限申请审批完成后，可获取一个有效期较长的正式Profile证书。
5. 签名完成后，在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b）。将鼠标悬停在Provisioning Profile: DevEco Managed Profile后![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/_ufmSZxnTT2YoGokHTcCwg/zh-cn_image_0000002561832929.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=ED950167188F6BB39214B4AB939F9F3B463BFFB542BB02E631CA88CEE05445FE)，可查看证书有效期、包名（bundle name）、ACL权限（acl）、开放能力（capability）等信息；或进入工程级build-profile.json5文件，在“signingConfigs”下可查看到配置成功的签名信息。

### 未关联注册应用

**HarmonyOS工程****按以下步骤操作：**

1. 连接真机设备或模拟器，具体请参考[使用本地真机运行应用/元服务](ide-run-device.md)或[使用模拟器运行应用/元服务](ide-run-emulator.md)，真机连接成功后如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/kRpaLSdkSoil3nIvjLJjMQ/zh-cn_image_0000002561832921.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=D82415FB8087D80A362484DC961F77BD9FB4AB736876CE62BFA7F9235ACDDCD9)

   说明

   如果同时连接多个设备，则使用自动化签名时，会同时将这多个设备的信息写到证书文件中。
2. 进入**File > Project Structure... > Project > Signing Configs**界面，勾选“**Automatically generate signature**”即可完成签名。如果未登录，请先单击**Sign In**进行登录，然后自动完成签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/vLtraaggQkad9cnZKGCgxQ/zh-cn_image_0000002530913004.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=B37D8EE2FFFCD3F22F079F16EE8E1259A7E3DB9442C8DE9FA9C6144A450AC780 "点击放大")
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Cu29IKK-SqSTJq50uFTMRQ/zh-cn_image_0000002561752925.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=DB025EDFCE70630123D473CF6A4DB184E71490714C242ACB32A70544EE91E5B7)

   说明

   * 在调试签名时，不会强校验配置文件中添加的ACL权限。
   * 涉及受限权限的应用，上架时，应用市场（AGC）将根据应用的使用场景审核是否可以使用对应的受限权限，如不符合，应用的上架申请将被驳回。在配置ACL权限前，请审视是否符合[受限权限的使用场景](restricted-permissions.md)。当前仅少量符合特殊场景的应用可在通过审批后，使用受限权限，申请方式请见[申请使用受限权限](declare-permissions-in-acl.md)。
4. 签名完成后，在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b）。将鼠标悬停在Provisioning Profile: DevEco Managed Profile后![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/5y-E05v4QGeUUc5l41FjcA/zh-cn_image_0000002530912988.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=7A3E93C712463631C08921FB86BE28316585944F5A8A24B936B6C7E301E76D02)，可查看证书有效期、包名（bundle name）、ACL权限（acl）、开放能力（capability）等信息；或进入工程级build-profile.json5文件，在“signingConfigs”下可查看到配置成功的签名信息。

**OpenHarmony工程****按以下步骤操作：**

1. 连接真机设备或模拟器，具体请参考[使用本地真机运行应用/元服务](ide-run-device.md)或[使用模拟器运行应用/元服务](ide-run-emulator.md)，真机连接成功后如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/wl3SvYryR56EHsKXh4X7DA/zh-cn_image_0000002561752941.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=530AE6F35186112B24F4D871943C5F16E28049F575E9236F10170014F063DC42)
2. 进入**File > Project Structure... > Project > Signing Configs**界面。仅勾选“**Automatically generate signature**”时，生成OpenHarmony签名；勾选“**Support HarmonyOS**”和“**Automatically generate signature**”时，生成HarmonyOS签名。如果未登录，请先单击**Sign In**进行登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/gc_COxLDSUqMrJ9hLDlExg/zh-cn_image_0000002530752992.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=36C09A2E68237C0228A314B63CF26BF7273995D5EF41BE2B5A9533221D64FFE3)

   签名完成后，如下图所示。在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b），数字证书在AGCt网站的“证书、APP ID和Profile”页签中可以查看。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/WlIfCgBiSDeAl2B4j0JaRA/zh-cn_image_0000002561752949.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=EFC093032BE229584B7021C036BD441E95665FC94FECA4D5D8A383BD95AB6F4C)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/rwkl61uhTcKGMO9XaGmftw/zh-cn_image_0000002561752935.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=1E65E9532D4EF6E3063A410CF01255D4C960087A403ACA85F338228EE4CF2AEB)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/RMyG4QGFRM6RMQDmV-2SpA/zh-cn_image_0000002561832933.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=7332FC607A5E67385D2CA448B67AEB84D9797498D8B1466E0719C8A4A082FA34)
4. 在**Generate** **Certificate Request File (CSR)**窗口，设置CSR文件名和CSR文件存储路径后，点击**Finish**。
   * **CSR File Name**：填写CSR文件名称，仅允许包含字母、数字、下划线（\_）、中划线（-）、句号（.）。
   * **Select file save path**：设置CSR文件存储路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/7WTlMi1sSveU6l8a1NtWTQ/zh-cn_image_0000002530912990.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=E77553481F5EB58B2DA9D01D1EFFCF504A91DB95A45F1B41F30EA07EB8463973)
5. 创建CSR文件成功，可以在存储路径下获取生成的密钥库文件（.p12）、证书请求文件（.csr）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/gbb_pLVXTFSaYlkMv0Mnmg/zh-cn_image_0000002530752998.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=7B2DE64222B7ECC531AC970C9B9BC6215BBC839914876C32DA1DBA9F3B9B4957)

**DevEco Studio 6.1.0 Beta2之前版本**

1. 在主菜单栏单击**Build > Generate Key** **and CSR**。

   说明

   如果本地已有对应的密钥，无需新生成密钥，可以在**Generate Key**界面中单击下方的Skip跳过密钥生成过程，直接使用已有密钥生成证书请求文件。
2. 在**Key store file**中，可以单击**Choose Existing**选择已有的密钥库文件（存储有密钥的.p12文件）；如果没有密钥库文件，单击**New**进行创建。下面以新创建密钥库文件为例进行说明。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/O36OtBugSSasl4lGIM3Igg/zh-cn_image_0000002561832925.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=82C21C2DFA98CF0007BE4B2B608E5979AE676AFFF81E16069B84D92847C31A17)
3. 在**Create Key Store**窗口，填写密钥库信息后，单击**OK**。
   * **Key store file**：设置密钥库文件存储路径，并填写p12文件名。
   * **Password**：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。
   * **Confirm password**：再次输入密钥库密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/rB-1FwiJSuu9Alwe--JCoA/zh-cn_image_0000002530753006.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=869D4635B27DECD64F693AE5D156AD8A7ACAE7F6BF0E34E1B69FAFD6FB556C66)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/ndJ6rYeLSPGD1mV87zCcBg/zh-cn_image_0000002561752939.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=E85D63D7FC96BE79FC470160DDFF9250FE0F9A04D9723C2D176469C4D8A82B97)
5. 在**Generate Key** **and CSR**界面，设置CSR文件存储路径和CSR文件名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/9cWHezrOQ5Ck5ztU2riWQw/zh-cn_image_0000002530912996.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=A89949572D99069A13473E9D35340FD3D24C269F06814E4FCE9C20C73E323891)
6. 单击**Finish**，创建CSR文件成功，可以在存储路径下获取生成的密钥库文件（.p12）、证书请求文件（.csr）和material文件夹（存放密码加密材料等）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/-OVUDZwLQWKL-M68WE0j0g/zh-cn_image_0000002530753004.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=3DC57C8295DBEF740222E87823B4B1FF9907665580C03E8B231E69BC3C0251E3)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/DBhap8YxRE6V4xGn5xoI2Q/zh-cn_image_0000002561832915.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=08E9060E1A9AA3EE92B0239997F7F0F01DCB14F0FB9501B8AE35947C442614F8)
2. 在AGC中申请和下载Profile文件，具体请参考[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。

### 配置签名信息

1. 连接真机设备，确保[DevEco Studio与真机设备已连接](ide-run-device.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/9x-3v4WmSouIKSV7kn_48Q/zh-cn_image_0000002561832911.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=3CAFB89B87FD5B255563E9387D89CCD42E384AE1FA8C03DA84C1F6858A1FC6AD)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/7hwiLXCzQQOaSgkoSlUlVw/zh-cn_image_0000002530753014.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=0D2B932F097053589C1F1821E15963FFAD76D33158470E872E849BF9AD8F0A39 "点击放大")

   配置完成后，将鼠标悬停在**Provisioning Profile: DevEco Manage Profile**后![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/rCTVvCQWRIiYeDwetnJtYw/zh-cn_image_0000002561752945.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=3197553FAB3E05407AC2D6BE9305AD8AF806DFE7D9C4D66BDE8D89B46B12A697)，可查看证书有效期、包名（bundle name）、企业名称（common name）、ACL权限（acl）、开放能力（capability）相关信息；或者进入工程级build-profile.json5文件，在“signingConfigs”下可查看到配置成功的签名信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/KUZQHCrGTgaG_L1ay1H4yQ/zh-cn_image_0000002530912984.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=6F9A4578070024FDB6A7CB9BA7324D309AD89499EA87DFB826C1FE1A0B03AE19 "点击放大")
3. 进入工程级build-profile.json5文件，在“signingConfigs”下可查看到配置成功的签名信息，点击右上角的“Run”按钮运行应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/uEHSOeOySlmUFivR_ezLaA/zh-cn_image_0000002530912992.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=F0D45C626621D925F0876950A6320AD389C22E3515B1522F70AEBB440E5AA907)

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
