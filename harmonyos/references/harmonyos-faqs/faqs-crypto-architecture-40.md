---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-40
title: "如何解决DES密钥生成报错Invalid param: input key length is invalid"
breadcrumb: "FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何解决DES密钥生成报错Invalid param: input key length is invalid"
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:668bbe6b2dc0a2524e8679c52dbf603b40f23072dc5e069ea6ac3715507a5fea
---

## 问题现象

使用密钥材料“TESTXXXX”进行DES加密，调用[SymKeyGenerator.convertKeySync](../harmonyos-references/js-apis-cryptoframework.md#convertkeysync12)生成密钥时报错：

```screen
ConvertSymmKey[316]: Invalid param: input key length is invalid!
```

## 背景知识

对称加密算法密钥长度必须按[对称密钥生成和转换规格](../harmonyos-guides/crypto-sym-key-generation-conversion-spec.md)中密钥长度提供，如果密钥长度不足，需要在末尾补'\0'填充长度。

## 问题定位

运行以下代码，使用密钥进行DES加密时报错如下图所示，根据报错信息可以判断是Key长度问题引起。

```screen
const keyData = new util.TextEncoder().encodeInto('TESTXXXX');
let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
const symKey = symKeyGenerator.convertKeySync({
  data: keyData
});
```

报错如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/Yz17j9cnQ7eRY7L0RfF9lA/zh-cn_image_0000002628768360.png "点击放大")

## 分析结论

参考背景知识中3DES算法规格的介绍，要求密钥长度必须为192位，即24个字节。而问题代码中的密钥材料“TESTXXXX”只有8个字节，因此需要用'\0'补充剩余长度。

| 对称密钥算法 | 密钥长度（bit） | 字符串参数 |
| --- | --- | --- |
| 3DES | 192 | 3DES192 |

## 修改建议

通过padEnd()补齐密钥长度，该方法会将当前字符串从末尾开始填充给定的字符串（如果需要会重复填充），直到达到给定的长度。

```screen
import { util } from '@kit.ArkTS';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct SolutionOfDESKeyGenerationFailed {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
          const keyData = new util.TextEncoder().encodeInto('TESTXXXX'.padEnd(24, '0'));
          let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
          const symKey = symKeyGenerator.convertKeySync({
            data: keyData
          });
          hilog.info(0x0000, 'TAG', `symKey: ${symKey}`);
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
