---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-55
title: 实现传入密码哈希值与目标密码哈希值的一致性比较函数
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 实现传入密码哈希值与目标密码哈希值的一致性比较函数
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:08d41ced03ba6faba64eb28f3beddf568f48f30463ab722553bbc35ec49e0b5a
---

## 问题现象

在项目开发过程中，需自主实现与bcrypt算法中compare功能等效的逻辑，而非直接调用现有API完成相关校验需求。

## 背景知识

为了密码安全，通常密码不会被明文存储在数据库中，密码会被进行加密或哈希存储。

* 加密是一个可逆的过程，通过特定的算法将明文转换为密文，并且在拥有正确密钥的前提下，密文可以被还原为明文。加密算法在数据传输和敏感数据保护中发挥着不可替代的作用。但与一般的认知可能恰恰相反，加密技术并不适合用于密码存储。原因在于，一旦存储密文的密钥遭到泄露，攻击者便可以通过解密操作直接恢复用户密码。鉴于此，加密在密码存储领域的应用相对有限。
* 哈希则是不可逆的。这意味着一旦数据经过哈希处理，理论上无法通过哈希值逆推出原始数据。哈希算法通过固定的规则对输入进行处理，并输出一个固定长度的哈希值。同样的输入必然会生成相同的输出，这使得哈希算法在验证数据一致性方面具有独特的优势。对于密码存储来说，哈希算法的不可逆性使得攻击者即便获取了哈希值，他们也无法轻易还原出原始密码。

## 解决方案

构建一个函数方法，传入密码值及密码哈希值两个参数，对密码值进行MD5摘要计算后与传入的密码哈希值进行比较，返回比较结果。

```ts
async function compareKey(password : string, hashed : string) : Promise<boolean> {
  let mdAlgName = 'MD5'; // 摘要算法名
  let message = password; // 待摘要的数据
  let md = cryptoFramework.createMd(mdAlgName);
  // 数据量较少时，可以只做一次update，将数据全部传入，接口未对入参长度做限制
  try {
    await md.update({ data: new Uint8Array(buffer.from(message, 'utf-8').buffer) });
    // 字符格式不局限于utf-8,很多密码为hex或base64格式
  } catch (error) {
    console.error(`error: ${error}`);
  }
  let mdResult = await md.digest();
  console.info(`Md result: ${mdResult.data}`);
  let mdLen = md.getMdLength();
  console.info(`md len: ${mdLen}`);
  let res = Array.from(mdResult.data).map(byte => byte.toString(16)).join('');
  console.info(`res: ${res}`);
  if (res === hashed) {
    return true;
  } else {
    return false;
  }
}
```

```ts
@Entry
@Component
struct Index {
  build(){
    Button('比较hello密码哈希值')
      .onClick(async () => {
        let res = await compareKey('hello','5d41402abc4b2a76b9719d911017c592');
        console.info(`result: ${res}`);
      })
  }
}
```

## 常见FAQ

Q：空字符串进行MD5摘要计算报错。

A：MD5摘要计算update方法进行了非空判断，传入空值会报错。对于空值进行摘要计算直接执行digest方法或对update方法进行异常捕获即可，空字符串MD5摘要计算结果为d41d8cd98f0b24e980998ecf8427e。
