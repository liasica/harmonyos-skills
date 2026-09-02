---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-6
title: NDK工程使用AES加密算法对任意长度明文加密失败
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > NDK工程使用AES加密算法对任意长度明文加密失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:499c3424a22878b0c600b8eea4feff2d378ce26f0dcb809a78ef422838bdc923
---

## 问题现象

使用密钥管理服务开发，参考[加解密(C/C++)](../harmonyos-guides/huks-encryption-decryption-ndk.md)中的样例，发现如下情况加密会失败：

```cpp
// 待加密内容，如下，能够加密成功
char tmpInData[] = "AES_ECB_INDATA_1";

// 修改为其他值，比如下面，加密就会失败
char tmpInData[] = "Hello World!";
char tmpInData[] = "abc";
```

加密成功日志如下：

```shell
04-18 16:06:52.181   55304-55304   A03200/com.exa...cation/MY_TAG  com.examp...lication  I     Success,  ohResult.errorCode=0, tmpInData=AES_ECB_INDATA_1.
```

加密失败日志如下：

```shell
04-18 16:04:11.635   54249-54249   C02F06/com.exa...lication/HUKS  com.examp...lication  I      HksReadRequestReply[84]: reply get errMsgLen = 145
04-18 16:04:11.635   54249-54249   C02F06/com.exa...lication/HUKS  com.examp...lication  E     [HksLog]: g_errMsg [ TeecRequestCmdInner[315]: invoke km command failed, cmd = 5, ret = 0xfffffffd, retOrigin = 4 <HksServiceFinish[2008] <HksIpcServiceUpdOrFin[830]]
04-18 16:04:11.635   54249-54249   C02F06/com.exa...lication/HUKS  com.examp...lication  E      HksClientFinish[789]: HksParamSet send fail, ret = -3
04-18 16:04:11.635   54249-54249   A03200/com.exa...cation/MY_TAG  com.examp...lication  I     Failed,  ohResult.errorCode=401, tmpInData=Hello World!.
```

## 背景知识

* [AES（Advanced Encryption Standard）](../harmonyos-guides/crypto-sym-key-generation-conversion-spec.md#aes)是最常见的对称加密算法。AES是一种分组加密算法，其加密/解密的基本单位是一个固定大小16字节（128位）的数据块，如果明文长度不是块大小的整数倍，通常需要填充补齐，否则加密无法进行。
* 在AES算法中，IV（Initialization Vector，初始化向量）是一个关键的安全参数，主要用于CBC(Cipher Block Chaining)、CTR(Counter)等分组加密模式中，确保即使相同的明文多次加密，也会生成不同的密文，从而增强安全性。算法中常见设置IV\_SIZE=16也是因为AES的块大小是16字节，IV数组必须和块大小一致。
* AES支持三种长度的密钥128位，192位，256位，通常说的AES128，AES192，AES256，实际上就是指的AES算法对不同长度密钥的使用。密钥长度决定加密强度，但不会影响块大小。
* 常见的填充方式：
  + NoPadding：不做任何填充，分组加密时要求明文必须是数据块大小的整数倍；
  + PKCS5Padding：块大小固定8字节（仅适用于64位块，如DES），如果明文块小于块大小，在明文块末尾补足相应数量的字符，且每个字节的值等于缺少的字符数。主要用于DES/3DES（64位块）。
  + PKCS7Padding：是PKCS5Padding的扩展，明确支持任意块大小（如AES的16字节），因此更推荐使用。
* 在使用通用密钥库完成应用开发前，可以简单了解[通用密钥库基础概念](../harmonyos-guides/huks-concepts.md)。
* C/C++场景下的加解密操作可以参考[加解密(C/C++)](../harmonyos-guides/huks-encryption-decryption-ndk.md)。

## 问题定位

加密失败错误码401为参数错误：

```txt
OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401
```

针对问题现象进行分析：

1. 字符串本身没有区别，唯一不同的是长度的差异；
2. 尝试修改字符串的长度，长度等于16字节，长度大于16字节，长度小于16字节；
3. 发现字符串长度等于16字节时可以正常加密，长度大于16字节，长度小于16字节均会加密失败。

   因此怀疑是跟明文长度和补位有关系。

## 分析结论

查看用例中：

```cpp
static const uint32_t IV_SIZE = 16;
static uint8_t IV[IV_SIZE] = { 0 };

static struct OH_Huks_Param g_genEncDecParams[] = {
  // ...
  {
        .tag = OH_HUKS_TAG_PADDING,
        .uint32Param = OH_HUKS_PADDING_NONE
  }
}
```

OH\_HUKS\_TAG\_PADDING补位标签设置的参数为OH\_HUKS\_PADDING\_NONE，表明不会进行补位，因此字符串长度必须是块大小（16字节）的整数倍，否则加密会失败。

## 修改建议

查看[HuksTypeApi](../harmonyos-references/capi-hukstypeapi.md)中，填充算法类型枚举值：OH\_HUKS\_PADDING\_NONE表示不使用填充算法，OH\_HUKS\_PADDING\_PKCS7表示使用PKCS7填充算法。

将uint32Param = OH\_HUKS\_PADDING\_NONE修改为OH\_HUKS\_PADDING\_PKCS7后加密成功，修改如下。完整示例代码见[加解密(C/C++)](../harmonyos-guides/huks-encryption-decryption-ndk.md)中的样例。

```cpp
static const uint32_t IV_SIZE = 16;
static uint8_t IV[IV_SIZE] = {0}; // this is a test value, for real use the iv should be different every time.
static struct OH_Huks_Param g_genEncDecParams[] = {
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT | OH_HUKS_KEY_PURPOSE_DECRYPT},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PKCS7},
    {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_CBC}};
static struct OH_Huks_Param g_encryptParams[] = {
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PKCS7},
    {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_CBC},
    {.tag = OH_HUKS_TAG_IV,
     .blob = {
         .size = IV_SIZE,
         .data = (uint8_t *)IV // this is a test value, for real use the iv should be different every time.
     }}};
static struct OH_Huks_Param g_decryptParams[] = {
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DECRYPT},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PKCS7},
    {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_CBC},
    {.tag = OH_HUKS_TAG_IV,
     .blob = {
         .size = IV_SIZE,
         .data = (uint8_t *)IV // this is a test value, for real use the iv should be different every time.
     }}};
```
