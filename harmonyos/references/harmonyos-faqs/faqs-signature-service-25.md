---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-25
title: 手动签名失败的常见问题
breadcrumb: FAQ > DevEco Studio > 签名服务 > 手动签名失败的常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6fde6bad558c20dead972779aaa782dafc49fb22cb5ec0cafd73e674033ca5a8
---

## 问题现象

本地调试或者打包时报错手动签名失败。

**场景一**：使用hdc命令将应用安装到手机时出现以下报错信息：

```txt
queuesize:0, msg:error: failed to install bundle. code:9568393 error: verify code signature failed.
```

**场景二**：配置签名的时候报错：

```txt
Decryption failed. Verify the encryption password, or delete the material folder where the .p12 file is located and select Automatically generate signature to re-sign the file.
```

**场景三**：配置签名弹窗报错：

```txt
Encryption failed. Delete the material folder where the .p12 file is located and select Automatically generate signature to re-sign the file.
```

**场景四**：手动签名报错：

```txt
KeyAlias {XXX} is not exist in {XXX.p12}
```

**场景五**：签名时报错：

```txt
Exception in thread "main" java.lang.NumberFormatException: For input string: "TG"
```

**场景六**：使用调试证书手动签名打包时，报错9568322，“error: signature verification failed due to not trusted app source.”。

**场景七**：在开发完成后，申请、下载证书及对应Profile，期望能打包并正式发布应用，在工具中单击Build->Build Hap(s)/APP(s)->Build APP(s)后报错：

```txt
hvigor ERROR: Failed :entry:default@SignHap...
hvigor ERROR: Tools execution failed.
08-22 18:07:18 ERROR - hap-sign-tool: error: Signature verify failed
Detail: Please check the message from tools.
hvigor ERROR: BUILD FAILED in 12 s 170 ms
```

**场景八**：本地java环境是jdk11，打包报错提示签名失败：

```txt
ERROR: Tools execution failed.
02-26 10:20:24 ERROR - hap-sign-tool: error: Init keystore failed: Integrity check failed: java.security.NoSuchAlgorithmException: Algorithm HmacPBESHA256 not available
* Try the following:
> The key store file does not exist, please check the key store file path.
> Incorrect keystore password, please input the correct plaintext password.
> The keystore was created by a newer JDK version, please use the same JDK version
Detail: Please check the message from tools.
```

**场景九**：在AGC上配置项目的SHA256指纹，其中在[手动生成签名证书指纹](../hiai-Guides/signature-information-harmonyos-0000001246159273.md#section819817413167)时报错：

```txt
C:\Program Files\Huawei\jdk1.8.0_242\bin>keytool -list -v -keystore D:\myProject\cer1\.p12
输入密钥库口令:
keytool 错误:java.io.IOException: Invalid keystore format
java.io.IOException: Invalid keystore format
at sun.security.provider.JavakeyStore.engineLoad(JavakeyStore.java:663)
at sun.security.provider.JavakeyStore$JKS.engineLoad(JavaKeyStore.java:56)
at sun.security.provider.KeyStoreDelegator.engineLoad(KeyStoreDelegator. java:224)
at	:sun.security.provider.JavaKeyStore$DualFormatJKS.engineLoad(JavaKeyStore.java:70)
at java.security.KeyStore.load(KeyStore.java:1445)
at sun.security.tools.keytool.Main.doCommands(Main.java:926)
at	: sun.security.tools.keytool.Main.run(Main.java:366)
at sun security.tools.keytool.Main.main(Main.java:359)
```

## 背景知识

* [手动签名](../harmonyos-guides/ide-signing.md#section297715173233)。
* [bm工具错误码](../harmonyos-guides/bm-tool.md#bm工具错误码)。
* [发布应用](../app/agc-help-releaseharmony-0000001933963166.md)：完成HarmonyOS应用开发、调试与测试后，开发者便可以在AGC正式提交应用上架申请。发布应用涉及申请发布证书、申请发布Profile和正式发布HarmonyOS应用三大步骤，证书和Profile是可能造成上述问题现象的原因之一。
* 通过DevEco Studio[生成密钥和证书请求文件](../harmonyos-guides/ide-publish-app.md#section1079214271414)时，实际是用IDE内置的jdk生成的密钥库。

## 问题定位

**场景一**：

根据[bm工具错误码](../harmonyos-guides/bm-tool.md#bm工具错误码)确定为[9568393 验证代码签名失败](../harmonyos-guides/bm-tool.md#section9568393-验证代码签名失败)。

**场景二**：

分析问题现象报错信息可知：解密失败，密码错误。

**场景三**：

分析问题现象报错信息可知：加密失败，删除.p12文件同目录下material文件夹，重新签名。

**场景四**：

根据KeyAlias {XXX} is not exist in {XXX.p12}可知：KeyAlias在XXX.p12中不存在。

**场景五**：

根据java.lang.NumberFormatException: For input string: "TG"可知：输入字符串有未格式化异常，排查密码是否转义。

**场景六**：

根据[bm工具错误码](../harmonyos-guides/bm-tool.md#bm工具错误码)确定为[9568322 由于应用来源不可信，签名验证失败](../harmonyos-guides/bm-tool.md#section9568322-由于应用来源不可信签名验证失败)。

**场景七**：

* 检查证书过期、误用了已吊销的证书。
* 检查证书文件和调试Profile文件是否配套使用。
* 检查调试证书和调试Profile文件的文件名是否包含中文。参考内容：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/uY-F1LM1Sge8k2oAQZpGIg/zh-cn_image_0000002628569308.png "点击放大")

**场景八**：

* 密码输入错误。
* 密钥(KeyAlias)密码和密钥库(p12)密码颠倒使用。
* 检查当前jdk版本在生成密钥文件后是否升级过。

**场景九**：

1. 查资料可知这个错误有可能是因为不同jdk版本间不兼容。
2. 查看DevEco Studio的jdk版本为17.0.12：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/kwz3Mkg8Tji3JaFDHpRshQ/zh-cn_image_0000002658928625.png "点击放大")
3. 查看本地jdk版本为1.8.0：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/RCvsViksSv2BDI1-wf8XMg/zh-cn_image_0000002628409404.png "点击放大")
4. 将本地的jdk升级到与IDE一致的版本后，再手动获取证书指纹，可以获取到：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/m9u2mpbGQp-U5JQpLoDfgA/zh-cn_image_0000002658808673.png "点击放大")

## 分析结论

**场景一**：

根据报错信息和错误码，分析可能的原因有两个：

* 当前编译构建使用的SDK版本过旧，不支持代码签名，与设备镜像版本不匹配。
* 应用包安装时HSP的bundleName与HAP的bundleName不一致导致。

**场景二**：

配置签名要确保密码正确，如果忘记密码则重新生成p12文件。

**场景三**：

加密失败，生成的加密信息错误。

**场景四**：

生成.p12证书文件时设置的KeyAlias和配置时的KeyAlias不一致。

**场景五**：

.p12证书文件的密码中含有需要转义的特殊字符。

**场景六**：

可能原因如下：

* 签名时使用了[发布Profile文件](../app/agc-help-release-profile-0000002248341090.md)。发布证书签名的应用不能启动调试或运行。
* 在[build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile-app.md)文件中，配置的Profile文件与.cer文件不匹配。
* 签名中未包含该调试设备的UDID。

**场景七**：

* 使用的证书状态“非生效”状态。
* 使用的证书类型与Profile类型不匹配：Build Hap(s)/APP(s)时，选用了发布证书+调测Profile，或调测证书+发布Profile。
* 调试证书和调试Profile文件是中文命名，本地调试配置这两个文件路径时发生乱码，把文件名修改成英文后重新进行配置会报此错误。

**场景八**：

当前报错是生成keystore的jdk版本和执行签名的jdk版本不一致导致的。

**场景九**：

IDE生成的密钥库与手动生成密钥指纹使用的jdk版本不一致，导致不兼容出现报错。

## 修改建议

**场景一**：

针对可能的原因，分别按照以下方式进行排查：

* 前往下载中心下载安装最新DevEco Studio版本。
* 使用打包工具中包名归一化指令修改包名，将HSP的bundleName与HAP的bundleName保持一致。

**场景二**：

配置签名密码和生成的p12文件要一致。具体步骤可参考：[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)。

**场景三**：

删除.p12文件同目录下生成的material文件夹后，重新签名。

**场景四**：

生成.p12证书文件时设置的KeyAlias和配置时的KeyAlias一致。可以用指令keytool -list -keystore xxx.p12查询配置的KeyAlias。

**场景五**：

修改p12的密码不带特殊字符或用转义后的字符。

**场景六**：

* 使用[调试Profile文件](../app/agc-help-debug-profile-0000002248181278.md)重新签名应用。
* 确保Profile文件是由配置中的.cer文件生成的，可以登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“证书、APP ID和Profile”，在左侧导航栏选择“证书、APP ID和Profile > Profile”，进入“Profile”页面，选择配置的Profile文件，右侧操作点击“查看”，确认“查看Profile”页面中“归属证书”是否与配置的.cer文件一致。
* 在连接设备后，重新为应用进行自动签名。

**场景七**：

* 核查证书状态，若证书已过期，请重新申请新的证书及Profile。
* 重新选取对应类型的证书及Profile，再次构建应用包。
* 在AGC平台生成对应的调试证书和调试Profile文件时，建议使用英文命名，后续本地调试配置文件路径时就不会产生乱码，避免了修改调试文件名，会避免因与云端文件不一致导致签名失败。

**场景八**：

保证电脑中jdk版本与DevEco Studio中jdk版本一致，重启daemon。

**场景九**：

将本地的jdk升级到与IDE一致的版本，如本例子中就是17.0.12。

## 常见FAQ

Q：如何使用keytool命令行工具获取.p12证书文件内容？

A：打开DevEco Studio Terminal窗口，使用keytool命令行工具验证密钥库文件口令，示例：keytool -list -keystore xxx.p12 -storepass ${Store password}。

Q：为什么使用的发布证书与发布Profile构建出来的包不能在手机上直接运行？

A：若需要本地安装到手机上，请使用调试证书签名；若需要上架应用、上传APP的时候，才需要使用发布证书。

Q：基于HarmonyOS Next版本，使用同一个CSR签名文件在华为平台配置发布证书和调试证书，生产出两个对应的.p7b证书，两个文件大小不一。如果在真机上获取APPID是否一致？

A：调试证书和发布证书生成的Profile文件，里面的应用信息是一样的，APPID是一致的，目前只有调试Profile有udid，发布Profile没有。

Q：证书与Profile确认都为发布类型，但为什么运行后还是报错？

A：发布证书以及发布Profile，应该Build->Build Hap(s)/APP(s)->Build APP(s)包用于上架应用市场，不能点运行直接本地跑，否则会报错。

Q：应用打包成APP时，里面的Hap包为何没有签名？

A：上架的时候应用市场会拆包重签名的，APP是上架用的，对APP签名就可以上架。应用市场校验完APP签名之后，会解压获取所有的Hap，再对Hap签名，所以不用在IDE里签名。

Q：IDE工具可正常运行，为什么使用验签工具报错：Failed to load keystore when sign with exception: keystore password was incorrect?。

A：配置的storePassword和keyPassword非密码原文，需使用原文密码。

Q：签名密钥库文件口令错误，打包签名提示：Init keystore failed: keystore password was incorrect错误。

A：使用正确的密钥库文件口令，密钥库文件口令验证方式如下：

打开DevEco Studio Terminal窗口，使用keytool命令行工具验证密钥库文件口令，示例：

keytool -list -keystore ${Store file} -storepass ${Store password}。

Q：每次使用p12文件生成的csr文件是否会变更？

A：生成的csr文件是会变更，这是正常的，因为里面有盐值。
