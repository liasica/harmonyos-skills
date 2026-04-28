---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-24
title: 如何使用SM3算法进行消息鉴别码计算
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何使用SM3算法进行消息鉴别码计算
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6acb99baf9354e6cfe0ca294e71f1031b4a0e51fc840dee2f0e7206f8371cea2
---

1. 设置算法，通过createMac接口生成消息鉴别码实例。
2. 接收对称密钥，通过init接口初始化Mac。
3. 接收数据，通过update接口更新Mac。此步骤可重复。
4. 通过doFinal接口，返回MAC计算结果。
5. 将结果转换为十六进制。

核心代码如下：

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
2. import { buffer } from '@kit.ArkTS';

4. @Entry
5. @Component
6. struct Hmac {
7. @State message: string = 'Hello World';

9. build() {
10. Row() {
11. Column() {
12. Button('使用SM3算法进行消息鉴别码计算')
13. .fontSize(20)
14. .fontWeight(FontWeight.Bold)
15. .onClick(() => {
16. getHmac('密钥')
17. })
18. }
19. .width('100%')
20. }
21. .height('100%')
22. }
23. }

25. // Convert understandable strings into byte streams
26. function stringToUint8Array(str: string) {
27. let arr = new Uint8Array(str.length);
28. for (let i = 0, j = str.length; i < j; ++i) {
29. arr[i] = str.charCodeAt(i);
30. }
31. return arr;
32. }

34. async function getHmac(message:string){

36. try {
37. let macAlgName = 'SM3';
38. let mac =cryptoFramework.createMac(macAlgName)
39. let arr = stringToUint8Array('30a86dc9056c44cc05420fec269270214bbb6914954e871e83771c9810ac1db0')
40. let KeyBlob: cryptoFramework.DataBlob = {data:arr};
41. let symKeyGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
42. const  symKey=await symKeyGenerator.convertKey(KeyBlob);
43. await mac.init(symKey)
44. await mac.update({data:stringToUint8Array(message)});
45. let macOutpt= await mac.doFinal();
46. const res=buffer.from(macOutpt.data).toString('hex');
47. console.log('Hmac---:'+res);
48. }catch (err){
49. console.log('err:'+err)
50. }

52. }
```

[GetHmac.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CryptoArchitectureKit/entry/src/main/ets/pages/GetHmac.ets#L21-L72)
