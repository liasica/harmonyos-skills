---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-faqs
title: 编译构建常见问题
breadcrumb: 指南 > 构建应用 > 构建报错排查 > 编译构建常见问题
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:073a18dabf93e932d382159641f6516779790d42eec8d6aca00f474c2038a4a7
---

## 如何解决编译过程内存过高

**问题现象**

编译构建时，内存或CPU占用过高，导致出现DevEco Studio运行卡顿、延迟等现象。

**解决措施**

* 在执行hvigor构建的过程中，通过减少内存中的缓存数据、减少线程数量，可以减少编译过程中的内存占用。

  可以在hvigor-config.json5中添加配置。

  ```
  1. "properties": {
  2. // 配置为0，表示不启用内存缓存配置，默认为4，数值越低，内存中缓存数据越少
  3. "hvigor.pool.cache.capacity": 0,
  4. // 默认配置为cpu核数-1， 包含ohos.arkCompile.maxSize，值越小，占用内存越少
  5. "hvigor.pool.maxSize" : 5,
  6. // 默认配置值为5, 值越小，占用内存越少
  7. "ohos.arkCompile.maxSize": 3,
  8. // 默认配置值为true, 表示开启内存缓存，占用内存较多，配置为false，关闭内存缓存，占用内存较少
  9. "hvigor.enableMemoryCache": false
  10. },
  ```

  说明

  当配置项"hvigor.pool.maxSize"和"ohos.arkCompile.maxSize"的值改小，"hvigor.enableMemoryCache"改为false后，可能会导致编译时长增加，请耐心等待。

* 如果以上修改没有取得明显的效果，可以使用非并行的模式来执行编译。
  + 在菜单栏点击“File > Settings（macOS为DevEco Studio > Preferences/Settings） > Build, Execution, Deployment > Build Tools > Hvigor”，取消勾选“Execute tasks in parallel mode (may require larger heap size)”。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/LtgALTwLSp2G6a5lLSNzig/zh-cn_image_0000002561833405.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=D21E6C95AE93499521412CEC00E5D30FFBDACCEA51E1761E6AF8F9A04E0F6A11)
  + 流水线场景中，在命令行最后增加 --no-parallel，示例：

    ```
    1. hvigorw assembleHap --no-parallel
    ```

  说明

  使用非并行模式编译，内存占用会减少，但可能会导致编译时长增加，请耐心等待。

## 构建报错“Cannot read properties of undefined(reading 'XXX')”

请先根据XXX的值从以下场景排查，没解决问题再参考最终方案。

* **场景一：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'setEnabled')”。

  **问题确认**

  hvigorfile.ts里有如下代码：

  ```
  1. import { hvigor, getHvigorNode } from "@ohos/hvigor"
  2. import { hapTasks} from '@ohos/hvigor-ohos-plugin';
  3. // 问题代码
  4. getHvigorNode(__filename).getTaskByName('XXX').setEnabled(false);
  5. export default {
  6. system: hapTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
  7. plugins: []         /* Custom plugin to extend the functionality of Hvigor. */
  8. }
  ```

  **处理措施**

  1. 确保XXX是当前的HvigorNode里存在的任务。

     假设是entry模块的hvigorfile.ts中的代码导致的问题 ，XXX的有效值就是下图中的“default@SignHap”、“default@CollectDebugSymbol”、“assembleHap”等值。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/ZaLpLjuNQgmFAIcEhnk-Yw/zh-cn_image_0000002561753579.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=E3E5B035561EA0041DD4FA747A006BBA634DFE8E547D0C3415B1D0A021926522)
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

  ```
  1. import { appTasks } from '@ohos/hvigor-ohos-plugin';

  3. export default {
  4. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  5. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
  6. }
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

  ```
  1. // 错误写法：空数组
  2. class w {
  3. public a: [][] = []
  4. test() {
  5. console.log("1", this.a[0])
  6. }
  7. }
  8. // 正确写法
  9. class w {
  10. public a: string[][] = []
  11. test() {
  12. console.log("1", this.a[0])
  13. }
  14. }
  ```
* **场景八：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'clear')”。

  **问题确认**

  在工程根目录hvigor/hvigor-config.json5文件中配置如下内容打开堆栈。

  ```
  1. "debugging": {
  2. "stacktrace": true                /* Disable stacktrace compilation. Value: [ true | false ]. Default: false */
  3. },
  ```

  确认堆栈内容是否如下。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/BMphr8dSRGqcwuyVkVDA3w/zh-cn_image_0000002561833453.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=0CCB89508C006B91A148DF11C77DE25ECB2B93BC5E78EAAAFC5AC8F33B5E744D)

  **处理措施**

  确认DevEco Studio是否有使用安全加固等三方插件。如果有，可以先禁用三方插件，看是否会复现问题，还能复现就参考下面的最终方案。
* **最终方案：**

  如果以上场景都不符合，打开堆栈后，根据堆栈信息排查代码。

  堆栈打开方法：工程根目录hvigor/hvigor-config.json5文件中配置如下内容。

  ```
  1. "debugging": {
  2. "stacktrace": true                /* Disable stacktrace compilation. Value: [ true | false ]. Default: false */
  3. },
  ```

  优先排查hvigorconfig.ts文件和hvigorfile.ts文件，其他代码次之。

  如果上述文件中并未排查出问题，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 构建报错“Duplicated files found in module xxx. This may cause unexpected errors at runtime”

**问题现象**

编译构建时，出现报错“Duplicated files found in module xxx. This may cause unexpected errors at runtime”。

问题原因是构建时存在不同版本的同名so文件。比如将har模块产物里的so文件拷贝到entry模块的libs目录下，这时har模块里有一个libhar.so，entry模块里也有一个libhar.so，再配置entry依赖har，构建entry就会出现报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/vGYWoXjuQAicMkw5P8G8LA/zh-cn_image_0000002530913588.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=2E0CB703800889BE8052A21B5DABAE7B6CCB7EDBFFC3E6580E8C18A3CE0CE365)

**解决措施**

使用select、pickFirsts、pickLasts等配置选中要使用的so文件; select提供native产物的精准选择能力，优先级高于excludes、pickFirsts等配置项。pickFirsts、pickLasts按照.so文件的优先级顺序，打包最高优先级的.so文件，优先级顺序是指依赖收集的顺序，越晚被收集优先级越高。

具体可参考：[配置CPP](ide-hvigor-cpp.md)。

基于上面的例子，可以在entry的build-profile.json5中添加配置select选中har模块中的so文件，package选中包名为“har”的模块, include选中“libhar.so”文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/jJYAixfDSzCSt9x6XYUbyw/zh-cn_image_0000002561753441.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=CDFF951BFDAAF2397242586A8B34866FB03C4FC24433975524B0A47B44E2A839)

## 构建报错“input module releaseType is different”

**问题现象**

打包APP时，提示“input module releaseType is different”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/py1ySuSGTm--hczgqKbMPw/zh-cn_image_0000002530913436.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=7DDAD4650961166AC4FEEED7BE9DC957A7DEBB58EF0C36B3036AD42298234D58)

**解决措施**

根据报错日志的Warning信息所提示的模块名称，检查模块间的apiReleaseType字段是否一致。

该apiReleaseType字段由编译构建工具自动生成，保存在HAP/HSP包的module.json文件中。如下图所示，首先确认各模块间该字段是否一致，如果存在不一致的情况，需要将应用的各个模块，使用相同版本的SDK重新打包，然后打包APP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/apIiTW1bThiaqYoKYGuAwA/zh-cn_image_0000002561833395.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=E9E6C9B91A339EE4A8263920923D909FC84DD5818D588C24D4B6C8C8050D4992)

## 构建报错“debug is different”

**问题现象**

打包APP时，提示“debug is different”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/T4VaKk_tRFeKJ_31jLYb_g/zh-cn_image_0000002561753545.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=02B158726942ABD0868C8938C18A5BC1C289F8B043BEC08BFDD0A9B7B57780DE)

**解决措施**

根据报错日志的Warning信息所提示的模块名称，检查模块间的debug字段是否一致，尤其需要关注本地模块和外部引用模块之间是否一致。

1.该debug字段由编译构建工具自动生成，保存在HAP/HSP包的module.json文件中，如下图所示，首先确认各模块间该字段是否一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/KMSMPmt0QGKp7naF68k0gA/zh-cn_image_0000002561753493.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=373187A157874D120D5C8F31B9AFA1FA7DAD27C7E540C449E49E343B0DF1A475)

2.编译工具根据设置的Build Mode选项生成debug标识，如图所示，可以通过此处进行设置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/F1N2GKxrTouA-T9oipeHWA/zh-cn_image_0000002530913508.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=A757B6A88C9BA8972ADEF56F8AFD648A1F2242E13501C36EE64E532C7E79CBBF)

## 构建报错“proxy data is duplicated”

**问题现象**

打包APP时，提示“uri datashareproxy://bundleName/\*\* in proxy data is duplicated”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/L_j7hrxSTFS8no_IX42IhA/zh-cn_image_0000002530913600.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=85D158001DD4083CFC624465882F7D05B8A4219727B587B78F01A3747425E1EB)

**解决措施**

proxyData标识模块提供的数据代理列表，只允许entry和feature配置，不同的proxyData中配置的URI不可重复。遇到此问题，检查模块间是否配置了相同uri的proxyData。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/26JxTBxBQwKuD7gwblLbYg/zh-cn_image_0000002530753584.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=198AC10076EAFDB925A7E057B34C7B5F156538311595EBC79B42CB6A03E52EE3)

## 编译报错“Init keystore failed: parseAlgParameters failed: ObjectIdentifier()”

**问题现象**

编译构建时，出现错误：Init keystore failed: parseAlgParameters failed: ObjectIdentifier()。

```
1. hap-sign-tool: error: ACCESS_ERROR, code: 109. Details:   Init keystore failed: parseAlgParameters failed: ObjectIdentifier() -- data isn't an object ID (tag = 48)   Detail: Please check the message from tools
```

**错误原因**

使用高版本JDK生成密钥对(p12)，再使用低版本的JDK执行签名命令时，会因为不兼容导致解析p12失败，从而签名失败。

**场景**

1. 使用DevEco Studio生产密钥对时，DevEco Studio默认会调用软件内预置的JDK17，而用户使用本地的低版本JDK进行签名时则会报错。
2. 用户本地使用高版本JDK生成密钥对时，又通过DevEco Studio进行签名，DevEco Studio中预置的JDK17版本低于用户的JDK，导致报错。

**解决方案**

请检查当前使用的JDK版本和生产密钥对使用的JDK版本，使用版本匹配的JDK执行签名命令。

## 编译报错“generate SignerBlock failed”

**问题现象**

编译构建时，出现错误：message:generate SignerBlock failed。

```
1. hap-sign-tool: error: {errorcode:0,message:generate SignerBlock failed}
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

```
1. hap-sign-tool: error: ACCESS_ERROR, code: 109. Details: java.io.IOException: DerValue.getOID, not an OID 49 Detail: Please check the message from tools
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/hEipbLDHTTmko848lt4D8A/zh-cn_image_0000002530753618.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=B23507ABFEE80F720E09039EA87A84C34D0504918427C506A2243F4E427282C4)

**解决措施**

出现该报错的原因是Hvigor运行时内存不足，在使用3.1.0及以上版本的Hvigor时，可通过以下方式修改Hvigor运行时内存的最大值。

勾选Enable the Daemon for tasks：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/7VSKP7uCTIamlASgVlR3-A/zh-cn_image_0000002530913606.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=47E5BC30D9839AC3684FC09B4095E44FAEA217F5FF019ABB910DF2471C827813)

在hvigor-config.json5中修改maxOldSpaceSize字段，根据工程的大小，适当将其增大（如设置为8192）：

```
1. "nodeOptions": {
2. "maxOldSpaceSize": 8192
3. }
```

## Linux环境下编译报错“JS heap out of memory”

**问题现象**

在Linux环境下，系统内存有64G，Hvigorw脚本中配置--max-old-space-size=40960，在编译构建时，实际在使用内存未达到配置的内存（例如使用到20G左右）就出现报错“JS heap out of memory“。

```
1. FATAL ERROR: NewSpace::Rebalance Allocation failed - JavaScript heap out of memory
2. Writing Node.js report to file: report.20200512.172528.47517.24.011.json
3. Node.js report completed
4. 1: 0xa295e0 node::Abort() [node]
5. 2: 0x9782df node::FatalError(char const*, char const*) [node]
6. 3: 0xb99c2e v8::Utils::ReportOOMFailure(v8::internal::Isolate*, char const*, bool) [node]
7. 4: 0xb99fa7 v8::internal::V8::FatalProcessOutOfMemory(v8::internal::Isolate*, char const*, bool) [node]
8. 5: 0xd3a3b5 [node]
9. 6: 0xd74f27 [node]
10. 7: 0xd84707 v8::internal::MarkCompactCollector::CollectGarbage() [node]
11. 8: 0xd481b9 v8::internal::Heap::MarkCompact() [node]
12. 9: 0xd48f0b v8::internal::Heap::PerformGarbageCollection(v8::internal::GarbageCollector, v8::GCCallbackFlags) [node]
13. 10: 0xd499a5 v8::internal::Heap::CollectGarbage(v8::internal::AllocationSpace, v8::internal::GarbageCollectionReason, v8::GCCallbackFlags) [node]
14. 11: 0xd4aebf v8::internal::Heap::HandleGCRequest() [node]
15. 12: 0xcf5f97 v8::internal::StackGuard::HandleInterrupts() [node]
16. 13: 0x104b803 v8::internal::Runtime_StackGuard(int, unsigned long*, v8::internal::Isolate*) [node]
17. 14: 0x13a5a99 [node]
18. Aborted (core dumped)
```

**问题原因**

vm.max\_map\_count是一个与内核虚拟内存子系统相关的参数，用于控制进程可以拥有的内存映射区域的最大数量。它通常用于限制一个进程可以打开的文件数量，特别是在使用大量内存映射文件的情况下。

在Linux系统上，vm.max\_map\_count参数的默认值通常是较小的数值，例如65530。然而，对于一些需要大量内存映射的应用程序或者特定的使用场景，可能需要增加该参数的值，以便支持更多的内存映射区域。

**解决措施**

修改vm.max\_map\_count的值：

* 临时修改：

  ```
  1. sysctl -w vm.max_map_count=新值
  ```
* 永久修改：如果希望永久修改参数的值，可以编辑/etc/sysctl.conf文件，并添加或修改以下行：

  ```
  1. vm.max_map_count=新值
  ```

  保存文件后，使用以下命令使更改生效：

  ```
  1. sysctl -p
  ```

## 编译报错“Cannot find module XXX or its corresponding type declarations”

* **场景一：**

  **问题现象**

  Stage模板工程编译引用native文件(.so) 提示 "Cannot find module XXX or its corresponding type declarations."。

  **处理措施**

  当前Stage工程在编译构建阶段新增对native文件(.so)导出符号的语法校验，如果引用了没有对应声明文件(.d.ts)的native文件(.so)的现有工程在编译构建阶段，语法校验工具便会报错提示找不到对应的声明文件。

  如果出现类似问题，可尝试通过如下方式进行解决：

  1. 在对应cpp目录下新建types/libxxx目录，并在该目录下新增index.d.ts用于声明native的类型符号；新增oh-package.json5配置文件用于校验工具的模块查询。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/OajHPSQCQrSX3z-8-wMvyA/zh-cn_image_0000002530753632.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=33D5D6A096F1CDF0227D90456D224B08550E8F20B058694F31ADDE4AEE12867E)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/jkco-EGYQmyspeSJ79_9lw/zh-cn_image_0000002561753499.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=87357D298298C8B223BA83E16A6ABE2FE1F097137B538C4EA69373F371EC8808)
  2. 在native引用的模块内的oh-package.json5中添加native模块的本地依赖，并根据提示点击**Sync Now**同步工程，下图以entry模块引用native模块为例。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/om3s7KHwT46HWvXWgchAmg/zh-cn_image_0000002561753377.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=5428FF2E972A916B57C57ADE79AC6E4BB39811CAAD7F9D68184E9A504CEBC6CD)

* 场景二：

  **问题现象**

  引用三方包，构建失败，提示“Cannot find module 'xxx' or its corresponding type declarations”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/LIh-zKfoSfStSsZyeRzruQ/zh-cn_image_0000002530913592.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=9121753F68C87ADE2475EE5A4249A9CE86BF09A55080F5F756D41DE421BBBA77)

  **处理措施**

  进入对应模块级oh-package.json5文件或工程级oh-package.json5文件中查看三方包是否已安装，若未安装，需执行ohpm install安装；若已安装，需查看“main”字段是否配置正确，若未配置或配置错误，需配置为正确的入口文件。
* 场景三：

  **问题现象**

  引用的包路径被混淆，代码中又是在引用包后面拼接了路径，导致模块引用不到而报错。

  例如：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/5YKNVHUJRdG3PG3ohRFp-g/zh-cn_image_0000002530913538.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=D25D59C66D90BA70C12A864216BB0F188182F64FBD95B126C7C35D2F4B5656B5)

  代码中这样引用

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/GRxOQH7ZSp-G6fByrNGAyg/zh-cn_image_0000002561753487.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=ADC654283C90E95CA43F3DB9DCF12485468AB5D1012554E6ABB19684FB7A23DE)这样引用会找不到模块，导致报错。

  **处理措施**

  修改引用方式，改为推荐的引用方式

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/ouEuUKu-THGs49HFNVivwQ/zh-cn_image_0000002561753379.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=C3F2F75278F562703617503A26C8A63BF084C8AECAAE444A5F9BD957D8B510B9)
* 场景四：

  **问题现象**

  被引用模块oh\_package.json5配置有误，执行了ohpm install 并且成功地安装了依赖，但是还报错模块找不到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/wqSqemtETOi38GYFZNwyww/zh-cn_image_0000002530753476.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=A6A0ED01C6FC2A78E09885C6D57ED5309D3858614CCF8C12D63C173C54083C52)

  被引用模块的 oh\_package.json5 中配置了错误的types字段。

  该字段优先于main字段。 如果 types 字段配置的不存在，就会报错模块找不到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/Tk_x7mzIRKyWSpGmhfZUyQ/zh-cn_image_0000002561753543.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=7B6668755AE30E1624937BB4D9AC289EDFCE27D431DCD4F87EB4C2E61CE659FE)

  **处理措施**

  如果该包中没有d.ets声明，则这个字段可以删除。配置不存在或者错误，会导致报错。
* 场景五：

  **问题现象**

  oh\_package.json5 中 dependencies 中引入模块的 名称 和 实际使用时 import 的 不一致。

  例如 在 oh\_package.json5 中这样引入：

  ```
  1. "dependencies": {   "har": "file:../har" }
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/iXeyK6wYQ0CpTpwePHsz8A/zh-cn_image_0000002530753616.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=4653688F6571AA166E3B20AF248520B177E39B0D42F3410166ECB55F0398A981)

  **解决措施**

  该问题是由于工程引用了无对应实现文件的.d.ts声明文件：

  1. 通过在build目录中搜索'rollup\_plugin\_ignore\_empty\_module\_placeholder'，找到报错的中间文件，并根据中间文件找到对应工程文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/4-mu8BWdQviKIpJnYJewqg/zh-cn_image_0000002530753462.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=3F70737E793A0A66336B93C95A9B7A6408027274920D461D3F6EC08104DDDA56)

     在输入栏中输入rollup\_plugin\_ignore\_empty\_module\_placeholder，找到问题模块的中间文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/eoKVH47cTju2POGyosIEUA/zh-cn_image_0000002530753638.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=CE786E7C3A7CA0969C8D8A8049CB0A4639EB27FA85BFD1787B697A248E1932E2)
  2. 在引用类型文件中通过添加type显式声明符号类型引用：

     ```
     1. export type {T} from './type';
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/B0uTk5jJSwiNZDrpXDA4Xg/zh-cn_image_0000002530913604.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=746189A65737C36F0ED38DA6E7D49CBA2BCD3CD8B8F4307DF2E7DA9EFC25D2C0)
  3. 同时排查是否从d.ts/d.ets中引用值类型符号，禁止在声明文件中声明值变量。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/HEoxS8YbS-6x8YDmyiUzWg/zh-cn_image_0000002561833401.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=D36CD7F1B583FF693012D8C23039241EE8C936BF0EBD4F41936148244C32C0EF)

## 编译报错“Module 'xxx' has no exported member 'yyy'”

**问题现象**

Stage模板工程编译构建失败，提示 "Module 'xxx' has no exported member 'yyy'" 并且"yyy"符号是由export \* from 'x.js'语法从js文件中导出。

**处理措施**

当前Stage工程编译构建期的语法校验工具对js文件不作检查，因此当使用export \* from 'x.js'导出js文件中的符号时，符号引用处便会提示"Module 'xxx' has no exported member 'yyy'"的错误信息。

如果出现类似问题，可尝试通过如下方式进行解决：

* 方法1（推荐使用）： 使用符号显式导出语法，从js文件中re-export符号 。

  ```
  1. export { yyy } from 'x.js'
  ```

* 方法2：新增x.js对应的声明文件(.d.ts)，并在引用时不指定后缀。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/kIYKmzk3TOuZ-1g3hTKC4Q/zh-cn_image_0000002530913584.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=572DD9EB259A07AEB97A27B49E864BFD849D76D1182E1E16FA34A608891ADE57)

## 编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”

**问题现象**

Stage模板工程编译构建失败，提示 "ERROR: Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/B4waNTFJQIW_4GAX1UVOwg/zh-cn_image_0000002530913510.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=EB1AC136B280689D11CB2561D4A99298CACB80E2FE621841A1B579375EB39D53)

**处理措施**

该问题是由于file1为当前工程外的代码：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/tkk2LihnTaGLHJGre0nOpQ/zh-cn_image_0000002561753503.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=3AB2F8ECA349C0C5F3946DABABC883FC44140A3427B7FD8DFA0DCAB2F687D0C1)

请新建Static Library模块，并将工程外的代码迁移至Static Library模块内，并使用HAP引用HAR方式进行模块间引用。

## 编译报错“Failed to get a resolved OhmUrl by filepath xx”

* **场景一：**

  **问题现象**

  三方包在配置依赖时，配置到devDependencies，源码中又有引用依赖中的API时，编译失败。如以下示例：三方包@hms-security/ucs-appauth将依赖@network/gr配置在devDependencies中，源码中使用了@network/grs的API时，编译失败，提示“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/enCIo6zzQfWa6l5MFbaQcw/zh-cn_image_0000002561833415.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=D061F88A37EE1D5478E2439BB7067DCBF9E232F1CF88D9293F19D9E74CB6A996)

  **问题确认**
  1. 进入上面报黄色的源码文件中，可以看到依赖有红色告警信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/NomGXe2VTLaKyRRaBZT3ew/zh-cn_image_0000002561833413.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=2D26E140AC0A367EA15AD2B6C7844C4EA4466BEC64B0F6E2EBC3B64684A29A2E "点击放大")
  2. 进入包下的oh-package.json5文件，查看依赖配置为devDependencies。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/HTtpAE8QQvSPngyw5aQzXQ/zh-cn_image_0000002561753569.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=74D3B0F0E5606D65709D09EF9315B0F2CC0224E6E456EC5FF9B239053ACBD5AB)

  **处理措施**
  + 向此包开发团队提改进建议：运行时的依赖，不能配置在devDependencies中。
  + 可在依赖上层引入对应devDependencies中的三方包规避此问题。

* **场景二：**

  **问题现象**

  DevEco Studio编译失败，提示“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/V_2QjMxlQhmEmFhEs4AMHA/zh-cn_image_0000002530753458.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=AA5A5FE9B3C9559BAE48EB04A2A60185CCBF26DAA941709BD55A3DD1F4AC39D0)

  **问题确认**

  查看工程目录下的build-profile.json5文件中modules字段配置的srcPath路径是否与真实路径不相同，是否存在大小写不一致问题。

  **处理措施**

  将工程目录下的build-profile.json5文件中modules字段配置的srcPath路径与真实路径保持一致。
* **场景三：**

  **问题现象**

  工程A以相对路径引用了工程B的模块，这种引用会导致报错。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/6gtOZqkwR-Oj-j7l1CsbJQ/zh-cn_image_0000002561753419.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=3A0CED7052516DB78FB09267DE88D6055BBC5C3A1259083B70C12270B94E8536)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/1RVS7MUFTkeA4Wvv_jTt3w/zh-cn_image_0000002561753391.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=DC21B5828E3B215F8AB57E051B14986294D75CF7EA9FAA7206481FE8FF5879FA)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/uyPesFugTwyU-ggyzJw-zg/zh-cn_image_0000002530913626.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=689BEF5375084E2170D54B04036FE489D36D5FDEFEF69D1222BCD2C668490928)**处理措施**

  + 把工程B这种的har转至工程A里，作为A的一个模块引用。
  + 把工程B的har提前打包，在A中 以.har的方式引用。
  + 上传到仓库，以版本号的方式引用。
* **场景四：**

  **问题现象**

  DevEco Studio编译失败，提示“Error Message: Failed to get a resolved OhmUrl for 'hvigor\_ignore\_xxxxx' imported by xxx”。

  **处理措施**

  如果hvigor\_ignore\_xxxxx所在的模块是一个har模块，需要排查oh\_package.json5中是否存在"packageType": "InterfaceHar"，如果存在，请删除"packageType": "InterfaceHar"。
* **场景五：**

  **问题现象**

  DevEco Studio编译失败，提示“Failed to get a resolved OhmUrl for 'xxx' imported by 'yyy'”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/9u1VjQZPTNOu-bAui4tPhA/zh-cn_image_0000002561833367.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=CFF5A798C4092A2A6DFD8768035D9A44DBC4358F4CA46FF074136C34E1DC1AA5 "点击放大")

  **问题确认**

  1. 排查yyy所在模块是否为[字节码har](ide-hvigor-build-har.md#section16598338112415)，查看工程级build-profile.json5的useNormalizedOHMUrl是否为true（缺省默认值为false），如果为true则默认构建字节码har。
  2. 如果yyy所在模块是字节码har，请排查xxx依赖是否被配置在工程级oh\_package.json5的dependencies，但没有配置在yyy模块级oh\_package.json5的dependencies中。

  **处理措施**

  + 将xxx依赖配置到yyy模块oh\_package.json5的dependencies中。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/aVFuHZNpQVGi9hADk97r1Q/zh-cn_image_0000002530753636.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=CDC5E2D749232CD7294F1A7DC2D7A61EE1BB1B547EC8B22176FA8312A55D9298 "点击放大")
  + 将yyy模块改为非字节码har，在模块级build-profile.json5文件中添加byteCodeHar字段并设置为false。

    ```
    1. "buildOption": {
    2. "arkOptions": {
    3. "byteCodeHar": false
    4. }
    5. }
    ```
* **场景六：**

  请确认当前使用的DevEco Studio和SDK版本是配套的，点击菜单栏**Help > About DevEco Studio**，**Help > About HarmonyOS SDK**分别查看配套的DevEco Studio和SDK版本。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/aooI8CWCQhOn2x5fUW-B4g/zh-cn_image_0000002561753449.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=A76F1632027C9EEE4494F9DE1A49BFE0AD5618D723015F1EE9EB715E041E82D7)
* **场景七：**

  **问题现象：**

  DevEco Studio编译失败，提示 "ERROR: ArkTS:ERROR failed to execute es2abc ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx"。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/yrX0KDbrQKeXvDdx8GV7ag/zh-cn_image_0000002530913528.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=34DE6AD0722455F9DAB1CE3E09C469C0DAE5647F54E122B108758B934C032AD7)

  **处理措施**

  该问题是由于在工程中引用了非工程标准模块目录（即目录内无模块描述文件module.json5），如下图utils目录所示：请新建Static Library模块，并将utils/common里面的代码迁移至Static Library模块内，并使用HAP引用HAR方式进行模块间引用。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/s7TIZoKXRl-Tf7_SkoGOFA/zh-cn_image_0000002530913504.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=E73DA8667ED43240589FBBBD57B0CDA53B14CCE66305DE757433FF7798237245)

## 编译报错“Property xxx does not exist on type 'typeof BuildProfile'.”

**问题现象****1**

使用了自定义参数BuildProfile，编译态无异常但编译构建失败，提示“Property xxx does not exist on type 'typeof BuildProfile'.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/-amwEo86QSmIKMxL27WPFA/zh-cn_image_0000002530753594.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=6325C97BAF19A490EBE23636B505BC203E1886717D1BCC68EB6078E77562622F)

**处理措施**

检查在当前模块下build-profile.json5中的targets > buildProfileFields配置的自定义参数中key值是否相同，如果不同请将targets内所有buildProfileFields中的key值保持相同。

以下为导致编译报错的**错误**配置示例：

```
1. "targets": [
2. {
3. "name": "default",
4. "config": {
5. "buildOption": {
6. "arkOptions": {
7. "buildProfileFields": {
8. "targetName": "default"
9. }
10. }
11. }
12. }
13. },
14. {
15. "name": "default1",
16. "config": {
17. "buildOption": {
18. "arkOptions": {
19. "buildProfileFields": {
20. "targetName1": "default1"
21. }
22. }
23. }
24. }
25. },
26. ]
```

请将targets内所有buildProfileFields中的key值修改一致，如以下示例：

```
1. "targets": [
2. {
3. "name": "default",
4. "config": {
5. "buildOption": {
6. "arkOptions": {
7. "buildProfileFields": {
8. "targetName": "default"
9. }
10. }
11. }
12. }
13. },
14. {
15. "name": "default1",
16. "config": {
17. "buildOption": {
18. "arkOptions": {
19. "buildProfileFields": {
20. "targetName": "default1"
21. }
22. }
23. }
24. }
25. },
26. ]
```

**问题现象2**

使用了自定义参数BuildProfile并且编译器标红且构建失败，提示“Property xxx does not exist on type 'typeof BuildProfile'.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/CjNQq6aeRJOpBKHULRLOrg/zh-cn_image_0000002561753461.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=094080D2BDA840A2E1E72C197BF40BA6F9265EEA91A347758FFDE950B5697D8D)

**处理措施**

请检查当前模块下build-profile.json5中buildProfileFields内是否添加了所使用的自定义参数，请确保该自定义参数已配置在buildProfileFields内。

## C++工程编译导致电脑卡顿的处理建议

**问题现象**

在执行代码规模较大的C++工程的编译时，由于C++编译时的CPU占用率较高，可能出现电脑卡顿、反应迟缓等现象。

**处理措施**

如果出现类似问题，可尝试通过如下方式进行解决：

打开模块下的build-profile.json5文件，在**arguments**参数中添加如下配置。并根据电脑CPU配置，修改compile和link的值。建议compile和link的值之和，设置为CPU核数的一半，如CPU为8核，则compile和link分别设置为2。

```
1. "arguments": "-DCMAKE_JOB_POOL_COMPILE:STRING=compile -DCMAKE_JOB_POOL_LINK:STRING=link -DCMAKE_JOB_POOLS:STRING=compile=2;link=2",
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

```
1. cmake_minimum_required(VERSION 3.10)
2. project(MyProject)
3. set(CMAKE_CXX_STANDARD 17)
4. include_directories(${CMAKE_CURRENT_SOURCE_DIR}
5. ${CMAKE_CURRENT_SOURCE_DIR}/include)
6. # 添加所有源文件
7. add_library(myProgram SHARED main.cpp myLibrary.cpp)
```

2. 确认源文件的符号定义。

确保在所有相关的源文件中正确定义了符号。例如，检查 myLibrary.cpp 是否包含 myFunction 的定义：

**myLibrary.cpp**

```
1. #include "myLibrary.h"
2. void myFunction() {
3. // Function implementation
4. }
```

**myLibrary.h**

```
1. #ifndef MY_LIBRARY_H
2. #define MY_LIBRARY_H
3. void myFunction();
4. #endif
```

3. 检查编译和链接顺序。

确保所有源文件和库文件按照正确的顺序进行编译和链接。CMake 和 Ninja 通常会处理这个问题，但在手动编译时可能会出现问题。

4. 清理和重新生成构建文件。

有时，构建文件可能会损坏或丢失符号定义。尝试清理构建目录并重新生成构建文件：

```
1. hvigorw clean 1
```

或手动删除模块下.cxx目录。

5. 检查库路径和链接器标志。

如果使用三方库，确保 CMakeLists.txt 中正确配置了库路径和链接器标志。例如：

```
1. cmake_minimum_required(VERSION 3.10)
2. project(MyProject)
3. set(CMAKE_CXX_STANDARD 17)
4. # 确保添加三方库的头文件
5. include_directories(${PATH_TO_EXTERNAL_LIBRARY}
6. ${PATH_TO_EXTERNAL_LIBRARY}/include)
7. # 添加源文件
8. add_library(myProgram SHARED main.cpp myLibrary.cpp)
9. # 链接三方库
10. target_link_libraries(myProgram PUBLIC /path/to/external/library)
```

6. 启用详细编译和链接输出。

为了解详细的编译和链接过程，可以启用更详细的输出。在 CMakeLists.txt 中添加以下内容：

```
1. set(CMAKE_VERBOSE_MAKEFILE ON)
```

7. 检查 Ninja 输出日志。

Ninja 默认生成 .ninja\_log 文件，其中包含构建过程的详细信息。您可以检查这个日志文件以了解构建过程中的问题。

```
1. cat {module}/.cxx/default/default/arm64-v8a/.ninja_log
```

检查编译日志中是否存在符号所在的源文件或头文件。

8. 使用 nm 工具检查符号。

使用 nm 工具检查目标文件和库文件中的符号，确保符号定义存在。

可使用sdk中内置的nm工具：sdk/default/openharmony/native/llvm/bin/llvm-nm。

**检查目标文件**

```
1. nm myLibrary.o | grep myFunction
```

**检查三方库文件**

```
1. nm /path/to/external/library | grep myFunction
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

   ```
   1. // main.cpp
   2. #include "myLibrary.h"
   3. int main() {
   4. MyType obj;
   5. // 使用自定义类型
   6. return 0;
   7. }

   9. // myLibrary.h
   10. #ifndef MY_LIBRARY_H
   11. #define MY_LIBRARY_H
   12. class MyType {
   13. public:
   14. MyType() {}
   15. void doSomething();
   16. };
   17. #endif
   ```
2. 检查头文件路径。

   确保 CMakeLists.txt 中正确设置了头文件的搜索路径。可以通过 include\_directories 添加头文件目录。

   **示例 CMakeLists.txt：**

   ```
   1. cmake_minimum_required(VERSION 3.10)
   2. project(MyProject)
   3. set(CMAKE_CXX_STANDARD 17)
   4. # 添加头文件目录
   5. include_directories(${CMAKE_SOURCE_DIR}/include)
   6. # 添加源文件
   7. add_library(myProgram SHARED src/main.cpp src/myLibrary.cpp)
   ```
3. 清理和重新生成构建文件。

   有时，构建文件可能会损坏或丢失符号定义。尝试清理构建目录并重新生成构建文件：

   ```
   1. hvigorw clean
   ```

   或手动删除模块下.cxx目录。
4. 启用详细编译输出。

   为了解详细的编译过程，可以启用更详细的输出。在 CMakeLists.txt 中添加以下内容：

   ```
   1. set(CMAKE_VERBOSE_MAKEFILE ON)
   ```
5. 检查编译输出日志。

   Ninja 默认生成 .ninja\_log 文件，其中包含构建过程的详细信息。你可以检查这个日志文件以了解构建过程中的问题。

   ```
   1. cat .cxx/default/default/arm64-v8a/.ninja_log
   ```
6. 使用 CMake 的 message 函数调试。

   可以在 CMakeLists.txt 文件中添加 message 函数来打印一些调试信息，以确保路径和变量正确设置。

   **示例：**

   ```
   1. message(STATUS "Source directory: ${CMAKE_SOURCE_DIR}")
   2. message(STATUS "Include directories: ${CMAKE_INCLUDE_PATH}")
   ```
7. 如果报错接口是系统API，请查阅对应API参考的起始版本，确认接口在当前版本是否可用。

**结论**

通过上述步骤，您可以定位和解决 unknown type name 问题。在使用 CMake、Ninja 和 LLVM 编译 C++ 项目时，确保所有头文件正确包含并设置正确的头文件路径是关键。如果问题依旧存在，详细的编译输出日志通常能提供更多线索，帮助您找到具体的原因。

## JDK版本不匹配导致编译失败

**问题现象**

通过命令行方式构建HarmonyOS应用或元服务过程中出现构建失败，现象如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/QFfTdsZFSgCz47WY0DPrRQ/zh-cn_image_0000002530753464.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=62FDAF8BB075CDBE4161EE1E5A33D3FC76AF5F52974F2ABD23479B99B0FF4C3D)

**解决措施**

该问题是由于JDK版本不匹配导致，当前配套的版本为JDK 17。因此，请根据如下方法进行修正：

1. 下载并安装JDK 17版本。
2. 修改JAVA\_HOME环境变量，取值修改为JDK 17。如果是Linux系统，可参考使用命令行方式构建元服务或应用的[配置JDK章节](ide-command-line-building-app.md#section195447475220)。

## LABEL\_VALUE\_ERROR处理指导

**问题现象**

在工程同步、编译构建过程中，提示**LABEL\_VALUE\_ERROR**错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/jaqKUk9_RDul8oSDMeFgIg/zh-cn_image_0000002561753497.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=3D365FAF7F56702A90D586B28338E9BC3E90BF322835ED248C6284C5646FC3C3)

**解决措施**

该问题是由于config.json文件的资源引用规则变更导致，需要将“label”字段的取值，修改为资源引用方式。

1. 在**resources > base > element**中的string.json中添加对应的字符串信息。
2. 然后在config.json中重新引用该字符串资源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/mlECaapSSNyERjsKfDPG5Q/zh-cn_image_0000002561833409.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=E0D50B64B5C7D02BD71B574566DDFAA8BA8AADCF704D174698099F4A5C50B5BE)

## 应用/元服务的启动界面信息缺失，提示"Schema validate failed"报错

**问题现象**

在工程同步或者编译构建时出现错误，提示“Schema validate failed”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/2fgRUr5AQ-inbfShtRa0zA/zh-cn_image_0000002561833537.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=BD6905CB7BBF90D93CF65D65FDDE6F4C9634C1D383D2BCDF150051137118C833)

**解决措施**

在开发应用/元服务时，可以设置应用/元服务的启动界面的图标及背景颜色，创建工程后自动设置了默认的启动界面信息，但若开发者误删其中某个字段后将导致报错。下面以重新设置启动界面信息为例，开发者可自定义启动界面的图标及背景颜色。

在开发应用/元服务时，为了提升应用/元服务冷启动的性能，您可以通过如下方式设置应用/元服务的启动界面的图标及背景颜色。

1. 在模块下的**resources > base > element**下，点击右键选择**New > Element Resource File**创建资源文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/SxckBGjZRbe7jesEXxMxzg/zh-cn_image_0000002561833373.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=D217E1D98CB686788EAF4CD312861A0790F0255D71EC87B437C2A0639315A333)
2. 在弹出的对话框中，“File name”开发者可自定义，如color；“Root element”请选择**color。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/1nTrF5TARXWNs-rwkcOAfw/zh-cn_image_0000002561753527.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=1C225BE8F8333697E4EED5D73EA1172128FA940D02227B251F398AEEB461B9B1)

   创建完成后，color.json文件如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/9mhNp4nWRLGh16lWwzao-w/zh-cn_image_0000002530913428.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=229BC527CF66A8ED72B21D06345D470D54CC30B26D4AC2317631F94E20C34199)
3. 将[2](ide-hvigor-faqs.md#li124901748185712)创建的color.json文件拷贝至模块的**ohosTest > resources > base > element**目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/qZFS9OhwRAea9r8OWJ1PDg/zh-cn_image_0000002561833349.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=ADE9319E231B4C44E14DBD2BA36E9838F7CD95BB82F975BBA4CBD5113A5382C9)
4. 在模块的**src > main > module.json5**文件的abilities数组中，添加startWindowIcon和startWindowBackground字段（若缺少任一字段，将出现ERROR: Schema validate failed报错）。其中，startWindowIcon字段索引模块下**resources > base > media**中的图标资源，startWindowBackground字段索引**resources > base > element** **> color.json**中的color。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/NnXDZ7C6TZOQXfzRO3o-9g/zh-cn_image_0000002561833385.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=0204FBC296C2A6FB514A1BD3AFAB1763838B78E930F01E406560C842F7814C70)
5. 在**src > ohosTest > module.json5**文件的abilities数组中，加startWindowIcon和startWindowBackground字段。其中，startWindowIcon字段索引模块ohosTest下**resources > base > media**中的图标资源， startWindowBackground字段索引**resources > base > element** **> color.json**中的color。

## 编译报错“Schema validate failed”

**问题现象**

DevEco Studio编译时出现错误，提示“Schema validate failed”错误信息。

**解决措施**

出现该问题的原因是配置文件中字段缺失或拼写错误，可根据报错的详细信息进行问题定位。

如将module.json5文件中abilities标签中的“name”错写为“nam”，报错信息如下：

```
1. Detail: Please check the following fields.
2. {
3. instancePath: 'module.abilities[0]',
4. keyword: 'required',
5. params: { missingProperty: 'name' },
6. message: "must have required property 'name'",
7. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
8. }
9. {
10. instancePath: 'module.abilities[0]',
11. keyword: 'required',
12. params: { missingProperty: 'srcEntrance' },
13. message: "must have required property 'srcEntrance'",
14. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
15. }
16. {
17. instancePath: 'module.abilities[0]',
18. keyword: 'required',
19. params: { missingProperty: 'name' },
20. message: "must have required property 'name'",
21. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
22. }
23. {
24. instancePath: 'module.abilities[0]',
25. keyword: 'oneOf',
26. params: { passingSchemas: null },
27. message: 'must match exactly one schema in oneOf',
28. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
29. }
30. {
31. instancePath: 'module.abilities[0]',
32. keyword: 'enum',
33. params: {
34. allowedValues: [
35. 'priority',
36. 'name',
37. 'srcEntrance',
38. 'srcEntry',
39. 'launchType',
40. 'description',
41. 'icon',
42. 'label',
43. 'permissions',
44. 'metadata',
45. 'visible',
46. 'exported',
47. 'skills',
48. 'backgroundModes',
49. 'continuable',
50. 'startWindowIcon',
51. 'startWindowBackground',
52. 'removeMissionAfterTerminate',
53. 'orientation',
54. 'supportWindowMode',
55. 'maxWindowRatio',
56. 'minWindowRatio',
57. 'maxWindowWidth',
58. 'minWindowWidth',
59. 'maxWindowHeight',
60. 'minWindowHeight',
61. 'excludeFromMissions'
62. ]
63. },
64. message: 'must be equal to one of the allowed values',
65. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
66. }
67. {
68. instancePath: 'module.abilities[0]',
69. keyword: 'propertyNames',
70. params: { propertyName: 'nam' },
71. message: 'property name must be valid',
72. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
73. }
```

以上述报错为例，说明报错中关键词的含义，便于开发者理解报错信息，完成问题定位及修改。

* instancePath：错误所在的文件位置。'module.abilities[0]'表示在module.json5文件中的第一个abilities。
* keyword：标识当前报错字段的可选配属性，当前报错中包括'required'、'oneOf'、'enum'、'propertyNames'。
  + required：表示该字段为必选配置项。由于缺失或拼写错误导致该属性未配置。
  + oneOf：表示当前配置不符合oneOf要求。通过instancePath已经确认报错出现在abilities标签，在DevEco Studio中，按住Ctrl点击"abilities"跳转到对应的module.json文件，可以查看到必须配置以下两组中的一组。根据对比排查，可识别到因拼写错误导致"name"属性未配置。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/D-12uK6lQDO7EfpLFewaSA/zh-cn_image_0000002561753561.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=23A8ADED93D93F2BAA6AE7BDA5B41FB69CAF339A30DA5959C9B526A835A634D4)
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/Z6RyfxOERASZbq3iSYPuiA/zh-cn_image_0000002530913532.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=004CF984F69F136044BCA1BE4A20E101BFA21B0AAE05AF39D57946C2C8C441FC)

**报错原因**

密钥库(p12)密码错误。

注意

**密钥库密码**和**密钥密码**是在创建p12文件时由开发者自行输入的，请牢记该密码。DevEco Studio工程的build-profile.json5文件中有记录密码的密文，但签名工具需要输入密码明文，不能直接将build-profile.json5中的值用到签名工具中。

**常见场景**

1. 密码输入错误。
2. 命令行中需要输入真实密码，误输入了加密后的密码。
3. 密钥(keyAlias)密码和密钥库(p12)密码记混。

**解决措施**

出现该问题的原因是签名文件中签名密码错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/wYbvW9nbSqytezhyLkxUxw/zh-cn_image_0000002530753454.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=E8541DE30D1D6999B6AC75592BC8DC25942E885FB3E8255BABC78ED73979DE8F)

开发者可通过重新自动签名解决该问题：

1. 点击**File > Project Structure > Project > Signing Configs**，打开签名配置页面。

2. 勾选“Automatically generate signature”，等待重新签名，然后点击**OK**即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/qsm9G3xZQk2NruqiDPw1_w/zh-cn_image_0000002561833403.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=31E10C63E688743442933052B1D9D54E56E650974E65955C77D276D56B107CA4)

## 编译报错“please check deviceType or distroFilter of the module”

**问题现象**

DevEco Studio编译时出现错误，出现如下提示之一：

* Module: (xxx) and Module: (xxx) are entry, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/w1FhgtceSxmxhkeruDY7Wg/zh-cn_image_0000002561753395.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=9293F1D01A4E0C4C410E62F42098EBB2F55A2E44F8C3EAB58BC341F755822A20)
* Module: (xxx) and Module: (xxx) have the same moduleName, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/-HKUA6mYRX67jKRon9bAeQ/zh-cn_image_0000002530913520.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=DC6581A6ADF9A6AA9070B8DC7B7B67E22430D96D6163E270EF1803E467A60E65)
* Module: (xxx) and Module: (xxx) have the same packageName, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/R1yS23NkRrSJqBGeQ8Hmkg/zh-cn_image_0000002561753469.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=FFFBC64D5C5EEE12B121297679E790D0F87815390955B3C574BB82133A612CED)
* Module: (xxx) and Module: (xxx) have the same ability name.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/7Z808dTcRTexRZRchqAuNw/zh-cn_image_0000002561753463.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=F0E14EB46DAA9B5CB33FBD5BFFC042C19861FC25D42113E31FF5095629EBBE2A)

**解决措施**

出现该问题的原因是打包时工程未满足HAP唯一性校验逻辑，请根据[HAP唯一性校验逻辑](ide-hvigor-verification-rule.md)修改工程，满足校验逻辑即可正常打包。

## 编译报错“Failed to generate test project build system”

**问题现象**

执行多模块native模块构建时，提示“Failed to generate test project build system.”错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/IQQih-2lSOep-V99jIwq-w/zh-cn_image_0000002530913558.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=7D986D5828171931DE6B3A1CB9BB3C3CF835C0C3DABF9D0D9306B84973E1FB80)

**解决措施**

请删除报错模块下的.cxx文件夹，然后选中需要构建的模块，执行**Make Module** **${moduleName}**完成单独构建，避免同时构建多个模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/6hkCDuSJQj2z_ttQ59MXsg/zh-cn_image_0000002561753407.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=60B4D007E2A866630DDD7ABA8CD96D8FAB6A338321DA3DDCCA97C89D6C557AFA)

## C/C++项目三方依赖库未打包入HAP

**问题现象**

C/C++项目依赖三方so时，在打包生成HAP后，发现三方so未打包到HAP中。

**解决措施**

当前DevEco Studio对C/C++项目三方so的寻址方式有限，如出现三方so未打包到HAP中，请尝试修改so引入方式。

1. 定义一个别名（如jsbind\_shared\_lib\_tracing），代表将要引入的三方so。
2. 使用SHARED IMPORT将三方so定义为动态引入。
3. 使用IMPORTED\_LOCATION定义引入so的具体位置。
4. 将定义的三方so声明给目标。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/U24kLlWfQQWq82KCRjtaXA/zh-cn_image_0000002530913548.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=F5A83A88BF3ECD388B2C41FCB37DB557CB5A6D77FCA0E51E1ACDD02F5F01C735)
5. 再次打包生成HAP，确认三方so是否打包到HAP中。

## Static Library模块中src/main/cpp目录下的文件未打包进HAR

**问题现象**

点击**Build > Make Module ${libraryName}**编译构建生成HAR后，发现构建产物中未出现cpp目录下的文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/VVnG2-oeQRueKcWPDFBESA/zh-cn_image_0000002561753459.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=01FC32CB5127B56C50E962FC2C2012D43A5ABD59BCFB1830D8F0220657F9205A)

**解决措施**

如果使用的Hvigor为2.5.0-s及以上版本，在编译构建HAR的过程中，只会将dependencies内处于本模块路径下的本地依赖也打包进.har文件中，devDependencies里的依赖不会打包进.har文件中。

请将相应的本地依赖移至dependencies中后重新编译。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/ZbNw2pWsQFGyN2JVmdZ-bg/zh-cn_image_0000002530913618.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=F83F127D91596CEF2203C10983F9DD30CA0766EEE6F27421293A971867E2025F)

## 工程编译告警提示“ArkTS:WARN: For details about ArkTS syntax errors”

**问题现象**

工程构建时，提示“ArkTS:WARN: For details about ArkTS syntax errors, see FAQs”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/0htjTuPCQXuMHC1cfg04nA/zh-cn_image_0000002530913564.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=CEC3DDCF1532E0C756574AE781C60589925C37ADB13C0457215A90BF8C27378A)

**解决措施**

出现该告警说明当前工程存在不符合ArkTS语法规范的写法，请根据ERROR报错中括号内的语法规则如(arkts-no-var)，查看[从TypeScript到ArkTS的适配规则](typescript-to-arkts-migration-guide.md#使用let而非var)中对应的说明，修改为ArkTS规范写法。

## 编译报错“ninja: error: mkdir(xxx): No such file or directory”

**问题现象**

Native工程编译报错，同时出现以下告警和报错信息。

出现工程目录长度超过250字符的告警，示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/aEQbUl5iR2mTWvi7xoEhlw/zh-cn_image_0000002561753411.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=176BA4708ABC31561A9F4C1AAEA118B91B680A1750ACC7B4679C120C49C6BEF4 "点击放大")

出现编译报错“ninja: error: mkdir(xxx): No such file or directory”，示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/jXeNJz-vSjibAPPWelVZpw/zh-cn_image_0000002561833411.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=EE3F083F89C6A0D067B8D55FF5CC37FD48ADEC83E0B1D44B4665BBD0C1F74EF8 "点击放大")

**解决措施**

CMAKE\_OBJECT\_PATH\_MAX默认大小为250，如果工程中object file实际路径长度超出该大小，将导致编译报错。

开发者需要根据object file实际路径长度在工程CMakeLists.txt中设置CMAKE\_OBJECT\_PATH\_MAX大小，具体方法如下：

* 方法一： 通常在CMAKE\_OBJECT\_PATH\_MAX默认值基础上增加一个文件名长度即可。

  示例中告警文件为TextMeasureCache.cpp.obj，长度为24字符，在默认值250的基础上增加24，即设置set(CMAKE\_OBJECT\_PATH\_MAX 274)
* 方法二：根据object file实际路径长度计算CMAKE\_OBJECT\_PATH\_MAX大小。

  计算公式：CMAKE\_OBJECT\_PATH\_MAX = 总路径长度 - object file中目录部分长度 + cmake哈希值字符数（固定为32）

  + 总路径长度 = object file directory长度 + object file长度，object file directory、object file如下图所示，两个长度之和为297字符，以实际为准

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/KQbbEFyVTxe4f4ABUo0ThQ/zh-cn_image_0000002561833517.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=F50AE14063E80BA201FF832CD886253A961941A5EFA43E0A2480E7353DF3C15D "点击放大")
  + object file中目录部分长度：示例中“\_\_/\_\_/\_\_/\_\_/\_\_/third-party/rn/ReactCommon/react/renderer/textlayoutmanager”长度为74字符，以实际为准
  + cmake哈希值字符数：cmake将长路径转换为哈希值时哈希值的长度，固定为32

  代入示例中的长度后，计算可得：CMAKE\_OBJECT\_PATH\_MAX = 297 - 74 + 32 = 255，即设置set(CMAKE\_OBJECT\_PATH\_MAX 255)

## 编译报错“(is the command line too long?)”

**问题现象**

Native工程编译报错，同时出现以下告警和报错信息。

出现工程目录长度超过250字符的告警，示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/kI_usi-DS8-BZ19X0NNn4Q/zh-cn_image_0000002530913466.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=1B6C934200F11D30D5CB1F5CF8FE8286F392503CCDCB048A746DA8AC9ABBFD05 "点击放大")

出现编译报错“(is the command line too long?)”，示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/CEHkAX5nQhCE-hYLy39LLg/zh-cn_image_0000002530913560.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=EEA3998364DE4DFD9BE203BBF0141BAC525E9E390A802344530DD36F7FA9625F)

**解决措施**

CMAKE\_OBJECT\_PATH\_MAX默认大小为250，如果工程中object file实际路径长度超出该大小，将导致编译报错。

开发者需要根据object file实际路径长度在工程CMakeLists.txt中设置CMAKE\_OBJECT\_PATH\_MAX大小，具体方法如下：

* 方法一： 通常在CMAKE\_OBJECT\_PATH\_MAX默认值基础上增加一个文件名长度即可。

  示例中告警文件为TextMeasureCache.cpp.obj，长度为24字符，在默认值250的基础上增加24，即设置set(CMAKE\_OBJECT\_PATH\_MAX 274)
* 方法二：根据object file实际路径长度计算CMAKE\_OBJECT\_PATH\_MAX大小。

  计算公式：CMAKE\_OBJECT\_PATH\_MAX = 总路径长度 - object file中目录部分长度 + cmake哈希值字符数（固定为32）

  + 总路径长度 = object file directory长度 + object file长度，object file directory、object file如下图所示，两个长度之和为297字符，以实际为准

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/_spWYzO0RquFzbgq8Oeskw/zh-cn_image_0000002530913620.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=0B1ED8CC11BE0A6840EDF1010766464EBD316177AE71ABE8E8603EF646C28E87 "点击放大")
  + object file中目录部分长度：示例中“\_\_/\_\_/\_\_/\_\_/\_\_/third-party/rn/ReactCommon/react/renderer/textlayoutmanager”长度为74字符，以实际为准
  + cmake哈希值字符数：cmake将长路径转换为哈希值时哈希值的长度，固定为32

  代入示例中的长度后，计算可得：CMAKE\_OBJECT\_PATH\_MAX = 297 - 74 + 32 = 255，即设置set(CMAKE\_OBJECT\_PATH\_MAX 255)
* 方法三：若设置CMAKE\_OBJECT\_PATH\_MAX后，仍然报相同错误，需要修改工程存放目录，将其存放在较短的目录下。

  设置CMAKE\_OBJECT\_PATH\_MAX后，cmake会将长路径转换为32字符的哈希值以缩短路径长度，如果转换后的路径依然过长，只能缩短工程的存放路径。

## 编译报错“CMake Error: The following variables are used in this project, but they are set to NOTFOUND”

**问题现象**

Native工程中使用find\_path时出现以下报错信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/B9eTWFx0SSOp-Fmd1DiyJw/zh-cn_image_0000002530913622.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=3E44224A3AFA043E5DDBE2ACAF14BD5F9E8BCD7F3F678A81AFBAAD4D0B75E999 "点击放大")

**解决措施**

OpenHarmony SDK提供的CMake交叉编译配置文件（ohos.toolchain.cmake）中，限制了搜索路径为CMAKE\_SYSROOT。

如果开发者需要添加搜索路径，可在CMakeLists.txt中使用list接口添加自定义路径，如将"D:demo"添加至搜索路径：

```
1. list(APPEND CMAKE_FIND_ROOT_PATH_MODE_INCLUDE "D:demo")
```

添加后，即可使用find\_path查找"D:demo"目录下的文件。

## 编译报错 “Unknown resource name”

* 场景一

**问题现象**

工程中模块A引用了模块B，编译模块A时出现错误，提示 "Unknown resource name 'xxxx'"，找不到模块B的资源。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/o9BOah78TzS2DDDKmQdBxQ/zh-cn_image_0000002530913432.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=FF8C2465BFC7BFC66CAD0B67DC89DEA5160487332DF9A4D38C19AE840C33568E "点击放大")

**解决措施**

请确保符合以下条件：

1. 资源需放置在目录resource/base路径下。
2. 模块B已安装。
3. 模块A中不能使用相对路径引用模块B的资源，应直接通过定义的模块名称来引用。

* 场景二

**问题现象**

引用模块的方式不对，如果引用的是一个其他模块的代码，也会报资源找不到。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/FSCtJXHQRdu-wt68C9Ep7w/zh-cn_image_0000002530753580.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=4D91791182D077666A39ADD9FA8292DDC08BCCCBB583073FDD370BA2F094F752)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/YdunEm-rTeKqxpI0YUaqrw/zh-cn_image_0000002561753573.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=AA5741A61F110E3B88B12E9E914B15AC8C571A243D2568621E45FB6BF7A3151C)

**解决措施**

在oh\_package.json5中引入该模块。通过定义的模块名称来引用。

如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/47S2S2HlTkaGgaUmXWdfNg/zh-cn_image_0000002530753582.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=006A1952F696028A888DF8464F7F3086B06A8F11274447904DE894CEE3C4AF97)

* 场景三

**问题现象**

HSP A 申请了某个权限，这个权限进行了资源的引用，在所有依赖A的组件进行构建时，报错 A 引用的资源找不到。

**解决措施**

手动在引用方配置对应资源可以解决此问题。

## 构建报错“Task xxx was not found in the project xxx”

**问题现象**

命令行手动执行构建命令时，构建失败，提示“Task xxx was not found in the project xxx”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/mTXAJSzJTPadfHlkhSeBXQ/zh-cn_image_0000002561753477.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=DEBD629DD90C931E1D73B73091C9A4A865F289242F823F4533452FB7955A9C4C)**问题确认**

1. 执行hvigorw tasks命令，查看对应命令是否存在。
2. 查看对应工程中module.json5文件中“type”字段是否为命令执行模块。比如图中执行assembleHar命令，是对工程中的har模块进行打包，若module.json5文件中的“type”字段不是"har"类型，则会出现上述错误提示。

**解决措施**

1. 执行正确命令。
2. 查看对应工程中module.json5文件中“type”字段类型，执行对应命令。

## 编译报错“The reason and usedScene attributes are mandatory for user\_grant permissions”

**问题现象**

DevEco Studio编译失败，提示“The reason and usedScene attributes are mandatory for user\_grant permissions”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/uXPo6UFdS0m4DtOPoAv6kg/zh-cn_image_0000002561753481.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=70258EF496AFA689361E2BC5E57845C57EE814327D1C768A3E257FF30A2850FB "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview2版本开始新增规则：APP包中，所有entry和feature hap的module下的requestPermissions权限清单必须指定(可以缺省为空，若非空则name必填,user\_grant权限则必填reason、usedScene字段)。

**解决措施**

进入对应module.json5文件中，补齐requestPermissions字段下的reason和usedScene字段。如以下示例：

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.READ_IMAGEVIDEO",
4. "reason": "$string:module_desc",
5. "usedScene": {
6. "abilities": [
7. "EntryAbility"
8. ],
9. "when": "inuse"
10. }
11. }
12. ]
```

## 编译报错“Only one default card can be configured in the form\_config.json file”

**问题现象**

DevEco Studio编译失败，提示“Only one default card can be configured in the form\_config.json file”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/XWPUnhq8QMSTn3MsfTf3vg/zh-cn_image_0000002561833419.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=C435816A4C2207C19B96515225E1A9F2D79796F1B522A2FA371E04C22EF914C6 "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview2版本开始新增规则：卡片的配置文件中isDefault不可缺省，每个UIAbility有且只有一个默认卡片。

**解决措施**

进入对应module.json5文件中，选择唯一默认卡片，将其他卡片的isDefault字段设置为false。

## 编译报错“In the form\_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty”

**问题现象**

DevEco Studio编译失败，提示“In the form\_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/voAJItvdT7iCSxRnJMtsWA/zh-cn_image_0000002530913566.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=AA222CBDBA3FB496A216C8AEF47EFF66CD51F6A7913F7FC70837261EA947F89D "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview2版本开始新增规则：卡片的配置文件中updateEnabled不可缺省，为true时可以在定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式任选其一，当两者同时配置时，定时刷新优先生效。

**解决措施**

进入对应module.json5文件中，按照需求，选择配置updateEnabled为false，或者增加定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式配置。

## 编译报错“The path XX is not writable. please choose a new location”

**问题现象**

在mac上，通过直接打开dmg中的DevEco Studio，构建报错 The path XX is not writable. please choose a new location.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/jQGCRh9cQiW2cPtUU2Yaxg/zh-cn_image_0000002561753399.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=853CD684E1715BD292FFC53904B22DC498D2E79C626DF539EE809698F4B92C9F)

**问题原因**

在mac上直接打开dmg 中的DevEco Studio，是会以只读的方式打开的，内置到DevEco Studio里面的文件是没有写权限的。

**解决措施**

将“DevEco-Studio.app”拖拽到“Applications”中，先安装再使用。

## 编译报错“Property 'XX' does not exist on type 'typeof BuildProfile'”

**问题现象**

本地HSP模块对外提供的接口中使用了HAP未定义的自定义参数BuildProfileFileds，且HAP引用了HSP中的该接口，导致编译失败，提示“Property 'XX' does not exist on type 'typeof BuildProfile'”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/fZ4McUJWRyyqqAYDD6iVfg/zh-cn_image_0000002530753578.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=1D0CA132D240AE426003EC3C8C8BD81DC3FC456639260C982A12C18ED8BA6AF6)

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

  ```
  1. {
  2. "app": {
  3. "products": [
  4. {
  5. "buildOption": {
  6. "strictMode": {
  7. "useNormalizedOHMUrl": true
  8. }
  9. }
  10. }
  11. ]
  12. }
  13. }
  ```
* 如果与工程不一致的依赖包较多，建议修改工程的工程级build-profile.json5中的useNormalizedOHMUrl值以及替换其它的不一致的依赖包。

如果修改了useNormalizedOHMUrl仍无法解决，表明当前hsp包是本地包，需要以本地hsp包的形式引入，请在工程下的build-profile.json5中的modules中添加报错hsp模块，示例如下：

```
1. "modules": [
2. {
3. name: "hsp",   // 引用的hsp包依赖
4. srcPath: "../MyApplication_stageB/hsp",   // 引用的hsp包的路径（绝对和相对都可以）
5. }
6. ]
```

## 如何配置oh-package.json5动态依赖

oh-package.json5文件中：

* dependencies（生产依赖）：声明需要在代码中import的三方库（参与编译/运行阶段使用的依赖）。
* devDependencies（开发依赖）：参与项目的开发或测试阶段。
* dynamicDependencies（动态依赖）：动态依赖的HSP模块。在开发者需要动态加载HSP的时候配置使用。

示例如下，详细内容可参考[oh-package.json5文件](ide-oh-package-json5.md)和[添加依赖项](ide-hvigor-dependencies.md)。

```
1. {
2. "name": "parameter-test",
3. "version": "@param:version",
4. "description": "test desc.",
5. "main": "index.ets",
6. "author": "test author",
7. "license": "ISC",
8. "dependencies": {
9. "libtest1": "@param:dependencies.libtest1"
10. },
11. "devDependencies": {
12. "libtest2": "@param:devDependencies.libtest2"
13. },
14. "dynamicDependencies": {
15. "libtest3": "@param:dynamicDependencies.libtest3"
16. },
17. "parameterFile": '.parameterFile/parameterFile.json5' // 开启参数化并指定参数化配置文件路径
18. }
```

## 如何解决SDK与镜像不匹配导致abc文件无法正常运行的问题

**问题现象**

当SDK版本与镜像版本不匹配时，应用将会闪退，出现jscrash，同时hilog出现日志。

**解决措施**

现象根本原因是SDK工具与镜像版本不匹配。推荐使用匹配的SDK与镜像版本。

查看SDK版本方法：

在DevEco Studio安装路径下的sdk路径中，执行 {sdk.dir}/openharmony/ets/build-tools/ets-loader/bin/ark/build-win/bin/es2abc.exe --bc-version可查看SDK版本号。用于检验SDK与镜像版本是否匹配。

## 如何解决编译报错“Could not resolve 'xxx' from”，但'xxx'目录存在的问题

**问题现象**

编译报错：“Could not resolve 'xxx' from”，但'xxx'目录存在，目录下存在Index文件。

**问题原因**

在引用目录时，编译时自动拼接小写的index文件，而目录中是大写的Index文件，在编译大小写敏感时，找不到index文件，则报错。

**解决措施**

在引用'xxx'目录时，明确写明引用到'xxx/Index'文件。

## 用户目录下没有npmrc文件

**问题现象**

新建项目报错 Error: The hvigor depends on the npmrc file. Configure the npmrc file first。

**问题原因**

在用户目录下没有 .npmrc 文件。

**解决措施**

在用户目录下创建.npmrc文件，配置如下信息：

```
1. registry=https://repo.huaweicloud.com/repository/npm/
2. @ohos:registry=https://repo.harmonyos.com/npm/
```

## 如何解决编译报错“ Error: 'icon' value `$media:icons` invalid value.”的问题

**问题现象**

编译报错“ Error: 'icon' value `$media:icons` invalid value”。

```
1. ERROR: Failed :entry:default@CompileResource...
2. ERROR: Tools execution failed.
3. Error: ref `$media:icons` don`t be defined.
4. Error: 'icon' value `$media:icons` invalid value.
5. at D:\project\process_profile\default\module.json
6. Detail: Please check the message from tools.
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/nj9drsMXSyWp-BBlWfeoZw/zh-cn_image_0000002561833527.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=8755BD62E5832F2412BB19C675394907C50C07FCA25C75A0D28A199685AD1737 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/QRz9j4WJQ9S5SEf_O0fQVQ/zh-cn_image_0000002561833369.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=38CCC762C547A450549E6841D7D6904551B18C3EBA1CB93F7D02DF9D90548282)

**解决方案**

检查文件名是否合法，文件名只能包含大小写字母、数字、下划线。

## 如何解决三方包require语句报错

**问题现象**

当引入三方包时编译报错。

**报错原因**

部分三方包由npm迁移而来，其开发环境为node， 其中的require语法arkcompiler不完全支持，出现运行报错情况。

**场景1**：

```
1. // Module/src/test.json
2. {a: 1, b: 2}
3. //use.js
4. let test = require("Module/src/test.json")
```

**需修改为：**

```
1. // Module/src/test.js
2. module.exports = {a: 1, b: 2}
3. //use.js
4. let test = require("Module/src/test")
```

**场景2：**

```
1. // Module/package.json
2. ...
3. main: "./src"
4. ...
5. // use.js
6. let module = require("Module")
```

**需修改为：**

```
1. // Module/package.json
2. ...
3. main: "./src/index.js"
4. ...
5. // use.js
6. let module = require("Module")
```

**场景3：**

编译出现warning信息：

```
1. Plugin node-resolve: preferring built-in module 'util' over local alternative at '/Users/~/Documents/fe-module/demo/node_modules/util/util.js', pass 'preferBuiltins: false' to disable this behavior or 'preferBuiltins: true' to disable this warning
```

**解决方案**

修改rollup 配置文件，rollup.config.js中修改 preferBuiltins 字段：

```
1. plugins: [
2. resolve({
3. preferBuiltins: false,    // true 或 false
4. mainFields: ['module', 'main'],
5. extensions
6. })
7. ];
```

**场景4：**

```
1. import {Buffer} from 'buffer'
```

**需修改为：**

```
1. import {Buffer} from 'buffer/'
```

## 如何解决编译报错“Indexed access is not supported for fields(arkts-no-props-by-index)”的问题

**问题现象**

动态调用类或者接口的字段，导致编译报错出现：Indexed access is not supported for fields(arkts-no-props-by-index)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/n7kKNJ0xR3GcJHky9Ae3fQ/zh-cn_image_0000002561753489.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=D267DCDEEAFFFC271C8EA80FEE54A269EA6F4E240942743F8B37250DDB8CD754)

**解决方案**

修改代码：

```
1. getValue(breakpoint: string): T {
2. return Reflect.get(this.options, breakpoint) as T;
3. }
```

## 如何解决编译报错“Declaration merging is not supported(arkts-no-decl-merging)” 或 “Cannot redeclare block-scoped variable 'xxx'”的问题

**问题现象**

在不同的文件中声明相同变量或者interface、enum等类型，DevEco Studio不报错，但是编译报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/Q9DwOj3wTYukFzTxv5u71Q/zh-cn_image_0000002561753525.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=8806D423EBC583918A672B011C3363C2736937E2452E3143D5B0C1C3553F8D47)

**解决方案**

如果文件中不包含export关键字，该文件将视作全局命名空间的一部分，相当于两个文件实质为同一个文件。请添加export关键字使其成为独立命名空间，或者将声明的内容添加到自定义的命名空间中。

## 如何解决编译报错“ The inferred type of 'xxx' cannot be named without a reference to 'xxx'. This is likely not portable. A type annotation is necessary**.**”的问题

**问题现象**

编译报错"The inferred type of 'xxx' cannot be named without a reference to 'xxx'. This is likely not portable. A type annotation is necessary"。

**问题原因**

HSP会生成.d.ts声明文件，由于原始文件中未注明类型，导致生成的.d.ts文件缺少类型注解。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/eMMCfjCYTHuTLS27A4AWNQ/zh-cn_image_0000002561753471.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=C1AC670DAAC80DE6F5D9CC4EE3AF47666D117922FA3268DA572E0DA574E83DE4 "点击放大")

**解决方案**

报错位置添加类型注解。

## 如何解决编译报错"arkts-no-any-unknown" 和 "Cannot find module 'xx' or its corresponding type declarations"的问题

**问题现象**

编译报错"arkts-no-any-unknown" 和 "Cannot find module 'xx' or its corresponding type declarations"。

**问题****原因**

大小写敏感导致模块找不到，常见于图片中的两种错误同时出现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/3ua3c42ZQ9OFchBeXij1AQ/zh-cn_image_0000002561833423.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=FD494E1AC579C23CD7EDDA69A7EC73D3CFFB2BDD5607C530C50CD36D7C126178)

**解决方案**

解决引用中的大小写问题。

## 如何解决编译报错“ERROR: ArkTS Compiler Error ERROR: /bin/sh: "xxxx/es2abc": Operation not permitted”的问题

**问题现象**

编译报错“ERROR: ArkTS Compiler Error ERROR: /bin/sh: "xxxx/es2abc": Operation not permitted”。

**问题原因**

由于获取SDK的方式是从网络上下载，mac的安全设置会给可执行文件添加来源于网络的标识（com.apple.quarantine），导致无法执行。

**解决方案**

执行命令删除可执行文件的com.apple.quarantine标识。

```
1. xattr -d com.apple.quarantine /path/to/es2abc
```

## 如何解决编译报错“Cannot add xxxx items to index”的问题

**问题现象**

编译报错“Cannot add xxxx items to index”。

**问题原因**

被编译文件中某函数内部有大量object literal, array literal和string，导致item的数量超过了上限（65536）。

**解决方案**

排查相关文件，将存在上述原因的函数进行拆分。

## 编译初始化报错“resource busy or locked, open 'xxx\outputs\build-logs\build.log'”

**问题现象**

在升级DevEco Studio至5.0.3.403版本后，打开旧工程概率性报错：resource busy or locked, open 'xxx\outputs\build-logs\build.log'。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/Lb5eA0rWS5CdlG5S5ex20g/zh-cn_image_0000002530913474.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=F61BE66C51774AE6C2325299E2040D25549BE86D47CF5CCCBA01B896DA03DDD4)

**问题原因**

初始化时日志写入存在冲突，.hvigor目录中的build-log文件被占用导致了该报错。

**解决方案**

* 方法一：点击编辑器窗口上方的Sync Now。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/g-xsK96wQbyo_3jxALZ-IQ/zh-cn_image_0000002561753401.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=2081284E94CA9BB98CE805B3819F040C44F90E422A3AD687FEC16097F7760C92)
* 方法二：点击工具栏**File > Sync and Refresh Project**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/U5iFgdiPT1eCQpHt2rz9dA/zh-cn_image_0000002561833425.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=AC45DC6DB16AC3CD6C055BC36E8B6E90137E9DEEB3C36F8AE6B58670DB730656)
* 方法三：如果方法1、2无法解决问题，可以手动删除工程目录下的.hvigor目录后重启执行Sync。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/SC8_t8ueRuGXyvQN9ixw3w/zh-cn_image_0000002530913438.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=83986F68F05282856115059145E5C66ECD36B34CA4849FCE52E9EE0590A09112)

## Mac环境下加载动态库，签名拦截导致未生效

**问题现象**

Mac环境下，在DevEco项目开发时，build-profile.json5中添加了如下的插桩配置，但是插桩功能未生效。

```
1. "transformLib": "<相对模块根路径的动态库路径，以./开头>"
```

**判断与验证**

1. 进入sdk中es2abc所在目录：[DevEco-Studio安装目录]/Contents/sdk/default/openharmony/ets/build-tools/ets-loader/bin/ark/build-mac/bin。
2. 执行下列命令：

   ```
   1. ./es2abc --merge-abc --transform-lib <动态库路径> <测试js文件路径>
   ```
3. 如果提示类似如下报错信息，原因可能是es2abc和动态库文件不属于一个签名组。

   ```
   1. os::library_loader::Load error: dlopen(..., 0x0001):
   2. tried: '...' (code signature in <...> '...' not valid for use in process: mapped file has no cdhash, completely unsigned? Code has to be at least ad-hoc signed.)
   ```
4. 用下面命令查看es2abc和动态库文件的签名组信息，如果两个文件，一个有签名信息，一个没有签名信息，或者都有签名信息，但是签名信息中属性'TeamIdentifier'的值是不一样的，那就说明问题是签名组不一致导致的，可以使用"解决方案"提供的方式处理。

   ```
   1. codesign -dv --verbose=1 <es2abc路径>
   2. codesign -dv --verbose=1 <动态库路径>
   ```

**解决方案**

执行下列命令，将es2abc文件的签名替换成和动态库文件一样的用户签名。

```
1. codesign --remove-signature <es2abc路径>
2. codesign -s - -v <es2abc路径>
```
