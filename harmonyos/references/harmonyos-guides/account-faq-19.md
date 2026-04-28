---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-19
title: 不同开发者的应用之间如何实现用户数据互通
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 不同开发者的应用之间如何实现用户数据互通
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:861f49f1acd2407de3cc67360a3c7b6e397ac51c73ad3d944492be2546cab10d
---

不同开发者的应用，可以使用GroupUnionID关联用户数据来实现数据互通。GroupUnionID是华为账号用户在关联主体账号组内的唯一标识。不同开发者账号加入同一关联主体账号组后，其组内所有开发者的应用获取到用户的GroupUnionID相同。应用获取GroupUnionID流程如下：

1. 开发者账号加入同一关联主体账号组。

   通过[创建账号组](../start/cag-0000001265390541.md)创建关联主体账号组，在关联主体账号组中[添加账号组成员](../start/aai-0000001265430513.md)。
2. 获取GroupUnionID。

   * 针对新用户，在登录时可以直接获取GroupUnionID，具体指导请参考：[通过Authorization Code获取GroupUnionID](../harmonyos-references/account-api-get-groupunionid-code.md)。
   * 针对已获取OpenID或UnionID的用户，可以批量获取GroupUnionID，具体指导请参考：[通过OpenID或UnionID获取GroupUnionID](../harmonyos-references/account-api-get-groupunionid.md)。

注意

GroupUnionID是一个大小写敏感的字符串，最大长度为64字符，在存储、查询、比较GroupUnionID时，请务必保留其原始大小写。
