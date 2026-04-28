---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-exception-stack-parsing-principle
title: 异常堆栈解析原理
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > 异常堆栈解析原理
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:422ddeb34989c846681d75f14aab0f3e30a20fa53f66115900b3d3868027f286
---

## 构建产物介绍

### ArkTS调试产物sourceMap

release模式编译产物，产物位置：{ProjectPath}/{ModuleName}/build/{product}/cache/default/default@CompileArkTS/esmodule/release/sourceMaps.map

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Wfct1Y4XSrWdzaEQOw2BpA/zh-cn_image_0000002530912872.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=25C362C21F483147B40C946F5333C66442F821FBA53D0B4DD5A19443228F191B)

### C++调试产物debug so

带debug信息的so数据，产物位置：{ProjectPath}/{ModuleName}/build/{product}/intermediates/libs

配置方式请参考[release编译带debug信息的so](ide-exception-stack-parsing-principle.md#section5147812132)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/FqnhGy-ORbCWjDmIg2v7jw/zh-cn_image_0000002530912888.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=F9D1994C4ADABE8EDE485DB619DB2A8620671A19BE6E0AAC57CFEBFB133AF3B7)

### 代码混淆产物nameCache

反混淆映射表，release模式编译产物，产物位置：{ProjectPath}/{ModuleName}/build/{product}/cache/default/default@CompileArkTS/esmodule/release/obfuscation

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/rSHSQPbDSjSHh0NvsbsYZQ/zh-cn_image_0000002530752886.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=291E7DBDFEF88D489826D6427D2DE770B9F41A7444E0B2906A3D4D59F99E4FF0)

## C++堆栈解析原理

### 编译选项差异

* Debug：不优化代码，附加调试信息。
* Release：最大化优化代码，但不包含调试信息。
* RelWithDebInfo：近似于Release模式，既进行了代码优化，同时保留部分调试信息。

### release编译带debug信息的so

通常release的so中的符号表、调试信息会被移除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/6Ob6xFUxT4C_mXr2g_D_PQ/zh-cn_image_0000002561832789.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=D4E5291AA352F874964796FA9A81D2DE543AEB23A5B98E747C90214C63B4AE46)

若需要保留so文件中的符号表、调试信息，需要在build-profile.json5的buildOption/externalNativeOptions中配置参数："arguments": "-DCMAKE\_BUILD\_TYPE=RelWithDebInfo"。

```
1. {
2. "apiType": "stageMode",
3. "buildOption": {
4. "externalNativeOptions": {
5. "path": "./src/main/cpp/CMakeLists.txt",
6. "arguments": "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
7. "cppFlags": "",
8. }
9. },
10. ...
11. }
```

编译后会生成2份so产物：

* libs：带debug信息的so。
* stripped\_native\_libs：移除调试信息等冗余数据后的so。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/vb-p2n5TRjmqvVYi0ZgCPw/zh-cn_image_0000002530912870.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=8EB2038D5770FF182CE91850E3C4E4AD0C243669BAEDFBE4EA2A70268E0AF88E)

### C++堆栈解析流程

llvm-addr2line（[获取llvm-addr2line工具](ide-exception-stack-parsing-principle.md#li11164144153)）是将函数地址解析成文件名或行号的工具。

给出一个可执行文件中的地址或一个可重定位对象中的偏移部分的地址，使用调试信息来找出与之相关的文件名和行号。

常用参数：

| 参数 | 用途 |
| --- | --- |
| -a | 以十六进制形式显示地址 |
| -C | 将符号名解码为用户级别的名字 |
| -e | 设置需要转换地址的可执行文件名 |
| -f | 显示文件名、行号和函数名信息 |
| -F | 显示函数名及文件行号 |
| -j | 读取指定部分的偏移量，而不是绝对地址 |
| -p | 每个地址信息单独占一行 |

参考示例：

查看文件名、行号和函数名相关信息：

```
1. llvm-addr2line -f -e File.so
```

查找指定的地址所对应的代码位置：

```
1. llvm-addr2line 0x00000000004005e7 -e test -f -C -s
```

例如：

```
1. llvm-addr2line -e libapplication.so 00003714 -f -C
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/Lzo9rhDBTvi_vDMIZTkchA/zh-cn_image_0000002530752868.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=3E17DC946DEA7C12183A0F7BB4FACFF62021E3B98B952C7361B3FE22943BE276)

ASan堆栈解析：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/WghJdmDUR620qgUKUYlXlA/zh-cn_image_0000002561832809.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=3A99A644134A381DC61CA0EE3FB754BADD6FE897CFB06FD11E26020A1E0ACD8B)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/jO6FZ_VkQ6S8NkwO2Fc10A/zh-cn_image_0000002530912890.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=9FE388BC28468D75E807CA8698C5B8530276FF1DA54D32AC7A8A5E506D8F6BD1)

### 常见问题

* 什么是UUID？

  每一个可执行程序都有一个build UUID来唯一标识。Crash日志包含发生crash的这个应用（app）的build UUID以及crash发生时应用加载的所有库文件的build UUID。
* 如何获取llvm-addr2line工具？

  在DevEco Studio安装目录/deveco-studio/sdk/default/openharmony/native/llvm/bin下即可找到llvm-addr2line.exe。

## ArkTS堆栈解析原理

### sourceMap格式

**图1** 源码   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/OlWeVcCdSj--lYV20zUN4Q/zh-cn_image_0000002530912876.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=13DE6A4A0E4D30EF8DD71104F5C76D284A67838CE9A3DF10B517A0093FF04B9D)

**图2** 编译后产物   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/Xv3_dbwUQO-FPa5Q-R-BJw/zh-cn_image_0000002561752827.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=FABCFEFD264521CCBD57412F19E70BC8E8BBFCFD00F47639678F4AF4C97EEA62 "点击放大")

**实际代码行映射关系：**

70->29

71->30

72->31

73->32

**sourceMap结构：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/DigfvSoKSie_gE-QWllI6w/zh-cn_image_0000002561752811.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=7B8DB3617BC8F006C1F826701F2B4958F028A0AB908FAA007033683EC47EE91D)

单个module构建产物sourceMaps.map为merge文件，实际包含该模块的所有文件的映射关系；每个json中key以编译构建产物的唯一路径作为主键，运行程序的abc中保留了对应的key信息，当运行时异常代码归属到该文件时输出信息为该key，sources为实际源码文件信息，用于异常堆栈还原源码；mappings为编码后的行列号映射表，每个文件有独立的映射关系。

* key：参考[sourceMap解析流程](ide-exception-stack-parsing-principle.md#section983741193211)。
* version：目前source map标准的版本为3。
* file：生成的文件名。
* sources：源文件地址列表。
* names：转换前的所有变量名和属性名。
* mappings：记录位置信息的字符串。
* sourceRoot：源文件目录地址，可以用于重新定位服务器上的源文件。
* entry-package-info："entry|1.0.0" 对应模块本身的oh-package.json中的name及version，用于关联反混淆nameCache资源版本。
* package-info: "har1|1.0.0" 对应非模块本身的oh-package.json中的name及version，即dependencies引用的代码，可用于引用三方库二次解析sourceMap。

### sourceMap解析流程

下图是sourceMap中每个json的key的结构化处理过程，以“entry|har1|1.0.0|src/main/ets/pages/w.ts”为例，各字段含义如下。

以“|”为分隔符，entry是本模块oh-package.json5中的name，har1|1.0.0是依赖的har1包的oh-package.json5中的name和version（如果没有依赖包，则是本模块oh-package.json5中的name和version），src/main/ets/pages/w.ts是引用的源码文件路径。

**图3** sourceMap中的key结构化处理   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/24FgIda-RRG8PMe8HQX2sg/zh-cn_image_0000002530912878.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=10ADE76AB9FE20314D6633285971366DEC1C9D83159F665AB3AA9D5E60266162 "点击放大")

## 反混淆解析原理

代码混淆配置请参考[代码混淆](ide-build-obfuscation.md)。

### 代码混淆产物介绍

混淆映射表：$ProjectPath\$ModuleName\build\$product\cache\default\default@CompileArkTS\esmodule\release\obfuscation\nameCache.json

```
1. {
2. "home/src/main/ets/homeability/HomeAbility.ets": {
3. "IdentifierCache": {
4. "#AbilityConstant": "AbilityConstant",
5. "#hilog": "hilog",
6. "#UIAbility": "UIAbility",
7. "#Want": "Want",
8. "#window": "window",
9. "HomeAbility#onWindowStageCreate#__function": "i"
10. },
11. "MemberMethodCache": {
12. "onCreate:10:16": "onCreate",
13. "onDestroy:18:20": "onDestroy",
14. "onWindowStageCreate:22:33": "onWindowStageCreate",
15. "onWindowStageDestroy:35:38": "onWindowStageDestroy",
16. "onForeground:40:43": "onForeground",
17. "onBackground:45:48": "onBackground"
18. },
19. "obfName": "home/src/main/ets/homeability/HomeAbility.ets"
20. },
21. "compileSdkVersion": "5.0.0.25",
22. "entryPackageInfo": "home|1.0.0",
23. "PropertyCache": {
24. "integratedHsp": "i",
25. "asanClick": "j",
26. "Index_Params": "m",
27. "testNapi": "o",
28. "Index": "t",
29. "testObfuscation": "g2"
30. }
31. }
```

* **originalfieldname**：该字段为每个文件的原始文件路径及名称，例如以上的"home/src/main/ets/homeability/HomeAbility.ets"。

* **ObfName**：key为固定字段，value为每个文件混淆后的名称，与**originalfieldname**配对。

  ```
  1. "obfName": "home/src/main/ets/pages/a.ts"
  ```
* **IdentifierCache**：该字段对应的值为该文件下的变量名混淆前后的映射关系。

  变量名分为两类：普通变量、类方法变量。

  普通变量映射关系的格式如下：

  ```
  1. originalvariablename :  obfuscatedvariablename
  ```

  + originalvariablename 表示原始的变量名称。
  + obfuscatedvariablename 表示混淆后的变量名称。

  类方法变量映射关系的格式如下：

  ```
  1. /*--------------------------key----------------------------------  :  -----------value----------*/
  2. originalmethodname: originalmethodstartline: originalmethodendline :  obfuscatedmethodname
  ```

  + originalmethodname 表示原始的方法名称。
  + [:originalmethodstartline:originalmethodendline] 表示原始的方法起始行数与结束行数，左右都是闭区间。
  + obfuscatedmethodname 表示混淆后的方法名称。
* **MemberMethodCache**：该字段对应的值为该文件下的成员方法名混淆前后的映射关系。

  开启属性混淆时，成员方法映射关系的格式如下：

  ```
  1. /*--------------------------key---------------------------------  :  -----------value----------*/
  2. originalmethodname:originalmethodstartline:originalmethodendline  :  obfuscatedmethodname
  ```

  未开启属性混淆时，成员方法映射关系的格式如下：

  ```
  1. /*--------------------------key-------------------------------------  :  -----------value----------*/
  2. originalmethodname : originalmethodstartline : originalmethodendline  :  originalmethodname
  ```

  + originalmethodname 表示原始的成员方法名称。
  + [:originalmethodstartline :originalmethodendline] 表示原始的成员方法起始行数与结束行数，左右都是闭区间。
  + obfuscatedmethodname 表示混淆后的成员方法名称。
* **PropertyCache**：该字段对应的值为全局所有属性名混淆前后的映射关系，只有在开启属性混淆时才会有值。

  属性名映射关系格式如下：

  ```
  1. /*--------key-------  :  -----------value----------*/
  2. originalpropertyname  :  obfuscatedmethodname
  ```

  + originalpropertyname 表示原始的属性名称。
  + obfuscatedmethodname 表示混淆后的属性名称。

### 代码混淆解析

异常堆栈如下：

```
1. Pid:58348
2. Uid:20020156
3. Reason:RangeError
4. Error name:RangeError
5. Error message:The number cannot be converted to a BigInt because it is not an integer
6. Stacktrace:
7. Cannot get SourceMap info, dump raw stack:
8. at g2 (home|home|1.0.0|src/main/ets/pages/a.ts:6:6)
9. at getVersion (home|home|1.0.0|src/main/ets/pages/a.ts:2:2)
10. at anonymous (home|home|1.0.0|src/main/ets/pages/Index.ts:61:61)
```

1. 经过sourceMap映射转码堆栈如下：

   ```
   1. at g2 (home/src/main/ets/pages/tool.ts:7:27)
   2. at getVersion (home/src/main/ets/pages/tool.ts:2:30)
   3. at anonymous (home/src/main/ets/pages/Index.ets:23:40)
   ```

   a.ts通过sourceMap还原为tool.ts。

   ```
   1. "home|home|1.0.0|src/main/ets/pages/a.ts": {
   2. "version": 3,
   3. "file": "tool.ts",
   4. "sources": [
   5. "home/src/main/ets/pages/tool.ts"
   6. ],
   7. "names": [],
   8. "mappings": "AAAA,MAAM,CAAC,OAAO,UAAU,UAAU,IAAI,MAAM;IAC1C,IAAI,KAAM,IAAiB,CAAA;IAC3B,UAAW;AACb,CAAC;AAED,eAA2B,MAAM;IAC/B,IAAI,GAAG,GAAG,MAAM,CAAC,MAAM,CAAC,CAAA;IACxB,OAAO,GAAG,CAAC;AACb,CAAC",
   9. "sourceRoot": "",
   10. "entry-package-info": "home|1.0.0"
   11. }
   ```
2. 函数级文件名映射。

   查看混淆映射表：$ProjectPath\$ModuleName\build\$product\cache\default\default@CompileArkTS\esmodule\release\obfuscation\nameCache.json

   ```
   1. "home/src/main/ets/pages/tool.ts": {
   2. "IdentifierCache": {
   3. "getVersion#res": "h2",
   4. "#testObfuscation:6:9": "g2"
   5. },
   6. "MemberMethodCache": {},
   7. "obfName": "home/src/main/ets/pages/a.ts"
   8. }
   ```

   该字段的IdentifierCache与MemberMethodCache中保存了方法名混淆前后的映射关系，对应格式为："源码方法名:该方法起始行号:该方法结束行号":"混淆后方法名"。

   源码方法名中的"源码方法名"代表上下级关系，故匹配后可以通过"#"保留最后名称。

   第一条堆栈混淆后的方法名为"g2"，若存在多个"g2"则需要通过行号范围过滤，故利用上述字段对该方法名进行还原：

   1. 通过key(home/src/main/ets/pages/tool.ts)查找到映射表。
   2. 在上述字段中找出所有混淆后方法名为"g2"的条目，该条目为：

      ```
      1. "#testObfuscation:6:9": "g2"
      ```
   3. 找到行号范围包含步骤一中还原后行号的条目，步骤一中得到的行号为7包含在6-9之内，因此可以得到源码对应方法名为"#testObfuscation"，经过字符串处理结果为"testObfuscation"。

      ```
      1. at testObfuscation (home/src/main/ets/pages/tool.ts:7:27)
      2. at getVersion (home/src/main/ets/pages/tool.ts:2:30)
      3. at anonymous (home/src/main/ets/pages/Index.ets:23:40)
      ```
