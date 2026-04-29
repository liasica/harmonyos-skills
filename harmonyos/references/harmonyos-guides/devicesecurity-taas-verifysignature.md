---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-taas-verifysignature
title: 验证签名
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 可信应用服务 > 签名验证 > 验证签名
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1c8259f9d7eba629b102d5b0d4c66ad14d3397bb566aefa2c5d8481501ee3446
---

如果需要在端侧校验安全图像数据或安全地理位置数据签名的有效性，可以使用[Crypto Architecture Kit](crypto-architecture-kit-intro.md)，使用方法请参考“[使用ECDSA密钥对签名验签](crypto-ecdsa-sign-sig-verify.md)”章节。

说明

推荐开发者在服务器端完成安全图像或安全地理位置的签名验证，请参考“[Device Certificate Kit 设备真实性证明服务器端开发](device-attestation-servers.md)”。

## 获取签名数据

### 安全摄像头图像数据格式

安全图像数据的结构如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/zfYlmX4cRt-L9igwS8KTqA/zh-cn_image_0000002589244693.png?HW-CC-KV=V1&HW-CC-Date=20260429T053131Z&HW-CC-Expire=86400&HW-CC-Sign=0A0EB100EAED47E1800609353B57F49330E862013A4671F56AD1AB2947CABE35)

其中，用户数据和图像数据为被签名的原始数据，图像数据长度固定为460800字节，签名数据是Base64编码的签名结果，开发者需要解析出这些数据用来验证安全图像数据签名。参考代码如下：

```
1. import { util } from '@kit.ArkTS';

3. // 获取被签名的原始数据
4. const secureImageBuffer = new ArrayBuffer(461844); // 实际使用时请替换为Camera Kit获取到的安全图像buffer
5. const view = new DataView(secureImageBuffer);
6. const imageBufferLength = 460800; // 安全图像buffer长度固定为460800
7. const userDataLength = view.getUint32(0, true); // 获取用户数据长度
8. const originData = secureImageBuffer.slice(4, 4 + userDataLength + imageBufferLength);
9. // 获取签名结果
10. const maxSignatureBufferLength = 512;
11. const signatureBuffer = secureImageBuffer.slice(4 + userDataLength + imageBufferLength,
12. 4 + userDataLength + imageBufferLength + maxSignatureBufferLength);
13. const signatureString = String.fromCharCode(...new Uint8Array(signatureBuffer).filter(code => code !== 0));
14. const base64Helper = new util.Base64Helper();
15. const signatureData = base64Helper.decodeSync(signatureString);
```

### 压缩、裁剪后安全图像数据格式

压缩、裁剪处理后返回的安全图像数据的结构如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/N-Q52rLJTDaBVtP3DIgPTA/zh-cn_image_0000002558764888.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053131Z&HW-CC-Expire=86400&HW-CC-Sign=2B64DB45D0831E0D266D27DA7531EF85ABDA9D6CF4ACF5BFB1D0A9B6B081CBA4)

返回的处理后安全图像数据具体包含：

1. 魔数Magic，其值当前默认为 0x53494D47，开发者可以通过检查Magic字段来验证返回的图像数据的正确性。
2. 版本Version，其值当前默认为 1，开发者可以通过检查Version字段来验证返回的图像数据的正确性。
3. 用户数据长度（16到127 Bytes之间）和用户数据。其中，用户数据是开发者在调用initializeAttestContext初始化证明会话时，传入的相关数据。
4. 图像数据长度，图像宽度（单位为：pixel，取值范围在0到640之间），图像高度（单位为：pixel，取值范围在0到480之间）和图像数据。
5. 签名数据，是Base64编码的签名结果。

其中，签名的原始数据由用户数据和图像数据组成，开发者需要解析出这些数据用来验证安全图像数据签名。参考代码如下：

```
1. import { util } from '@kit.ArkTS';

3. let offset = 0;
4. const secureImageBuffer = new ArrayBuffer(461844); // 实际使用时请替换为Camera Kit获取到的安全图像buffer
5. const view = new DataView(secureImageBuffer);
6. const magic = view.getUint32(offset, true); // 获取安全图像的Magic字段，该值默认为 0x53494D47
7. offset += 4;
8. const version = view.getUint32(offset, true); // 获取安全图像的Version字段，该值默认为 1
9. offset += 4;
10. const userDataLength = view.getUint32(offset, true); // 获取用户数据长度
11. offset += 4;
12. const userdata = secureImageBuffer.slice(offset, offset + userDataLength);
13. offset += userDataLength;
14. const imageLen = view.getUint32(offset, true); // 获取压缩、裁剪处理后的图像数据长度
15. offset += 4;
16. const imageWidth = view.getUint32(offset, true); // 获取图像的宽度，单位为像素
17. offset += 4;
18. const imageHeight = view.getUint32(offset, true); // 获取图像的高度，单位为像素
19. offset += 4;
20. const imageBuffer = secureImageBuffer.slice(offset, offset + imageLen);
21. offset += imageLen;
22. // 获取被签名的原始数据
23. const totalLength = userdata.byteLength + imageBuffer.byteLength;
24. const originData = new Uint8Array(new ArrayBuffer(totalLength));
25. originData.set(new Uint8Array(userdata), 0);
26. originData.set(new Uint8Array(imageBuffer), userdata.byteLength);
27. // 获取签名结果
28. const maxSignatureLength = 512;
29. const signatureBuffer = secureImageBuffer.slice(offset, offset + maxSignatureLength);
30. const signatureString = String.fromCharCode(...new Uint8Array(signatureBuffer).filter(code => code !== 0));
31. const base64Helper = new util.Base64Helper();
32. const signatureData = base64Helper.decodeSync(signatureString);
```

### 安全地理位置数据格式

安全地理位置数据的结构请参考[TrustedAppService（可信应用服务）](../harmonyos-references/devicesecurity-taas-api.md)。

对安全地理位置数据验签时，需要将返回的结构体中的数据拼接成字符串形式，格式要求如下：

1. 数据排列顺序为：纬度、经度、高度、精确度、时间戳和用户数据。
2. 纬度、经度和高度类型为浮点型，精度为小数点后保留15位；精确度为浮点型，精度为小数点后保留6位；时间戳类型为64位正整数；用户数据类型为字符串。
3. 数据之间的分隔符使用英文逗号。

签名数据是Base64编码后的签名结果。获取签名和签名原始数据的参考代码（不含异常处理逻辑，由开发者根据业务场景实现）如下：

```
1. import { trustedAppService } from '@kit.DeviceSecurityKit';
2. import { util } from '@kit.ArkTS';

4. // 以下均为示例值，仅用于展示如何获取原始签名数据和签名结果
5. const location: trustedAppService.Location = {
6. latitude: 40.053903635898685,
7. longitude: 116.17356591910897,
8. altitude: 0,
9. accuracy: 11.160304069519043,
10. timestamp: 1722151680187
11. };
12. const userData = "trusted_app_service_userdata";
13. const secureLocation: trustedAppService.SecureLocation = {
14. originalLocation: location,
15. userData: userData,
16. signature: "MEQCIEAcJHgaU8aAoMqD1wgoxiXR5I4jmwVG6ncgSKkW4uBHAiBnfv96T+gt1ef83kNZ+U0gBLsq9byuBLP1RBx30hByuQ=="
17. };
18. // 获取原始数据
19. const originString = secureLocation.originalLocation.latitude.toFixed(15) + ',' +
20. secureLocation.originalLocation.longitude.toFixed(15) + ',' +
21. secureLocation.originalLocation.altitude.toFixed(15) + ',' +
22. secureLocation.originalLocation.accuracy.toFixed(6) + ',' +
23. secureLocation.originalLocation.timestamp + ',' + secureLocation.userData.toString();
24. const textEncoder = new util.TextEncoder();
25. const originData = textEncoder.encodeInto(originString);
26. // 获取签名结果
27. const base64Helper = new util.Base64Helper();
28. const signatureData = base64Helper.decodeSync(secureLocation.signature.toString());
```

## 验证签名

在安全摄像头场景和安全地理位置场景中，由于使用的是相同的证明密钥，因此签名验证的流程是一致的。结合“[安全摄像头场景](devicesecurity-taas-securecamera.md)”和“[安全地理位置场景](devicesecurity-taas-securelocation.md)”中获取到的原始数据和签名结果，验证签名的参考代码（不含异常处理逻辑，由开发者根据业务场景实现）如下：

1. 从匿名证书链中获取公钥。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   3. import { util } from '@kit.ArkTS';
   4. import { trustedAppService } from '@kit.DeviceSecurityKit';

   6. // 以安全摄像头场景为例，忽略异常情况处理
   7. const userData = "trusted_app_service_demo";
   8. const deviceId = 7483679320805398131;
   9. const initProperties: Array<trustedAppService.AttestParam> = [
   10. {
   11. tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_TYPE,
   12. value: trustedAppService.AttestType.ATTEST_TYPE_CAMERA
   13. },
   14. {
   15. tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_ID,
   16. value: BigInt(deviceId)
   17. }
   18. ];
   19. const initOptions: trustedAppService.AttestOptions = {
   20. properties: initProperties
   21. };
   22. const returnResult = await trustedAppService.initializeAttestContext(userData, initOptions);
   23. // 解析匿名证书链数据，获取三级证书
   24. const certChain = returnResult.certChains;
   25. const certList = certChain[0].split('-----BEGIN CERTIFICATE-----');
   26. const thirdCert = '-----BEGIN CERTIFICATE-----' + certList[1];
   27. // 获取公钥
   28. const textEncoder = new util.TextEncoder();
   29. const encodingBlob: cert.EncodingBlob = {
   30. data: textEncoder.encodeInto(thirdCert),
   31. encodingFormat: cert.EncodingFormat.FORMAT_PEM
   32. };
   33. const x509Cert = await cert.createX509Cert(encodingBlob);
   34. const asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
   35. const keyPair = asyKeyGenerator.convertKeySync(x509Cert.getPublicKey().getEncoded(), null);
   36. const pubKey = keyPair.pubKey; // 证书中的公钥需要转换成cryptoFramework能够接收的格式
   ```
2. 创建非对称密钥类型为ECC256、摘要算法为SHA256的verify实例，并使用步骤1中获取到的公钥进行初始化。

   ```
   1. const verifier = cryptoFramework.createVerify('ECC256|SHA256');
   2. verifier.initSync(pubKey);
   ```
3. 使用原始数据和签名结果进行验证签名。

   ```
   1. const originData = ...; // 请使用获取到的安全图像原始数据
   2. const signatureData = ...; // 请使用获取到的签名结果
   3. const inputData: cryptoFramework.DataBlob = {
   4. data: new Uint8Array(originData)
   5. };
   6. const signature: cryptoFramework.DataBlob = {
   7. data: new Uint8Array(signatureData)
   8. };
   9. // 验证签名结果
   10. const result = verifier.verifySync(inputData, signature);
   ```
