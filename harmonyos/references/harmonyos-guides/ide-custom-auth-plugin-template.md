---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-custom-auth-plugin-template
title: 模板文件
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 自定义认证插件 > 模板文件
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9322d87c355b1959b937046c6c6f50fa6f2180c0066b0d80c6f394c7c301ab07
---

模板文件中包含自定义auth插件需要的两个文件：CustomAuth.ts和tsconfig.json。

## 插件模板CustomAuth.ts

```ts
import {AuthPlugin} from '../libs/plugins/auth/AuthPlugin';  // 插件文件CustomAuth.ts存储在默认位置（ohpm-repo解压根目录的plugins文件夹内），默认引用地址
export class CustomAuth implements AuthPlugin {
  /**
   * 用户认证:根据accessToken的值，返回用户的数据:用户的id，用户的名字，用户所属的组织，用户所创建的组织
   * @param accessToken 用户的accessToken
   */
  async auth(accessToken: string): Promise<{
    id: string;                         // 用户的id，保证唯一性
    name: string;                       // 用户的名字，保证唯一性
    belongGroupList: Array<string>;     // 用户所在的组织，具有发布指定组织包的权限
    groupAdminList: Array<string>;      // 用户所管理的组织，具有删除指定组织内包的权限
  }> {
    let id: string, name: string, belongGroupList: Array<string>, groupAdminList: Array<string>;
    return {id, name, belongGroupList, groupAdminList};
  }

  /**
   * 用户信息获取:根据只读accessToken的值，返回用户的数据:用户id，用户名字，用户所属的组织，用户所创建的组织
   * @param accessToken 用户的只读accessToken
   */
  async authWithReadOnly(accessToken: string): Promise<{
    id: string;                         // 用户的id，保证唯一性
    name: string;                       // 用户的名字，保证唯一性
    belongGroupList: Array<string>;     // 用户所在的组织，具有发布指定组织包的权限
    groupAdminList: Array<string>;      // 用户所管理的组织，具有删除指定组织内包的权限
  }> {
    let id: string, name: string, belongGroupList: Array<string>, groupAdminList: Array<string>;
    return {id, name, belongGroupList, groupAdminList};
  }

  /**
   * 根据用户id,返回用户的名字
   * @param id 用户的id值
   */
  async getUserInfo(id: string): Promise<string> {
    let name: string;
    return name;
  }
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
