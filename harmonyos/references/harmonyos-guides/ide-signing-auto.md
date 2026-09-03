---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing-auto
title: 自动签名
breadcrumb: 指南 > 编写与调试应用 > 配置调试签名 > 自动签名
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:16+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:e06710bbf1b334a3d6e263067755fe29535560971d405e33acb02d2304fea94b
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/-oQZYqZWQFWlWGmBdpi7hA/zh-cn_image_0000002701662824.png "点击放大")

   **说明** 

   * 点击**Team**下拉框，可以切换团队账号。
   * DevEco Studio根据Bundle name查询该团队在AGC上同包名的应用。若在AGC查询到应用，则进行自动签名；若在AGC未查询到应用或应用冲突，请根据提示信息修改后重新自动签名，具体修改请参考[常见问题](../harmonyos-faqs/faqs-signature-service-18.md)。
3. 点击**Enable open capabilities**，管理接入的[开放能力](../app/agc-help-create-app-0000002247955506.md#section1817619495251)，开放能力接入方式包括默认开启、直接开启、申请开启。当前支持的开放能力请参考[自动签名支持的开放能力](ide-signing-auto.md#section179851045217)。
   * 默认开启：默认勾选该开放能力，包括Account Kit、Location Kit、Intents Kit。
   * 直接开启：点击开放能力名称，在界面右侧查看功能简介，勾选后可直接开启。
   * 申请开启：点击开放能力名称，在界面右侧查看功能简介，填写申请理由（Application Reason）和上传附件（Upload Attachment）。申请后在AGC的[互动中心页面](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/interactive)可看到已提交的申请消息，具体请参考[管理接入的华为开放能力](../app/agc-help-open-capability-0000002465058093.md)。

   **说明** 

   Push Kit（推送服务）开放能力接入后不可取消。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/ExcPa0jHQYmsfBdXQHz55w/zh-cn_image_0000002731382057.png)
4. （可选）添加ACL权限信息，ACL权限清单请参考[自动签名支持的ACL权限](ide-signing-auto.md#section5301916183411)。

   **26.0.0及以上版本**
   1. 点击**Enable ACL Permissions**进入ACL权限配置界面，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/S9XXzQ6-TM67Jp3HPB-rVg/zh-cn_image_0000002701662830.png)添加模块的ACL权限。添加的权限会同步至模块的module.json5文件，以及模块module.json5文件中添加的权限信息也会同步至ACL权限配置界面。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/ZEKpgJwnSjmgQ6gxJuJFBw/zh-cn_image_0000002731382053.png)
   2. 选中ACL权限名称后点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/TjyFgeMvSPas6dXn7M2g5g/zh-cn_image_0000002731542031.png)，选择权限适用模块（Module）、填写申请原因（Reason）、勾选调用时机（When）和Abilities，点击**OK**完成ACL权限配置。此外，开发者可点击编辑/删除按钮，对已填写的ACL权限配置进行修改或移除。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/XzDBHKXjR-Ocu_O2t3yz3Q/zh-cn_image_0000002731382061.png)
   3. 填写所有ACL权限的申请原因（Request reason）和上传附件（Attachment），点击**OK**提交申请。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/uhzZF31_SAaiVc4NLWcThA/zh-cn_image_0000002731542021.png)
   4. 提交后可在AGC的[互动中心页面](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/interactive)查看ACL权限申请进度，或点击**Enable ACL Permissions**进入权限申请界面，过滤查看权限申请状态。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/U9txcSiVSE2HlHkOksry_g/zh-cn_image_0000002701662828.png "点击放大")

   **26.0.0以下版本**

   在需要使用权限的模块的module.json5文件中添加“requestPermissions”字段，并在字段下添加对应的权限名等信息，以在Stage模型工程中增加"ohos.permission.ACCESS\_DDK\_USB"权限为例。

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/275Rcyz4RvKkVFpUxwYEEg/zh-cn_image_0000002701822742.png)

   **说明** 

   * 申请ACL前注意事项：
     + 在申请ACL权限前，请审视是否符合[受限权限的使用场景](restricted-permissions.md)。当前仅少量符合特殊场景的应用可在通过审批后，使用受限权限。申请方式请见[申请使用受限权限](declare-permissions-in-acl.md)。
     + 涉及受限权限的应用，在上架时，应用市场（AGC）将根据应用的使用场景审核是否可以使用对应的受限权限。如不符合，应用的上架申请将被驳回，审核方式请见[发布HarmonyOS应用](../app/agc-help-release-app-0000002271695230.md)。
   * 申请ACL后Profile证书说明：
     + 在ACL权限申请审批完成前，可获得一个有效期较短的临时Profile证书，使应用完成签名。临时证书到期后，若申请仍未审批通过，签名时需再次申请和再次获取临时证书。
     + 在ACL权限申请审批完成后，可获取一个有效期较长的正式Profile证书。
5. 签名完成后，在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b）。将鼠标悬停在Provisioning Profile: DevEco Managed Profile后![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/zI36KhxuS3Om-XA0AvKk2Q/zh-cn_image_0000002701822754.png)，可查看证书有效期、包名（bundle name）、ACL权限（acl）、开放能力（capability）等信息；或进入工程级build-profile.json5文件，在“signingConfigs”下查看到配置成功的签名信息。

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
       ...
       "requestPermissions": [{
         "name": "ohos.permission.ACCESS_DDK_USB",
       }],
       ...
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/W_mMYO1LS0Gkre4q3MN-VA/zh-cn_image_0000002731382043.png)

   **说明** 

   * 在调试签名时，不会强制校验配置文件中添加的ACL权限。
   * 涉及受限权限的应用，上架时，应用市场（AGC）将根据应用的使用场景审核是否可以使用对应的受限权限，如不符合，应用的上架申请将被驳回。在配置ACL权限前，请审视是否符合[受限权限的使用场景](restricted-permissions.md)。当前仅少量符合特殊场景的应用可在通过审批后，使用受限权限，申请方式请见[申请使用受限权限](declare-permissions-in-acl.md)。
3. 进入**File > Project Structure... > Project > Signing Configs**界面，勾选“**Automatically generate signature**”，点击**OK**即可完成签名。如果未登录，请先单击**Sign In**进行登录，然后自动完成签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/bwD6-DPbQUGEOBujM0rf9g/zh-cn_image_0000002701822750.png "点击放大")
4. 签名完成后，在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b）。将鼠标悬停在Provisioning Profile: DevEco Managed Profile后![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/hv_KgwuaSMSYrM_C0Sez7Q/zh-cn_image_0000002701822746.png)，可查看证书有效期、包名（bundle name）、ACL权限（acl）、开放能力（capability）等信息；或进入工程级build-profile.json5文件，在“signingConfigs”下查看到配置成功的签名信息。

## （可选）OpenHarmony工程

**说明** 

* OpenHarmony工程签名时，推荐使用HarmonyOS签名。因为OpenHarmony签名是Release签名，Release签名的应用不支持调试和打印debug日志等。此外，OpenHarmony签名可能会影响应用运行。
* 如果同时连接多个设备，则使用自动签名时，会同时将这多个设备的信息写到证书文件中。

1. 连接[本地真机设备](ide-run-device.md)/[模拟器设备](ide-run-emulator.md)，或将[真机调试设备注册到AGC设备列表](../app/agc-help-add-device-0000002283189937.md)后，开始签名。从26.0.0版本开始，支持在AGC注册设备后开始签名。
2. 进入**File > Project Structure... > Project > Signing Configs**界面。仅勾选“**Automatically generate signature**”时，生成OpenHarmony签名；勾选“**Support HarmonyOS**”和“**Automatically generate signature**”时，生成HarmonyOS签名（如果未登录，请先单击**Sign In**进行登录）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/gKlDmjfpT_ifOzWASp6cnQ/zh-cn_image_0000002731542029.png)

   签名完成后，如下图所示。在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b），数字证书在AGC网站的“证书、APP ID和Profile”页签中可以查看。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Gdxk4qAeRxe1sLY9PyV6Uw/zh-cn_image_0000002701662826.png)

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
