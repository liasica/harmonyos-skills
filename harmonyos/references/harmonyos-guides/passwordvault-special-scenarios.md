---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/passwordvault-special-scenarios
title: 系统可适配的场景
breadcrumb: 指南 > 系统 > 安全 > 密码自动填充服务 > 应用接入密码保险箱 > 系统可适配的场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7a4eb56023483ae7e88b149a3c75348324c4458177e615213728812a8bf6994e
---

考虑到实际场景的多样性，除了上述接入示例中的场景外，密码保险箱针对部分场景的非标准场景进行了适配，可支持使用邮箱、手机号作为用户名登录、注册的场景。

当页面上存在一个Password/NEW\_PASSWORD类型输入框，且页面上同时存在USER\_NAME、Email、PhoneNumber类型输入框中的一种时，会正常触发密码保险箱保存和填充的能力。

当页面上仅有两个TextInput输入框，且其中一个为Password/NEW\_PASSWORD类型，另外一个为非密码类型时，也会正常触发密码保险箱逻辑。具体类型请参考[输入框类型说明](passwordvault-quick-adaptation.md#约束与限制)。

密码保险箱当前支持的所有场景：

* 页面上有**两个输入框**时，根据输入框类型的不同，密码保险箱的表现如下表。

  | 输入框类型 | 密码保险箱的表现 |
  | --- | --- |
  | InputType.USER\_NAME / InputType.Email / InputType.PhoneNumber输入框 + InputType.Password输入框 | - 点击其中一个输入框，触发账号密码填充提示。  - 页面跳转时，自动弹出账号密码保存提示框。 |
  | 非密码类型输入框 + InputType.Password输入框 | - 点击其中一个输入框，触发账号密码填充提示。  - 页面跳转时，自动弹出账号密码保存提示框。 |
  | InputType.USER\_NAME / InputType.Email / InputType.PhoneNumber输入框 + InputType.NEW\_PASSWORD输入框 | - 点击新密码输入框（InputType.NEW\_PASSWORD），触发强密码填充。  - 页面跳转时，如果直接使用生成的强密码，将静默保存到密码保险箱；如果使用自定义密码，即未使用或修改了生成的强密码，将弹出账号密码保存提示框。 |
  | 非密码类型输入框 + InputType.NEW\_PASSWORD输入框 | - 点击新密码输入框（InputType.NEW\_PASSWORD），触发强密码填充。  - 页面跳转时，如果直接使用生成的强密码，将静默保存到密码保险箱；如果使用自定义密码，即未使用或修改了生成的强密码，将弹出账号密码保存提示框。 |
* 当页面上有**多个输入框**时，根据输入框类型的不同，密码保险箱的表现如下表。

  | 输入框类型 | 密码保险箱的表现 |
  | --- | --- |
  | 含InputType.USER\_NAME / InputType.Email / InputType.PhoneNumber其中一种或多种 + 含InputType.Password输入框 | - 点击其中一个输入框，触发账号密码填充提示。  - 页面跳转时，自动弹出账号密码保存提示框。  - 保存账号密码时，优先保存USER\_NAME输入框的内容作为账户名。 |
  | 含InputType.USER\_NAME / InputType.Email / InputType.PhoneNumber其中一种或多种 + 含InputType.NEW\_PASSWORD输入框 | - 点击新密码输入框（InputType.NEW\_PASSWORD），触发强密码填充。  - 页面跳转时，如果直接使用生成的强密码，将静默保存到密码保险箱；如果使用自定义密码，即未使用或修改了生成的强密码，将弹出账号密码保存提示框。  - 保存账号密码时，优先保存USER\_NAME输入框的内容作为账户名。 |
  | 含InputType.USER\_NAME / InputType.Email / InputType.PhoneNumber其中一种或多种 + 含InputType.Password输入框 + 含InputType.NEW\_PASSWORD输入框 | - 点击其中一个输入框，触发账号密码填充提示。  - 点击新密码输入框（InputType.NEW\_PASSWORD），触发强密码填充。  - 页面跳转时，如果直接使用生成的强密码，将静默保存到密码保险箱；如果使用自定义密码，即未使用或修改了生成的强密码，将弹出账号密码保存提示框。  - 保存账号密码时，优先保存USER\_NAME输入框的内容作为账户名。 |
