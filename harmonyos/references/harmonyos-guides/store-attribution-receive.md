---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-attribution-receive
title: 归因结果回传
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用归因服务 > 归因结果回传
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4e53a3b82d7acf731dcc5b85eed4707301c500b40303e018c3b93956738985c6
---

应用归因将满足隐私要求的归因结果，回传给开发者、获胜的分发平台以及分发平台配置的归因监测平台。归因结果回传详细信息请参考[归因结果回传](../harmonyos-references/store-rest-receive.md)。分发平台/开发者/归因监测平台需按照回传接口的要求完成相应的接口实现。

说明

归因结果回传地址为注册归因角色时维护的链接地址。

为保证信息合法性，分发平台/开发者/归因监测平台需要对回传的归因结果进行验签（验签算法：SHA256withRSA/PSS）。

## 验签计算规则

1. 按照如下规则拼接待验签的字符串：

   ```
   1. ad_tech_id + '\u2063' + campaign_id + '\u2063' + source_id + '\u2063' + destination_id + '\u2063' + trigger_data + '\u2063' + nonce + '\u2063' + timestamp
   ```

   其中，非必填字段仅当满足回传条件时才携带，验签时，应根据接收到的请求中包含的字段拼接字符串进行验签，例如，回传的消息结构中，仅包含ad\_tech\_id、destination\_id，则拼接的待验签字符串为：

   ```
   1. ad_tech_id + '\u2063' + destination_id + '\u2063' + nonce + '\u2063' + timestamp
   ```
2. 使用应用归因服务提供的公钥，对步骤1拼接的字符串进行验签，验签方法可参考[回传结果验签方法](../harmonyos-references/store-rest-receive.md#回传结果验签方法)。

   应用归因服务提供的公钥：

   ```
   1. -----BEGIN PUBLIC KEY-----
   2. MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEA0IgrEtIR1kVF/ImKIo3/5AxEFZzL156jLn2CilqGQmFByiMlpa2G0dotCK1mj9bdhDJbUPd3Plx1zVX9WoW/L/mg25+ng0iPlcItqhUuTIVi+0N50BHlVKPFWG/vYxCkR1ABU44zHyg2XAmqs2L6nUA9Hjbmwn5WX9JUWFF3RF4ja6GJRDkq0HFQ6ouM8Vpm3ZnnRTCuEzOpUcG+FMYAa9M9coRMMM3w0M/IgbYL4n86tQ6ybicaeadSwJIzXExLL0bSf1tYZ7CWvdK0V2ftLWC7Wmho64/g/AjqXc5d2nq88Cn+Vm48jLW1gibI1sPLjFhcfgRg0EOHD/FeUHLxhGeLc4KZ7hrcaW+IuVaTpHxbxJ9WiIokf6blQSEyPHx4w95IdGYNe/BGFhYaf3AhCe6b62e//0JdaYPKNDUKOpTf60vAhqQeibx4iaRZh8dEAU1m9lD0aR6+0trNCzdsC0iPCRLCXcFJXN2/ZJRug39xuJoSEkCxUsJdcoYknbRxAgMBAAE=
   3. -----END PUBLIC KEY-----
   ```
