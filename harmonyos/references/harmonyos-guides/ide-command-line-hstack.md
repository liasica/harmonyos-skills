---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-hstack
title: 堆栈解析工具（hstack）
breadcrumb: 指南 > 命令行工具 > 堆栈解析工具（hstack）
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0488d2b71be36a73395a9cbacbe128e0d0457a8af2b0ade8dc65a20d1ae7f598
---

## 简介

hstack是为开发人员提供的用于将release应用混淆后的crash堆栈解析为源码对应堆栈的工具，支持Windows、Mac、Linux三个平台，关于堆栈解析的原理，请查看[异常堆栈解析原理](ide-exception-stack-parsing-principle.md)。

hstack命令行格式为：

```
1. hstack [options]
```

options: 可选配置，请参考[表hstack命令行配置](ide-command-line-hstack.md#table25697717185)。

**表1** hstack命令行配置

| 指令 | 说明 |
| --- | --- |
| -i/--input | 可选，指定工程crash文件归档目录。 |
| -c/--crash | 可选，指定一条crash堆栈。 |
| -o/--output | 可选，指定解析结果输出目录（输入指定为-c时， -o参数指定一个输出文件）。 |
| -s/--sourcemapDir | 可选，指定工程sourceMap文件归档目录。 |
| --so/--soDir | 可选，指定工程shared object文件归档目录。 |
| -n/--nameObfuscation | 可选 ，指定工程nameCache文件归档目录。 |
| -v/--version | 查看hstack版本。 |
| -h/--help | 查询hstack命令行帮助。 |

说明

* crash文件归档目录与crash堆栈必须且只能提供一项。
* sourceMap与shared object文件归档目录至少提供一项。
* 如果需要对方法名进行解析还原，则需要同时提供sourceMap与nameCache文件。
* 路径参数不支持以下特殊字符：`~!@#$^&\*=|{};,\s\[\]<>?~！@#￥……&\*（）——|{}【】‘；：。，、？

## 环境配置

1. hstack工具在Command Line Tools的bin目录下，需要[将bin目录配置到PATH变量中](ide-commandline-get.md#section17776863449)。
2. 本工具依赖Node环境，需要[将Node.js配置到环境变量中](ide-command-line-building-app.md#section159168531288)。
3. 如果需要对C++文件产生的异常进行解析，则需要将SDK中的native\llvm\bin目录配置到环境变量中，变量名设置为“ADDR2LINE\_PATH”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/JjetjPOLQwqVe5wIDyM_Mw/zh-cn_image_0000002561752979.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=6C0678AAF88F885F92C62A689F055ECBF24FBE80A0BDE39506CEF33FCF46D39E)

## 使用示例

1. 将应用产生的crash文件归档到crashDir目录下（或者-c指定一条crash堆栈），关于堆栈的获取方式请参考[崩溃检测](fault-detection-overview.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/-Ivpzj8GQJGoyD14T8iA8g/zh-cn_image_0000002561832965.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=BB6E5682AE01EC54CC34F55557F665CB7D6D2BCC58705A062AB0E2476495DDD8)
2. 使用-o指定输出目录，当不指定时，会输出至-i指定的crashDir目录下（通过-c输入为crash堆栈时，可以使用-o指定一个输出文件，或不指定，直接将结果输出至控制台）。
3. 使用-s指定工程对应sourceMap文件归档目录（可选，与shared object文件归档目录至少提供一项）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/GQYidI79S_-2CvsXe3uFjA/zh-cn_image_0000002530753056.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=B0D5CE27A640EC438DE21A4C3523927A422B1407AD2C8D42582E21119DA1E72F)
4. 使用--so指定shared object文件归档目录（可选，与sourceMap归档目录至少提供一项）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/ZHTm0FeUQaazmKVaP9KIag/zh-cn_image_0000002530753050.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=59DFA246B67AF59174B531632F2FB086B7B2AB8ADFB3F4A43750DE29892E4B0A)
5. 使用-n指定nameCache文件归档目录（可选）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/V_zQK1W7TY-Hk8c3COtppQ/zh-cn_image_0000002561752993.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=4F075B9A5BDE9B153EBD45EA4DFF7753CC98A5BD9BC869150F52D2EC23282F9F)
6. 执行以下命令，可将release应用crash堆栈解析为源码对应堆栈。

   ```
   1. # 通过-i指定crash文件归档目录，并将解析结果输出至outputDir目录
   2. hstack -i D:\crashDir -o D:\outputDir -s D:\sourcemapDir --so D:\soDir -n D:\nameCacheDir
   3. # 通过-c指定一条堆栈，并将解析结果输出至out.txt文件
   4. hstack -c "at anonymous (entry|entry|1.0.0|src/main/ets/pages/Index.ts:401:1)" -o D:\outputDir\out.txt -s D:\sourcemapDir --so D:\soDir -n D:\nameCacheDir
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/5x2U-KfmRRm4ot1b1kUXeQ/zh-cn_image_0000002530753040.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=020D2A3E3D6872DC46CE85E9567C5F9C123BEAB6442C620114A3F06E87E1D210)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/pUEMbQNCQu-tHFnpH2Ffug/zh-cn_image_0000002532098826.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=5960483942479FCA061A5F573545255B6EB0D04C797517F29E6471F0F86DAD11 "点击放大")

   如果是指定crash文件归档目录，解析完成后，outputDir目录下会生成对应的解析结果，文件以原始crash文件名加“\_”前缀进行命名。crash堆栈中的C++日志以及ArkTS日志均已解析为源码对应的文件路径以及行列号，结果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/DWNEm2vXTjauo-Z7X1L0Wg/zh-cn_image_0000002561752987.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=282F92AF561AE4FCF6235387EDE4A77FFEDC71E7FC3E8439875E60A175F82D97)

   在构建Release应用时，so文件是默认不包含符号表信息的，如果需要在构建Release应用时生成包含符号表的so文件，需要在工程的模块级build-profile.json5文件的buildOption属性中，配置如下信息：

   ```
   1. "buildOption": {
   2. "externalNativeOptions": {
   3. "arguments": "-DCMAKE_BUILD_TYPE=RelWithDebInfo"
   4. }
   5. }
   ```

## 堆栈解析方案说明

以如下代码为例。

Entry模块通过独立har包形式引用har模块中的har方法：

```
1. import {har} from 'Har'
2. @Entry
3. @Component
4. struct Index {
5. @State har: string = 'Har';
6. build() {
7. Row() {
8. Column() {
9. Text(this.har)
10. .fontSize(50)
11. .fontWeight(FontWeight.Bold)
12. .onClick(() => {
13. let entryClass = new EntryClass();
14. entryClass.callHarFunction();
15. })
16. }
17. .width('100%')
18. }
19. .height('100%')
20. }
21. }

23. class EntryClass {
24. callHarFunction() {
25. har()
26. }
27. }
```

```
1. @Component
2. export struct MainPage {
3. @State message: string = 'Hello World';

5. build() {
6. Row() {
7. Column() {
8. Text(this.message)
9. .fontSize(50)
10. .fontWeight(FontWeight.Bold)
11. }
12. .width('100%')
13. }
14. .height('100%')
15. }
16. }

18. export function har() {
19. BigInt(1.1)
20. }
```

生成的crash如下：

```
1. at har (entry|har|1.0.0|src/main/ets/components/mainpage/MainPage.js:58:58)
2. at i (entry|entry|1.0.0|src/main/ets/pages/Index.ts:71:71)
3. at anonymous (entry|entry|1.0.0|src/main/ets/pages/Index.ts:55:55)
```

crash中，包含混淆后的方法名（或属性名）、路径信息以及混淆后的行列号信息，其中：

* 方法名在配置相应混淆规则后，会进行混淆处理（例如上述例子中EntryClass的callHarFunction被混淆为i）。方法名混淆前后的映射关系保存在对应模块编译产物的nameCache文件中。
* 路径信息格式为：引用方entry-packageName|被引用方packageName|version|源码相对路径，其中packageName以及version保存在对应模块编译产物的sourceMap文件中。
* 行列号混淆前后的映射关系保存在对应模块编译产物的sourceMap文件中，可利用文件对应的mappings字段进行解析还原。

在对堆栈进行还原时，可分为以下三步：

1. 根据路径信息，找到引用方模块sourceMap。例如第一条堆栈：

   ```
   1. at har (entry|har|1.0.0|src/main/ets/components/mainpage/MainPage.js:58:58)
   ```

   根据路径信息entry|har|1.0.0|src/main/ets/components/mainpage/MainPage.js，可在entry模块sourceMap文件中找到如下字段：

   ```
   1. "entry|har|1.0.0|src/main/ets/components/mainpage/MainPage.js": {
   2. "version": 3,
   3. "file": "MainPage.js",
   4. "sources": [
   5. "oh_modules/.ohpm/Har@ue9rwlwgmslvadnmypsedjcin6a=/oh_modules/Har/src/main/ets/components/mainpage/MainPage.js"
   6. ],
   7. "names": [],
   8. "mappings": "AAAA,IAAA,CAAA,CAAA,sBAAA,IAAA,MAAA,CAAA,SAAA,CAAA,EAAA;IACA,OAAA,CAAA,GAAA,CAAA,MAAA,CAAA,SAAA,EAAA,sBAAA,EAAA,GAAA,EAAA,GAAA,CAAA,CAAA,CAAA;CACA;AACA,MAAA,OAAA,QAAA,SAAA,MAAA;IACA,YAAA,CAAA,EAAA,EAAA,EAAA,CAAA,EAAA,CAAA,GAAA,CAAA,CAAA,EAAA,CAAA,GAAA,SAAA,EAAA,CAAA;QACA,KAAA,CAAA,CAAA,EAAA,CAAA,EAAA,CAAA,EAAA,CAAA,CAAA,CAAA;QACA,IAAA,OAAA,CAAA,KAAA,UAAA,EAAA;YACA,IAAA,CAAA,gBAAA,GAAA,CAAA,CAAA;SACA;QACA,IAAA,EAAA,GAAA,IAAA,wBAAA,CAAA,aAAA,EAAA,IAAA,EAAA,SAAA,CAAA,CAAA;QACA,IAAA,CAAA,yBAAA,IAAA,CAAA;QACA,IAAA,CAAA,oBAAA,EAAA,CAAA;IACA,CAAA;IACA,yBAAA,CAAA,EAAA;QACA,IAAA,GAAA,OAAA,KAAA,SAAA,EAAA;YACA,IAAA,CAAA,OAAA,GAAA,GAAA,OAAA,CAAA;SACA;IACA,CAAA;IACA,eAAA,CAAA,CAAA;IACA,CAAA;IACA,iCAAA,CAAA,CAAA;QACA,IAAA,EAAA,CAAA,uBAAA,CAAA,CAAA,CAAA,CAAA;IACA,CAAA;IACA,gBAAA;QACA,IAAA,EAAA,CAAA,gBAAA,EAAA,CAAA;QACA,iBAAA,CAAA,GAAA,EAAA,CAAA,MAAA,CAAA,IAAA,CAAA,IAAA,EAAA,CAAA,CAAA;QACA,IAAA,CAAA,wBAAA,EAAA,CAAA;IACA,CAAA;IACA,IAAA,OAAA;QACA,OAAA,IAAA,EAAA,CAAA,GAAA,EAAA,CAAA;IACA,CAAA;IACA,IAAA,OAAA,CAAA,EAAA;QACA,IAAA,EAAA,CAAA,GAAA,IAAA,CAAA;IACA,CAAA;IACA,aAAA;QACA,IAAA,CAAA,yBAAA,CAAA,CAAA,CAAA,EAAA,EAAA,EAAA,EAAA;YACA,GAAA,CAAA,MAAA,EAAA,CAAA;YACA,GAAA,CAAA,MAAA,CAAA,MAAA,CAAA,CAAA;QACA,CAAA,EAAA,GAAA,CAAA,CAAA;QACA,IAAA,CAAA,yBAAA,CAAA,CAAA,CAAA,EAAA,CAAA,EAAA,EAAA;YACA,MAAA,CAAA,MAAA,EAAA,CAAA;YACA,MAAA,CAAA,KAAA,CAAA,MAAA,CAAA,CAAA;QACA,CAAA,EAAA,MAAA,CAAA,CAAA;QACA,IAAA,CAAA,yBAAA,CAAA,CAAA,CAAA,EAAA,CAAA,EAAA,EAAA;YACA,IAAA,CAAA,MAAA,CAAA,IAAA,CAAA,OAAA,CAAA,CAAA;YACA,IAAA,CAAA,QAAA,CAAA,EAAA,CAAA,CAAA;YACA,IAAA,CAAA,UAAA,CAAA,UAAA,CAAA,IAAA,CAAA,CAAA;QACA,CAAA,EAAA,IAAA,CAAA,CAAA;QACA,IAAA,CAAA,GAAA,EAAA,CAAA;QACA,MAAA,CAAA,GAAA,EAAA,CAAA;QACA,GAAA,CAAA,GAAA,EAAA,CAAA;IACA,CAAA;IACA,QAAA;QACA,IAAA,CAAA,mBAAA,EAAA,CAAA;IACA,CAAA;CACA;AACA,MAAA,UAAA,GAAA;IACA,MAAA,CAAA,GAAA,CAAA,CAAA;AACA,CAAA",
   9. "entry-package-info": "entry|1.0.0",
   10. "package-info": "har|1.0.0"
   11. }
   ```
2. 利用对应sourceMap信息进行堆栈路径以及行列号还原：

   基于步骤1找到的sourceMap信息，根据sources及mappings字段进行解析，可以将路径以及行列号还原如下：

   ```
   1. at har (oh_modules/.ohpm/Har@ue9rwlwgmslvadnmypsedjcin6a=/oh_modules/Har/src/main/ets/components/mainpage/MainPage.js:58:58)
   ```

   该文件位于entry模块oh\_modules路径下。

   如果对应sourceMap中包含package-info字段，则可以利用package-info中对应模块的sourceMap，对该条堆栈进行二次解析。例如该堆栈中包package-info为har|1.0.0，可利用har中的sourceMap对该堆栈进行再次解析，方案如下：

   1. 由路径中最后一个oh\_modules起，向下两级，截断上述第一次解析结果路径，结果如下：

      ```
      1. src/main/ets/components/mainpage/MainPage.js
      ```
   2. 上述路径拼接package-info， 拼接方式为：packageName|packageName|version|截断路径，得到拼接路径如下：

      ```
      1. har|har|1.0.0|src/main/ets/components/mainpage/MainPage.js
      ```
   3. 利用拼接后的路径，在har模块sourceMap文件中找到如下字段：

      ```
      1. "har|har|1.0.0|src/main/ets/components/mainpage/MainPage.js": {
      2. "version": 3,
      3. "file": "MainPage.ets",
      4. "sources": [
      5. "har/src/main/ets/components/mainpage/MainPage.ets"
      6. ],
      7. "names": [],
      8. "mappings": ";;;AAEA,MAAA,OAAA,QAAA,SAAA,MAAA;IADA,YAAA,CAAA,EAAA,CAAA,EAAA,CAAA,EAAA,IAAA,CAAA,CAAA,EAAA,IAAA,SAAA,EAAA,CAAA;;;;;;;;IADyB,CAAA;;;;;;;;;;;;;;;;;;;;;;IAKvB,aAAA;;;;;;;;;;;;YAGM,IAAA,CAAA,UAAA,CAAA,UAAA,CAAA,IAAA,CAAA,CAAA;;;;;IAOL,CAAA;;;;;AAGH,MAAA,UAAA,GAAA;;AAEA,CAAA",
      9. "entry-package-info": "har|1.0.0"
      10. }
      ```
   4. 根据该sourceMap的sources及mappings字段进行再次解析，可得到该堆栈对应的源码信息为：

      ```
      1. at har (har/src/main/ets/components/mainpage/MainPage.ets:20:1)
      ```
3. 利用nameCache文件，对方法名进行解析还原。

   以第二条堆栈为例：

   ```
   1. at i (entry|entry|1.0.0|src/main/ets/pages/Index.ts:71:71)
   ```

   通过步骤1与步骤2，将该堆栈路径以及行列号信息进行解析，结果如下：

   ```
   1. at i (entry/src/main/ets/pages/Index.ets:25:3)
   ```

   在对应模块编译产物中的nameCache文件中，通过解析后的文件路径找到如下字段：

   ```
   1. "entry/src/main/ets/pages/Index.ets": {
   2. "IdentifierCache": {
   3. "Index#initialRender#__function": "o",
   4. "Index#initialRender#$2#__function": "t",
   5. "Index#initialRender#$2#$0#entryClass": "u",
   6. "$0#__function": "a1"
   7. },
   8. "MemberMethodCache": {
   9. "initialRender:6:20": "initialRender",
   10. "callHarFunction:24:26": "i"
   11. },
   12. "obfName": "entry/src/main/ets/pages/Index.ets"
   13. }
   ```

   该字段的IdentifierCache与MemberMethodCache中保存了方法名混淆前后的映射关系，对应格式为：

   "源码方法名:该方法起始行号:该方法结束行号":"混淆后方法名"。

   第二条堆栈混淆后的方法名为"i"，利用上述字段对该方法名进行还原：

   1. 在上述字段中找出所有混淆后方法名为"i"的条目，可能存在多个，该字段中为：

      ```
      1. "callHarFunction:24:26": "i"
      ```
   2. 找到行号范围包含步骤2中还原后行号的条目，根据步骤2得到还原后的行号为25，包含在24-26之内，因此可以得到源码对应方法名为"callHarFunction"。

   通过上述方式，可以得到源码的方法名。
4. 步骤2与步骤3所得结果进行整合，得到最终堆栈结果如下：

   ```
   1. at har (har/src/main/ets/components/mainpage/MainPage.ets:20:1)
   2. at callHarFunction (entry/src/main/ets/pages/Index.ets:25:3)
   3. at anonymous (entry/src/main/ets/pages/Index.ets:14:47)
   ```

通过上述方式，即可利用编译产物对release应用的crash信息进行解析还原。
