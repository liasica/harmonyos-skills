---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-22
title: 邀请测试如何创建邀请码并使用
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 邀请测试如何创建邀请码并使用
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:29+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:c5aa520bfd0401f2e02c8148540c77c4013e08b8f28144afc60ea0b6691408e1
---

## 问题现象

在使用邀请测试时，选择邀请码添加方式，如何使用邀请码？

## 背景知识

开发者在应用正式版本发布之前，需要挑选特定的用户群组来测试HarmonyOS应用/元服务。当开发者使用邀请测试并选择邀请码添加方式进行测试时需要了解相关知识。

## 解决方案

**注意** 

AppGallery邀请测试拼接邀请码是&作为连接符，AppTest邀请测试拼接邀请码是以?作为连接符。

AppTest邀请测试的邀请码链接中的是群组级邀请码，用户通过邮件收到的是个人邀请码，个人邀请码无法直接拼接分享链接使用。

**AppGallery邀请测试：**

1. 在[创建测试群组](../app/agc-help-appgallery-create-testgroup-0000002258071216.md)中添加测试用户时，选择“邀请码添加”添加。
2. 勾选邀请码有效期并填写邀请参与测试的人数上限。
3. 点击生成邀请码，邀请码生成后，会在邀请码管理页签展示邀请码信息。
4. 邀请码生成后，您需要[通过“分享链接+邀请码”邀请用户](../app/agc-help-appgallery-invite-testuser-0000002292624413.md#section8765163593316)，此方式无需提前收集用户的华为账号，使用更方便，但仅限于分享给您非常信任的、不会将邀请码链接外泄的用户群体，否则可能导致邀请范围之外的用户加入您的测试群组。即可通过分享链接的方式，邀请测试用户。
5. 拼接方式：
   * 测试版本提交审核后，[复制生成的分享链接](../app/agc-help-appgallery-invite-testuser-0000002292624413.md#li10574539121315)，如：“http://xx.xx.xx?taskId=123456”。
   * 在上述链接的末尾，拼接上“&invitationCode=邀请码”。
   * 获取拼接后的完整链接：“http://xx.xx.xx?taskId=123456&invitationCode=邀请码”。

**AppTest邀请测试：**

1. AppTest邀请测试可以[创建内部测试用户群组](../app/agc-help-apptest-create-internalgroup-0000002486254204.md)，也可以[创建外部测试用户群组](../app/agc-help-apptest-create-externalgroup-0000002486414168.md)。内部群组下不支持创建公开链接邀请测试用户，也不支持创建邀请码。
2. 在创建外部测试用户群组添加测试用户时，选择“邀请码添加”添加。
3. 勾选邀请码有效期并填写邀请参与测试的人数上限。
4. 点击生成邀请码，邀请码生成后，会在邀请码管理页签展示邀请码信息。
5. 邀请码生成后，您需要[通过“分享链接+群组邀请码”邀请用户](../app/agc-help-apptest-invite-testuser-0000002258071224.md#section11447163533618)，此方式无需提前收集用户的华为账号，但仅限于分享给您非常信任的、不会将邀请码链接外泄的用户群体，否则可能导致邀请范围之外的用户加入您的测试群组。
6. 拼接方式如下：
   * 测试版本提交审核后，复制生成的分享链接，如：“https://appgallery.huawei.com/apptest/join/123456”。
   * 在上述链接的末尾，拼接上“?invitationCode=邀请码”。
   * 获取拼接后的完整链接：“https://appgallery.huawei.com/apptest/join/123456?invitationCode=邀请码”。

## 常见FAQ

Q：AppGallery中生成的测试版本，状态为正在测试，测试阶段是邀请测试，跳转到邀请测试介绍页显示测试任务已结束。

A：该问题一般是链接输入错误，建议将链接生成二维码，扫码跳转浏览器下载。

Q：邀请测试支持同时测试的版本数有限制吗？

A：邀请测试最多允许100个版本同时在架，邀请测试和公开测试的总计版本数量不超过100个。

Q：邀请测试，测试群组中邀请码是必须在提交邀请测试版本前生成吗？

A：邀请码不需要在提交邀请测试版本前生成，邀请码可以在需要的时候直接添加。

Q：AppTest邀请测试中的添加软件包，邀请用户等操作，是否可以使用[Testing API](../app/agc-help-test-api-reference-0000002271000709.md)进行自动化部署？

A：已开放的Testing API都是可用的，直接使用即可，但AppTest邀请测试创建内部测试群组、公开链接能力暂不支持API对接。
