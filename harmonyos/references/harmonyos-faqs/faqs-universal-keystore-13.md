---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-universal-keystore-13
title: 如何解决DH公钥在服务端协商报参数不兼容的问题
breadcrumb: FAQ > 系统开发 > 安全 > 密钥管理（Universal Keystore） > 如何解决DH公钥在服务端协商报参数不兼容的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f60682f11c1ad23cd7fd0a27b714c02fa760646588c08811a3854a5c3f94b7d4
---

## 问题现象

HarmonyOS使用ArkTS生成的DH公钥，在服务端协商失败，报错Incompatible parameters。

```java
class TestDh {
    public static void main(String[] args) throws Exception {
        // 生成并初始化DH密钥
        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("DH");
        keyPairGenerator.initialize(512);
        /* 服务端公私钥 */
        KeyPair keyPair= keyPairGenerator.generateKeyPair();
        DHPublicKey publicKey = (DHPublicKey) keyPair.getPublic();
        String serverPuk = Base64.getEncoder().encodeToString(publicKey.getEncoded());
        // HarmonyOS公钥
        String pukClient = "替换为HarmonyOS的公钥";
        X509EncodedKeySpec keySpec = new X509EncodedKeySpec(Base64.getDecoder().decode(pukClient));
        // 根据DH算法获取KeyFactory
        KeyFactory kf = KeyFactory.getInstance("DH");
        // 通过KeyFactory创建公钥
        PublicKey receivedPublicKey = kf.generatePublic(keySpec);
        // 创建KeyAgreement对象
        KeyAgreement keyAgreement = KeyAgreement.getInstance("DH");
        // 初始化协议，设置我方密钥
        DHPrivateKey privateKey = (DHPrivateKey) keyPair.getPrivate();
        keyAgreement.init(privateKey);
        // 添加对方的公钥
        keyAgreement.doPhase((DHPublicKey)receivedPublicKey, true);
        // 生成协商密钥
        byte[] sharedSecret = keyAgreement.generateSecret();
        // 输出协商的密钥
    }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/VS0x-vEJTv6KCORPLMynUg/zh-cn_image_0000002658849153.png "点击放大")

## 背景知识

[DH密钥协商算法](../harmonyos-guides/crypto-key-agreement-overview.md#dh)流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/0jsdf1ErT4KsXEZdG_BQ_Q/zh-cn_image_0000002628769786.png "点击放大")

## 定位思路

1. **检查公钥：**

   从DH算法的生成流程看，最关键的核心是密钥对的生成和交换，首先检查公钥的解析是否正确，核心代码：

   ```ts
   // 来自服务端的公钥serverPubString
   let serverPubString ='替换下xxx';
   const serverPubArray: Uint8Array = new util.Base64Helper().decodeSync(serverPubString);
   ```

   检查方法：查看serverPubArray的值是否成功生成。
2. **检查密钥：**

   检查密钥生成器的配置参数是否正确，即参数要写成“DH\_modp1536”。

   ```ts
   let keyGen = cryptoFramework.createAsyKeyGenerator('DH_modp1536');
   ```
3. **检查密钥协商传参是否传错：**

   公钥和私钥的前后顺序不能错。

   ```ts
   keyAgreement.generateSecret(clientPair.priKey, serverPubKey.pubKey)
   ```

   通过以上步骤分析，发现服务端代码，密钥位数为512，而HarmonyOS侧提高了安全性，要求最低密钥长度为1536，导致协商失败。

## 分析结论

DH密钥交换算法，务必按照定位思路中的三个步骤，逐个检查是否合法，如果参数不合法，将出现协商失败的情况。

## 修改建议

将服务端代码密钥长度设置为1536后重新协商，即keyPairGenerator的initialize参数为initialize(1536)。

协商成功的截图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/KL14H8AGSZ67DuZj30BFxg/zh-cn_image_0000002628609890.png)

这里提供HarmonyOS密钥协商的正确代码实现：

```ts
import { util } from '@kit.ArkTS';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State res: string = 'init value';

  build() {
    Column() {
      Button('启动测试')
        .onClick(() => {
          dhCreate().then((result: string) => {
            this.res = result;
          });
        })
      Text('Result:\n' + this.res)
    }
    .height('100%')
    .width('100%')
  }
}

async function dhCreate(): Promise<string> {
  // 生成客户端公私钥对
  let keyGen = cryptoFramework.createAsyKeyGenerator('DH_modp1536');
  let clientPair = await keyGen.generateKeyPair();
  let clientPub = clientPair.pubKey.getEncoded();
  let base64Helper = new util.Base64Helper();
  // 传给服务端的公钥:toServerPuk
  let toServerPuk = base64Helper.encodeToStringSync(clientPub.data);
  hilog.debug(1, 'Index', `createKeyAgreement toServerPuk ${toServerPuk}`);
  // 来自服务端的公钥serverPubString，以下为模拟key，非真实值！！！
  let serverPubString =
    'MIIBoDCB1QYJKoZIhvcNAQMBMIHHAoHBAP//////////yQ/aoiFowjTExmKLgNwc0SkCTgiKZ8x0Agu+pjsTmyJRSgh5jjQE3e+VGbPNOkMbMCsKbfJfFDdP4TVtbVHCReSFtXZiXn7G9ExC6aY37WsL/1y29Aa37e44a/taiZ+lrp8kEXxLH+ZJKGZR7ORbPcIAfLihY78FmNpINhxV05ppFj+o/STPX4NlXSPco62WHGLzViCFUrue1SkHcJaWbWcMNU5KvJgE8XRsCMojcyf//////////wIBAgOBxQACgcEAnwrTwUX2xwrz0RYuYe2feqrD5wgJWDDeZSu0AnpIHFGZER1eYUJ1TTEZjE1gtBQAMbcVngSekfqFn5mHjDSA3JCLa7E2GK0GvhETtKv0m3BD/aR7bNpwwEqb0865ybD+y75P2ehYlre9XOiWcdMSs7Vc04ac0Ru1h/vyuN7ljtciJeSg8kvLJjEQSNF0QdZ5vMpOVRDLWpB0/fVRlfVdvUs2F2V95cPTK0SIXrmS9xN6quV5nDYwj+3+4rm0+VDs';
  const serverPubArray: Uint8Array = new util.Base64Helper().decodeSync(serverPubString);
  try {
    let serverPubKey = keyGen.convertKeySync({ data: serverPubArray }, null);
    let keyAgreement = cryptoFramework.createKeyAgreement('DH_modp1536');
    // 使用服务端的公钥和客户端的私钥进行密钥协商
    return keyAgreement.generateSecret(clientPair.priKey, serverPubKey.pubKey).then((reslove) => {
      let strBase = new util.Base64Helper().encodeToStringSync(reslove.data);
      hilog.debug(1, 'Index', 'result is:' + strBase);
      return strBase;
    }).catch((err: BusinessError) => {
      hilog.error(1, 'Index', 'createKeyAgreement error', err);
      return 'createKeyAgreement error';
    });
  } catch (err) {
    hilog.error(1, 'Index', 'dhCreate error', err);
    return 'dhCreate error';
  }
}
```
