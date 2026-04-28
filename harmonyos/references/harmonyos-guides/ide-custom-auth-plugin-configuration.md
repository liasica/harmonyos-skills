---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-custom-auth-plugin-configuration
title: 自定义认证插件配置
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 自定义认证插件 > 自定义认证插件配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:55+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:879b891f9b296ad12be6454a23f78febf8d9eef07e29f23f594cba5f73e6ab86
---

ohpm-repo从2.3.0版本开始支持自定义认证插件（需配套使用1.8.0及以上版本ohpm命令行工具），允许您使用AccessToken认证，开发定制化的认证插件来对接开发者自己的用户信息系统。

注意

当您使用自定义认证插件对接自己的用户系统时，如果存在网络通信，建议使用https协议，确保信息安全传输。

## 准备工作

1. 下载ohpm-repo私仓工具安装包并解压。
2. 进入ohpm-repo解压根目录，把模板文件中[tsconfig.json 文件](ide-custom-auth-plugin-template.md#section14188258114612)移动到ohpm-repo解压根目录。
3. 建议将模板文件中[CustomAuth.ts](ide-custom-auth-plugin-template.md#section14072085013)文件存入ohpm-repo解压根目录的plugins文件夹内。

## 编辑CustomAuth.ts文件，实现认证插件接口AuthPlugin

注意

打开CustomAuth.ts模板文件，需要编写代码实现接口类AuthPlugin，实现auth和getUserInfo两个基础方法，实现类CustomAuth的名字可自定义修改。

接口类AuthPlugin中包含如下三个方法，需要在实现类中完成功能的实现。

```
1. // 插件文件的接口类定义如下
2. export interface AuthPlugin {
3. /**
4. * 用户信息获取:根据读写accessToken的值，返回用户的数据:用户的id，用户的名字，用户所属的组织，用户所创建的组织
5. * @param accessToken 用户的读写accessToken
6. * @returns
7. * id：用户的id，保证唯一性
8. * name：用户的名字，保证唯一性
9. * belongGroupList：用户所在的组织，具有发指定组织包的权限
10. * groupAdminList： 用户所管理的组织，具有删除组织内包的权限
11. */
12. auth(accessToken: string): Promise<{
13. id: string;
14. name: string;
15. belongGroupList: Array<string>;
16. groupAdminList: Array<string>;
17. }>;

19. /**
20. * 用户信息获取:根据只读accessToken的值，返回用户的数据:用户的id，用户的名字，用户所属的组织，用户所创建的组织
21. * @param accessToken 用户的只读accessToken
22. * @returns
23. * id：用户的id，保证唯一性
24. * name：用户的名字，保证唯一性
25. * belongGroupList：用户所在的组织，具有发指定组织包的权限
26. * groupAdminList： 用户所管理的组织，具有删除组织内包的权限
27. */
28. authWithReadOnly(accessToken: string): Promise<{
29. id: string;
30. name: string;
31. belongGroupList: Array<string>;
32. groupAdminList: Array<string>;
33. }>;

35. /**
36. * 根据用户id,返回用户的名字
37. * @param id 用户的id值
38. */
39. getUserInfo(id: string): Promise<string>;
40. }
```

1. auth

   通过读写AccessToken获取对应用户信息，函数的入参为读写AccessToken值，返回值有四个参数：用户的id值，用户的name值，用户所属的组织列表belongGroupList，用户所管理的组织列表groupAdminList。
2. authWithReadOnly（5.0.5版本新增）

   通过只读AccessToken获取对应用户信息，函数的入参为只读AccessToken值，返回值有四个参数：用户的id值，用户的name值，用户所属的组织列表belongGroupList，用户所管理的组织列表groupAdminList。当ohpm-repo配置不支持匿名访问时，ohpm可以通过配置只读AccessToken值，获取执行install,info和update命令的权限。
3. getUserInfo

   实现根据用户id获取用户名字的功能。函数入参为用户的id值；返回值为用户的名字。

注意

1. AccessToken分两种权限等级：只读AccessToken允许ohpm命令行执行info，install和update操作，只需要ohpm-repo读权限；读写AccessToken除了包含只读权限外，还支持执行publish，unpublish和dist-tags相关操作，需要ohpm-repo读写权限。
2. 如果ohpm-repo支持匿名访问，ohpm执行info，install和update等读操作命令，不需要配置AccessToken值；当ohpm-repo配置不支持匿名访问时，必须配置只读/读写AccessToken，才能获得执行info，install和update命令权限。
3. 在实现上述三个函数时，插件文件CustomAuth.ts需要引用AuthPlugin接口类，故需要根据当前插件文件CustomAuth.ts所在位置，正确地编写AuthPlugin接口类的引用地址，被引用接口类所在文件的地址如下：
   * AuthPlugin接口类所在文件的位置：ohpm-repo解压根目录/libs/plugins/auth/AuthPlugin
4. 如果插件文件CustomAuth.ts存储在默认位置（ohpm-repo解压根目录中plugins文件夹内），插件文件CustomAuth.ts中默认AuthPlugin接口类引用地址如下：
   * import {AuthPlugin} from '../libs/plugins/auth/AuthPlugin';

## 插件文件的使用和ohpm-repo的启动

1. 安装必要的npm包。安装typescript和@types/node包，编译ts文件为js文件。

   ```
   1. $ npm i typescript
   2. $ npm i @types/node
   ```
2. 编译插件文件。
   * 如果CustomAuth.ts存放在ohpm-repo解压根目录的plugins文件夹中，在ohpm-repo解压根目录下执行编译命令。

     ```
     1. $ tsc
     ```
   * 命令成功执行后会在ohpm-repo解压根目录的plugins/outDir文件夹中生成编译后的文件CustomAuth.js。

     说明

     如果CustomAuth.ts没有存放在ohpm-repo解压根目录的plugins内，请先修改[tsconfig.json 文件](ide-custom-auth-plugin-template.md#section14188258114612)中include和outDir参数，前者指定待编译插件代码的存储目录，后者指定编译完成后文件的输出位置，然后再在ohpm-repo解压根目录执行编译命令tsc。

     ```
     1. // tsconfig.json 文件中的默认配置
     2. // 默认值：插件存放在 ./plugins 中，编译后的文件存放在./plugins/outDir中
     3. "include": "plugins/*"          // 插件文件的位置
     4. "outDir": "./plugins/outDir"    // 编译后文件的存放位置
     ```
3. 编译后文件存放指定位置。

   编译后获得的CustomAuth.js需要与CustomAuth.ts 保持在同一级目录中，否则会编译出错，默认输出在./plugins/outDir内，需要把CustomAuth.js拷贝到CustomAuth.ts同级目录./plugins中（ohpm-repo成功启动后可删除CustomAuth.ts文件）。
4. 编辑配置文件。为了保证ohpm-repo能够正确加载自定义认证插件，需要修改配置文件config.yaml中auth\_plugin配置项（配置文件默认没有配置auth\_plugin参数）。

   ```
   1. // 配置文件中 auth_plugin 项的格式参考
   2. auth_plugin:
   3. name: CustomAuth
   4. path: plugins/CustomAuth.js
   ```

   参数说明：

   * name: 插件名称，自定义插件文件CustomAuth.js中定义的实现类名称，如果实现类为CustomAuth，故此处name值为：CustomAuth 。
   * path: 编译后插件文件CustomAuth.js的存储位置。支持绝对路径和相对路径，相对路径的基准为ohpm-repo解压根目录。
5. ohpm-repo服务部署。在完成上述操作之后，按照ohpm-repo[部署指导](ide-ohpm-deploy-guide.md)，完成服务部署。
6. 使用自定义认证插件进行包的发布和下架等操作。

   当ohpm-repo成功启动后，在ohpm客户端的配置文件.ohpmrc中新增一行（//是有效字符，不是注释，勿删）。

   * 通过authWithReadOnly认证：配置只读AccessToken，ohpm能够执行info，install和update命令，这三个命令需要读取ohpm-repo数据权限。

     ```
     1. //<ip>:<port>/repos/ohpm/:_read_auth=<readOnlyToken>
     ```
   * 通过auth认证：配置读写AccessToken，ohpm除了能够执行需要ohpm-repo读权限的info，install和update命令，还能够执行publish，unpublish和dist-tags等需要读写权限命令。

     ```
     1. //<ip>:<port>/repos/ohpm/:_auth=<readWriteToken>
     ```

   其中ip和port为ohpm-repo私仓启动机器所在的ip值和端口值；readOnlyToken/readWriteToken为用户信息系统内有效的只读/读写accessToken值，通过该accessToken值，用户调用自定义认证插件CustomAuth中auth和authWithReadOnly方法，能够获取到有效的用户信息。
