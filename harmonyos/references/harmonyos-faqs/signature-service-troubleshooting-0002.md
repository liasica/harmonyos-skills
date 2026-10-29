---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/signature-service-troubleshooting-0002
title: 手动签名失败问题排查与解决
breadcrumb: FAQ > DevEco Studio > 签名服务 > 故障排查 > 手动签名失败问题排查与解决
category: harmonyos-faqs
scraped_at: 2026-10-30T07:59:19+08:00
doc_updated_at: 2026-10-29
content_hash: sha256:2d4cc6ad4c413d6b8f67872a5fc1f327042f4aba3b451597d1728c62932fecd3
---

## hdc安装应用报错9568393

### 问题现象

使用hdc命令将应用安装到手机时出现以下报错信息：

```txt
queuesize:0, msg:error: failed to install bundle. code:9568393 error: verify code signature failed.
```

### 定位过程

根据[bm工具错误码](../harmonyos-guides/bm-tool.md#bm工具错误码)确定为[9568393 验证代码签名失败](../harmonyos-guides/bm-tool.md#section9568393-验证代码签名失败)。

### 分析结论

根据报错信息和错误码，分析可能的原因有两个：

* 当前编译构建使用的SDK版本过旧，不支持代码签名，与设备镜像版本不匹配。
* 应用包安装时HSP的bundleName与HAP的bundleName不一致导致。

### 修改建议

针对可能的原因，分别按照以下方式进行排查：

* 前往下载中心下载安装最新DevEco Studio版本。
* 使用打包工具中包名归一化指令修改包名，将HSP的bundleName与HAP的bundleName保持一致。

## 配置签名报错Decryption failed

### 问题现象

配置签名的时候报错：

```txt
Decryption failed. Verify the encryption password, or delete the material folder where the .p12 file is located and select Automatically generate signature to re-sign the file.
```

### 定位过程

分析问题现象报错信息可知：解密失败，密码错误。

### 分析结论

配置签名要确保密码正确，如果忘记密码则重新生成.p12文件。

### 修改建议

配置签名密码和生成的.p12文件要一致。具体步骤可参考[手动签名](../doccenter-deveco-studio/ide-signing.md#section297715173233)。

## 配置签名弹窗报错Encryption failed

### 问题现象

配置签名弹窗报错：

```txt
Encryption failed. Delete the material folder where the .p12 file is located and select Automatically generate signature to re-sign the file.
```

### 定位过程

分析问题现象报错信息可知：加密失败，删除.p12文件同目录下material文件夹，重新签名。若删除material文件夹后问题仍存在，则可能是本地.p12文件未更新。

### 分析结论

加密失败，生成的加密信息错误。本地.p12文件未更新时也会导致此问题。

### 修改建议

删除.p12文件同目录下生成的material文件夹后，重新签名。若删除material文件夹后问题仍未解决，删除本地的.p12文件，重新下载并配置签名。

## 手动签名报错KeyAlias不存在

### 问题现象

手动签名报错：

```txt
KeyAlias {XXX} is not exist in {XXX.p12}
```

### 定位过程

根据KeyAlias {XXX} is not exist in {XXX.p12}可知：KeyAlias在XXX.p12中不存在。

### 分析结论

生成.p12证书文件时设置的KeyAlias和配置时的KeyAlias不一致。

### 修改建议

生成.p12证书文件时设置的KeyAlias和配置时的KeyAlias一致。可以用指令keytool -list -keystore xxx.p12查询配置的KeyAlias。

## 签名报错NumberFormatException

### 问题现象

签名时报错：

```txt
Exception in thread "main" java.lang.NumberFormatException: For input string: "TG"
```

### 定位过程

根据java.lang.NumberFormatException: For input string: "TG"可知：输入字符串有未格式化异常，排查密码是否转义。

### 分析结论

.p12证书文件的密码中含有需要转义的特殊字符

### 修改建议

修改.p12的密码不带特殊字符或用转义后的字符。

## 调试证书签名打包报错9568322

### 问题现象

使用调试证书手动签名打包时，报错9568322，"error: signature verification failed due to not trusted app source."。

### 定位过程

根据[bm工具错误码](../harmonyos-guides/bm-tool.md#bm工具错误码)确定为[9568322 由于应用来源不可信，签名验证失败](../harmonyos-guides/bm-tool.md#section9568322-由于应用来源不可信签名验证失败)。

### 分析结论

可能原因如下：

* 签名时使用了[发布Profile文件](../app/agc-help-release-profile-0000002248341090.md)。发布证书签名的应用不能启动调试或运行。
* 在[build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile-app.md)文件中，配置的Profile文件与.cer文件不匹配。
* 签名中未包含该调试设备的UDID。

### 修改建议

* 使用[调试Profile文件](../app/agc-help-debug-profile-0000002248181278.md)重新签名应用。
* 确保Profile文件是由配置中的.cer文件生成的，可以登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择"证书、APP ID和Profile"，在左侧导航栏选择"证书、APP ID和Profile > Profile"，进入"Profile"页面，选择配置的Profile文件，右侧操作点击"查看"，确认"查看Profile"页面中"归属证书"是否与配置的.cer文件一致。
* 在连接设备后，重新为应用进行自动签名。

## 构建报错Signature verify failed

### 问题现象

在开发完成后，申请、下载证书及对应Profile，期望能打包并正式发布应用，在工具中单击Build->Build Hap(s)/APP(s)->Build APP(s)后报错：

```txt
hvigor ERROR: Failed :entry:default@SignHap...
hvigor ERROR: Tools execution failed.
08-22 18:07:18 ERROR - hap-sign-tool: error: Signature verify failed
Detail: Please check the message from tools.
hvigor ERROR: BUILD FAILED in 12 s 170 ms
```

### 定位过程

* 检查证书过期、误用了已吊销的证书。
* 检查证书文件和调试Profile文件是否配套使用。
* 检查调试证书和调试Profile文件的文件名是否包含中文。参考内容：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Bmn4XZroQIexjXvNvmgicw/zh-cn_image_0000002774463322.png "点击放大")

### 分析结论

* 使用的证书状态"非生效"状态。
* 使用的证书类型与Profile类型不匹配：Build Hap(s)/APP(s)时，选用了发布证书+调测Profile，或调测证书+发布Profile。
* 调试证书和调试Profile文件是中文命名，本地调试配置这两个文件路径时发生乱码，把文件名修改成英文后重新进行配置会报此错误。

### 修改建议

* 核查证书状态，若证书已过期，请重新申请新的证书及Profile；
* 重新选取对应类型的证书及Profile，再次构建应用包。
* 在HarmonyOS 开发者中心平台生成对应的调试证书和调试Profile文件时，建议使用英文命名，后续本地调试配置文件路径时就不会产生乱码，避免了修改调试文件名，会避免因与云端文件不一致导致签名失败。

## jdk11环境下打包报错签名失败

### 问题现象

本地java环境是jdk11，打包报错提示签名失败：

```txt
  ERROR: Tools execution failed.
  02-26 10:20:24 ERROR - hap-sign-tool: error: Init keystore failed: Integrity check failed: java.security.NoSuchAlgorithmException: Algorithm HmacPBESHA256 not available
  * Try the following:
  > The key store file does not exist, please check the key store file path.
  > Incorrect keystore password, please input the correct plaintext password.
  > The keystore was created by a newer JDK version, please use the same JDK version
  Detail: Please check the message from tools.
```

### 定位过程

* 密码输入错误。
* 密钥(KeyAlias)密码和密钥库(.p12)密码颠倒使用。
* 检查当前jdk版本在生成密钥文件后是否升级过。

### 分析结论

当前报错是生成keystore的jdk版本和执行签名的jdk版本不一致导致的。

### 修改建议

保证电脑中jdk版本与DevEco Studio中jdk版本一致，重启daemon。

## 手动生成签名证书指纹报错Invalid keystore format

### 问题现象

在HarmonyOS 开发者中心上配置项目的SHA256指纹，其中在[手动生成签名证书指纹](../hiai-Guides/signature-information-harmonyos-0000001246159273.md#section819817413167)时报错：

```txt
C:\Program Files\Huawei\jdk1.8.0_242\bin>keytool -list -v -keystore D:\myProject\cer1\.p12
输入密钥库口令:
keytool 错误:java.io.IOException: Invalid keystore format
java.io.IOException: Invalid keystore format
at sun.security.provider.JavakeyStore.engineLoad(JavakeyStore.java:663)
at sun.security.provider.JavakeyStore$JKS.engineLoad(JavaKeyStore.java:56)
at sun.security.provider.KeyStoreDelegator.engineLoad(KeyStoreDelegator. java:224)
at sun.security.provider.JavaKeyStore$DualFormatJKS.engineLoad(JavaKeyStore.java:70)
at java.security.KeyStore.load(KeyStore.java:1445)
at sun.security.tools.keytool.Main.doCommands(Main.java:926)
at sun security.tools.keytool.Main.run(Main.java:359)
at sun security.tools.keytool.Main.main(Main.java:359)
```

### 定位过程

1. 查资料可知这个错误有可能是因为不同jdk版本间不兼容。
2. 查看DevEco Studio的jdk版本为17.0.12：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/sY160ZyKTFOZ6Et6IFnCbg/zh-cn_image_0000002803623261.png "点击放大")
3. 查看本地jdk版本为1.8.0：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/26eczOHCTz2RYUpA6cnlVA/zh-cn_image_0000002803783177.png "点击放大")
4. 将本地的jdk升级到与IDE一致的版本后，再手动获取证书指纹，可以获取到。

### 分析结论

IDE生成的密钥库与手动生成密钥指纹使用的jdk版本不一致，导致不兼容出现报错。

### 修改建议

将本地的jdk升级到与IDE一致的版本，如本例子中就是17.0.12。

## 签名调试元服务报错11111002

### 问题现象

签名调试元服务时报错：

```txt
ERROR: 11111002 Certificates Error
```

### 定位过程

根据报错信息ERROR: 11111002 Certificates Error可知：证书相关配置存在问题，需排查证书格式内容和签名参数KeyAlias的值是否正确。

### 分析结论

可能原因如下：

* 证书格式内容不正确。
* 签名参数KeyAlias的值不正确。

### 修改建议

* 检查证书格式内容是否正确。
* 检查参数KeyAlias的值是否正确。
