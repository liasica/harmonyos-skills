---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-11
title: 如何对大文件进行SM4加密
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何对大文件进行SM4加密
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:57+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:96746e0450bf9ad7dc88097c1a27e722a9407eb236e8022983282560eb3e4142
---

使用分段加解密时，对于ECB和CBC模式，不论update传入的数据是否为分组长度的整数倍，都会以分组为单位进行加/解密，并输出本次update产生的新分组结果。当update积累的数据达到分组长度时产生输出，否则返回null。未加/解密的数据将保留，等待下一次update/doFinal时拼接继续处理。最后，doFinal会将剩余未加/解密的数据，根据创建cipher时设置的padding模式进行填充，补齐到分组的整数倍长度，再输出剩余加解密结果。

参考代码如下：

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

3. function genIvParamsSpec() {
4. let arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
5. let dataIv = new Uint8Array(arr);
6. // The production environment should use randomly generated IVs. All zeros here are only for display purposes.
7. let ivBlob: cryptoFramework.DataBlob = { data: dataIv };
8. let ivParamsSpec: cryptoFramework.IvParamsSpec = {
9. algName: 'IvParamsSpec',
10. iv: ivBlob
11. };
12. return ivParamsSpec;
13. }

15. function stringToUint8Array(str: string): Uint8Array {
16. let arr: Array<number> = [];
17. for (let i = 0, j = str.length; i < j; i++) {
18. arr.push(str.charCodeAt(i));
19. }
20. return new Uint8Array(arr);
21. }

23. async function testAesMultiUpdate(plainText: string) {
24. let symAlgName = 'SM4_128';
25. let length = 1024;
26. let symKeyGenerator = cryptoFramework.createSymKeyGenerator(symAlgName);
27. let cipherAlgName = 'SM4_128|CBC|PKCS7';
28. let globalCipher = cryptoFramework.createCipher(cipherAlgName);
29. let result = new Uint8Array();
30. let data: cryptoFramework.DataBlob;
31. let startEncrypt = 0;
32. let endEncrypt = 0;
33. let promiseSymKey = await symKeyGenerator.generateSymKey();
34. await globalCipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, promiseSymKey, genIvParamsSpec());
35. let updateOutput: cryptoFramework.DataBlob;
36. while (plainText.length > 0) {
37. const contentCurr = plainText.substring(0, length);
38. plainText = plainText.substring(length, plainText.length);
39. let messageBlob: cryptoFramework.DataBlob = { data: stringToUint8Array(contentCurr) };
40. updateOutput = await globalCipher.update(messageBlob);
41. if (updateOutput !== null) {
42. let mergeText = new Uint8Array(result.length + updateOutput.data.length);
43. mergeText.set(result);
44. mergeText.set(updateOutput.data, result.length);
45. result = mergeText;
46. }
47. }
48. startEncrypt = new Date().getTime();
49. data = await globalCipher.doFinal(null);
50. endEncrypt = new Date().getTime();
51. console.info('TEST加密' + (endEncrypt - startEncrypt));
52. let mergeText = new Uint8Array(result.length + data.data.length);
53. mergeText.set(result);
54. mergeText.set(data.data, result.length);
55. result = mergeText;
56. let contentTemp = result;
57. console.info('TEST加密成功', contentTemp);
58. await globalCipher.init(cryptoFramework.CryptoMode.DECRYPT_MODE, promiseSymKey, genIvParamsSpec());
59. console.info('TEST == 长度' + contentTemp.length);
60. }

62. @Entry
63. @Component
64. struct SM4Encryption {
65. @State message: string = 'Hello World';

67. aboutToAppear(): void {
68. testAesMultiUpdate('123456789102345566478416518498454151689546549849');
69. }

71. build() {
72. RelativeContainer() {
73. Text(this.message)
74. .id('SM4EncryptionHelloWorld')
75. .fontSize(50)
76. .fontWeight(FontWeight.Bold)
77. .alignRules({
78. center: { anchor: '__container__', align: VerticalAlign.Center },
79. middle: { anchor: '__container__', align: HorizontalAlign.Center }
80. })
81. }
82. .height('100%')
83. .width('100%')
84. }
85. }
```

[TestAesMultiUpdate.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CryptoArchitectureKit/entry/src/main/ets/pages/TestAesMultiUpdate.ets#L21-L105)

**参考链接**

[@ohos.security.cryptoFramework (加解密算法库框架)](../harmonyos-references/js-apis-cryptoframework.md)
