---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-faqs
title: 编译构建常见问题
breadcrumb: 指南 > 构建应用 > 构建报错排查 > 编译构建常见问题
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2bc0618fc1dadd5ccbff827950e4893079c9f1252b8a46f329c619ea7203c48d
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

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/-zWjvqnpQAqYg7HIvd6FjA/zh-cn_image_0000002731382759.png)
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

     假设是entry模块的hvigorfile.ts中的代码导致的问题 ，XXX的有效值就是下图中的“default@SignHap”、“default@CollectDebugSymbol”、“assembleHap”等值。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/Czp2MvNKTem_MEa_Lsj8nA/zh-cn_image_0000002701663584.png)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/WGinssApTCK5HWf2eIPyTQ/zh-cn_image_0000002731542741.png)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/Dg5jl_DvSV6OYoTFHLEqIA/zh-cn_image_0000002731382805.png)

**解决措施**

使用select、pickFirsts、pickLasts等配置选中要使用的so文件; select提供native产物的精准选择能力，优先级高于excludes、pickFirsts等配置项。pickFirsts、pickLasts按照.so文件的优先级顺序，打包最高优先级的.so文件，优先级顺序是指依赖收集的顺序，越晚被收集优先级越高。

具体可参考：[配置CPP](ide-hvigor-cpp.md)。

基于上面的例子，可以在entry的build-profile.json5中添加配置select选中har模块中的so文件，package选中包名为“har”的模块, include选中“libhar.so”文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/vb-wsqggShS99pyl7mBkpA/zh-cn_image_0000002701823460.png)

## 构建报错“input module releaseType is different”

**问题现象**

打包APP时，提示“input module releaseType is different”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/c0-pw_zUQlSO2mN6ABSChg/zh-cn_image_0000002701663578.png)

**解决措施**

根据报错日志的Warning信息所提示的模块名称，检查模块间的apiReleaseType字段是否一致。

该apiReleaseType字段由编译构建工具自动生成，保存在HAP/HSP包的module.json文件中。如下图所示，首先确认各模块间该字段是否一致，如果存在不一致的情况，需要将应用的各个模块，使用相同版本的SDK重新打包，然后打包APP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/ZdL-77TWQWqSnHDDYSYwXg/zh-cn_image_0000002701663518.png)

## 构建报错“debug is different”

**问题现象**

打包APP时，提示“debug is different”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/hx8K1q2HRZ2jsicA5cInjQ/zh-cn_image_0000002701823428.png)

**解决措施**

根据报错日志的Warning信息所提示的模块名称，检查模块间的debug字段是否一致，尤其需要关注本地模块和外部引用模块之间是否一致。

1.该debug字段由编译构建工具自动生成，保存在HAP/HSP包的module.json文件中，如下图所示，首先确认各模块间该字段是否一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/1-FMLrtpR7mv2dXL-ltDwQ/zh-cn_image_0000002701663524.png)

2.编译工具根据设置的Build Mode选项生成debug标识，如图所示，可以通过此处进行设置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/Axm-wCJxQ9eDE-zSNr9DBg/zh-cn_image_0000002731542709.png)

## 构建报错“proxy data is duplicated”

**问题现象**

打包APP时，提示“uri datashareproxy://bundleName/\*\* in proxy data is duplicated”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/c_bhaZcATgi9SDrjeG5vzQ/zh-cn_image_0000002731382753.png)

**解决措施**

proxyData标识模块提供的数据代理列表，只允许entry和feature配置，不同的proxyData中配置的URI不可重复。遇到此问题，检查模块间是否配置了相同uri的proxyData。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/20BNLrp6TBWRm_vKhciFuw/zh-cn_image_0000002731542713.png)

## 编译报错“Init keystore failed: parseAlgParameters failed: ObjectIdentifier()”

**问题现象**

编译构建时，出现错误：Init keystore failed: parseAlgParameters failed: ObjectIdentifier()。

```txt
hap-sign-tool: error: ACCESS_ERROR, code: 109. Details:   Init keystore failed: parseAlgParameters failed: ObjectIdentifier() -- data isn't an object ID (tag = 48)   Detail: Please check the message from tools
```

**错误原因**

使用高版本JDK生成密钥对(p12)，再使用低版本的JDK执行签名命令时，会因为不兼容导致解析p12失败，从而签名失败。

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

签名用的公私钥对不匹配，使用私钥签名后，用公钥验签失败。需保证私钥(keyalias)和公钥(appCertPath)配对使用。

**场景**

1. 本地生产签名材料时，未导出正确的keyalias对应的csr(证书请求文件)，导致生成证书时，公钥与keyalias对应的私钥不匹配。
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

## 编译报错“JS heap out of memory”

**问题现象**

编译构建时，出现报错“JS heap out of memory“。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/JHe4Ek9xTk-AxOvl2OUsSw/zh-cn_image_0000002731542745.png)

**解决措施**

出现该报错的原因是Hvigor运行时内存不足，在使用3.1.0及以上版本的Hvigor时，可通过以下方式修改Hvigor运行时内存的最大值。

勾选Enable the Daemon for tasks：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/KWCxlHzlQM2IhwUFYl_bqw/zh-cn_image_0000002701663544.png)

在hvigor-config.json5中修改maxOldSpaceSize字段，根据工程的大小，适当将其增大（如设置为8192）：

```json5
"nodeOptions": {
  "maxOldSpaceSize": 8192
}
```

## Linux环境下编译报错“JS heap out of memory”

**问题现象**

在Linux环境下，系统内存有64G，Hvigorw脚本中配置--max-old-space-size=40960，在编译构建时，实际在使用内存未达到配置的内存（例如使用到20G左右）就出现报错“JS heap out of memory“。

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

  Stage模板工程编译引用native文件(.so) 提示 "Cannot find module XXX or its corresponding type declarations."。

  **处理措施**

  当前Stage工程在编译构建阶段新增对native文件(.so)导出符号的语法校验，如果引用了没有对应声明文件(.d.ts)的native文件(.so)的现有工程在编译构建阶段，语法校验工具便会报错提示找不到对应的声明文件。

  如果出现类似问题，可尝试通过如下方式进行解决：

  1. 在对应cpp目录下新建types/libxxx目录，并在该目录下新增index.d.ts用于声明native的类型符号；新增oh-package.json5配置文件用于校验工具的模块查询。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/rOcP_bHXQNmiIS8qTGY7zw/zh-cn_image_0000002701663522.png)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/gneJ4zXLTFuckeXF-F-M9Q/zh-cn_image_0000002701823466.png)
  2. 在native引用的模块内的oh-package.json5中添加native模块的本地依赖，并根据提示点击**Sync Now**同步工程，下图以entry模块引用native模块为例。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/RAZpygtnTm2HRCXKiLPzgA/zh-cn_image_0000002731542723.png)

* 场景二：

  **问题现象**

  引用三方包，构建失败，提示“Cannot find module 'xxx' or its corresponding type declarations”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/VPPtDQhhT0iOPuAfelk2XA/zh-cn_image_0000002701823476.png)

  **处理措施**

  进入对应模块级oh-package.json5文件或工程级oh-package.json5文件中查看三方包是否已安装，若未安装，需执行ohpm install安装；若已安装，需查看“main”字段是否配置正确，若未配置或配置错误，需配置为正确的入口文件。
* 场景三：

  **问题现象**

  引用的包路径被混淆，代码中又是在引用包后面拼接了路径，导致模块引用不到而报错。

  例如：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/nsQGGfA2RFKzyvpphMEKVg/zh-cn_image_0000002701663506.png)

  代码中这样引用

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/bbveg8JxQ7S1NbSb2j8MoQ/zh-cn_image_0000002701823482.png)这样引用会找不到模块，导致报错。

  **处理措施**

  修改引用方式，改为推荐的引用方式

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/V4Dy6PQGTVS0S3Tc-65qIA/zh-cn_image_0000002701823490.png)
* 场景四：

  **问题现象**

  被引用模块oh\_package.json5配置有误，执行了ohpm install 并且成功地安装了依赖，但是还报错模块找不到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/Q-5k_riJTcCqxlQxzd-flw/zh-cn_image_0000002701663594.png)

  被引用模块的 oh\_package.json5 中配置了错误的types字段。

  该字段优先于main字段。 如果 types 字段配置的不存在，就会报错模块找不到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/z-HH1XvsR7mcTeT3Qx2ZEQ/zh-cn_image_0000002731542743.png)

  **处理措施**

  如果该包中没有d.ets声明，则这个字段可以删除。配置不存在或者错误，会导致报错。
* 场景五：

  **问题现象**

  oh\_package.json5 中 dependencies 中引入模块的 名称 和 实际使用时 import 的 不一致。

  例如 在 oh\_package.json5 中这样引入：

  ```json5
  "dependencies": {   "har": "file:../har" }
  ```

  但是实际上在代码中import 的时候是 大写 HAR 或者其他而不是 dependencies 里面配置的 ‘har’ 的值，要注意保持完全一致。（目前windows 没有问题，linux会报错模块找不到）

  **处理措施**

  引入和使用改成一致。
* 场景六：

  **问题现象**

  引用模块的 oh\_package.json5 中 main 字段值和实际的文件名称大小写不一致。

  **处理措施**

  将main字段和实际文件名称的大小写改为一致。
* 场景七：

  **问题现象**

  Stage模板工程编译构建失败，提示 "Cannot find module '@bundle:rollup\_plugin\_ignore\_empty\_module\_placeholder' or its corresponding type declarations"。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/z8Pl09seT9aCDWx1EfcjbQ/zh-cn_image_0000002701663592.png)

  **解决措施**

  该问题是由于工程引用了无对应实现文件的.d.ts声明文件：

  1. 通过在build目录中搜索'rollup\_plugin\_ignore\_empty\_module\_placeholder'，找到报错的中间文件，并根据中间文件找到对应工程文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/ZP8ldh0rQw21Eu4Fxef4Kg/zh-cn_image_0000002701823480.png)

     在输入栏中输入rollup\_plugin\_ignore\_empty\_module\_placeholder，找到问题模块的中间文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/PInYhXgrTf2aKEgz6Ud5mg/zh-cn_image_0000002701823440.png)
  2. 在引用类型文件中通过添加type显式声明符号类型引用：

     ```ts
     export type {T} from './type';
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/hizv8swJS--E4ChVyAbQHA/zh-cn_image_0000002731542781.png)
  3. 同时排查是否从d.ts/d.ets中引用值类型符号，禁止在声明文件中声明值变量。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/2_N-gcTpRC6u2RGf9fU9TA/zh-cn_image_0000002701663530.png)

## 编译报错“Module 'xxx' has no exported member 'yyy'”

**问题现象**

Stage模板工程编译构建失败，提示 "Module 'xxx' has no exported member 'yyy'" 并且"yyy"符号是由export \* from 'x.js'语法从js文件中导出。

**处理措施**

当前Stage工程编译构建期的语法校验工具对js文件不作检查，因此当使用export \* from 'x.js'导出js文件中的符号时，符号引用处便会提示"Module 'xxx' has no exported member 'yyy'"的错误信息。

如果出现类似问题，可尝试通过如下方式进行解决：

* 方法1（推荐使用）： 使用符号显式导出语法，从js文件中re-export符号 。

  ```ts
  export { yyy } from 'x.js'
  ```

* 方法2：新增x.js对应的声明文件(.d.ts)，并在引用时不指定后缀。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/IIuFJQl1S6SFDDP60zgz8Q/zh-cn_image_0000002701663590.png)

## 编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”

**问题现象**

Stage模板工程编译构建失败，提示 "ERROR: Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/yWyO4_z9QaGBSJv8l149Hg/zh-cn_image_0000002701823514.png)

**处理措施**

该问题是由于file1为当前工程外的代码：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/dgFC4biEQym9cijpsljJHQ/zh-cn_image_0000002701823506.png)

请新建Static Library模块，并将工程外的代码迁移至Static Library模块内，并使用HAP引用HAR方式进行模块间引用。

## 编译报错“Failed to get a resolved OhmUrl by filepath xx”

* **场景一：**

  **问题现象**

  三方包在配置依赖时，配置到devDependencies，源码中又有引用依赖中的API时，编译失败。如以下示例：三方包@hms-security/ucs-appauth将依赖@network/gr配置在devDependencies中，源码中使用了@network/grs的API时，编译失败，提示“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/P2OUqmQbTlaE-ghKNBTZJA/zh-cn_image_0000002701823516.png)

  **问题确认**
  1. 进入上面报黄色的源码文件中，可以看到依赖有红色告警信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/wWtfJIeAS3-cRGRBY839PA/zh-cn_image_0000002731382757.png "点击放大")
  2. 进入包下的oh-package.json5文件，查看依赖配置为devDependencies。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/ASjHB42GQTy8odS3nie4mA/zh-cn_image_0000002731382795.png)

  **处理措施**
  + 向此包开发团队提改进建议：运行时的依赖，不能配置在devDependencies中。
  + 可在依赖上层引入对应devDependencies中的三方包规避此问题。

* **场景二：**

  **问题现象**

  DevEco Studio编译失败，提示“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/q6r_Y9s3QrmdvTZmgKiQYg/zh-cn_image_0000002731382743.png)

  **问题确认**

  查看工程目录下的build-profile.json5文件中modules字段配置的srcPath路径是否与真实路径不相同，是否存在大小写不一致问题。

  **处理措施**

  将工程目录下的build-profile.json5文件中modules字段配置的srcPath路径与真实路径保持一致。
* **场景三：**

  **问题现象**

  工程A以相对路径引用了工程B的模块，这种引用会导致报错。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/31Anz58RT2CA0dddHh-YvQ/zh-cn_image_0000002731382779.png)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/87x99srjSaq5KiSIzse7pg/zh-cn_image_0000002701663560.png)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/nFcg7YRzTeqNZ3EXUcYAgQ/zh-cn_image_0000002731542751.png)**处理措施**

  + 把工程B这种的har转至工程A里，作为A的一个模块引用。
  + 把工程B的har提前打包，在A中 以.har的方式引用。
  + 上传到仓库，以版本号的方式引用。
* **场景四：**

  **问题现象**

  DevEco Studio编译失败，提示“Error Message: Failed to get a resolved OhmUrl for 'hvigor\_ignore\_xxxxx' imported by xxx”。

  **处理措施**

  如果hvigor\_ignore\_xxxxx所在的模块是har模块，需排查oh\_package.json5中是否存在"packageType": "InterfaceHar"，若存在则删除。
* **场景五：**

  **问题现象**

  DevEco Studio编译失败，提示“Failed to get a resolved OhmUrl for 'xxx' imported by 'yyy'”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/cda9-9TYR2WtWPy81hYRSQ/zh-cn_image_0000002731542727.png "点击放大")

  **问题确认**

  1. 排查yyy所在模块是否为[字节码har](ide-hvigor-build-har.md#section16598338112415)，查看工程级build-profile.json5的useNormalizedOHMUrl是否为true（缺省默认值为false），如果为true则默认构建字节码har。
  2. 如果yyy所在模块是字节码har，请排查xxx依赖是否被配置在工程级oh\_package.json5的dependencies，但没有配置在yyy模块级oh\_package.json5的dependencies中。

  **处理措施**

  + 将xxx依赖配置到yyy模块oh\_package.json5的dependencies中。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/QlKqJktVRMKwlrRbd0wqJQ/zh-cn_image_0000002701823452.png "点击放大")
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/CgVN19aWT7ip-KRGLbnYgw/zh-cn_image_0000002731382823.png)
* **场景七：**

  **问题现象：**

  DevEco Studio编译失败，提示 "ERROR: ArkTS:ERROR failed to execute es2abc ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx"。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/Z6Hj6iBgSi2i1AYnQbO2pA/zh-cn_image_0000002731542735.png)

  **处理措施**

  该问题是由于在工程中引用了非工程标准模块目录（即目录内无模块描述文件module.json5），如下图utils目录所示：请新建Static Library模块，并将utils/common里面的代码迁移至Static Library模块内，并使用HAP引用HAR方式进行模块间引用。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/3M4G0dh-SSuCoGvmC82Z0A/zh-cn_image_0000002701823442.png)

## 编译报错“Property xxx does not exist on type 'typeof BuildProfile'.”

**问题现象****1**

使用了自定义参数BuildProfile，编译态无异常但编译构建失败，提示“Property xxx does not exist on type 'typeof BuildProfile'.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/uMOmO8ymSXiWDMbdo5gLKQ/zh-cn_image_0000002731542765.png)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/lVkZbTL7TMW7EA4Whln3mQ/zh-cn_image_0000002731542701.png)

**处理措施**

请检查当前模块下build-profile.json5中buildProfileFields内是否添加了所使用的自定义参数，请确保该自定义参数已配置在buildProfileFields内。

## C++工程编译导致电脑卡顿的处理建议

**问题现象**

在执行代码规模较大的C++工程的编译时，由于C++编译时的CPU占用率较高，可能出现电脑卡顿、反应迟缓等现象。

**处理措施**

如果出现类似问题，可尝试通过如下方式进行解决：

打开模块下的build-profile.json5文件，在**arguments**参数中添加如下配置。并根据电脑CPU配置，修改compile和link的值。建议compile和link的值之和，设置为CPU核数的一半，如CPU为8核，则compile和link分别设置为2。

```json5
"arguments": "-DCMAKE_JOB_POOL_COMPILE:STRING=compile -DCMAKE_JOB_POOL_LINK:STRING=link -DCMAKE_JOB_POOLS:STRING=compile=2;link=2",
```

需要说明的是，修改了compile和link的值，可能会导致编译时长增加，请耐心等待。

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

## LABEL\_VALUE\_ERROR处理指导

**问题现象**

在工程同步、编译构建过程中，提示**LABEL\_VALUE\_ERROR**错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/cKHr_OXMSBOuIHUOx-zDsg/zh-cn_image_0000002731382821.png)

**解决措施**

该问题是由于config.json文件的资源引用规则变更导致，需要将“label”字段的取值，修改为资源引用方式。

1. 在**resources > base > element**中的string.json中添加对应的字符串信息。
2. 然后在config.json中重新引用该字符串资源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/_G7lia1yTMCv4HBVTpMh5g/zh-cn_image_0000002731382813.png)

## 应用/元服务的启动界面信息缺失，提示"Schema validate failed"报错

**问题现象**

在工程同步或者编译构建时出现错误，提示“Schema validate failed”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/k9htFypgRcy2X5WZz29PBA/zh-cn_image_0000002701823432.png)

**解决措施**

在开发应用/元服务时，可以设置应用/元服务的启动界面的图标及背景颜色，创建工程后自动设置了默认的启动界面信息，但若开发者误删其中某个字段后将导致报错。下面以重新设置启动界面信息为例，开发者可自定义启动界面的图标及背景颜色。

在开发应用/元服务时，为了提升应用/元服务冷启动的性能，您可以通过如下方式设置应用/元服务的启动界面的图标及背景颜色。

1. 在模块下的**resources > base > element**下，点击右键选择**New > Element Resource File**创建资源文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/xvPy_tPcRFaHOm_5zcVkTA/zh-cn_image_0000002731542697.png)
2. 在弹出的对话框中，“File name”开发者可自定义，如color；“Root element”请选择**color。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/xI5O2J-7R5SKmY2PBSeQ1Q/zh-cn_image_0000002701823464.png)

   创建完成后，color.json文件如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/7hf6GhwTQNKFpmgqipBTtw/zh-cn_image_0000002731382737.png)
3. 将[2](ide-hvigor-faqs.md#li124901748185712)创建的color.json文件拷贝至模块的**ohosTest > resources > base > element**目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/t7dT2G9pTReYJN7vPy8bGg/zh-cn_image_0000002731542731.png)
4. 在模块的**src > main > module.json5**文件的abilities数组中，添加startWindowIcon和startWindowBackground字段（若缺少任一字段，将出现ERROR: Schema validate failed报错）。其中，startWindowIcon字段索引模块下**resources > base > media**中的图标资源，startWindowBackground字段索引**resources > base > element** **> color.json**中的color。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/A3c_6H1rRsuaLnkwM1LsaA/zh-cn_image_0000002701823512.png)
5. 在**src > ohosTest > module.json5**文件的abilities数组中，加startWindowIcon和startWindowBackground字段。其中，startWindowIcon字段索引模块ohosTest下**resources > base > media**中的图标资源， startWindowBackground字段索引**resources > base > element** **> color.json**中的color。

## 编译报错“Schema validate failed”

**问题现象**

DevEco Studio编译时出现错误，提示“Schema validate failed”错误信息。

**解决措施**

出现该问题的原因是配置文件中字段缺失或拼写错误，可根据报错的详细信息进行问题定位。

如将module.json5文件中abilities标签中的“name”错写为“nam”，报错信息如下：

```txt
	 Detail: Please check the following fields.
{
  instancePath: 'module.abilities[0]',
  keyword: 'required',
  params: { missingProperty: 'name' },
  message: "must have required property 'name'",
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities[0]',
  keyword: 'required',
  params: { missingProperty: 'srcEntrance' },
  message: "must have required property 'srcEntrance'",
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities[0]',
  keyword: 'required',
  params: { missingProperty: 'name' },
  message: "must have required property 'name'",
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities[0]',
  keyword: 'oneOf',
  params: { passingSchemas: null },
  message: 'must match exactly one schema in oneOf',
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities[0]',
  keyword: 'enum',
  params: {
    allowedValues: [
      'priority',
      'name',
      'srcEntrance',
      'srcEntry',
      'launchType',
      'description',
      'icon',
      'label',
      'permissions',
      'metadata',
      'visible',
      'exported',
      'skills',
      'backgroundModes',
      'continuable',
      'startWindowIcon',
      'startWindowBackground',
      'removeMissionAfterTerminate',
      'orientation',
      'supportWindowMode',
      'maxWindowRatio',
      'minWindowRatio',
      'maxWindowWidth',
      'minWindowWidth',
      'maxWindowHeight',
      'minWindowHeight',
      'excludeFromMissions'
    ]
  },
  message: 'must be equal to one of the allowed values',
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities[0]',
  keyword: 'propertyNames',
  params: { propertyName: 'nam' },
  message: 'property name must be valid',
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
}
```

以上述报错为例，说明报错中关键词的含义，便于开发者理解报错信息，完成问题定位及修改。

* instancePath：错误所在的文件位置。'module.abilities[0]'表示在module.json5文件中的第一个abilities。
* keyword：标识当前报错字段的可选配属性，当前报错中包括'required'、'oneOf'、'enum'、'propertyNames'。
  + required：表示该字段为必选配置项。由于缺失或拼写错误导致该属性未配置。
  + oneOf：表示当前配置不符合oneOf要求。通过instancePath已经确认报错出现在abilities标签，在DevEco Studio中，按住Ctrl点击"abilities"跳转到对应的module.json文件，可以查看到必须配置以下两组中的一组。根据对比排查，可识别到因拼写错误导致"name"属性未配置。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/l5BAUkJDRFOViLwXMnI8Ng/zh-cn_image_0000002701663574.png)
  + enum：该标签内所有可配置的属性。开发者可根据枚举值确认属性的正确写法。
  + propertyNames：如果字段拼写错误将出现propertyNames，propertyName: 'nam'指明“nam”为错误属性。
* params：不同keyword对应不同的详细说明，如keyword为'required'时，params的missingProperty: 'name' 表示缺失的属性为“name”。
* message：修改要求的说明，如keyword为'required'时，message表示必须配置name属性。
* location：错误的具体位置，点击可以跳转。

## 编译报错“No available entry module found”

**问题现象**

DevEco Studio编译时出现错误，提示“No available entry module found”错误信息。

**解决措施**

feature模块中需要配置依赖的entry模块，DevEco Studio在编译时会校验feature模块所依赖的entry模块是否存在，出现该问题的原因可能为以下情况：

1. 在feature模块的build-profile.json5文件中，entryModules字段配置的名称与实际entry模块的名称不一致。请将entryModules字段的值修改为entry模块的名称；
2. 在项目级build-profile.json5文件的modules字段中，feature模块位于entry模块之前。由于DevEco Studio在进行编译时会按照从前往后的顺序进行配置，当配置feature模块时，尚未读取和配置entry模块，则会报entry模块不存在的错误。请在modules字段中将feature模块置于所依赖的entry模块之后。

## 编译报错“keystore password was incorrect”

**问题现象**

DevEco Studio编译时出现错误，提示“keystore password was incorrect”错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/kSOxOq9aRCefXHeZalN9Ag/zh-cn_image_0000002701823426.png)

**报错原因**

密钥库(p12)密码错误。

**注意** 

**密钥库密码**和**密钥密码**是在创建p12文件时由开发者自行输入的，请牢记该密码。DevEco Studio工程的build-profile.json5文件中有记录密码的密文，但签名工具需要输入密码明文，不能直接将build-profile.json5中的值用到签名工具中。

**常见场景**

1. 密码输入错误。
2. 命令行中需要输入真实密码，误输入了加密后的密码。
3. 密钥(keyAlias)密码和密钥库(p12)密码记混。

**解决措施**

出现该问题的原因是签名文件中签名密码错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/j04vjr4ZSi6pgai2ykhZZQ/zh-cn_image_0000002701823448.png)

开发者可通过重新自动签名解决该问题：

1. 点击**File > Project Structure > Project > Signing Configs**，打开签名配置页面。

2. 勾选“Automatically generate signature”，等待重新签名，然后点击**OK**即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/d8PfkVghTM-k7EVeztnf0A/zh-cn_image_0000002731382781.png)

## 编译报错“please check deviceType or distroFilter of the module”

**问题现象**

DevEco Studio编译时出现错误，出现如下提示之一：

* Module: (xxx) and Module: (xxx) are entry, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/G7dKvgyGTaaEz1nMhEdjLg/zh-cn_image_0000002731382807.png)
* Module: (xxx) and Module: (xxx) have the same moduleName, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/NBMpewzGQ0GT_6JK-35Udg/zh-cn_image_0000002701663564.png)
* Module: (xxx) and Module: (xxx) have the same packageName, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/BXVkVgeqR5qBQ9PC2itaMA/zh-cn_image_0000002731382797.png)
* Module: (xxx) and Module: (xxx) have the same ability name.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/GW_bi0EeRP-pP79EIHsLGw/zh-cn_image_0000002701823438.png)

**解决措施**

出现该问题的原因是打包时工程未满足HAP唯一性校验逻辑，请根据[HAP唯一性校验逻辑](ide-hvigor-verification-rule.md)修改工程，满足校验逻辑即可正常打包。

## 编译报错“Failed to generate test project build system”

**问题现象**

执行多模块native模块构建时，提示“Failed to generate test project build system.”错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/k0QEhMWyRuSPo3F9OfY0zQ/zh-cn_image_0000002701823496.png)

**解决措施**

请删除报错模块下的.cxx文件夹，然后选中需要构建的模块，执行**Make Module** **${moduleName}**完成单独构建，避免同时构建多个模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/QNgSvAApSmyDpwzdZeZkfw/zh-cn_image_0000002701663528.png)

## C/C++项目三方依赖库未打包入HAP

**问题现象**

C/C++项目依赖三方so时，在打包生成HAP后，发现三方so未打包到HAP中。

**解决措施**

当前DevEco Studio对C/C++项目三方so的寻址方式有限，如出现三方so未打包到HAP中，请尝试修改so引入方式。

1. 定义一个别名（如jsbind\_shared\_lib\_tracing），代表将要引入的三方so。
2. 使用SHARED IMPORT将三方so定义为动态引入。
3. 使用IMPORTED\_LOCATION定义引入so的具体位置。
4. 将定义的三方so声明给目标。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/yWmpBEX3T92K6oa6-mJfiA/zh-cn_image_0000002701823462.png)
5. 再次打包生成HAP，确认三方so是否打包到HAP中。

## Static Library模块中src/main/cpp目录下的文件未打包进HAR

**问题现象**

点击**Build > Make Module ${libraryName}**编译构建生成HAR后，发现构建产物中未出现cpp目录下的文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/GhdJ3O8eTUSn94mFVhXXDw/zh-cn_image_0000002701823500.png)

**解决措施**

如果使用的Hvigor为2.5.0-s及以上版本，在编译构建HAR的过程中，只会将dependencies内处于本模块路径下的本地依赖也打包进.har文件中，devDependencies里的依赖不会打包进.har文件中。

请将相应的本地依赖移至dependencies中后重新编译。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/JZ2lB4RUQ8uNH0RhlGB5aw/zh-cn_image_0000002701663536.png)

## 工程编译告警提示“ArkTS:WARN: For details about ArkTS syntax errors”

**问题现象**

工程构建时，提示“ArkTS:WARN: For details about ArkTS syntax errors, see FAQs”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/5r2vJRA8R3Sq-eDOe2_2BQ/zh-cn_image_0000002701663562.png)

**解决措施**

出现该告警说明当前工程存在不符合ArkTS语法规范的写法，请根据ERROR报错中括号内的语法规则如(arkts-no-var)，查看[从TypeScript到ArkTS的适配规则](typescript-to-arkts-migration-guide.md#使用let而非var)中对应的说明，修改为ArkTS规范写法。

## 编译报错“ninja: error: mkdir(xxx): No such file or directory”

**问题现象**

Native工程编译报错，同时出现以下告警和报错信息。

出现工程目录长度超过250字符的告警，示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/-7w5pTQFRQ6ngzv9ZywZcw/zh-cn_image_0000002731542769.png "点击放大")

出现编译报错“ninja: error: mkdir(xxx): No such file or directory”，示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/elKzXmWTRYiS6lAJnMg1_w/zh-cn_image_0000002731542759.png "点击放大")

**解决措施**

CMAKE\_OBJECT\_PATH\_MAX默认大小为250，如果工程中object file实际路径长度超出该大小，将导致编译报错。

开发者需要根据object file实际路径长度在工程CMakeLists.txt中设置CMAKE\_OBJECT\_PATH\_MAX大小，具体方法如下：

* 方法一： 通常在CMAKE\_OBJECT\_PATH\_MAX默认值基础上增加一个文件名长度即可。

  示例中告警文件为TextMeasureCache.cpp.obj，长度为24字符，在默认值250的基础上增加24，即设置set(CMAKE\_OBJECT\_PATH\_MAX 274)
* 方法二：根据object file实际路径长度计算CMAKE\_OBJECT\_PATH\_MAX大小。

  计算公式：CMAKE\_OBJECT\_PATH\_MAX = 总路径长度 - object file中目录部分长度 + cmake哈希值字符数（固定为32）

  + 总路径长度 = object file directory长度 + object file长度，object file directory、object file如下图所示，两个长度之和为297字符，以实际为准

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/1GN8UrsmSV2gfiMePq4VsA/zh-cn_image_0000002731542725.png "点击放大")
  + object file中目录部分长度：示例中“\_\_/\_\_/\_\_/\_\_/\_\_/third-party/rn/ReactCommon/react/renderer/textlayoutmanager”长度为74字符，以实际为准
  + cmake哈希值字符数：cmake将长路径转换为哈希值时哈希值的长度，固定为32

  代入示例中的长度后，计算可得：CMAKE\_OBJECT\_PATH\_MAX = 297 - 74 + 32 = 255，即设置set(CMAKE\_OBJECT\_PATH\_MAX 255)

## 编译报错“(is the command line too long?)”

**问题现象**

Native工程编译报错，同时出现以下告警和报错信息。

出现工程目录长度超过250字符的告警，示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/ZPbzivl3TdWhUgCDPj36Dw/zh-cn_image_0000002701823484.png "点击放大")

出现编译报错“(is the command line too long?)”，示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/yiHF-Y9KRpqBWOjtQoNwww/zh-cn_image_0000002731382801.png)

**解决措施**

CMAKE\_OBJECT\_PATH\_MAX默认大小为250，如果工程中object file实际路径长度超出该大小，将导致编译报错。

开发者需要根据object file实际路径长度在工程CMakeLists.txt中设置CMAKE\_OBJECT\_PATH\_MAX大小，具体方法如下：

* 方法一： 通常在CMAKE\_OBJECT\_PATH\_MAX默认值基础上增加一个文件名长度即可。

  示例中告警文件为TextMeasureCache.cpp.obj，长度为24字符，在默认值250的基础上增加24，即设置set(CMAKE\_OBJECT\_PATH\_MAX 274)
* 方法二：根据object file实际路径长度计算CMAKE\_OBJECT\_PATH\_MAX大小。

  计算公式：CMAKE\_OBJECT\_PATH\_MAX = 总路径长度 - object file中目录部分长度 + cmake哈希值字符数（固定为32）

  + 总路径长度 = object file directory长度 + object file长度，object file directory、object file如下图所示，两个长度之和为297字符，以实际为准

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/FMAg58STRuijXOUr3EeMrQ/zh-cn_image_0000002701823488.png "点击放大")
  + object file中目录部分长度：示例中“\_\_/\_\_/\_\_/\_\_/\_\_/third-party/rn/ReactCommon/react/renderer/textlayoutmanager”长度为74字符，以实际为准
  + cmake哈希值字符数：cmake将长路径转换为哈希值时哈希值的长度，固定为32

  代入示例中的长度后，计算可得：CMAKE\_OBJECT\_PATH\_MAX = 297 - 74 + 32 = 255，即设置set(CMAKE\_OBJECT\_PATH\_MAX 255)
* 方法三：若设置CMAKE\_OBJECT\_PATH\_MAX后，仍然报相同错误，需要修改工程存放目录，将其存放在较短的目录下。

  设置CMAKE\_OBJECT\_PATH\_MAX后，cmake会将长路径转换为32字符的哈希值以缩短路径长度，如果转换后的路径依然过长，只能缩短工程的存放路径。

## 编译报错“CMake Error: The following variables are used in this project, but they are set to NOTFOUND”

**问题现象**

Native工程中使用find\_path时出现以下报错信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/MaTVLMlyRNeYbxYu9eNX4A/zh-cn_image_0000002701663510.png "点击放大")

**解决措施**

OpenHarmony SDK提供的CMake交叉编译配置文件（ohos.toolchain.cmake）中，限制了搜索路径为CMAKE\_SYSROOT。

如果开发者需要添加搜索路径，可在CMakeLists.txt中使用list接口添加自定义路径，如将"D:demo"添加至搜索路径：

```txt
list(APPEND CMAKE_FIND_ROOT_PATH_MODE_INCLUDE "D:demo")
```

添加后，即可使用find\_path查找"D:demo"目录下的文件。

## 编译报错 “Unknown resource name”

* 场景一

**问题现象**

工程中模块A引用了模块B，编译模块A时出现错误，提示 "Unknown resource name 'xxxx'"，找不到模块B的资源。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/cMSyJKFjSGG38Et57UIYrw/zh-cn_image_0000002731542791.png "点击放大")

**解决措施**

请确保符合以下条件：

1. 资源需放置在目录resource/base路径下。
2. 模块B已安装。
3. 模块A中不能使用相对路径引用模块B的资源，应直接通过定义的模块名称来引用。

* 场景二

**问题现象**

引用模块的方式不对，如果引用的是一个其他模块的代码，也会报资源找不到。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/gxvJgZ2NSQ6BGuXmi0p6Pw/zh-cn_image_0000002701663552.png)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/Xn7f_p86SIKe47vTBcX14Q/zh-cn_image_0000002701823446.png)

**解决措施**

在oh\_package.json5中引入该模块。通过定义的模块名称来引用。

如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/85X8Mz-4TkGX_7VagJjhRw/zh-cn_image_0000002731382739.png)

* 场景三

**问题现象**

HSP A 申请了某个权限，这个权限进行了资源的引用，在所有依赖A的组件进行构建时，报错 A 引用的资源找不到。

**解决措施**

手动在引用方配置对应资源可以解决此问题。

## 构建报错“Task xxx was not found in the project xxx”

**问题现象**

命令行手动执行构建命令时，构建失败，提示“Task xxx was not found in the project xxx”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/rVuCNgf8QUib7nAZHjhF2Q/zh-cn_image_0000002701663546.png)**问题确认**

1. 执行hvigorw tasks命令，查看对应命令是否存在。
2. 查看对应工程中module.json5文件中“type”字段是否为命令执行模块。比如图中执行assembleHar命令，是对工程中的har模块进行打包，若module.json5文件中的“type”字段不是"har"类型，则会出现上述错误提示。

**解决措施**

1. 执行正确命令。
2. 查看对应工程中module.json5文件中“type”字段类型，执行对应命令。

## 编译报错“The reason and usedScene attributes are mandatory for user\_grant permissions”

**问题现象**

DevEco Studio编译失败，提示“The reason and usedScene attributes are mandatory for user\_grant permissions”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/oCOnJQhQR5q3vLJue73LdA/zh-cn_image_0000002701663586.png "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview2版本开始新增规则：APP包中，所有entry和feature hap的module下的requestPermissions权限清单必须指定(可以缺省为空，若非空则name必填,user\_grant权限则必填reason、usedScene字段)。

**解决措施**

进入对应module.json5文件中，补齐requestPermissions字段下的reason和usedScene字段。如以下示例：

```screen
"requestPermissions": [
  {
    "name": "ohos.permission.READ_IMAGEVIDEO",
    "reason": "$string:module_desc",
    "usedScene": {
      "abilities": [
        "EntryAbility"
      ],
      "when": "inuse"
    }
  }
]
```

## 编译报错“Only one default card can be configured in the form\_config.json file”

**问题现象**

DevEco Studio编译失败，提示“Only one default card can be configured in the form\_config.json file”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/t84CS0DqRyuPF2tV8LSKNA/zh-cn_image_0000002701823474.png "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview2版本开始新增规则：卡片的配置文件中isDefault不可缺省，每个UIAbility有且只有一个默认卡片。

**解决措施**

进入对应module.json5文件中，选择唯一默认卡片，将其他卡片的isDefault字段设置为false。

## 编译报错“In the form\_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty”

**问题现象**

DevEco Studio编译失败，提示“In the form\_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/B_rgVP1wTdKBzMRbzzIs3g/zh-cn_image_0000002731382755.png "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview2版本开始新增规则：卡片的配置文件中updateEnabled不可缺省，为true时可以在定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式任选其一，当两者同时配置时，定时刷新优先生效。

**解决措施**

进入对应module.json5文件中，按照需求，选择配置updateEnabled为false，或者增加定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式配置。

## 编译报错“The path XX is not writable. please choose a new location”

**问题现象**

在mac上，通过直接打开dmg中的DevEco Studio，构建报错 The path XX is not writable. please choose a new location.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/7mOpDnGcQca3_luATYis2g/zh-cn_image_0000002731542775.png)

**问题原因**

在mac上直接打开dmg 中的DevEco Studio，是会以只读的方式打开的，内置到DevEco Studio里面的文件是没有写权限的。

**解决措施**

将“DevEco-Studio.app”拖拽到“Applications”中，先安装再使用。

## 编译报错“Property 'XX' does not exist on type 'typeof BuildProfile'”

**问题现象**

本地HSP模块对外提供的接口中使用了HAP未定义的自定义参数BuildProfileFileds，且HAP引用了HSP中的该接口，导致编译失败，提示“Property 'XX' does not exist on type 'typeof BuildProfile'”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/if9GiNfiSx-UuZ3PAVKY0Q/zh-cn_image_0000002731542767.png)

**解决措施**

可采用以下两种方式解决该问题：

* 在HAP中配置与HSP相同的自定义参数BuildProfileFileds。
* 将与HSP相同的自定义参数BuildProfileFields配置到工程级build-profile.json5中，该方法会使HSP中的自定义参数在全局生效。

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

## 如何解决编译报错“ Error: 'icon' value `$media:icons` invalid value.”的问题

**问题现象**

编译报错“ Error: 'icon' value `$media:icons` invalid value”。

```txt
ERROR: Failed :entry:default@CompileResource...
ERROR: Tools execution failed.
Error: ref `$media:icons` don`t be defined.
Error: 'icon' value `$media:icons` invalid value.
at D:\project\process_profile\default\module.json
Detail: Please check the message from tools.
```

**报错原因**

引用的资源不存在时，编译报错指向的文件路径是build目录。

**常见场景**

1. 资源文件未添加。
2. 资源文件被意外删除。

**解决方案**

根据报错的资源id全局搜索，查看报错的资源是否存在。

## 如何解决编译报错“Error: cJSON\_Parse failed, please check the JSON file.”的问题

**问题现象**

编译报错“Error: cJSON\_Parse failed, please check the JSON file”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/Kw4SHdx_SVGVP7cHxybzDQ/zh-cn_image_0000002731382775.png "点击放大")

**报错原因**

module.json文件格式不正确。

**常见场景**

1. json文件内末尾多了逗号。

2. 根标签不是大括号{}。

**解决方案**

检查报错指向的json文件格式，比如是否末尾多了逗号，根标签是否为大括号{}。

## 如何解决编译报错“Error: the name 'XXX' can only contain [a-zA-Z0-9\_].”的问题

**问题现象**

编译报错“Error: the name 'XXX' can only contain [a-zA-Z0-9\_]”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/Nb8Xh8zsS8erikyd3Df_mA/zh-cn_image_0000002731542719.png)

**解决方案**

检查文件名是否合法，文件名只能包含大小写字母、数字、下划线。

## 如何解决编译报错“Cannot add xxxx items to index”的问题

**问题现象**

编译报错“Cannot add xxxx items to index”。

**问题原因**

被编译文件中某函数内部有大量object literal, array literal和string，导致item的数量超过了上限（65536）。

**解决方案**

排查相关文件，将存在上述原因的函数进行拆分。
