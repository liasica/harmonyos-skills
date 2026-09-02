---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-custom-sign-plugin-configuration
title: 自定义登录验证插件配置
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 自定义登录验证插件 > 自定义登录验证插件配置
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:50e50e834863d47ef1a7491a39eae30e4a3ee37e7e13a6f4201108e47f1d0af6
---

ohpm-repo从6.0.1版本开始，支持配置自定义登录验证插件，允许您在登录时添加验证码进行校验，验证码可发送至您的邮箱或手机短信。按照如下步骤开发自定义登录验证插件。

在开启自定义登录验证插件前，需保证管理员账号已完善邮箱或手机号信息。否则开启登录验证插件后，收不到验证码，影响登录。

当您使用自定义登录验证插件对接自己的验证码发送系统时，如果存在网络通信，建议使用https协议，确保信息安全传输。

## 准备工作

1. 下载ohpm-repo私仓工具安装包并解压。
2. 进入ohpm-repo部署根目录，把模板文件[tsconfig.json](ide-custom-sign-plugin-template.md#section114302981817)存放到ohpm-repo解压根目录。
3. 建议将模板文件中[CustomVerify.ts](ide-custom-sign-plugin-template.md#section3671144204619)文件存放到ohpm-repo解压根目录的plugins文件夹内。

## 编辑插件文件，实现登录验证插件接口

在插件文件（CustomVerify.ts文件）中编写代码，实现验证插件接口类VerifyPlugin，类中包含sendMsg、generateCode和verifyCode三个函数。

在CustomVerify.ts文件中，通过相对路径或绝对路径引用接口类VerifyPlugin，VerifyPlugin接口类所在文件的位置为ohpm-repo解压根目录/libs/plugins/verify/VerifyPlugin。如果文件CustomVerify.ts存储在默认位置（即在ohpm-repo解压根目录下的plugins文件夹内），VerifyPlugin接口类地址为import {VerifyPlugin} from '../libs/plugins/verify/VerifyPlugin'。

**表1** 函数介绍

| 函数名 | 函数功能 | 参数 | 返回值 |
| --- | --- | --- | --- |
| sendMsg | 实现发送验证码功能。 | user：函数入参为待登录用户的用户信息。  code：验证码。  VerifyPluginConf：验证插件配置的验证插件对象。 | 返回一个对象，包含successCode字段，successCode为'0'表示成功，其他值表示失败。 |
| generateCode | 实现生成和发送验证码功能。 | user：函数入参为待登录用户的用户信息。  VerifyPluginConf：验证插件配置的验证插件对象。 |
| verifyCode | 实现对验证码进行验证功能。 | user：函数入参为待登录用户的用户信息。  code：验证码。  VerifyPluginConf：验证插件配置的验证插件对象。 |

**说明** 

[config.yaml](ide-ohpm-repo-configuration.md)文件中verify\_plugin.type为onlySend时，只需实现sendMsg一个函数；verify\_plugin.type为custom时，只需实现generateCode和verifyCode两个函数。

接口类VerifyPlugin实现如下：

```ts
// 验证插件接口类定义如下
export interface VerifyPlugin {

  /**
   * 发送验证码，返回发送结果
   * @param user
   * @param code
   * @param config
   * @returns 响应的返回信息，successCode为'0'表示成功
   */
  sendMsg(user: VerifyUser, code: string, config: VerifyPluginConf): Promise<{
    successCode:string
  }>;

  /**
   * 生成验证码
   * @param user
   * @param config
   * @returns 响应的返回信息，successCode为'0'表示成功
   */
  generateCode(user: VerifyUser, config: VerifyPluginConf): Promise<{
    successCode:string
  }>;

  /**
   * 验证用户输入的验证码
   * @param user
   * @param code
   * @param config
   * @returns 响应的返回信息，successCode为'0'表示成功
   */
  verifyCode(user: VerifyUser, code: string, config: VerifyPluginConf): Promise<{
    successCode:string
  }>;
}
```

## 使用插件文件和部署ohpm-repo

1. 安装typescript和@types/node的npm包。

   ```screen
   $ npm i typescript
   $ npm i @types/node
   ```
2. 编译插件文件，将CustomVerify.ts文件编译为CustomVerify.js文件。

   * 若CustomVerify.ts存放在ohpm-repo解压根目录下的plugins文件夹中，在ohpm-repo解压根目录下执行编译命令。

     ```screen
     $ tsc
     ```

     命令成功执行后在ohpm-repo解压目录下的plugins/outDir文件夹中生成CustomVerify.js文件。
   * 若CustomVerify.ts未存放在ohpm-repo解压根目录下的plugins文件夹中，请先修改[tsconfig.json](ide-custom-sign-plugin-template.md#section114302981817)文件include和outDir参数，前者指定待编译插件代码的存储目录，后者指定编译完成后文件的输出位置，然后在ohpm-repo解压根目录下执行编译命令tsc。

     ```screen
     // tsconfig.json 文件中的默认配置
     // 默认值：插件存放在 ./plugins 中，编译后的文件存放在./plugins/outDir中
     "include": "plugins/*"          // 插件文件的位置
     "outDir": "./plugins/outDir"    // 编译后文件的存放位置
     ```
3. 为编译后的CustomVerify.js文件指定存放位置。

   编译后获得的CustomVerify.js需要与CustomVerify.ts保持在同一级目录中，否则会运行出错。默认输出在./plugins/outDir内，需要把CustomVerify.js拷贝到CustomVerify.ts同级目录./plugins中。

   **说明** 

   ohpm-repo成功启动后可删除CustomVerify.ts文件。
4. 编辑config.yaml配置文件。

   为了保证ohpm-repo能够正确加载自定义登录验证插件，需要修改config.yaml配置文件，主要修改[verify\_plugin](ide-ohpm-repo-configuration.md#section1225919486412)。

   ```screen
   // 配置文件中store项的格式参考
   verify_plugin:
     type: onlySend                      # 插件实现类型，onlySend只发送验证码，验证码生成和验证有系统自动完成，custom插件负责生成发送和验证验证码
     name: CustomVerify                  # 验证码验证插件名称
     path: plugins/CustomVerify.js       # 插件的绝对路径或者相对于ohpm-repo软件包的路径，建议将插件放在软件包的plugins目录下
     length: 6                           # 验证码长度，取值范围为[4, 12]，onlySend模式使用
     liveTime: 300                       # 验证码有效时间，默认是5分钟，单位为秒，取值范围为[1, 3600], onlySend模式使用
     receiver: email                     # 接收验证码的终端，email：邮件，phone：手机号，对应到用户信息的邮箱和手机号
   ```
5. 部署ohpm-repo。

   在完成上述操作之后，按照[ohpm-repo部署指导](ide-ohpm-deploy-guide.md)，完成服务部署。
