---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-custom-auth-plugin-template
title: 模板文件
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 自定义认证插件 > 模板文件
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:55+08:00
doc_updated_at: 2026-03-24
content_hash: sha256:244fbf73ed50880acb1d9b439ca887823f88ba4329eac81fb81c53842295909f
---

模板文件中包含自定义auth插件需要的两个文件：CustomAuth.ts和tsconfig.json。

## 插件模板CustomAuth.ts

```
1. import {AuthPlugin} from '../libs/plugins/auth/AuthPlugin';  // 插件文件CustomAuth.ts存储在默认位置（ohpm-repo解压根目录的plugins文件夹内），默认引用地址
2. export class CustomAuth implements AuthPlugin {
3. /**
4. * 用户认证:根据accessToken的值，返回用户的数据:用户的id，用户的名字，用户所属的组织，用户所创建的组织
5. * @param accessToken 用户的accessToken
6. */
7. async auth(accessToken: string): Promise<{
8. id: string;                         // 用户的id，保证唯一性
9. name: string;                       // 用户的名字，保证唯一性
10. belongGroupList: Array<string>;     // 用户所在的组织，具有发布指定组织包的权限
11. groupAdminList: Array<string>;      // 用户所管理的组织，具有删除指定组织内包的权限
12. }> {
13. let id: string, name: string, belongGroupList: Array<string>, groupAdminList: Array<string>;
14. return {id, name, belongGroupList, groupAdminList};
15. }

17. /**
18. * 用户信息获取:根据只读accessToken的值，返回用户的数据:用户id，用户名字，用户所属的组织，用户所创建的组织
19. * @param accessToken 用户的只读accessToken
20. */
21. async authWithReadOnly(accessToken: string): Promise<{
22. id: string;                         // 用户的id，保证唯一性
23. name: string;                       // 用户的名字，保证唯一性
24. belongGroupList: Array<string>;     // 用户所在的组织，具有发指定组织包的权限
25. groupAdminList: Array<string>;      // 用户所管理的组织，具有删除指定组织内包的权限
26. }> {
27. let id: string, name: string, belongGroupList: Array<string>, groupAdminList: Array<string>;
28. return {id, name, belongGroupList, groupAdminList};
29. }

31. /**
32. * 根据用户id,返回用户的名字
33. * @param id 用户的id值
34. */
35. async getUserInfo(id: string): Promise<string> {
36. let name: string;
37. return name;
38. }
39. }
```

## ts编译的配置文件tsconfig.json

```
1. // tsconfig.json 文件指定了编译项目所需的根目录下的文件以及编译选项，编译自定义插件文件.ts为.js文件。
2. {
3. "include": [
4. "plugins/*" // 插件文件的位置
5. ],
6. "compilerOptions": {
7. "target": "es2016",
8. "experimentalDecorators": true,
9. "emitDecoratorMetadata": true,
10. "module": "commonjs",
11. "rootDirs": [
12. "./src",
13. "./test"
14. ],
15. "typeRoots": [
16. "./node_modules/@types"
17. ],
18. "types": [
19. "node",
20. ],
21. "resolveJsonModule": true,
22. "outDir": "./plugins/outDir",   // 编译后文件输出的位置
23. "esModuleInterop": true,
24. "forceConsistentCasingInFileNames": true,
25. "alwaysStrict": true,
26. "noImplicitReturns": true,
27. "skipLibCheck": true
28. }
29. }
```
