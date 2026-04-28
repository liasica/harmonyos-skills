---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-plugin-configuration
title: 自定义存储插件配置
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 自定义存储插件 > 自定义存储插件配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:54+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:c6dda6e0417ac96d5c2a9e3eea355fd3310be86fae6dc411bfb32a8f984bc526
---

ohpm-repo从2.2.0版本开始支持自定义存储插件（需要配套使用1.7.0及以上版本ohpm命令行工具），允许您开发定制化的存储插件来对接您自己的存储系统，您希望将ohpm-repo下的三方包文件存储在华为云OBS或者其他云存储平台，可以按照如下步骤来实现自定义存储插件。

注意

当您使用自定义存储插件对接自己的存储系统时，如果存在网络通信，建议使用https协议，确保信息安全传输。

## 准备工作

1. 下载ohpm-repo私仓工具安装包并解压。
2. 进入ohpm-repo部署根目录，把模板文件[tsconfig.json 文件](ide-ohpm-repo-template-file.md#section14188258114612)移动到ohpm-repo解压根目录。
3. **建议**将模板文件中[CustomStorage.ts](ide-ohpm-repo-template-file.md#section3671144204619)文件存入ohpm-repo解压根目录的plugins文件夹内。

## 编辑CustomStorage.ts文件，实现存储插件接口StoragePlugin

注意

* 打开CustomStorage.ts模板文件，需要编写代码实现接口类StoragePlugin，实现init, save, delete, download和getDownloadUrl五个基础函数，实现类CustomStorage的名字可自定义修改。
* 当使用自定义存储插件时，db存储位置必须为**MySQL**。

接口类StoragePlugin中包含如下五个函数，需要在实现类中完成功能的实现。

```
1. // 存储插件接口类定义如下
2. export interface StoragePlugin {

4. /**
5. * 初始化插件
6. */
7. init(): Promise<void>;

9. /**
10. * 上传文件
11. * @param srcPath 上传文件的本地路径
12. * @param packageInfo: 待上传包的详细信息，包括包名（含组织名）和包版本号两部分，包名：packageInfo.packageName，包版本：packageInfo.version.
13. * @returns 响应的返回信息
14. */
15. save(srcPath: string, packageInfo: any): Promise<string>;
16. /**
17. * 删除文件
18. * @param savedResponse 上传文件的响应值
19. * @returns 删除的结果：true表示删除成功
20. */
21. delete(savedResponse: string): Promise<boolean>;

23. /**
24. * 获取已上传文件的数据
25. * @param savedResponse 上传文件的响应值
26. * @returns 获取文件的内容，数据格式为 Buffer
27. */
28. download(savedResponse: string): Promise<Buffer>;

30. /**
31. * 根据保存文件生成的结果字符串，获取文件下载url
32. * @param savedResponse 保存文件的结果字符串
33. */
34. getDownloadUrl(savedResponse: string): Promise<string>;
35. }
```

1. init

   实现初始化准备工作。在配置文件config.yaml中store.config处可自定义一些插件所需要的参数信息，可通过函数getStorageConfigInfo()读取配置文件中自定义的参数信息。
2. save

   实现本地文件的上传功能。返回值为一个字符串，能够标识所上传的文件。函数入参为上传文件的本地路径srcPath和待上传包的详细信息packageInfo，packageInfo为可选项。

   在实现save方法的时候，上传每一个三方包有三类文件待上传：

   * 包文件（har包有：<package\_name>.har一个文件，tgz包有：<package\_name>.har和<package\_name>.hsp两个文件）；
   * 元数据文件（metadata.json文件）；
   * 文档文件（readme.md和changelog.md文件）。

   由于后面两类文件在每个三方包中名称都相同，请存放在不同位置或者使用不同文件名存储，避免文件被覆盖。
3. delete

   实现已上传文件的删除功能。函数入参为savedResponse：上传文件save后的返回信息，通过入参信息定位已上传文件，进行文件的删除；返回值信息为删除的结果，布尔类型。
4. download

   实现已上传文件的内容读取功能。函数入参为savedResponse：上传文件save后的返回信息，通过入参信息定位已上传文件，进行文件内容读取；返回所读取到的文件信息，数据类型为Buffer。
5. getDownloadUrl

   实现已上传文件下载URL的获取。函数入参为savedResponse：上传文件save后的返回信息，通过入参信息定位已上传文件，进行文件内容读取；返回所读取到文件的下载URL，数据类型为String。

注意

1. 在实现上述五个函数时，插件文件CustomStorage.ts需要引用：StoragePlugin接口类和getStorageConfigInfo方法，故需要根据当前插件文件CustomStorage.ts所在位置，正确地书写引用地址，被引用的接口类和方法地址如下：
   * getStorageConfigInfo方法所在文件的位置：ohpm-repo解压根目录/libs/common/getStorageConfigInfo
   * StoragePlugin接口类所在文件的位置：ohpm-repo解压根目录/libs/plugins/storage/customStorage/StoragePlugin
2. 如果插件文件CustomStorage.ts存储在默认位置（ohpm-repo解压根目录的plugins文件夹内），插件文件CustomStorage.ts中引用StoragePlugin类和getStorageConfigInfo方法的默认地址如下：
   * import {StoragePlugin} from '../libs/plugins/storage/customStorage/StoragePlugin';
   * import {getStorageConfigInfo} from '../libs/common/getStorageConfigInfo';

## 使用插件文件和启动ohpm-repo

1. 安装必要的npm包

   安装typescript包，编译ts文件为js文件。

   ```
   1. $ npm i typescript -g
   ```
2. 编译插件文件

   * 如果CustomStorage.ts存放在ohpm-repo安装根目录的plugins文件夹中，在ohpm-repo安装根目录下执行编译命令。

     ```
     1. $ tsc
     ```
   * 命令成功执行后会在ohpm-repo解压目录的plugins/outDir文件夹中生成编译后的文件CustomStorage.js。

     说明

     如果CustomStorage.ts没有存放在plugins内，请先修改[tsconfig.json](ide-ohpm-repo-template-file.md#section14188258114612)文件include和outDir参数，前者指定待编译插件代码的存储目录，后者指定编译完成后文件的输出位置，然后再在ohpm-repo解压根目录执行编译命令tsc。

     ```
     1. // tsconfig.json 文件中的默认配置
     2. // 默认值：插件存放在 ./plugins 中，编译后的文件存放在./plugins/outDir中
     3. "include": "plugins/*"          // 插件文件的位置
     4. "outDir": "./plugins/outDir"    // 编译后文件的存放位置
     ```
3. 编译后文件存放指定位置

   编译后获得的CustomStorage.js需要与CustomStorage.ts保持在同一级目录中，否则会运行出错，默认输出在./plugins/outDir 内，需要把CustomStorage.js拷贝到CustomStorage.ts同级目录./plugins中（ohpm-repo成功启动后可删除CustomStorage.ts文件）。
4. 编辑配置文件

   为了保证ohpm-repo能够正确加载自定义存储插件，需要修改配置文件config.yaml，主要涉及store处内容修改。

   ```
   1. // 配置文件中 store 项的格式参考
   2. store:
   3. type: custom
   4. config:
   5. export_name: CustomStorage
   6. plugin_path: plugins/CustomStorage.js
   7. custom_field: "test"
   8. #server: http://localhost:8088
   ```

   **参数说明****：**

   * type: 插件名称，如果是自定义插件，值必须为：custom。
   * config: 插件配置项，具体为：
     + export\_name: **必填**，自定义插件文件CustomStorage.js中定义的实现类名称，如果实现类为CustomStorage，故此处export\_name值为：CustomStorage。
     + plugin\_path: **必填**，编译后插件文件CustomStorage.js的存储位置。支持绝对路径和相对路径，相对路径的基准为ohpm-repo解压根目录。
     + custom\_field: **选填**，可配置多个，自定义名称和值，值的类型为字符串，方便在插件文件CustomStorage.ts中通过函数getStorageConfigInfo()进行读取。参考上述store项的格式，已添加配置参数custom\_field，故getStorageConfigInfo()函数的返回结果中会包含与custom\_field配置项同名的属性。
     + server: **选填项**，仓库内容的下载地址，但当[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)的host为0.0.0.0且本机存在多个网络接口时，则必须配置。
       - server的格式如下：<[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen) 的proto>://<host>:<[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen) 的port>
       - 当配置项[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)的host不为0.0.0.0时，则server**默认**取listen的完整格式，例如listen为127.0.0.1:8088，故server默认值为http://127.0.0.1:8088；
       - 当配置项[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)的host为0.0.0.0时，如果本机仅存在一个网络接口，则server中的host默认为 本机网络接口的ipv4地址；如果本机存在多个网络接口，则server中的host默认为本机获取到的第一个网络接口的ipv4地址，建议手动修改host为指定的本机ip/域名，例如listen为0.0.0.0:8088，故server需配置为http://<本机ip/域名>:8088；
       - 如果需要通过反向代理来访问ohpm-repo服务，则该字段须配置为反向代理服务器的域名地址。
5. ohpm-repo服务部署

   在完成上述操作之后，按照ohpm-repo部署指导，完成服务部署。
