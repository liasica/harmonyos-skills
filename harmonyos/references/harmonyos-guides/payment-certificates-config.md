---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-certificates-config
title: 准备证书
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > 准备证书
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ed594f6e31d0b045b543fb8e3cf6d3b0912f24b8746a24042444cb6d08c39997
---

开发者接入华为支付开放API接口，需要通过证书来对请求内容及响应内容做签名和验证签名，以保证请求的安全性和可靠性。

本文将介绍接入过程中相关证书的作用和获取方法。在准备证书前，请在[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)入网，具体请参见[商户入网](../hwzf-jieruliucheng-0000001251448455.md)。

需准备证书：商户证书、华为支付证书（公钥）。

## 证书说明

证书使用如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/H-uwXPxwTJmv8557JM5KeQ/zh-cn_image_0000002552959080.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=F5A7378FBF6F340E061ED3655B78F8C775DD960B3407215BFD161F4BA69C514E)

## 商户证书

商户证书是指由商户自行生成（参见[生成商户证书](payment-certificates-config.md#生成商户证书)）或申请（可自行选择符合资质的CA认证机构申请证书）的，包含商户公钥和私钥信息的证书。

私钥用于商户在华为支付开放API接口请求过程中的[签名](../harmonyos-references/payment-rest-overview.md#签名规则)，公钥用于提供给华为支付侧进行请求验签。

该证书文件要求为pem格式，支持RSA和SM2两种算法类型的证书。

**证书私钥**

商户自行生成或申请商户证书时，会配套生成商户私钥。

* 商户私钥用于商户对华为支付开放API请求中的信息进行签名。
* 请妥善保管好商户私钥文件，不要把私钥文件暴露在公共场合，如上传到Github，写在客户端代码等。

**证书公钥**

商户自行生成或申请商户证书时，会配套生成商户公钥。

* 商户需将生成的证书公钥上传到[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)来获取证书ID，证书ID为请求华为支付开放API接口时请求头鉴权信息[PayMercAuth](../harmonyos-references/payment-model.md#paymercauth)对象中的authId字段以及订单信息参数[orderStr](../harmonyos-references/payment-model.md#orderstr)中的auth\_id字段。
* 证书上传（参见[上传商户证书](payment-certificates-config.md#上传商户证书)）后，可以在“商户中心 > 证书管理 > 上传商户证书 > 证书ID”处获取。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/ZPCnga4mRJurNVkJV-5AJA/zh-cn_image_0000002583479081.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=5AE7133B5B2F45A83EA4C88D89A819F2AA5142859096B69624CD0E96440D90EC)

### 生成商户证书

**方式1：使用JavaScript的库线下生成（生成RSA算法类型证书为例，推荐方法）**

1. 配置Node.js执行环境。下面以Windows开发环境为例：

   登录[Node.js](https://nodejs.org/en/download/)官方网站，下载Node.js软件包。请选择LTS版本，并根据电脑操作系统选择对应的软件包。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/GdzWLwneRN-h0G3Hq2CN-g/zh-cn_image_0000002552799432.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=0151A09F66243BC1B18042177040762DEFF845B39766B5C86741F73BB4B971A1)

   双击下载后的软件包进行安装。全部按照默认设置点击“Next”，直至“Finish”。安装过程中，Node.js会自动在系统的path环境变量中配置node.exe的目录路径。

   说明

   如果安装Node.js没有选择默认安装目录，则需要在系统变量“path”中手动添加环境变量信息“我的电脑>属性>高级系统设置>环境变量”增加Node.js的安装路径。

   打开命令行工具，输入**node -v**命令，能正常查询Node.js的版本号，说明Node.js执行环境配置完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/cO3ekOHDSba7Tiizx0hgAA/zh-cn_image_0000002583439127.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=4B9596ED45FE7E231F1756FB097FD4F067825AE1E71210233C42EAD9468C7E32)
2. 使用文本编辑器新建文件（编码为UTF-8），拷贝以下代码到文件中并保存命名为“generateKeyPair.js”。

   ```
   1. const crypto = require('crypto');
   2. // 生成密钥对
   3. const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
   4. modulusLength: 3072, // 密钥长度，不少于3072
   5. publicKeyEncoding: {
   6. type: 'spki', // 公钥编码格式
   7. format: 'pem' // 公钥输出格式
   8. },
   9. privateKeyEncoding: {
   10. type: 'pkcs8', // 私钥编码格式
   11. format: 'pem' // 私钥输出格式
   12. }
   13. });
   14. console.info('生成的公钥：');
   15. console.info(publicKey);
   16. console.info('生成的私钥：');
   17. console.info(privateKey);
   ```
3. 打开命令行工具，进入generateKeyPair.js所在目录，执行**node generateKeyPair.js**命令。
4. 从结果中拷贝生成的公私钥并保存。结果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/rJPiJXFSQyeJFUGLTUshKg/zh-cn_image_0000002552959082.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=1E1F00D7D2E0351A3F4CC98900DD698FC65BF2AF041FF680032805D80FDABCC2)

**方式2：使用在线工具生成**

开发者可自行搜索使用相关开源的在线工具或网站生成相应证书公私钥对。

注意

生成公私钥为敏感操作，请谨慎使用，建议开发者自行生成密钥对。

### 上传商户证书

证书公钥生成后须商户手动上传到[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)，用于华为支付服务器对支付请求验证签名。

说明

1. 私钥信息用于对发送请求的内容签名，请妥善保管，请勿公开泄露。
2. 商户成功登录[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)后，须在证书管理中上传商户证书，上传完商户证书后商户方可进行交易。证书必须与商户号相匹配且是有效的。

上传的证书公钥需要满足如下要求：

* 后缀要求：[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)接收的公钥证书格式为“\*.pem”。
* 格式要求：生成RSA公私钥时，密钥长度要求不小于3072，密钥格式为PKCS#8。

请登录[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)，在“证书管理 > 上传商户证书”模块进行商户证书公钥上传。

待上传公钥信息示例：

```
1. -----BEGIN PUBLIC KEY-----
2. MIIBIjANBgkq*********************************vW7gQTM8BHFTezQjdRI
3. A7xka2TaVHt***********************************rOA3P5rew9cO96q/7Z
4. kQ6lRd3oVsf************************************rGYCrA2RVgr79mRx+
5. s22qfA5FdTC*************************************i6I2cRVb1grBQphR
6. yFBxCGC/NeV*************************************K1QM1SC4GCORHocS
7. MQvApBQwQF9*************************************eEQvwpVfFxg4dGBz
8. DQIDAQAB
9. -----END PUBLIC KEY-----
```

## 华为支付证书

华为支付证书是指由华为支付提供的，包含华为支付平台标识、公钥信息的证书。该证书算法为SM2。

* 商户请通过[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)下载华为支付证书。
* 华为支付证书中的公钥用于商户对回调通知中的信息进行验签。

### 下载华为支付证书

登录[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)后，通过“商户中心 > 证书管理 > 华为支付证书”页签进行华为支付证书下载，该证书用于校验华为支付给商户业务系统发送的信息，如支付结果信息等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/pyMVa-JnSyGGCtuujF-z7g/zh-cn_image_0000002583479083.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=FA5FE07C9A0B4AB24CBCB2E8764B1842B2D356407AFCFCC89480955FAA5B50EE)
