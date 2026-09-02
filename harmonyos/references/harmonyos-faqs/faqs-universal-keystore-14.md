---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-universal-keystore-14
title: 关于huks.exportKeyItem函数401报错的原因
breadcrumb: FAQ > 系统开发 > 安全 > 密钥管理（Universal Keystore） > 关于huks.exportKeyItem函数401报错的原因
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4aca72b5dfed63ff6a9cc5f23551bfab64e8c9f03a2fb41bac57a96d8b920f33
---

## 问题现象

huks.exportKeyItem导出密钥时，总是报401，Invalid parameters.部分代码如下。加密算法使用的为AES，RSA和SM4算法。

* 方法generateKey。

  ```screen
  export async function generateKey(mode: number) {
    let properties: Array<huks.HuksParam> = getGenerateProperties(mode); // 根据所选模式进行切换算法
    let options: huks.HuksOptions = {
      properties: properties
    };
    const exportOptions: huks.HuksOptions = {
      properties: properties,
      inData: new Uint8Array([])
    }
    // 确认Key是否存在
    huks.isKeyItemExist(keyAlias, options, async (error, data) => {
      if (data) {
        try {
          // 导出密钥
          huks.exportKeyItem(keyAlias, HuksPropertiesConstants.EMPTY_OPTION, (error, data) => {
            if (error) {
              isInit = false
            } else {
              isInit = true
            }
          });
        } catch (error) {
          isInit = false
        }
      } else {
        await huks.generateKeyItem(keyAlias, options)
        await huks.importKeyItem(keyAlias, options);
      }
    });
  }
  ```

* 方法encryptData。

  ```screen
  export async function encryptData(plainText: string, mode: number): Promise<string> {
    if (!isInit) {
      generateKey(mode)
    }
    // ...
    await huks.initSession(keyAlias, options).then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
    });

    await huks.finishSession(handle, options).then((data) => {
      showToast({
        message: $r('app.string.encrypt_success'),
        duration: CommonConstants.TOAST_DURATION
      });
      encryptResult = new util.Base64Helper().encodeToStringSync(data.outData);
    })
    return encryptResult;
  }
  ```
* 方法getGenerateProperties。

  ```screen
  export function getGenerateProperties(mode: number) { // 根据模式不同选择相应的算法参数：AES，RSA，SM4
    let properties: Array<huks.HuksParam> = new Array();
    let index: number = 0;
    switch (mode) {
      case 0:
        properties[index++] = {
          tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
          value: huks.HuksKeyAlg.HUKS_ALG_AES
        };
        properties[index++] = {
          tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
          value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
        };
        properties[index++] = {
          tag: huks.HuksTag.HUKS_TAG_PURPOSE,
          value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
          huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
        };
        break;
      case 1:
        properties[index++] = {
          tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
          value: huks.HuksKeyAlg.HUKS_ALG_RSA
        };
        properties[index++] = {
          tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
          value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
        };
        properties[index++] = {
          tag: huks.HuksTag.HUKS_TAG_PURPOSE,
          value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
          huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
        };
        break;
      case 2:
        properties[index++] = {
          tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
          value: huks.HuksKeyAlg.HUKS_ALG_SM4
        };
        properties[index++] = {
          tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
          value: huks.HuksKeySize.HUKS_SM4_KEY_SIZE_128
        };
        properties[index++] = {
          tag: huks.HuksTag.HUKS_TAG_PURPOSE,
          value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
          huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
        };
        break;
      default:
        break;
    }
    return properties;
  }
  ```

  使用SM4和AES的报错截图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/xpaxH7_STx6PXZMsutnpuQ/zh-cn_image_0000002658969105.png "点击放大")

  使用RSA算法输出正常：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/0wJ5SwOOS9-56m0iSGYwRA/zh-cn_image_0000002658849155.png "点击放大")

## 解决方案

加解密的核心代码都是一致的，但是RSA整个过程正常，SM4和AES却报错401。

业务需要获取持久化存储的非对称密钥的公钥时可以使用[huks.exportKeyItem](../harmonyos-references/js-apis-huks.md#huksexportkeyitem9)进行公钥导出，但是当前支持ECC/RSA/ED25519/X25519/SM2的[公钥导出](../harmonyos-guides/huks-export-key-arkts.md)。代码入参均无问题，其中AES和SM4不在huks.exportKeyItem的支持范围内，而支持的RSA算法无问题，因此导致报错的原因应为使用了不正确的加密算法。变更为支持的加解密算法即可解决报错问题。
