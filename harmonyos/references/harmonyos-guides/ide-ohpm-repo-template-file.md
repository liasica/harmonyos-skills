---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-template-file
title: 模板文件
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 自定义存储插件 > 模板文件
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3d99bbfef6add434b0b6889888b1490876f4b96a1f7dc558e690a5c41075f13b
---

模板文件中包含自定义storage插件需要的两个文件：CustomStorage.ts和tsconfig.json。

## 插件模板CustomStorage.ts

```ts
import {StoragePlugin} from '../libs/plugins/storage/customStorage/StoragePlugin';  // 插件文件CustomStorage.ts存储在默认位置（ohpm-repo解压根目录的plugins文件夹内），StoragePlugin接口类的默认引用地址
import {getStorageConfigInfo} from '../libs/common/getStorageConfigInfo';           // 插件文件CustomStorage.ts存储在默认位置（ohpm-repo解压根目录的plugins文件夹内），getStorageConfigInfo方法的默认引用地址
export class CustomStorage implements StoragePlugin {
  async init(): Promise<void>{
    // 配置文件中 store 项格式参考
    // store:
    //   type: custom    // store 存储类型为 custom，即用户自定义
    //   config:         // 配置信息：export_name和plugin_path 是必选配置项
    //     export_name: ExampleDemo          // 插件类的名字：例如 ExampleDemo
    //     plugin_path: ../plugins/storage/customStorage/ExampleDemo.js    // 插件文件的存放位置
    //     configInfo1: "info1";             // 自定义配置信息（可选项）
    //     configInfo2: "info2";             // 自定义配置信息（可选项）
    //     ...
    // 通过函数 getStorageConfigInfo() 可以获取到配置文件config.yaml中store.config处自定义配置的信息
    const configStorageInfo = await getStorageConfigInfo();
    //举例说明：当配置文件 store.config处定义 configInfo1和 configInfo2信息，可读取
    const configInfo1 = configStorageInfo.configInfo1 as string; //获取到configInfo1的值为 "info1"
    const configInfo2 = configStorageInfo.configInfo2 as string; //获取到configInfo2的值为: "info2"
  };

  /**
   * 通过文件的本地路径，把数据保存到指定的 storage 内
   * @param srcPath： 上传文件的本地路径
   * @param packageInfo: 可选参数，待上传包的详细信息，包含包名（含组织名）和包版本号两部分，包名：packageInfo.packageName，包版本：packageInfo.version.
   * @returns 上传文件 save 后的返回信息： 能够标识文件，方便文件删除和读取
   */
  async save(srcPath: string, packageInfo: any): Promise<string>{
    let savedResponse: string;
    return savedResponse;
  };

  /** 通过上传文件获得的返回信息，定位文件，进行文件的删除，返回删除结果
   * @param savedResponse： 上传文件 save 后的返回信息
   * @returns 删除的结果：true 表示删除成功
   */
  async delete(savedResponse: string): Promise<boolean>{
    let isDeleteSuccess: boolean;
    return isDeleteSuccess;
  };

  /**
   * 通过上传文件获得的返回信息，定位文件，进行获取文件内容，数据格式为 Buffer
   * @param savedResponse 上传文件 save 后的返回信息
   * @returns 获取文件的内容，数据格式为 Buffer
   */
  async download(savedResponse: string): Promise<Buffer>{
    let fileContent: Buffer;
    return fileContent;
  };

 /**
   * 根据保存文件生成的结果字符串，获取文件下载url
   * @param savedResponse 保存文件的结果字符串
   */
  async getDownloadUrl(savedResponse: string): Promise<string>{
    let fileDownloadUrl: string;
    return fileDownloadUrl;
  };
}
```

## ts编译的配置文件tsconfig.json

```json
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
