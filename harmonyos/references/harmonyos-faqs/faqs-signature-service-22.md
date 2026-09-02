---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-22
title: 自动签名报错常见问题定位
breadcrumb: FAQ > DevEco Studio > 签名服务 > 自动签名报错常见问题定位
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1376bfcede5edcd5700f83176e660a6fbfb8f387c122acda8bd6d066d2671cc3
---

## 问题现象

自动签名时报错，常见报错信息如下：

* **问题一：** 签名报错提示如下：

  ```txt
  The signing config name must be less than or equal to 64 characters, and can contain only letters and digits.
  ```
* **问题二：** 签名报错提示如下：

  ```txt
  > hvigor ERROR: Failed :sdk_sample:default@SignModuleRemoteHsp...
  > hvigor ERROR: Unsupported state or unable to authenticate data
          Detail: signing failed. Reconfigure the signature or clear the c:\XXX\.ohos config folder and perform signing again.
          at D:\XXX\XXX\XXX\build-profile.json5
  > hvigor ERROR: BUILD FAILED in 3 s 527 ms
  ```
* **问题三：** 使用自动化签名功能对HarmonyOS进行签名时，提示“Provision number exceeds limit”信息，报错信息如下：

  ```txt
  Provision number exceeds limit.please click Help > Contact Support for assistance FAQ
  ```
* **问题四：** 签名时在DevEco Studio的build-profile.json5文件中无法生成签名信息或出现如下报错。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/hKugROwqTzGdU-UzuyMgvw/zh-cn_image_0000002628569278.png "点击放大")
* **问题五：** 签名报错提示，报错信息如下：

  ```txt
  Failed to query agreement signing records. The unverified user need to sign the agreement before using automatic signing.
  ```
* **问题六：** 签名报时间戳问题，报错信息如下：

  ```txt
  The signature does not take effect or has expired. It may be the current system time is inaccurate, please calibrate the system time and sign again.
  ```
* **问题七：** 签名文件达到上限，报错信息如下：

  ```txt
  The number of certificates has reached the limit. Delete some certificates and try again. Certificate Number Exceeds Limit.
  ```
* **问题八：** 自动签名失败，无法生成密钥：

  ```txt
  Error occurred while generating the key. Unable to generate the key
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/xtzEeYwMSpKVrAnIx4QLew/zh-cn_image_0000002628409372.png "点击放大")
* **问题九：** 签名报时间戳问题，且已经设置了时间同步，但多个项目中存在某一个项目无法自动签名，报错信息如下：

  ```txt
  The signature does not take effect or has expired. It may be the current system time is inaccurate, please calibrate the system time and sign again.
  ```
* **问题十：** 签名报错，报错信息如下：

  ```txt
  Unable to create the profile due to a lack of a device. Connect a device via IP or USB first.
  Skip this step if you are installing a HAP on the emulator.
  ```
* **问题十一：** 签名材料校验失败，报错信息如下：

  ```txt
  > hvigor ERROR: Failed :entry:default@SignHap... 

  > hvigor ERROR: 00303242 Configuration Error

  Error Message: Signature material verification failed, as: Unsupported state or unable to authenticate data. At file: xxx
  ```
* **问题十二：** 签名报错找不到压缩文件，报错信息如下：

  ```txt
  > hvigor ERROR: Failed :MessageCenter:default@SignModuleRemoteHsp...

  > hvigor ERROR: Tools execution failed.

  xx-xx xx:xx:xx ERROR - hap-sign-tool: error: read zip file failed
  ```
* **问题十三：** 运行安装报错，无签名文件，报错信息如下：

  ```txt
  Install Failed: error: failed to install bundle.
  code:9568320
  error: no signature file.
  ```

## 背景知识

* [自动签名](../harmonyos-guides/ide-signing.md#section18815157237)是一种由系统自动生成签名文件的流程，主要用于简化开发者的操作并提高效率。在HarmonyOS中，自动签名可以帮助开发者快速进行应用的调试和测试。
* 使用场景：自动签名主要适用于开发调试场景，便于开发者在开发过程中进行快速迭代和测试。然而，对于一些特定的情况，如跨设备调试、断网情况下调试或者需要使用特定权限的场景，[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)可能是必需的。

## 问题定位

* **问题一：** 检查signingConfigs的name字段是否超过了64个字符，是否存在特殊字符。
* **问题二：** 检查签名所用文件是否正确。
* **问题三：** 检查自动化签名功能使用次数30天内是否超过150次。
* **问题四：** 签名文件确认无误的话，可能是material文件损坏导致。
* **问题五：** 检查开发者账号有无实名，检查是否有外网权限，检查DevEco Studio设置中的HTTP代理是否为自动检测代理设置。
* **问题六：** 检查本地pc和北京时间是否一致。
* **问题七：** 检查工程级build-profile.json5文件中的signingConfigs下的material字段中存放的自动签名文件；检查AppGallery Connect平台上的调试证书是否达到了数量上限。
* **问题八：** 检查本地是否配置jdk环境。
* **问题九：** 检查build-profile.json5配置。
* **问题十：** 检查IDE是否[识别调试设备](faqs-app-debugging-3.md)。
* **问题十一：** 参考错误码：[00303242 签名材料校验失败](../harmonyos-guides/ide-hvigor-errorcode-00303-1.md#section1728115150102)，检查对应文件位置签名材料是否损坏。
* **问题十二：** 配置[hvigor-config.json5文件](../harmonyos-guides/ide-hvigor-set-options.md)，开启[日志debug](../harmonyos-guides/ide-hvigor-set-options.md#section85176471028)和[堆栈stacktrace信息](../harmonyos-guides/ide-hvigor-set-options.md#section76575554217)，获取日志如下：

  ```txt
  > hvigor Finished :EF_WebView:default@PackageSharedHar... after 741 ms

  > hvigor DEBUG MessageCenter:Signhos_hap 12-17 14:46:44 INFO  - Start sign-app

  > hvigor DEBUG MessageCenter:Signhos_hap 12-17 14:46:45 INFO  - certificate in profile: xxxx

  > hvigor DEBUG MessageCenter:Signhos_hap 12-17 14:46:45 INFO  - sign-app failed

  > hvigor DEBUG MessageCenter:Signhos_hap ERROR: command = java -jar /Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/toolchains/lib/hap-sign-tool.jar sign-app -mode localSign -keystoreFile xxx.p12 -keystorePwd *** -keyAlias xxx -keyPwd *** -signAlg SHA256withECDSA -profileFile xxx.p7b -appCertFile xxx.cer -inFile /xxx/build/cache/default/integrated_hsp/@xxx+xxx@1.3.6/@xxx
  +xxx.hsp -outFile /xxx/build/cache/default/remote_hsp/@xxx+xxx@1.3.6/@xxx+xxx-signed.hsp
  ```

  根据-inFile /xxx/build/cache/default/integrated\_hsp/@xxx+xxx@1.3.6/@xxx +xxx.hsp查看对应文件夹，确认缺失@xxx+xxx@1.3.6，存在@xxx+xxx@1.4.2。
* **问题十三：** 参考错误码：[9568320 签名文件不存在](../harmonyos-guides/bm-tool.md#section9568320-签名文件不存在)，检查工程级build-profile.json5是否正确配置签名。

## 分析结论

* **问题一：** 签名配置名称不能超过64个字符的限制，并且字符串内只能包含字母和数字。
* **问题二：** 签名文件使用错误或文件过期，导致自动签名失败。
* **问题三：** AppGallery Connect平台对自动化签名使用次数有限制，同一个开发者帐号，在最近30天使用自动化签名功能使用次数不能超过150次。
* **问题四：** material文件损坏导致自动签名报错。
* **问题五：** 报错根因是自动签名在生成签名证书时，需要与AppGallery Connect平台进行数据交换，此时会对登录的账号进行数据校验和处理。当发现账号未实名认证、或者其他请求AppGallery Connect平台数据失败的情况、以及HTTP代理未正确配置的情况都会导致这个报错。
* **问题六：** 由于本地pc和服务器时间不一致，导致签名失败。
* **问题七：** 当前存放在.ohos/config文件下的自动签名达到了签名上限；或者是AppGallery Connect平台上的调试证书数量达到了上限。
* **问题八：** 由于本地缺少jdk环境，导致签名失败。
* **问题九：** signingConfigs.name与products.signingConfig不匹配。
* **问题十：** 当前报错代表签名工具无法通过hdc查询到调试设备的udid，有多种可能会导致IDE[无法获取调试设备的udid](faqs-app-debugging-3.md)。
* **问题十一：** 报错签名文件损坏。
* **问题十二：** 缺失相应版本的依赖包，无法签名。
* **问题十三：** 工程级build-profile.json5的products字段内，相应编译产物未正确配置signingConfig。

## 修改建议

* **问题一：** 签名配置名称不能超过64个字符的限制，并且字符串内只能包含字母和数字，根据该规则修改build-profile.json文件中signingConfigs的name字段。
* **问题二：** 项目根目录build-profile.json5里的signingConfigs配置信息全部删除，重新打开Project Structure配置自动签名。
* **问题三：**
  + 方案一：建议相同BundleName的应用，如果设备无变化，请使用同一套签名文件信息，不要反复进行重签名操作。
  + 方案二：更换其它开发者帐号进行登录，然后进行签名。
  + 方案三：AppGallery Connect平台限制同一个帐号，在近30天使用自动化签名的次数不能超过150次。因此，可以等待一段时间后，重新使用该帐号进行签名。
* **问题四：** material文件损坏，删除签名文件所在地的material文件后重新签名，若还是不行则删除material文件和签名文件后重新签名，项目根目录build-profile.json5里的signingConfigs中查看.ohos下的config文件存放位置。
* **问题五：**
  + 账号未实名认证：

    如报错所示，当前登录的华为开发者账号需要实名认证才能在AppGallery Connect平台中创建项目获取签名证书。[实名认证](../start/itrna-0000001076878172.md)建议使用人脸认证、银行卡认证。
  + 网络环境无法下载p7b证书（无外网权限）：

    自动签名就是手动签名的自动化。手动签名在下载p7b证书的步骤，需要用到外网权限，同理自动签名也需要。所以如果在确认账号已实名认证的签名前提下，通过手动在AppGallery Connect平台上验证是否能够下载p7b来排查是否为外网权限问题。
  + DevEco Studio设置中的HTTP代理选择的是自动检测代理设置：

    需设置为无代理模式或手工配置代理模式。
* **问题六：**

  出现该报错是由于pc的系统时间与北京时间不一致。请将pc的系统时间与北京时间调整为一致，然后重新签名。步骤如下：

  1. 关闭自动签名弹窗。
  2. 右键点击电脑右下角时间，选择（调整日期、时间）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/75ZdcBkeRwimh2eyHZMIEQ/zh-cn_image_0000002658928595.png "点击放大")
  3. 点击立即同步。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/4TxLLZpDQuS0XZfWeZg96A/zh-cn_image_0000002658808645.png "点击放大")
  4. 同步完成后会有√。此操作需要电脑联网！

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/Sf6oadMDTACgUS4CXoy7lA/zh-cn_image_0000002628569280.png "点击放大")
  5. 重新自动签名即可。
  6. 使用Mac电脑开发时，如果以上方法仍未解决问题，需关闭自动同步时间，手动修改系统时间与北京时间一致，精确到秒。
  7. 如果重置时间后仍不能正确签名，有可能是因为VPN把系统时间覆盖了。请检查是否打开或打开过VPN。若有，请重置一下VPN或把VPN的节点设置到国内IP。
* **问题七：**将.ohos下的config文件夹整个删除后，重新签名；若还是报错，就尝试删除一个AppGallery Connect平台上的调试证书。
* **问题八：**在本地安装jdk，配置java环境，即可自动签名。
* **问题九：**signingConfigs.name与products.signingConfig匹配，同时检查文件路径是否含特殊字符或空格。
* **问题十：**在项目根目录下local.properties里SDK路径下的toolchains文件夹中（确保有可执行的hdc工具）手动执行hdc shell bm get --udid，确认下是否能够正确获取设备udid，若获取不到则重新刷设备镜像或更换设备。
* **问题十一：**删除build-profile.json5中签名信息，点击File > Project Structure > Project > Signing Configs重新签名。
* **问题十二：**配置工程级oh-package.json5的[overrides](../harmonyos-guides/ide-oh-package-json5.md#zh-cn_topic_0000001792256137_overrides)字段，将版本设置为已有版本。
* **问题十三：**工程级build-profile.json5中，[products](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619)相应产物添加signingConfig配置，并与[signingConfigs](../harmonyos-guides/ide-hvigor-build-profile-app.md#section153288223224)关联。

## 常见FAQ

Q：自动签名能否多人共用？

A：build-profile.json5文件里signingConfigs是每个人自己的签名，所以自动签名无法共用。

Q：在30天内使用自动化签名的次数不能超过150次，如何申请增加自动签名次数？

A：发公邮agconnect@huawei申请增加自动签名次数，邮件正文提供申请的应用名称、应用ID、账号ID、申请原因即可。

Q：自动签名失败提示网络问题，实际网络并无问题，经常时好时坏怎么办？

A：将签名信息复制本地，不同项目使用同一个签名。

Q：自动签名生成的签名文件是否支持修改默认路径？

A：自动签名生成的签名文件不支持修改默认路径。
