---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-template-file
title: 模板文件
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 自定义存储插件 > 模板文件
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:55+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:2e64b25b216de1402a94b446965f6e12c38c8396436a34522b38a7ec0a0c5b85
---

模板文件中包含自定义storage插件需要的两个文件：CustomStorage.ts和tsconfig.json。

## 插件模板CustomStorage.ts

```
1. import {StoragePlugin} from '../libs/plugins/storage/customStorage/StoragePlugin';  // 插件文件CustomStorage.ts存储在默认位置（ohpm-repo解压根目录的plugins文件夹内），StoragePlugin接口类的默认引用地址
2. import {getStorageConfigInfo} from '../libs/common/getStorageConfigInfo';           // 插件文件CustomStorage.ts存储在默认位置（ohpm-repo解压根目录的plugins文件夹内），getStorageConfigInfo方法的默认引用地址
3. export class CustomStorage implements StoragePlugin {
4. async init(): Promise<void>{
5. // 配置文件中 store 项格式参考
6. // store:
7. //   type: custom    // store 存储类型为 custom，即用户自定义
8. //   config:         // 配置信息：export_name和plugin_path 是必选配置项
9. //     export_name: ExampleDemo          // 插件类的名字：例如 ExampleDemo
10. //     plugin_path: ../plugins/storage/customStorage/ExampleDemo.js    // 插件文件的存放位置
11. //     configInfo1: "info1";             // 自定义配置信息（可选项）
12. //     configInfo2: "info2";             // 自定义配置信息（可选项）
13. //     ...
14. // 通过函数 getStorageConfigInfo() 可以获取到配置文件config.yaml中store.config处自定义配置的信息
15. const configStorageInfo = await getStorageConfigInfo();
16. //举例说明：当配置文件 store.config处定义 configInfo1和 configInfo2信息，可读取
17. const configInfo1 = configStorageInfo.configInfo1 as string; //获取到configInfo1的值为 "info1"
18. const configInfo2 = configStorageInfo.configInfo2 as string; //获取到configInfo2的值为: "info2"
19. };

21. /**
22. * 通过文件的本地路径，把数据保存到指定的 storage 内
23. * @param srcPath： 上传文件的本地路径
24. * @param packageInfo: 可选参数，待上传包的详细信息，包含包名（含组织名）和包版本号两部分，包名：packageInfo.packageName，包版本：packageInfo.version.
25. * @returns 上传文件 save 后的返回信息： 能够标识文件，方便文件删除和读取
26. */
27. async save(srcPath: string, packageInfo: any): Promise<string>{
28. let savedResponse: string;
29. return savedResponse;
30. };

32. /** 通过上传文件获得的返回信息，定位文件，进行文件的删除，返回删除结果
33. * @param savedResponse： 上传文件 save 后的返回信息
34. * @returns 删除的结果：true 表示删除成功
35. */
36. async delete(savedResponse: string): Promise<boolean>{
37. let isDeleteSuccess: boolean;
38. return isDeleteSuccess;
39. };

41. /**
42. * 通过上传文件获得的返回信息，定位文件，进行获取文件内容，数据格式为 Buffer
43. * @param savedResponse 上传文件 save 后的返回信息
44. * @returns 获取文件的内容，数据格式为 Buffer
45. */
46. async download(savedResponse: string): Promise<Buffer>{
47. let fileContent: Buffer;
48. return fileContent;
49. };

51. /**
52. * 根据保存文件生成的结果字符串，获取文件下载url
53. * @param savedResponse 保存文件的结果字符串
54. */
55. async getDownloadUrl(savedResponse: string): Promise<string>{
56. let fileDownloadUrl: string;
57. return fileDownloadUrl;
58. };
59. }
```

## ts编译的配置文件tsconfig.json

```
1. // tsconfig.json 文件指定了编译项目所需的根目录下的文件以及编译选项，编译自定义插件文件 .ts 为 .js文件。
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
