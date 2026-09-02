---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-223
title: es2abc常见问题定位
breadcrumb: FAQ > DevEco Studio > 编译构建 > es2abc常见问题定位
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8cd62971c99eedf6b9ac753ce1cac5ef212ade09f516557adb937d6c78a08800
---

## 问题现象

使用IDE编译ArkTS/TS文件的时候，出现报错。

## 背景知识

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/PbJ3bmnpRlenuyqsPy9KVA/zh-cn_image_0000002628409364.png "点击放大")

* [ets\_frontend组件](https://gitcode.com/openharmony/arkcompiler_ets_frontend)是方舟运行时子系统的前端工具，结合[ace-ets2bundle组件](https://gitcode.com/openharmony/developtools_ace_ets2bundle/tree/master)，支持将ets文件转换为方舟字节码文件。使用ets\_frontend组件下的es2abc可执行文件将JavaScript文件转换为方舟字节码文件。

  ```txt
  cd out/rk3568/clang_x64/arkcompiler/ets_frontend/
  ./es2abc [options] file.js
  ```

  当不输入任何option参数时，默认生成方舟二进制文件。

  | 选项 | 描述 | 取值范围 | 默认值 |
  | --- | --- | --- | --- |
  | --debug-info | 携带调试信息。 | - | - |
  | --debugger-evaluate-expression | 在调试器下对输入的base64格式表达式进行求值。 | - | - |
  | --dump-assembly | 输出为汇编文件。 | - | - |
  | --dump-ast | 打印解析得到的抽象语法树（AST）。 | - | - |
  | --dump-debug-info | 打印调试信息。 | - | - |
  | --dump-literal-buffer | 打印字面量缓冲区内容。 | - | - |
  | --dump-size-stat | 显示字节码相关的统计信息。 | - | - |
  | --extension | 指定输入类型。 | ['js', 'ts', 'as'] | - |
  | --help | 帮助提示。 | - | - |
  | --module | 按照ESM模式编译。 | - | - |
  | --opt-level | 指定编译优化等级。 | ['0', '1', '2'] | 0 |
  | --output | 输出文件路径。 | - | - |
  | --parse-only | 只对输入文件做解析动作。 | - | - |
  | --thread | 指定生成字节码时所用的线程数目。 | 0-机器支持的线程数目 | 0 |

  更多使用说明请参考：[方舟运行时使用指南](https://gitcode.com/openharmony/arkcompiler_ets_runtime/blob/master/docs/README_zh.md)。
* [es2abc 编译器错误码](../harmonyos-references/errorcode-es2abc.md)和[通用错误码](../harmonyos-references/errorcode-universal.md)。

## 问题定位

编译时有如下报错信息：

1. Variable 'b' has already been declared.
2. Failed to get a resolved OhmUrl for "xxx" imported by "yyy".
3. ERROR: Cannot read properties of undefined (reading 'split').
4. ERROR: Cannot read properties of undefined (reading 'bundleName').
5. Error message:cannot find record '&<packageName>/&2.1.0', please check the request path.'/data/storage/el1/bundle/demo/ets/modules.abc'.
6. Error message:cannot find record '&<bytecodeharname>/<path>/filename&<version>', please check the request path.'/data/storage/el1/bundle/demo/ets/modules.abc'.
7. ArkTS:ERROR Failed to execute es2abc. Error Message: Failed to emit D:\xxx...\default\ets\modules.abc, error: Field {recordName.moduleRecordIdx} has different value.
8. ts2abc.js脚本，报错Lock blocked xxxx。

## 分析结论

1. 混淆增量编译的bug，混淆增量编译时，导入的名称和已有的名称重复。
2. 无法根据xxx生成ohmurl。
3. 没有从moduleInfo中获取到pkgPath。如果没有抛出报错Failed to get a resolved OhmUrl for "xxx" imported by "yyy"，打开SDK中module\_source\_file文件（目录在“sdk\HarmonyOS-NEXT-DB1\openharmony\ets\build-tools\ets-loader\lib\fast\_build\ark\_compiler\module\module\_source\_file.js”）找到getOhmurl方法打印日志。
4. 没有从moduleInfo中获取到pkgName或者语境信息表中没有收集到这个包。如果没有抛出报错Failed to get a resolved OhmUrl for "xxx" imported by "yyy"，打开SDK中module\_source\_file文件（目录在“sdk\HarmonyOS-NEXT-DB1\openharmony\ets\build-tools\ets-loader\lib\fast\_build\ark\_compiler\module\module\_source\_file.js”）找到getOhmurl方法打印日志。
5. ohmurl不合规，<packageName> + '/' + '&'这种格式的ohmurl不完整导致运行时找不到。
6. 运行时找不到&<bytecodeharname>/<path>/filename&<version>。
7. recordName对应了两个不同的文件路径。
8. 信息安全管理软件等进行了文件更改。

## 修改建议

1. 全量重新编译。关闭use\_hvigor\_cache=true选项，重新构建。
2. 排查方法：需要确认xxx所在模块类型。
   1. 如果是yyy所在模块是字节码har，排查yyy所在的包是否依赖xxx的包，如果没有依赖xxx模块，需要依赖xxx模块，字节码har不能通过相对路径引用本地源码har，可以将本地源码打成har包，做成依赖。
   2. 如果xxx所在模块是hsp，开发者检查yyy是否根据相对路径引入hsp内文件，如果是需要通过包依赖导入。
   3. 如果xxx所在模块是har包且以"hvigor\_ignore\_\_"开头，需要排查下所在模块的oh-package.json5是否包含packageType：interfaceHar，如果包含需要去掉。
   4. 检查xxx的路径是否和实际路径完全一致，如果不一致，需要改为正确路径。
   5. 如果xxx是以"hvigor\_ignore\_\_"开头，需要排查为什么xxx声明文件参与编译，检查yyy文件的import xxx位置是否符合规格。
   6. 如果xxx是个模块名，需要排查yyy所在模块中是否有依赖xxx，不能在devDependce中依赖，或者检查loader.json中"hspNameOhmMap"，"harNameOhmMap"是否包含xxx，校验是否存在大小写问题，如果大小写有问题需要在yyy中import的位置修改正确的模块名。
3. 根据打印日志排查问题。
4. 根据打印日志排查问题。
5. 导入只能是包名和具体文件路径，不能以'/'结尾；需要在此模块oh-package.json5中添加types或者main字段，或者排查此模块为什么没有配置入口。
6. 排查和修改方法：
   1. 排查record中的<path>/filename（注：报错信息中的路径）是否是所在模块正确的路径，如果不是，则是导入方式错误，全局搜索<path>/filename，修改正确的路径。
   2. 排查报错的version与语境信息表中（“projectName\entry\build\default\intermediates\loader\default\pkgContextInfo.json”）中<bytecodeharname>的version是否一致。如果不一致，修改oh-package.json5中的version为依赖的版本，重新编译。
7. 搜索报错中的recordName，分析不同文件的依赖关系，根据依赖关系情况进行处理。
8. 联系信息安全管理软件厂商解决。
