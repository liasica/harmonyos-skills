---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing-auto
title: 自动签名
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 配置调试签名 > 自动签名
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:29+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:14f39764686df0ffef04182beb9b28faac7a24109c7e2d1246ded7ccac56c6b4
---

## 功能介绍

HarmonyOS应用调试时，自动签名分为关联注册应用和未关联注册应用两种。

* 关联注册应用的自动签名：从DevEco Studio 6.0.0 Beta5版本开始支持，与应用市场（AppGallery Connect，简称AGC）的应用绑定，可在DevEco Studio开通开放能力和添加ACL权限，以及AGC与DevEco Studio的开放能力和权限信息可同步。
* 未关联注册应用的自动签名：未与应用市场的应用绑定。

## 约束与限制

* DevEco Studio 6.1.1 Beta1及以上版本，关联注册应用的自动签名支持在各国家/地区使用。DevEco Studio 6.1.1 Beta1以下版本，关联注册应用的自动签名仅支持中国境内（不包含中国香港、中国澳门、中国台湾）。
* 使用自动签名前，请确保本地系统时间与北京时间（UTC/GMT+08:00）保持一致。如果不一致，将导致签名失败。

## HarmonyOS工程

### 关联注册应用

1. 连接[本地真机设备](ide-run-device.md)/[模拟器设备](ide-run-emulator.md)，或将[真机调试设备注册到AGC设备列表](../app/agc-help-add-device-0000002283189937.md)后，开始签名。

   **说明** 

   * 从26.0.0版本开始，支持在AGC注册设备后开始签名。
   * 如果同时连接多个设备，则使用自动签名时，会同时将这多个设备的信息写到证书文件中。
2. 进入**File > Project Structure... > Project > Signing Configs**界面，勾选"**Associate with registered application**"。如果未登录，请先点击**Sign In**进行登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/qlmOcFvxTcKxQ4axP7clTA/zh-cn_image_0000002808886231.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE1F02AAC599D2AC56C63B1E5F57806BD8F7AF0D3AB0AA8061A9D7A12FFA09E9 "点击放大")

   **说明** 

   * 点击**Team**下拉框，可以切换团队账号。
   * DevEco Studio根据Bundle name查询该团队在AGC上同包名的应用。若在AGC查询到应用，则进行自动签名；若在AGC未查询到应用或应用冲突，请根据提示信息修改后重新自动签名，具体修改请参考[常见问题](../harmonyos-faqs/signature-service-faq-0002.md)。
3. 点击**Enable open capabilities**，管理接入的开放能力，开放能力接入方式包括默认开启、直接开启、申请开启。当前支持的开放能力请参考[自动签名支持的开放能力](ide-signing-auto.md#section179851045217)。
   * 默认开启：默认勾选该开放能力，包括Account Kit、Location Kit、Intents Kit。
   * 直接开启：点击开放能力名称，在界面右侧查看功能简介，勾选后可直接开启。
   * 申请开启：点击开放能力名称，在界面右侧查看功能简介，填写申请理由（Application Reason）和上传附件（Upload Attachment）。申请后在AGC的[互动中心页面](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/interactive)可看到已提交的申请消息，具体请参考[管理接入的华为开放能力](../app/agc-help-open-capability-0000002465058093.md)。

   **说明** 

   Push Kit（推送服务）开放能力接入后不可取消。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/bUVdY-FZSLqJCPV5KB0f7w/zh-cn_image_0000002808766161.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A5B9A82E44AD3E6A44DE3058C968721341B0E98D56684944790B9EA5555DE4F "点击放大")
4. （可选）添加ACL权限信息，ACL权限清单请参考[自动签名支持的ACL权限](ide-signing-auto.md#section5301916183411)。

   **26.0.0及以上版本**

   **说明** 

   Enable ACL Permissions功能仅支持中国境内（不包含中国香港、中国澳门、中国台湾）。

   1. 点击**Enable ACL Permissions**进入ACL权限配置界面，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/KmzaGUuhTRCwq4acOHxTrg/zh-cn_image_0000002808766157.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=1CA175C0A7820B9D5097BC19AACF1B820552870C33E8B6D627BF9E55F707AF39)添加模块的ACL权限。添加的权限会同步至模块的module.json5文件，以及模块module.json5文件中添加的权限信息也会同步至ACL权限配置界面。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/1xLJ0CbWSVSXSAxAZKvvog/zh-cn_image_0000002808886241.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1E8285363D6D78A668BD0F0005C5A6E2EF783EE4257563277B909A8961EC5B9 "点击放大")
   2. 选中ACL权限名称后点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/VLiVdd5fTeepaYGZqvS5ZA/zh-cn_image_0000002779566582.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=743F29B2A136EE99B66AE5A3412EF368E9C7DFBB06200403F7B8DEA90B8C3D4D)，选择权限适用模块（Module）、填写申请原因（Reason）、勾选调用时机（When）和Abilities，点击**OK**完成ACL权限配置。此外，开发者可点击编辑/删除按钮，对已填写的ACL权限配置进行修改或移除。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/MvsVF0zfRreR8mzDiJ3uEA/zh-cn_image_0000002808766165.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=370C04AF1B1CC8A55C5F84CCDC5379BAA44DB406ABCCB77A9CA6B0F64FBE7529)
   3. 填写所有ACL权限的申请原因（Request reason）和上传附件（Attachment），点击**OK**提交申请。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/ClWG1wHlRWuIzP9eoEScUg/zh-cn_image_0000002808886233.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=96F7837865A69DD8C688D4756EFF9E6DF3C5877FB62F5064CD1842A7A0D5D260)
   4. 提交后可在AGC的[互动中心页面](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/interactive)查看ACL权限申请进度，或点击**Enable ACL Permissions**进入权限申请界面，过滤查看权限申请状态。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/LsmE7bYFRimLzFADEQoPUQ/zh-cn_image_0000002808766151.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=76DD93CA44A51264AB520D8C1315BB288A8AFAD07BA2FA6981DC24391182F872)

   **26.0.0以下版本**

   在需要使用权限的模块的module.json5文件中添加“requestPermissions”字段，并在字段下添加对应的权限名等信息，以在Stage模型工程中增加"ohos.permission.ACCESS\_DDK\_USB"权限为例。

   ```screen
   {
     "module": {
       "requestPermissions": [{
         "name": "ohos.permission.ACCESS_DDK_USB",
       }],
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/uUSGl7DuRRqNZDFPGAdeZw/zh-cn_image_0000002779566572.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E6E16E0669D7B67B676A8341FB9EBA04888F5B98752007CC26D58B6083E6784)

   **说明** 

   * 申请ACL前注意事项：
     + 在申请ACL权限前，请审视是否符合[受限权限的使用场景](restricted-permissions.md)。当前仅少量符合特殊场景的应用可在通过审批后，使用受限权限。申请方式请见[申请使用受限权限](declare-permissions-in-acl.md)。
     + 涉及受限权限的应用，在上架时，应用市场（AGC）将根据应用的使用场景审核是否可以使用对应的受限权限。如不符合，应用的上架申请将被驳回，审核方式请见[发布HarmonyOS应用](../app/agc-help-release-app-0000002271695230.md)。
   * 申请ACL后Profile证书说明：
     + 在ACL权限申请审批完成前，可获得一个有效期较短的临时Profile证书，使应用完成签名。临时证书到期后，若申请仍未审批通过，签名时需再次申请和再次获取临时证书。
     + 在ACL权限申请审批完成后，可获取一个有效期较长的正式Profile证书。
5. 配置完成后查看签名信息。

   方式一：配置完成后，将鼠标悬停在**Provisioning Profile: DevEco Manage Profile**后![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/pYwCERm7Qk24OyXRQ1EVLA/zh-cn_image_0000002808886237.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=D15D9A98BB17667F88984F04428D0DEA2006B037F7EF6CA941762246BDD1D8E9)，可查看证书有效期、包名（bundle name）、企业名称（common name）、ACL权限（acl）、开放能力（capability）相关信息。

   方式二：26.0.1之前版本，进入工程级build-profile.json5文件，在“signingConfigs”下查看到配置成功的签名信息。从26.0.1版本开始，根据${default}所在的签名文件（build-profile.json5/sign-config.json5）进行查看。

### 未关联注册应用

1. 连接[本地真机设备](ide-run-device.md)/[模拟器设备](ide-run-emulator.md)，或将[真机调试设备注册到AGC设备列表](../app/agc-help-add-device-0000002283189937.md)后，开始签名。

   **说明** 

   * 从26.0.0版本开始，支持在AGC注册设备后开始签名。
   * 如果同时连接多个设备，则使用自动签名时，会同时将这多个设备的信息写到证书文件中。
2. （可选）在配置文件中添加ACL权限信息，ACL权限清单请参考[自动签名支持的ACL权限](ide-signing-auto.md#section5301916183411)。

   在需要使用权限的模块的module.json5（Stage模型）/config.json（FA模型）文件中添加“requestPermissions”/“reqPermissions”字段，并在字段下添加对应的权限名等信息，以在Stage模型工程中增加"ohos.permission.ACCESS\_DDK\_USB"权限为例。

   ```screen
   {
     "module": {
       "requestPermissions": [{
         "name": "ohos.permission.ACCESS_DDK_USB",
       }],
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/KxJtFl6dTNupoqiIinkbVA/zh-cn_image_0000002808886235.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF067FCC07981F1EB9C35CF477213F436DFFC14E34978C6DA4D02B25DC0D6FE7)

   **说明** 

   * 在调试签名时，不会强制校验配置文件中添加的ACL权限。
   * 涉及受限权限的应用，上架时，应用市场（AGC）将根据应用的使用场景审核是否可以使用对应的受限权限，如不符合，应用的上架申请将被驳回。在配置ACL权限前，请审视是否符合[受限权限的使用场景](restricted-permissions.md)。当前仅少量符合特殊场景的应用可在通过审批后，使用受限权限，申请方式请见[申请使用受限权限](declare-permissions-in-acl.md)。
3. 进入**File > Project Structure... > Project > Signing Configs**界面，勾选“**Automatically generate signature**”，点击**OK**即可完成签名。如果未登录，请先单击**Sign In**进行登录，然后自动完成签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/txhNU5iVTsymExghlxAo-w/zh-cn_image_0000002779566576.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=319CC9F50095DF699AA94EEBB47A7D033124F8510B40A20BBD6A7E398C8F18AF)
4. 签名完成后，在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b）。
5. 配置完成后查看签名信息。

   方式一：配置完成后，将鼠标悬停在**Provisioning Profile: DevEco Manage Profile**后![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/uCV01xA2TeymoZEb3TpvQQ/zh-cn_image_0000002779406594.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=539571BEFEBD277F73A65ADB79C09AAFA8F124A5C5B2C92506D004E9DF92E138)，可查看证书有效期、包名（bundle name）、企业名称（common name）、ACL权限（acl）、开放能力（capability）相关信息。

   方式二：26.0.1之前版本，进入工程级build-profile.json5文件，在“signingConfigs”下查看到配置成功的签名信息。从26.0.1版本开始，根据${default}所在的签名文件（build-profile.json5/sign-config.json5）进行查看。

## （可选）OpenHarmony工程

**说明** 

* OpenHarmony工程签名时，推荐使用HarmonyOS签名。因为OpenHarmony签名是Release签名，Release签名的应用不支持调试和打印debug日志等。此外，OpenHarmony签名可能会影响应用运行。
* 如果同时连接多个设备，则使用自动签名时，会同时将这多个设备的信息写到证书文件中。

1. 连接[本地真机设备](ide-run-device.md)/[模拟器设备](ide-run-emulator.md)，或将[真机调试设备注册到AGC设备列表](../app/agc-help-add-device-0000002283189937.md)后，开始签名。从26.0.0版本开始，支持在AGC注册设备后开始签名。
2. 进入**File > Project Structure... > Project > Signing Configs**界面。仅勾选“**Automatically generate signature**”时，生成OpenHarmony签名；勾选“**Support HarmonyOS**”和“**Automatically generate signature**”时，生成HarmonyOS签名（如果未登录，请先单击**Sign In**进行登录）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/nbMBCiElTH-id4_0mwfKsg/zh-cn_image_0000002808766155.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C8FA1F816964DF0117D3A46C39798D340A724A453D01F09458E6C4297759163)

   签名完成后，如下图所示。在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b），数字证书在AGC网站的“证书、APP ID和Profile”页签中可以查看。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/xH6oWHQMTuKa7srwaE6cqQ/zh-cn_image_0000002779566580.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF1F76874B0235B739B5D10671961FEEE34351E7C0BE80983A5B08A5F8B6C4BD)

## 附录

### 自动签名支持的ACL权限

自动签名当前支持申请的ACL权限的清单如下所示。执行操作步骤后，DevEco Studio将校验当前配置的ACL权限是否在以下列表中，然后通过应用市场（AGC）申请对应的Profile文件，用于签名打包，从而避免繁琐的手动签名步骤。

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

**5.0.4 Release**

新增权限

* ohos.permission.PERSISTENT\_BLUETOOTH\_PEERS\_MAC
* ohos.permission.ACCESS\_VIRTUAL\_SCREEN

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

### 自动签名支持的开放能力

**26.0.0版本**

* Intents Kit (意图框架)
* Location Kit（定位服务）
* Indoor high-precision positioning（室内高精度定位）
* Semantic location（位置语义）
* Background wake-up triggered by Beacon geofence（围栏后台唤醒）
* Bluetooth scan information retrieval (获取蓝牙扫描信息)
* Account Kit（华为账号）
* HUAWEI ID instant login （华为账号一键登录）
* Obtain user's mobile number （获取您的手机号）
* Obtain shipping address （获取收货地址）
* Push Kit（[推送服务](push-kit-introduction.md)）
* the In-App Call Message（推送应用内通话消息）
* Push text-to-speech messages （推送语音播报消息）
* Device status detection （[应用设备状态检测](devicesecurity-deviceverify-develop.md)）
* Map Kit（[地图服务](map-introduction.md)）
* Safety Detect （[安全检测服务](devicesecurity-safetydetect-develop.md)）
* Standby form （待机屏保卡片）
* Back transparent card （背板透明卡片）
* Second-Level Game Launch (秒级启动)
* Live View Kit （实况窗服务）
* Agent-powered reminder （代理提醒）
* SmartFill (智能填充)
* Digital Shield Service (数字盾服务)
* Lock screen widget （锁屏卡片）

**6.0.0 Beta5**

* Push Kit（[推送服务](push-kit-introduction.md)）
* Device status detection（[应用设备状态检测](devicesecurity-deviceverify-develop.md)）
* Map Kit（[地图服务](map-introduction.md)）
* Safety Detect（[安全检测服务](devicesecurity-safetydetect-develop.md)）
