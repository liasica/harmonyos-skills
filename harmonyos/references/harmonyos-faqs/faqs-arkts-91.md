---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-91
title: Uint8Array类型和String以及hex如何互相转换
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > Uint8Array类型和String以及hex如何互相转换
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0ecfb836def87175ae99f580f65b0dd49467064a8925cba913d78f4ead1944fb
---

Uint8Array类型和String以及hex实现互相转换，可参考如下代码：

```
1. import { buffer, util } from '@kit.ArkTS';

4. // Convert string to byte stream
5. function stringToUint8Array(str: string) {
6. console.info('Convert string to byte stream:' + new Uint8Array(buffer.from(str, 'utf-8').buffer));
7. return new Uint8Array(buffer.from(str, 'utf-8').buffer);
8. }

11. // Byte flow into understandable strings
12. function uint8ArrayToString(array: Uint8Array) {
13. let textDecoderOptions: util.TextDecoderOptions = {
14. fatal: false,
15. ignoreBOM: true
16. }
17. let decodeToStringOptions: util.DecodeToStringOptions = {
18. stream: false
19. }
20. let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
21. let retStr = textDecoder.decodeToString(array, decodeToStringOptions);
22. console.info('Byte flow into understandable strings：' + retStr);
23. return retStr;
24. }

27. //Hexadecimal to Uint8Array
28. function HexStrTouint8Array(data: string): Uint8Array {
29. console.info('Hexadecimal to Uint8Array:' + new Uint8Array(buffer.from(data, 'hex').buffer));
30. return new Uint8Array(buffer.from(data, 'hex').buffer);
31. }

34. // Uint8Array to hexadecimal
35. function uint8ArrayToHexStr(data: Uint8Array): string {
36. let hexString = '';
37. let i: number;
38. for (i = 0; i < data.length; i++) {
39. let char = ('00' + data[i].toString(16)).slice(-2);
40. hexString += char;
41. }
42. console.info('Uint8Array to hexadecimal:' + hexString);
43. return hexString;
44. }

47. let uint8Array: Uint8Array;

50. @Entry
51. @Component
52. struct TypeConversion {
53. build() {
54. Column({ space: 12 }) {
55. Button('Convert string to byte stream')
56. .onClick(() => {
57. let str = 'hello';
58. uint8Array = stringToUint8Array(str);
59. })
60. Button('Byte flow string')
61. .onClick(() => {
62. if (uint8Array) {
63. uint8ArrayToString(uint8Array);
64. }
65. })
66. Button('Hexadecimal to Uint8Array')
67. .onClick(() => {
68. let data = '05160b22';
69. HexStrTouint8Array(data);
70. })
71. Button('Uint8Array to hexadecimal')
72. .onClick(() => {
73. let uint8Array = new Uint8Array([5, 22, 11, 34]);
74. uint8ArrayToHexStr(uint8Array);
75. })
76. }
77. .width('100%')
78. .justifyContent(FlexAlign.Center)
79. }
80. }
```

[UintArray.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/UintArray.ets#L21-L100)
