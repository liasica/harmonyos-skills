---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device-certificate-glossary
title: Device Certificate Kit术语
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > Device Certificate Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:29+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:a2693d0a7d3533860b8137b591b2fbf385df87a06017b844a26d9d60cffd7cba
---

## C

### CA Certificate；CA证书

可以颁发下级CA证书或实体证书的数字证书，CA证书由CA机构进行管理和运营。

### Certificate Chain；证书链

也称Certificate Path，由根CA证书（无上级CA证书、自签发的证书）、多级中间CA证书、实体证书依次序组成的证书列表。

### Certificate Credential；证书凭据

包含证书链和实体证书对应的私钥信息。

### Certificate File；证书文件

用于存储数字证书、证书链的文件，常见的证书文件格式为der、pem、crt、p7b。

### CertUri；CA证书标识

用于在证书管理服务中唯一标识已安装的CA证书。

## D

### Digital Certificate；数字证书

简称Certificate（证书）。经数字证书认证机构（Certificate Authority，CA）进行数字签名的、包含公钥拥有者信息以及公钥信息。当前Device Certificate Kit只支持X.509规范的数字证书。

## E

### Entity Certificate；实体证书

也称终端证书或叶子证书，是给业务实体（网站、服务器、设备、个人）使用的数字证书，实体证书不能签发下级证书，主要用于实际业务的身份认证与加密通信。

## K

### KeyStore；密钥库

用于存储证书凭据的容器，可以包含证书链、私钥、CA证书等，常见的密钥库文件格式为P12文件（PKCS #12），可以使用密码对密钥库文件进行加密保护。

### KeyUri；证书凭据标识

用于在证书管理服务中唯一标识已安装的证书凭据。

## S

### Signature；签名

使用私钥对需要传输的数据计算摘要并加密得到的密文。

### Signature Verification；验签

用公钥对签名密文进行解密，得到文本的摘要，然后使用与发送方同样的方法对文本计算摘要值，再与解密得到的摘要做对比，二者一致则说明文本没有被篡改过。
