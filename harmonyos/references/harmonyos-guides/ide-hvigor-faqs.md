---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-faqs
title: 编译构建常见问题
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 构建报错排查 > 编译构建常见问题
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:0b0d9fae21af13b83a5acfc363058903110496166c1a65e3fdeb11546731c347
---

## 如何解决编译过程内存过高

**问题现象**

编译构建时，内存或CPU占用过高，导致出现DevEco Studio运行卡顿、延迟等现象。

**解决措施**

* 在执行hvigor构建的过程中，通过减少内存中的缓存数据、减少线程数量，可以减少编译过程中的内存占用。

  可以在hvigor-config.json5中添加配置。

  ```json5
  "properties": {
    // 配置为0，表示不启用内存缓存配置，默认为4，数值越低，内存中缓存数据越少
    "hvigor.pool.cache.capacity": 0,
    // 默认配置为cpu核数-1， 包含ohos.arkCompile.maxSize，值越小，占用内存越少
    "hvigor.pool.maxSize" : 5,
    // 默认配置值为5, 值越小，占用内存越少
    "ohos.arkCompile.maxSize": 3,
    // 默认配置值为true, 表示开启内存缓存，占用内存较多，配置为false，关闭内存缓存，占用内存较少
    "hvigor.enableMemoryCache": false
  },
  ```

  **说明** 

  当配置项"hvigor.pool.maxSize"和"ohos.arkCompile.maxSize"的值改小，"hvigor.enableMemoryCache"改为false后，可能会导致编译时长增加，请耐心等待。

* 如果以上修改没有取得明显的效果，可以使用非并行的模式来执行编译。
  + 在菜单栏点击“File > Settings（macOS为DevEco Studio > Preferences/Settings） > Build, Execution, Deployment > Build Tools > Hvigor”，取消勾选“Execute tasks in parallel mode (may require larger heap size)”。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/frT-wpR3R6uNEx4EP-dIcA/zh-cn_image_0000002808766841.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=ECBDE7D08F8ED46A16EC4FF3AEE94FD9157CAE418C6E967FE5BBA41ED5DDA262)
  + 流水线场景中，在命令行最后增加 --no-parallel，示例：

    ```bash
    hvigorw assembleHap --no-parallel
    ```

  **说明** 

  使用非并行模式编译，内存占用会减少，但可能会导致编译时长增加，请耐心等待。

## 构建报错“Cannot read properties of undefined(reading 'XXX')”

请先根据XXX的值从以下场景排查，没解决问题再参考最终方案。

* **场景一：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'setEnabled')”。

  **问题确认**

  hvigorfile.ts里有如下代码：

  ```ts
  import { hvigor, getHvigorNode } from "@ohos/hvigor"
  import { hapTasks} from '@ohos/hvigor-ohos-plugin';
  // 问题代码
  getHvigorNode(__filename).getTaskByName('XXX').setEnabled(false);
  export default {
      system: hapTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
      plugins: []         /* Custom plugin to extend the functionality of Hvigor. */
  }
  ```

  **处理措施**

  1. 确保XXX是当前的HvigorNode里存在的任务。

     假设是entry模块的hvigorfile.ts中的代码导致的问题，XXX的有效值就是下图中的“default@SignHap”、“default@CollectDebugSymbol”、“assembleHap”等值。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/idB_L8ODSMCAkwSGdeRuuQ/zh-cn_image_0000002808766873.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=76ED3C7C3F2B6BF3B897BFDF567AB7472F302E82F779E2044F95929E678B957D)
  2. 确保getTaskByName的使用位置是在[Hvigor的配置阶段](ide-hvigor-life-cycle.md#section746253616316)及之后的生命周期里，包括beforeNodeEvaluate、afterNodeEvaluate、nodesEvaluated、taskGraphResolved、buildFinished。
* **场景二：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'isSO')”。

  **处理措施**

  升级到DevEco Studio 5.1.0.840及以上的版本。
* **场景三：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'getPluginId')”**。**

  **处理措施**

  确保hvigorfile.ts里export default的对象中的字段system的值是appTasks/hapTasks/hspTasks/harTasks之一。

  ```ts
  import { appTasks } from '@ohos/hvigor-ohos-plugin';

  export default {
      system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
      plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
  }
  ```
* **场景四：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'getNeedExecTargetServiceList')”**。**

  **处理措施**

  确保模块下的module.json5的type字段的值和hvigorfile.ts中export default的对象的system字段符合以下对应关系：

  **表1**

  | module.json5的type字段 | hvigorfile.ts中export default的对象的system字段 |
  | --- | --- |
  | entry | hapTasks |
  | feature | hapTasks |
  | shared | hspTasks |
  | har | harTasks |
* **场景五：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'app')”。

  **处理措施**

  确保工程目录下AppScope/app.json5文件存在。
* **场景六：**

  **问题现象**

  Linux环境下，执行单元测试，出现报错“Cannot read properties of undefined(reading 'toString')”。

  **处理措施**

  Linux环境暂不支持单元测试。
* **场景七：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'kind')”。

  **处理措施**

  检查ArkTS代码是否有如下写法：

  ```ts
  // 错误写法：空数组
  class w {
    public a: [][] = []
    test() {
      console.log("1", this.a[0])
    }
  }
  // 正确写法
  class w {
    public a: string[][] = []
    test() {
      console.log("1", this.a[0])
    }
  }
  ```
* **场景八：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'clear')”。

  **问题确认**

  在工程根目录hvigor/hvigor-config.json5文件中配置如下内容打开堆栈。

  ```json5
  "debugging": {
    "stacktrace": true                /* Disable stacktrace compilation. Value: [ true | false ]. Default: false */
  },
  ```

  确认堆栈内容是否如下。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/WyEPOoeIS6qMq-Rm1HVjww/zh-cn_image_0000002808886935.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FF15706BA6EE4A5AAA66BF5F8D5C08DF4DAA9E036860CD4AF08329DA8AD33DC)

  **处理措施**

  确认DevEco Studio是否有使用安全加固等三方插件。如果有，可以先禁用三方插件，看是否会复现问题，还能复现就参考下面的最终方案。
* **最终方案：**

  如果以上场景都不符合，打开堆栈后，根据堆栈信息排查代码。

  堆栈打开方法：工程根目录hvigor/hvigor-config.json5文件中配置如下内容。

  ```json5
  "debugging": {
    "stacktrace": true                /* Disable stacktrace compilation. Value: [ true | false ]. Default: false */
  },
  ```

  优先排查hvigorconfig.ts文件和hvigorfile.ts文件，其他代码次之。

  如果上述文件中并未排查出问题，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 构建报错“Duplicated files found in module xxx. This may cause unexpected errors at runtime”

**问题现象**

编译构建时，出现报错“Duplicated files found in module xxx. This may cause unexpected errors at runtime”。

问题原因是构建时存在不同版本的同名so文件。比如将har模块产物里的so文件拷贝到entry模块的libs目录下，这时har模块里有一个libhar.so，entry模块里也有一个libhar.so，再配置entry依赖har，构建entry就会出现报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/7FB4SzkWTt2wLkV_YPFrHQ/zh-cn_image_0000002779567282.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B5C471EB1A17EC84EB0A537D8BB23428BDE8A88188925A1C09811CA87F5FB7FA)

**解决措施**

使用select、pickFirsts、pickLasts等配置选中要使用的so文件，select提供native产物的精准选择能力，优先级高于excludes、pickFirsts等配置项。pickFirsts、pickLasts按照.so文件的优先级顺序，打包最高优先级的.so文件，优先级顺序是指依赖收集的顺序，越晚被收集优先级越高。

具体可参考：[配置CPP](ide-hvigor-cpp.md)。

基于上面的例子，可以在entry的build-profile.json5中添加配置select选中har模块中的so文件，package选中包名为“har”的模块, include选中“libhar.so”文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/i-zRf60uROiZFXWtFPKmbA/zh-cn_image_0000002779407286.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=69B91ED4A55AA563B0F42E43018E42ACE06BA4C2AA16C5D177E5F0912476F93D)

## Linux环境下编译报错“JS heap out of memory”

**问题现象**

在Linux环境下，系统内存有64G，Hvigorw脚本中配置--max-old-space-size=40960，在编译构建时，实际在使用内存未达到配置的内存（例如使用到20G左右）就出现报错“JS heap out of memory”。

```txt
FATAL ERROR: NewSpace::Rebalance Allocation failed - JavaScript heap out of memory
Writing Node.js report to file: report.20200512.172528.47517.24.011.json
Node.js report completed
1: 0xa295e0 node::Abort() [node]
2: 0x9782df node::FatalError(char const*, char const*) [node]
3: 0xb99c2e v8::Utils::ReportOOMFailure(v8::internal::Isolate*, char const*, bool) [node]
4: 0xb99fa7 v8::internal::V8::FatalProcessOutOfMemory(v8::internal::Isolate*, char const*, bool) [node]
5: 0xd3a3b5 [node]
6: 0xd74f27 [node]
7: 0xd84707 v8::internal::MarkCompactCollector::CollectGarbage() [node]
8: 0xd481b9 v8::internal::Heap::MarkCompact() [node]
9: 0xd48f0b v8::internal::Heap::PerformGarbageCollection(v8::internal::GarbageCollector, v8::GCCallbackFlags) [node]
10: 0xd499a5 v8::internal::Heap::CollectGarbage(v8::internal::AllocationSpace, v8::internal::GarbageCollectionReason, v8::GCCallbackFlags) [node]
11: 0xd4aebf v8::internal::Heap::HandleGCRequest() [node]
12: 0xcf5f97 v8::internal::StackGuard::HandleInterrupts() [node]
13: 0x104b803 v8::internal::Runtime_StackGuard(int, unsigned long*, v8::internal::Isolate*) [node]
14: 0x13a5a99 [node]
Aborted (core dumped)
```

**问题原因**

vm.max\_map\_count是一个与内核虚拟内存子系统相关的参数，用于控制进程可以拥有的内存映射区域的最大数量。它通常用于限制一个进程可以打开的文件数量，特别是在使用大量内存映射文件的情况下。

在Linux系统上，vm.max\_map\_count参数的默认值通常是较小的数值，例如65530。然而，对于一些需要大量内存映射的应用程序或者特定的使用场景，可能需要增加该参数的值，以便支持更多的内存映射区域。

**解决措施**

修改vm.max\_map\_count的值：

* 临时修改：

  ```bash
  sysctl -w vm.max_map_count=新值
  ```
* 永久修改：如果希望永久修改参数的值，可以编辑/etc/sysctl.conf文件，并添加或修改以下行：

  ```bash
  vm.max_map_count=新值
  ```

  保存文件后，使用以下命令使更改生效：

  ```bash
  sysctl -p
  ```

## 编译报错“Cannot find module XXX or its corresponding type declarations”

* **场景一：**

  **问题现象**

  Stage模板工程编译引用native文件（.so）提示“Cannot find module XXX or its corresponding type declarations.”。

  **处理措施**

  当前Stage工程在编译构建阶段新增对native文件（.so）导出符号的语法校验，如果引用了没有对应声明文件（.d.ts）的native文件（.so）的现有工程在编译构建阶段，语法校验工具便会报错提示找不到对应的声明文件。

  如果出现类似问题，可尝试通过如下方式进行解决：

  1. 在对应cpp目录下新建types/libxxx目录，并在该目录下新增index.d.ts用于声明native的类型符号；新增oh-package.json5配置文件用于校验工具的模块查询。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/ei1pACnTSsKA0cPegMrcDQ/zh-cn_image_0000002779567288.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD31BDDD71A61A82F9A162A0C70A72533018BE17195D90BB9AD24468F0AC4DAD)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/e6x8WD6bQkuLxq6LqlMXMg/zh-cn_image_0000002808766859.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F7FD5EEAD813B71A748136E7F359B24E1C8A8BFDF5C0891A721D18B3F307064)
  2. 在native引用的模块内的oh-package.json5中添加native模块的本地依赖，并根据提示点击**Sync Now**同步工程，下图以entry模块引用native模块为例。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/TTx264hbQyShkYgHeNUrMA/zh-cn_image_0000002779407268.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=33D8B174CF4C4D5729A7C76EEF22302BBF4353AAADE660499FA04E774A4B2F61)

* 场景二：

  **问题现象**

  引用三方包，构建失败，提示“Cannot find module 'xxx' or its corresponding type declarations”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/LLaSKvKKTHK3MnRUxdmoJg/zh-cn_image_0000002779567284.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF500D5BE0D5CACF938780B7C92828C6F060509BDFDC2ECA6BD4E0E6AD11141E)

  **处理措施**

  进入对应模块级oh-package.json5文件或工程级oh-package.json5文件中查看三方包是否已安装，若未安装，需执行ohpm install安装；若已安装，需查看“main”字段是否配置正确，若未配置或配置错误，需配置为正确的入口文件。
* 场景三：

  **问题现象**

  引用的包路径被混淆，代码中又是在引用包后面拼接了路径，导致模块引用不到而报错。

  例如：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/17b1AV0QRHuquyMjaZKxPw/zh-cn_image_0000002808886937.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=2437A6A7523619A3733EF40CD4CF5CEBE0EC648A69E0BD55FD2547A930E26CC9)

  代码中这样引用会找不到模块，导致报错。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/7CHkdp2YTWmJdVvelHfnMg/zh-cn_image_0000002779407298.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E4692CD32665148752C3B58C028CBD54D493F2360CEDC6B30C8529CFF3D7911)

  **处理措施**

  修改引用方式，改为推荐的引用方式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/f5tbu9w_RjGzqfLY--GMqQ/zh-cn_image_0000002808766829.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF56FC4CC6AD934C68BE3CCD682C1669F1BABE02863B5A20962DF249455D3189)
* 场景四：

  **问题现象**

  被引用模块oh\_package.json5配置有误，执行了ohpm install 并且成功地安装了依赖，但是还报错模块找不到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/7hVxQamCTFCGDY_rrZKpDQ/zh-cn_image_0000002808886919.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B1C4A19B7CF45C3E072EDE112BAD001A28C6FA7A899174672976B9C8D9BB114)

  被引用模块的oh\_package.json5中配置了错误的types字段。

  该字段优先于main字段。如果types字段配置的不存在，就会报错模块找不到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/KfniTwWUR1Sgf7fqdXjrdA/zh-cn_image_0000002808886947.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A358EED5A93E43559DEDDC398505BEF8C5407BEEF1358082E21B9536B80FED27)

  **处理措施**

  如果该包中没有d.ets声明，则这个字段可以删除。配置不存在或者错误，会导致报错。
* 场景五：

  **问题现象**

  oh\_package.json5中dependencies中引入模块的名称和实际使用时import的不一致。

  例如在oh\_package.json5中这样引入：

  ```json5
  "dependencies": {   "har": "file:../har" }
  ```

  但是实际上在代码中import的时候是大写HAR或者其他，而不是dependencies里面配置的‘har’的值，要注意保持完全一致。

  **处理措施**

  引入和使用改成一致。
* 场景六：

  **问题现象**

  引用模块的oh\_package.json5中main字段值和实际的文件名称大小写不一致。

  **处理措施**

  将main字段和实际文件名称的大小写改为一致。
* 场景七：

  **问题现象**

  Stage模板工程编译构建失败，提示“Cannot find module '@bundle:rollup\_plugin\_ignore\_empty\_module\_placeholder' or its corresponding type declarations”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/Pgnpy0DMSqumadYkqWksAA/zh-cn_image_0000002808766867.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3609666EF9A67EC5C5499CF6DAFDFEB35B5DC9C1B57C9B756887B79D3A001A5B)

  **解决措施**

  该问题是由于工程引用了无对应实现文件的.d.ts声明文件：

  1. 通过在build目录中搜索'rollup\_plugin\_ignore\_empty\_module\_placeholder'，找到报错的中间文件，并根据中间文件找到对应工程文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/tB0SixWjTcS9B555x6RYUg/zh-cn_image_0000002779567256.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF636B5108F3FAD8BF959E146CCAA483C5AA7E5FCC3C195117CFB46031F3FBAA)

     在输入栏中输入rollup\_plugin\_ignore\_empty\_module\_placeholder，找到问题模块的中间文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/u7_uIR4DQ_m0qJepZ4uEOA/zh-cn_image_0000002808886953.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=DAC57B564663A3167123FAAAD68E1AA3922A7B49CC10DBD8A3B55BD4FA588DCD)
  2. 在引用类型文件中通过添加type显式声明符号类型引用：

     ```ts
     export type {T} from './type';
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/445vcFVIRRSfLPHYJ-hFzQ/zh-cn_image_0000002779567286.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=749593891CC6F8A606F8C9E99300420276BD7F7295920F209F62A41E6CA568FE)
  3. 同时排查是否从d.ts/d.ets中引用值类型符号，禁止在声明文件中声明值变量。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/KqSkwfubToWtxpFvy_NnLg/zh-cn_image_0000002808886921.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF10C972FE10AE70DD6A100358699DACC19F89EB38589079AF48A7425F540CBB)

## 编译报错“Failed to get a resolved OhmUrl by filepath xx”

* **场景一：**

  **问题现象**

  三方包在配置依赖时，配置到devDependencies，源码中又有引用依赖中的API时，编译失败。如以下示例：三方包@hms-security/ucs-appauth将依赖@network/gr配置在devDependencies中，源码中使用了@network/grs的API时，编译失败，提示“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/m8PipOF7QuC28LD3QEG75g/zh-cn_image_0000002808886925.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD4B1931BE60BBB8B8A0420864C0AE996C192B3498506F5F7EED281F121A468B)

  **问题确认**
  1. 进入上面报黄色的源码文件中，可以看到依赖有红色告警信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/rhR2j5gcQcajpw-EDMCz5g/zh-cn_image_0000002779567262.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA0F5AA3D0CAE54DD439ADEFD8664B84ECC906941C183A1C2BDBC2FCBC3326EF "点击放大")
  2. 进入包下的oh-package.json5文件，查看依赖配置为devDependencies。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/Kt2M3CIQQimTKXfbgEtWUQ/zh-cn_image_0000002779407308.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DD64F9ECEFED6CE6E1CE51D956A81A5CC1121C84FCE6D6B428BB059757BE92E)

  **处理措施**
  + 向此包开发团队提改进建议：运行时的依赖，不能配置在devDependencies中。
  + 可在依赖上层引入对应devDependencies中的三方包规避此问题。

* **场景二：**

  **问题现象**

  DevEco Studio编译失败，提示“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/bkEuQSWOR7a0hUscwvlKqw/zh-cn_image_0000002808766835.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C79665BD487AE5704C81A591EDF9277ED2CCA34E5AABAAA0A851B85E1EF6656D)

  **问题确认**

  查看工程目录下的build-profile.json5文件中modules字段配置的srcPath路径是否与真实路径不相同，是否存在大小写不一致问题。

  **处理措施**

  将工程目录下的build-profile.json5文件中modules字段配置的srcPath路径与真实路径保持一致。
* **场景三：**

  **问题现象**

  工程A以相对路径引用了工程B的模块，这种引用会导致报错。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/Vm7O4a7vTXSs-YNnU5VaOg/zh-cn_image_0000002808766839.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF48B3B85098A4DD2E062C960E0F5E6A391357070C1DB0AB321E6D98951258C1)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/CDv1Ist_Rxa3QMGPMbSOgA/zh-cn_image_0000002808886913.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=634FB9193F5D470E29F20FED35E9F22119E10BE9F6CBAE0A7019362C6EC14C4D)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/GHJ4_ikFRSmLJ21rRJ8vfQ/zh-cn_image_0000002808886951.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1122C3D948C754DF1BA4D9B4E5019B4E0BAB3FA450B86518EE071CEF09B01F9D)**处理措施**

  + 把工程B这种的har转至工程A里，作为A的一个模块引用。
  + 把工程B的har提前打包，在A中以.har的方式引用。
  + 上传到仓库，以版本号的方式引用。
* **场景四：**

  **问题现象**

  DevEco Studio编译失败，提示“Error Message: Failed to get a resolved OhmUrl for 'hvigor\_ignore\_xxxxx' imported by xxx”。

  **处理措施**

  如果hvigor\_ignore\_xxxxx所在的模块是har模块，需排查oh\_package.json5中是否存在"packageType": "InterfaceHar"，若存在则删除。
* **场景五：**

  **问题现象**

  DevEco Studio编译失败，提示“Failed to get a resolved OhmUrl for 'xxx' imported by 'yyy'”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/GCM97ZjgSaS8y_1WmNkI7w/zh-cn_image_0000002779567250.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA5D114CB416933CC8DAA36DC92B3895F918EF47F6D576175C9AA6A0DCF859DB "点击放大")

  **问题确认**

  1. 排查yyy所在模块是否为[字节码har](ide-hvigor-build-har.md#section16598338112415)，查看工程级build-profile.json5的useNormalizedOHMUrl是否为true（缺省默认值为false），如果为true则默认构建字节码har。
  2. 如果yyy所在模块是字节码har，请排查xxx依赖是否被配置在工程级oh\_package.json5的dependencies，但没有配置在yyy模块级oh\_package.json5的dependencies中。

  **处理措施**

  + 将xxx依赖配置到yyy模块oh\_package.json5的dependencies中。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/fSECfAoeTwOM1wdCwrMO3Q/zh-cn_image_0000002808766871.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=557E013762897B37936050E938E4ED7AD944E3ACBF16C953178F6F8F54A0BED9 "点击放大")
  + 将yyy模块改为非字节码har，在模块级build-profile.json5文件中添加byteCodeHar字段并设置为false。

    ```json5
    "buildOption": { 
      "arkOptions": { 
        "byteCodeHar": false
      }
    }
    ```
* **场景六：**

  请确认当前使用的DevEco Studio和SDK版本是配套的，点击菜单栏**Help > About DevEco Studio**，**Help > About HarmonyOS SDK**分别查看配套的DevEco Studio和SDK版本。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/s__gzR7pT7-qENLq-ZjY5g/zh-cn_image_0000002779567266.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B6CA5170ED064E7A56728FA5C734E5EB5E5F55B0258776C6B28BA55EDEEB11C)

## 编译报错“Property xxx does not exist on type 'typeof BuildProfile'.”

**问题现象****1**

使用了自定义参数BuildProfile，编译态无异常但编译构建失败，提示“Property xxx does not exist on type 'typeof BuildProfile'.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/Px0_gKzrSo6Sqn_utA4k7A/zh-cn_image_0000002808766861.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=DEE3FAB4D55AD2A6F097F2C451FBC950B15D0C9343A0CE9E3AC5ED54B2630BE6)

**处理措施**

检查在当前模块下build-profile.json5中的targets > buildProfileFields配置的自定义参数中key值是否相同，如果不同请将targets内所有buildProfileFields中的key值保持相同。

以下为导致编译报错的**错误**配置示例：

```json5
"targets": [
  {
    "name": "default",
    "config": {
      "buildOption": {
        "arkOptions": {
          "buildProfileFields": {
            "targetName": "default"
          }
        }
      }
    }
  },
  {
    "name": "default1",
    "config": {
      "buildOption": {
        "arkOptions": {
          "buildProfileFields": {
            "targetName1": "default1"
          }
        }
      }
    }
  },
]
```

请将targets内所有buildProfileFields中的key值修改一致，如以下示例：

```json5
"targets": [
  {
    "name": "default",
    "config": {
      "buildOption": {
        "arkOptions": {
          "buildProfileFields": {
            "targetName": "default"
          }
        }
      }
    }
  },
  {
    "name": "default1",
    "config": {
      "buildOption": {
        "arkOptions": {
          "buildProfileFields": {
            "targetName": "default1"
          }
        }
      }
    }
  },
]
```

**问题现象2**

使用了自定义参数BuildProfile并且编译器标红且构建失败，提示“Property xxx does not exist on type 'typeof BuildProfile'.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/5U7LhC6HSyuV7qhTmAwbBA/zh-cn_image_0000002808886931.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=76A5B8735A76A82E77D433A697958D8B358D3E7729220A8669E820AA6D35B251)

**处理措施**

请检查当前模块下build-profile.json5中buildProfileFields内是否添加了所使用的自定义参数，请确保该自定义参数已配置在buildProfileFields内。

## CPP编译报错"A 'undefined symbol' error has occurred"

**问题现象**

在编译HarmonyOS C++ 项目时，报错提示"A 'undefined symbol' error has occurred"。

**解决措施**

"undefined symbol"错误通常表示链接器找不到特定符号的定义。这通常是因为源文件没有正确编译或链接，或者因为缺少必要的库文件。以下是如何定位和解决这个问题的步骤：

1. 确保所有源文件都已包含在 CMake 构建中。

首先，检查您的 CMakeLists.txt 文件，确保所有相关的源文件都已包含在项目中。

**示例 CMakeLists.txt**

```txt
cmake_minimum_required(VERSION 3.10) 
project(MyProject)  
set(CMAKE_CXX_STANDARD 17)  
include_directories(${CMAKE_CURRENT_SOURCE_DIR}                    
                    ${CMAKE_CURRENT_SOURCE_DIR}/include)  
# 添加所有源文件
add_library(myProgram SHARED main.cpp myLibrary.cpp)
```

2. 确认源文件的符号定义。

确保在所有相关的源文件中正确定义了符号。例如，检查 myLibrary.cpp 是否包含 myFunction 的定义：

**myLibrary.cpp**

```cpp
#include "myLibrary.h" 
void myFunction() {     
// Function implementation
}
```

**myLibrary.h**

```cpp
#ifndef MY_LIBRARY_H
#define MY_LIBRARY_H 
void myFunction();  
#endif
```

3. 检查编译和链接顺序。

确保所有源文件和库文件按照正确的顺序进行编译和链接。CMake 和 Ninja 通常会处理这个问题，但在手动编译时可能会出现问题。

4. 清理和重新生成构建文件。

有时，构建文件可能会损坏或丢失符号定义。尝试清理构建目录并重新生成构建文件：

```bash
hvigorw clean 1
```

或手动删除模块下.cxx目录。

5. 检查库路径和链接器标志。

如果使用三方库，确保 CMakeLists.txt 中正确配置了库路径和链接器标志。例如：

```txt
cmake_minimum_required(VERSION 3.10) 
project(MyProject)  
set(CMAKE_CXX_STANDARD 17)  
# 确保添加三方库的头文件
include_directories(${PATH_TO_EXTERNAL_LIBRARY}
                    ${PATH_TO_EXTERNAL_LIBRARY}/include)  
# 添加源文件
add_library(myProgram SHARED main.cpp myLibrary.cpp)  
# 链接三方库
target_link_libraries(myProgram PUBLIC /path/to/external/library)
```

6. 启用详细编译和链接输出。

为了解详细的编译和链接过程，可以启用更详细的输出。在 CMakeLists.txt 中添加以下内容：

```txt
set(CMAKE_VERBOSE_MAKEFILE ON)
```

7. 检查 Ninja 输出日志。

Ninja 默认生成 .ninja\_log 文件，其中包含构建过程的详细信息。您可以检查这个日志文件以了解构建过程中的问题。

```bash
cat {module}/.cxx/default/default/arm64-v8a/.ninja_log
```

检查编译日志中是否存在符号所在的源文件或头文件。

8. 使用 nm 工具检查符号。

使用 nm 工具检查目标文件和库文件中的符号，确保符号定义存在。

可使用sdk中内置的nm工具：sdk/default/openharmony/native/llvm/bin/llvm-nm。

**检查目标文件**

```bash
nm myLibrary.o | grep myFunction
```

**检查三方库文件**

```bash
nm /path/to/external/library | grep myFunction
```

**结论**

通过上述步骤，您可以定位和解决 error: undefined symbol 问题。在使用 CMake、Ninja 和 LLVM 编译 C++ 项目时，确保所有源文件和库文件正确包含在项目中，并正确配置编译和链接选项是关键。如果问题依旧存在，详细的编译和链接输出日志通常能提供更多线索，帮助您找到具体的原因。

## CPP编译报错"A 'unknown type name' error has occurred"

**问题现象**

在编译HarmonyOS C++ 项目时，报错提示"A 'unknown type name' error has occurred"。

**解决措施**

在编译HarmonyOS C++ 项目时，遇到"unknown type name"错误通常表示编译器无法识别某个类型。这可能是因为类型未定义、未包含相关的头文件，或者包含的头文件路径不正确。以下是定位和解决这个问题的步骤：

1. 检查是否包含头文件。

   确保所有必要的头文件都已正确包含在源文件中。例如，如果您正在使用某个自定义类型或库提供的类型，请确保在使用该类型的文件中包含了相关的头文件。

   **示例：**

   ```cpp
   // main.cpp
   #include "myLibrary.h" 
   int main() {
        MyType obj;
        // 使用自定义类型
        return 0;
   }

   // myLibrary.h
   #ifndef MY_LIBRARY_H
   #define MY_LIBRARY_H
   class MyType {
   public:
        MyType() {}
        void doSomething();
   };
   #endif
   ```
2. 检查头文件路径。

   确保 CMakeLists.txt 中正确设置了头文件的搜索路径。可以通过 include\_directories 添加头文件目录。

   **示例 CMakeLists.txt：**

   ```txt
   cmake_minimum_required(VERSION 3.10) 
   project(MyProject)  
   set(CMAKE_CXX_STANDARD 17)  
   # 添加头文件目录
   include_directories(${CMAKE_SOURCE_DIR}/include)  
   # 添加源文件
   add_library(myProgram SHARED src/main.cpp src/myLibrary.cpp)
   ```
3. 清理和重新生成构建文件。

   有时，构建文件可能会损坏或丢失符号定义。尝试清理构建目录并重新生成构建文件：

   ```bash
   hvigorw clean
   ```

   或手动删除模块下.cxx目录。
4. 启用详细编译输出。

   为了解详细的编译过程，可以启用更详细的输出。在 CMakeLists.txt 中添加以下内容：

   ```txt
   set(CMAKE_VERBOSE_MAKEFILE ON)
   ```
5. 检查编译输出日志。

   Ninja 默认生成 .ninja\_log 文件，其中包含构建过程的详细信息。你可以检查这个日志文件以了解构建过程中的问题。

   ```bash
   cat .cxx/default/default/arm64-v8a/.ninja_log
   ```
6. 使用 CMake 的 message 函数调试。

   可以在 CMakeLists.txt 文件中添加 message 函数来打印一些调试信息，以确保路径和变量正确设置。

   **示例：**

   ```txt
   message(STATUS "Source directory: ${CMAKE_SOURCE_DIR}") 
   message(STATUS "Include directories: ${CMAKE_INCLUDE_PATH}")
   ```
7. 如果报错接口是系统API，请查阅对应API参考的起始版本，确认接口在当前版本是否可用。

**结论**

通过上述步骤，您可以定位和解决 unknown type name 问题。在使用 CMake、Ninja 和 LLVM 编译 C++ 项目时，确保所有头文件正确包含并设置正确的头文件路径是关键。如果问题依旧存在，详细的编译输出日志通常能提供更多线索，帮助您找到具体的原因。

## 编译报错“Init keystore failed: parseAlgParameters failed: ObjectIdentifier()”

**问题现象**

编译构建时，出现错误：Init keystore failed: parseAlgParameters failed: ObjectIdentifier()。

```txt
hap-sign-tool: error: ACCESS_ERROR, code: 109. Details:   Init keystore failed: parseAlgParameters failed: ObjectIdentifier() -- data isn't an object ID (tag = 48)   Detail: Please check the message from tools
```

**错误原因**

使用高版本JDK生成密钥对（p12），再使用低版本的JDK执行签名命令时，会因为不兼容导致解析p12失败，从而签名失败。

**场景**

1. 使用DevEco Studio生成密钥对时，DevEco Studio默认会调用软件内预置的JDK，而用户使用本地的低版本JDK进行签名时则会报错。
2. 用户本地使用高版本JDK生成密钥对时，又通过DevEco Studio进行签名，DevEco Studio中预置的JDK版本低于用户的JDK，导致报错。

**解决方案**

请检查当前使用的JDK版本和生成密钥对使用的JDK版本，使用版本匹配的JDK执行签名命令。

## 编译报错“generate SignerBlock failed”

**问题现象**

编译构建时，出现错误：message:generate SignerBlock failed。

```txt
hap-sign-tool: error: {errorcode:0,message:generate SignerBlock failed}
```

**错误原因**

签名用的公私钥对不匹配，使用私钥签名后，用公钥验签失败。需保证私钥（keyalias）和公钥（appCertPath）配对使用。

**场景**

1. 本地生产签名材料时，未导出正确的keyalias对应的csr（证书请求文件），导致生成证书时，公钥与keyalias对应的私钥不匹配。
2. 签名过程参数填写错误，使用了错误的keyalias或者appCertPath文件。

**解决方案**

请选择正确、配对的keyalias和appCertPath文件。

## 编译报错“java.io.IOException: DerValue.getOID, not an OID 49”

**问题现象**

编译构建时，出现错误：java.io.IOException: DerValue.getOID, not an OID 49。

```txt
hap-sign-tool: error: ACCESS_ERROR, code: 109. Details: java.io.IOException: DerValue.getOID, not an OID 49 Detail: Please check the message from tools
```

**报错原因**

证书文件解析失败，找不到证书的OID。

**场景**

1. 证书被篡改。
2. appCertPath参数中传入了非证书文件。

**解决方案**

请检查证书文件是否正确。

## 构建报错“input module releaseType is different”

**问题现象**

打包APP时，提示“input module releaseType is different”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/ApqwVRjYSSqniRbJc6dEWw/zh-cn_image_0000002780681220.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FEF5A231046B3CD344BCA54D30065E41294FDF7CB3FC194109D7C0B25A8252C)

**解决措施**

根据报错日志的Warning信息所提示的模块名称，检查模块间的apiReleaseType字段是否一致。

该apiReleaseType字段由编译构建工具自动生成，保存在HAP/HSP包的module.json文件中。如下图所示，首先确认各模块间该字段是否一致，如果存在不一致的情况，需要将应用的各个模块，使用相同版本的SDK重新打包，然后打包APP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/ID8G-fZjTR2bCkWzUaz2Iw/zh-cn_image_0000002810120827.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=92C31AF45E4C4E5B4E929DECA401309B44AF22B7CC0AB32F871883EDAD088846)

## 构建报错“debug is different”

**问题现象**

打包APP时，提示“debug is different”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/4ua-VhPJRd-CC6HDq1At-Q/zh-cn_image_0000002810040731.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=7334DBA321CC3754EE20CB6EF362679D7689261EE1E3964B779E8C6C5ECA8283)

**解决措施**

根据报错日志的Warning信息所提示的模块名称，检查模块间的debug字段是否一致，尤其需要关注本地模块和外部引用模块之间是否一致。

1. 该debug字段由编译构建工具自动生成，保存在HAP/HSP包的module.json文件中，如下图所示，首先确认各模块间该字段是否一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/qcbvqHEdRcWrJbsEztvCOA/zh-cn_image_0000002780841182.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA83F18F470482CD0187761F4833EE510187C2A2E7B43F518EA1AE67EBD51345)
2. 编译工具根据设置的Build Mode选项生成debug标识，如图所示，可以通过此处进行设置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Wl_ztU6VSvKFjP0hBZGnnw/zh-cn_image_0000002780681232.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8D69434D9DEAC1CAAFAFA9B2AB3AAD5EB079A6D555BF7AD114786BDB548AF67)

## 编译报错 “Unknown resource name”

* 场景一

**问题现象**

工程中模块A引用了模块B，编译模块A时出现错误，提示 "Unknown resource name 'xxxx'"，找不到模块B的资源。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/ff2xvVzRRFiGDx64x884jw/zh-cn_image_0000002810120863.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C13E9DF1C4F3595F74A0DED4DD29203EFC1AFD337B94D76515C70628C4C2CDF6 "点击放大")

**解决措施**

请确保符合以下条件：

1. 资源需放置在目录resource/base路径下。
2. 模块B已安装。
3. 模块A中不能使用相对路径引用模块B的资源，应直接通过定义的模块名称来引用。

* 场景二

**问题现象**

引用模块的方式不对，如果引用的是一个其他模块的代码，也会报资源找不到。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/0klQlYJpTlKkaMiHa6HOSg/zh-cn_image_0000002810040785.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=77022ED9C8C8FEAAFA7BBF79A501F28D8D5AD507B8C93337C80361195AF75E84)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/69UpOypzSra2m6FdRP2S6g/zh-cn_image_0000002780841240.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3DA2314BF934CF73B48A72E21724557010E620BAE48F92D9795FBD10694A775F)

**解决措施**

在oh\_package.json5中引入该模块。通过定义的模块名称来引用。

如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/B-NyjdQ1Q0u_bilpV-O77w/zh-cn_image_0000002780681286.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8002D434EF7F9595F68C850B79D36A6F3D41BA3F1E4FA587D7F9FA2AADD9A719)

* 场景三

**问题现象**

HSP A 申请了某个权限，这个权限进行了资源的引用，在所有依赖A的组件进行构建时，报错 A 引用的资源找不到。

**解决措施**

手动在引用方配置对应资源可以解决此问题。

## 如何解决编译报错“Error: cJSON\_Parse failed, please check the JSON file.”的问题

**问题现象**

编译报错“Error: cJSON\_Parse failed, please check the JSON file”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/oE_nt_vNQ0-SDriA0hZ5aw/zh-cn_image_0000002810120895.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A2D8A625F132D2AAD09ACA50168F083DA0AD175F79DD459AE13698BB23FF2FB "点击放大")

**报错原因**

module.json文件格式不正确。

**常见场景**

1. json文件内末尾多了逗号。
2. 根标签不是大括号{}。

**解决措施**

检查报错指向的json文件格式，比如是否末尾多了逗号，根标签是否为大括号{}。

## 编译报错“The useNormalizedOHMUrl settings of packages xxx and the project useNormalizedOHMUrl: xxx do not match”

**问题现象**

编译报错“The useNormalizedOHMUrl settings of packages xxx and the project useNormalizedOHMUrl: xxx do not match”。

**解决措施**

[useNormalizedOHMUrl](ide-hvigor-build-profile-app.md#section13181758123312) 为true的时候ohmurl使用的是新的拼接和解析方式，不能和旧的ohmurl混用，会导致运行时无法识别。

可采用以下两种方式解决该问题：

* 将报错的依赖包的工程级build-profile.json5中的useNormalizedOHMUrl修改为与当前工程一致，重新生成依赖包并替换（useNormalizedOHMUrl缺省默认值为false）。

  ```json5
  {
    "app": {
      "products": [
        {
           "buildOption": {
             "strictMode": {
               "useNormalizedOHMUrl": true
             }
           }
        }
      ]
    }
  }
  ```
* 如果与工程不一致的依赖包较多，建议修改工程的工程级build-profile.json5中的useNormalizedOHMUrl值以及替换其它的不一致的依赖包。

如果修改了useNormalizedOHMUrl仍无法解决，表明当前hsp包是本地包，需要以本地hsp包的形式引入，请在工程下的build-profile.json5中的modules中添加报错hsp模块，示例如下：

```json5
"modules": [
  {
    name: "hsp",   // 引用的hsp包依赖
    srcPath: "../MyApplication_stageB/hsp",   // 引用的hsp包的路径（绝对和相对都可以）
  }
]
```

## 如何解决编译报错“Could not resolve 'xxx' from”，但'xxx'目录存在的问题

**问题现象**

编译报错：“Could not resolve 'xxx' from”，但'xxx'目录存在，目录下存在Index文件。

**问题原因**

在引用目录时，编译时自动拼接小写的index文件，但目录中是大写的Index文件，在编译大小写敏感时，因找不到index文件而报错。

**解决措施**

在引用'xxx'目录时，明确写明引用到'xxx/Index'文件。

## 用户目录下没有npmrc文件

**问题现象**

新建项目报错 Error: The hvigor depends on the npmrc file. Configure the npmrc file first。

**问题原因**

在用户目录下没有 .npmrc 文件。

**解决措施**

在用户目录下创建.npmrc文件，配置如下信息：

```txt
registry=https://repo.huaweicloud.com/repository/npm/
@ohos:registry=https://repo.harmonyos.com/npm/
```

## 如何解决编译报错“Error: the name 'XXX' can only contain [a-zA-Z0-9\_].”的问题

**问题现象**

编译报错“Error: the name 'XXX' can only contain [a-zA-Z0-9\_]”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/UODGgYGNQBeOFcMlDRCVyQ/zh-cn_image_0000002810040795.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FB0952794259C2B3B5482B8D688CA34721E5EDB1B1F7D76F7BF349FC0923DA6)

**解决措施**

检查文件名是否合法，文件名只能包含大小写字母、数字、下划线。

## 如何解决编译报错“Cannot add xxxx items to index”的问题

**问题现象**

编译报错“Cannot add xxxx items to index”。

**问题原因**

被编译文件中某函数内部有大量object literal, array literal和string，导致item的数量超过了上限（65536）。

**解决措施**

排查相关文件，将存在上述原因的函数进行拆分。

## 如何解决编译卡死，提示“The modules directory at "xxx/workspace/node\_modules" will be removed and reinstalled from scratch. Proceed? (Y/n) > true”的问题

**问题现象**

编译卡死，提示“The modules directory at "xxx/workspace/node\_modules" will be removed and reinstalled from scratch. Proceed? (Y/n) > true”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/B_f70fJ2T2yrxX8dpGvRGg/zh-cn_image_0000002779407274.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=CAA4B04F574CD9F386A5BB45606EF9DA4CA11EF9D6CCF1E978BE127C9703A7B7)

**问题原因**

安装构建插件使用的pnpm版本和当前DevEco Studio使用的pnpm版本不一致。

**解决措施**

1. 使用DevEco Studio 26.0.0及以上版本。
2. 如果还是使用当前DevEco Studio版本，删除报错中的路径（例如以上是删除“C:\Users\xxxx\.hvigor\project\_caches\8e4ab2ae81c130fec666aeb0b81bd299”目录）和“C:\Users\xxxx\.hvigor\wrapper”目录。
