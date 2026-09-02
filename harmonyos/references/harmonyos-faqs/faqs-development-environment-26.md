---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-26
title: DevEco Studio无法登录成功
breadcrumb: FAQ > DevEco Studio > 环境准备 > DevEco Studio无法登录成功
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f866503d46cf38fc85623958806e286a152146ae9546235db4ed6b3db665fdd2
---

## 问题现象

IDE登录华为账号，跳转浏览器登录华为账号后点击“允许”按钮，浏览器跳转至https://localhost:10101/xxx，提示“无法访问此网站”。

## 解决方案

出现该问题的原因一般是登录授权过程中，DevEco Studio与华为账号之间的登录通道异常导致，如点击了DevEco Studio登录界面的Cancel按钮，或者登录过程中，DevEco Studio异常关闭。

尝试以下操作：

1. 请尝试重新登录，建议在登录过程中不要做其他操作，避免误操作。
2. 检查HTTP Proxy设置。
   * 如果您的网络无需代理即可访问Internet，设置了代理会影响登录授权，请检查并将HTTP Proxy设置为“No proxy”。
   * 如果您的网络需要代理访问Internet，未设置代理会影响登录授权，请检查并将HTTP Proxy设置为“Manual proxy configuration”，设置方法可参考[DevEco Studio代理设置](../harmonyos-guides/ide-environment-config.md#section10369436568)。
