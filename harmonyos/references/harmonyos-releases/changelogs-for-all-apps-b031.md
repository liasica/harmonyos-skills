---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-b031
title: 针对所有应用的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > 接口行为变更说明 > HarmonyOS NEXT Developer Beta2引入的接口行为变更 > 针对所有应用的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:13+08:00
doc_updated_at: 2026-01-19
content_hash: sha256:15a317c3f6c6c46d3b54a2e0ce3cb240fa80082f106328452c48ea7eb41891d2
---

## NDK开发

### 匿名内存执行权限管控策略变更说明

**变更原因**

为了维护生态的纯净，防止恶意应用向匿名内存注入指令，实现任意代码执行，以绕过代码签名管控，达到变脸或攻击系统的目的，系统要限制应用内设置匿名内存为可执行的行为。

**变更影响**

此变更涉及应用适配。

应用在申请内存或修改内存权限时，将匿名内存（MAP\_ANONYMOUS）的权限设置为可执行（PROT\_EXEC），相应行为会被系统拦截，具体如下：

1. 应用调用mmap申请包含执行权限的匿名内存将返回MAP\_FAILED。
2. 应用调用mprotect更新匿名内存为可执行权限，调用失败，结果返回-1，errno输出为EINVAL。

**该能力起始支持的API Level**

不涉及API

**变更的接口/组件**

不涉及

**适配指导**

变更后，开发者使用如下样例申请匿名内存或修改匿名内存权限将被系统禁止：

```
1. // 管控行为1：申请匿名内存时设置内存权限为可执行
2. mmap(NULL, len, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_ANONYMOUS, -1, 0);

4. // 管控行为2：申请匿名内存后，再设置内存的权限为可执行
5. addr = mmap(NULL, len, PROT_READ | PROT_WRITE, MAP_ANONYMOUS, -1, 0);

7. // ...
8. mprotect(addr, leng, PROT_READ | PROT_EXEC);
```

如开发者应用嵌入了V8或LuaJIT引擎，需要关闭引擎的JIT功能或考虑接入系统预置的JS引擎（有JIT能力）：

* 关闭v8的JIT功能：

  + 编译时关闭：在编译v8的GN文件里面加入v8\_jitless = true选项
  + 运行时关闭：在v8启动时传入--jitless参数，例如：

    ```
    1. int secArgc = ARGCNT;
    2. char *secArgv[ARGCNT] = {"--jitless"};
    3. v8::V8::SetFlagsFromCommandLine(&secArgc, secArgv, false);
    ```
* 关闭LuaJIT的JIT功能：

  + 编译时关闭：在编译时XCFLAGS添加-DLUAJIT\_DISABLE\_JIT 参数，支持make时直接传入，以及修改LuaJIT源码目录src/Makefile
* 接入系统预置JS引擎：

  为满足开发者对性能的要求，系统内提供了预置JS引擎。具体可参考[NDK开发指导](../harmonyos-guides-V5/ndk-development-overview-V5.md)。

### 应用编译构建对不支持命令强校验

**变更原因**

cmake从3.16.5版本升级到3.28.2版本，引入了该项变更。

**变更影响**

此变更涉及应用适配。

变更前：

应用编译构建会忽略不支持的命令参数，功能正常。

变更后：

在开发者使用不支持的命令参数（如 -v）时，应用编译构建将出现失败提示，提示内容如下：

```
1. CMake Error: Unknown argument -v
2. CMake Error: Run 'cmake --help' for all supported options.
```

**该能力起始支持的API Level**

不涉及API

**变更的接口/组件**

不涉及

**适配指导**

1. 查询支持的命令参数

   命令行执行 cmake --help 可以查看支持的命令参数合集

   我们也可以在 [cmake.org](https://cmake.org/cmake/help/v3.28/manual/cmake.1.html) 查看 cmake 官方指导文档，Options 详细描述了支持的命令参数合集及其说明
2. DevEco Studio构建的项目适配，删除项目模块目录下 build-profile.json5 中 arguments 配置的不支持的参数，删除内容如下：

   ```
   1. {
   2. "apiType": '',
   3. "buildOption": {
   4. "externalNativeOptions": {
   5. "path": "",
   6. "arguments": "-v",   // 删除该项配置中不支持的参数，如删除-v
   7. "cppFlags": "",
   8. }
   9. },
   10. // ...
   11. }
   ```
3. 命令行构建的项目适配，删除构建命令中不支持的参数，删除内容如下：

   ```
   1. {native所在目录}/build-tools/cmake/bin/cmake
   2. -HC:{项目所在目录}/entry/src/main/cpp
   3. -BC:{项目所在目录}/entry/.cxx/default/default/arm64-v8a
   4. -DOHOS_ARCH=arm64-v8a
   5. -DCMAKE_LIBRARY_OUTPUT_DIRECTORY={项目所在目录}/entry/build/default/intermediates/cmake/default/obj/arm64-v8a
   6. -DCMAKE_BUILD_TYPE=Debug
   7. -DOHOS_SDK_NATIVE={native所在目录}
   8. -DCMAKE_SYSTEM_NAME=OHOS
   9. -DCMAKE_OHOS_ARCH_ABI=arm64-v8a
   10. -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
   11. -DCMAKE_TOOLCHAIN_FILE={native所在目录}/build/cmake/ohos.toolchain.cmake
   12. -GNinja
   13. -DCMAKE_MAKE_PROGRAM={native所在目录}/build-tools/cmake/bin/ninja
   14. --no-warn-unused-cli
   15. -v  // 删除执行命令中不支持的参数-v
   ```

### 应用编译构建建议cmake\_minimum\_required修改为不低于3.5.0的版本

**变更原因**

cmake从3.16.5版本升级到3.28.2版本，引入了该项变更。

**变更影响**

此变更涉及应用适配。

变更前：

开发者使用默认模板（配置为：cmake\_minimum\_required(VERSION 3.4.1)）时，应用编译构建正常

变更后：

开发者使用默认模板（配置为：cmake\_minimum\_required(VERSION 3.4.1)）时，将出现告警提示，提示内容如下：

```
1. CMake Deprecation Warning at CMakeLists.txt:2 (CMAKE_MINIMUM_REQUIRED):
2. Compatibility with CMake < 3.5 will be removed from a future version of
3. CMake.

5. Update the VERSION argument <min> value or use a ...<max> suffix to tell
6. CMake that the project does not need compatibility with older versions.
```

**该能力起始支持的API Level**

不涉及API

**变更的接口/组件**

不涉及

**适配指导**

修改项目 CMakeLists.txt 中 cmake\_minimum\_required 配置，修改内容如下：

```
1. # the minimum version of CMake.
2. cmake_minimum_required(VERSION 3.4.1)  // 修改为 cmake_minimum_required(VERSION 3.5.0)

4. project(xxx)
5. ...
```

### 应用编译构建harA链接harB的so，导致hap包so冲突

**变更原因**

cmake从3.16.5版本升级到3.28.2版本，引入了该项变更。

**变更影响**

cmake版本升级到3.28.2之后，当某har模块（如harA）的CMakeLists.txt中链接了 ”依赖har模块（如harB）中的so” 时，此so会被打包到harA中，可能导致最终打HAP包时so版本冲突。

**该能力起始支持的API Level**

不涉及API

**变更的接口/组件**

不涉及

**适配指导**

如果so版本冲突，请在工程级或者模块级build-profile.json5文件中buildOption下添加nativeLib/filter/select字段，根据包名、版本、产物名称等，选择打包或排除so文件到HAP产物。具体请参考[关于select的使用](../harmonyos-guides-V5/ide-hvigor-cpp-V5.md#section14491810432)。

```
1. {
2. buildOption:{
3. nativeLib:{
4. filter:{
5. select:[ // select的优先级高于excludes、pickFirsts等配置项
6. {
7. package: "@ohos/curl", // 包名
8. version： "1.3.5", // 包版本
9. include： ["libcurl.so"], // 选择打包的native产物
10. exclude： ["libc++shared.so"], // 排除的native产物
11. },
12. ];
13. }
14. }
15. }
16. }
```

## ArkWeb

### fileAccess接口行为变更

**变更原因**

API version 11及之前，fileAccess为false的时候，应用使用file协议依然可以加载部分可读可写目录，造成注入攻击的安全问题。同时将fileAccess默认值变更为false，提高应用安全性。

**变更影响**

从API version 12开始，fileAccess的默认值变为false，如果应用不手动设置fileAccess属性，则默认ArkWeb不允许file协议的加载，应用只读资源目录/data/storage/el1/bundle/entry/resources/resfile除外。

**该能力起始支持的API Level**

8

**变更的接口/组件**

变更前接口行为

| 名称 | 默认值 | 描述 |
| --- | --- | --- |
| fileAccess | true | 默认允许file协议访问，同时当fileAccess设置为false的时候，应用沙箱路径/data/storage/el2/base和/data/storage/el1/bundle目录下的文件依然可以用file协议访问。 |

变更后接口行为

| 名称 | 默认值 | 描述 |
| --- | --- | --- |
| fileAccess | false | 默认不允许file协议访问，同时当fileAccess设置为false的时候，仅应用沙箱路径/data/storage/el1/bundle/entry/resources/resfile目录下的文件依然可以用file协议访问。 |

**适配指导**

影响应用使用ArkWeb加载本地file协议资源。如果需要使用file协议加载本地资源（以下方法任选其一）：

1.设置fileAccess为true。

2.使用资源拦截的方式加载本地文件，具体参考[解决Web组件本地资源跨域问题](../harmonyos-guides-V5/web-cross-origin-V5.md)。

## ArkData

### Asset属性类型变更

**变更原因**

Asset的属性在HarmonyOS NEXT Developer Beta1阶段增加了undefined类型，破坏了Asset的通用性。

**变更影响**

此变更涉及应用适配。Asset的属性去掉了undefined对类型的支持。

如果已经按照HarmonyOS NEXT Developer Beta1的方法使用了undefined类型，则会由于类型不匹配，导致代码编译失败。

**该能力起始支持的API Level**

11

说明

Asset属性增加undefined类型为HarmonyOS NEXT Developer Beta1阶段引入的行为变更。

**变更的接口/组件**

Asset/数据通用类型（commonType）

**适配指导**

对于已按照HarmonyOS NEXT Developer Beta1版本的方法在Asset属性使用undefined类型的应用工程，必须改为空字符串来解决数据覆盖问题。

对于其他使用Asset属性的应用工程，建议设置空字符串来解决数据覆盖问题。

### setSessionId接口行为变更

**变更原因**

分布式数据对象的同步数据时，会尝试同步与同账号网络中的所有设备建立链接，并进行数据同步。但实际上组网中的其他设备未必创建了分布式数据对象，它们不需要同步数据。所以可能产生无效的数据同步，浪费系统资源。

**变更影响**

此变更涉及应用适配。现在分布式数据对象只会和处于跨端迁移或多端协同的对端设备进行数据同步。未适配跨端迁移或多端协同的应用，使用分布式数据对象，数据不会自动同步。

**该能力起始支持的API Level**

9

**变更的接口/组件**

setSessionId/分布式数据对象（data\_object）

**适配指导**

详见分布式数据对象开发指南中的[在跨端迁移中使用分布式数据对象迁移数据](../harmonyos-guides-V5/data-sync-of-distributed-data-object-V5.md#在跨端迁移中使用分布式数据对象迁移数据)和[在多端协同中使用分布式数据对象](../harmonyos-guides-V5/data-sync-of-distributed-data-object-V5.md#在多端协同中使用分布式数据对象)示例代码。

## ArkGraphics 2D

### OH\_Drawing\_RegisterFont()、OH\_Drawing\_RegisterFontBuffer()接口增加报错码

**变更原因**

OH\_Drawing\_RegisterFont()、OH\_Drawing\_RegisterFontBuffer()接口缺少对文件内容校验的报错。

**变更影响**

此变更涉及应用适配。

1. 变更之前，没有对文件内容进行校验，如果文件损坏，会使用默认字体，并返回成功。
2. 变更之后，增加了对文件内容的校验，如果没有成功创建出字体，则会报出错误码9，即文件损坏。

**该能力起始支持的API Level**

11

**变更的接口/组件**

OH\_Drawing\_RegisterFont()、OH\_Drawing\_RegisterFontBuffer()接口增加报错码：9 文件损坏。

**适配指导**

全局搜索OH\_Drawing\_RegisterFont和OH\_Drawing\_RegisterFontBuffer接口，适配新增的错误码。

## ArkTS

### 编译语法检查场景补齐

**变更原因**

interface的属性名为数字字面量不符合ArkTS语法规则，编译语法检查场景遗漏，需要修复。

**变更影响**

此变更涉及应用适配。

变更前，interface可以声明数字字面量为属性名。

```
1. interface I {
2. one: string,
3. 2: string // no compile-time error
4. }
```

变更后，interface不可以使用数字字面量为属性名。

```
1. interface I {
2. one: string,
3. 2: string // compile-time error
4. }
```

由于class和对象字面量中均不可以使用数字字面量作为属性名，因此如果使用了包含数字字面量作为属性名的interface不会有影响。

只有在声明了这类interface但不使用它们的场景下为涉及适配。

**该能力起始支持的API Level**

ArkTS语法检查从API 10起启用。

**变更的接口/组件**

不涉及。

**适配指导**

建议声明阶段变更数字字面量的属性名为常量字符串或者标识符。具体说明和修改方式请参考[适配指导案例](../harmonyos-guides-V5/typescript-to-arkts-migration-guide-V5.md#对象的属性名必须是合法的标识符)。

### TreeSet.clear()和TreeMap.clear()接口行为变更

**变更原因**

容器类TreeMap和TreeSet的构造函数支持传入比较器，用户可以通过传入比较器来控制元素在二叉树上的插入位置。当用户调用了TreeMap和TreeSet的clear方法时，预期结果为仅清除数据，

实际结果为清除数据的同时还清除了用户传入的比较器，导致再次插入数据时不会遵循用户传入的比较器的规则，而是按照默认比较器的规则，不符合用户预期，需要变更接口行为。

**变更影响**

影响调用clear()后的排序规则。

变更前

* 情况一： 用户传入比较器，调用了TreeMap的clear方法后，比较器失效。

  ```
  1. //使用comparator firstValue > secondValue，表示为降序排序。
  2. let treeMap : TreeMap<string,string> = new TreeMap<string,string>((firstValue: string, secondValue: string) : boolean => {return firstValue > secondValue});
  3. treeMap.set("aa","3");
  4. treeMap.set("dd","1");
  5. treeMap.set("cc","2");
  6. treeMap.set("bb","4");
  7. let numbers = Array.from(treeMap.keys())
  8. for (let item of numbers) {
  9. console.log("treeMap:" + item); // key: dd  cc  bb  aa
  10. }
  11. treeMap.clear();
  12. treeMap.set("aa","3");
  13. treeMap.set("dd","1");
  14. treeMap.set("cc","2");
  15. treeMap.set("bb","4");
  16. numbers = Array.from(treeMap.keys())
  17. for (let item of numbers) {
  18. console.log("treeMap:" + item); //key: aa  bb  cc  dd
  19. }
  ```
* 情况二： 用户传入比较器，调用了TreeSet的clear方法后，比较器失效。

  ```
  1. let treeSet : TreeSet<string> = new TreeSet<string>((firstValue: string, secondValue: string) : boolean => {return firstValue > secondValue});
  2. treeSet.add("a");
  3. treeSet.add("c");
  4. treeSet.add("d");
  5. treeSet.add("b");
  6. let numbers = Array.from(treeSet.values())
  7. for (let item of numbers) {
  8. console.log("TreeSet:" + item); // value: d  c  b  a
  9. }
  10. treeSet.clear();
  11. treeSet.add("a");
  12. treeSet.add("c");
  13. treeSet.add("d");
  14. treeSet.add("b");
  15. numbers = Array.from(treeSet.values())
  16. for (let item of numbers) {
  17. console.log("TreeSet:" + item); // value: a  b  c  d
  18. }
  ```

变更后

* 情况一： 用户传入比较器，调用了TreeMap的clear方法后，比较器正常排序。

  ```
  1. //使用comparator firstValue > secondValue，表示为降序排序。
  2. let treeMap : TreeMap<string,string> = new TreeMap<string,string>((firstValue: string, secondValue: string) : boolean => {return firstValue > secondValue});
  3. treeMap.set("aa","3");
  4. treeMap.set("dd","1");
  5. treeMap.set("cc","2");
  6. treeMap.set("bb","4");
  7. let numbers = Array.from(treeMap.keys())
  8. for (let item of numbers) {
  9. console.log("treeMap:" + item); // treeMap: dd  cc  bb  aa
  10. }
  11. treeMap.clear();
  12. treeMap.set("aa","3");
  13. treeMap.set("dd","1");
  14. treeMap.set("cc","2");
  15. treeMap.set("bb","4");
  16. numbers = Array.from(treeMap.keys())
  17. for (let item of numbers) {
  18. console.log("treeMap:" + item); // treeMap: dd  cc  bb  aa
  19. }
  ```
* 情况二： 用户传入比较器，调用了TreeSet的clear方法后，比较器正常排序。

  ```
  1. let treeSet : TreeSet<string> = new TreeSet<string>((firstValue: string, secondValue: string) : boolean => {return firstValue > secondValue});
  2. treeSet.add("a");
  3. treeSet.add("c");
  4. treeSet.add("d");
  5. treeSet.add("b");
  6. let numbers = Array.from(treeSet.values())
  7. for (let item of numbers) {
  8. console.log("TreeSet:" + item); // TreeSet: d  c  b  a
  9. }
  10. treeSet.clear();
  11. treeSet.add("a");
  12. treeSet.add("c");
  13. treeSet.add("d");
  14. treeSet.add("b");
  15. numbers = Array.from(treeSet.values())
  16. for (let item of numbers) {
  17. console.log("TreeSet:" + item); // TreeSet: d  c  b  a
  18. }
  ```

**该能力起始支持的API Level**

8

**变更的接口/组件**

TreeMap.clear();

TreeSet.clear();

**适配指导**

TreeSet.clear()和TreeMap.clear()方法行为变更之后，用户无需重新设置比较器也能正常排序，也可以重新设置比较器来改变元素的排序方式。

文档可参考如下：

[TreeMap.clear()](../harmonyos-references-V5/js-apis-treemap-V5.md#clear)

[TreeSet.clear()](../harmonyos-references-V5/js-apis-treeset-V5.md#clear)

### TreeMap.setAll()接口行为变更

**变更原因**

使用setAll接口添加一个空的TreeMap，预期长度+0，实际长度+1。

**变更影响**

此变更涉及应用适配，影响调用TreeMap.setAll()后TreeMap的长度。

* **变更前** 使用setAll接口添加treeMap1后treeMap长度为1

```
1. let treeMap : TreeMap<string, number> = new TreeMap();
2. let treeMap1 : TreeMap<string, number> = new TreeMap();
3. treeMap.setAll(treeMap1); // 将treeMap1中的所有元素添加到treeMap中
4. console.info("length:", treeMap.length) // length:1
```

* **变更后** 使用setAll接口添加treeMap1后treeMap长度为0

```
1. let treeMap : TreeMap<string, number> = new TreeMap();
2. let treeMap1 : TreeMap<string, number> = new TreeMap();
3. treeMap.setAll(treeMap1); // 将treeMap1中的所有元素添加到treeMap中
4. console.info("length:",treeMap.length) // length:0
```

**该能力起始支持的API Level**

8

**变更的接口/组件**

TreeMap.setAll();

**适配指导**

对于TreeMap.setAll()传入空TreeMap的情况，开发者需要针对变更前后TreeMap的长度变化进行适配。

文档可参考如下：

[TreeMap.setAll()](../harmonyos-references-V5/js-apis-treemap-V5.md#setall)

### TreeMap、TreeSet的hasKey和has接口行为变更

**变更原因**

1. 对于传入用户自定义比较器的TreeMap， 不能正确区分undefined或null与其他元素的比较关系，导致在没有插入null或undefined的情况下hasKey(null/undefined)错误返回true。
2. 对于传入用户自定义比较器的TreeSet， 不能正确区分undefined或null与其他元素的比较关系，导致在没有插入null或undefined的情况下has(null/undefined)错误返回true。

**变更影响**

影响TreeMap.hasKey()、TreeSet.has()传入undefined或null时的返回值。

* **变更前**
* 情况一： 对于传入用户自定义比较器的TreeMap，在没有插入null或undefined的情况下hasKey(null/undefined)错误返回true。

```
1. let treeMap : TreeMap<string, number> = new TreeMap((firstValue: string, secondValue: string) : boolean => {return firstValue > secondValue});
2. treeMap.set("aa",3);
3. treeMap.set("dd",1);
4. let res = treeMap.hasKey(null);
5. let res1 = treeMap.hasKey(undefined);
6. console.info("res:", res) // res:true
7. console.info("res1:",res1) // res1:true
```

* 情况二： 对于传入用户自定义比较器的TreeSet，在没有插入null或undefined的情况下has(null/undefined)错误返回true。

```
1. let treeSet : TreeSet<string> = new TreeSet<string>((firstValue: string, secondValue: string) : boolean => {return firstValue > secondValue});
2. treeSet.add("a");
3. treeSet.add("c");
4. let res = treeSet.has(null);
5. let res1 = treeSet.has(undefined);
6. console.info("res:", res) // res:true
7. console.info("res1:",res1) // res1:true
```

* **变更后**
* 情况一： 对于传入用户自定义比较器的TreeMap，在没有插入null或undefined的情况下hasKey(null/undefined)返回false。

```
1. let treeMap : TreeMap<string, number> = new TreeMap((firstValue: string, secondValue: string) : boolean => {return firstValue > secondValue});
2. treeMap.set("aa",3);
3. treeMap.set("dd",1);
4. let res = treeMap.hasKey(null);
5. let res1 = treeMap.hasKey(undefined);
6. console.info("res:", res) // res:false
7. console.info("res1:",res1) // res1:false
```

* 情况二： 对于传入用户自定义比较器的TreeSet，在没有插入null或undefined的情况下has(null/undefined)返回false。

```
1. let treeSet : TreeSet<string> = new TreeSet<string>((firstValue: string, secondValue: string) : boolean => {return firstValue > secondValue});
2. treeSet.add("a");
3. treeSet.add("c");
4. let res = treeSet.has(null);
5. let res1 = treeSet.has(undefined);
6. console.info("res:", res) // res:false
7. console.info("res1:",res1) // res1:false
```

**该能力起始支持的API Level**

8

**变更的接口/组件**

TreeMap.hasKey();

TreeSet.has();

**适配指导**

对于TreeMap.hasKey()、TreeSet.has()接口传入null或undefined的情况。开发者需要针对变更前后返回值的变化进行适配。

文档可参考如下：

[TreeMap.hasKey()](../harmonyos-references-V5/js-apis-treemap-V5.md#haskey)

[TreeSet.has()](../harmonyos-references-V5/js-apis-treeset-V5.md#has)

### URLParams类append接口添加的值中包含连续空格时行为变更

**变更原因**

URLParams类append接口添加的字符串中包含连续多个空格时，连续空格会被错误处理成只转换为一个'+'，该实现不符合URL的标准。

**变更影响**

影响URLParams.append()接口在入参包含连续空格时的处理结果。

**该能力起始支持的API Level**

9

**变更的接口/组件**

URLParams对象的append接口。

变更前：URLParams对象使用append()方法添加键值对时，若添加的字符串中存在连续多个空格时，接口表现为将连续多个空格只转换为一个'+'。

```
1. {
2. const objectParams = new url.URLParams("key=abc")
3. console.log(objectParams.toString())  // "key=abc"
4. objectParams.append('key1', 'd   e   f');
5. console.log(objectParams.toString())  // "key=abc&key1=d+e+f"
6. }
```

变更后：URLParams对象使用append()方法添加键值对时，若添加的字符串中存在连续多个空格时，接口表现为将连续多个空格转换为对应空格数量的'+'。

```
1. {
2. const objectParams = new url.URLParams("key=abc")
3. console.log(objectParams.toString())  // "key=abc"
4. objectParams.append('key1', 'd   e   f');
5. console.log(objectParams.toString())  // "key=abc&key1=d+++e+++f"
6. }
```

**适配指导**

开发者在涉及上面append的使用场景时，在变更生效前如果对append添加的键值对做后续处理操作，变更后需针对不同表现做针对性适配。

### URLParams类在入参字符串中包含大小写不同编码值时，toString()接口表现结果不一致变更

**变更原因**

URLParams类在入参字符串中包含大小写不同编码值时toString()接口返回值有误，主要涉及："%2b"和"%2B"的表现不一致，"%2B"被处理为"%2B"是符合标准的，但"%2b"会被错误处理成'+'。

**变更影响**

影响当URLParams构造函数入参字符串中存在"%2b"时URLParams.toString()的返回结果。

**该能力起始支持的API Level**

9

**变更的接口/组件**

URL模块URLParams类toString接口，

变更前：创建URLParams对象，如果入参字符串中存在"%2b"和"%2B"时，在toString()后返回的字符串分别表现为"+"和"%2B"。

```
1. {
2. const objectParams = new url.URLParams("key%2b=abc%2B")
3. console.log(objectParams.toString())  // "key+=abc%2B"
4. }
```

变更后：创建URLParams对象，如果入参字符串中存在"%2b"和"%2B"时，在toString()后返回的字符串均表现为"%2B";

```
1. {
2. const objectParams = new url.URLParams("key%2b=abc%2B")
3. console.log(objectParams.toString())  // "key%2B=abc%2B"
4. }
```

**适配指导**

开发者在涉及上述使用场景时，在变更生效前如果对toString()返回值做后续处理操作，变更后需针对表现不同做针对性适配。

### URLParams类append接口行为变更

**变更原因**

URLParams使用append()方法时，对入参键值对中的特殊字符会错误进行encode，该行为与URL标准不一致，导致后续对键值对进行增删改查等操作出现异常。

**变更影响**

影响当URLParams.append()入参包含中文等特殊字符时该函数的处理结果。

**该能力起始支持的API Level**

9

**变更的接口/组件**

URLParams类append接口。

变更前：URLParams使用append()方法添加键值对, 若想通过添加的key使用get、has、delete、set接口进行增删改查操作，需先对key进行额外encode。

```
1. {
2. const objectParams = new url.URLParams('?fod=1&bard=2')
3. objectParams.append("key&大", "abc");
4. objectParams.has('key&大');  // false
5. objectParams.has('%E5%A4%A7');  // true
6. objectParams.get('key&大');  // undefined
7. objectParams.get('%E5%A4%A7');  // abc
8. }
```

变更后: URLParams使用append()方法添加键值对,可直接使用添加的key拿到对应value进行增删改查操作。

```
1. {
2. const objectParams = new url.URLParams('?fod=1&bard=2')
3. objectParams.append("key&大", "abc");
4. objectParams.has('key&大');  // true
5. objectParams.has('%E5%A4%A7');  // false
6. objectParams.get('key&大');  // abc
7. objectParams.get('%E5%A4%A7');  // undefined
8. }
```

**适配指导**

对于URLParams.append()入参包含中文等特殊字符的情况。开发者需要针对变更前后调用has()、get()、delete()、set()传入这些字符时处理结果及返回值的变化进行适配。

## ArkUI

### @Component和@ComponentV2修饰的自定义组件使用@Observed或者@ObservedV2修饰的类增加相关校验

**变更原因**

此变更涉及应用适配。

1. 在@Component修饰的自定义组件中通过@State、@Prop、@Link、@Provide、@Consume、@StorageLink、@StorageProp、LocalStorageLink、@LocalStorageProp修饰并使用@ObservedV2修饰的变量类型时，进行校验并输出错误信息。

   简化示例如下：

   ```
   1. @ObservedV2
   2. class TmpA{}

   4. @Entry
   5. @Component
   6. struct testTmp {
   7. @State value_string: TmpA = new TmpA()
   8. build() {
   9. Column(){

   11. }
   12. }
   13. }
   ```
2. 在@ComponentV2修饰的自定义组件中通过@Param、@Local、@Event、@Provider()、@Consumer()修饰并使用@Observed修饰的类时，进行校验并输出错误信息。

   简化示例如下：

   ```
   1. @Observed
   2. class TmpA{}

   4. @Entry
   5. @ComponentV2
   6. struct testTmp {
   7. @Param value_string: TmpA = new TmpA()
   8. build() {
   9. Column(){

   11. }
   12. }
   13. }
   ```
3. 以上的变量类型联合使用时，也会进行校验并输出错误信息。

   示例如下：

   ```
   1. @ObservedV2
   2. class TmpA{}

   4. @Observed
   5. class TmpB{}

   7. @Entry
   8. @Component
   9. struct testTmp {
   10. @State value_string: TmpA | TmpB = new TmpA()
   11. build() {
   12. Column(){

   14. }
   15. }
   16. }
   ```

**变更影响**

变更前无报错。

变更后报错：

1. The type of the @State property can not be a class decorated with @ObservedV2.
2. The type of the @Param property can not be a class decorated with @Observed.
3. The type of the @State property can not be a class decorated with @ObservedV2.

**该能力起始支持的API Level**

不涉及API变更

**适配指导**

如果开发者不按规范使用对应范式，则需按日志提示信息进行修改。

### TextTimer的onTimer回调频率与参数单位调整

**变更原因**

调整onTimer回调频率与参数的单位，使其符合文档描述。

**变更影响**

此变更涉及应用适配。

TextTimer的format属性用于自定义时间格式。其中，毫秒可使用S、SS和SSS关键字表示，分别代表100ms、10ms和1ms。

变更前，当TextTimer的format属性包含毫秒时，TextTimer的文本发生变化，便会几毫秒触发一次onTimer事件，且回调参数utc和elapsedTime的单位为毫秒。

变更后，TextTimer的文本发生变化时，onTimer事件的触发时间与回调参数utc和elapsedTime的单位随format属性的自定义时间格式变化。format为mm:ss.S时，100ms回调一次onTimer事件，回调参数的单位为100ms。format为mm:ss.SS时，10ms回调一次onTimer事件，回调参数的单位为10ms。format为mm:ss.SSS时，与变更前保持一致。

**该能力起始支持的API Level**

11

**变更的接口/组件**

textTimer组件的onTimer接口

**适配指导**

需要开发者主动适配，调整回调参数的数量级。

```
1. @Entry
2. @Component
3. struct TextTimerExample {
4. textTimerController: TextTimerController = new TextTimerController();
5. build() {
6. Column(){
7. TextTimer({isCountDown: true, count: 30000, controller: this.textTimerController})
8. .format('mm:ss.SS')
9. .fontSize(50)
10. .onTimer((utc: number, elapsedTime: number) => {
11. // 如果开发者需改回变更前的效果，可以将utc、elapsedTime乘10
12. console.info('textTimer countDown utc is:' + utc * 10 + ',elapsedTime is:' + elapsedTime * 10)
13. })

15. TextTimer({isCountDown: true, count: 30000, controller: this.textTimerController})
16. .format('mm:ss.S')
17. .fontSize(50)
18. .onTimer((utc: number, elapsedTime: number) => {
19. // 如果开发者需改回变更前的效果，可以将utc、elapsedTime乘100
20. console.info('textTimer countDown utc is:' + utc * 100 + ',elapsedTime is:' + elapsedTime * 100)
21. })
22. }
23. }
24. }
```

### RichEditor组件builderSpan支持绑定自定义菜单

**变更原因**

富文本支持builderSpan绑定自定义菜单。

**变更影响**

此变更涉及应用适配。

变更前：右击或长按builderSpan会弹出对RichEditorSpanType.IMAGE类型绑定的自定义菜单。

变更后：新增自定义菜单绑定类型RichEditorSpanType.BUILDER，builderSpan和imageSpan分开绑定和弹出自定义菜单。右击或长按builderSpan不再弹出对RichEditorSpanType.IMAGE类型绑定的自定义菜单，而是弹出对RichEditorSpanType.BUILDER类型绑定的自定义菜单。

**该能力起始支持的API Level**

10

**变更的接口/组件**

RichEditor组件的RichEditorSpanType接口。

**适配指导**

若开发者需要右击或长按builderSpan时弹出RichEditorSpanType.IMAGE类型的自定义菜单，需要对该自定义菜单绑定RichEditorSpanType.BUILDER类型。

```
1. @Entry
2. @Component
3. struct Example {
4. @Builder
5. menu() {
6. Column() {
7. Text("自定义菜单");
8. }
9. }
10. build() {
11. Column() {
12. RichEditor({controller: new RichEditorController()})
13. // 变更前
14. .bindSelectionMenu(RichEditorSpanType.IMAGE, this.menu(), ResponseType.LongPress)

16. // 变更后
17. .bindSelectionMenu(RichEditorSpanType.IMAGE, this.menu(), ResponseType.LongPress)
18. // 绑定RichEditorSpanType.BUILDER类型
19. .bindSelectionMenu(RichEditorSpanType.BUILDER, this.menu(), ResponseType.LongPress)
20. }
21. }
22. }
```

### RichEditor的lineHeight、letterSpacing、lineSpacing属性返回值单位变更

**变更原因**

文本字体相关属性的返回值单位应默认使用fp类型。

**变更影响**

此变更涉及应用适配。

API version 11及以前：lineHeight、letterSpacing、 lineSpacing属性的返回值单位是vp。

API version 12及以后：lineHeight、letterSpacing、 lineSpacing属性的返回值单位从vp变更为fp，若开发者原来将返回值按vp单位处理，变更后该处理逻辑会导致数据错误。

**该能力起始支持的API Level**

10

**变更的接口/组件**

RichEditor组件，lineHeight、letterSpacing、lineSpacing属性。

**适配指导**

默认返回值变更，开发者需通过[像素单位转换接口](../harmonyos-references-V5/ts-pixel-units-V5.md#像素单位转换)，对返回值进行正确处理。

### RichEditor的fontSize属性的返回值单位变更

**变更原因**

文本字体相关属性的返回值单位应默认使用fp类型。

**变更影响**

此变更涉及应用适配。

API version 11及以前：fontSize属性的返回值单位是vp。

API version 12及以后：fontSize属性的返回值单位从vp变更为fp，若开发者原来将返回值按vp单位处理，变更后该处理逻辑会导致数据错误。

**该能力起始支持的API Level**

10

**变更的接口/组件**

RichEditor组件，fontSize属性。

**适配指导**

默认返回值变更，开发者需通过[像素单位转换接口](../harmonyos-references-V5/ts-pixel-units-V5.md#像素单位转换)，对返回值进行正确处理。

### 文本计算接口fontSize参数默认单位实现修正

**变更原因**

fontSize参数在文档描述中number类型默认单位是fp，实际实现是vp。

**变更影响**

系统设置显示和亮度下字体大小使用标准字体，变更前后文本计算接口返回结果相同。

系统设置显示和亮度下字体大小使用特大字体，此变更涉及应用适配。

变更前：measureText接口的fontSize参数传入number类型数值，获取到的文本计算宽度小于实际文本显示所需宽度。

变更后：measureText接口的fontSize参数传入number类型数值，获取到的文本计算宽度等于实际文本显示所需宽度。

**该能力起始支持的API Level**

measureText:9，measureTextSize:10

**变更的接口/组件**

measureText和measureTextSize接口。

**适配指导**

若在Text组件上，fontSize设置的是vp类型字号，则在measureText测算接口将fontSize的number类型参数改为string类型，传入vp类型字号参数。

```
1. import { MeasureText } from '@kit.ArkUI'

3. @Entry
4. @Component
5. struct Index {
6. @State text: string = "Hello world"
7. //变更前
8. @State textWidth: number = MeasureText.measureText({
9. textContent: this.text,
10. fontSize: 24
11. })
12. //变更后
13. @State textWidth2: number = MeasureText.measureText({
14. textContent: this.text,
15. fontSize: '24vp'
16. })

18. build() {
19. Row() {
20. Column() {
21. //被计算文本
22. Text(this.text).fontSize('24vp')
23. Text(`The width of '24vp Hello World': ${this.textWidth}`)
24. Text(`The another width of '24vp Hello World': ${this.textWidth2}`)
25. }
26. .width('100%')
27. }
28. .height('100%')
29. }
30. }
```

若在Text组件上，fontSize设置的是fp类型字号则无需适配，测算接口fontSize参数传入number类型数值和Text组件上使用的字号单位是一致的。

## Media Library Kit

### @ohos.multimedia.medialibrary变更

**变更原因**

根据工信部关于应用软件调用行为记录能力要求，需要进行媒体库接口能力变更。

**变更影响**

此变更涉及应用适配。

@ohos.multimedia.medialibrary模块中的所有接口将从SDK中删除，不再支持新开发应用使用，历史代码工程编译报错。

针对已上架的应用，medialibrary接口原本的功能无法正常使用，调用接口会抛出错误码8000001。

**该能力起始支持的API Level**

6

**变更的接口/组件**

@ohos.multimedia.medialibrary模块中的所有接口。

**适配指导**

开发者需停止使用@ohos.multimedia.medialibrary模块，并使用@ohos.file.photoAccessHelper模块替代实现相关功能。

新接口使用指南请参考[Media Library Kit使用指导](../harmonyos-guides-V5/photoaccesshelper-overview-V5.md)。

## 公共能力

### 开发态下代码签名强制管控策略变更

**变更原因**

为统一底层代码签名管控逻辑，降低鸿蒙系统被攻击的安全风险，所有运行在设备端的应用代码都需要包含合法签名。应用进程加载代码时，系统会检查对应文件签名的合法性。禁止未签名及签名不合法的代码在设备上运行。

**变更影响**

此变更涉及应用适配。

**变更前**

在开发者模式下，设备上允许运行未包含合法代码签名的调试应用代码。

**变更后**

1. 开发者尝试在设备上运行未包含合法代码签名的调试应用代码，会被系统拦截。
2. 开发者直接推送到设备端的代码文件，未走包安装流程，会因为缺乏签名，而被系统拦截。

**该能力起始支持的API Level**

不涉及API

**变更的接口/组件**

不涉及

**适配指导**

1. 开发者需要从华为申请合法的开发者调试证书，并使用ROM配套的IDE（DevEco Studio 5.0.3.424及以上）对打包后的调试应用包做签名操作。
2. 二进制代码（如bin及so库文件）需打包在鸿蒙支持的应用包内（如HAP、 HSP和HQF）做代码签名，然后走包安装流程，否则会因为缺乏签名而被系统拦截。

开发者可以按[应用/服务签名指导](../harmonyos-guides-V5/ide-signing-V5.md)对应用进行签名。
