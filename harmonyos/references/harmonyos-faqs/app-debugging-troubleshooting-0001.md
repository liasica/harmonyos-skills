---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/app-debugging-troubleshooting-0001
title: 真机安装HAP包失败故障排查
breadcrumb: FAQ > DevEco Studio > 应用调试 > 故障排查 > 真机安装HAP包失败故障排查
category: harmonyos-faqs
scraped_at: 2026-11-28T10:41:39+08:00
doc_updated_at: 2026-11-27
content_hash: sha256:03558eec4fd11b995fa9d8933e015d931a00779f9dcccb36950f553cbdc11953
---

## HAP包安装报code:9568263 error: install version downgrade错误排查

### 问题现象

在HarmonyOS 开发者中心中配置了真机的udid，并应用了更新后的p7b文件、证书文件进行sign后重新打包，使用hdc命令始终无法安装新HAP包，报9568263错误。其他机器均正常安装。

```txt
[Info]App install path:xxx.hap, queuesize:0, msg:error: failed to install bundle. code:9568263 error: install version downgrade.
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/e4T65k0WRKelsyQZZiJ-BQ/zh-cn_image_0000002797478296.png?HW-CC-KV=V1&HW-CC-Date=20261128T024139Z&HW-CC-Expire=31536000000&HW-CC-Sign=B38E189F0C89060B66738D99164A651F8C603B2CA64F2DEAB83DB16EF26A64CE "点击放大")

### 问题定位

1. 查看日志返回的错误信息code:9568263 error: install version downgrade。正在安装的应用的版本号versionCode小于系统已安装的该应用的版本号。
2. 如何修改应用的版本号versionCode。

   Stage模型修改app.json5中的versionCode字段。

### 分析结论

由报错信息可以看到是待安装应用的版本号小于已安装的同应用的版本号。

### 修改建议

* 桌面直接卸载原版本应用（PC/2in1设备需要确保所有用户下都卸载完成，手机/平板侧需要关注隐私空间和主用户下是否卸载完成），重新执行安装。
  1. 手机界面直接卸载应用。
  2. 重新执行hdc install命令。
* 使用命令卸载工具再重装。
  1. 切换到可执行hdc命令目录下，一般是DevEco Studio工具的SDK目录toolchains中会有hdc.exe的可执行文件。
  2. 先执行hdc shell bm dump -a检查下看是否之前的包还存在，如果存在就执行hdc uninstall <应用bundleName>卸载。
  3. 重新执行hdc install命令。

## HAP包安装报code:9568283 error: install releaseType compatible not same错误排查

### 问题现象

先安装老包，修改build-profile.json5中的API版本后，再安装新包，报错如下：

```txt
Install Failed: error: failed to install bundle.
code:9568283
error: install releaseType compatible not same.
```

### 定位过程

检查修改API版本前后的两个包对应的打包产物的versionCode、apiReleaseType、minAPIVersion、targetAPIVersion的一致性。打包产物查看路径：工程目录build/default/outputs/default/，找到对应.hap包后，打开module.json文件可核对相关字段。

### 分析结论

由于只修改了API版本号，两个版本的versionCode相同，但apiReleaseType、minAPIVersion、targetAPIVersion两个产物中的值不都分别一致，导致报错。

### 修改建议

修改app.json5中的versionCode值，使新包中的值大于老包中的值。

## 多入口ability导致运行报错

### 问题现象

项目配置了多个入口ability，运行项目报错，错误信息如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/8Q44TzgLRou2p7l6vQRegA/zh-cn_image_0000002797142633.png?HW-CC-KV=V1&HW-CC-Date=20261128T024139Z&HW-CC-Expire=31536000000&HW-CC-Sign=FAABAFEE74E813C872DE322934711335559A94527D6C5E79B9BA6CD5F5F3CDB7 "点击放大")

### 定位过程

1. 检查项目中各个模块的module.json5是否配置了skills字段，配置了该字段则表示该模块为入口ability。确认项目的正确入口ability是哪个，一个项目只需要一个主入口即可。
2. 检查IDE运行项目时的命令是否正确，如：hdc shell aa start -a EntryAbility -b com.example.myapplication中的入口模块EntryAbility是否与项目主入口ability相同。

### 分析结论

由于项目配置了多个入口ability，IDE运行项目时的默认入口ability错误，导致项目运行时启动报错。

### 修改建议

* 在运行报错时，把该命令中对应ability的module.json5中的skills字段去掉，不作为入口ability；
* 在运行项目前，编辑运行配置，在Launch Options下手动选择项目的正确入口ability。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/1H2i0hr0SSO5wRPVD7rzGg/zh-cn_image_0000002767982646.png?HW-CC-KV=V1&HW-CC-Date=20261128T024139Z&HW-CC-Expire=31536000000&HW-CC-Sign=33CB7B812EC055E2D122C32D842572F9A7F67C58CF4CBD7DB8E25C24F2CCB80F "点击放大")

## 报9568320错误：缺少签名文件

### 问题现象

运行项目出现如下报错信息。

```txt
Install Failed: error: failed to install bundle.
code:9568320.
error: no signature file.
```

根据错误码[9568320](../harmonyos-guides/bm-tool.md#section9568320-签名文件不存在)提供的处理方案无法解决问题。

### 定位过程

检查工程级build-profile.json5文件中配置是否正确，是否缺少字段。

### 分析结论

工程级build-profile.json5文件的products配置项中缺少signingConfig字段。

### 修改建议

在工程级build-profile.json5文件的products配置项中增加signingConfig字段的配置信息，例如："signingConfig": "default"。

## 修改包名后安装失败

### 问题现象

项目修改包名后安装失败，报错信息如下：

```txt
hvigor ERROR: Failed :entry:default@SignHap...
hvigor ERROR: BundleName in the project configuration does not match that in the SigningConfigs.
Detail: Open the project-level build-profile.json5 file. Change the bundleName value.
to that in the SigningConfigs. Otherwise, go to the app.json5 file and change the bundleName value there.
at /Users/hmn/Desktop/xxx/ztyhm/build-profile.json5.
hvigor ERROR: BUILD FAILED in 18 s 719 ms.
```

### 定位过程

根据报错提示"BundleName in the project configuration does not match that in the SigningConfigs."可知：修改包名后需要同步修改签名信息。

### 分析结论

修改包名后，需要同步修改签名信息。

### 修改建议

在工程级build-profile.json5中把signingConfigs属性值删除，同步信息后重新签名。

## 多设备部署卸载重装报错

### 问题现象

多设备部署时选择卸载重装，实际卸载的设备与预期不一致，且部分设备重新安装时报9568263错误。

### 定位过程

DevEco Studio在部署应用时，检测到设备上已存在相同bundleName的应用包，会执行卸载命令hdc uninstall <包名>。第一个设备上已存在与正在安装应用bundleName相同的应用，因此执行了卸载操作。第二个设备也执行了卸载操作，但已安装应用的VersionCode大于正在安装应用的VersionCode，导致重新安装时报9568263错误。

### 分析结论

多设备部署时，DevEco Studio会对每个检测到相同bundleName应用的设备执行卸载操作。当某设备上已安装应用的VersionCode高于正在安装应用的VersionCode时，卸载后重新安装会报9568263错误。

### 修改建议

* 提前在相关设备上卸载已存在的同bundleName应用（PC/2in1设备需要确保所有用户下都卸载完成，手机/平板侧需要关注隐私空间和主用户下是否卸载完成），保证设备上不存在与正在安装应用bundleName相同的应用，然后进行多设备部署。即使设备上有相同包名的应用，正在安装应用的VersionCode也应高于系统中已安装应用的VersionCode。
* 若需降级安装，对于已安装的证书分发类型为app\_gallery或签名证书类型为debug的三方应用，可使用-d命令实现降级安装：hdc shell bm install -p /data/example.hap -d。
* 多设备运行可参考[多设备运行](../harmonyos-guides/ide-run-debug-configurations.md#section109181222131217)。

## HAP包安装报9568344错误排查

### 问题现象

使用命令行安装HAP和HSP包时，报9568344错误。

### 定位过程

1. 对比IDE安装和命令行安装推送的包，确认推送的HSP包无问题，问题出在命令行安装方式上。
2. bm install -p aaa.hap -s xxx.hsp yyy.hsp命令用于安装应用间HSP，安装应用内共享库应使用bm install -p命令指定包含HAP和HSP的文件夹路径。

### 分析结论

问题根因是使用了错误的命令安装应用内共享库。bm install -p aaa.hap -s xxx.hsp yyy.hsp命令用于安装应用间HSP，安装应用内共享库应使用bm install -p命令指定文件夹路径。

### 修改建议

安装应用内共享库应使用[bm install -p](../harmonyos-guides/bm-tool.md#安装命令install)命令指定包含HAP和HSP的文件夹路径，而不是使用bm install -p aaa.hap -s xxx.hsp yyy.hsp命令（该命令用于安装应用间HSP）。完整命令使用方式如下：

```txt
hdc file send <HAP包路径> "data/local/tmp/test"
hdc file send <HSP包路径> "data/local/tmp/test"
hdc shell bm install -p data/local/tmp/test
```

## 打包后安装失败，错误码：9568320

### 问题现象

打包后的hap包安装失败，构建产物为未签名包，错误码：9568320。

```txt
install Failed: error: failed to install bundle.
code:9568320
error: no signature file.
```

项目本地运行安装时提示安装失败，错误码9568324，签名完整性校验未通过。

```txt
error: signature verification failed due to out of integrity.
code:9568324
```

### 定位过程

根据报错信息可知，是签名文件或签名信息异常导致。可根据以下场景进行排查：

* 场景一：检查工程级build-profile.json5文件中是否配置signingConfigs签名配置，并且products中指定了对应的signingConfig。
* 场景二：DevEco Studio缓存异常可能导致签名失效，尝试清理缓存后重启是否正常。
* 场景三：排查证书是否使用正确。
* 场景四：检查工程级build-profile.json5文件中[packOptions](../harmonyos-guides/ide-hvigor-build-profile-app.md#section03812484215)的appWithSignedPkg属性是否配置为true，该属性默认为false，此时APP包中的HAP/HSP为未签名包。
* 场景五：根据错误码9568324可知，HAP包签名完整性校验未通过，可能原因为HAP包签名不正确。
* 场景六：修改应用bundleName后未重新生成签名材料，原先自动签名绑定了旧bundleName，导致构建产出未签名包。

### 分析结论

* 场景一：工程级build-profile.json5文件配置错误，例如：产品未配置signingConfig。
* 场景二：DevEco Studio缓存异常导致签名失效。
* 场景三：证书使用错误。
* 场景四：工程级build-profile.json5文件中未配置packOptions的appWithSignedPkg属性为true，导致APP包中的HAP/HSP没有签名。
* 场景五：HAP包签名不正确，导致签名完整性校验未通过。
* 场景六：修改bundleName后未重新触发自动签名，原签名材料与新bundleName不匹配，导致构建产物为未签名包。

### 修改建议

* 场景一：工程级build-profile.json5文件配置准确，保证products中指定了对应的signingConfig。
* 场景二：
  1. 执行菜单栏操作：Build -> Clean Project -> File -> Invalidate Caches，然后重启DevEco Studio。
  2. 删除本地签名目录（路径在签名页面可见），重新运行自动签名。
* 场景三：保证证书类型使用正确，调试包使用调试证书，正式发布包使用发布证书，发布证书需要在HarmonyOS 开发者中心创建获取。
* 场景四：在工程级build-profile.json5文件中配置[packOptions](../harmonyos-guides/ide-hvigor-build-profile-app.md#section03812484215)的appWithSignedPkg属性为true，保证APP包中的HAP/HSP有签名。
* 场景五：方法一：使用[自动签名](../doccenter-deveco-studio/ide-signing-auto.md)，在连接设备后，重新为应用进行签名。方法二：使用[手动签名](../doccenter-deveco-studio/ide-signing-manual.md)，参考手动签名配置流程。
* 场景六：
  1. 在DevEco Studio中打开File -> Project Structure -> Signing Configs，先取消勾选Automatically generate signature，点击OK；再次进入Signing Configs，重新勾选Automatically generate signature，点击OK保存。
  2. 检查工程级build-profile.json5配置，确认products下的signingConfig字段值与signingConfigs中定义的签名配置name一致且不为空，参考结构如下：

     ```json
       {
         "app": {
           "signingConfigs": [
             {
               "name": "default",
               "type": "HarmonyOS",
               "material": {
                 "certpath": "...",
                 "storePassword": "..."
               }
             }
           ],
           "products": [
             {
               "name": "default",
               "signingConfig": "default"
             }
           ]
         }
       }
     ```

     若signingConfig值为空、缺失，或仍指向旧签名配置名，需同步改为当前生效的签名配置name。
  3. 重新构建并运行应用。

## HAP包安装报code:9568389 error: unknown错误排查

### 问题现象

通过[hdc](../harmonyos-guides/hdc.md)执行[bm install](../harmonyos-guides/bm-tool.md)命令安装HAP包时，安装失败，报错信息如下：

```screen
Install Failed: error: failed to install bundle.
code:9568389
error: unknown.
```

### 定位过程

1. 分析安装链路日志，签名校验、MDM/EDM管控、AccessToken初始化、安装目录创建、so解包等步骤均成功，失败点位于installd调用MoveHapToCodeDir -> MoveFile（rename系统调用）将HAP从安装暂存目录移动到应用安装目录时，rename返回errno:18。
2. errno:18为POSIX标准错误码EXDEV（Invalid cross-device link），表示源路径与目的路径不在同一文件系统，rename无法跨文件系统执行；移动失败后安装整体回滚，bm工具错误码表中无9568389的映射，最终显示error: unknown。
3. 安装暂存文件从收流目录拷贝至安装暂存目录（拷贝方式，可跨文件系统）成功，从安装暂存目录移动至应用安装目录（rename方式，不可跨文件系统）失败，失败边界锁定在安装暂存目录（/data/service/el1/public/bms/bundle\_manager\_service/security\_stream\_install）与应用安装目录（/data/app/el1/bundle/public）之间。
4. 系统浏览器更新扩展资源的另一条独立代码路径在同样的目录间执行rename也报errno:18，证明该问题是设备文件系统布局层面的系统性问题，与具体应用无关。

### 分析结论

设备上hdc安装暂存目录与应用安装目录不在同一文件系统，installd在安装落盘阶段调用rename移动HAP时报errno:18（EXDEV），移动失败导致安装整体回滚，最终向用户报code:9568389。

### 修改建议

1. 确认跨文件系统。在设备上执行以下命令，输出中两个%d（设备ID）不同即确认两个目录不在同一文件系统，%m显示各自所属的挂载点：

   ```txt
   hdc shell "stat -c '%d %m' /data/service/el1/public/bms/bundle_manager_service /data/app/el1/bundle/public"
   ```
2. 找出挂载边界。执行以下命令，从输出确认被单独挂载的边界目录（如security\_stream\_install、bundle\_manager\_service或/data/app/el1/bundle）及其文件系统类型（tmpfs/独立分区/overlay），再到ROM源码中全量搜索该挂载路径（fstab、init\*.cfg、挂载脚本、param参数文件），确认该挂载是否为定制时自行添加：

   ```txt
   hdc shell "cat /proc/mounts | grep -E '/data/app|/data/service'"
   ```
3. 按挂载来源选择修复方式：
   * 挂载为定制添加且可去掉：删除该挂载，让暂存目录和安装目录回到/data同一文件系统。
   * 挂载必须保留：修改配置，把hdc安装暂存路径改到与/data/app同一文件系统的目录。
   * 挂载无法修改（基线自带）：修改installd代码（installd\_operator.cpp的MoveFile、installd\_host\_impl.cpp的MoveHapToCodeDir），rename报EXDEV时降级为“拷贝+fsync+删源文件”，注意评估代码签名（codesign）对拷贝的兼容性。
