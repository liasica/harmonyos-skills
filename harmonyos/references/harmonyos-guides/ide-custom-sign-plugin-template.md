---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-custom-sign-plugin-template
title: 模板文件
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 自定义登录验证插件 > 模板文件
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1ed7c9317ec61e254b93d88655de09967686dab93226d0714baee9507945c16b
---

模板文件中包含自定义插件需要的两个文件：CustomVerify.ts和tsconfig.json。

## 插件模板CustomVerify.ts

**说明** 

插件模板文件支持自定义，开发者可修改类CustomVerify名称。

类CustomVerify名称需要与config.yaml配置文件中verify\_plugin的name属性保持一致。

```ts
import {VerifyPlugin} from '../libs/plugins/verify/VerifyPlugin';  // 插件文件CustomVerify.ts存储在默认位置（ohpm-repo解压根目录的plugins文件夹内），VerifyPlugin接口类的默认引用地址

interface VerifyUser {
  id: string;
  name: string;
  phone: string;
  email: string;
}

interface VerifyPluginConf {
  type: string;
  name: string;
  path: string;
  length: number;
  liveTime: number;
  receiver: string;
  [key: string]: any;
}

export class CustomVerify implements VerifyPlugin {

  /**
   * 发送验证码，返回发送结果
   * @param user
   * @param code
   * @param config
   * @returns 响应的返回信息，successCode为'0'表示成功
   */
  sendMsg(user: VerifyUser, code: string, config: VerifyPluginConf): Promise<{
    successCode:string
  }> {
    let successCode: string;
    return {
      successCode
    };
  };

  /**
   * 生成验证码
   * @param user
   * @param config
   * @returns 响应的返回信息，successCode为'0'表示成功
   */
  generateCode(user: VerifyUser, config: VerifyPluginConf): Promise<{
    successCode:string
  }> {
    let successCode: string;
    return {
      successCode
    };
  };

  /**
   * 验证用户输入的验证码
   * @param user
   * @param code
   * @param config
   * @returns 响应的返回信息，successCode为'0'表示成功
   */
  verifyCode(user: VerifyUser, code: string, config: VerifyPluginConf): Promise<{
    successCode:string
  }> {
    let successCode: string;
    return {
      successCode
    };
  };
}
```

## ts编译的配置文件tsconfig.json

```screen
// tsconfig.json 文件指定了编译项目所需的根目录下的文件以及编译选项，编译自定义插件文件.ts为.js文件。
{
  "include": [
    "plugins/*" // 插件文件的位置
  ],
  "compilerOptions": {
    "target": "es2016",
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true,
    "module": "commonjs",
    "rootDir": "./plugins",
    "typeRoots": [
      "./node_modules/@types"
    ],
    "types": [
      "node",
    ],
    "resolveJsonModule": true,
    "outDir": "./plugins/outDir",   // 编译后文件输出的位置
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "alwaysStrict": true,
    "strict": false,
    "noImplicitReturns": true,
    "skipLibCheck": true
  }
}
```
